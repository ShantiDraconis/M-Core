# Upstream candidate 02 — the free rank of a f.g. abelian group is its rank over ℤ

Status: READY_FOR_AUTHOR_REVIEW; UPSTREAM_NOT_SUBMITTED.

- Target: `leanprover-community/mathlib4`, existing file
  `Mathlib/GroupTheory/FiniteAbelian/Basic.lean` (+34 lines, no new imports).
- Base: mathlib4 `master` at `8678dc2` (2026-10-14), Lean `v4.35.0`.
- Local commit on that base: `e403f3b`, branch `free-rank-finrank`
  (`feat(GroupTheory/FiniteAbelian): the free rank is the rank over ℤ`).
  `0001-…patch` here is that commit (`git am` applies it on `8678dc2`).
- Derived from `atk-kernel/ATK/PostoLivre.lean` (Mathlib v4.34.1), rewritten for `master`: there
  the torsion-free hypothesis is `IsAddTorsionFree`; on `master` (since 2026-09-29) commutative
  monoids should use `HasUniqueDiv`, so the lemma takes `[HasUniqueDiv G]`.

## Why

Mathlib defines `AddCommGroup.freeRank G` as the minimal number of generators of
`G ⧸ torsion G`, but has no lemma relating it to `Module.finrank ℤ G` or `Module.rank ℤ G`, the
usual way to write the rank of a f.g. abelian group (for instance the Mordell–Weil rank). The
comparison of the ATK and formal-conjectures statements of BSD needs exactly this lemma
(`ATK.IntegracaoFCBSD.postoMW_eq_freeRank`).

## Declarations

- `AddGroup.rank_eq_finrank_int [HasUniqueDiv G] [AddGroup.FG G] :
  AddGroup.rank G = Module.finrank ℤ G`
- `AddCommGroup.freeRank_eq_finrank [AddGroup.FG G] : freeRank G = Module.finrank ℤ G`

## Checks run on the Mathlib base

- `lake build Mathlib.GroupTheory.FiniteAbelian.Basic`: success, no warnings.
- `#print axioms` on both: `propext`, `Classical.choice`, `Quot.sound` only.
- `#lint in Mathlib.GroupTheory.FiniteAbelian.Basic`: 0 errors, 20 declarations, 15 linters.
- `lake exe lint-style`: no output; added lines are at most 100 characters.

## Possible review points

- A multiplicative version (`CommGroup.freeRank G = Module.finrank ℤ (Additive G)`) is not included.
- `HasUniqueDiv (G ⧸ torsion G)` is built inside the proof from `IsAddTorsionFree`; Mathlib may
  prefer a global instance next to `QuotientGroup.instIsMulTorsionFree`.

## Before opening the PR (owner)

1. Fork `leanprover-community/mathlib4`; push the branch `free-rank-finrank`.
2. Write the PR description in your own words, saying that AI (Claude, Anthropic) was used and
   how; then comment `LLM-generated` on the PR to add the label.
3. Be ready to explain the proof to reviewers (generators vs. a basis, and rank-nullity for the
   quotient by the torsion subgroup).
