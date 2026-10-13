# Inventário mestre — todos os repositórios, todas as linguagens de prova

Varredura de **todos os branches** de cada repositório acessível da conta (blobs deduplicados por conteúdo). Lean: declarações que concluem um dos alvos dos 7 problemas (enunciados, terminais, obrigações), com hipóteses, `sorry`/`?_`/`axiom` no arquivo. Coq/Rocq, Agda, Isabelle: enunciados que mencionam os problemas + escapatórias da linguagem (`Admitted`/`Axiom`/`Parameter`/`Hypothesis`; `postulate`; `sorry`/`oops`/`axiomatization`). Reproduzir: `scripts/inventory_scan.py` e `scripts/aggregate_inv.py`.

## Números

| | |
|---|---|
| Repositórios no catálogo | 250 |
| Varridos (todos os branches) | **148** |
| Vazios (sem nenhum commit) | 13 |
| Sem acesso nesta sessão (privados não anexados) | 89 |
| Branches varridos | 3522 |
| Arquivos distintos (por conteúdo) | 34085 |
| Lean / Coq / Agda / Isabelle | 7842 / 696 / 231 / 457 |
| Python (+notebooks) / LaTeX | 5229 / 2133 |
| Declarações Lean que concluem um alvo | 829 |
| …sem hipótese explícita, sem sorry/axiom no próprio arquivo | 135: 115 equivalências (↔) + 20 afirmações diretas, revisadas abaixo |
| Enunciados-alvo em Coq/Agda/Isabelle | 546 (447 em arquivos com escapatória) |
| Alegações textuais de fechamento (`CLOSED_MATH = true`, `state := .proved`…) | 31 em 13 repositórios |

## Veredito

Nenhum arquivo, em nenhuma linguagem, em nenhum branch, contém um termo sem hipóteses e sem escapatória que prove o enunciado oficial de qualquer um dos 7 problemas ou uma das obrigações O1–O8. Os resultados "sem hipótese" listados abaixo foram revisados um a um: são alvos definidos localmente como fórmulas triviais, modelos de brinquedo, registros de estado ou o resultado P01 (SAT ∈ NP no modelo do lane). As alegações textuais de fechamento são texto: nenhuma vem acompanhada de um termo que o kernel aceite. `CLOSED_MATH` continua sendo calculado pelo portão do kernel e continua `false`.

## Por repositório (com material de prova)

