# Os 2.440 teoremas auditados — o que cada um pode (e não pode) provar

Fonte: `PUBLICATION/MASTER/inventories/<lane>/PROOF_INVENTORY.json` (gerados pelo kernel no CI, listados em `FINAL_PROOF_STRUCTURE.md`). Cada teorema foi localizado **no commit exato que o CI verificou** (`sources.json`), sua assinatura foi extraída do código-fonte e classificada pela forma lógica. Reproduzir: `python3 scripts/thm2440.py <M-Core> <clones> saida.json` e `python3 scripts/report2440.py saida.json THEOREMS_2440.md theorems_2440.json`.

## Veredito

- **2440 teoremas**, todos CLEAN no kernel (só `propext`, `Classical.choice`, `Quot.sound`). Isso é verdade e continua verdade.
- **653 deles (27%) não são provas incondicionais dos alvos**: são projeções automáticas de campos `Prop` de `structure`/`class`. O Lean gera `S.campo : S → P` para cada campo; isso só dá `P` a quem já tem um `S`. É uma hipótese empacotada, contada como teorema pelo inventário.
- **19 condicionais** concluem um enunciado-alvo ou terminal. **Nenhum** tem todas as hipóteses provadas por outro teorema dos 2.440 (descarregados: 0).
- Os enunciados finais estão no relatório de proposições do próprio kernel como `NO_PROOF_IN_LIBRARY` (`MCore.OfficialSpecRH`, `MCore.BealConjecture`, `MCore.Real.CanonicalFinalProof.PneqNP`, `MCore.Real.MachinePneqNP`, `MCore.Real.FINAL_PROOF_RESIDUAL`…).
- Conclusão: usar os 2.440 juntos dá exatamente as pontes e a infraestrutura dos modelos (B1–B7, L1–L5 do livro-razão). **Não produz nenhuma das obrigações O1–O8.** `CLOSED_MATH` continua `false`, agora com a razão medida teorema por teorema.

## Classificação por lane

| Forma | Riemann | P vs NP | Navier–Stokes | Hodge | BSD | Yang–Mills | Beal | Total |
|---|---|---|---|---|---|---|---|---|
| Campo de estrutura (hipótese empacotada) | 21 | 115 | 151 | 126 | 9 | 154 | 77 | **653** |
| Condicional → alvo | 2 | 5 | 0 | 5 | 0 | 0 | 7 | **19** |
| Equivalência (↔) | 4 | 33 | 0 | 34 | 3 | 2 | 65 | **141** |
| Refutação / negação / firewall | 26 | 132 | 2 | 30 | 29 | 44 | 36 | **299** |
| Status / registro / execução | 11 | 129 | 0 | 24 | 22 | 39 | 10 | **235** |
| Implicação estrutural | 45 | 367 | 37 | 89 | 8 | 56 | 198 | **800** |
| Fato estrutural sem hipótese | 22 | 81 | 27 | 118 | 8 | 26 | 10 | **292** |
| Fonte não localizada | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| **Total** | 132 | 862 | 217 | 426 | 79 | 321 | 403 | **2440** |

Leitura: *equivalências* transportam um problema para outra formulação (não provam nenhum dos lados); *refutações* são em geral firewalls (rotas fechadas como falsas, alegações bloqueadas); *status/registro* são fatos sobre o próprio livro-razão ou execuções finitas de máquinas; *implicações estruturais* são lemas internos dos modelos.

## Os 19 condicionais que concluem um alvo

Cada linha é `hipóteses → alvo`, certificada. A coluna *descarregada?* responde se algum dos 2.440 (que não seja campo de estrutura) prova a hipótese.

