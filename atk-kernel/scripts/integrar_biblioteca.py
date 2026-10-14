#!/usr/bin/env python3
"""Integra uma biblioteca Lean externa (p.ex. o pacote ATK-T1) ao atk-kernel, sob auditoria.

Uso:
  python3 scripts/integrar_biblioteca.py PACOTE.zip PREFIXO [--aplicar] [--compilar]

* Sem `--aplicar`: só inspeciona e mostra o que faria (nada é escrito).
* Com `--aplicar`: copia os `.lean` para `ATK/<PREFIXO>/`, reescreve os `import` internos para
  `ATK.<PREFIXO>.…`, acrescenta `#print axioms` a cada teorema, registra os módulos em `ATK.lean` e os
  teoremas em `scripts/expected_theorems.txt`. A partir daí o CI audita a biblioteca como o resto.
* Com `--compilar`: compila cada módulo localmente e mostra os axiomas.

Recusa se houver `sorry`/`admit`/`axiom` nas fontes, se o pacote declarar outra versão do Lean, ou se
algum nome de teorema tiver apóstrofo (o auditor não o lê). Os namespaces originais são preservados.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile


def theorems_with_ns(text):
    ns, out = [], []
    for line in text.split("\n"):
        m = re.match(r"^namespace (\S+)", line)
        if m:
            ns.append(m.group(1))
            continue
        m = re.match(r"^end (\S+)", line)
        if m and ns and ns[-1] == m.group(1):
            ns.pop()
            continue
        m = re.match(r"^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?theorem\s+(\S+)", line)
        if m:
            out.append(".".join(ns + [m.group(1)]))
    return out


def flags(text):
    code = re.sub(r"/-.*?-/", "", text, flags=re.S)
    code = re.sub(r"--.*", "", code)
    f = [w for w in ("sorry", "admit") if re.search(rf"\b{w}\b", code)]
    if re.search(r"^\s*axiom\s", code, re.M):
        f.append("axiom")
    return f


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    zpath, prefix = argv[1], argv[2]
    apply, compile_ = "--aplicar" in argv, "--compilar" in argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ours = open(os.path.join(root, "lean-toolchain")).read().strip()
    tmp = tempfile.mkdtemp(prefix="integrar_")
    try:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
        leans = []
        for d, _, fs in os.walk(tmp):
            leans += [os.path.join(d, f) for f in fs if f.endswith(".lean") and f not in ("lakefile.lean",)]
        if not leans:
            print("RECUSADO — nenhum arquivo .lean no pacote.")
            return 2
        tcs = []
        for d, _, fs in os.walk(tmp):
            if "lean-toolchain" in fs:
                tcs.append(open(os.path.join(d, "lean-toolchain")).read().strip())
        base = None
        for d, _, fs in os.walk(tmp):
            if any(f.startswith("lakefile") for f in fs):
                base = d
                break
        if base is None:
            base = os.path.commonpath([os.path.dirname(f) for f in leans])
            if len(leans) == 1 or all(os.path.dirname(f) == base for f in leans):
                pass
        rels = sorted(os.path.relpath(f, base) for f in leans)
        roots = sorted({r.split(os.sep)[0].replace(".lean", "") for r in rels})
        problems = []
        if tcs and any(t != ours for t in tcs):
            problems.append(f"toolchain do pacote {sorted(set(tcs))} ≠ {ours}")
        plan, thms = [], []
        for r in rels:
            text = open(os.path.join(base, r), encoding="utf-8").read()
            fl = flags(text)
            if fl:
                problems.append(f"{r}: {', '.join(fl)}")
            ts = theorems_with_ns(text)
            bad = [t for t in ts if "'" in t]
            if bad:
                problems.append(f"{r}: nomes com apóstrofo {bad[:3]}")
            new = text
            for rt in roots:
                new = re.sub(rf"^import {re.escape(rt)}(\.|\s*$)", rf"import ATK.{prefix}.{rt}\1", new, flags=re.M)
            mod = "ATK." + prefix + "." + r[:-len(".lean")].replace(os.sep, ".")
            plan.append((r, mod, new, ts))
            thms += ts
        print(f"Pacote: {len(rels)} módulos, {len(thms)} teoremas, raízes {roots}, toolchain {tcs or ['(não declarado)']}.")
        for r, mod, _, ts in plan:
            print(f"  {r} → {mod} ({len(ts)} teoremas)")
        if problems:
            print("RECUSADO — " + "; ".join(problems) + ". Nada integrado.")
            return 3
        if not apply:
            print("Inspeção ok. Rode de novo com --aplicar para integrar.")
            return 0
        added = []
        for r, mod, new, ts in plan:
            dest = os.path.join(root, "ATK", prefix, r)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            body = re.sub(r"\n#print axioms .*", "", new).rstrip("\n")
            body += "\n\n" + "".join(f"#print axioms {t}\n" for t in ts) if ts else "\n"
            open(dest, "w", encoding="utf-8").write(body)
            added.append(mod)
        atk = os.path.join(root, "ATK.lean")
        cur = open(atk, encoding="utf-8").read()
        with open(atk, "a", encoding="utf-8") as fh:
            for mod in added:
                if f"import {mod}\n" not in cur:
                    fh.write(f"import {mod}\n")
        exp = os.path.join(root, "scripts", "expected_theorems.txt")
        have = set(l.strip() for l in open(exp, encoding="utf-8"))
        with open(exp, "a", encoding="utf-8") as fh:
            for t in thms:
                if t not in have:
                    fh.write(t + "\n")
        print(f"INTEGRADO — {len(added)} módulos em ATK/{prefix}/, {len(thms)} teoremas registrados.")
        if compile_:
            for r, mod, _, _ in plan:
                rel = os.path.join("ATK", prefix, r)
                out = os.path.join(root, ".lake", "build", "lib", "lean", rel[:-len(".lean")] + ".olean")
                os.makedirs(os.path.dirname(out), exist_ok=True)
                p = subprocess.run(["lake", "env", "lean", "-o", out, rel], cwd=root, capture_output=True, text=True)
                log = p.stdout + p.stderr
                ax = re.findall(r"depends on axioms: \[([^\]]*)\]", log)
                print(f"  {rel}: {'compila' if p.returncode == 0 else 'ERRO'}; axiomas extras: "
                      f"{sorted({a.strip() for s in ax for a in s.split(',')} - {'propext', 'Classical.choice', 'Quot.sound'}) or 'nenhum'}")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
