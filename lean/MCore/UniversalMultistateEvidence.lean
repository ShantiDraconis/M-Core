import MCore.FinalFail.SevenProblemSignatures
import MCore.FinalFail.ExactGapLedger

namespace MCore.UniversalMultistateEvidence

open MCore.FinalFail

/-- The common structural coordinate.  These are structural positions, not
problem-specific values. -/
inductive StructuralState where
  | start
  | obstruction
  | terminal
  deriving DecidableEq, Repr

def structuralNumber : StructuralState → Nat
  | .start => 0
  | .obstruction => 1
  | .terminal => 2

/-- Different mathematical manifestations of the same structural skeleton. -/
inductive ManifestationKind where
  | vanishing
  | positiveGap
  | separation
  | realization
  | equality
  | exclusion
  | limitClosure
  | fixedPointClassification
  deriving DecidableEq, Repr

def manifestationOf : ProblemId → ManifestationKind
  | .beal => .exclusion
  | .navierStokes => .limitClosure
  | .hodge => .realization
  | .pVsNP => .separation
  | .bsd => .equality
  | .riemann => .vanishing
  | .yangMills => .positiveGap

/-- A problem-specific realization of the same structural state. -/
structure Realization where
  problem : ProblemId
  state : StructuralState
  number : Nat
  kind : ManifestationKind
  signature : ProblemSignature
  obstruction : TerminalObstruction
  number_ok : number = structuralNumber state
  kind_ok : kind = manifestationOf problem
  signature_ok : signature = signatureOf problem
  obstruction_ok : obstruction = obstructionOf problem

def realize (p : ProblemId) (s : StructuralState) : Realization where
  problem := p
  state := s
  number := structuralNumber s
  kind := manifestationOf p
  signature := signatureOf p
  obstruction := obstructionOf p
  number_ok := rfl
  kind_ok := rfl
  signature_ok := rfl
  obstruction_ok := rfl

/-- First invariant: every active problem carries exactly the same 0/1/2
structural coordinate. -/
theorem common_three_state_skeleton (p : ProblemId) :
    (realize p .start).number = 0 ∧
    (realize p .obstruction).number = 1 ∧
    (realize p .terminal).number = 2 := by
  exact ⟨rfl, rfl, rfl⟩

/-- Second invariant: changing the problem does not change the structural
number at a fixed state. -/
theorem same_number_different_problem
    (p q : ProblemId) (s : StructuralState) :
    (realize p s).number = (realize q s).number := by
  rfl

/-- Evidence bridge: the problem-specific signature in each realization
carries exactly the terminal obstruction already certified by the existing
SevenProblemSignatures theorem. -/
theorem realization_preserves_existing_obstruction
    (p : ProblemId) (s : StructuralState) :
    (realize p s).signature.obstruction =
      match (realize p s).obstruction with
      | .primitiveSolution => .primitive
      | .signedTransferDefect => .transfer
      | .nonAlgebraicHodgeClass => .algebraicity
      | .polynomialSATDecider => .complexity
      | .rankMismatch => .rank
      | .nonzeroDNLimit => .residue
      | .nonpositiveSpectralGap => .spectral := by
  simpa [realize] using signature_obstruction_matches p

/-- Distinct active problems remain distinct manifestations: sharing the
0/1/2 skeleton does not identify their signatures. -/
theorem distinct_problem_signatures
    {p q : ProblemId} (h : p ≠ q) (s : StructuralState) :
    (realize p s).signature ≠ (realize q s).signature := by
  intro hs
  apply h
  apply signature_assignment_injective
  simpa [realize] using hs

/-- Poincare is recorded in the existing exact-gap evidence ledger as the
historically solved control case. -/
theorem poincare_control_present :
    ∃ g ∈ exactGaps,
      g.problem = "POINCARE" ∧
      g.state = GapState.historicallySolvedToAudit := by
  refine ⟨exactGaps[1], ?_, ?_, ?_⟩
  · simp [exactGaps]
  · simp [exactGaps]
  · simp [exactGaps]

/-- Main cross-problem theorem.
The common object is the 0/1/2 structural number.  Its manifestation is
problem-specific and is anchored to the already-existing signature and
terminal-obstruction evidence. -/
theorem universal_structure_distinct_manifestations :
    ∀ p : ProblemId,
      (realize p .start).number = 0 ∧
      (realize p .obstruction).number = 1 ∧
      (realize p .terminal).number = 2 ∧
      (realize p .terminal).kind = manifestationOf p ∧
      (realize p .terminal).signature = signatureOf p ∧
      (realize p .terminal).obstruction = obstructionOf p := by
  intro p
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

#print axioms common_three_state_skeleton
#print axioms same_number_different_problem
#print axioms realization_preserves_existing_obstruction
#print axioms distinct_problem_signatures
#print axioms poincare_control_present
#print axioms universal_structure_distinct_manifestations

end MCore.UniversalMultistateEvidence
