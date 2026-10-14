#!/usr/bin/env python3
"""Instala um portão terminal — só se ele for uma prova genuína.

Uso: python3 scripts/instalar_portao.py LINHA
LINHA ∈ RH, Beal, NS, PNP, Hodge, BSD, YM (prova), <Linha>Refutacao (refutação), <Linha>Modelo (ligação),
        VerdeFiel, ClosedMathGate

Recusa (sem tocar em nada) se:
  * o arquivo do portão não existe (mostra o modelo e as peças que faltam);
  * restam peças `PROVA_*`/`LIGACAO_*`, ou há `sorry`/`admit`/`axiom` na fonte;
  * não compila, ou `#print axioms` sai do padrão {propext, Classical.choice, Quot.sound};
  * o tipo elaborado não é o enunciado oficial (`example : _root_.<enunciado> := <teorema>`).
Se tudo passa: acrescenta o `import` em `ATK.lean` e os teoremas em `scripts/expected_theorems.txt`;
o CI recalcula `UNIVERSAL_GREEN` e `FINAL_ROOT`.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import universal_green as ug  # noqa: E402

PH = re.compile(r"\b(PROVA_[A-Z0-9_]+|LIGACAO_[A-Z0-9_]+)\b")


def entry(gates, line):
    if line == "VerdeFiel":
        return gates["universal_green_fiel"]
    if line == "ClosedMathGate":
        return gates["final_root"]
    for ln in gates["lines"]:
        if ln["id"] == line:
            return ln
        if line == ln["id"] + "Refutacao":
            return {"gate_file": ln["refutation_gate_file"], "gate_theorem": ln["refutation_gate_theorem"],
                    "statement_root": ln["refutation_statement_root"], "template": ln["refutation_template"]}
        if line == ln["id"] + "Modelo" and ln.get("linking_module"):
            return {"gate_file": ln["linking_module"], "gate_theorem": None, "statement_root": None,
                    "template": ln["linking_template"]}
    return None


def main(argv):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if len(argv) != 2:
        print(__doc__)
        return 1
    line = argv[1]
    gates = json.load(open(os.path.join(root, "scripts", "terminal_gates.json"), encoding="utf-8"))
    e = entry(gates, line)
    if e is None:
        print(f"linha desconhecida: {line}")
        return 1
    gfile, gthm = e["gate_file"], e["gate_theorem"]
    path = os.path.join(root, gfile)
    tpl = os.path.join(root, e.get("template", ""))
    if not os.path.exists(path):
        holes = sorted(set(PH.findall(open(tpl, encoding="utf-8").read()))) if os.path.exists(tpl) else []
        print(f"RECUSADO — {gfile} não existe. Nada instalado.")
        print(f"Modelo: {e.get('template')}. Peças que faltam: {', '.join(holes) or 'só os outros portões'}.")
        return 2
    src = open(path, encoding="utf-8").read()
    holes = sorted(set(PH.findall(src)))
    flags = ug._flags(path)
    if holes or flags:
        print(f"RECUSADO — {gfile} ainda tem " + ", ".join(holes + flags) + ". Nada instalado.")
        return 3
    mod = gfile[:-len(".lean")].replace("/", ".")
    out = os.path.join(root, ".lake", "build", "lib", "lean", gfile[:-len(".lean")] + ".olean")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    p = subprocess.run(["lake", "env", "lean", "-o", out, gfile], cwd=root, capture_output=True, text=True)
    log = p.stdout + p.stderr
    axioms = {}
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
        axioms[m.group(1)] = [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", log):
        axioms[m.group(1)] = []
    if p.returncode != 0 or ": error" in log:
        print(f"RECUSADO — {gfile} não compila. Nada instalado.\n" + "\n".join(log.splitlines()[:10]))
        return 4
    if gthm is not None:  # módulos de ligação (…Modelo) não têm teorema terminal
        if gthm not in axioms or not set(axioms[gthm]) <= ug.ALLOWED:
            print(f"RECUSADO — axiomas de {gthm}: {axioms.get(gthm)}. Nada instalado.")
            return 4
        ok, why = ug.typecheck(root, gfile, gthm, e["statement_root"], ug.default_runner(root))
        if not ok:
            print(f"RECUSADO — {why}. Nada instalado.")
            return 5
    atk = os.path.join(root, "ATK.lean")
    if f"import {mod}\n" not in open(atk, encoding="utf-8").read():
        open(atk, "a", encoding="utf-8").write(f"import {mod}\n")
    exp = os.path.join(root, "scripts", "expected_theorems.txt")
    have = set(l.strip() for l in open(exp, encoding="utf-8"))
    new = [n for n in re.findall(r"^#print axioms (\S+)", src, re.M) if n not in have]
    if new:
        open(exp, "a", encoding="utf-8").write("".join(n + "\n" for n in new))
    if gthm is None:
        print(f"INSTALADO — módulo de ligação {mod}. A ligação só conta como fechada depois da revisão "
              "humana (status CLOSED em scripts/obligations.json).")
    else:
        print(f"INSTALADO — {gthm} : {e['statement_root']} (axiomas {axioms[gthm]}). "
              "O CI recalcula UNIVERSAL_GREEN e FINAL_ROOT.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
