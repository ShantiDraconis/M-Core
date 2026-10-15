# Upstream candidate 02 — the free rank of a f.g. abelian group is its rank over ℤ

Status: READY_FOR_AUTHOR_REVIEW; UPSTREAM_NOT_SUBMITTED (no fork of mathlib4 yet).

- Target: `leanprover-community/mathlib4`, two existing files (+32 lines):
  `Mathlib/GroupTheory/Torsion.lean` and `Mathlib/GroupTheory/FiniteAbelian/Basic.lean`.
- Base: mathlib4 `master` at `8678dc2` (2026-10-14), Lean `v4.35.0`.
- Local branch `free-rank-finrank`, two commits on that base:
  - `e403f3b` feat(GroupTheory/FiniteAbelian): the free rank is the rank over ℤ
  - `772104b` feat(GroupTheory/Torsion): the torsion-free quotient has unique roots
- `0001-…patch`, `0002-…patch`: those commits (`git am` applies them on `8678dc2`; checked).
  `free-rank-finrank.diff`: the combined diff.
- Derived from `atk-kernel/ATK/PostoLivre.lean` (Mathlib v4.34.1), rewritten for `master`.
- `DEFESA.md`: study notes for the owner (the mathematics, every design choice, likely review
  questions). Mathlib requires review comments to be written by the author, without AI.

## Declarations

- `QuotientGroup.instHasUniqueRoots : HasUniqueRoots (G ⧸ torsion G)` and the additive
  `QuotientAddGroup.instHasUniqueDiv` (name given explicitly to `to_additive`)
- `AddGroup.rank_eq_finrank_int [HasUniqueDiv G] [AddGroup.FG G] :
  AddGroup.rank G = Module.finrank ℤ G`
- `AddCommGroup.freeRank_eq_finrank [AddGroup.FG G] : freeRank G = Module.finrank ℤ G`
  (two lines: `rank_eq_finrank_int` on the quotient plus the existing
  `finrank_quotient_torsion_eq`)
- New private `import Mathlib.LinearAlgebra.Dimension.Torsion.Basic` in `FiniteAbelian/Basic.lean`;
  it adds exactly one module (itself) to that file's import closure of 2198 modules.

## Checks run on the Mathlib base

- `lake build` of both files and of every module that imports `Mathlib.GroupTheory.Torsion`
  directly (`Algebra.Module.Torsion.Basic`, `GroupTheory.Descent`,
  `NumberTheory.NumberField.Units.Basic`): success, no warnings (3348 jobs).
- `#print axioms` on the four declarations: `propext`, `Classical.choice`, `Quot.sound` only.
- `#lint in Mathlib.GroupTheory.FiniteAbelian.Basic`: 0 errors (20 declarations, 15 linters).
- `#lint in Mathlib.GroupTheory.Torsion`: 0 errors (144 declarations, 15 linters).
- `lake exe lint-style` on both files: exit 0; added lines at most 100 characters.
- Not run locally: the full Mathlib build (Mathlib's CI does it on the PR).

## Before opening the PR (owner)

1. Fork `leanprover-community/mathlib4` on GitHub (this session cannot create forks: the GitHub
   proxy refuses `POST /repos/…/forks`).
2. Add the fork to the session with push access; then the branch `free-rank-finrank` can be
   pushed from here. Or apply the two patches yourself with `git am`.
3. Write the PR title and description in your own words. Say that AI (Claude, Anthropic, in
   Claude Code) wrote the Lean code and how you checked it; then comment `LLM-generated`.
4. Answer review comments yourself, without AI (see `DEFESA.md`).
