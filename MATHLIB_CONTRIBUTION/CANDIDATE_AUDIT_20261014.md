# ATK → Mathlib: source-level candidate audit (2026-10-14)

Status: SOURCE_INSPECTED; KERNEL_NOT_RUN; UPSTREAM_NOT_SUBMITTED.

## Inspected source files

1. `ShantiDraconis/m-core-riemann/atk-kernel/ATK/Riemann.lean`
   Blob SHA `018b395f949eca88536537428244f4c2d369e06b`.
   - `ATK.Riemann.residual_tendsto_zero`: nonnegative residual bounded by `K / log (N+2)` tends to zero; conditional on the bound.
   - `ATK.Riemann.schur_step_monotone`: real square/division nonnegativity yields a decreasing residual; extracted to `Lean/ResidualInequalities.lean` with origin preserved.
   - `ATK.Riemann.gram_complete_square`: symmetric invertible real matrix completing-square identity.
   - `ATK.Riemann.gram_residual_le`: lower bound using positive semidefiniteness and completing square.

2. `ShantiDraconis/m-core-beal/atk-kernel/ATK/Beal.lean`
   Blob SHA `9f5b1fd68eab75d34d3f843d0308c518012c85c1`.
   - `ATK.Beal.exponent_gcd_le_two`: assumes `hFLT : FermatLastTheorem`; concludes `Nat.gcd x (Nat.gcd y z) ≤ 2` for nonzero bases satisfying the power equation. This is conditional and is NOT a proof of Beal.

## Next audit gates

- Run `lake build` and inspect `#print axioms` output on original files and extracted candidate.
- Compare declarations against existing Mathlib results to avoid duplications.
- Check source license and whether reuse or upstream licensing requires permissions.
- Generalize useful results without changing meaning.
- Preserve authorship/provenance metadata; Git history is evidence of repository activity, not standalone proof of first discovery.
- Keep all seven terminal problems `OPEN_MATH` until their actual unconditional proof terms exist.

## Counters

- Source files read in full: 2
- Lean theorem declarations individually inspected: 5
- Candidate declarations extracted into new ATK branch: 1
- Kernel validations performed in this step: 0
- Mathlib upstream pull requests submitted: 0
