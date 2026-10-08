# ATK — Unified inventory of already formalized fragments

State: SOURCE_CONSOLIDATED / NOT EXHAUSTIVE / KERNEL NOT RE-RUN.
This consolidates inspected source declarations and pre-existing certified-evidence registry without asserting that the seven open conjectures are proved.

## Verified by reading source text
| Area | Declaration or chain | Source | Classification |
|---|---|---|---|
| PNP | construction_closes_p01 | m-core-p-vs-np/lean/MCore/Real/P01FinalCertificate.lean | Conditional on P01ConstructionGap |
| PNP | g21_pointwise_iff_p02_target; g21_iff_g22 | M-Core/imports/pnp/c102d9d4/lean/MCore/Real/P02G21G22Attack.lean | Equivalence, not G21 inhabitant |
| PNP | final_external_gap_of_two_gap; final_external_two_gap_closes | M-Core/imports/pnp/b406b806/lean/MCore/Real/FinalExternalTwoGap.lean | Conditional on P01ConstructionGap and G21Pointwise |
| PNP | final_external_certificate; final_external_gap_closes | M-Core/imports/pnp/c102d9d4/lean/MCore/Real/FinalExternalCertificate.lean | Conditional on FinalExternalInputs |
| PNP | fixed_witness_implies_final; endpoint_compression; endpoint_from_c12_open_bridge | M-Core/imports/pnp/recovery/7abed945/audit/EndpointCompression.lean | Conditional historical classical-interface proofs |
| RH | finiteSpanApproximatesChi_iff_DNLimit_eq_zero | m-core-riemann/GATE_LEDGER.json; frozen/nb-zero-limit-density-equivalence-green-d6a291b4 | Frozen evidence reported; inhabitant OPEN_MATH |
| RH | VanishingUpperBound -> DNToZero -> DNLimit=0 | m-core-riemann/GATE_LEDGER.json; frozen/vanishing-upper-bound-green-5c66f8dc | Frozen conditional chain reported |
| Beal | noCommonPrime_is_counterexample | m-core-beal/lean/MCore/K8.lean | Elementary equivalence |
| Global | seven_lane_kernel_exact; structural_closure_does_not_imply_material_closure; refined_atom_accounting | axiomatic-millenium/AxiomaticMillenium/SevenLaneClosureKernel.lean | Structural theorem declarations; build not rerun |

## Certified/frozen provenance already registered (not freshly compiled)
Source: M-Core/ATK_PROOF_CHAIN_EVIDENCE_REGISTRY.md (blob 362efc08cf6b7d1db30682523f5ca215e5218d9d).
- Beal K6 SHA 434d6b7bba82298e7f90e13817f147011bef5b1e run 35092395821; K9 SHA e3b8598a2513b539b285dfb31dc383b770ab840f.
- Hodge R3 relative cycle frozen branch frozen/hodge-r3-relative-cycle-cut-v4-8ba37af1.
- YM K21 SHA 0352c6afb7e9255bf0fc777269984a2def047080 run 35170322803; old trivial physical interface rejected.
- RH K8 SHA ad3011f14bdab32161205e053fa925bc8c851ad4 run 35565114760.
- PNP K7 SHA 6b965e39dddffb23b407b6779c6241d2c6721997 run 35135679032; C1 frozen/C1-ecdbb0b1.
- BSD K7–K14 certified evidence, TOTAL SHA d24472341ce161cbb49388ef5e1379ea36ac39b2 run 35146718972. Architecture/audit only.
- NS certified failproof run 35565581964; not global regularity.

## Additional formal sources / discovery queues
- M-Core/final-proof/cross_repository_certificate_registry.json
- M-Core/final-proof/structural_certificate_discovery_20261008.json (14 candidates; default branch only)
- M-Core/ATK_PROOF_CHAIN_EVIDENCE_REGISTRY.md
- M-Core/ATK/RECOVERED_FORMAL_PROOFS_20261008.md
- M-Core/ATK/EXACT_TERMINAL_CHAIN_20261008.md
- M-Core/ATK/G21_EXACT_TYPE_REUSE_AUDIT_20261008.md
- Historical snapshots of BSD, Hodge, PNP, RH, YM, NS in navier-stokes-critical-barrier-audit forensic genealogy.

## Important unresolved checks
- Paginate all branches and inspect theorem source files, including frozen/cert refs; no completeness claim yet.
- Pin source commit and blob; verify exact theorem types, domains, assumptions, circularity, and axioms.
- Compile all compatible Lean packages and aggregate import root; no build run from this inventory.
- Keep terminal OPEN_MATH and certification flags unchanged until actual material terms are verified.
