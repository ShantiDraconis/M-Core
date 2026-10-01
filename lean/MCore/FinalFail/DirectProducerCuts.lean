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
    target := "LogMajorantCertificate concreteNBData concreteGeneratorFamily: ∃ K≥0, ∀ N, DN(N) ≤ K / log(N+2)"
    reduction := "atk/rh-gram-final-closure-20261001 proves logMajorant(K,N)=K/log(N+2) tends to zero and constructs VanishingUpperBound, DNToZero, DNLimit=0 and FINAL_ROOT from this certificate. Gram normal equations, optimal coefficients and the exact Gram residual equivalence are already closed. The sole material residue on this route is the concrete uniform logarithmic upper bound."
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
    target := "ActualNS → genuine StretchSplit + BulkAbsorption + ExceptionalTailControl + SubcriticalBudget"
    reduction := "StrictSignedDepletionProducer already proves BulkAbsorption + ExceptionalTailControl + SubcriticalBudget ⇒ ∃ theta, 0≤theta<1 and stretch≤theta*nu*z. K1aExactFrechetProducer also closes the regularized-direction Frechet derivative and chain rule. Therefore theta<1 is downstream, not an independent gap; the material residue is deriving the bulk/tail split and strict budget from genuine Navier-Stokes dynamics."
    state := .openMath },
  { problem := .hodge
    target := "Nonempty (ConcreteHodgeMaterialTarget G M) on the intended nonempty graded Hodge model"
    reduction := "The bare ConcreteAlgebraicityPayload admits a vacuous empty-variety model. The hardened target (commit f1f0f848d97c32221c2d929451b0f05b907a1ee0) requires Nonempty G.Variety + CycleSpanAdapter G M + ConcreteAlgebraicityPayload M, projects to the prior payload, and closes the same graded Hodge endpoint without the empty-model loophole."
    state := .openMath },
  { problem := .bsd
    target := "concrete elliptic-curve realizability semantics + high-rank residual + refined leading-coefficient identity on the same curve"
    reduction := "HighRankDomainGapClosure formally refutes blanket realizability on BSDArithmeticAnalyticData. RealizableRankFrontier proves that, once a genuine realizability predicate and valid low-rank contract are fixed, universal rank reduces to the analytic-rank≥2 residual. The refined leading-coefficient formula remains independent. Thus the abstract domain is closed negatively; the next material object must bind actual elliptic curves and their analytic/arithmetic invariants."
    state := .openMath },
  { problem := .yangMills
    target := "field-level B60 realization: state/observable maps + physicality + K23 inputs + K25 clustering bridges + K27 regulated-gap/limit bridge + nonvacuum excitation + K30 transfer witness"
    reduction := "ExactFinalProducer.finalExternal_of_fields already constructs the B60 FinalExternal object and FINAL_ROOT from these narrower fields; K22 construction/infrared/limit blocks are downstream and are not independent gaps. B60InhabitationMining searches existing declarations field-by-field. The material task is therefore to inhabit these fixed physical fields on one common regulated 4D model."
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
