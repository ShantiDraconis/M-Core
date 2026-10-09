# ATK — Material proof chains and unconditionality audit, recovery 2026-10-09

Status: SOURCE_RECOVERED / TERMINAL_MATERIAL_OPEN / NOT_COMPILED. All paths below are complete archival source copies on this branch, not yet Lake imports.

## Hodge
- [HodgeMaterialInhabitant.lean](recovered-sources/20261009/HodgeMaterialInhabitant.lean), source m-core-hodge/main lean/MCore/HodgeMaterialInhabitant.lean, blob 4099c8ec0cd93a67de2fee2f1a89826dac60695d, 220 lines. Defines CodimZeroCycleProducer, CodimOneCycleProducer, HigherMaterialProducer, HodgeConcreteInhabitant, AnchoredHodgeInhabitant; conditional endpoint theorem AnchoredHodgeInhabitant.certifies (H : AnchoredHodgeInhabitant ...). Dependencies HodgeMaterialFrontier, HodgeTerminalLaw, BackwardAudit.R2AfterR3.
- [HodgeTheoryComplete.lean](recovered-sources/20261009/HodgeTheoryComplete.lean), source m-core-hodge/main lean/P05/Hodge/HodgeTheoryComplete.lean, blob 5841041ee0d5ce6657c0cbac7e811083da605487, 176 lines. Formal realization + six material leaves, theorem hodge_theory_package_closes_terminal (T : HodgeTheoryPackage ...). Ledger declares all six material leaves open.
- [Hodge_CandidateBridge.lean](recovered-sources/20261009/Hodge_CandidateBridge.lean), conditional reductions, 240 lines. No concrete HodgeTheoryPackage or AnchoredHodgeInhabitant constructed in inspected files.

## P vs NP
- [PNP_P01Adapter.lean](recovered-sources/20261009/PNP_P01Adapter.lean), source m-core-p-vs-np/main lean/MCore/Material/P01Adapter.lean, blob 193f0e919ab945470fd09c9c5087febbd733015d, 13 lines. P01CanonicalMaterial := P01ConstructionGap; theorem p01_material_closes_sat_machine (h : P01CanonicalMaterial) conditional.
- [PNP_IntegratedMaterialProofs.lean](recovered-sources/20261009/PNP_IntegratedMaterialProofs.lean), 43 lines. Conditional P01 construction and separation; proves impossibility of arbitrary encoder SAT lower-bound certificate.

## RH
- [RH_MaterialClosure.lean](recovered-sources/20261009/RH_MaterialClosure.lean), source m-core-riemann/main lean/MCore/Material/Closure.lean, blob 197dd3d32059a231188eea65e61f517005f40493, 14 lines. RHClosure contains K0, K0_nonneg, log_pos, bound : ∀ N, DN N ≤ K0 / log(N+2); theorem closure_produces_bound (h : RHClosure DN) conditional. No constructed K0 or unconditional bound.

## Global
- [Global_AcceptedInhabitants.lean](recovered-sources/20261009/Global_AcceptedInhabitants.lean), source M-Core/main lean/MCore/FinalFail/AcceptedInhabitants.lean, blob 2115501ef89dabeec6205ac8329c3a520caa9b21, 154 lines. All seven accepted inhabitants require hypotheses as arguments; no unconditional constructors.
- [Global_UniversalTerminalClosure.lean](recovered-sources/20261009/Global_UniversalTerminalClosure.lean), source M-Core/main lean/MCore/FinalFail/UniversalTerminalClosure.lean, blob 48caa8fd975ac17561c255c9520368070aba6061, 109 lines. TerminalInhabitants ↔ conjunction of seven endpoints; projections and fail-closed audit producedDirectCount=0, openDirectCount=7.
- [Global_SevenLaneClosureKernel.lean](recovered-sources/20261009/Global_SevenLaneClosureKernel.lean), 66 lines, seven-lane structural bookkeeping only.

## Recovery accounting
- Four files copied in batch 1; six files copied in batch 2; ten complete Lean files preserved in ATK/recovered-sources/20261009. No exhaustive recursive tree extraction is available through the current GitHub connector actions; branch listing is not a file tree. 1665 branch names were discovered, not 1665 trees fetched.
- Frozen/certified sources remain unmodified.
- Exact transitive import graph, deduplication by declaration and type, Lake build and actual #print axioms output are pending.

## Proof integrity
None of the examined source files above supplies an unconditional mathematical proof of all seven Millennium statements. The typed producer/inhabitant structures are useful obligations; conditional implications do not discharge their own inputs. No automatic promotion to CLOSED_MATH or material certified status.
