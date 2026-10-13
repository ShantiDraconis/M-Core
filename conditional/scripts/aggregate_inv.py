#!/usr/bin/env python3
"""Agrega /home/claude/inv/*.json num inventário mestre (INVENTORY.md + inventory.json).

Uso: aggregate_inv.py <inv_dir> <catalog/repos.txt> <saida.md> <saida.json>
"""
import json, os, sys, glob, re
from collections import Counter, defaultdict

inv_dir, catalog, out_md, out_json = sys.argv[1:5]
cat = []
for l in open(catalog):
    if l.startswith("#") or not l.strip(): continue
    parts = l.strip().split("|")
    cat.append((parts[0], parts[1] if len(parts) > 1 else ""))

PROVER_LANGS = ["Lean", "Coq/Rocq", "Agda", "Isabelle", "Metamath", "SMT", "TPTP"]
CALC_LANGS = ["Python", "Jupyter", "Julia", "Sage", "R", "C/C++", "Rust", "JS/TS", "Haskell", "MATLAB/ObjC"]
DOC_LANGS = ["LaTeX", "Markdown"]

na_status = {}
_nf = os.path.join(os.path.dirname(os.path.abspath(catalog)), "na_status.json")
if os.path.exists(_nf):
    na_status = json.load(open(_nf))
REVIEW = {
    "rh_material_vacuous": "firewall: D_N ≡ 0 satisfaz a cota trivialmente — mostra que o alvo precisa estar ligado ao D_N concreto",
    "positive_rh_incompatible_with_negative_lane": "implicação (RH → …), não prova de RH",
    "P01MachineConstruction": "P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP)",
    "P01ConstructionGap": "P01: idem",
    "concretePayload_vacuous_on_empty_model": "firewall: modelo vazio torna o payload de Hodge vácuo",
    "toyB60ConcretePhysicalAdapter": "firewall: modelo degenerado habita o adaptador B60 de Yang–Mills",
    "b60_inhabited_by_degenerate_model": "firewall: idem",
    "riemann_hypothesis": "depende de `axiom collapse_law` e `axiom I_ne_one` declarados em outro arquivo (RH reescrita); o próprio branch atk/label-circular-rh-20261008 a rotula como circular",
    "all_millennium_problems": "importa `Gaps/*.lean` e `HorizonPrime/ProfiniteUniformity.lean`, que declaram `axiom zero_density_uniform`, `axiom explicit_formula_uniform_error` e até os objetos (`axiom EllipticCurve : Type`…); os alvos são `def` locais",
    "RH_final": "idem (axiomas importados de Gaps/RH_ZD_UEF.lean)", "BSD_final": "idem (axiomas importados)",
    "Hodge_final": "idem (axiomas importados)", "PneqNP_final": "idem (axiomas importados)", "YM_final": "idem (axiomas importados)",
    "UETheta_implies_RH": "`def RiemannHypothesis : Prop := True` no próprio arquivo — vácuo",
    "MasterTheorem": "hipótese de classe `[UniversalThetaFramework]` e axiomas nos arquivos *FromUT.lean importados",
}
rows, missing, empty = [], [], []
lang_tot = Counter()
lean_unc_clean = []
other_stmts = []
claims_tot = Counter()
for name, vis in cat:
    if name == "copilot-cli": continue
    f = os.path.join(inv_dir, name.lower() + ".json")
    if not os.path.exists(f):
        missing.append((name, vis, "não varrido")); continue
    d = json.load(open(f))
    if d.get("branches", 0) == 0:
        missing.append((name, vis, "vazio (repositório sem commits)" if na_status.get(name) == "empty"
                        else "sem acesso (privado, não anexado)")); continue
    langs = d.get("languages", {})
    if sum(langs.values()) == 0:
        empty.append(name)
    for k, v in langs.items(): lang_tot[k] += v
    lean = d.get("lean") or {}
    finds = lean.get("findings", [])
    unc = [x for x in finds if x["explicit_hypotheses"] == 0 and not x["negated"] and not x["section_variables"]]
    clean = [x for x in unc if not x["file_sorry"] and not x["file_axioms"]]
    for x in clean:
        lean_unc_clean.append({"repo": name, "name": x["name"], "kind": x["kind"], "target": x["target"],
                               "conclusion": x["conclusion"][:160], "locations": x["locations"][:2],
                               "n_locations": x["n_locations"]})
    po = d.get("provers_other", {})
    for s in po.get("target_statements", []):
        other_stmts.append(dict(s, repo=name))
    nclaims = len(lean.get("claims", []))
    claims_tot[name] = nclaims
    rows.append({"repo": name, "visibility": vis, "branches": d["branches"],
                 "lean": langs.get("Lean", 0), "coq": langs.get("Coq/Rocq", 0), "agda": langs.get("Agda", 0),
                 "isabelle": langs.get("Isabelle", 0), "python": langs.get("Python", 0) + langs.get("Jupyter", 0),
                 "latex": langs.get("LaTeX", 0), "markdown": langs.get("Markdown", 0),
                 "files_total": sum(langs.values()),
                 "lean_target_decls": len(finds), "lean_unconditional": len(unc), "lean_unconditional_clean": len(clean),
                 "lean_with_sorry_or_axiom": sum(1 for x in finds if x["file_sorry"] or x["file_axioms"]),
                 "other_prover_files": po.get("files", 0), "other_prover_with_escape": po.get("with_escape", 0),
                 "other_prover_target_statements": len(po.get("target_statements", [])),
                 "text_claims_closed": nclaims})

