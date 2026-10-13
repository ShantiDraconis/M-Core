# Busca de provas em todos os repositórios e branches (13/10/2026)

Pergunta: algum dos seus repositórios, em qualquer branch, já tem uma prova que feche uma das
obrigações de `CLOSED_MATH`? Resposta curta: **não**. O único resultado sem hipóteses é o P01
(SAT ∈ NP no modelo do lane P vs NP), que já está no livro-razão como avanço da ponte B4.

## Escopo

- **32 repositórios**, **2210 branches**, **4858 arquivos Lean distintos**.
- Os 8 núcleos (M-Core e os 7 lanes), os 5 de integração/auditoria, os 8 espelhos públicos `atk-*-public`
  e os 13 históricos citados no inventário (`millennium-*`, `proofs-multiprover`, `universal-proof-hub`, …).
- **688 declarações** cuja conclusão é um enunciado, um terminal do registro ou uma obrigação.

## Método

Cada arquivo `.lean` de cada branch é lido uma vez (deduplicado por conteúdo). Para cada declaração
cuja conclusão é um alvo, o scanner registra: hipóteses explícitas, hipóteses de seção (`variable … include`),
`sorry`/`admit`/`exact ?_`, `axiom` declarados, negação e equivalência. Os candidatos sem hipóteses foram
lidos à mão, incluindo os axiomas em outros arquivos. Script: `conditional/scripts/proof_scan.py`.

## Resultado

| Categoria | Quantas | O que significa |
|---|---|---|
| CONDICIONAL | 492 | recebe a peça aberta como hipótese — não fecha nada sozinho |
| EQUIVALÊNCIA | 108 | `Problema ↔ outra forma` — reformula, não prova |
| NEGAÇÃO | 39 | conclui a negação de um alvo (contraexemplos, refutações de rotas) |
| BURACO (sorry/?_) | 27 | prova incompleta (`sorry` ou `exact ?_`), não compila como prova |
| AXIOMA | 12 | depende de `axiom` declarado no próprio repositório |
| AUDITORIA DE VACUIDADE | 7 | suas próprias auditorias: o alvo vale num modelo vazio/de brinquedo |
| SEM HIPÓTESES | 3 | conclusão direta, sem hipóteses, sem sorry, sem axiom |

### Os únicos sem hipóteses: P01 (P vs NP)

| Repositório | Branch | Declaração |
|---|---|---|
| `m-core-p-vs-np` | `atk/p01-material-inhabitant-frontier-20260930` | `p01ConstructionGap` : `P01ConstructionGap` — `lean/MCore/Real/P01TerminalCertificate.lean` |
| `m-core-p-vs-np` | `atk/p01-terminal-promotion-candidate-20260930` | `p01_closed_no_hypothesis` : `P01ConstructionGap` — `lean/MCore/Real/P01TerminalMaterialCertificate.lean` |
| `m-core-p-vs-np` | `work/pnp-minimal-separation-20261005` | `(example)` : `P01MachineConstruction` — `lean/MCore/PNPMaterialAtoms.lean` |

Todos dizem a mesma coisa: SAT ∈ NP no modelo de máquinas do lane. Nenhum `axiom` nem `sorry` nesses
branches; certificado pelo CI do lane (Lean 4.19), não recompilado aqui. É metade da ponte B4 (Cook–Levin),
não P ≠ NP: o próprio `PNPAfterP01.lean` diz que G2.1 (SAT ∉ P) "continua aberta".

### Falso positivo: `riemann_hypothesis` no `millennium-riemann-I`

Branches `atk-rh-g21-mold` e `atk/label-circular-rh-20261008`, arquivo `src/Riemann/CollapseProof/Contradiction.lean`.
A "prova" usa dois axiomas declarados no repositório:

- `axiom collapse_law : (∃ z : NontrivialZero, z.s.re ≠ 1/2) → I = one`
- `axiom I_ne_one : I ≠ 1`

Juntos, eles são a própria Hipótese de Riemann reescrita. Além disso, `RiemannHypothesis` ali é uma
definição local (`∀ z : NontrivialZero, onCriticalLine z.s`), não a da Mathlib. O nome do seu próprio branch
`atk/label-circular-rh-20261008` já registra que é circular.

### Outros pontos que parecem fechamento e não são

- `m-core-riemann`, `open_math/lean/RHAllGaps.lean` e `RHMaterialChallenge.lean`: `GAP_F2_UNIFORM_LOG_DN` e
  `DISCOVER_material_inhabitant` concluem o terminal de RH, mas a prova é `exact ?_` (arquivos marcados
  "intentionally RED").
- M-Core `ProposedHypothesis.lean`: `riemann_enabled`, `beal_enabled` usam `variable (H : ProposedHypothesis M)`
  — condicionais; o próprio arquivo diz `unconditionalCount` = 0.
- `m-core-yang-mills` `B60TrivialityAudit.lean`, `m-core-hodge` `…COUNTERAUDIT.lean`, M-Core `LogicAudit.lean`:
  auditorias suas mostrando que os terminais valem em modelos degenerados — ou seja, que não bastam.

## Os 14 arquivos do inventário anexado

