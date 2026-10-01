# GLOBAL MATERIAL MODULE STRICT CERTIFICATE

Status: CERTIFIED
Scope: semantic/global composition module only

Validated SHA:
`9dc4db35c141cdd9f57eeeeb9c2247478bc00aa9`

Frozen branch:
`frozen/global-material-strict-green-9dc4db35`

Certificate branch:
`cert/global-material-strict-9dc4db35-run36848516979`

GitHub Actions run:
`36848516979`

Artifact:
`global-material-strict-9dc4db35c141cdd9f57eeeeb9c2247478bc00aa9`

Artifact ID:
`11154856645`

Artifact digest:
`sha256:705f32a1d8d813b84b2607450326f5e72db9add4caa694d42426a0fd50b10617`

## Strict gates passed

1. Source hygiene on 12 direct semantic/global files:
   - no `sorry`
   - no `admit`
   - no explicit `axiom`
   - no explicit `constant`
2. Semantic orientation inventory:
   - 7 total lanes
   - 6 positive
   - 1 refutational (Riemann off-critical-zero legacy lane)
3. Lean build:
   - `MCore.FinalFail.SemanticParallel`
   - `MCore.FinalFail.GlobalConditionalFinal`
   - `MCore.FinalFail.GlobalPositiveMaterialFrontier`
4. Axiom audit:
   - no `sorryAx`
   - only ordinary foundational axioms appearing in the dependency chain (`propext`, `Classical.choice`, `Quot.sound`)

## Errors found and corrected before certification

- The original mixed global root used the negative Riemann orientation without a machine-readable orientation tag.
- `SemanticLane` now has explicit `SemanticOrientation`.
- All seven lanes now carry orientation values: six positive and one refutational.
- The first edit left six new orientation fields absent; this was caught by pre-CI review and fixed before the strict run.
- `GlobalConditionalFinalRoot` is explicitly documented as mixed-orientation.
- `globalConditionalFinalRoot_implies_not_RH` formally proves that an inhabitant of the old mixed root entails `¬ RiemannHypothesis`.
- `GlobalPositiveMaterialRoot` is the positive-orientation seven-lane root.
- `positive_root_excludes_mixed_negative_root` prevents simultaneous promotion of the positive and mixed-negative global roots.
- `global_positive_root_iff_components` gives the exact information-preserving global frontier.

## Certified central laws

- `beal_target_iff_gcd_lower_bound`
- `pvsnp_target_iff_sat_np_and_not_p`
- `ns_target_iff_exists_universal_stabilizer`
- `hodge_target_iff_pointwise_realization`
- `bsd_target_iff_rank_and_refined`
- `ym_target_iff_exists_physical_theory`
- `rh_excludes_offCriticalZero`
- `positive_rh_incompatible_with_negative_lane`
- `globalConditionalFinalRoot_implies_not_RH`
- `global_positive_root_iff_components`
- `positive_root_excludes_mixed_negative_root`
- `build_global_positive_material_root`

## Scientific boundary

This certificate validates the Lean module, its semantic orientation, equivalence/composition laws, source hygiene and axiom audit.

It does NOT certify unconditional inhabitants for the seven open mathematical terminal producers and does NOT claim proofs of RH, Beal, P≠NP, Navier–Stokes, Hodge, BSD or Yang–Mills.