rows.sort(key=lambda r: (-r["lean_target_decls"], -r["lean"], r["repo"]))
tot = lambda k: sum(r[k] for r in rows)
summary = {
    "catalog": len([c for c in cat if c[0] != "copilot-cli"]),
    "scanned": len(rows), "not_accessible": sum(1 for m in missing if m[2].startswith("sem acesso")),
    "empty_repos": sum(1 for m in missing if m[2].startswith("vazio")),
    "branches": tot("branches"), "files_distinct": sum(lang_tot.values()),
    "lean_files": lang_tot.get("Lean", 0), "coq_files": lang_tot.get("Coq/Rocq", 0),
    "agda_files": lang_tot.get("Agda", 0), "isabelle_files": lang_tot.get("Isabelle", 0),
    "python_files": lang_tot.get("Python", 0) + lang_tot.get("Jupyter", 0), "latex_files": lang_tot.get("LaTeX", 0),
    "lean_target_decls": tot("lean_target_decls"), "lean_unconditional_clean": len(lean_unc_clean),
    "lean_unconditional_equivalences": sum(1 for x in lean_unc_clean if "↔" in x["conclusion"]),
    "lean_unconditional_direct": sum(1 for x in lean_unc_clean if "↔" not in x["conclusion"]),
    "other_prover_target_statements": len(other_stmts),
    "other_prover_statements_in_files_with_escape": sum(1 for s in other_stmts if s["file_escapes"]),
    "text_claims_closed": sum(claims_tot.values()),
    "repos_with_text_claims": sum(1 for v in claims_tot.values() if v),
}
json.dump({"summary": summary, "languages": dict(lang_tot.most_common()), "repos": rows,
           "not_accessible": [{"repo": a, "visibility": b, "reason": c} for a, b, c in missing],
           "lean_unconditional_clean": lean_unc_clean, "other_prover_target_statements": other_stmts},
          open(out_json, "w"), ensure_ascii=False, indent=1)

