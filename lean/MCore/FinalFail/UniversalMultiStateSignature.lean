import MCore.FinalFail.SevenProblemSignatures
import MCore.FinalFail.ExactGapLedger

namespace MCore.FinalFail

/-!
# Universal multistate signature

This file formalizes a meta-classification theorem.  It does not prove any
open mathematical endpoint.

The common object is a three-stage state machine

  C0 -> O -> C2

together with a problem-specific terminal gap form.  A natural-number code is
a canonical, injective encoding of the full classification signature.
-/

/-- The eight problems in the current atlas, including the historically solved
Poincare positive control. -/
inductive AtlasProblemId where
  | riemann
  | yangMills
  | pVsNP
  | beal
  | navierStokes
  | hodge
  | bsd
  | poincare
  deriving DecidableEq, Repr

/-- The common three-state skeleton. -/
inductive MultiStateStage where
  | c0Closed
  | openCore
  | c2Closed
  deriving DecidableEq, Repr

def MultiStateStage.code : MultiStateStage -> Nat
  | .c0Closed => 0
  | .openCore => 1
  | .c2Closed => 2

/-- Terminal shapes in the user's F-taxonomy. -/
inductive GapForm where
  | f1Vanishing
  | f2GapOrSeparation
  | f4Realization
  | f5Equality
  | f6Exclusion
  | f7Limit
  | f8FixedPoint
  deriving DecidableEq, Repr

def GapForm.code : GapForm -> Nat
  | .f1Vanishing => 1
  | .f2GapOrSeparation => 2
  | .f4Realization => 4
  | .f5Equality => 5
  | .f6Exclusion => 6
  | .f7Limit => 7
  | .f8FixedPoint => 8

def gapFormOf : AtlasProblemId -> GapForm
  | .riemann => .f1Vanishing
  | .yangMills => .f2GapOrSeparation
  | .pVsNP => .f2GapOrSeparation
  | .beal => .f6Exclusion
  | .navierStokes => .f7Limit
  | .hodge => .f4Realization
  | .bsd => .f5Equality
  | .poincare => .f8FixedPoint

/-- Human-readable terminal observable.  This is metadata, not evidence. -/
def terminalObservable : AtlasProblemId -> String
  | .riemann => "S_N -> 0"
  | .yangMills => "Delta > 0"
  | .pVsNP => "asymptotic separation / P != NP"
  | .beal => "X_bad = empty"
  | .navierStokes => "limit/regularity closure"
  | .hodge => "cycle-class realization / coker = 0"
  | .bsd => "r_alg = r_an / defect = 0"
  | .poincare => "M simply-connected => M ~= S3"

/-- Status of the mathematical producer, kept separate from the architecture. -/
inductive ProducerState where
  | openMath
  | historicallyProven
  deriving DecidableEq, Repr

def producerStateOf : AtlasProblemId -> ProducerState
  | .poincare => .historicallyProven
  | _ => .openMath

/-- Canonical ordinal for the atlas problem itself. -/
def AtlasProblemId.code : AtlasProblemId -> Nat
  | .riemann => 0
  | .yangMills => 1
  | .pVsNP => 2
  | .beal => 3
  | .navierStokes => 4
  | .hodge => 5
  | .bsd => 6
  | .poincare => 7

/--
The multistate signature.  The three stages are common to every problem; the
F-form and terminal observable identify what must collapse at C2.
-/
structure MultiStateSignature where
  problem : AtlasProblemId
  c0 : MultiStateStage := .c0Closed
  o : MultiStateStage := .openCore
  c2 : MultiStateStage := .c2Closed
  form : GapForm
  observable : String
  producer : ProducerState
  deriving Repr

def multistateSignatureOf (p : AtlasProblemId) : MultiStateSignature :=
  { problem := p
    form := gapFormOf p
    observable := terminalObservable p
    producer := producerStateOf p }

/--
A compact natural-number signature.

Digits/blocks:
  problem-code | F-code | C0 | O | C2 | producer-state

The coding constants are deliberately separated enough that exhaustive kernel
checking can establish injectivity for the finite atlas.
-/
def signatureNumber (p : AtlasProblemId) : Nat :=
  p.code * 100000 +
  (gapFormOf p).code * 1000 +
  MultiStateStage.code .c0Closed * 100 +
  MultiStateStage.code .openCore * 10 +
  MultiStateStage.code .c2Closed +
  match producerStateOf p with
  | .openMath => 0
  | .historicallyProven => 1

/-- Every problem has the same 0 -> 1 -> 2 multistate skeleton. -/
theorem common_three_state_skeleton (p : AtlasProblemId) :
    (multistateSignatureOf p).c0.code = 0 /\
    (multistateSignatureOf p).o.code = 1 /\
    (multistateSignatureOf p).c2.code = 2 := by
  cases p <;> decide

/-- Every problem has a canonical multistate number. -/
theorem multistate_number_exists (p : AtlasProblemId) :
    exists n : Nat, n = signatureNumber p := by
  exact ⟨signatureNumber p, rfl⟩

/-- The number determines the problem inside this atlas. -/
theorem signatureNumber_injective :
    Function.Injective signatureNumber := by
  intro a b h
  cases a <;> cases b <;> simp [signatureNumber, AtlasProblemId.code,
    gapFormOf, GapForm.code, producerStateOf] at h ⊢

/-- The full structural signature is likewise problem-identifying. -/
theorem multistateSignature_injective :
    Function.Injective multistateSignatureOf := by
  intro a b h
  have hp : (multistateSignatureOf a).problem =
      (multistateSignatureOf b).problem :=
    congrArg MultiStateSignature.problem h
  simpa [multistateSignatureOf] using hp

/--
Meta-theorem requested by the multistate attack:
all atlas problems admit one common state architecture and each has a canonical
numerical signature identifying its terminal behavior.
-/
theorem universal_multistate_signature :
    forall p : AtlasProblemId,
      exists n : Nat,
        n = signatureNumber p /\
        (multistateSignatureOf p).c0.code = 0 /\
        (multistateSignatureOf p).o.code = 1 /\
        (multistateSignatureOf p).c2.code = 2 := by
  intro p
  refine ⟨signatureNumber p, rfl, ?_⟩
  exact common_three_state_skeleton p

/--
Important firewall: classification and numerical encoding do not discharge any
OPEN_MATH producer.
-/
theorem signature_does_not_promote_open_math
    (p : AtlasProblemId)
    (h : producerStateOf p = .openMath) :
    (multistateSignatureOf p).producer = .openMath := by
  simpa [multistateSignatureOf] using h

#print axioms MCore.FinalFail.common_three_state_skeleton
#print axioms MCore.FinalFail.multistate_number_exists
#print axioms MCore.FinalFail.signatureNumber_injective
#print axioms MCore.FinalFail.multistateSignature_injective
#print axioms MCore.FinalFail.universal_multistate_signature
#print axioms MCore.FinalFail.signature_does_not_promote_open_math

end MCore.FinalFail