| Repositório | Branches | Lean | Coq | Agda | Isabelle | Python | LaTeX | Decl. Lean → alvo | sem hip. limpas | Enunc. outros provadores | Alegações textuais |
|---|---|---|---|---|---|---|---|---|---|---|---|
| m-core-p-vs-np | 696 | 1410 | 0 | 0 | 0 | 33 | 0 | 256 | 34 | 0 | 3 |
| m-core-beal | 246 | 367 | 0 | 0 | 0 | 12 | 0 | 111 | 49 | 0 | 1 |
| m-core-hodge | 252 | 323 | 0 | 0 | 0 | 19 | 0 | 71 | 1 | 0 | 1 |
| M-Core | 215 | 609 | 2 | 0 | 2 | 50 | 0 | 69 | 11 | 12 | 10 |
| atk-certified-priority-record | 1 | 466 | 0 | 0 | 0 | 1 | 0 | 67 | 9 | 0 | 2 |
| Millennium | 107 | 510 | 163 | 42 | 82 | 1229 | 352 | 53 | 2 | 199 | 2 |
| m-core-riemann | 175 | 391 | 0 | 0 | 0 | 24 | 8 | 31 | 1 | 0 | 1 |
| millennium-riemann-classical | 7 | 83 | 27 | 4 | 19 | 141 | 85 | 17 | 1 | 9 | 0 |
| Elyon-Public-Proof | 1 | 120 | 0 | 0 | 0 | 4 | 0 | 16 | 3 | 0 | 1 |
| universal-emergent-logic- | 63 | 322 | 36 | 12 | 25 | 669 | 160 | 15 | 2 | 33 | 0 |
| navier-stokes-critical-barrier-audit | 148 | 382 | 13 | 9 | 13 | 52 | 4 | 13 | 0 | 10 | 1 |
| horizon-prime---framework | 24 | 86 | 20 | 15 | 15 | 93 | 63 | 12 | 6 | 46 | 0 |
| atk-math-core-public | 2 | 21 | 0 | 0 | 0 | 0 | 0 | 11 | 1 | 0 | 0 |
| atk-beal-public | 2 | 20 | 0 | 0 | 0 | 2 | 0 | 9 | 3 | 0 | 0 |
| Millennium-rh-energy-torus-quantum | 30 | 18 | 10 | 0 | 7 | 277 | 33 | 9 | 0 | 7 | 0 |
| open-math-scoped-final | 6 | 64 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| millennium-riemann-I | 8 | 77 | 8 | 5 | 6 | 25 | 5 | 7 | 2 | 4 | 0 |
| atk-riemann-public | 2 | 8 | 0 | 0 | 0 | 2 | 0 | 7 | 2 | 0 | 0 |
| atk-bsd-public | 2 | 7 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 0 | 0 |
| atk-p-vs-np-public | 2 | 7 | 0 | 0 | 0 | 3 | 0 | 6 | 2 | 0 | 0 |
| Universe-0-0 | 217 | 207 | 23 | 5 | 13 | 378 | 233 | 5 | 0 | 14 | 0 |
| Heu-7-universal-framework | 7 | 153 | 29 | 0 | 26 | 56 | 88 | 5 | 2 | 8 | 0 |
| m-core-yang-mills | 190 | 227 | 0 | 0 | 0 | 9 | 0 | 4 | 2 | 0 | 1 |
| sfh-formalization-lab | 33 | 33 | 6 | 5 | 6 | 53 | 10 | 4 | 0 | 0 | 0 |
| riemann-transverse-stability-program | 6 | 22 | 2 | 1 | 1 | 28 | 38 | 3 | 2 | 0 | 0 |
| Riemann-multistate-program | 13 | 13 | 4 | 0 | 3 | 66 | 31 | 3 | 0 | 0 | 0 |
| atk-hodge-public | 2 | 12 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| unified-classical-foundations | 3 | 96 | 68 | 0 | 15 | 41 | 4 | 2 | 0 | 10 | 0 |
| Riemann-energy-proofline | 15 | 33 | 17 | 0 | 11 | 59 | 57 | 2 | 0 | 6 | 0 |
| 0-0-FORMAL-SUITE | 8 | 41 | 0 | 0 | 0 | 0 | 8 | 1 | 0 | 0 | 0 |
| cryptographic-logic-foundations | 4 | 34 | 10 | 0 | 7 | 21 | 0 | 1 | 0 | 3 | 0 |
| hawking-singularities-millennium-problems | 1 | 21 | 13 | 0 | 3 | 18 | 20 | 1 | 0 | 3 | 0 |
| atk-navier-stokes-public | 2 | 12 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 1 |
| m-core-bsd | 158 | 227 | 0 | 0 | 0 | 23 | 0 | 0 | 0 | 0 | 1 |
| M-private | 75 | 160 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| Millenium--core | 14 | 114 | 0 | 0 | 1 | 51 | 27 | 0 | 0 | 0 | 0 |
| Meta-millenium-independence-00 | 6 | 112 | 0 | 0 | 0 | 8 | 53 | 0 | 0 | 0 | 0 |
| axiomatic-millenium | 50 | 96 | 0 | 0 | 0 | 37 | 0 | 0 | 0 | 0 | 6 |
| M-Navier-Stokes | 56 | 68 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| indeterminate-collapse-core | 8 | 62 | 2 | 3 | 3 | 27 | 75 | 0 | 0 | 11 | 0 |
| Eclectic_S | 5 | 56 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| Genesis_Elyon | 13 | 54 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 |
| federated-trivalent-manifold | 18 | 52 | 6 | 3 | 5 | 62 | 54 | 0 | 0 | 2 | 0 |
| millennium-birch-swinnerton-dyer-classical | 1 | 51 | 7 | 5 | 6 | 10 | 0 | 0 | 0 | 1 | 0 |
| The-Algebra-of-Ideterminate-I | 7 | 46 | 22 | 9 | 13 | 76 | 69 | 0 | 0 | 0 | 0 |
| emergent-complexity-N-NP | 7 | 37 | 21 | 0 | 21 | 25 | 25 | 0 | 0 | 0 | 0 |
| millennium-p-vs-np-classical | 2 | 35 | 13 | 10 | 14 | 5 | 17 | 0 | 0 | 22 | 0 |
| S5-Core-Private | 13 | 34 | 16 | 7 | 9 | 146 | 2 | 0 | 0 | 10 | 0 |
| Singulariity | 12 | 30 | 10 | 20 | 10 | 48 | 6 | 0 | 0 | 27 | 0 |
| millennium-navier-stokes-classical | 2 | 30 | 23 | 1 | 20 | 11 | 12 | 0 | 0 | 9 | 0 |
| millennium-hodge-classical | 1 | 29 | 5 | 5 | 5 | 9 | 0 | 0 | 0 | 20 | 0 |
| Meta-mathematical-foundation-00 | 5 | 28 | 12 | 1 | 1 | 8 | 47 | 0 | 0 | 3 | 0 |
| universal-arithmetic-stability | 8 | 28 | 19 | 3 | 12 | 14 | 82 | 0 | 0 | 0 | 0 |
| i-constant-core | 4 | 24 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| lc-rh-coercivity | 1 | 21 | 15 | 15 | 15 | 1 | 9 | 0 | 0 | 0 | 0 |
| millennium-yang-mills-classical | 1 | 21 | 20 | 20 | 19 | 3 | 17 | 0 | 0 | 31 | 0 |
| millennium-p-vs-np-I | 14 | 17 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 |
| Trans | 2 | 16 | 3 | 1 | 2 | 121 | 79 | 0 | 0 | 0 | 0 |
| riemann-offcritical-zero-certifier | 1 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| lean-audit-kit | 2 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| collatz_reverse-tree | 67 | 12 | 9 | 8 | 9 | 278 | 14 | 0 | 0 | 14 | 0 |
| meta-mathematics-indeterminate-I | 3 | 12 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 |
| universal-proof-hub | 9 | 11 | 1 | 1 | 1 | 6 | 6 | 0 | 0 | 0 | 0 |
| -millennium-bsd-hodge-yangmills-I | 2 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Lunar-Hive | 28 | 10 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 |
| millennium-hodge | 7 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| millennium-navier-stokes-I | 6 | 10 | 2 | 0 | 2 | 32 | 3 | 0 | 0 | 0 | 0 |
| UMA | 3 | 9 | 8 | 2 | 5 | 62 | 9 | 0 | 0 | 0 | 0 |
| millennium-yang-mills | 4 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Oral-substrate-br | 27 | 8 | 2 | 1 | 2 | 29 | 5 | 0 | 0 | 8 | 0 |
| Riemann-unity-zero | 40 | 7 | 2 | 2 | 2 | 115 | 121 | 0 | 0 | 10 | 0 |
| emergent-identity-rh | 1 | 7 | 5 | 0 | 5 | 4 | 11 | 0 | 0 | 0 | 0 |
| Harappan-guilds-0-0 | 8 | 6 | 4 | 3 | 2 | 12 | 8 | 0 | 0 | 0 | 0 |
| navier-stokes-critical-L3 | 2 | 6 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 |
| millennium-poincare-symbolic | 5 | 5 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| indus-operational-mathematics | 4 | 4 | 3 | 3 | 3 | 112 | 58 | 0 | 0 | 0 | 0 |
| complexity-collapse-pnp | 2 | 3 | 1 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0 |
| millennium-bsd | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| proofs-multiprover | 2 | 3 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| atk-yang-mills-public | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| critical-bridge-formalization-private | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 0 | 0 | 0 | 0 |
| m-core-openai-ns-audit | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| millennium-classical-parameters | 2 | 2 | 1 | 1 | 1 | 3 | 0 | 0 | 0 | 9 | 0 |
| millennium-poincare-classical | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ussf-millennium-locks | 1 | 2 | 2 | 2 | 2 | 17 | 1 | 0 | 0 | 0 | 0 |
| 00-limit-foundation | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Spectrally-Guided | 3 | 1 | 1 | 1 | 1 | 18 | 0 | 0 | 0 | 0 | 0 |
| Universal-translation-0-0 | 68 | 1 | 1 | 1 | 1 | 132 | 9 | 0 | 0 | 0 | 0 |
| continuum-fields-indeterminacy | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| harappan-unified-audit- | 45 | 1 | 0 | 0 | 0 | 38 | 0 | 0 | 0 | 0 | 0 |
| i-theology-unified | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| lean-winwin-logic | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| millennium-symbolic-program | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| navier-stokes-noncircular | 4 | 1 | 1 | 1 | 1 | 3 | 19 | 0 | 0 | 0 | 0 |
| pi-border-primes | 62 | 1 | 1 | 0 | 1 | 104 | 16 | 0 | 0 | 0 | 0 |
| riemann-indeterminacy | 5 | 1 | 1 | 0 | 1 | 9 | 42 | 0 | 0 | 0 | 0 |
| seet-r-off-lab- | 13 | 1 | 1 | 1 | 1 | 16 | 0 | 0 | 0 | 5 | 0 |

Outros 51 repositórios varridos não têm arquivo de assistente de prova nem alegação de fechamento (documentação, dados, código de aplicação): -sbfe-physics-unified, 0-0, Beit-Hamikdash-iii, Codex_Indeterminancy, Horizon_Prime_-framework, I-Framework-Nexus, Indus-System, Millenium-delta-unified-frame, NIPAH-research-HUB, S5-BIO-SHIELD-, The-Proof-Log, Zero--OS, archetypes-humanity, cardinality-and-infinity, closed-loop-engineering-00, consciousness-symbolic-model-00, cosmic-geometry-00, discrete-dynamics-indeterminacy, dmt-timelines-00, equations-of-unsolved-problems-book, global-systems-lab, hawking-bsd, hawking-framework, hawking-hodge, hawking-lean, hawking-ns, hawking-numerics, hawking-pnp, hawking-rh, hawking-ym, latex-library-global, lean-cursor-shuttle, lean-fin-composition, lean-preserving-read, lean-refinement-bridge, lean-uniform-bounds, metalogic-infinity-00, millennium-engineering-00, millennium-hypothesi, millennium-mass-gap-I, millennium-regularity-I, millennium-research-os, proof-engineering-00, quantum-axioms-lab, symbolic-analysis-00, symbolic-arithmetic-00, symbolic-complexity-00, symbolic-metamathematics-00, symbolic-topology-00, tiago-fagliari-creative-technical-portfolio, tiefc-audit-lab.

## Afirmações diretas sem hipótese explícita — revisão uma a uma

O scanner só vê `axiom` no próprio arquivo e hipóteses entre parênteses. Por isso cada afirmação direta foi aberta e lida.

