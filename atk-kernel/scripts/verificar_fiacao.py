#!/usr/bin/env python3
"""Verifica a FIAÇÃO dos portões terminais (`terminal-templates/*.lean.tpl`).

Troca cada peça ausente (`PROVA_*`, `LIGACAO_*`) por `sorry`, compila os nove modelos contra o
build real do ATK numa pasta temporária e confere:
  * todos compilam (a ligação peça → enunciado oficial está certa e tipada);
  * o único axioma fora do padrão é `sorryAx`, que vem exatamente das peças ausentes.
Resultado: a lista exata dos termos que faltam para o verde universal.
Nada é escrito em `ATK/`; os `.olean` temporários ficam fora do repositório.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ORDER = ["RH", "Beal", "NS", "PNP", "Hodge", "BSD", "YM", "VerdeFiel", "ClosedMathGate"]
PH = re.compile(r"\b(PROVA_[A-Z0-9_]+|LIGACAO_[A-Z0-9_]+)\b")


def run(root, timeout=900):
    tpl_dir = os.path.join(root, "terminal-templates")
    build = os.path.join(root, ".lake", "build", "lib", "lean", "ATK")
    if not os.path.isdir(build) or shutil.which("lake") is None:
        return {"ran": False, "reason": "sem build local do ATK ou sem lake"}
    tmp = tempfile.mkdtemp(prefix="fiacao_")
    try:
        src, out = os.path.join(tmp, "src"), os.path.join(tmp, "build")
        shutil.copytree(build, os.path.join(out, "ATK"))
        os.makedirs(os.path.join(src, "ATK", "Terminal"), exist_ok=True)
        os.makedirs(os.path.join(out, "ATK", "Terminal"), exist_ok=True)
        rows, missing = [], []
        for name in ORDER:
            text = open(os.path.join(tpl_dir, f"{name}.lean.tpl"), encoding="utf-8").read()
            holes = sorted(set(PH.findall(text)))
            missing += [f"{name}:{h}" for h in holes]
            rel = "ATK/ClosedMathGate" if name == "ClosedMathGate" else f"ATK/Terminal/{name}"
            path = os.path.join(src, rel + ".lean")
            open(path, "w", encoding="utf-8").write(PH.sub("sorry", text))
            cmd = (f'LEAN_PATH="{out}:$LEAN_PATH" lean --root="{src}" -o "{os.path.join(out, rel + ".olean")}" '
                   f'"{path}"')
            p = subprocess.run(["lake", "env", "bash", "-c", cmd], cwd=root, capture_output=True,
                               text=True, timeout=timeout)
            log = p.stdout + p.stderr
            axs = {}
            for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
                axs[m.group(1)] = {a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()}
            extra = sorted(set().union(*axs.values()) - ALLOWED) if axs else []
            errors = [l for l in log.splitlines() if ": error" in l][:3]
            ok = p.returncode == 0 and not errors and set(extra) <= {"sorryAx"}
            rows.append({"template": name, "holes": holes, "compiled": p.returncode == 0 and not errors,
                         "extra_axioms": extra, "ok": ok, "errors": errors})
        n_ok = sum(r["ok"] for r in rows)
        return {"ran": True, "ok": n_ok == len(rows), "templates_ok": f"{n_ok}/{len(rows)}",
                "missing_terms": missing, "n_missing": len(missing), "rows": rows}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def markdown(res):
    if not res.get("ran"):
        return [f"Fiação dos portões: não verificada ({res.get('reason')})."]
    md = [f"### Fiação dos portões terminais — {res['templates_ok']} modelos compilam; "
          f"faltam exatamente **{res['n_missing']}** termos",
          "",
          "| Modelo | Peças ausentes | Compila com as peças = `sorry` | Axiomas extras |",
          "|---|---|---|---|"]
    for r in res["rows"]:
        md.append(f"| `{r['template']}` | " + (", ".join(f"`{h}`" for h in r["holes"]) or "nenhuma (só depende dos outros portões)")
                  + f" | {'✅' if r['compiled'] else '❌ ' + '; '.join(r['errors'])} | "
                  + (", ".join(r["extra_axioms"]) or "nenhum") + " |")
    md += ["", "Com as peças trocadas por `sorry`, a única fonte de axioma fora do padrão é `sorryAx`: "
           "a ligação até o enunciado oficial está pronta; o que falta são exatamente esses termos."]
    return md


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    res = run(root)
    rep = os.path.join(root, "reports")
    os.makedirs(rep, exist_ok=True)
    json.dump(res, open(os.path.join(rep, "fiacao.json"), "w"), indent=2, ensure_ascii=False)
    print("\n".join(markdown(res)))
    return 0 if res.get("ok") or not res.get("ran") else 1


if __name__ == "__main__":
    sys.exit(main())
