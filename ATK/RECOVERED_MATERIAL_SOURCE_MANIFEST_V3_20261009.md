# ATK — Recovered material sources, preservation manifest v3

State: SOURCE_COPIED / PROOF_DEPENDENCY_AUDIT_PENDING / KERNEL_NOT_RUN.

Six additional complete Lean sources were copied unchanged to ATK/recovered-sources/20261009; 16 complete sources now in this archival folder.

| Lane | Full source | Material target |
|---|---|---|
| PNP | [PNP_P01FinalCertificate.lean](recovered-sources/20261009/PNP_P01FinalCertificate.lean) | `P01ConstructionGap` |
| HODGE | [HodgeMaterialFrontier.lean](recovered-sources/20261009/HodgeMaterialFrontier.lean) | `ConcreteAlgebraicityPayload` |
| HODGE | [HodgeMaterialMincut.lean](recovered-sources/20261009/HodgeMaterialMincut.lean) | `HodgeMaterialMincut` |
| BEAL | [Beal_GCDLowerBoundProducer.lean](recovered-sources/20261009/Beal_GCDLowerBoundProducer.lean) | `UniversalTripleGCDLowerBound` |
| BSD | [BSD_MaterialClosure.lean](recovered-sources/20261009/BSD_MaterialClosure.lean) | `BSD` |
| YM | [YM_MaterialClosure.lean](recovered-sources/20261009/YM_MaterialClosure.lean) | `YangMills` |

## Integrity protocol
- Original source modules are archived, not compiled as part of a single Lake package.
- Imports must be resolved transitively; matching names alone do not establish definitional equality.
- Inspect theorem binders and assumptions to detect circular hypotheses.
- Do not promote any terminal claim until material inhabitants are constructed and kernel verified.

## Earlier recovered modules
- PNP_IntegratedMaterialProofs.lean; PNP_P01Adapter.lean; Beal_K8.lean; Hodge_CandidateBridge.lean; HodgeMaterialInhabitant.lean; HodgeTheoryComplete.lean; RH_MaterialClosure.lean; Global_AcceptedInhabitants.lean; Global_UniversalTerminalClosure.lean; Global_SevenLaneClosureKernel.lean.