| Lane | Teorema | Hipóteses (abertas) | Conclusão | Obrigação | Descarregada? |
|---|---|---|---|---|---|
| Riemann | `RH.NB.NBHilbertData.finiteSpanApproximatesChi_of_DNToZero` | `D.GeneratorFamily`<br>`D.DNToZero rho` | `D.FiniteSpanApproximatesChi rho` | O1 | não |
| Riemann | `rh_endpoint_of_adapter` | `RHAdapterObligations` | `RiemannHypothesis` | O1 | não |
| P vs NP | `Real.CanonicalFinalProof.separation_certificate_closes` | `SeparationCertificate` | `PneqNP` | O4 | não |
| P vs NP | `Real.CanonicalFinalProof.target_failure_implies_p_ne_np` | `InNP language`<br>`UniversalFailure language` | `PneqNP` | O4 | não |
| P vs NP | `Real.CanonicalSATBoundary.sat_internal_closure_implies_p_ne_np` | `SATInternalClosure` | `PneqNP` | O4 | não |
| P vs NP | `Real.FailProofAllGaps.failure_generator_implies_universal_failure` | `FailureGenerator language` | `UniversalFailure language` | O4 | não |
| P vs NP | `minimalSeparationInhabitant_closes` | `MinimalSeparationInhabitant` | `PneqNP` | O4 | não |
| Hodge | `BackwardAudit.all_exact_three_residues_yield_concrete_payload` | `AllExactThreeResidues M` | `ConcreteAlgebraicityPayload M` | O5 | não |
| Hodge | `BackwardAudit.all_three_residues_yield_concrete_payload` | `AllThreeResidues M` | `ConcreteAlgebraicityPayload M` | O5 | não |
| Hodge | `fa_hodge_to_algebraicity` | `HodgeCertificationBoundary G M` | `GradedRationalHodgeConjecture G → ConcreteAlgebraicityPayload M` | O5 | não |
| Hodge | `hodge_implies_payload_at_boundary` | `HodgeCertificationBoundary G M`<br>`GradedRationalHodgeConjecture G` | `ConcreteAlgebraicityPayload M` | O5 | não |
| Hodge | `k22_hodge_recovers_payload` | `ConcreteModelObligation G M`<br>`GeometryObligation G M`<br>`GradedRationalHodgeConjecture G` | `ConcreteAlgebraicityPayload M` | O5 | não |
| Beal | `BackwardAudit.witness_contract_closes_beal` | `CommonPrimeWitnessContract` | `BealConjecture` | O2 | não |
| Beal | `T1_v0_to_beal` | `V0EquationToCommonDivisor` | `BealConjecture` | O2 | não |
| Beal | `T26_missing_bridge_to_beal` | `T26CertifiedBaseToFreyBridge` | `BealConjecture` | O2 | não |
| Beal | `T35_all_gaps_to_beal` | `T35AllGapContracts G` | `BealConjecture` | O2 | não |
| Beal | `T3_closes_beal` | `T3RawEquationDivisorBridge` | `BealConjecture` | O2 | não |
| Beal | `T42_final_bundle_exports_beal` | `T42FinalProofBundle G` | `BealConjecture` | O2 | não |
| Beal | `closeBeal_from_commonPrime_witnesses` | `∀ d:BealData,CommonPrime d.a d.b d.c` | `BealConjecture` | O2 | não |

Caso exemplar — `closeBeal_from_commonPrime_witnesses`: a hipótese `∀ d : BealData, CommonPrime d.a d.b d.c` *parece* descarregada por `BackwardAudit.CommonPrimeWitnessContract.witness`, que tem exatamente esse tipo. Mas esse "teorema" é o campo `witness` da estrutura `CommonPrimeWitnessContract`: só existe se alguém fornecer o contrato. É a própria conjectura de Beal reembalada. Por isso campos de estrutura nunca contam como descarga.

## Relatório de proposições do kernel (`props`)

O inventário do CI verifica, para cada `def … : Prop` fechada, se existe um teorema CLEAN cujo tipo é exatamente ela (PROVED) ou sua negação (REFUTED).

| Estado | Quantidade |
|---|---|
| NO_PROOF_IN_LIBRARY | 79 |
| PROVED | 12 |
| REFUTED | 8 |
| VACUOUS | 1 |

### PROVED e REFUTED (todos)

