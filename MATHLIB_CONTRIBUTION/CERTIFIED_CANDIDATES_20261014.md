# ATK → Mathlib: kernel-certified candidates (2026-10-14)

Status: KERNEL_CERTIFIED_IN_ATK_CI; MATHLIB_OVERLAP_CHECKED; UPSTREAM_NOT_SUBMITTED.

This file complements `CANDIDATE_AUDIT_20261014.md`. That audit inspected the oldest lane copies
of `atk-kernel` (`m-core-riemann`, `m-core-beal`). The candidates below are the current files in
`ShantiDraconis/M-Core`, branch `conditional`, already compiled by the ATK kernel CI. They follow
the gates in `PROVENANCE_AND_GATES.md`. None of them proves any of the seven terminal problems:
`OPEN_MATH = true`.

## Common evidence

- Toolchain: Lean 4.34.1, Mathlib `v4.34.1` (pinned in `atk-kernel/lakefile.toml`).
- Axioms of every listed declaration: only `propext`, `Classical.choice`, `Quot.sound`;
  no `sorry`, `admit` or `axiom` in the source (checked by `atk-kernel/scripts/check_axioms.py`).
- Current CI: `conditional` at `b5db6e8`, workflow run `38599073934`,
  `ATK-KERNEL CERTIFIED 1149/1149`. All candidate files below are in that build, at the blob SHAs
  listed.
- Runs that first certified each file: `9e27bb5` → run `38475715221` (256/256);
  `c17a627` → run `38483008123` (283/283); `2acfe25` → run `38498390388` (675/675).
- Overlap check: `leanprover-community/mathlib4` master at `8678dc2`
  (2026-10-14 16:51 UTC) and tag `v4.34.1`, by searching declaration names, statements and
  docstrings. A search can miss an equivalent result under another name; reviewers decide.
- Authorship: git author Tiago Paschoalatto Fagliari. The proofs were written with AI assistance
  (Claude, Anthropic); the commits carry a `Co-Authored-By: Claude` trailer. A Mathlib PR must
  disclose this in its description and carry the `LLM-generated` label (comment `LLM-generated`).
  Under Mathlib policy the PR author must understand every proof and write review replies in
  their own words.
- License: these files live in M-Core (`COMMERCIAL_LICENSE.txt`). Mathlib is Apache-2.0, so any
  submitted code must be released under Apache-2.0. That is the owner's decision.

## Candidates, in priority order

### 1. Fermat's right triangle theorem

- File: `atk-kernel/ATK/FermatRightTriangle.lean`, blob `bb575dd388a94839949acd133096f23bc0a4b029`,
  added in `c17a627`; 18 declarations, 425 lines.
- Main statements:
  - `not_fermat_4m4 {a b c : ℤ} (hb : b ≠ 0) (hc : c ≠ 0) : a ^ 4 - b ^ 4 ≠ c ^ 2`
    (infinite descent on `|a|`; odd and even cases via `PythagoreanTriple.coprime_classification'`);
  - `not_fourth_add_sq_eq_fourth : x ≠ 0 → y ≠ 0 → x ^ 4 + y ^ 2 ≠ z ^ 4`;
  - `not_sq_add_and_sub_sq`: `x² + y²` and `x² − y²` are not both squares (`y ≠ 0`);
  - `fermat_right_triangle`: the area of a nonzero Pythagorean triangle is not a square
    (`a * b ≠ 2 * d ^ 2`);
  - `one_not_congruent`: no rational right triangle has area 1.
- Mathlib overlap: none found. Mathlib has `not_fermat_42` (`a⁴ + b⁴ ≠ c²`) and
  `fermatLastTheoremFour` in `Mathlib/NumberTheory/FLT/Four.lean`, but not `a⁴ − b⁴ = c²`, the
  right-triangle area theorem or congruent numbers.
- Drop before submission: `sq_ne_two_mul_sq` (irrationality of √2 is already `irrational_sqrt_two`).
- Target: next to `Mathlib/NumberTheory/FLT/Four.lean`, reusing its `Fermat42` descent pattern.
- Work needed: English names following Mathlib conventions, module system (`module`,
  `public import`), copyright header, references (Fermat; Mordell, *Diophantine Equations*).

### 2. Nyman–Beurling criterion, easy direction (`D_N → 0 ⇒ RH`)

