# Upstream candidate 01 — Fermat's right triangle theorem

Status: READY_FOR_AUTHOR_REVIEW; UPSTREAM_NOT_SUBMITTED.

- Target: `leanprover-community/mathlib4`, new file `Mathlib/NumberTheory/FermatRightTriangle.lean`
  (+1 line in `Mathlib.lean`, added by `lake exe mk_all`).
- Base: mathlib4 `master` at `8678dc2` (2026-10-14), Lean `v4.35.0`.
- Local commit on that base: `075ff0a` (`feat(NumberTheory): Fermat's right triangle theorem`).
  `0001-…patch` here is that commit (`git am` applies it on `8678dc2`).
- Derived from `atk-kernel/ATK/FermatRightTriangle.lean` (blob `bb575dd`, certified in ATK CI),
  rewritten in Mathlib style: English names, module system, Apache-2.0 header.

## Checks run on the Mathlib base

- `lake build Mathlib.NumberTheory.FermatRightTriangle`: success, no warnings.
- `#print axioms` on the 6 main theorems: `propext`, `Classical.choice`, `Quot.sound` only.
- `#lint in Mathlib.NumberTheory.FermatRightTriangle`: 0 errors, 20 declarations, 15 linters.
- `lake exe lint-style`: exit 0.
- `lake exe mk_all`: `Mathlib.lean` updated.

## Main declarations

- `Int.fourth_pow_sub_fourth_pow_ne_sq : b ≠ 0 → c ≠ 0 → a ^ 4 - b ^ 4 ≠ c ^ 2`
- `Int.fourth_pow_add_sq_ne_fourth_pow : a ≠ 0 → b ≠ 0 → a ^ 4 + b ^ 2 ≠ c ^ 4`
- `Int.sq_ne_two_mul_sq : a ≠ 0 → a ^ 2 ≠ 2 * d ^ 2`
- `Int.not_isSquare_sq_add_sq_and_sq_sub_sq : b ≠ 0 → ¬ (IsSquare (a²+b²) ∧ IsSquare (a²−b²))`
- `PythagoreanTriple.mul_ne_two_mul_sq`: the area of a Pythagorean triangle is not a square
- `Rat.mul_ne_two_of_sq_add_sq_eq_sq`: 1 is not a congruent number

## Before opening the PR (owner)

1. Release this file under Apache-2.0 (the header already says so).
2. Fork `leanprover-community/mathlib4`; push the branch `fermat-right-triangle`.
3. Write the PR description in your own words. It must say that AI (Claude, Anthropic) was used
   and how. Then comment `LLM-generated` on the PR to add the label.
4. Be ready to explain the descent (odd and even cases) to reviewers yourself.
