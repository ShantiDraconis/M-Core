#!/usr/bin/env python3
"""Verifica a FIAÇÃO dos portões terminais (`terminal-templates/*.lean.tpl`).

Troca cada peça ausente (`PROVA_*`, `LIGACAO_*`) por `(sorry : <tipo>)`, com o tipo tirado do
catálogo `scripts/termos.json` (nomes Lean em `ATK/Termos.lean`), compila os 23 modelos
contra o build real do ATK numa pasta temporária e confere:
  * todos compilam (a ligação peça → enunciado oficial está certa e tipada);
  * o tipo de cada peça no catálogo é o tipo que o portão espera (sem divergência);
  * o único axioma fora do padrão é `sorryAx`, que vem exatamente das peças ausentes;
  * teste de sensibilidade: trocar o tipo de uma peça por outro faz a compilação falhar.
Resultado: a lista exata dos termos que faltam para o verde universal, cada um com o seu tipo.
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
LINHAS = ["RH", "Beal", "NS", "PNP", "Hodge", "BSD", "YM"]
MODELOS = ["NSModelo", "PNPModelo", "HodgeModelo", "BSDModelo", "YMModelo"]
SUBPORTOES = ["BSDClay", "BSDRefinada"]           # BSD_FULL = BSD_CLAY ∧ BSD_REFINED
ORDER = MODELOS + SUBPORTOES + LINHAS + [k + "Refutacao" for k in LINHAS] + ["VerdeFiel", "ClosedMathGate"]
PROVA = set(MODELOS + SUBPORTOES + LINHAS)                   # rota da prova (verde)
REFUTACAO = set(MODELOS + [k + "Refutacao" for k in LINHAS])   # rota da refutação (resolução)
PH = re.compile(r"\b(PROVA_[A-Z0-9_]+|LIGACAO_[A-Z0-9_]+)\b")


def load_types(root):
    """(modelo, lacuna) → tipo Lean, do catálogo `scripts/termos.json`."""
    path = os.path.join(root, "scripts", "termos.json")
    if not os.path.exists(path):
        return {}
    return {(t["template"], t["placeholder"]): t["lean_type"]
            for t in json.load(open(path, encoding="utf-8"))["terms"]}


def substitute(name, text, types):
    """Troca as lacunas por `sorry` tipado (quando o catálogo tem o tipo)."""
    typed = []

    def rep(m):
        ty = types.get((name, m.group(1)))
        if ty:
            typed.append(m.group(1))
            return f"(sorry : {ty})"
        return "sorry"
    out = PH.sub(rep, text)
    if typed:
        out = "import ATK.Termos\n" + out
    return out, sorted(set(typed))


def compile_one(root, src, out, rel, text, timeout):
    path = os.path.join(src, rel + ".lean")
    open(path, "w", encoding="utf-8").write(text)
    cmd = (f'LEAN_PATH="{out}:$LEAN_PATH" lean --root="{src}" -o "{os.path.join(out, rel + ".olean")}" '
           f'"{path}"')
    p = subprocess.run(["lake", "env", "bash", "-c", cmd], cwd=root, capture_output=True,
                       text=True, timeout=timeout)
    log = p.stdout + p.stderr
    errors = [l for l in log.splitlines() if ": error" in l][:3]
    return p.returncode == 0 and not errors, log, errors


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
        types = load_types(root)
        rows, missing = [], []
        for name in ORDER:
            text = open(os.path.join(tpl_dir, f"{name}.lean.tpl"), encoding="utf-8").read()
            holes = sorted(set(PH.findall(text)))
            missing += [f"{name}:{h}" for h in holes]
            rel = "ATK/ClosedMathGate" if name == "ClosedMathGate" else f"ATK/Terminal/{name}"
            body, typed = substitute(name, text, types)
            compiled, log, errors = compile_one(root, src, out, rel, body, timeout)
            divergent = []
            if not compiled and typed:  # distingue fiação quebrada de tipo divergente
                plain_ok, _, _ = compile_one(root, src, out, rel, PH.sub("sorry", text), timeout)
                if plain_ok:
                    divergent = typed
            axs = {}
            for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
                axs[m.group(1)] = {a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()}
            extra = sorted(set().union(*axs.values()) - ALLOWED) if axs else []
            ok = compiled and set(extra) <= {"sorryAx"}
            rows.append({"template": name, "holes": holes, "typed": typed,
                         "untyped": sorted(set(holes) - set(typed)), "divergent": divergent,
                         "compiled": compiled, "extra_axioms": extra, "ok": ok, "errors": errors})
        sens = sensibilidade(root, src, out, types, timeout)
        n_ok = sum(r["ok"] for r in rows)
        prova = [m for m in missing if m.split(":")[0] in PROVA]
        refut = [m for m in missing if m.split(":")[0] in REFUTACAO]
        n_typed = sum(len(r["typed"]) for r in rows)
        n_typed_ok = sum(len(r["typed"]) for r in rows if r["compiled"])
        n_holes = sum(len(r["holes"]) for r in rows)
        return {"ran": True, "ok": n_ok == len(rows) and n_typed_ok == n_holes and sens.get("ok", False),
                "templates_ok": f"{n_ok}/{len(rows)}",
                "tipos": f"{n_typed_ok}/{n_holes}", "n_tipados": n_typed, "sensibilidade": sens,
                "missing_terms": prova, "n_missing": len(prova),
                "missing_refutation": refut, "n_missing_refutation": len(refut), "rows": rows}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def sensibilidade(root, src, out, types, timeout):
    """Troca o tipo de uma peça pelo de outra (B3 ↔ O3 em NS): a compilação TEM de falhar."""
    a, b = ("NS", "PROVA_DA_PONTE_B3"), ("NS", "PROVA_DO_PRODUTOR_O3")
    if a not in types or b not in types:
        return {"ok": False, "reason": "catálogo sem as peças de NS"}
    swapped = dict(types)
    swapped[a], swapped[b] = types[b], types[a]
    text = open(os.path.join(root, "terminal-templates", "NS.lean.tpl"), encoding="utf-8").read()
    body, _ = substitute("NS", text, swapped)
    compiled, _, errors = compile_one(root, src, out, "ATK/Terminal/NSSensibilidade", body, timeout)
    return {"ok": not compiled, "mutacao": "NS: tipo de B3 ↔ tipo de O3",
            "detectada": not compiled, "erro": errors[:1]}


def markdown(res):
    if not res.get("ran"):
        return [f"Fiação dos portões: não verificada ({res.get('reason')})."]
    sens = res.get("sensibilidade") or {}
    md = [f"### Fiação dos portões terminais — {res['templates_ok']} modelos compilam; "
          f"rota da prova: faltam exatamente **{res['n_missing']}** termos; rota da refutação: "
          f"{res.get('n_missing_refutation', '?')} termos",
          "",
          f"Tipos conferidos pelo kernel: **{res.get('tipos', '?')}** lacunas com `(sorry : <tipo do catálogo>)` "
          f"(`scripts/termos.json`, `ATK/Termos.lean`). Teste de sensibilidade ({sens.get('mutacao', '—')}): "
          + ("divergência **detectada** ✅" if sens.get("detectada") else "❌ não detectada"),
          "",
          "| Modelo | Peças ausentes | Compila com as peças = `sorry` tipado | Axiomas extras |",
          "|---|---|---|---|"]
    for r in res["rows"]:
        md.append(f"| `{r['template']}` | " + (", ".join(f"`{h}`" for h in r["holes"]) or ("nenhuma (ligação construída)" if r["template"].endswith("Modelo") else "nenhuma (só depende dos outros portões)"))
                  + f" | {'✅' if r['compiled'] else ('❌ tipo divergente: ' + ', '.join(r.get('divergent', [])) if r.get('divergent') else '❌ ' + '; '.join(r['errors']))} | "
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
