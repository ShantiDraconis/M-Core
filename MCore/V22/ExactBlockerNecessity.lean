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
  refine ⟨{ problem := .hodge, parent := ⟨.hodge, .middle⟩,
    kind := .hodgeAlgebraicityConstructor,
    expectedArtifact := "forall smooth projective X and rational Hodge class alpha, construct rationalSpanOfCycles alpha" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem bsd_has_exact_blocker : HasExactBlocker .bsd := by
  refine ⟨{ problem := .bsd, parent := ⟨.bsd, .middle⟩,
    kind := .bsdRankConstructor,
    expectedArtifact := "forall BSDArithmeticAnalyticData d, prove BSDRankPart d" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem beal_has_exact_blocker : HasExactBlocker .beal := by
  refine ⟨{ problem := .beal, parent := ⟨.beal, .middle⟩,
    kind := .bealCommonPrimeConstructor,
    expectedArtifact := "forall BealData d, construct CommonPrime d.a d.b d.c" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem pnp_has_exact_blocker : HasExactBlocker .pVsNP := by
  refine ⟨{ problem := .pVsNP, parent := ⟨.pVsNP, .middle⟩,
    kind := .pnpMaterialOrientation,
    expectedArtifact := "either PolySATCertificate + SATCompletenessTransfer, or LowerBoundWitness P NP" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem riemann_has_exact_blocker : HasExactBlocker .riemann := by
  refine ⟨{ problem := .riemann, parent := ⟨.riemann, .middle⟩,
    kind := .rhClassicalZetaAdapter,
    expectedArtifact := "construct ClassicalZetaAdapter with exact zero_match and line_match" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem yangMills_has_exact_blocker : HasExactBlocker .yangMills := by
  refine ⟨{ problem := .yangMills, parent := ⟨.yangMills, .middle⟩,
    kind := .ymConcreteTheoryAdapter,
    expectedArtifact := "construct ConcreteTheoryAdapter matching concrete existence, positivity, and mass-gap semantics" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

theorem navierStokes_has_exact_blocker : HasExactBlocker .navierStokes := by
  refine ⟨{ problem := .navierStokes, parent := ⟨.navierStokes, .middle⟩,
    kind := .nsPointwiseDepletionFromActualNS,
    expectedArtifact := "derive PointwiseClosedDepletion from ActualNS without an oracle" }, ?_, rfl⟩
  simp [exactMathematicalBlockers]

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
