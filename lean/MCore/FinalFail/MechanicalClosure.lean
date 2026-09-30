import MCore.FinalFail.DirectProducerCuts

namespace MCore.FinalFail.Semantic

/-!
# Mechanical closure ledger

This file contains obligations that may block packaging or executable closure but
are not OPEN_MATH.  They must never increment the material producer count.

For P vs NP the mathematical producer is G21Pointwise.  P01 is a finite formal
machine-construction obligation and therefore lives here.
-/

inductive MechanicalState where
  | recoveredCandidate
  | pending
  | closed
  deriving DecidableEq, Repr

structure MechanicalClosure where
  problem : ProblemId
  target : String
  evidence : String
  state : MechanicalState
  deriving Repr

def mechanicalClosures : List MechanicalClosure := [
  { problem := .pVsNP
    target := "link preservingRead_forall into the input-node 000++encodeNat(i) evalStep refinement"
    evidence := "m-core-p-vs-np dfe9aec4: preservingRead_forall restores witness exactly and returns witness.getD i false; promotion/kernel audit still required"
    state := .recoveredCandidate },
  { problem := .pVsNP
    target := "global physical verifier execution theorem refining frozen evalRun"
    evidence := "all five finite tags, frame push/pop, cursor/source movement and evaluator semantics already GREEN/FROZEN"
    state := .pending },
  { problem := .pVsNP
    target := "one fixed finite-control NTM composing parser + witness guess + physical verifier"
    evidence := "parser simulation, witness guesser and deterministic-TM-to-NTM transport already certified/reusable"
    state := .pending },
  { problem := .pVsNP
    target := "one polynomial bound proving global HaltsWithin and AcceptsWithin iff SATBits circuitBitEncoding"
    evidence := "local polynomial cost envelopes and phase correctness already available; only global composition remains"
    state := .pending }
]

def mechanicalClosureCount : Nat := mechanicalClosures.length

def pendingMechanicalCount : Nat :=
  mechanicalClosures.foldl
    (fun n lane => if lane.state = .closed then n else n + 1) 0

def closedMechanicalCount : Nat :=
  mechanicalClosures.foldl
    (fun n lane => if lane.state = .closed then n + 1 else n) 0

theorem mechanicalClosureCount_eq_four :
    mechanicalClosureCount = 4 := by
  decide

theorem pendingMechanicalCount_eq_four :
    pendingMechanicalCount = 4 := by
  decide

theorem closedMechanicalCount_eq_zero :
    closedMechanicalCount = 0 := by
  decide

/-- Mechanical obligations are explicitly outside the seven OPEN_MATH slots. -/
theorem material_count_ignores_mechanical :
    openDirectCount = 7 := openDirectCount_eq_seven

end MCore.FinalFail.Semantic
