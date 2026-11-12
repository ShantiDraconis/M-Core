#!/usr/bin/env python3
"""Compila a árvore `MCore/` da raiz (o núcleo K15) num diretório próprio de .olean.

O `lakefile.lean` declara a biblioteca `MCore` com `srcDir := "lean"`; a árvore `MCore/` da raiz, que define as
declarações auditadas pelo K15 (`MCore/AxiomAudit.lean`), não entra no `lake build`. Este script compila os
módulos que o módulo raiz `MCore.lean` importa, em ordem, com a Mathlib do projeto, e grava os .olean em `<saida>/`, que deve vir
antes no `LEAN_PATH` para que `MCore.*` resolva para esta árvore.

Uso (dentro do projeto, depois do `lake build`):
  lake env python3 .github/scripts/compilar_raiz.py <saida>
"""
import os
import re
import subprocess
import sys

saida = os.path.abspath(sys.argv[1])
mods = {"MCore": "MCore.lean"}
for f in sorted(os.listdir("MCore")):
    if f.endswith(".lean") and f != "AxiomAudit.lean":
        mods["MCore." + f[:-5]] = os.path.join("MCore", f)
deps = {m: [i for i in re.findall(r"^import\s+(\S+)", open(p, encoding="utf-8").read(), re.M) if i in mods]
        for m, p in mods.items()}
ordem, feitos = [], set()


def visita(m, pilha=()):
    if m in feitos:
        return
    if m in pilha:
        sys.exit(f"ciclo de importação em {m}")
    for d in deps[m]:
        visita(d, pilha + (m,))
    feitos.add(m)
    ordem.append(m)


visita("MCore")  # só o fecho de importação do módulo raiz, que é o que o `AxiomAudit.lean` importa
fora = sorted(set(mods) - feitos)
env = dict(os.environ, LEAN_PATH=saida + os.pathsep + os.environ.get("LEAN_PATH", ""))
for m in ordem:
    destino = os.path.join(saida, *m.split(".")) + ".olean"
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    print(f"compilando {m}", flush=True)
    r = subprocess.run(["lean", "-o", destino, mods[m]], env=env)
    if r.returncode != 0:
        sys.exit(f"{m} não compilou")
print(f"{len(ordem)} módulos em {saida}; fora do fecho do K15 (não compilados): {', '.join(fora) or 'nenhum'}")
