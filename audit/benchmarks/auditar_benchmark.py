#!/usr/bin/env python3
"""Roda o `Auditor.lean` sobre um benchmark Lean já compilado e grava o relatório.

Uso (no diretório do projeto do benchmark, com o `Auditor` já compilado):
  python3 auditar_benchmark.py --nome miniF2F-test --raiz MiniF2F/Test --lean "lake env lean" --saida resultados/

- `--raiz` é a pasta dos módulos auditados (um teorema por arquivo ou vários por arquivo);
- módulos sem `.olean` (não compilaram) entram como `nao_elabora`;
- o auditor roda em lotes de `--lote` módulos; se um lote derruba o processo, os módulos dele rodam um a um.
"""
import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from collections import Counter

CERTIFICADAS = ("hipoteses_contraditorias", "conclusao_vazia", "falso", "axioma_extra")


def modulos(raiz):
    out = []
    for dp, _, fns in os.walk(raiz):
        for fn in sorted(fns):
            if fn.endswith(".lean"):
                out.append(os.path.join(dp, fn)[:-5].replace(os.sep, "."))
    return sorted(out)


def compilado(mod, build):
    return os.path.exists(os.path.join(build, *mod.split(".")) + ".olean")


def roda(mods, lean, tmp, prefixo):
    f = os.path.join(tmp, "Rodar.lean")
    with open(f, "w") as h:
        h.write("import Auditor\n" + "".join(f"import {m}\n" for m in mods) + f"\n#auditar_prefixo {prefixo}\n")
    r = subprocess.run(shlex.split(lean) + [f], capture_output=True, text=True, timeout=7200)
    linhas = [l[l.index("AUDITORIA"):] for l in (r.stdout + r.stderr).splitlines() if "AUDITORIA\t" in l]
    return r.returncode, linhas, (r.stdout + r.stderr)[-2000:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nome", required=True)
    ap.add_argument("--raiz", required=True)
    ap.add_argument("--lean", default="lake env lean")
    ap.add_argument("--build", default=".lake/build/lib/lean")
    ap.add_argument("--lote", type=int, default=60)
    ap.add_argument("--saida", default="resultados")
    ap.add_argument("--fonte", default="", help="repositório e commit do benchmark")
    a = ap.parse_args()
    os.makedirs(a.saida, exist_ok=True)
    tmp = os.path.abspath(os.path.join(a.saida, "tmp"))
    os.makedirs(tmp, exist_ok=True)
    todos = modulos(a.raiz)
    ok = [m for m in todos if compilado(m, a.build)]
    falhou = [m for m in todos if m not in ok]
    linhas, caidos = [], []
    for i in range(0, len(ok), a.lote):
        lote = ok[i:i + a.lote]
        # prefixo por componentes do nome de módulo (não por caracteres)
        partes = [m.split(".") for m in lote]
        comum = []
        for xs in zip(*partes):
            if all(x == xs[0] for x in xs):
                comum.append(xs[0])
            else:
                break
        prefixo = ".".join(comum) or lote[0]
        rc, ls, cauda = roda(lote, a.lean, tmp, prefixo)
        if rc != 0 and len(ls) < len(lote):
            # o processo caiu (ou faltou linha): refaz um a um para isolar
            ls = []
            for m in lote:
                rc1, l1, c1 = roda([m], a.lean, tmp, m)
                if rc1 != 0 and not l1:
                    caidos.append({"modulo": m, "cauda": c1[-400:]})
                ls += l1
        linhas += ls
        print(f"{a.nome}: {min(i + a.lote, len(ok))}/{len(ok)} módulos", flush=True)
    vistos = {}
    for l in linhas:
        _, nome, mod, linha, achados = (l.split("\t") + [""])[:5]
        if mod not in ok and not any(mod == m for m in ok):
            continue
        vistos[(nome, mod)] = {"teorema": nome, "modulo": mod, "linha": int(linha or 0),
                               "achados": [x for x in achados.strip().split(";") if x]}
    itens = sorted(vistos.values(), key=lambda x: (x["modulo"], x["linha"]))
    classes = Counter()
    for it in itens:
        for x in it["achados"]:
            classes[x.split("=")[0]] += 1
    resumo = {
        "benchmark": a.nome, "fonte": a.fonte, "modulos": len(todos), "modulos_compilados": len(ok),
        "nao_elabora": falhou, "caidos": caidos, "teoremas_auditados": len(itens), "classes": dict(classes),
        "certificados": sum(1 for it in itens if any(x.split("=")[0] in CERTIFICADAS for x in it["achados"])),
    }
    json.dump({"resumo": resumo, "itens": itens}, open(os.path.join(a.saida, f"{a.nome}.json"), "w"),
              ensure_ascii=False, indent=1)
    md = [f"# Auditoria: {a.nome}", "", f"Fonte: {a.fonte}", "",
          f"- módulos: {len(todos)}; compilam: {len(ok)}; teoremas auditados: {len(itens)}",
          f"- com defeito certificado no kernel: {resumo['certificados']}", ""]
    md += ["| Classe | Teoremas |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(classes.items())]
    md += ["", "## Defeitos certificados", "", "| Teorema | Arquivo:linha | Achados |", "|---|---|---|"]
    for it in itens:
        if any(x.split("=")[0] in CERTIFICADAS for x in it["achados"]):
            arq = it["modulo"].replace(".", "/") + ".lean"
            md.append(f"| `{it['teorema']}` | `{arq}:{it['linha']}` | {'; '.join(it['achados'])} |")
    md += ["", "## Para revisão (trivial por uma tática; riscos de codificação)", "",
           "| Teorema | Arquivo:linha | Achados |", "|---|---|---|"]
    for it in itens:
        if it["achados"] and not any(x.split("=")[0] in CERTIFICADAS for x in it["achados"]):
            arq = it["modulo"].replace(".", "/") + ".lean"
            md.append(f"| `{it['teorema']}` | `{arq}:{it['linha']}` | {'; '.join(it['achados'])} |")
    if falhou:
        md += ["", "## Não compilam nesta versão", ""] + [f"- `{m}`" for m in falhou]
    open(os.path.join(a.saida, f"{a.nome}.md"), "w").write("\n".join(md) + "\n")
    print(json.dumps(resumo, ensure_ascii=False))


if __name__ == "__main__":
    main()
