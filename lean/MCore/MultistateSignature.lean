import MCore.FinalFail.ProblemSignature
import MCore.FinalFail.SevenProblemSignatures

namespace MCore.MultistateSignature

open MCore.FinalFail

/-- Canonical 0/1/2 closure stage. -/
inductive ClosureStage where
  | c0
  | open
  | c2
  deriving DecidableEq, Repr

/-- Small injective codes for every signature coordinate. -/
def codeDirectionality : Directionality → Nat
  | .inward => 0
  | .outward => 1
  | .bidirectional => 2

def codeLocality : Locality → Nat
  | .local => 0
  | .global => 1
  | .localToGlobal => 2

def codeObstruction : ObstructionKind → Nat
  | .primitive => 0
  | .transfer => 1
  | .algebraicity => 2
  | .complexity => 3
  | .rank => 4
  | .residue => 5
  | .spectral => 6

def codeClosure : ClosureKind → Nat
  | .vanishing => 0
  | .positivity => 1
  | .emptiness => 2

def codeScalar : ScalarGeometry → Nat
  | .discrete => 0
  | .real => 1
  | .complex => 2
  | .mixed => 3

def codeBool : Bool → Nat
  | false => 0
  | true => 1

/-- Mixed-radix code of a ProblemSignature.
The chosen bases are strictly larger than each coordinate range. -/
def signatureNumber (s : ProblemSignature) : Nat :=
  codeDirectionality s.direction
  + 3 * (codeLocality s.locality
  + 3 * (codeObstruction s.obstruction
  + 7 * (codeClosure s.closure
  + 3 * (codeScalar s.scalar
  + 4 * (codeBool s.hasCompression
  + 2 * codeBool s.hasRetraction)))))

/-- The same signature number observed in the 0/open/2 closure stages.
The stage tag is part of the state; the invariant numeric signature is preserved. -/
structure MultistateNumber where
  signature : ProblemSignature
  number : Nat
  state : ClosureStage
  invariant : number = signatureNumber signature

def atStage (s : ProblemSignature) (st : ClosureStage) : MultistateNumber where
  signature := s
  number := signatureNumber s
  state := st
  invariant := rfl

/-- Every tracked problem has a canonical multistate numeric signature. -/
def numberOfProblem (p : ProblemId) : Nat :=
  signatureNumber (signatureOf p)

def stateOfProblem (p : ProblemId) (st : ClosureStage) : MultistateNumber :=
  atStage (signatureOf p) st

theorem state_preserves_number (p : ProblemId) (a b : ClosureStage) :
    (stateOfProblem p a).number = (stateOfProblem p b).number := by
  rfl

theorem problem_has_three_states (p : ProblemId) :
    ∃ n : Nat,
      (stateOfProblem p .c0).number = n ∧
      (stateOfProblem p .open).number = n ∧
      (stateOfProblem p .c2).number = n := by
  exact ⟨numberOfProblem p, rfl, rfl, rfl⟩

/-- A signature can be recovered from its number on the finite tracked problem set:
different tracked problems cannot share the same numeric signature. -/
theorem numberOfProblem_injective : Function.Injective numberOfProblem := by
  intro a b h
  apply signature_assignment_injective
  cases a <;> cases b <;> simp [numberOfProblem, signatureNumber, signatureOf,
    codeDirectionality, codeLocality, codeObstruction, codeClosure, codeScalar, codeBool] at h ⊢

/-- Main architectural theorem:
every tracked problem carries one invariant number across the C0/O/C2 states,
and that number uniquely identifies its repository-level signature among the
tracked problems. -/
theorem universal_multistate_signature :
    ∀ p : ProblemId,
      ∃ n : Nat,
        (stateOfProblem p .c0).number = n ∧
        (stateOfProblem p .open).number = n ∧
        (stateOfProblem p .c2).number = n ∧
        (∀ q : ProblemId, numberOfProblem q = n → q = p) := by
  intro p
  refine ⟨numberOfProblem p, rfl, rfl, rfl, ?_⟩
  intro q hq
  exact numberOfProblem_injective hq

#print axioms state_preserves_number
#print axioms problem_has_three_states
#print axioms numberOfProblem_injective
#print axioms universal_multistate_signature

end MCore.MultistateSignature
