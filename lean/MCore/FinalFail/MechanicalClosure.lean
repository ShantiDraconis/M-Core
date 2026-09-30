import MCore.FinalFail.DirectProducerCuts

namespace MCore.FinalFail.Semantic

/-!
# Mechanical closure ledger

Mechanical obligations may block executable packaging, but never increment
OPEN_MATH.  All P01 wiring has been compressed through the already-proved
integrated assembly theorem:

  P01PrepPhase + P01VerifierPhase -> P01MachineConstruction.

The prep phase is already inhabited on the advanced P01 line.  Therefore the
only remaining mechanical min-cut is one verifier-phase inhabitant.
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
    target := "P01VerifierPhase P01WitnessPrepGlobal.prepPhase.layout"
    evidence := "P01WitnessPrepGlobal.prepPhase and P01IntegratedAssembly.p01_of_verifier give an exact structural reduction from one verifier-phase inhabitant to P01ConstructionGap. A 2026-09-30 clean rebuild of the stronger exact-verifier candidate exposed broken imports, unresolved helper names and sorryAx in its dependency footprint, so no canonical exact-verifier closure is credited here."
    state := .pending }
]

def mechanicalClosureCount : Nat := mechanicalClosures.length

def pendingMechanicalCount : Nat :=
  mechanicalClosures.foldl
    (fun n lane => if lane.state = .closed then n else n + 1) 0

def closedMechanicalCount : Nat :=
  mechanicalClosures.foldl
    (fun n lane => if lane.state = .closed then n + 1 else n) 0

theorem mechanicalClosureCount_eq_one :
    mechanicalClosureCount = 1 := by
  decide

theorem pendingMechanicalCount_eq_one :
    pendingMechanicalCount = 1 := by
  decide

theorem closedMechanicalCount_eq_zero :
    closedMechanicalCount = 0 := by
  decide

/-- Mechanical obligations are explicitly outside the seven OPEN_MATH slots. -/
theorem material_count_ignores_mechanical :
    openDirectCount = 7 := openDirectCount_eq_seven

end MCore.FinalFail.Semantic
