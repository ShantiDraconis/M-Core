# ATK Mathlib source triage — 2026-10-14
Status: SOURCE_AUDIT, not a new kernel run or upstream acceptance.

## I-Mathematics clean-room sources
Repo: ShantiDraconis/meta-mathematics-indeterminate-I; historical source commit b8b1da782366a581fccd1118c389a2e191b67f0b; recorded run 35310277736.

| File | Blob SHA | Result | Disposition |
|---|---|---|---|
| src/IMath/Certificates/Core.lean | 8bb83bfd90e1482dc227912cac9089fe1658d107 | C01-C15, no source sorry | ATK certificate evidence; rerun kernel |
| src/IMath/Core/Phi3.lean | 1a37e5f44db8cef31eef7e6ad773cd9ea7e212b7 | three-state datatype, injections, no source sorry | ATK foundations |
| src/IMath/Refinement/Realization.lean | 773ee9ed6bc5d3fa1f4150770b3b0ca2bae5b8b8 | reflexivity, transitivity, antisymmetry, no source sorry | PRIORITY: compare to Mathlib order theory |
| src/IMath/Analysis/Germ.lean | cd4b6386b16d3f36b741d5f23f5de8a62da4ff32 | contextual zero-over-zero germs, no source sorry | ATK analysis; seek generalization |

## Existing extracted candidates
ResidualInequalities.lean; GramQuadratic.lean; LogResidualConvergence.lean; ConditionalExponentGCD.lean.

## Other evidence to audit
federated-trivalent-manifold/formal/lean/RadialGeometry.lean and FiniteEvidence.lean (scoped core); open-math-scoped-final/RIEMANN/Riemann/frozen/vanishing_upper_bound_green_5c66f8dc.lean (conditional only); Elyon-Public-Proof/lean/MCore/Real/Claim1To7Only.lean and BridgeSeven.lean (semantic review required).
Exclude unresolved declarations in Millenium--core/Core/Theorems.lean, Millennium/lean4/TUNS/Theorem.lean, and Heu-7-universal-framework/src/lean/HEU/Problems/RH/Lemmas_RH.lean.

## Admission gates
1. Provenance and source blob SHA.
2. Independent pinned Lean kernel build and axiom audit.
3. Nonvacuous semantics and correct intended statement.
4. Compare with existing Mathlib declarations.
5. Reusable theorem and upstream review.
6. Certificates stay with ATKMathlib as audit artifacts.

Not exhaustive: all branches of 251 repositories have not been inspected.