#!/usr/bin/env python3
"""Congela a biblioteca certificada (etapa T2 do plano do verde universal).

Gera `audits/`:
  * provenance.json — SHA-256 das fontes (mesmo algoritmo do `check_axioms.py`), SHA-256 por arquivo,
    toolchain do Lean, revisão da Mathlib, commit, contagem de teoremas esperados;
  * axioms.txt      — `#print axioms` de cada teorema esperado, compilando localmente (`--axiomas`);
                      módulos que não compilam aqui ficam marcados "VER CI" (o CI é a autoridade);
  * ci_attestation  — (opcional, `--ci RUN RESULTADO SHA`) o resultado do CI para estas mesmas fontes.

O CI compara `provenance.json` com as fontes atuais: se mudaram, T2 fica DESATUALIZADO até
rodar `python3 scripts/congelar.py` de novo. `audits/` não entra no SHA das fontes (sem circularidade).
"""
import glob
import hashlib
import json
import os
import re
import subprocess
import sys


def sources_sha(root):
    sha = hashlib.sha256()
    files = sorted(glob.glob(os.path.join(root, "ATK", "**", "*.lean"), recursive=True)) + [os.path.join(root, "ATK.lean")]
    per = {}
    for f in files:
        data = open(f, "rb").read()
        sha.update(data)
        per[os.path.relpath(f, root)] = hashlib.sha256(data).hexdigest()
    return sha.hexdigest(), per


def mathlib_rev(root):
    p = os.path.join(root, "lake-manifest.json")
    if not os.path.exists(p):
        return None
    for pkg in json.load(open(p)).get("packages", []):
        if pkg.get("name") == "mathlib":
            return pkg.get("rev")
    return None


def git_commit(root):
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True).stdout.strip() or None
    except Exception:
        return None


def provenance(root):
    src, per = sources_sha(root)
    expected = [l.strip() for l in open(os.path.join(root, "scripts", "expected_theorems.txt")) if l.strip()]
    return {
        "schema": "atk-kernel.freeze.v1",
        "sources_sha256": src,
        "files": per,
        "n_files": len(per),
        "expected_theorems": len(expected),
        "lean_toolchain": open(os.path.join(root, "lean-toolchain")).read().strip(),
        "mathlib_rev": mathlib_rev(root),
        "commit_at_freeze": git_commit(root),
        "authority": "O certificado é o CI (check-run 'Lean 4 + Mathlib — compilação e auditoria de axiomas'), "
                     "que recompila tudo e imprime o mesmo sources_sha256.",
    }


FALLBACK = ("import Mathlib.Analysis.SpecialFunctions.Pow.Real\n"
            "import Mathlib.Analysis.SpecialFunctions.Log.Basic\n"
            "import Mathlib.LinearAlgebra.Matrix.NonsingularInverse\n")


def axioms_local(root, timeout=1200):
    """Compila cada módulo com `lake env lean` e lê `#print axioms`."""
    out = {}
    files = sorted(glob.glob(os.path.join(root, "ATK", "**", "*.lean"), recursive=True))
    for f in files:
        rel = os.path.relpath(f, root)
        try:
            p = subprocess.run(["lake", "env", "lean", rel], cwd=root, capture_output=True, text=True, timeout=timeout)
            log = p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            log = ""
        suffix = ""
        if "Mathlib.olean" in log and "does not exist" in log:
            # este ambiente não tem a Mathlib inteira compilada: tenta com importações reduzidas
            tmpdir = os.path.join(root, ".tmp_congelar")
            os.makedirs(tmpdir, exist_ok=True)
            src = open(f, encoding="utf-8").read().replace("import Mathlib\n", FALLBACK, 1)
            tmpf = os.path.join(tmpdir, rel.replace("/", "_"))
            open(tmpf, "w", encoding="utf-8").write(src)
            try:
                p = subprocess.run(["lake", "env", "lean", os.path.relpath(tmpf, root)], cwd=root,
                                   capture_output=True, text=True, timeout=timeout)
                log = p.stdout + p.stderr
                suffix = " (local, importações reduzidas)"
                if p.returncode != 0 or ": error" in log:
                    log = ""  # com importações reduzidas não compilou: fica "VER CI" (não registra sorryAx de recuperação)
            except subprocess.TimeoutExpired:
                log = ""
            os.remove(tmpf)
        for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
            out[m.group(1)] = ", ".join(a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()) + suffix
        for m in re.finditer(r"'([^']+)' does not depend on any axioms", log):
            out[m.group(1)] = "nenhum"
        print(f"{rel}: {'ok' if p.returncode == 0 else 'não compila aqui'}", file=sys.stderr, flush=True)
    return out


def main(argv):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    aud = os.path.join(root, "audits")
    os.makedirs(aud, exist_ok=True)
    prov = provenance(root)
    json.dump(prov, open(os.path.join(aud, "provenance.json"), "w"), indent=2, ensure_ascii=False)
    print(f"provenance.json: {prov['n_files']} arquivos · sources_sha256 {prov['sources_sha256']}")
    if "--axiomas" in argv:
        ax = axioms_local(root)
        expected = [l.strip() for l in open(os.path.join(root, "scripts", "expected_theorems.txt")) if l.strip()]
        lines = [f"# axiomas por teorema — congelamento de {prov['sources_sha256']}",
                 "# padrão permitido: propext, Classical.choice, Quot.sound; 'VER CI' = não compilou neste ambiente"]
        local_ok = 0
        for t in expected:
            a = ax.get(t)
            if a is not None:
                local_ok += 1
            lines.append(f"{t}\t{a if a is not None else 'VER CI'}")
        open(os.path.join(aud, "axioms.txt"), "w").write("\n".join(lines) + "\n")
        bad = [t for t in expected if ax.get(t) not in (None,) and any(
            x.strip() not in ("propext", "Classical.choice", "Quot.sound", "nenhum") for x in ax[t].split(" (")[0].split(","))]
        print(f"axioms.txt: {local_ok}/{len(expected)} verificados localmente; fora do padrão: {len(bad)}")
    if "--ci" in argv:
        # atestação do CI para estas mesmas fontes: --ci <check_run_id> <resultado> <sha impresso pelo CI>
        i = argv.index("--ci")
        run_id, result, ci_sha = argv[i + 1], argv[i + 2], argv[i + 3]
        prov["ci_attestation"] = {"check_run": run_id, "result": result, "sources_sha256": ci_sha,
                                  "matches_freeze": ci_sha == prov["sources_sha256"]}
        json.dump(prov, open(os.path.join(aud, "provenance.json"), "w"), indent=2, ensure_ascii=False)
        print(f"atestação do CI {run_id}: {result}; SHA {'confere' if ci_sha == prov['sources_sha256'] else 'NÃO confere'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
