# ATK — Dependency recovery batch 2026-10-09

Status: SOURCE_PRESERVED / IMPORT_GRAPH_OPEN / MATERIAL_ENDPOINT_NOT_CERTIFIED.

This batch preserves ten additional complete Lean files under [recovered-sources/20261009](recovered-sources/20261009). Twenty-six complete source copies now reside in this directory across three recovery batches. These are archives, not imported Lake modules.

| Lane | Original repository / source path | Archived complete source |
|---|---|---|
| PNP | m-core-p-vs-np/lean/MCore/Real/P01FullVerifierMachine.lean | [PNP_P01FullVerifierMachine.lean](recovered-sources/20261009/PNP_P01FullVerifierMachine.lean) |
| PNP | m-core-p-vs-np/lean/MCore/Real/FinalProofAttack.lean | [PNP_FinalProofAttack.lean](recovered-sources/20261009/PNP_FinalProofAttack.lean) |
| Beal | m-core-beal/lean/MCore/BealDirectProducer.lean | [Beal_DirectProducer.lean](recovered-sources/20261009/Beal_DirectProducer.lean) |
| Beal | m-core-beal/lean/MCore/Material/GCDAdapter.lean | [Beal_GCDAdapter.lean](recovered-sources/20261009/Beal_GCDAdapter.lean) |
| Hodge | m-core-hodge/lean/MCore/BackwardAudit/R2FiberAlgebraicityBoundary.lean | [Hodge_R2FiberAlgebraicityBoundary.lean](recovered-sources/20261009/Hodge_R2FiberAlgebraicityBoundary.lean) |
| Hodge | m-core-hodge/lean/MCore/BackwardAudit/R3SpecializationBoundary.lean | [Hodge_R3SpecializationBoundary.lean](recovered-sources/20261009/Hodge_R3SpecializationBoundary.lean) |
| BSD | m-core-bsd/lean/MCore/Material/RankAdapter.lean | [BSD_RankAdapter.lean](recovered-sources/20261009/BSD_RankAdapter.lean) |
| YM | m-core-yang-mills/lean/MCore/Material/EndpointResidueAdapter.lean | [YM_EndpointResidueAdapter.lean](recovered-sources/20261009/YM_EndpointResidueAdapter.lean) |
| NS | navier-stokes-critical-barrier-audit/audit/producer-first/NSMaterialInhabitant.lean | [NS_MaterialInhabitant.lean](recovered-sources/20261009/NS_MaterialInhabitant.lean) |
| NS | navier-stokes-critical-barrier-audit/formal/lean/CriticalBarrier/GlobalRegularityFromG1.lean | [NS_GlobalRegularityFromG1.lean](recovered-sources/20261009/NS_GlobalRegularityFromG1.lean) |

## Next mandatory gates
1. Recursively resolve exact import paths and repository revisions for each candidate.
2. Compare theorem signatures, universe parameters and premises; deduplicate identical declarations, not merely filenames.
3. Require concrete inhabitants for all terminal producer targets; disallow circular hypotheses and axiom shortcuts.
4. Compile via Lake, inspect #print axioms, and record actual run ID and commit SHA.

No terminal theorem or unconditional conjecture proof has been certified by this recovery operation.