| Lane | Proposição | Estado | Por | Leitura |
|---|---|---|---|---|
| Riemann | `MCore.RH.R0.ChiMemLpTwo` | PROVED | `chi_memLp_two` | χ = 𝟙_(0,1] ∈ L² — lema de infraestrutura da rota Nyman–Beurling. |
| P vs NP | `MCore.C12.Calibration.S_OfficialComplexityCalibration` | PROVED | `s_officialComplexityCalibration` |  |
| P vs NP | `MCore.Real.CanonicalSATBoundary.SATEncodingGap` | PROVED | `canonical_sat_encoding_closed` |  |
| P vs NP | `MCore.Real.CanonicalSATFrameMachineV2.BlankNormalizedFrameTapeOperationalGap` | PROVED | `blank_normalized_frame_tape_operational_closed` |  |
| P vs NP | `MCore.Real.CanonicalSATParserAttack.RecursiveParserOperationalGap` | PROVED | `legacy_recursive_parser_gate_is_trivially_inhabited` | o próprio nome do teorema diz: portão legado trivialmente habitado. |
| P vs NP | `MCore.Real.FailProofFiniteAttack.FiniteToUniversalPrinciple` | REFUTED | `finite_to_universal_principle_refuted` |  |
| P vs NP | `MCore.Real.P01FullVerifierPhysicalControl.DecoderEvaluatorLocalGap` | PROVED | `decoderEvaluatorLocalGap_closed` |  |
| P vs NP | `MCore.Real.P01FullVerifierPhysicalRefinementV2.LocalPhysicalInstructionLayerClosed` | VACUOUS | `localPhysicalInstructionLayerClosed` |  |
| P vs NP | `MCore.Real.P01WitnessIndexedRead.WitnessIndexedReadGap` | PROVED | `witnessIndexedReadGap_closed` |  |
| P vs NP | `MCore.Real.SATNotInP` | REFUTED | `current_SATNotInP_refuted` | refutada **no modelo do lane**: a codificação arbitrária coloca toda linguagem em P (`every_language_inP_under_arbitrary_encode`). Defeito do modelo, não P = NP. |
| P vs NP | `MCore.Real.UniversalSATFailure` | REFUTED | `current_UniversalSATFailure_refuted` | idem (mesmo defeito do modelo). |
| Navier–Stokes | `G1FailProofFinal.CURRENT_ARCHITECTURE_FAIL_PROOF_PROP` | PROVED | `CURRENT_ARCHITECTURE_FAIL_PROOF` | prova de que a arquitetura atual do NS falha (firewall). |
| Beal | `MCore.PrimeDivisorProperty` | PROVED | `primeDivisorProperty_core`, `primeDivisorProperty_proved` |  |
| Beal | `MCore.T26UnrestrictedCrossDomainPromotion` | REFUTED | `T26_unrestricted_cross_domain_promotion_refuted` |  |
| Beal | `MCore.T28PrimeProductProperty` | PROVED | `T29_prime_product_property_proved` |  |
| Beal | `MCore.T35UniversalGapSkip` | REFUTED | `T35_universal_gap_skip_refuted` |  |
| Beal | `MCore.T43UniversalSingleResidualPrimeRule` | REFUTED | `T43_universal_single_residual_prime_rule_refuted` |  |
| Beal | `MCore.T44UniversalLevelTwoPromotion` | REFUTED | `T44_universal_level_two_promotion_refuted` |  |
| Beal | `MCore.T52UniversalNonemptyPromotion` | REFUTED | `T52_nonempty_only_is_insufficient` |  |
| Beal | `MCore.T8EuclidKernel` | PROVED | `T9_euclidKernel_proved` |  |
| Beal | `MCore.T8PrimePowerReflection` | PROVED | `T9_primePowerReflection_proved` |  |

Nenhuma proposição PROVED é um enunciado final ou uma obrigação O1–O8.

## Por obrigação

| Obrigação | Teoremas que a mencionam | Algum a produz sem hipótese? |
|---|---|---|
| O1 — RH — FiniteSpanApproximatesChi / UniformLogBound | 18 | não |
| O2 — Beal — GCDLowerBound universal | 72 | não |
| O3 — NS — G1Bridge / regularidade global | 2 | não |
| O4 — P≠NP — SATNotInP / UniversalFailure | 24 | não |
| O5 — Hodge — ConcreteAlgebraicityPayload | 46 | não |
| O6 — BSD — parte do posto | 12 | não |
| O7 — BSD — fórmula refinada | 15 | não |
| O8 — YM — construção 4D + gap | 34 | não |

"Mencionam" = o nome ou a conclusão contém o vocabulário da obrigação. Todos esses são condicionais, equivalências, refutações de rotas, campos de estrutura ou fatos de registro.

## Como os 2.440 entram no kernel (o uso correto)

1. **Pontes**: os condicionais certificados são exatamente a forma `PONTE → ABERTA → ENUNCIADO` já usada em `atk-kernel/ATK/Conditional/*.lean` e no teorema-mestre `ATK.ClosedMath.closedMath_of_obligations`.
2. **Firewalls**: as refutações impedem promoções indevidas (ex.: `SATNotInP` refutada mostra que o modelo de máquina precisa ser corrigido antes de qualquer prova de P≠NP valer).
3. **Infraestrutura**: lemas estruturais (L², máquinas, resíduos, Gram) são reutilizáveis num produtor futuro.
4. **O que falta** é o mesmo de antes: um termo, sem hipóteses, de cada obrigação O1–O8. Quando existir, o portão calculado `ATK.ClosedMathGate.closed_math` muda `CLOSED_MATH` sozinho.

