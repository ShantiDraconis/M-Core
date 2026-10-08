# ATK — Cross-repository linked Lean source index v2

Status: SOURCE_LINKED / NONEXHAUSTIVE / KERNEL_NOT_RUN. This is a cross-repository link inventory, not an assertion that all proofs are material or that imports compile.

## Source links — PNP
- [P01 machine and conditional closure](https://github.com/ShantiDraconis/m-core-p-vs-np/blob/atk/global-material-audit-20261008/lean/MCore/Real/P01FinalCertificate.lean)
- [Recovered P01/witness module](https://github.com/ShantiDraconis/m-core-p-vs-np/blob/atk/global-material-audit-20261008/lean/MCore/Real/ATKRecoveredProofs.lean)
- [Historical integrated implications](https://github.com/ShantiDraconis/m-core-p-vs-np/blob/atk/p01-successor-cycle-20261005/lean/MCore/Real/IntegratedMaterialProofs.lean)
- [P02 G21 G22 equivalences](https://github.com/ShantiDraconis/M-Core/blob/main/imports/pnp/c102d9d4/lean/MCore/Real/P02G21G22Attack.lean)
- [Final external two-gap](https://github.com/ShantiDraconis/M-Core/blob/main/imports/pnp/b406b806/lean/MCore/Real/FinalExternalTwoGap.lean)
- [Final external certificate](https://github.com/ShantiDraconis/M-Core/blob/main/imports/pnp/c102d9d4/lean/MCore/Real/FinalExternalCertificate.lean)
- [Fixed-witness historical compression](https://github.com/ShantiDraconis/M-Core/blob/main/imports/pnp/recovery/7abed945/audit/EndpointCompression.lean)
- [K0–K10 PNP directory](https://github.com/ShantiDraconis/m-core-p-vs-np/tree/main/lean/MCore)

## Source links — RH, Beal, Hodge
- [RH material closure](https://github.com/ShantiDraconis/m-core-riemann/blob/main/lean/MCore/Material/Closure.lean)
- [RH GATE_LEDGER and frozen provenance](https://github.com/ShantiDraconis/m-core-riemann/blob/main/GATE_LEDGER.json)
- [Beal K8 exact equivalences](https://github.com/ShantiDraconis/m-core-beal/blob/atk/global-material-audit-20261008/lean/MCore/K8.lean)
- [Beal GCD lower-bound producer](https://github.com/ShantiDraconis/m-core-beal/blob/main/lean/MCore/GCDLowerBoundProducer.lean)
- [Hodge candidate bridge](https://github.com/ShantiDraconis/m-core-hodge/blob/atk/global-material-audit-20261008/lean/MCore/Frontier/CandidateBridge.lean)
- [Hodge K26](https://github.com/ShantiDraconis/m-core-hodge/blob/main/lean/MCore/K26.lean)

## Source links — seven-lane architecture
- [Seven-lane structural kernel](https://github.com/ShantiDraconis/axiomatic-millenium/blob/main/AxiomaticMillenium/SevenLaneClosureKernel.lean)
- [Global OPEN_MATH cut](https://github.com/ShantiDraconis/axiomatic-millenium/blob/main/AxiomaticMillenium/GlobalOpenMathCut.lean)
- [Global final root audit](https://github.com/ShantiDraconis/axiomatic-millenium/blob/main/AxiomaticMillenium/GlobalFinalRootAudit.lean)
- [BSD terminal staging](https://github.com/ShantiDraconis/millennium-bsd/blob/main/formal/ATKTerminalStaging.lean)
- [Yang–Mills terminal staging](https://github.com/ShantiDraconis/millennium-yang-mills/blob/main/formal/ATKTerminalStaging.lean)
- [Navier–Stokes global existence](https://github.com/ShantiDraconis/millennium-navier-stokes-I/blob/main/src/lean/global_existence.lean)
- [Riemann-I theorem catalog](https://github.com/ShantiDraconis/millennium-riemann-I/blob/main/MillenniumRiemann/Theorems.lean)
- [Poincare symbolic frozen branch](https://github.com/ShantiDraconis/millennium-poincare-symbolic/tree/frozen/K1A-2d098d18)
- [Multiprover basic Lean](https://github.com/ShantiDraconis/proofs-multiprover/blob/main/lean4/ProofsMultiprover/Basic.lean)
- [Formal Suite RH](https://github.com/ShantiDraconis/0-0-FORMAL-SUITE/blob/main/src/FormalSuite/Zeta/CollapseLemmaRH.lean)

## Index and forensic genealogy
- [Previous consolidated inventory](UNIFIED_FORMALIZED_PROOFS_INVENTORY_20261008.md)
- [Cross-repo registry](../final-proof/cross_repository_certificate_registry.json)
- [Structural discovery 14 candidates](../final-proof/structural_certificate_discovery_20261008.json)
- [Historical certificate genealogy](../ATK_PROOF_CHAIN_EVIDENCE_REGISTRY.md)

## Branch discovery
A fresh GitHub branch query checked 16 repositories. Five large repos (M-Core, m-core-p-vs-np, m-core-riemann, m-core-beal, m-core-hodge) returned exactly 100 first-page branches each and require pagination. Other 11 repos returned 120 branch entries combined (49+6+7+4+6+14+8+5+2+9+8). No claim of all branches. Frozen/certified refs remain read-only.

## Integration policy
Before importing across repos: pin commit, compare Lean/toolchain/mathlib, prove type compatibility, check axioms, deduplicate identical statements, then build. No unconditional terminal inhabitants identified by this index.
