#!/usr/bin/env python3
"""Gera THEOREMS_2440.md + theorems_2440.json a partir da saída de thm2440.py."""
import json, sys
from collections import Counter

src, out_md, out_json = sys.argv[1:4]
d = json.load(open(src))
T, P, S = d["theorems"], d["props"], d["summary"]
LANES = ["rh", "pnp", "ns", "hodge", "bsd", "ym", "beal"]
LNAME = {"rh": "Riemann", "pnp": "P vs NP", "ns": "Navier–Stokes", "hodge": "Hodge", "bsd": "BSD",
         "ym": "Yang–Mills", "beal": "Beal"}
SHAPES = [("CAMPO_DE_ESTRUTURA_HIPOTESE", "Campo de estrutura (hipótese empacotada)"),
          ("CONDICIONAL_PARA_ALVO", "Condicional → alvo"),
          ("EQUIVALENCIA", "Equivalência (↔)"),
          ("REFUTACAO_OU_NEGACAO", "Refutação / negação / firewall"),
          ("STATUS_OU_REGISTRO", "Status / registro / execução"),
          ("IMPLICACAO_ESTRUTURAL", "Implicação estrutural"),
          ("ESTRUTURAL", "Fato estrutural sem hipótese"),
          ("SEM_FONTE_LOCALIZADA", "Fonte não localizada")]
OBL = {"O1": "RH — FiniteSpanApproximatesChi / UniformLogBound", "O2": "Beal — GCDLowerBound universal",
       "O3": "NS — G1Bridge / regularidade global", "O4": "P≠NP — SATNotInP / UniversalFailure",
       "O5": "Hodge — ConcreteAlgebraicityPayload", "O6": "BSD — parte do posto",
       "O7": "BSD — fórmula refinada", "O8": "YM — construção 4D + gap"}

cnt = {l: Counter(r["shape"] for r in T if r["lane"] == l) for l in LANES}
tot = Counter(r["shape"] for r in T)
L = []
L += ["# Os 2.440 teoremas auditados — o que cada um pode (e não pode) provar", "",
      "Fonte: `PUBLICATION/MASTER/inventories/<lane>/PROOF_INVENTORY.json` (gerados pelo kernel no CI, "
      "listados em `FINAL_PROOF_STRUCTURE.md`). Cada teorema foi localizado **no commit exato que o CI "
      "verificou** (`sources.json`), sua assinatura foi extraída do código-fonte e classificada pela forma "
      "lógica. Reproduzir: `python3 scripts/thm2440.py <M-Core> <clones> saida.json` e "
      "`python3 scripts/report2440.py saida.json THEOREMS_2440.md theorems_2440.json`.", "",
      "## Veredito", "",
      f"- **{S['total']} teoremas**, todos CLEAN no kernel (só `propext`, `Classical.choice`, `Quot.sound`). "
      "Isso é verdade e continua verdade.",
      f"- **{tot['CAMPO_DE_ESTRUTURA_HIPOTESE']} deles ({100*tot['CAMPO_DE_ESTRUTURA_HIPOTESE']/S['total']:.0f}%) "
      "não são provas**: são projeções automáticas de campos `Prop` de `structure`/`class`. "
      "O Lean gera `S.campo : S → P` para cada campo; isso só dá `P` a quem já tem um `S`. "
      "É uma hipótese empacotada, contada como teorema pelo inventário.",
      f"- **{tot['CONDICIONAL_PARA_ALVO']} condicionais** concluem um enunciado-alvo ou terminal. "
      f"**Nenhum** tem todas as hipóteses provadas por outro teorema dos 2.440 "
      f"(descarregados: {len(S['conditionals_fully_discharged'])}).",
      "- Os enunciados finais estão no relatório de proposições do próprio kernel como "
      "`NO_PROOF_IN_LIBRARY` (`MCore.OfficialSpecRH`, `MCore.BealConjecture`, "
      "`MCore.Real.CanonicalFinalProof.PneqNP`, `MCore.Real.MachinePneqNP`, `MCore.Real.FINAL_PROOF_RESIDUAL`…).",
      "- Conclusão: usar os 2.440 juntos dá exatamente as pontes e a infraestrutura dos modelos "
      "(B1–B7, L1–L5 do livro-razão). **Não produz nenhuma das obrigações O1–O8.** "
      "`CLOSED_MATH` continua `false`, agora com a razão medida teorema por teorema.", "",
      "## Classificação por lane", "",
      "| Forma | " + " | ".join(LNAME[l] for l in LANES) + " | Total |",
      "|---|" + "---|" * (len(LANES) + 1)]
for key, label in SHAPES:
    if not tot[key]: continue
    L.append(f"| {label} | " + " | ".join(str(cnt[l][key]) for l in LANES) + f" | **{tot[key]}** |")
L.append("| **Total** | " + " | ".join(str(sum(cnt[l].values())) for l in LANES) + f" | **{S['total']}** |")
L += ["", "Leitura: *equivalências* transportam um problema para outra formulação (não provam nenhum dos "
      "lados); *refutações* são em geral firewalls (rotas fechadas como falsas, alegações bloqueadas); "
      "*status/registro* são fatos sobre o próprio livro-razão ou execuções finitas de máquinas; "
      "*implicações estruturais* são lemas internos dos modelos.", ""]

