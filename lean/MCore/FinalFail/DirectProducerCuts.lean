import MCore.FinalFail.SemanticParallel

namespace MCore.FinalFail.Semantic

/-!
# Direct producer min-cuts

Forward-only ledger after the semantic frontier audit.

Each entry names the smallest currently admissible material producer.  These are
not wrappers around BoundaryAtom and are not promoted by accepted hypotheses.
The only way to move an entry from OPEN_MATH is to construct the named target
(or a strictly stronger object with a kernel-checked projection to it).
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
    target := "RiemannOffCriticalZero"
    reduction := "¬RiemannHypothesis ↔ Nonempty RiemannOffCriticalZero; unconditional witness still absent"
    state := .openMath },
  { problem := .beal
    target := "universal CommonPrime/CommonDivisor producer on canonical BealData"
    reduction := "CommonPrime ↔ nontrivial CommonDivisor is proved; conductor/level route has not produced the universal divisor"
    state := .openMath },
  { problem := .pVsNP
    target := "genuine LowerBoundWitness on the fixed official model (or genuine PolySATCertificate + completeness transfer)"
    reduction := "MaterialOrientation is the exact two-sided material cut; materialOrientationBuilt = false on the frozen base"
    state := .openMath },
  { problem := .navierStokes
    target := "ActualNS → G1Bridge / strict signed-depletion producer"
    reduction := "bulk + tail + strict budget → signed depletion is proved; deriving those certificates from ActualNS remains open"
    state := .openMath },
  { problem := .hodge
    target := "ConcreteAlgebraicityPayload / universal R2 cycle production"
    reduction := "R2 on the constant Qbar regression family is equivalent to the original concrete algebraicity payload"
    state := .openMath },
  { problem := .bsd
    target := "realizable elliptic-curve rank equality + refined leading-coefficient/Sha formula on the same domain"
    reduction := "the unrestricted abstract forall is counter-audited; rank and refined obligations remain material"
    state := .openMath },
  { problem := .yangMills
    target := "B60ConcretePhysicalAdapter with genuine 4D realization, IR/limit control, non-vacuum physical state, and K30 transfer witness"
    reduction := "B3/B4/B5 legacy interfaces are insufficient; B60 is the fail-closed physical min-cut"
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
