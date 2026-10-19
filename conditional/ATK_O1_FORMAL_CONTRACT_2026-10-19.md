# ATK-O1: hypothetical formalization contract

**Lane:** RH / O1. **Status:** HYPOTHETICAL_SPECIFIED, KERNEL_NOT_EXECUTED, UNCONDITIONAL_NOT_ESTABLISHED.

## Grammar and semantics
Sorts: `ℕ`, `ℝ`, `Prop`; source-dependent function `DN : ℕ → ℝ`. Terms: `DN N`, `⨅ N, DN N`. Operators: `≤`, `→`, `↔`, `∧`, `Tendsto`, `⨅`. Quantification: `∀ N`, `∀ ε > 0`, `∃ N₀`, `∀ N ≥ N₀`. No temporal or verbal modality changes mathematical truth.

## Laws and derivations
- `DN_antitone`: monotonicity (existing source).
- `DN_tendsto_iInf`: limit existence (existing source).
- `O1_iff_iInf_zero`: convergence iff infimum zero (existing source).
- `rh_obrigacao_suficiente`: convergence implies RH (existing source).
- `O1_implica_minima`: original uniform log bound implies convergence (existing source).
- New module `ATK/O1Hypothetical.lean`: conditional transport lemmas, all with visible hypotheses.

## Hypothetical producer
`H* := (⨅ N, DN N) = 0`. If an independently proven theorem of this type were added, `rh_of_terminal` would produce RH. A rate `DN N ≤ C/log(N+2)` with `C ≥ 0` is a possible sufficient *research target*, not a demonstrated estimate. The log bound is stronger than the minimal terminal.

## Temporal/verbal states
`SOURCE` means files read; `SPECIFIED` means interfaces written; `BUILD_PENDING` means no Lean invocation; `GREEN` requires a successful pinned Lean build; `CERTIFIED` requires a faithful theorem with transitive axioms audited. Never infer `GREEN` from `SPECIFIED`.

## Rigorous defenses
- Never replace the genuine `DN` with a toy function.
- Never replace `RiemannHypothesis` with a local weaker predicate.
- Never discharge H* by restating it, assuming RH, adding a custom axiom, `sorry`, or circular imports.
- Check imports, exact elaborated type, `#print axioms`, source SHA and CI run.
- Never treat 7/7 conditional certificates as 7 unconditional results.

## Source anchors
`ATK/RiemannConcrete.lean`, `ATK/ObrigacoesMinimas.lean`, `ATK/NecessidadeBD.lean`, `ATK/FinalRoot.lean`, `scripts/terminal_gates.json` (in `M-Core/atk-kernel/`).

## Pending
Compile the new module under the pinned Mathlib toolchain; integrate it into an opt-in CI job; audit all dependencies. No kernel execution has been performed by this commit.
