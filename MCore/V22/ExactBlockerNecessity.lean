import MCore.V22.ExactBlockers
import MCore.V22.BidirectionalClosure

namespace MCore.V22

/-!
Exact-blocker necessity layer.

This module proves only structural facts already encoded by the registry.
It deliberately does not prove any open mathematical endpoint.
-/

def HasExactBlocker (p : ProblemId) : Prop :=
  ∃ b ∈ exactMathematicalBlockers, b.problem = p

theorem blocker_mem_implies_hasExactBlocker
    {b : ExactBlocker}
    (hb : b ∈ exactMathematicalBlockers) :
    HasExactBlocker b.problem := by
  exact ⟨b, hb, rfl⟩

theorem hodge_has_exact_blocker : HasExactBlocker .hodge := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[0]!) (by native_decide)

theorem bsd_has_exact_blocker : HasExactBlocker .bsd := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[1]!) (by native_decide)

theorem beal_has_exact_blocker : HasExactBlocker .beal := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[2]!) (by native_decide)

theorem pnp_has_exact_blocker : HasExactBlocker .pVsNP := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[3]!) (by native_decide)

theorem riemann_has_exact_blocker : HasExactBlocker .riemann := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[4]!) (by native_decide)

theorem yangMills_has_exact_blocker : HasExactBlocker .yangMills := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[6]!) (by native_decide)

theorem navierStokes_has_exact_blocker : HasExactBlocker .navierStokes := by
  exact blocker_mem_implies_hasExactBlocker (b := exactMathematicalBlockers[8]!) (by native_decide)

def OpenResearchProblem (p : ProblemId) : Prop :=
  p = .hodge ∨ p = .bsd ∨ p = .beal ∨ p = .pVsNP ∨
  p = .riemann ∨ p = .yangMills ∨ p = .navierStokes

theorem open_problem_has_registered_exact_blocker
    {p : ProblemId} (hp : OpenResearchProblem p) :
    HasExactBlocker p := by
  rcases hp with rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact hodge_has_exact_blocker
  · exact bsd_has_exact_blocker
  · exact beal_has_exact_blocker
  · exact pnp_has_exact_blocker
  · exact riemann_has_exact_blocker
  · exact yangMills_has_exact_blocker
  · exact navierStokes_has_exact_blocker

/-- A registered blocker is a research obligation, not a proof hypothesis.
    Closure requires an explicit discharge object supplied by the problem repo. -/
structure BlockerDischarge (b : ExactBlocker) where
  witnessType : Type
  witness : witnessType
  validates : witnessType → Prop
  valid : validates witness

def AllBlockersDischarged
    (D : (b : ExactBlocker) → b ∈ exactMathematicalBlockers → Prop) : Prop :=
  ∀ (b : ExactBlocker) (hb : b ∈ exactMathematicalBlockers), D b hb

end MCore.V22
