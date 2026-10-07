namespace MCore.FinalFail.ClosedScope

/-!
# Global CLOSED_MATH-only certificate

This module certifies only propositions explicitly supplied as already-closed
mathematical obligations. It deliberately has no OPEN_MATH field and makes no
claim about obligations outside its scope.

The certificate is therefore a scoped aggregate, not a proof that every
Millennium endpoint is closed.
-/

/-- One material obligation admitted to the CLOSED_MATH-only scope.
Membership requires the proposition itself together with its witness. -/
structure ClosedMathEntry : Type 1 where
  statement : Prop
  witness : statement

/-- A finite, auditable collection of CLOSED_MATH entries. -/
structure GlobalClosedScope : Type 1 where
  entries : List ClosedMathEntry

/-- Every entry in a GlobalClosedScope carries its material witness by
construction. -/
theorem entry_is_closed
    (C : GlobalClosedScope)
    (e : ClosedMathEntry)
    (hmem : e ∈ C.entries) :
    e.statement := by
  exact e.witness

/-- The global scoped certificate is the conjunction-like assertion that every
registered CLOSED_MATH entry is inhabited. -/
def GlobalClosedScopeCertificate (C : GlobalClosedScope) : Prop :=
  ∀ e, e ∈ C.entries → e.statement

/-- Any well-formed CLOSED_MATH-only scope produces its scoped certificate.
This theorem does not create endpoint proofs: each witness was required when
its ClosedMathEntry was constructed. -/
theorem certify (C : GlobalClosedScope) :
    GlobalClosedScopeCertificate C := by
  intro e hmem
  exact entry_is_closed C e hmem

/-- Adding an already witnessed CLOSED_MATH proposition preserves global
scoped certification. -/
def cons
    (P : Prop)
    (hP : P)
    (C : GlobalClosedScope) :
    GlobalClosedScope :=
  ⟨⟨P, hP⟩ :: C.entries⟩

theorem certify_cons
    (P : Prop)
    (hP : P)
    (C : GlobalClosedScope) :
    GlobalClosedScopeCertificate (cons P hP C) :=
  certify _

#print axioms MCore.FinalFail.ClosedScope.entry_is_closed
#print axioms MCore.FinalFail.ClosedScope.certify
#print axioms MCore.FinalFail.ClosedScope.certify_cons

end MCore.FinalFail.ClosedScope