| Repositório | Branch | Arquivo | Resultado |
|---|---|---|---|
| `m-core-p-vs-np` | `atk/p01-closure-audit-20261013-pnp-reduction` | `PNPAfterP01.lean` | `pneqnp_of_universal_failure` → `PneqNP` (condicional); `pneqnp_of_sat_not_in_p` → `PneqNP` (condicional) |
| `m-core-p-vs-np` | `atk/p01-closure-audit-20261013-pnp-reduction` | `PNPAfterP01Audit.lean` | não conclui nenhum alvo/terminal |
| `m-core-beal` | `atk/beal-effective-kernel-20261003` | `BealEffectiveKernel.lean` | `exact_remaining_closes_beal` → `BealConjecture` (condicional) |
| `m-core-beal` | `atk/beal-effective-kernel-20261003` | `ExactRemainingObligation.lean` | não conclui nenhum alvo/terminal |
| `m-core-bsd` | `atk/material-rigid-integration-20261009` | `BSD_MaterialDense.lean` | não conclui nenhum alvo/terminal |
| `m-core-hodge` | `atk/material-rigid-integration-20261009` | `Hodge_MaterialDense.lean` | `material_identity` → `ConcreteAlgebraicityPayload` (condicional) |
| `m-core-yang-mills` | `atk/ym-material-promotion-v13-20261007` | `ContinuumSpectralTransferV13.lean` | não conclui nenhum alvo/terminal |
| `m-core-yang-mills` | `atk/ym-material-promotion-v13-20261007` | `K14HamiltonianConcreteRealizationV13.lean` | não conclui nenhum alvo/terminal |
| `m-core-riemann` | `atk/terminal-parameter-law-20261003` | `FiniteSpan.lean` | não conclui nenhum alvo/terminal |
| `m-core-riemann` | `atk/terminal-parameter-law-20261003` | `LogMajorantFinalProducer.lean` | não conclui nenhum alvo/terminal |
| `m-core-riemann` | `atk/terminal-parameter-law-20261003` | `GramTerminalLink.lean` | não conclui nenhum alvo/terminal |
| `navier-stokes-critical-barrier-audit` | `atk/ns-bulk-tail-material-producer-20261001` | `ActualNSBulkTailProducer.lean` | `ActualNSBulkTailProducer.toSignedGainCore` → `ActualNSToSignedGainCore` (condicional); `ns_bulk_tail_open_math_closes_signed_gain` → `ActualNSToSignedGainCore` (condicional) |
| `navier-stokes-critical-barrier-audit` | `atk/ns-bulk-tail-material-producer-20261001` | `G1SignedGainCoreAdapter.lean` | `actualNS_to_signedGainCore_of_g1` → `ActualNSToSignedGainCore` (condicional) |
| `navier-stokes-critical-barrier-audit` | `atk/ns-bulk-tail-material-producer-20261001` | `UniversalBulkTailProducer.lean` | não conclui nenhum alvo/terminal |

## Por problema

| Problema | Condicional | Equivalência | Negação | Buraco | Axioma | Vacuidade | Sem hipóteses |
|---|---|---|---|---|---|---|---|
| beal | 74 | 59 | 14 | 1 | 2 | 0 | 0 |
| bsd | 9 | 0 | 1 | 0 | 0 | 0 | 0 |
| hodge | 111 | 0 | 1 | 0 | 0 | 1 | 0 |
| navier-stokes | 16 | 0 | 1 | 2 | 0 | 0 | 0 |
| pvsnp | 242 | 43 | 10 | 19 | 1 | 2 | 3 |
| riemann | 35 | 6 | 12 | 5 | 9 | 2 | 0 |
| yang-mills | 5 | 0 | 0 | 0 | 0 | 2 | 0 |

## Alegações de fechamento nos textos

Nenhum arquivo afirma `CLOSED_MATH = true` ou `OPEN_MATH = false` como fato. Todas as ocorrências são regras
("só depois que toda obrigação for provada"), avisos ("No terminal OPEN_MATH=false … is made here") ou o portão
deste branch. O registro `OfficialObservableLawAudit` do `axiomatic-millenium` marca leis auxiliares
(`provedUpstreamLaw`, `provedNegativeObject`), não os problemas.

## Veredito por obrigação

| Obrigação | Encontrada fechada em algum repositório/branch? |
|---|---|
| B1–B3, B5–B7 (pontes) | não formalizadas em nenhum lugar |
| B4 Cook–Levin | **parcial**: SAT ∈ NP provado no modelo do lane (P01); NP-dificuldade não |
| O1 Riemann (cota D_N) | não — só arquivos com `exact ?_` e uma versão com axiomas |
| O2 Beal | não — 59 equivalências e 74 condicionais, nenhuma prova |
| O3 Navier–Stokes | não — e a rota G5 foi refutada (`ns_19_false`) |
| O4 P vs NP (SAT ∉ P) | não — G2.1 aberta |
| O5 Hodge | não — terminal só vale em modelo vazio (sua contra-auditoria) |
| O6–O7 BSD | não |
| O8 Yang–Mills | não — terminal só vale em modelo degenerado (sua auditoria) |
| L1–L5 (ligações de modelo) | não |

`CLOSED_MATH` continua `false`, agora com a busca completa como evidência.
