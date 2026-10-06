import MCore.FinalFail.SevenTerminalParameterLaw

namespace MCore.FinalFail.RPA

/-!
# RPA transition duality

A confirmed OPEN -> CLOSED transition contains both endpoint inhabitants and
an identity-preserving bridge.  The five names below are views of one object;
none of them can manufacture a missing material inhabitant.
-/

structure Transition (Open Closed : Prop) : Prop where
  openSource : Open
  closedTarget : Closed
  preservesIdentity : Open ↔ Closed

def OpenMathClosedMath (Open Closed : Prop) : Prop :=
  Nonempty (Transition Open Closed)

def OpenBridgeClosedBridge (Open Closed : Prop) : Prop :=
  Nonempty (Transition Open Closed)

def Math (Open Closed : Prop) : Prop :=
  Nonempty (Transition Open Closed)

def FinalRoot (Open Closed : Prop) : Prop :=
  Nonempty (Transition Open Closed)

def GlobalExternalCertificate (Open Closed : Prop) : Prop :=
  Nonempty (Transition Open Closed)

theorem transition_iff_source_target_identity
    (Open Closed : Prop) :
    Nonempty (Transition Open Closed) ↔
      Open ∧ Closed ∧ (Open ↔ Closed) := by
  constructor
  · rintro ⟨h⟩
    exact ⟨h.openSource, h.closedTarget, h.preservesIdentity⟩
  · rintro ⟨ho, hc, hid⟩
    exact ⟨⟨ho, hc, hid⟩⟩

theorem cannot_confirm_from_open_alone
    (Open Closed : Prop)
    (hnot : ¬ Closed) :
    Open → ¬ Nonempty (Transition Open Closed) := by
  intro _ h
  rcases h with ⟨t⟩
  exact hnot t.closedTarget

theorem cannot_confirm_from_closed_alone
    (Open Closed : Prop)
    (hnot : ¬ Open) :
    Closed → ¬ Nonempty (Transition Open Closed) := by
  intro _ h
  rcases h with ⟨t⟩
  exact hnot t.openSource

theorem open_closed_eq_bridge
    (Open Closed : Prop) :
    OpenMathClosedMath Open Closed ↔ OpenBridgeClosedBridge Open Closed :=
  Iff.rfl

theorem bridge_eq_math
    (Open Closed : Prop) :
    OpenBridgeClosedBridge Open Closed ↔ Math Open Closed :=
  Iff.rfl

theorem math_eq_finalRoot
    (Open Closed : Prop) :
    Math Open Closed ↔ FinalRoot Open Closed :=
  Iff.rfl

theorem finalRoot_eq_globalExternalCertificate
    (Open Closed : Prop) :
    FinalRoot Open Closed ↔ GlobalExternalCertificate Open Closed :=
  Iff.rfl

theorem five_views_same_identity
    (Open Closed : Prop) :
    (OpenMathClosedMath Open Closed ↔ OpenBridgeClosedBridge Open Closed) ∧
    (OpenBridgeClosedBridge Open Closed ↔ Math Open Closed) ∧
    (Math Open Closed ↔ FinalRoot Open Closed) ∧
    (FinalRoot Open Closed ↔ GlobalExternalCertificate Open Closed) := by
  exact ⟨Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl⟩

/-- A confirmed transition projects both material sides. -/
theorem confirmed_projects_open
    {Open Closed : Prop}
    (h : GlobalExternalCertificate Open Closed) : Open := by
  rcases h with ⟨t⟩
  exact t.openSource

theorem confirmed_projects_closed
    {Open Closed : Prop}
    (h : GlobalExternalCertificate Open Closed) : Closed := by
  rcases h with ⟨t⟩
  exact t.closedTarget

/--
Fail-closed theorem: renaming a transition as MATH / FINAL_ROOT / certificate
does not bypass either endpoint.
-/
theorem global_external_no_escape
    {Open Closed : Prop}
    (h : GlobalExternalCertificate Open Closed) :
    Open ∧ Closed := by
  exact ⟨confirmed_projects_open h, confirmed_projects_closed h⟩

#print axioms MCore.FinalFail.RPA.transition_iff_source_target_identity
#print axioms MCore.FinalFail.RPA.five_views_same_identity
#print axioms MCore.FinalFail.RPA.global_external_no_escape

end MCore.FinalFail.RPA