| Repositório | Declaração | Conclusão | Onde | Revisão |
|---|---|---|---|---|
| M-Core | `rh_material_vacuous` | `ConcreteUniformLogDNBound (fun _ => 0)` | `atk-kernel-check`:`atk-kernel/ATK/LogicAudit.lean` | firewall: D_N ≡ 0 satisfaz a cota trivialmente — mostra que o alvo precisa estar ligado ao D_N concreto |
| M-Core | `positive_rh_incompatible_with_negative_lane` | `RiemannHypothesis → ¬ Nonempty RiemannInterpretation` | `atk/global-material-frontier-20261001`:`lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean` | implicação (RH → …), não prova de RH |
| m-core-p-vs-np | `(example)` | `Nonempty P01MachineConstruction` | `atk-kernel-check`:`probe/P01MachineConstructionExpectedFailure.lean` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| m-core-p-vs-np | `p01ConstructionGap` | `P01ConstructionGap` | `atk/p01-material-inhabitant-frontier-20260930`:`lean/MCore/Real/P01TerminalCertificate.lean` | P01: idem |
| m-core-p-vs-np | `p01_closed_no_hypothesis` | `P01ConstructionGap` | `atk/p01-terminal-promotion-candidate-20260930`:`lean/MCore/Real/P01TerminalMaterialCertificate.lean` | P01: idem |
| m-core-p-vs-np | `(example)` | `P01MachineConstruction` | `work/pnp-minimal-separation-20261005`:`lean/MCore/PNPMaterialAtoms.lean` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| m-core-hodge | `concretePayload_vacuous_on_empty_model` | `ConcreteAlgebraicityPayload emptyCycleSpanMechanics` | `atk/concrete-payload-model-binding-audit`:`audit/ATK_CONCRETE_PAYLOAD_MODEL_BINDING_COUNTERAUDIT.lean` | firewall: modelo vazio torna o payload de Hodge vácuo |
| m-core-yang-mills | `toyB60ConcretePhysicalAdapter` | `B60ConcretePhysicalAdapter toyConstruction toyK20Frontier toyPhysicalHilbert toy` | `atk/b60-triviality-audit`:`lean/MCore/YangMills/A1/B60TrivialityAudit.lean` | firewall: modelo degenerado habita o adaptador B60 de Yang–Mills |
| m-core-yang-mills | `b60_inhabited_by_degenerate_model` | `Nonempty (B60ConcretePhysicalAdapter toyConstruction toyK20Frontier toyPhysicalH` | `atk/b60-triviality-audit`:`lean/MCore/YangMills/A1/B60TrivialityAudit.lean` | firewall: idem |
| atk-certified-priority-record | `(example)` | `Nonempty P01MachineConstruction` | `main`:`snapshots/m-core-p-vs-np/probe/P01MachineConstructionExpectedFailure.lean` | P01: SAT ∈ NP no modelo de máquina do lane P vs NP (resultado genuíno, mas não é P ≠ NP) |
| millennium-riemann-I | `riemann_hypothesis` | `RiemannHypothesis` | `atk-rh-g21-mold`:`src/Riemann/CollapseProof/Contradiction.lean` | depende de `axiom collapse_law` e `axiom I_ne_one` declarados em outro arquivo (RH reescrita); o próprio branch atk/label-circular-rh-20261008 a rotula como circular |
| millennium-riemann-I | `riemann_hypothesis` | `RiemannHypothesis` | `atk/label-circular-rh-20261008`:`src/Riemann/CollapseProof/Contradiction.lean` | depende de `axiom collapse_law` e `axiom I_ne_one` declarados em outro arquivo (RH reescrita); o próprio branch atk/label-circular-rh-20261008 a rotula como circular |
| horizon-prime---framework | `all_millennium_problems` | `RiemannHypothesis ∧ PneqNP ∧ YangMillsMassGap ∧ NavierStokesRegularity ∧ HodgeCo` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/All.lean` | importa `Gaps/*.lean` e `HorizonPrime/ProfiniteUniformity.lean`, que declaram `axiom zero_density_uniform`, `axiom explicit_formula_uniform_error` e até os objetos (`axiom EllipticCurve : Type`…); os alvos são `def` locais |
| horizon-prime---framework | `BSD_final` | `BSDConjecture` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/BSD_final.lean` | idem (axiomas importados) |
| horizon-prime---framework | `Hodge_final` | `HodgeConjecture` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/Hodge_final.lean` | idem (axiomas importados) |
| horizon-prime---framework | `PneqNP_final` | `PneqNP` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/PvsNP_final.lean` | idem (axiomas importados) |
| horizon-prime---framework | `RH_final` | `RiemannHypothesis` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/RH_final.lean` | idem (axiomas importados de Gaps/RH_ZD_UEF.lean) |
| horizon-prime---framework | `YM_final` | `YangMillsMassGap` | `copilot/formalize-final-theorem`:`formal/lean/FinalTheorems/YM_final.lean` | idem (axiomas importados) |
| universal-emergent-logic- | `UETheta_implies_RH` | `RiemannHypothesis` | `ShantiDraconis-patch-1`:`formalization/lean/UETheta_to_RH.lean` | `def RiemannHypothesis : Prop := True` no próprio arquivo — vácuo |
| universal-emergent-logic- | `MasterTheorem` | `RiemannHypothesis ∧ GRH ∧ HardyLittlewood_k_tuple ∧ BatemanHorn ∧ GoldbachWeak` | `ShantiDraconis-patch-1`:`src/lean/EmergentTheta/Main/MasterTheorem.lean` | hipótese de classe `[UniversalThetaFramework]` e axiomas nos arquivos *FromUT.lean importados |

As outras 115 são equivalências (`Alvo ↔ Reformulação`): transportam o problema, não o resolvem. Lista completa em `inventory.json`.


## Coq/Rocq, Agda, Isabelle — enunciados que mencionam os problemas

447 dos 546 estão em arquivos com `Admitted`/`Axiom`/`Parameter`/`postulate`/`sorry`. Os demais foram lidos: são condicionais (`CookLevin → SATnotP → PneqNP`, `StoneLemma ⟶ P_neq_NP`), equivalências (`RiemannHypothesis ↔ …`), enunciados `True`, contas sobre definições locais (`Omega S_cl p ≥ 3`) ou registros de autoria. Nenhum prova um enunciado oficial.

| Repositório | Linguagem | Nome | Enunciado | Escapatórias no arquivo | Onde |
|---|---|---|---|---|---|
| M-Core | Coq/Rocq | `global_projects_pnp` | `: forall (T : SevenTerminalTypes) (B : SevenInhabitants T), PNP T` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/coq/ATKSevenLanes.v` |
| M-Core | Coq/Rocq | `global_projects_bsd` | `: forall (T : SevenTerminalTypes) (B : SevenInhabitants T), BSD T` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/coq/ATKSevenLanes.v` |
| M-Core | Coq/Rocq | `global_projects_hodge` | `: forall (T : SevenTerminalTypes) (B : SevenInhabitants T), Hodge T` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/coq/ATKSevenLanes.v` |
| M-Core | Coq/Rocq | `global_projects_beal` | `: forall (T : SevenTerminalTypes) (B : SevenInhabitants T), Beal T` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/coq/ATKSevenLanes.v` |
| M-Core | Coq/Rocq | `global_iff_seven_inputs` | `: forall (T : SevenTerminalTypes), (exists B : SevenInhabitants T, True) <-> (exists hRH :` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/coq/ATKSevenLanes.v` |
| M-Core | Isabelle | `build_seven_projects_rh` | `"rh_of (build_seven rh pnp ym ns bsd hodge beal) = rh"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_pnp` | `"pnp_of (build_seven rh pnp ym ns bsd hodge beal) = pnp"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_ym` | `"ym_of (build_seven rh pnp ym ns bsd hodge beal) = ym"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_ns` | `"ns_of (build_seven rh pnp ym ns bsd hodge beal) = ns"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_bsd` | `"bsd_of (build_seven rh pnp ym ns bsd hodge beal) = bsd"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_hodge` | `"hodge_of (build_seven rh pnp ym ns bsd hodge beal) = hodge"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| M-Core | Isabelle | `build_seven_projects_beal` | `"beal_of (build_seven rh pnp ym ns bsd hodge beal) = beal"` | — | `atk/cross-prover-terminal-closure-20261001`:`formal/isabelle/ATK_Seven_Lanes.thy` |
| navier-stokes-critical-barrier-audit | Agda | `PNP-closure` | `(P : PNPTarget) → CookLevin P → SATnotP P → PneqNP P` | — | `a2.1-weightedIBP`:`formal/agda/ClosureTargetTree.agda` |
| navier-stokes-critical-barrier-audit | Agda | `BSD-closure` | `(P : BSDTarget) → RankBridge P → LeadingCoefficientBridge P → BSD P` | — | `a2.1-weightedIBP`:`formal/agda/ClosureTargetTree.agda` |
| navier-stokes-critical-barrier-audit | Agda | `Hodge-closure` | `(P : HodgeTarget) → CycleBridge P → Hodge P` | — | `a2.1-weightedIBP`:`formal/agda/ClosureTargetTree.agda` |
| navier-stokes-critical-barrier-audit | Coq/Rocq | `PNP_chain` | `: forall P : PNPTarget, CookLevin P -> SATnotP P -> PneqNP P` | — | `a2.1-weightedIBP`:`formal/coq/ClosureTargetTree.v` |
| navier-stokes-critical-barrier-audit | Coq/Rocq | `BSD_chain` | `: forall B : BSDTarget, RankBridge B -> LeadingCoefficientBridge B -> BSD B` | — | `a2.1-weightedIBP`:`formal/coq/ClosureTargetTree.v` |
| navier-stokes-critical-barrier-audit | Coq/Rocq | `Hodge_chain` | `: forall H : HodgeTarget, CycleClassBridge H -> Hodge H` | — | `a2.1-weightedIBP`:`formal/coq/ClosureTargetTree.v` |
| navier-stokes-critical-barrier-audit | Coq/Rocq | `YM_chain` | `: forall Y : YMTarget, ConstructiveContinuumQFT Y -> OsterwalderSchrader Y -> PositiveMass` | — | `a2.1-weightedIBP`:`formal/coq/ClosureTargetTree.v` |
| navier-stokes-critical-barrier-audit | Isabelle | `PNP_closure` | `"CookLevin ⟹ SATnotP ⟹ PneqNP"` | — | `a2.1-weightedIBP`:`formal/isabelle/Closure_Target_Tree.thy` |
| navier-stokes-critical-barrier-audit | Isabelle | `BSD_closure` | `"RankBridge ⟹ LeadingCoefficientBridge ⟹ BSD"` | — | `a2.1-weightedIBP`:`formal/isabelle/Closure_Target_Tree.thy` |
| navier-stokes-critical-barrier-audit | Isabelle | `Hodge_closure` | `"CycleClassBridge ⟹ Hodge"` | — | `a2.1-weightedIBP`:`formal/isabelle/Closure_Target_Tree.thy` |
| millennium-riemann-I | Coq/Rocq | `zeros_satisfy_integral_equation` | `: forall s : CollapseComplex, isSymbolicZero s <-> zeta_integral_representation s == CC_ze` | Axiom | `atk-rh-g21-mold`:`coq/Millennium/Riemann/Zeros/Nontrivial.v` |
| millennium-riemann-I | Agda | `default-params` | `ZetaKernelParams` | 




postulate, 


postulate | `atk-rh-g21-mold`:`cross/agda/AnomalousZeros.agda` |
| millennium-riemann-I | Agda | `functional` | `ZetaKernelParams → INumber → Float` | 




postulate, 


postulate | `atk-rh-g21-mold`:`cross/agda/AnomalousZeros.agda` |
| millennium-riemann-I | Isabelle | `zeros_satisfy_integral_equation` | `"isSymbolicZero s \<longleftrightarrow> zeta_integral_representation s = CC_zero"` | axiomatization, sorry | `atk-rh-g21-mold`:`isabelle/Millennium/Riemann/Zeros/Nontrivial.thy` |
| horizon-prime---framework | Isabelle | `riemann_hypothesis_conditional` | `assumes "HorizonEquidistribution" "ZeroDensityBound" "UniformExplicitFormula"` | axiomatization, sorry | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.thy` |
| horizon-prime---framework | Isabelle | `yang_mills_conditional` | `assumes "UniformReflectionPositivity" "ClusterExpansionStability"` | axiomatization, sorry | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.thy` |
| horizon-prime---framework | Isabelle | `navier_stokes_conditional` | `assumes "EnergyEnstrophyUniformBounds" "CriticalContinuation"` | axiomatization, sorry | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.thy` |
| horizon-prime---framework | Isabelle | `hodge_conditional` | `assumes "TateOnPi" "EquidistributionPi"` | axiomatization, sorry | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.thy` |
| horizon-prime---framework | Coq/Rocq | `riemann_hypothesis_conditional` | `: HorizonEquidistribution -> ZeroDensityBound -> UniformExplicitFormula -> forall s : Comp` | , Axiom, Parameter | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.v` |
| horizon-prime---framework | Coq/Rocq | `yang_mills_conditional` | `: UniformReflectionPositivity -> ClusterExpansionStability -> exists Delta : R, (Delta > 0` | , Axiom, Parameter | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.v` |
| horizon-prime---framework | Coq/Rocq | `navier_stokes_conditional` | `: EnergyEnstrophyUniformBounds -> CriticalContinuation -> GlobalRegularity` | , Axiom, Parameter | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.v` |
| horizon-prime---framework | Coq/Rocq | `hodge_conditional` | `: TateOnPi -> EquidistributionPi -> forall X : ProjectiveVariety, HodgeConjectureHolds X` | , Axiom, Parameter | `copilot/add-hodge-conjecture-reduction`:`HorizonPrime.v` |
| horizon-prime---framework | Coq/Rocq | `riemann_hypothesis_via_collapse` | `: forall s : C, True -> True` | , Axiom | `copilot/add-hyperprime-existence-study`:`formal_verification/coq/HorizonPrime.v` |
| horizon-prime---framework | Coq/Rocq | `p_neq_np_via_collapse` | `: exists collapse : ComplexityClass, collapse = CollapseClass /\ P <> NP` | , Axiom | `copilot/add-hyperprime-existence-study`:`formal_verification/coq/HorizonPrime.v` |
| horizon-prime---framework | Isabelle | `riemann_hypothesis_via_collapse` | `assumes "True"` | axiomatization, sorry | `copilot/add-hyperprime-existence-study`:`formal_verification/isabelle/HorizonPrime.thy` |
| horizon-prime---framework | Isabelle | `p_neq_np_via_collapse` | `shows "\<exists>collapse. collapse = CollapseClass \<and> P \<noteq> NP"` | axiomatization, sorry | `copilot/add-hyperprime-existence-study`:`formal_verification/isabelle/HorizonPrime.thy` |
| horizon-prime---framework | Agda | `hodge-component-1` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `hodge-component-2` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `hodge-component-3` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `hodge-components` | `List ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `hodge-proof` | `StructuredProof` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `lambda-pi-Hodge` | `CompletenessParameter` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `bsd-component-1` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `bsd-component-2` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `bsd-component-3` | `ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `bsd-components` | `List ProofComponent` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `bsd-proof` | `StructuredProof` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Agda | `lambda-pi-BSD` | `CompletenessParameter` | 



postulate, 

postulate, 
postulate, postulate | `copilot/clarify-mathematical-parameters`:`formal_verification/agda/LambdaPi.agda` |
| horizon-prime---framework | Coq/Rocq | `hodge_tate_coupling` | `: value lambda_pi_Hodge >= 0.5` | — | `copilot/clarify-mathematical-parameters`:`formal_verification/coq/LambdaPi.v` |
| horizon-prime---framework | Coq/Rocq | `millennium_problems_structured` | `: forall (problem : StructuredProof), (length (components problem) > 1)%nat -> exists c, I` | — | `copilot/clarify-mathematical-parameters`:`formal_verification/coq/LambdaPi.v` |
| horizon-prime---framework | Coq/Rocq | `millennium_problems_implicit_deficit` | `: forall problem, In problem [rh_proof; pvsnp_proof; ym_proof; ns_proof; hodge_proof; bsd_` | — | `copilot/clarify-mathematical-parameters`:`formal_verification/coq/LambdaPi.v` |
| horizon-prime---framework | Isabelle | `hodge_tate_coupling` | `"lambda_pi_Hodge \<ge> 0.5"` | sorry | `copilot/clarify-mathematical-parameters`:`formal_verification/isabelle/LambdaPi.thy` |
| horizon-prime---framework | Isabelle | `millennium_problems_structured` | `assumes "length (components problem) > 1"` | sorry | `copilot/clarify-mathematical-parameters`:`formal_verification/isabelle/LambdaPi.thy` |
| horizon-prime---framework | Isabelle | `millennium_problems_implicit_deficit` | `assumes "problem \<in> set [rh_proof, pvsnp_proof_struct, ym_proof,` | sorry | `copilot/clarify-mathematical-parameters`:`formal_verification/isabelle/LambdaPi.thy` |
| horizon-prime---framework | Coq/Rocq | `riemannHypothesis_incomplete` | `: (0 < completionDeficit riemannHypothesisRequirements)%R` | , Axiom | `copilot/clarify-scope-requirements`:`coq/CompletionDeficit.v` |
| horizon-prime---framework | Isabelle | `riemannHypothesis_incomplete` | `"completionDeficit riemannHypothesisRequirements > 0"` | sorry | `copilot/clarify-scope-requirements`:`isabelle/CompletionDeficit.thy` |
| horizon-prime---framework | Coq/Rocq | `hodge_conjecture_CONDITIONAL` | `: forall (X : ProjectiveVariety) (k : nat) (alpha : HodgeClass X k), exists (cycles : Rati` | , Axiom, Parameter | `copilot/define-accepted-proof-criteria`:`formal_verification/coq/FinalTheorem_Hodge.v` |
| horizon-prime---framework | Coq/Rocq | `navier_stokes_global_regularity_CONDITIONAL` | `: forall (u0 : VelocityField), True -> exists (sol : NavierStokesSolution), forall (t : R)` | , Axiom, Parameter | `copilot/define-accepted-proof-criteria`:`formal_verification/coq/FinalTheorem_NS.v` |
| horizon-prime---framework | Coq/Rocq | `p_neq_np_CONDITIONAL` | `: exists (L : Language), NP L /\ ~(P L)` | , Axiom, Parameter | `copilot/define-accepted-proof-criteria`:`formal_verification/coq/FinalTheorem_PvsNP.v` |
| horizon-prime---framework | Coq/Rocq | `riemann_hypothesis_CONDITIONAL` | `: forall (s : C), is_nontrivial_zero s -> critical_line s` | , Axiom, Parameter | `copilot/define-accepted-proof-criteria`:`formal_verification/coq/FinalTheorem_RH.v` |
| horizon-prime---framework | Coq/Rocq | `yang_mills_mass_gap_CONDITIONAL` | `: exists (Delta : R), Delta > 0 /\ forall (theory : nat), mass_gap theory >= Delta` | , Axiom, Parameter | `copilot/define-accepted-proof-criteria`:`formal_verification/coq/FinalTheorem_YM.v` |
| horizon-prime---framework | Isabelle | `hodge_conjecture_CONDITIONAL` | `"\<forall>X k \<alpha>. \<exists>cycles. True"` | axiomatization, oops | `copilot/define-accepted-proof-criteria`:`formal_verification/isabelle/FinalTheorem_Hodge.thy` |
| horizon-prime---framework | Isabelle | `navier_stokes_global_regularity_CONDITIONAL` | `"\<forall>u0. \<exists>sol. \<forall>t\<ge>0. energy sol t < \<infinity>"` | axiomatization, oops | `copilot/define-accepted-proof-criteria`:`formal_verification/isabelle/FinalTheorem_NS.thy` |
| horizon-prime---framework | Isabelle | `p_neq_np_CONDITIONAL` | `"\<exists>L. NP L \<and> \<not>P L"` | axiomatization, oops | `copilot/define-accepted-proof-criteria`:`formal_verification/isabelle/FinalTheorem_PvsNP.thy` |
| horizon-prime---framework | Isabelle | `riemann_hypothesis_CONDITIONAL` | `assumes "is_nontrivial_zero s"` | axiomatization, oops | `copilot/define-accepted-proof-criteria`:`formal_verification/isabelle/FinalTheorem_RH.thy` |
| horizon-prime---framework | Isabelle | `yang_mills_mass_gap_CONDITIONAL` | `"\<exists>\<Delta>>0. \<forall>theory. mass_gap theory \<ge> \<Delta>"` | axiomatization, oops | `copilot/define-accepted-proof-criteria`:`formal_verification/isabelle/FinalTheorem_YM.thy` |
| horizon-prime---framework | Agda | `riemannHypothesisReqs` | `RequirementSet` | 

postulate | `copilot/formalize-logic-with-lean`:`agda/MillenniumAudit.agda` |
| horizon-prime---framework | Agda | `yangMillsReqs` | `RequirementSet` | 

postulate | `copilot/formalize-logic-with-lean`:`agda/MillenniumAudit.agda` |
| horizon-prime---framework | Agda | `navierStokesReqs` | `RequirementSet` | 

postulate | `copilot/formalize-logic-with-lean`:`agda/MillenniumAudit.agda` |
| horizon-prime---framework | Agda | `hodgeConjectureReqs` | `RequirementSet` | 

postulate | `copilot/formalize-logic-with-lean`:`agda/MillenniumAudit.agda` |
| Millennium | Agda | `PNP-local` | `NP-Problem → ℝ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `PNP-invariant` | `NP-Problem → ℝ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Framework-PNP` | `Framework` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `PNP-has-bridge` | `HasBridge Framework-PNP` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `BSD-local` | `EllipticCurve → ℤ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `BSD-invariant` | `EllipticCurve → ℤ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Framework-BSD` | `Framework` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Hodge-local` | `HodgeClass → ℝ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Hodge-invariant` | `HodgeClass → ℝ` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Framework-Hodge` | `Framework` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `Hodge-has-bridge` | `HasBridge Framework-Hodge` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `framework-consistency` | `HasBridge Framework-PNP × HasBridge Framework-NS ×` | 




postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/Framework.agda` |
| Millennium | Agda | `at-least-one-true` | `∃[ i ] MillenniumConjecture i` | 





postulate, 




 

postulate, 
 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/LocalGlobalFramework.agda` |
| Millennium | Agda | `L_ρ` | `ZetaZero → NPLanguage` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `balance` | `ZetaZero → ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `balance-zero` | `(ρ : ZetaZero) → balance ρ ≡ 0ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `vertical-transfer` | `(ρ : ZetaZero) → delta_RH ρ ≡ 0ℝ → delta_NP (L_ρ ρ) ≡ 0ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `horizontal-transfer` | `(ρ : ZetaZero) → delta_RH ρ ≡ 0ℝ → delta_NP (L_ρ ρ) ≡ 0ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `in-paired-variety` | `ZetaZero → Set` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `all-in-variety` | `(ρ : ZetaZero) → in-paired-variety ρ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `gap-point` | `ZetaZero → GapPoint` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `gap-point-on-diagonal` | `(ρ : ZetaZero) → on-diagonal (gap-point ρ)` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `RH-implies-images-in-P` | `RH-holds → (ρ : ZetaZero) → delta_NP (L_ρ ρ) ≡ 0ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `gap-sign-symmetry` | `(ρ : ZetaZero) → sgn (delta_RH ρ) ≡ sgn (delta_NP (L_ρ ρ))` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `gap-magnitude-symmetry` | `(ρ : ZetaZero) → abs (delta_RH ρ) ≡ abs (delta_NP (L_ρ ρ))` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `ZeroFiber` | `ZetaZero → NPLanguage → Set` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `LanguageFiber` | `NPLanguage → ZetaZero → Set` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `image-in-zero-fiber` | `(ρ : ZetaZero) → ZeroFiber ρ (L_ρ ρ)` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `zero-in-language-fiber` | `(ρ : ZetaZero) → LanguageFiber (L_ρ ρ) ρ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `delta-RH-well-defined` | `(ρ : ZetaZero) → ∃[ x ] (delta_RH ρ ≡ x)` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `balance-well-defined` | `(ρ : ZetaZero) → ∃[ x ] (balance ρ ≡ x)` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `framework-consistent` | `(ρ : ZetaZero) → balance ρ ≡ 0ℝ` | 





postulate, 

postulate, postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/ParityGap.agda` |
| Millennium | Agda | `PvsNP-to-BSD` | `Set` | 





postulate, 

postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/UnificationTheorem.agda` |
| Millennium | Agda | `BSD-to-Hodge` | `Set` | 





postulate, 

postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/UnificationTheorem.agda` |
| Millennium | Agda | `Hodge-to-Poincare` | `Set` | 





postulate, 

postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/UnificationTheorem.agda` |
| Millennium | Agda | `seven-problem-cycle` | `RH-to-NS × NS-to-YM × YM-to-PvsNP × PvsNP-to-BSD ×` | 





postulate, 

postulate | `attack/poincare-f7-f8-multistate-20260926`:`agda/UnificationTheorem.agda` |
| Millennium | Coq/Rocq | `Theorem1` | `(f : BoundingFunction) : Conjecture1 f -> Conjecture2 -> ((forall rho, In C ZetaZeros rho ` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/DeltaGap44.v` |
| Millennium | Coq/Rocq | `exponential_gaps_follow_from_p_ne_np` | `: forall ir, P_ne_NP (ir_languages ir) -> exponential_gaps_exist ir` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/DeltaGap44/Theorems.v` |
| Millennium | Coq/Rocq | `framework_models_independence` | `: forall ir, RH_false (ir_zeros ir) -> P_ne_NP (ir_languages ir) -> classifyRegime true tr` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/DeltaGap44/Theorems.v` |
| Millennium | Coq/Rocq | `seven_problems` | `: length allMillenniumProblems = 7%nat` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/GapUniversal.v` |
| Millennium | Coq/Rocq | `gap_universal_unification` | `: forall (GU : GapUniversalStructure), GapUniversalConjecture GU -> forall p q : Millenniu` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/GapUniversal.v` |
| Millennium | Coq/Rocq | `problem_decidable` | `: forall p q : MillenniumProblem, {p = q} + {p <> q}` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/GapUniversal.v` |
| Millennium | Coq/Rocq | `partition_size_5` | `: forall p1 p2 p3 p4 p5 : MillenniumPartition, p1 = P_Computational -> p2 = P_Spectral -> ` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/NonUnification/NonUnification.v` |
| Millennium | Coq/Rocq | `solutionTypesDistinct` | `: forall d1 d2 : MillenniumDomain, d1 <> d2 -> solutionTypeOf d1 <> solutionTypeOf d2` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/NonUnification/NonUnification.v` |
| Millennium | Coq/Rocq | `nonUnificationMetaTheorem` | `: forall d1 d2 : MillenniumDomain, partitionOf d1 <> partitionOf d2 -> millenniumNonUnify ` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/NonUnification/NonUnification.v` |
| Millennium | Coq/Rocq | `methodologicalSeparation` | `: forall d1 d2 : MillenniumDomain, partitionOf d1 <> partitionOf d2 -> solutionTypeOf d1 <` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/NonUnification/NonUnification.v` |
| Millennium | Coq/Rocq | `zero_obstruction_implies_params_one` | `: forall w S p, (w_alpha w > 0) -> (w_beta w > 0) -> (w_gamma w > 0) -> (w_delta w > 0) ->` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ObstructionOperator.v` |
| Millennium | Coq/Rocq | `balance_zero` | `: forall (rho : ZetaZero), balance rho = 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `vertical_transfer` | `: forall (rho : ZetaZero), delta_RH rho = 0 -> delta_NP (L_rho rho) = 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `horizontal_transfer` | `: forall (rho : ZetaZero), delta_NP (L_rho rho) <> 0 -> delta_RH rho <> 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `all_in_variety` | `: forall (rho : ZetaZero), in_paired_variety rho` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `gap_point_on_diagonal` | `: forall (rho : ZetaZero), on_diagonal (delta_RH rho, delta_NP (L_rho rho))` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `RH_implies_images_in_P` | `: RH_holds -> forall (rho : ZetaZero), delta_NP (L_rho rho) = 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `gap_sign_symmetry` | `: forall (rho : ZetaZero), (delta_RH rho > 0 <-> delta_NP (L_rho rho) > 0) /\ (delta_RH rh` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `delta_RH_well_defined` | `: forall (rho : ZetaZero), exists x : R, delta_RH rho = x` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `balance_well_defined` | `: forall (rho : ZetaZero), exists x : R, balance rho = x` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `variety_nonempty` | `: exists (rho : ZetaZero), in_paired_variety rho` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `balance_invariant` | `: forall (rho : ZetaZero), balance rho = balance rho` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/ParityGap.v` |
| Millennium | Coq/Rocq | `delta_Hodge_nonneg` | `: forall hp : HodgePair, delta_Hodge hp >= 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Problems/Hodge.v` |
| Millennium | Coq/Rocq | `delta_Hodge_zero_iff` | `: forall hp : HodgePair, delta_Hodge hp = 0 <-> is_algebraic (hp_manifold hp) (hp_class hp` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Problems/Hodge.v` |
| Millennium | Coq/Rocq | `Hodge_delta_equivalence` | `: Hodge_Conjecture <-> problem_true Hodge_DeltaOp` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Problems/Hodge.v` |
| Millennium | Coq/Rocq | `mass_gap_delta_nonneg` | `: mass_gap_exists -> forall cfg : YMConfig, delta_YM cfg >= 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Problems/YangMills.v` |
| Millennium | Coq/Rocq | `YM_delta_equivalence` | `: YM_Mass_Gap_Problem <-> (forall cfg : YMConfig, YM_critical cfg -> delta_YM cfg >= 0)` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Problems/YangMills.v` |
| Millennium | Coq/Rocq | `Hodge_unification` | `: (WeakSol S_new P4 <-> StrongSol S_new P4) /\ Omega_eq S_new P4 = 0` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/SOF/UnificationTheorem.v` |
| Millennium | Coq/Rocq | `YangMills_unification` | `: (WeakSol S_new P6 <-> StrongSol S_new P6) /\ Omega_eq S_new P6 = 0` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/SOF/UnificationTheorem.v` |
| Millennium | Coq/Rocq | `inadequacy_theorem` | `: forall (S : ClassicalMathematics) (p : MillenniumProblem), ~ exists (sol : StrongSolutio` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralInadequacy.v` |
| Millennium | Coq/Rocq | `laws_imply_inadequacy` | `: all_structural_laws -> forall (S : ClassicalMathematics) (p : MillenniumProblem), ~ exis` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralInadequacy.v` |
| Millennium | Coq/Rocq | `Omega_nonneg` | `: forall (w : Weights) (S : MathSystem) (p : MillenniumProblem), 0 <= Omega w S p` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralObstruction.v` |
| Millennium | Coq/Rocq | `Omega_upper` | `: forall (w : Weights) (S : MathSystem) (p : MillenniumProblem), Omega w S p <= 1` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralObstruction.v` |
| Millennium | Coq/Rocq | `StructuralObstructionTheorem` | `: forall (w : Weights) (p : MillenniumProblem), ~ StrongSol p ClassicalSystem` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralObstruction.v` |
| Millennium | Coq/Rocq | `NoStrongSolutionForAnyProblem` | `: forall (w : Weights) (p : MillenniumProblem), In p AllProblems -> ~ StrongSol p Classica` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/StructuralObstruction.v` |
| Millennium | Coq/Rocq | `seven_problem_cycle` | `: RH_to_NS /\ NS_to_YM /\ YM_to_PvsNP /\ PvsNP_to_BSD /\ BSD_to_Hodge /\ Hodge_to_Poincare` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/UnificationTheorem.v` |
| Millennium | Coq/Rocq | `Omega_S_cl_positive` | `: forall p : MillenniumProblem, Omega S_cl p > 0` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/ClassicalOperators.v` |
| Millennium | Coq/Rocq | `no_strong_solution_in_classical` | `: forall p : MillenniumProblem, ~ StrongSolution_p S_cl p` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/ClassicalOperators.v` |
| Millennium | Coq/Rocq | `no_strong_solution_BSD` | `: ~ StrongSolution_p S_cl BSD` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/ClassicalOperators.v` |
| Millennium | Coq/Rocq | `no_strong_solution_Hodge` | `: ~ StrongSolution_p S_cl Hodge` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/ClassicalOperators.v` |
| Millennium | Coq/Rocq | `Hodge_bridge_equivalence` | `: Hodge_true <-> (HasBridge Framework_Hodge /\ forall alpha : HodgeClass, Hodge_invariant ` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/Framework.v` |
| Millennium | Coq/Rocq | `YM_bridge_equivalence` | `: YM_mass_gap <-> (HasBridge Framework_YM /\ exists A : GaugeField, YM_invariant A > 0)` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/Framework.v` |
| Millennium | Coq/Rocq | `at_least_one_true` | `: exists i : MillenniumIndex, MillenniumConjecture i` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/LocalGlobalFramework.v` |
| Millennium | Coq/Rocq | `conjecture_bridge_equiv` | `: forall i : MillenniumIndex, select_conjecture i <-> Bridge_i i` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/MetaTheorem.v` |
| Millennium | Coq/Rocq | `MetaTheorem_MillenniumProblems` | `: AllBridges <-> AllConjectures` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/MetaTheorem.v` |
| Millennium | Coq/Rocq | `at_least_one_solved` | `: exists i : MillenniumIndex, select_conjecture i` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/MetaTheorem.v` |
| Millennium | Coq/Rocq | `at_least_one_bridge` | `: exists i : MillenniumIndex, Bridge_i i` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/MetaTheorem.v` |
| Millennium | Coq/Rocq | `all_solved_from_bridges` | `: AllBridges -> C_RH /\ C_NS /\ C_PvsNP /\ C_BSD /\ C_Hodge /\ C_YM /\ C_Poincare` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/MetaTheorem.v` |
| Millennium | Coq/Rocq | `millennium_unified` | `: forall (S_cl : ClassicalSystem) (S_exp : ExpandedSystem) (S_new : UnifiedNewSystem) (mp ` | , Axiom, Axioms, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/UnifiedSystem.v` |
| Millennium | Coq/Rocq | `problems_unified_theory` | `: forall (U : UnifiedSystem) (p : Problem), In p MillenniumProblems -> Obstruction (expand` | , Axiom, Axioms, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/UnifiedSystem.v` |
| Millennium | Coq/Rocq | `all_problems_delta_equiv` | `: (RH_holds <-> problem_true RH_DeltaOp) /\ (P_equals_NP <-> problem_true PNP_DeltaOp) /\ ` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/UnifiedTheorem.v` |
| Millennium | Coq/Rocq | `delta_independence` | `: forall x : GlobalPoint, vec_Delta x = mkR7 (delta_RH (gp_RH x)) (delta_PNP (gp_PNP x)) (` | Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/Unified/VectorDelta.v` |
| Millennium | Coq/Rocq | `canonical_satisfies_blocks` | `: RH_block canonical_parameters /\ NS_block canonical_parameters /\ PNP_block canonical_pa` | — | `attack/poincare-f7-f8-multistate-20260926`:`coq/UnifiedTheory/UnifiedCore.v` |
| Millennium | Coq/Rocq | `rh_certificate` | `: forall (rh : RH_Structure), RiemannHypothesis <-> is_finite (K_RH rh)` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/UniversalCriticalFunctional.v` |
| Millennium | Coq/Rocq | `hodge_delta_collapse` | `: forall (V : AlgebraicVariety) (c : HodgeCycle V), True` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/millennium/HodgeModule.v` |
| Millennium | Coq/Rocq | `millennium_unification` | `: forall (p : MillenniumProblem), classical_formulation p -> delta_resolution p` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/millennium/MillenniumTheorem.v` |
| Millennium | Coq/Rocq | `navier_stokes_delta_bounded` | `: forall v : VelocityField, delta_bounded_flow v` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/millennium/NavierStokesModule.v` |
| Millennium | Coq/Rocq | `riemann_delta_collapse` | `: True` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/millennium/RiemannModule.v` |
| Millennium | Coq/Rocq | `yang_mills_delta_gap` | `: forall g : GaugeField, delta_mass_gap g` | , Axiom | `attack/poincare-f7-f8-multistate-20260926`:`coq/millennium/YangMillsModule.v` |
| Millennium | Coq/Rocq | `T1_conditional_equivalence` | `: Conj1_delta_gap_equivalence -> Conj2_strong_critical -> (RiemannHypothesis <-> P_eq_NP_o` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/DeltaGap.v` |
| Millennium | Coq/Rocq | `T4_transfer` | `: forall delta, delta > 0 -> (forall rho, ZetaZero rho -> Rabs (Delta_RH rho) <= delta) ->` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/DeltaGap.v` |
| Millennium | Coq/Rocq | `theorem_A` | `: forall (w : ObstructionWeights) (p : MillenniumProblem), Omega w classical_system p > 0` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `theorem_B` | `: forall (w : ObstructionWeights) (S : MathSystem) (p : MillenniumProblem), StrongSol w S ` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `theorem_C` | `: forall (w : ObstructionWeights) (p : MillenniumProblem), ~ StrongSol w classical_system ` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `weak_implies_strong_in_expanded` | `: forall (w : ObstructionWeights) (p : MillenniumProblem), WeakSol expanded_system p -> St` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `Omega_nonneg` | `: forall (w : ObstructionWeights) (S : MathSystem) (p : MillenniumProblem), 0 <= Omega w S` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `Omega_zero_iff` | `: forall (w : ObstructionWeights) (S : MathSystem) (p : MillenniumProblem), Omega w S p = ` | , Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`formal/coq/StructuralInsufficiency.v` |
| Millennium | Coq/Rocq | `main_delta_collapse` | `: forall (problem : MillenniumProblem), classical_formulation problem -> delta_resolution ` | — | `attack/poincare-f7-f8-multistate-20260926`:`formal/theorems/main_delta_collapse.v` |
| Millennium | Isabelle | `seven_problems` | `"length allMillenniumProblems = 7"` | — | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/GapUniversal.thy` |
| Millennium | Isabelle | `all_problems_grouped` | `"p \<in> set allMillenniumProblems \<Longrightarrow> \<exists>g. problemGroup p = g"` | — | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/GapUniversal.thy` |
| Millennium | Isabelle | `hodge_delta_collapse` | `"True"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Millennium/HodgeModule.thy` |
| Millennium | Isabelle | `millennium_unification` | `"\<forall>p. classical_formulation p \<longrightarrow> delta_resolution p"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Millennium/MillenniumTheorem.thy` |
| Millennium | Isabelle | `navier_stokes_delta_bounded` | `"\<forall>v. delta_bounded_flow v"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Millennium/NavierStokesModule.thy` |
| Millennium | Isabelle | `riemann_delta_collapse` | `"True"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Millennium/RiemannModule.thy` |
| Millennium | Isabelle | `yang_mills_delta_gap` | `"\<forall>g. delta_mass_gap g"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Millennium/YangMillsModule.thy` |
| Millennium | Isabelle | `partition_size_5` | `"card (UNIV :: MillenniumPartition set) = 5"` | axiomatization, sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/NonUnification/NonUnification.thy` |
| Millennium | Isabelle | `delta_Hodge_nonneg` | `"delta_Hodge hp \<ge> 0"` | axiomatization | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Problems/Hodge.thy` |
| Millennium | Isabelle | `delta_Hodge_zero_iff` | `"delta_Hodge hp = 0 \<longleftrightarrow> is_algebraic (hp_manifold hp) (hp_class hp)"` | axiomatization | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Problems/Hodge.thy` |
| Millennium | Isabelle | `Hodge_delta_equivalence` | `"Hodge_Conjecture \<longleftrightarrow> problem_true Hodge_DeltaOp"` | axiomatization | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Problems/Hodge.thy` |
| Millennium | Isabelle | `mass_gap_delta_nonneg` | `assumes "mass_gap_exists"` | axiomatization | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Problems/YangMills.thy` |
| Millennium | Isabelle | `YM_delta_equivalence` | `"YM_Mass_Gap_Problem \<longleftrightarrow>` | axiomatization | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Problems/YangMills.thy` |
| Millennium | Isabelle | `Hodge_bridge_equivalence` | `"has_bridge Framework_Hodge"` | — | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/Unified/Framework.thy` |
| Millennium | Isabelle | `rh_certificate` | `shows "riemann_hypothesis \<longleftrightarrow> K_RH < \<infinity>"` | sorry | `attack/poincare-f7-f8-multistate-20260926`:`isabelle/UniversalCriticalFunctional.thy` |
| Millennium | Coq/Rocq | `allTrue_iff_allDeltaZero` | `(F : MillenniumFamily) : allTrue F <-> allDeltaZero F` | Axiom | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/CoreDelta.v` |
| Millennium | Coq/Rocq | `not_all_true_if_one_false` | `(F : MillenniumFamily) (i : ProblemIndex) : ~ (F i).(statement) -> ~ allTrue F` | Axiom | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/CoreDelta.v` |
| Millennium | Coq/Rocq | `allTrue_implies_each_zero` | `(F : MillenniumFamily) (i : ProblemIndex) : allTrue F -> forall x, (F i).(Xcrit) x -> (F i` | Axiom | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/CoreDelta.v` |
| Millennium | Coq/Rocq | `summary_independence` | `: ~ Equivalence MillenniumPair /\ (forall s, In s AllScenarios -> scenario_consistent s)` | Axiom | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Framework/NoEquivalence.v` |
| Millennium | Coq/Rocq | `Hodge_delta_formulation` | `: HodgeConjecture <-> (forall hp, smooth_hodge_pair hp -> delta_Hodge hp = 0)` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Millennium/Hodge.v` |
| Millennium | Coq/Rocq | `hodge_solved_iff_conjecture` | `: solved hodgeProblem <-> HodgeConjecture` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Millennium/Hodge.v` |
| Millennium | Coq/Rocq | `RH_delta_formulation` | `: RiemannHypothesis <-> (forall s, non_trivial_zero s -> delta_RH s = 0)` | Parameter | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Millennium/RH.v` |
| Millennium | Coq/Rocq | `rh_solved_iff_hypothesis` | `: solved rhProblem <-> RiemannHypothesis` | Parameter | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Millennium/RH.v` |
| Millennium | Coq/Rocq | `YM_delta_formulation` | `: YMMassGap <-> (forall ym, valid_ym_theory ym -> delta_YM ym = 0)` | Axiom, Parameter | `attack/poincare-f7-f8-multistate-20260926`:`src/coq/Millennium/YangMills.v` |
| … | | | (346 a mais em inventory.json) | | |

## Vazios e sem acesso

**Vazios (sem nenhum commit):** invariance-signature-framework, riemann-transverse-signature, structural-signature-calculus, Lunar-Hive-00, umi-master, umi-core-axioms, unified-millennium-invariant, riemann-coercivity-program, TABP-weighted-irregular-sampling, Omega-completa, emergent-identity-framework, millennium-limit-unification, universal-indeterminate-constant-I.

**Sem acesso nesta sessão** (privados não anexados; os nomes indicam arte, arquivo pessoal/jurídico, arquitetura, idiomas, cultura etc.). Podem ser incluídos sob pedido: metaos-operational-system, zero-engine-00, Marella-RWS-Evidence-Repository, stationary-photon-moving-geometry, zero-ai-00, mishkan-iii-core, zeta-i-formal.lean, harappan-universal-dictionary, harappan-00-universal, orion, projeto-0-0, maritimo-delta-estrela-k13, digital-fire-la28, lighting-narrative-lab, LA-2008-R-, Parque-do-Bixiga-00, olympic-symbolic-00, The-Legal-Playbook-Script, Psychological-Warfare-Vault, The-Vessel-Logos-Admin, Network-Investment-Fund, The-America-Call-LA2028-Master, The-Crew-Voice-Archive-, The-Consortium-of-Redemption, System-Integrity-Audit, Protocol-Vessel-Control, Archive-Mystic-Silence, Archive-Royal-Blue, universal, Ceremony-OS, universal-0-5-emergent-identity, universe-00-ci-templates, universal-sustainable-engineering, psychology-symbolic-00, sacred-texts-mirror, art-00-vision, universal-archive, universe-archives-00-, universe-archives-00, olympic-livebook-00, olympic-operations-00, olympic-architecture-00, olympic-costumes-00, olympic-choreography-00, olympic-video-00, olympic-lighting-00, olympic-score-00, olympic-rituals-00, olympic-dramaturgy-00, olympic-00-core, olympic-show-prototype-00, olympic-00-chama, urban-lighting-00, installations-design-00, creative-direction-portfolio-00, stage-management-portfolio-00, sound-tech-portfolio-00, lighting-tech-portfolio-00, urban-future-architecture-00, infinite-energy-reactor-00, i-foundations.lean, collapse-lemma-rh.lean, water-cycles-00, ship-zero-waste-00, hotel-terra-00, hotel-lunar-00, siamese-consciousness-00, identity-fields-00, linguistic-universal-00, symbolic-grammar-00, phonology-ancestral-00, universal-education-00, tanakh-mirror-00, tupi-hebrew-bridge-00, primordial-language-00, symbolic-chemistry-00, symbolic-biology-00, symbolic-automata-00, symbolic-quantum-computing, quantum-field-symbolic-00, quantum-spacetime-00, symbolic-cosmology-00, symbolic-gravitational-collapse-00, symbolic-balance-field-equation, symbolic-collapse-00, symbolic-linguistics-00, music-harmonic-00, zero-game-00, zero-codex-archive-00.

## Linguagens (todos os repositórios varridos)

| Linguagem/formato | Arquivos distintos |
|---|---|
| Markdown | 10617 |
| Lean | 7842 |
| Python | 5099 |
| LaTeX | 2133 |
| YAML | 1940 |
| JSON | 1469 |
| (sem extensão) | 960 |
| Coq/Rocq | 696 |
| Shell | 602 |
| Isabelle | 457 |
| .txt | 395 |
| Agda | 231 |
| CSV | 189 |
| TOML | 155 |
| Jupyter | 130 |
| .pyc | 128 |
| .png | 126 |
| .bib | 118 |
| .tsx | 94 |
| .cff | 92 |
| .sha256 | 70 |
| C/C++ | 59 |
| .log | 57 |
| .pdf | 44 |
| JS/TS | 39 |
| HTML | 37 |
| .hpp | 24 |
| .tikz | 22 |
| .css | 19 |
| .svg | 17 |
