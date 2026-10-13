# ATK external statement reference (2026-10-13)

Upstream: https://github.com/lean-dojo/LeanMillenniumPrizeProblems
This directory records external interfaces; it does not import, vendor, or claim to prove external statements.

## RH
Upstream: Problems/RiemannHypothesis/Millennium.lean
Target: Millennium.ClayRiemannHypothesis (equivalent to Mathlib RiemannHypothesis according to upstream).
ATK candidate: finiteSpanApproximatesChi / DNLimit_eq_zero.
Required: prove a theorem in the *same Lean environment* mapping the genuine ATK endpoint to the upstream target. Do not assume density or RH as a hypothesis.

## P vs NP
Upstream: Problems/PVersusNP/Millennium.lean
Definitions: Millennium.Language, Millennium.InPolynomialTime, FinEncoding, TM2ComputableInPolyTime.
ATK candidate: P01ConstructionGap and G21Pointwise.
Required: explicit encoding equivalence, polynomial overhead both ways where needed, and a proof of SAT nonmembership in P. Do not confuse counting 2^n assignments with a lower bound.

## Guards
- No sorry, admit, synthetic axioms, or theorem-shaped assumptions equivalent to the goal.
- Check #print axioms and ensure theorem target is faithful to original.
- Hodge and Yang-Mills external statements are marked incomplete upstream.
- No kernel execution or certificate is claimed by this document.
- ATK original producer ledgers remain unchanged.
