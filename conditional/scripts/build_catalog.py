#!/usr/bin/env python3
"""Gera CATALOG.md e catalog/repos.json a partir de catalog/repos.txt.

Classificação por regras de nome (ordem importa). Ajuste NOTES/regras e rode de novo:
    python3 scripts/build_catalog.py
"""
import json, os, re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "catalog", "repos.txt")

repos = []
for line in open(SRC, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    name, vis = line.split("|")
    repos.append({"name": name, "visibility": vis})

CORE = OrderedDict([
    ("M-Core", "Registro central: FinalProofRegistry (7 lanes, todos openMath) + atk-kernel com 19 lemas auxiliares."),
    ("m-core-riemann", "Lane RH (Nyman–Beurling/Báez-Duarte). Terminal: FiniteSpanApproximatesChi / majorante de D_N."),
    ("m-core-beal", "Lane Beal. Terminal: GCDLowerBoundProducer."),
    ("navier-stokes-critical-barrier-audit", "Lane NS. Terminal: ActualNSToSignedGainCore em EnstrophyData genuína."),
    ("m-core-hodge", "Lane Hodge. Terminal: ConcreteAlgebraicityPayload."),
    ("m-core-p-vs-np", "Lane P vs NP. Terminal: P01MachineConstruction ∧ G21Pointwise."),
    ("m-core-bsd", "Lane BSD. Terminal: domínio realizável + igualdade de posto + fórmula refinada."),
    ("m-core-yang-mills", "Lane Yang–Mills. Terminal: B60ConcretePhysicalAdapter."),
    ("m-core-openai-ns-audit", "Kernel NS no formato atk-kernel + CI de axiomas (modelo deste monorepo)."),
    ("axiomatic-millenium", "GlobalOpenMathCut (importado no atk-math-core-public)."),
    ("atk-certified-priority-record", "Registro de prioridade/autoria."),
])

PROBLEMS = [
    ("riemann", r"riemann|(^|[-_])rh([-_.]|$)|zeta|lc-rh"),
    ("navier-stokes", r"navier|stokes|(^|-)ns$|regularity"),
    ("p-vs-np", r"p-vs-np|pnp|n-np|complexity-collapse"),
    ("hodge", r"hodge"),
    ("bsd", r"bsd|birch"),
    ("yang-mills", r"yang|(^|-)ym$|mass-gap"),
    ("poincare", r"poincare"),
    ("beal", r"beal"),
    ("collatz", r"collatz"),
]

GROUPS = [
    ("A", "Núcleo canônico (M-Core + 7 lanes)", lambda n: n in CORE),
    ("B", "Espelhos públicos ATK", lambda n: re.match(r"atk-.*-public$", n)),
    ("C", "Millennium por problema (histórico/exploratório)", lambda n: problems_of(n)),
    ("D", "Programas Millennium unificados e meta", lambda n: re.search(r"millen|hawking|meta-math|open-math|equations-of-unsolved", n, re.I)),
    ("E", "Lean, verificação formal e ferramentas", lambda n: re.search(r"lean|proof|formal|multiprover|latex|ci-templates|copilot", n, re.I)),
    ("F", "Fundações próprias (indeterminação, 0-0, I, identidade emergente)", lambda n: re.search(
        r"indetermin|ideterminate|^0-0|00-limit|^zero-(codex|game)|i-constant|i-foundations|I-Framework|emergent|universal-arithmetic|"
        r"metalogic|cardinality|omega|^umi|^UMA$|spectrally|signature|horizon|orion|^trans$|trivalent|pi-border|"
        r"universal-0-5|unified-classical|universal-emergent|indeterminate|codex|heu-7|TABP|cryptographic-logic|i-theology|singular", n, re.I)),
    ("G", "Ciência simbólica (série -00)", lambda n: re.search(r"symbolic|quantum|cosmic|sbfe|consciousness|identity-fields|dmt-|siamese|photon", n, re.I)),
    ("H", "Linguagem, história e textos", lambda n: re.search(
        r"harappan|indus|linguistic|phonology|tupi|primordial|tanakh|sacred|theology|beit|mishkan|elyon|genesis|oral-substrate|translation|archetypes|education", n, re.I)),
    ("I", "Arte, espetáculo e portfólio", lambda n: re.search(
        r"olympic|lighting|stage|sound|creative|installations|art-00|music|ceremony|digital-fire|la-2008|la2028|bixiga|portfolio|lunar-hive", n, re.I)),
    ("J", "Engenharia, sistemas e laboratórios", lambda n: re.search(
        r"engineering|reactor|water|ship-|hotel|urban|closed-loop|global-systems|metaos|zero--os|zero-engine|zero-ai|research-os|"
        r"^s5-|nipah|maritimo|tiefc|seet|universe|universal|eclectic|projeto|m-private", n, re.I)),
    ("K", "Jurídico, negócios e arquivos pessoais", lambda n: True),
]

def problems_of(n):
    return [p for p, rx in PROBLEMS if re.search(rx, n, re.I)]

for r in repos:
    n = r["name"]
    r["problems"] = problems_of(n)
    for gid, gname, rule in GROUPS:
        if rule(n):
            r["group"] = gid
            r["group_name"] = gname
            break
    r["note"] = CORE.get(n, "")
    r["url"] = f"https://github.com/ShantiDraconis/{n}"

os.makedirs(os.path.join(ROOT, "catalog"), exist_ok=True)
json.dump(repos, open(os.path.join(ROOT, "catalog", "repos.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)

md = ["# Catálogo dos repositórios",
      "",
      f"{len(repos)} repositórios da conta `ShantiDraconis`, agrupados por função. "
      "Gerado por `scripts/build_catalog.py` a partir de `catalog/repos.txt` "
      "(lista obtida por buscas em 2026-10-13; algum repositório antigo pode faltar).",
      "",
      "Nada aqui altera os repositórios originais.",
      ""]

# resumo
md += ["| Grupo | Repositórios |", "|---|---|"]
for gid, gname, _ in GROUPS:
    c = sum(1 for r in repos if r["group"] == gid)
    md.append(f"| {gid}. {gname} | {c} |")
md.append("")

# por problema
md += ["## Por problema", "", "| Problema | Repositórios |", "|---|---|"]
for p, _ in PROBLEMS:
    names = [r["name"] for r in repos if p in r["problems"]]
    md.append(f"| {p} | " + ", ".join(f"`{x}`" for x in names) + " |")
md.append("")

for gid, gname, _ in GROUPS:
    rows = [r for r in repos if r["group"] == gid]
    if not rows:
        continue
    md += [f"## {gid}. {gname} ({len(rows)})", ""]
    if gid == "A":
        md += ["| Repositório | Papel |", "|---|---|"]
        for name in CORE:
            md.append(f"| [`{name}`](https://github.com/ShantiDraconis/{name}) | {CORE[name]} |")
    else:
        md += ["| Repositório | Visibilidade | Problema |", "|---|---|---|"]
        for r in sorted(rows, key=lambda r: r["name"].lower()):
            md.append(f"| [`{r['name']}`]({r['url']}) | {r['visibility']} | {', '.join(r['problems']) or '—'} |")
    md.append("")

open(os.path.join(ROOT, "CATALOG.md"), "w", encoding="utf-8").write("\n".join(md))
print(f"{len(repos)} repos")
for gid, gname, _ in GROUPS:
    print(gid, gname, sum(1 for r in repos if r["group"] == gid))