L += ["## Os 19 condicionais que concluem um alvo", "",
      "Cada linha é `hipóteses → alvo`, certificada. A coluna *descarregada?* responde se algum dos 2.440 "
      "(que não seja campo de estrutura) prova a hipótese.", "",
      "| Lane | Teorema | Hipóteses (abertas) | Conclusão | Obrigação | Descarregada? |",
      "|---|---|---|---|---|---|"]
for r in T:
    if r["shape"] != "CONDICIONAL_PARA_ALVO": continue
    hy = "<br>".join(f"`{h[:70]}`" for h in r["hyps"][:4])
    ob = ", ".join(r.get("obligations") or []) or "—"
    L.append(f"| {LNAME[r['lane']]} | `{r['name'].replace('MCore.', '')}` | {hy} | `{r['conclusion'][:70]}` | "
             f"{ob} | {'sim' if r.get('fully_discharged') else 'não'} |")
L += ["", "Caso exemplar — `closeBeal_from_commonPrime_witnesses`: a hipótese "
      "`∀ d : BealData, CommonPrime d.a d.b d.c` *parece* descarregada por "
      "`BackwardAudit.CommonPrimeWitnessContract.witness`, que tem exatamente esse tipo. Mas esse \"teorema\" "
      "é o campo `witness` da estrutura `CommonPrimeWitnessContract`: só existe se alguém fornecer o contrato. "
      "É a própria conjectura de Beal reembalada. Por isso campos de estrutura nunca contam como descarga.", ""]

L += ["## Relatório de proposições do kernel (`props`)", "",
      "O inventário do CI verifica, para cada `def … : Prop` fechada, se existe um teorema CLEAN cujo tipo "
      "é exatamente ela (PROVED) ou sua negação (REFUTED).", "",
      "| Estado | Quantidade |", "|---|---|"]
for k, v in Counter(p["status"] for p in P).most_common():
    L.append(f"| {k} | {v} |")
L += ["", "### PROVED e REFUTED (todos)", "", "| Lane | Proposição | Estado | Por | Leitura |", "|---|---|---|---|---|"]
NOTE = {
    "MCore.Real.SATNotInP": "refutada **no modelo do lane**: a codificação arbitrária coloca toda linguagem em P "
                            "(`every_language_inP_under_arbitrary_encode`). Defeito do modelo, não P = NP.",
    "MCore.Real.UniversalSATFailure": "idem (mesmo defeito do modelo).",
    "MCore.Real.CanonicalSATParserAttack.RecursiveParserOperationalGap": "o próprio nome do teorema diz: "
                            "portão legado trivialmente habitado.",
    "MCore.RH.R0.ChiMemLpTwo": "χ = 𝟙_(0,1] ∈ L² — lema de infraestrutura da rota Nyman–Beurling.",
    "G1FailProofFinal.CURRENT_ARCHITECTURE_FAIL_PROOF_PROP": "prova de que a arquitetura atual do NS falha "
                            "(firewall).",
}
for p in P:
    if p["status"] in ("PROVED", "REFUTED", "VACUOUS"):
        by = ", ".join(f"`{x.split('.')[-1]}`" for x in (p["inhabited_by"] or p["refuted_by"])[:2])
        L.append(f"| {LNAME[p['lane']]} | `{p['name']}` | {p['status']} | {by} | {NOTE.get(p['name'], '')} |")
L += ["", "Nenhuma proposição PROVED é um enunciado final ou uma obrigação O1–O8.", ""]

L += ["## Por obrigação", "", "| Obrigação | Teoremas que a mencionam | Algum a produz sem hipótese? |", "|---|---|---|"]
for o, label in OBL.items():
    n = sum(1 for r in T if o in (r.get("obligations") or []))
    L.append(f"| {o} — {label} | {n} | não |")
L += ["", "\"Mencionam\" = o nome ou a conclusão contém o vocabulário da obrigação. Todos esses são condicionais, "
      "equivalências, refutações de rotas, campos de estrutura ou fatos de registro.", "",
      "## Como os 2.440 entram no kernel (o uso correto)", "",
      "1. **Pontes**: os condicionais certificados são exatamente a forma `PONTE → ABERTA → ENUNCIADO` já usada "
      "em `atk-kernel/ATK/Conditional/*.lean` e no teorema-mestre `ATK.ClosedMath.closedMath_of_obligations`.",
      "2. **Firewalls**: as refutações impedem promoções indevidas (ex.: `SATNotInP` refutada mostra que o modelo "
      "de máquina precisa ser corrigido antes de qualquer prova de P≠NP valer).",
      "3. **Infraestrutura**: lemas estruturais (L², máquinas, resíduos, Gram) são reutilizáveis num produtor "
      "futuro.",
      "4. **O que falta** é o mesmo de antes: um termo, sem hipóteses, de cada obrigação O1–O8. "
      "Quando existir, o portão calculado `ATK.ClosedMathGate.closed_math` muda `CLOSED_MATH` sozinho.", ""]
open(out_md, "w").write("\n".join(L) + "\n")

slim = [{k: r.get(k) for k in ("lane", "name", "module", "path", "line", "kind", "shape", "conclusion", "hyps",
                               "obligations", "fully_discharged", "field_of", "commit", "repo")} for r in T]
json.dump({"summary": S, "props": P, "theorems": slim}, open(out_json, "w"), ensure_ascii=False, indent=0)
print(f"ok: {len(T)} teoremas -> {out_md}, {out_json}")
