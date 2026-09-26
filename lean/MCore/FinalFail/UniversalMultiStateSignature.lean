import MCore.FinalFail.TriadicObstructionCalculus
import MCore.FinalFail.SevenProblemSignatures

namespace MCore.FinalFail

/--
A single number-valued object with three distinguished states.
The states are the common structural coordinates 0 -> 1 -> 2.
-/
structure MultiStateNumber where
  value : Fin3 → Nat
  start_eq_zero : value .start = 0
  middle_eq_one : value .middle = 1
  finish_eq_two : value .finish = 2

/-- Canonical common 0/1/2 multistate number. -/
def canonicalMultiStateNumber : MultiStateNumber where
  value
    | .start => 0
    | .middle => 1
    | .finish => 2
  start_eq_zero := rfl
  middle_eq_one := rfl
  finish_eq_two := rfl

theorem canonical_multistate_values :
    canonicalMultiStateNumber.value .start = 0 ∧
    canonicalMultiStateNumber.value .middle = 1 ∧
    canonicalMultiStateNumber.value .finish = 2 := by
  exact ⟨rfl, rfl, rfl⟩

theorem canonical_multistate_injective :
    Function.Injective canonicalMultiStateNumber.value := by
  intro a b h
  cases a <;> cases b <;> simp [canonicalMultiStateNumber] at h ⊢

/--
Per-problem adapter.  The 0/1/2 object is shared; the terminal digit and the
qualitative ProblemSignature identify the problem-specific terminal class.
This is a structural adapter only and does not assert endpoint closure.
-/
structure ProblemMultiStateAdapter where
  problem : ProblemId
  multistate : MultiStateNumber
  multistate_is_canonical : multistate = canonicalMultiStateNumber
  terminalDigit : Nat
  terminalDigit_eq : terminalDigit = slotOf problem
  terminalDigit_range : 3 ≤ terminalDigit ∧ terminalDigit < 10
  signature : ProblemSignature
  signature_eq : signature = signatureOf problem

def problemMultiStateAdapter (p : ProblemId) : ProblemMultiStateAdapter where
  problem := p
  multistate := canonicalMultiStateNumber
  multistate_is_canonical := rfl
  terminalDigit := slotOf p
  terminalDigit_eq := rfl
  terminalDigit_range := slotOf_range p
  signature := signatureOf p
  signature_eq := rfl

/--
Main structural theorem:
there exists one common multistate number whose states are 0,1,2 and which
admits a signature-preserving adapter for every active problem.
-/
theorem exists_multistate_number_in_every_problem :
    ∃ N : MultiStateNumber,
      N.value .start = 0 ∧
      N.value .middle = 1 ∧
      N.value .finish = 2 ∧
      ∀ p : ProblemId,
        ∃ A : ProblemMultiStateAdapter,
          A.problem = p ∧
          A.multistate = N ∧
          A.terminalDigit = slotOf p ∧
          A.signature = signatureOf p := by
  refine ⟨canonicalMultiStateNumber, rfl, rfl, rfl, ?_⟩
  intro p
  refine ⟨problemMultiStateAdapter p, rfl, rfl, rfl, rfl⟩

/--
The terminal numeric signature is unique across the seven problem ids.
-/
theorem terminal_digit_signature_injective :
    Function.Injective slotOf :=
  slotOf_injective

/--
The qualitative signature is also unique across the seven active problem ids.
-/
theorem qualitative_signature_injective :
    Function.Injective signatureOf :=
  signature_assignment_injective

/--
Combined signature: common 0/1/2 dynamics plus problem-specific terminal
digit and qualitative signature.
-/
def fullMultiStateSignature (p : ProblemId) :
    Nat × ProblemSignature :=
  (slotOf p, signatureOf p)

theorem full_multistate_signature_injective :
    Function.Injective fullMultiStateSignature := by
  intro a b h
  have hdigit : slotOf a = slotOf b := congrArg Prod.fst h
  exact slotOf_injective hdigit

/--
Fail-closed scope marker: this theorem closes the universal structural
signature layer only.  It does not discharge any mathematical Core proposition
of the seven individual problems.
-/
def universalMultiStateSignatureLayerClosed : Bool := true

theorem universal_multistate_signature_layer_closed :
    universalMultiStateSignatureLayerClosed = true := by
  rfl

#print axioms MCore.FinalFail.exists_multistate_number_in_every_problem
#print axioms MCore.FinalFail.canonical_multistate_injective
#print axioms MCore.FinalFail.full_multistate_signature_injective
#print axioms MCore.FinalFail.universal_multistate_signature_layer_closed

end MCore.FinalFail
