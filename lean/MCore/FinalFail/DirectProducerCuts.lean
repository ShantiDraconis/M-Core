import MCore.FinalFail.SemanticParallel
import MCore.FinalFail.BSDConcreteDomain

namespace MCore.FinalFail.Semantic

/-!
# Direct producer min-cuts

Forward-only ledger after the semantic frontier audit.

Each entry names the smallest currently admissible material producer. These are
not wrappers around BoundaryAtom and are not promoted by accepted hypotheses.
The only way to move an entry from OPEN_MATH is to construct the named target
(or a strictly stronger object with a kernel-checked projection to it).

This file is aligned to the canonical per-repository GATE_LEDGER.json frontiers
audited through 2026-10-01, including the post-P01 and concrete Gram frontiers.
-/

inductive DirectProducerState where
  | openMath
  | produced
  deriving DecidableEq, Repr

structure DirectProducerCut where
  problem : ProblemId
  target : String
  reduction : String
  state : DirectProducerState
  deriving Repr

def directProducerCuts : List DirectProducerCut := [
  { problem := .riemann
    target := "Concrete Gram scalar endpoint: ∀ ε>0, ∃ N,c, G_N c = b_N ∧ 1 - cᵀb_N < ε²"
    reduction := "The advanced RH branches prove this endpoint equivalent to DNLimit=0 and FiniteSpanApproximatesChi for the concrete generator family. Normal equations and optimal finite coefficients are already constructed; only the scalar defect tending to zero remains OPEN_MATH."
    state := .openMath },
  { problem := .beal
    target := "GCDLowerBoundProducer: ∀ d : BealData, 1 < Nat.gcd d.a (Nat.gcd d.b d.c)"
    reduction := "m-core-beal freezes bealConjecture_iff_gcdLowerBoundProducer and the CommonDivisor/CommonPrime projections on the positive Beal domain; the universal scalar gcd lower bound remains OPEN_MATH."
    state := .openMath },
  { problem := .pVsNP
    target := "UniversalSATLowerBound / UniversalFailure for the canonical SAT bit-language"
    reduction := "P01ConstructionGap is CLOSED_KERNEL_GREEN_FROZEN_CERTIFIED at frozen SHA 720596c0bd3900b5de25eab57b7b979d2a6aaf68 (run 36862291065), yielding canonical SAT-in-NP. The sole remaining material producer is ∀ M : PolyDTMCandidate, ∃ x, ¬ M.CorrectAt SAT x; the consolidated kernel proves equivalence with CanonicalSATP02Producer, NormalizedAdversary, G21Pointwise, and SAT∉P. UniformEffectiveCoverage is only a sufficient constructive route and still contains the genuine semantic realizer obligation."
    state := .openMath },
  { problem := .navierStokes
    target := "NSProducerFirst.ActualNSToSignedGainCore on genuine flow-derived EnstrophyData"
    reduction := "The frozen signed-gain core keeps exactly theta < 1 and stretch(t) ≤ theta*nu*z(t) + C*y(t)^2; all normalization and downstream differential consequences are certified. The PDE-derived producer from ActualNS remains OPEN_MATH."
    state := .openMath },
  { problem := .hodge
    target := "Nonempty (ConcreteHodgeMaterialTarget G M) on the intended nonempty graded Hodge model"
    reduction := "The bare ConcreteAlgebraicityPayload admits a vacuous empty-variety model. The hardened target (commit f1f0f848d97c32221c2d929451b0f05b907a1ee0) requires Nonempty G.Variety + CycleSpanAdapter G M + ConcreteAlgebraicityPayload M, projects to the prior payload, and closes the same graded Hodge endpoint without the empty-model loophole."
    state := .openMath },
  { problem := .bsd
    target := "realizable elliptic-curve domain + universal rank equality + refined leading-coefficient identity on that same domain"
    reduction := "The abstract BSDArithmeticAnalyticData universal contract is rejected by a certified firewall because it admits unrelated Nat data. Progress requires binding genuine elliptic-curve arithmetic/analytic data first, then proving BSD rank equality and the refined formula on that realizable domain."
    state := .openMath },
  { problem := .yangMills
    target := "Nonempty (B60ConcretePhysicalAdapter C F D H G O)"
    reduction := "The frozen B3-B5 hardening blocks phantom witnesses; B60ConcretePhysicalAdapter is the current sufficient material producer tying the regulated 4D construction to the same physical Hilbert/Hamiltonian/K30 data. No B60 inhabitant is currently supplied."
    state := .openMath }
]

def directProducerCutCount : Nat := directProducerCuts.length

def producedDirectCount : Nat :=
  directProducerCuts.foldl
    (fun n lane => if lane.state = .produced then n + 1 else n) 0

def openDirectCount : Nat :=
  directProducerCuts.foldl
    (fun n lane => if lane.state = .openMath then n + 1 else n) 0

theorem directProducerCutCount_eq_seven :
    directProducerCutCount = 7 := by
  decide

theorem producedDirectCount_eq_zero :
    producedDirectCount = 0 := by
  decide

theorem openDirectCount_eq_seven :
    openDirectCount = 7 := by
  decide

/-- No-wrapper invariant at the administrative layer: merely accepting all
semantic hypotheses does not mutate the direct-producer ledger. -/
theorem accepted_semantics_do_not_move_direct_count :
    assumedSemanticLaneCount = 7 ∧ producedDirectCount = 0 := by
  exact ⟨assumedSemanticLaneCount_eq_seven, producedDirectCount_eq_zero⟩

end MCore.FinalFail.Semantic
