# ATK — Full-source recovery batch 2026-10-09

State: SOURCE_COPIED_EXACT / IMPORT_RESOLUTION_PENDING / KERNEL_NOT_RUN.

Each file below was fetched in full and written unchanged to this branch. Git blob SHA identifies the original file content. Copies under ATK/recovered-sources are archival and are NOT yet part of Lake search paths; importing them directly may cause module namespace collisions.

| Original repo/ref/path | Original blob SHA | Preserved complete file | Lines |
|---|---|---|---|
| m-core-p-vs-np / atk/p01-successor-cycle-20261005 / lean/MCore/Real/IntegratedMaterialProofs.lean | 306107982115ea1ed41b69888c5e2e39fb58fbb5 | [PNP_IntegratedMaterialProofs.lean](recovered-sources/20261009/PNP_IntegratedMaterialProofs.lean) | 43 |
| m-core-beal / atk/global-material-audit-20261008 / lean/MCore/K8.lean | db0593e99aa26cc0f2919f3fc8b3d204ba41ab96 | [Beal_K8.lean](recovered-sources/20261009/Beal_K8.lean) | 32 |
| m-core-hodge / atk/global-material-audit-20261008 / lean/MCore/Frontier/CandidateBridge.lean | 2b0fd2bcf460cf2babbdde3d659ee441dc9fba95 | [Hodge_CandidateBridge.lean](recovered-sources/20261009/Hodge_CandidateBridge.lean) | 240 |
| axiomatic-millenium / main / AxiomaticMillenium/SevenLaneClosureKernel.lean | d98b0d4f08de24b9c93495f368387b7f37924dcd | [Global_SevenLaneClosureKernel.lean](recovered-sources/20261009/Global_SevenLaneClosureKernel.lean) | 66 |

Branch pagination: M-Core 194; m-core-p-vs-np 689; m-core-riemann 170; m-core-beal 243; m-core-hodge 249; 11 smaller repos 120. Total 1665 branch names discovered, not 1665 source trees extracted.

## Semantic grouping and dependencies
- PNP integrated: imports MCore.K10, MCore.Real.P01FinalCertificate, MCore.Real.FinalProofAttack; contains conditional implications and an impossibility result for an arbitrary-encoder SAT lower-bound certificate.
- Beal K8: imports MCore.K7; contains definitional counterexample equivalence and conditional closure rules.
- Hodge CandidateBridge: imports MCore.FinalAttack; contains conditional candidate reductions and frontier metadata.
- SevenLaneClosureKernel: imports SevenLaneClosedMath, SevenLaneClosedBridge, SevenLaneExactFrontier; proves structural accounting, explicitly buildVerified=false.

## Remaining
- Extract Lean trees from branch heads, deduplicate by exact declaration type and proof dependencies.
- Port full transitive imports and resolve Lean/mathlib compatibility into separately versioned packages.
- Run lake build and #print axioms in real Lean environment; no build or audit result is claimed here.
