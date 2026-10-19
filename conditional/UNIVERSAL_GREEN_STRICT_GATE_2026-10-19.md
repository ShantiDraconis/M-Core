# UNIVERSAL_GREEN — strict terminal gate contract

**Purpose:** define exactly what must be satisfied before the label `UNIVERSAL_GREEN=true` can be emitted. This document does **not** certify the seven conjectures.

## Logical gate
`UNIVERSAL_GREEN := faithful_targets_proven ∧ terminal_producers_proven ∧ mathematical_bridges_proven ∧ model_links_proven ∧ kernel_pass ∧ transitive_axioms_approved ∧ no_sorry_admit_or_unproved_custom_axiom ∧ pinned_reproducibility`.

The booleans `CLOSED_MATH`, `CLOSED_BRIDGE`, `OPEN_MATH` and `OPEN_BRIDGE` are **derived audit outputs**, never substitute premises. A theorem `ClosedMath M → ClosedBridge M → SevenStatements M` is conditional even when it compiles.

## Mathematical proof obligations
1. RH: prove `Tendsto DN atTop (𝓝 0)` for the *concrete* `DN` or directly prove the exact official RH predicate.
2. Beal: discharge `ExclusaoResidualDescida` (or prove the exact Beal statement).
3. Navier–Stokes: prove the required a priori bound / genuine global regularity statement with physically faithful models and quantifiers.
4. P ≠ NP: prove `SATNotInP` for the faithful complexity/SAT encoding and bridge.
5. Hodge: prove the required middle-codimension algebraicity obligation with faithful algebraic varieties/cycles.
6. BSD: prove both rank and refined-leading-coefficient obligations, including the relevant bridge.
7. Yang–Mills: construct the physical 4D theory and positive spectral mass gap with reconstruction and faithful model linkage.

The minimal conditional root in `ATK/ObrigacoesMinimas.lean` is `closedMath_minimo`; its five bridge fields are `leray`, `cookLevin`, `lefschetz`, `grossZagierKolyvagin`, `osterwalderSchrader`. The final root in `ATK/FinalRoot.lean` also describes model-link obligations L1–L5. Check the actual declaration types rather than inferring from names.

## Formal grammar and semantics
- Sorts: `Prop`, `Type`, `Nat`, `Real`, `Complex`, concrete geometric/analytic structures.
- Connectives: `∀`, `∃`, `∧`, `→`, `↔`, equality and inequality; proof terms are typed evidence.
- Operators: integral, limit, infimum, norm, spectral gap, algebraic cycle, rank, computation-time bounds, depending on lane.
- Modal/verbal states: `ASSUMED`, `SPECIFIED`, `BUILD_PENDING`, `GREEN`, `FROZEN`, `CERTIFIED` are provenance labels, not logical inference rules.
- `OPEN_MATH=false` only if each exact terminal obligation has an unconditional producer; `OPEN_BRIDGE=false` only if each faithful bridge and model link is proved.

## Rigorous audit and defenses
- Compile every imported file under the pinned Lean/mathlib versions.
- Verify every theorem's elaborated type against the original statement.
- Reject `sorry`, `admit`, `native_decide` for unchecked external data, untrusted custom axioms, hidden hypotheses, circular derivations, and weakening of targets.
- Run `#print axioms` and check transitive dependency graph.
- Record SHA, workflow run ID, Lean version, Mathlib commit, successful command and logs.
- Do not mark a gate `PASS` if it has not actually run.

## Current observed state
`SOURCE_VERIFIED | CONTRACT_CREATED | HYPOTHETICAL_CLOSED_ONLY | KERNEL_NOT_EXECUTED | OPEN_MATH_TRUE | OPEN_BRIDGE_NOT_DISCHARGED | UNIVERSAL_GREEN_FALSE`.

## Strict terminal output
```text
UNIVERSAL_GREEN = true
```
may be emitted **only after** the above proof and audit conditions all pass. No finite number of status changes can replace the missing proofs.
