# ATK — Plano de inventário completo de alterações

**Estado:** PARTIAL_SOURCE_AUDIT. Nenhuma varredura nova de todas as refs foi executada neste commit.

## Cobertura comprovada
- Inventário histórico: 250 repositórios catalogados; 224 com histórico; 26 vazios; 4.094 branches; 65.217 blobs/arquivos distintos por conteúdo.
- Inventário de revisão gerado nesta rodada: 21 declarações em 20 combinações repositório/branch/caminho.
- Esses registros são *casos para inspeção*, não mudanças necessárias confirmadas.
- A busca recente identificou 251 repositórios, mas ainda não conciliou essa diferença com o inventário histórico.
- A contagem exata de arquivos que contêm um ou mais dos 28 termos ainda não existe.

## Ordem de auditoria
1. Alegações textuais de fechamento: 54 ocorrências registradas em 14 repositórios. Recuperar caminho/linha do JSON estruturado e confirmar o contexto antes de alterar.
2. Declarações Lean relacionadas a alvos: 872 registros históricos. Conferir objeto original, imports e axiomas transitivos.
3. Coq/Rocq, Agda, Isabelle: 552 enunciados-alvo históricos, 453 em arquivos com escapatórias detectadas.
4. Documentação e relatórios: buscar os 28 termos em todos os arquivos de texto e classificá-los como CORRECT/REVIEW/CHANGE_REQUIRED.
5. CI e scripts: assegurar que o rótulo CERTIFIED refere-se ao teorema exato, não à conjectura.
6. Aplicar mudanças somente aos casos CHANGE_REQUIRED, preservar branches originais e rodar os respectivos kernels.

## Casos individualizados disponíveis
| Repositório | Branch | Arquivo | Declaração | Motivo |
|---|---|---|---|---|
| M-Core | `atk-kernel-check` | `atk-kernel/ATK/LogicAudit.lean` | `rh_material_vacuous` | firewall: D_N ≡ 0 satisfaz a cota trivialmente — mostra que o alvo precisa estar ligado ao D_N concreto |
| M-Core | `atk/global-material-frontier-20261001` | `lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean` | `positive_rh_incompatible_with_negative_lane` | implicação (RH → …), não prova de RH |
| M-Core | `atk/hypothesis-ports-20261014` | `atk-kernel/ATK/ObrigacoesMinimas.lean` | `O1_implica_minima` | implicação (cota uniforme UniformLogBound → D_N → 0), não prova de RH; a cota é a obrigação O1 aberta |
| m-core-p-vs-np | `atk-kernel-check` | `probe/P01MachineConstructionExpectedFailure.lean` | `(example)` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| m-core-p-vs-np | `atk/p01-material-inhabitant-frontier-20260930` | `lean/MCore/Real/P01TerminalCertificate.lean` | `p01ConstructionGap` | P01: idem |
| m-core-p-vs-np | `atk/p01-terminal-promotion-candidate-20260930` | `lean/MCore/Real/P01TerminalMaterialCertificate.lean` | `p01_closed_no_hypothesis` | P01: idem |
| m-core-p-vs-np | `work/pnp-minimal-separation-20261005` | `lean/MCore/PNPMaterialAtoms.lean` | `(example)` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| m-core-hodge | `atk/concrete-payload-model-binding-audit` | `audit/ATK_CONCRETE_PAYLOAD_MODEL_BINDING_COUNTERAUDIT.lean` | `concretePayload_vacuous_on_empty_model` | firewall: modelo vazio torna o payload de Hodge vácuo |
| m-core-yang-mills | `atk/b60-triviality-audit` | `lean/MCore/YangMills/A1/B60TrivialityAudit.lean` | `toyB60ConcretePhysicalAdapter` | firewall: modelo degenerado habita o adaptador B60 de Yang–Mills |
| m-core-yang-mills | `atk/b60-triviality-audit` | `lean/MCore/YangMills/A1/B60TrivialityAudit.lean` | `b60_inhabited_by_degenerate_model` | firewall: idem |
| atk-certified-priority-record | `main` | `snapshots/m-core-p-vs-np/probe/P01MachineConstructionExpectedFailure.lean` | `(example)` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| millennium-riemann-I | `atk-rh-g21-mold` | `src/Riemann/CollapseProof/Contradiction.lean` | `riemann_hypothesis` | depende de `axiom collapse_law` e `axiom I_ne_one` declarados em outro arquivo (RH reescrita); o próprio branch atk/label-circular-rh-20261008 a rotula como circular |
| millennium-riemann-I | `atk/label-circular-rh-20261008` | `src/Riemann/CollapseProof/Contradiction.lean` | `riemann_hypothesis` | depende de `axiom collapse_law` e `axiom I_ne_one` declarados em outro arquivo (RH reescrita); o próprio branch atk/label-circular-rh-20261008 a rotula como circular |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/All.lean` | `all_millennium_problems` | importa `Gaps/*.lean` e `HorizonPrime/ProfiniteUniformity.lean`, que declaram `axiom zero_density_uniform`, `axiom explicit_formula_uniform_error` e até os objetos (`axiom EllipticCurve : Type`…); os alvos são `def` locais |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/BSD_final.lean` | `BSD_final` | idem (axiomas importados) |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/Hodge_final.lean` | `Hodge_final` | idem (axiomas importados) |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/PvsNP_final.lean` | `PneqNP_final` | idem (axiomas importados) |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/RH_final.lean` | `RH_final` | idem (axiomas importados de Gaps/RH_ZD_UEF.lean) |
| horizon-prime---framework | `copilot/formalize-final-theorem` | `formal/lean/FinalTheorems/YM_final.lean` | `YM_final` | idem (axiomas importados) |
| universal-emergent-logic- | `ShantiDraconis-patch-1` | `formalization/lean/UETheta_to_RH.lean` | `UETheta_implies_RH` | `def RiemannHypothesis : Prop := True` no próprio arquivo — vácuo |
| universal-emergent-logic- | `ShantiDraconis-patch-1` | `src/lean/EmergentTheta/Main/MasterTheorem.lean` | `MasterTheorem` | hipótese de classe `[UniversalThetaFramework]` e axiomas nos arquivos *FromUT.lean importados |

## Artefatos
- `conditional/INVENTORY.md`: inventário histórico e revisão detalhada.
- `conditional/FORMAL_LANGUAGE_STANDARD.md`: taxonomia e regra de certificação.
- `conditional/FORMAL_LANGUAGE_REVIEW_SEED.csv`: casos individualizados.
- `conditional/scripts/audit_language_all_refs.py`: scanner de termos; exige clones com todas as refs previamente buscadas.

## Critério de encerramento
Para cada repositório e branch: `REFS_ENUMERATED`, `FILES_SCANNED`, `OCCURRENCES_CLASSIFIED`, `CHANGES_REVIEWED`, `KERNEL_VERIFIED`. Não declarar 100% antes de todos esses critérios serem atendidos.
