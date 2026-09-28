import MCore.FinalFail.BoundaryAtoms
import Mathlib.NumberTheory.LSeries.RiemannZeta

namespace MCore.FinalFail.Semantic

/-- The exact counterexample object selected for the RH lane. -/
structure RiemannOffCriticalZero where
  s : ℂ
  zero : riemannZeta s = 0
  nontrivial : ¬ ∃ n : ℕ, s = -2 * (n + 1)
  notPole : s ≠ 1
  offCriticalLine : s.re ≠ 1 / 2

abbrev RiemannInterpretation :=
  BoundaryInterpretation .riemann RiemannOffCriticalZero

theorem riemann_interpretation_iff_target :
    Nonempty RiemannInterpretation ↔ Nonempty RiemannOffCriticalZero :=
  nonempty_boundaryInterpretation_iff_nonempty_target

/-- Any inhabitant of the selected semantic target really refutes Mathlib's RH
statement; it is not merely an audit label. -/
theorem offCriticalZero_refutes_RH
    (w : RiemannOffCriticalZero) : ¬ RiemannHypothesis := by
  intro h
  exact w.offCriticalLine (h w.s w.zero w.nontrivial w.notPole)

end MCore.FinalFail.Semantic