S = summary
L = ["# Inventário mestre — todos os repositórios, todas as linguagens de prova", "",
     "Varredura de **todos os branches** de cada repositório acessível da conta (blobs deduplicados por "
     "conteúdo). Lean: declarações que concluem um dos alvos dos 7 problemas (enunciados, terminais, "
     "obrigações), com hipóteses, `sorry`/`?_`/`axiom` no arquivo. Coq/Rocq, Agda, Isabelle: enunciados que "
     "mencionam os problemas + escapatórias da linguagem (`Admitted`/`Axiom`/`Parameter`/`Hypothesis`; "
     "`postulate`; `sorry`/`oops`/`axiomatization`). Reproduzir: `scripts/inventory_scan.py` e "
     "`scripts/aggregate_inv.py`.", "",
     "## Números", "",
     "| | |", "|---|---|",
     f"| Repositórios no catálogo | {S['catalog']} |",
     f"| Varridos (todos os branches) | **{S['scanned']}** |",
     f"| Vazios (sem nenhum commit) | {S['empty_repos']} |",
     f"| Sem acesso nesta sessão (privados não anexados) | {S['not_accessible']} |",
     f"| Branches varridos | {S['branches']} |",
     f"| Arquivos distintos (por conteúdo) | {S['files_distinct']} |",
     f"| Lean / Coq / Agda / Isabelle | {S['lean_files']} / {S['coq_files']} / {S['agda_files']} / {S['isabelle_files']} |",
     f"| Python (+notebooks) / LaTeX | {S['python_files']} / {S['latex_files']} |",
     f"| Declarações Lean que concluem um alvo | {S['lean_target_decls']} |",
     f"| …sem hipótese explícita, sem sorry/axiom no próprio arquivo | {S['lean_unconditional_clean']}: "
     f"{S['lean_unconditional_equivalences']} equivalências (↔) + {S['lean_unconditional_direct']} afirmações diretas, revisadas abaixo |",
     f"| Enunciados-alvo em Coq/Agda/Isabelle | {S['other_prover_target_statements']} "
     f"({S['other_prover_statements_in_files_with_escape']} em arquivos com escapatória) |",
     f"| Alegações textuais de fechamento (`CLOSED_MATH = true`, `state := .proved`…) | "
     f"{S['text_claims_closed']} em {S['repos_with_text_claims']} repositórios |", "",
     "## Veredito", "",
     "Nenhum arquivo, em nenhuma linguagem, em nenhum branch, contém um termo sem hipóteses e sem "
     "escapatória que prove o enunciado oficial de qualquer um dos 7 problemas ou uma das obrigações O1–O8. "
     "Os resultados \"sem hipótese\" listados abaixo foram revisados um a um: são alvos definidos localmente "
     "como fórmulas triviais, modelos de brinquedo, registros de estado ou o resultado P01 (SAT ∈ NP no modelo "
     "do lane). As alegações textuais de fechamento são texto: nenhuma vem acompanhada de um termo que o "
     "kernel aceite. `CLOSED_MATH` continua sendo calculado pelo portão do kernel e continua `false`.", "",
     "## Por repositório (com material de prova)", "",
     "| Repositório | Branches | Lean | Coq | Agda | Isabelle | Python | LaTeX | Decl. Lean → alvo | sem hip. limpas | Enunc. outros provadores | Alegações textuais |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    if not (r["lean"] or r["coq"] or r["agda"] or r["isabelle"] or r["text_claims_closed"]): continue
    L.append(f"| {r['repo']} | {r['branches']} | {r['lean']} | {r['coq']} | {r['agda']} | {r['isabelle']} | "
             f"{r['python']} | {r['latex']} | {r['lean_target_decls']} | {r['lean_unconditional_clean']} | "
             f"{r['other_prover_target_statements']} | {r['text_claims_closed']} |")
others = [r for r in rows if not (r["lean"] or r["coq"] or r["agda"] or r["isabelle"] or r["text_claims_closed"])]
L += ["", f"Outros {len(others)} repositórios varridos não têm arquivo de assistente de prova nem alegação de "
      "fechamento (documentação, dados, código de aplicação): " + ", ".join(r["repo"] for r in others) + ".", ""]
L += ["## Afirmações diretas sem hipótese explícita — revisão uma a uma", "",
      "O scanner só vê `axiom` no próprio arquivo e hipóteses entre parênteses. Por isso cada afirmação "
      "direta foi aberta e lida.", "",
      "| Repositório | Declaração | Conclusão | Onde | Revisão |", "|---|---|---|---|---|"]
for x in lean_unc_clean:
    if "↔" in x["conclusion"]: continue
    loc = x["locations"][0] if x["locations"] else ["", ""]
    nm = x["name"] or x["conclusion"].split()[-1]
    note = REVIEW.get(x["name"]) or REVIEW.get(x["conclusion"].replace("Nonempty ", "").split()[0], "")
    L.append(f"| {x['repo']} | `{x['name'] or '(example)'}` | `{x['conclusion'][:80]}` | `{loc[0]}`:`{loc[1]}` | {note} |")
L += ["", f"As outras {S['lean_unconditional_equivalences']} são equivalências (`Alvo ↔ Reformulação`): "
      "transportam o problema, não o resolvem. Lista completa em `inventory.json`.", ""]
L += ["", "## Coq/Rocq, Agda, Isabelle — enunciados que mencionam os problemas", "",
      f"{S['other_prover_statements_in_files_with_escape']} dos {S['other_prover_target_statements']} estão em arquivos com "
      "`Admitted`/`Axiom`/`Parameter`/`postulate`/`sorry`. Os demais foram lidos: são condicionais "
      "(`CookLevin → SATnotP → PneqNP`, `StoneLemma ⟶ P_neq_NP`), equivalências (`RiemannHypothesis ↔ …`), "
      "enunciados `True`, contas sobre definições locais (`Omega S_cl p ≥ 3`) ou registros de autoria. "
      "Nenhum prova um enunciado oficial.", "",
      "| Repositório | Linguagem | Nome | Enunciado | Escapatórias no arquivo | Onde |", "|---|---|---|---|---|---|"]
for s in other_stmts[:200]:
    L.append(f"| {s['repo']} | {s['lang']} | `{s['name']}` | `{s['statement'][:90]}` | "
             f"{', '.join(s['file_escapes']) or '—'} | `{s['branch']}`:`{s['path']}` |")
if len(other_stmts) > 200:
    L.append(f"| … | | | ({len(other_stmts) - 200} a mais em inventory.json) | | |")
L += ["", "## Vazios e sem acesso", "",
      "**Vazios (sem nenhum commit):** " + ", ".join(a for a, b, c in missing if c.startswith("vazio")) + ".", "",
      "**Sem acesso nesta sessão** (privados não anexados; os nomes indicam arte, arquivo pessoal/jurídico, "
      "arquitetura, idiomas, cultura etc.). Podem ser incluídos sob pedido: "
      + ", ".join(a for a, b, c in missing if c.startswith("sem acesso")) + ".", ""]
L += ["## Linguagens (todos os repositórios varridos)", "", "| Linguagem/formato | Arquivos distintos |", "|---|---|"]
for k, v in lang_tot.most_common(30):
    L.append(f"| {k} | {v} |")
open(out_md, "w").write("\n".join(L) + "\n")
print(json.dumps(summary, ensure_ascii=False, indent=1))