- Files (all added in `9e27bb5`):
  - `atk-kernel/ATK/ZetaStrip.lean`, blob `f35c76c864b8e91e4ee1c5b74459a0402d58504e`, 14 declarations:
    `H_eq_zeta : 0 < s.re → s ≠ 1 → ∫_{(1,∞)} {t} t^{-s-1} dt = 1/(s − 1) − ζ(s)/s`
    (Abel summation for `Re s > 1`, then the identity principle on `Re s > 0`);
  - `atk-kernel/ATK/MellinRho.lean`, blob `d0921cac925f77c5223014ccca60b478fe696646`, 10 declarations:
    `mellin_rho : 1 ≤ k → 0 < s.re → s.re < 1 → mellin (fun t => {1/(k t)}) s = −k^{−s} ζ(s)/s`;
  - `atk-kernel/ATK/BaezDuarteBridge.lean`, blob `39b2e11ba86c1e1e27444f3d04edb41d9c41e586`,
    22 declarations: `baezDuarteCriterion : Tendsto DN atTop (𝓝 0) → RiemannHypothesis`, with
    Mathlib's own `RiemannHypothesis`.
- Mathlib overlap: none found for Nyman, Beurling or Báez-Duarte, nor for the fractional-part
  integral formula for ζ on `Re s > 0`. Related, already used: `LSeries_eq_mul_integral'`
  (`LSeries/SumCoeff.lean`), `riemannZeta_one_sub`, `riemannZeta_ne_zero_of_one_le_re`, and the
  real-variable analysis in `NumberTheory/Harmonic/ZetaAsymp.lean`.
- Work needed: split into three PRs (ζ on the strip; Mellin of `{1/(kt)}`; the criterion).
  `DN` is defined through `ATK.Conditional.Riemann`; restate it as a distance in `L²(0, ∞)` or
  directly as the infimum, in Mathlib terms.

### 3. Carlström wheels (division by zero)

- File: `atk-kernel/ATK/Roda.lean`, blob `36651c43de406de44a9303ed163bece7e0012185`, added in
  `dd09f5c` (renamed in `2acfe25`); 50 declarations, 385 lines.
- Content: the wheel `K⊙` of a field as a quotient of `K × K` by scaling; commutative monoids;
  Carlström's eight wheel axioms (`roda_w1` … `roda_w8`); `x / x = 1 + 0·x/x`; `/0 = ∞`,
  `0/0 = ∞/∞ = 0·∞ = ∞ + ∞ = ∞ − ∞ = ⊥`; `⊥` absorbing; `⊥ ≠ 0, 1, ∞`; the embedding of `K`;
  failure of `0 · x = 0` and of `x − x = 0`.
- Mathlib overlap: no wheel structure found (master or `v4.34.1`).
- Work needed: discuss on Zulip before writing the PR. Mathlib would most likely want an abstract
  `Wheel` class (Carlström's axioms) and the wheel of fractions of a commutative ring with a
  multiplicative submonoid, of which the field case is an instance. Reference: J. Carlström,
  *Wheels — on division by zero*, Math. Structures Comput. Sci. 14 (2004).

### 4. Elementary trigonometric and algebraic limits (low priority)

- File: `atk-kernel/ATK/LimitesUm.lean`, blob `22e7bdac477713f5d5be8628f4b225d6e2682429`, added in
  `dd09f5c`; 11 declarations.
- Mathlib overlap: **`sin_div_x` duplicates `Real.tendsto_sin_div_nhdsNE_zero`**, added to master
  in `Mathlib/Analysis/SpecialFunctions/Trigonometric/Deriv.lean`. Master also has
  `Real.tendsto_one_sub_cos_div_nhdsNE_zero` (`(1 − cos x)/x → 0`), and `v4.34.1` already has
  `Real.sinc`.
- Not found in master: `(1 − cos x)/x² → 1/2`, `(sin x − x)/x³ → −1/6`,
  `(tan x − sin x)/x³ → 1/2`, `x(√(x² + 1) − x) → 1/2`, and `√(x² + 1/4)/x → 1` at `+∞`.
- Assessment: at most a small PR next to the new master lemmas. Reviewers may judge these too
  routine.

## Not candidates

- `ATK.MathlibCandidates.residual_sub_square_div_le` (`Lean/ResidualInequalities.lean`):
  `r − c²/d ≤ r` for `d > 0` is `sub_le_self _ (by positivity)`; too elementary for Mathlib. It
  also sits outside `atk-kernel`, so the kernel CI does not compile it.
- `ATK.Riemann.gram_complete_square`, `gram_residual_le`: check against
  `Mathlib/LinearAlgebra/Matrix/SchurComplement.lean` first; likely covered there.
- `ATK.Beal.exponent_gcd_le_two`: conditional on `FermatLastTheorem`.
- `TeoremaGlobal`, the obligation registry, the Beal residual reductions, `FronteiraUm`,
  `OscilacaoHiperreal`, `TeoriaI`: ATK-specific or one-line consequences of existing Mathlib API.

## Counters

- Candidate files: 6 in 4 groups; theorem declarations: 125 (18 + 14 + 10 + 22 + 50 + 11).
- Kernel validations: through the ATK CI runs listed above.
- Mathlib upstream pull requests submitted: 0.
