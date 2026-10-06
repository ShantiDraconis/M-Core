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


/-! ## Boundary closure: beginning and end are the endpoint pair -/

/--
The endpoint is not an extra proposition beyond the transition.
It is exactly the coexistence of beginning, end, and preserved identity.
-/
def BoundaryEndpoint (Begin End : Prop) : Prop :=
  Begin ∧ End ∧ (Begin ↔ End)

theorem boundaryEndpoint_iff_transition
    (Begin End : Prop) :
    BoundaryEndpoint Begin End ↔ Nonempty (Transition Begin End) := by
  rw [transition_iff_source_target_identity]
  rfl

/--
Beginning and end close the endpoint precisely when both are inhabited and
their logical identity is preserved.
-/
theorem begin_end_close_endpoint
    {Begin End : Prop}
    (hBegin : Begin)
    (hEnd : End)
    (hId : Begin ↔ End) :
    BoundaryEndpoint Begin End := by
  exact ⟨hBegin, hEnd, hId⟩

theorem endpoint_projects_begin
    {Begin End : Prop}
    (h : BoundaryEndpoint Begin End) : Begin :=
  h.1

theorem endpoint_projects_end
    {Begin End : Prop}
    (h : BoundaryEndpoint Begin End) : End :=
  h.2.1

theorem endpoint_preserves_identity
    {Begin End : Prop}
    (h : BoundaryEndpoint Begin End) : Begin ↔ End :=
  h.2.2

/--
Full RPA chain with the endpoint explicitly identified as the begin/end
boundary of the same transition.
-/
theorem boundary_full_chain
    (Begin End : Prop) :
    (BoundaryEndpoint Begin End ↔ OpenMathClosedMath Begin End) ∧
    (OpenMathClosedMath Begin End ↔ OpenBridgeClosedBridge Begin End) ∧
    (OpenBridgeClosedBridge Begin End ↔ Math Begin End) ∧
    (Math Begin End ↔ FinalRoot Begin End) ∧
    (FinalRoot Begin End ↔ GlobalExternalCertificate Begin End) := by
  exact ⟨boundaryEndpoint_iff_transition Begin End,
    Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl⟩

/--
No extra endpoint remains after the boundary is inhabited: every final view
reduces to the same begin/end transition object.
-/
theorem endpoint_no_extra_parameter
    (Begin End : Prop) :
    BoundaryEndpoint Begin End ↔ GlobalExternalCertificate Begin End := by
  exact (boundaryEndpoint_iff_transition Begin End).trans Iff.rfl

#print axioms MCore.FinalFail.RPA.boundaryEndpoint_iff_transition
#print axioms MCore.FinalFail.RPA.begin_end_close_endpoint
#print axioms MCore.FinalFail.RPA.boundary_full_chain
#print axioms MCore.FinalFail.RPA.endpoint_no_extra_parameter

end MCore.FinalFail.RPA
