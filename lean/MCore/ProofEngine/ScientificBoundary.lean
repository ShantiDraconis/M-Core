import MCore.ProofEngine.Registry

namespace MCore.ProofEngine

structure ScientificEvidence (S : Prop) where
  proof : Option S
  refutation : Option (Not S)

def CanIssue {S : Prop} (e : ScientificEvidence S) : Prop :=
  e.proof.isSome ∧ e.refutation.isNone

theorem empty_cannot_issue (S : Prop) :
    ¬ CanIssue (ScientificEvidence.mk (S := S) none none) := by
  simp [CanIssue]

theorem conflict_cannot_issue {S : Prop} (hS : S) (hnS : ¬ S) :
    ¬ CanIssue (ScientificEvidence.mk (some hS) (some hnS)) := by
  simp [CanIssue]

end MCore.ProofEngine
