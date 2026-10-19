# ATK-O1 — rigorous hypothetical laws and semantic firewall

This is a *source-aligned formal research interface*, not a solved RH claim.

## Objects and syntax
- Sorts: natural indices `N : ℕ`, real coefficients `c : Fin N → ℝ`, real argument `t`, real-valued error `DN N`, propositions `Prop`.
- Concrete semantics: `chi t` is the indicator of `(0,1]`; `rho k t = Int.fract (1 / ((k : ℝ) * t))`; `residualSq N c` is the integral on `(0,∞)` of the squared residual; `DN N` is its infimum over `c`.
- Quantifiers: `∀ N`, `∃ K`, `Tendsto DN atTop (𝓝 0)`; all are interpreted with their Lean/Mathlib types, not informal analogies.
- Logical connectives: `→` for conditional implications, `↔` for equivalence, `∧` for simultaneous claims.
- Operators: integration, finite sum, squared norm, infimum, subtraction, `Tendsto`, `HasSum`, logarithm.
- Temporal/verb phases are *audit workflow metadata*, not operators that change truth: DEFINED → SOURCE_VERIFIED → BUILD_PASS → AXIOM_AUDITED → TERMINAL_PRODUCER_PROVED → CERTIFIED.
- Transitions must be justified by recorded build run and SHA; no self-certification.

## Source-derived laws
1. `DN_nonneg`: all residual errors are nonnegative.
2. `DN_antitone`: adding basis generators cannot increase the infimum.
3. `DN_tendsto_iInf`: the monotone bounded sequence converges to its infimum.
4. `O1_iff_iInf_zero`: `DN → 0 ↔ inf DN = 0`.
5. `O1_iff_dissipacao`: total telescoping dissipation ↔ `DN → 0`.
6. `DN_tendsto_zero`: the **assumed** uniform logarithmic bound implies convergence.
7. `rh_obrigacao_suficiente`: convergence implies `RiemannHypothesis`.

## Hypothetical construction
`QuantitativeLaw := UniformLogBound`, `TerminalLaw := (⨅ N, DN N) = 0`.
Then:
`QuantitativeLaw → TerminalLaw → RiemannHypothesis`.
The new Lean module `ATK/O1HypotheticalLaws.lean` encodes these implications using existing lemmas and explicit assumptions. It contains no `sorry` and declares no new `axiom`, but **has not been compiled in this operation**.

## Exact gap and falsification defenses
The real mathematical gap is to provide an unconditional term of type `TerminalLaw` or a genuinely proved `QuantitativeLaw`. The latter is a stronger statement. Merely adding a `theorem` whose input is `h : QuantitativeLaw` does not prove the input. Reject circularity, vacuous toy models, definition shadowing, unsupported numeric extrapolation, accidental replacement of `rho`, unsound imported axioms, and altered target statements.

## CI acceptance
Pin the exact source commit; `cd atk-kernel && lake build ATK.O1HypotheticalLaws`; inspect all `#print axioms`; check source definitions; confirm the theorem target elaborates to Mathlib's `RiemannHypothesis`. Only after an actual new independent terminal producer is proven may `UNCONDITIONAL` change.

**Status: SOURCE_VERIFIED | MODULE_CREATED | KERNEL_NOT_EXECUTED | TERMINAL_CONDITIONAL | UNCONDITIONAL_NOT_ESTABLISHED.**
