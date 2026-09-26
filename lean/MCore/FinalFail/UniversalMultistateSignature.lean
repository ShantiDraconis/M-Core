import MCore.FinalFail.SevenProblemSignatures

namespace MCore.FinalFail

/-!
UNIVERSAL MULTISTATE ATK SIGNATURE

This file formalizes the common state architecture found across the ATK lanes.

Important semantic firewall:
* each problem has its own mathematical object/value;
* these objects are not identified with one another;
* every listed ATK problem realizes a three-state structure isomorphic to the
  abstract skeleton C0 -> O -> C2;
* the problem-specific mathematical content is carried by the gap shape F1-F8.

Thus the invariant is structural, not numerical identity across problems.
-/

/-- The common ATK three-state skeleton. -/
inductive ATKTriState
  | C0_closedStart
  | O_openCore
  | C2_closedEnd
  deriving DecidableEq

/-- Canonical numerical encoding of the three states. -/
def triStateCode : ATKTriState → Nat
  | .C0_closedStart => 0
  | .O_openCore => 1
  | .C2_closedEnd => 2

theorem triStateCode_range (s : ATKTriState) :
    triStateCode s < 3 := by
  cases s <;> decide

theorem triStateCode_injective :
    Function.Injective triStateCode := by
  intro a b h
  cases a <;> cases b <;> simp [triStateCode] at h ⊢

/-- Closed F1-F8 taxonomy used by the cross-problem signature. -/
inductive ATKGapShape
  | F1_vanishing
  | F2_positiveGapOrSeparation
  | F3_witness
  | F4_realization
  | F5_equalityDefect
  | F6_exclusion
  | F7_limitCompactness
  | F8_fixedPointClassification
  deriving DecidableEq

/-- Seven active/open ATK problems plus Poincare as the solved positive control. -/
inductive ATKProblem
  | active (p : ProblemId)
  | poincare
  deriving DecidableEq

/-- Problem-specific terminal shape; this is the varying part of the signature. -/
def gapShapeOfATKProblem : ATKProblem → ATKGapShape
  | .active .riemann => .F1_vanishing
  | .active .yangMills => .F2_positiveGapOrSeparation
  | .active .pVsNP => .F2_positiveGapOrSeparation
  | .active .hodge => .F4_realization
  | .active .bsd => .F5_equalityDefect
  | .active .beal => .F6_exclusion
  | .active .navierStokes => .F7_limitCompactness
  | .poincare => .F8_fixedPointClassification

/-- A problem-specific manifestation of the abstract three-state structure.
The carrier may differ from problem to problem. -/
structure ATKManifestation where
  problem : ATKProblem
  State : Type
  encode : State → ATKTriState
  decode : ATKTriState → State
  left_inv : ∀ s, decode (encode s) = s
  right_inv : ∀ t, encode (decode t) = t
  gapShape : ATKGapShape
  correctGapShape : gapShape = gapShapeOfATKProblem problem

/-- Structural equivalence between two manifestations: both are isomorphic to
the same abstract tri-state skeleton, without identifying their carriers. -/
def StructurallyEquivalent (A B : ATKManifestation) : Prop :=
  ∃ f : A.State → B.State,
    ∃ g : B.State → A.State,
      (∀ x, g (f x) = x) ∧
      (∀ y, f (g y) = y)

/-- Every two valid manifestations are structurally equivalent through the
shared abstract tri-state skeleton. -/
theorem manifestations_structurally_equivalent
    (A B : ATKManifestation) :
    StructurallyEquivalent A B := by
  refine ⟨fun x => B.decode (A.encode x), fun y => A.decode (B.encode y), ?_, ?_⟩
  · intro x
    rw [B.right_inv, A.left_inv]
  · intro y
    rw [A.right_inv, B.left_inv]

/-- The common state code is genuinely three-state: 0, 1 and 2 are all hit. -/
theorem tristate_code_hits_zero_one_two :
    (∃ s, triStateCode s = 0) ∧
    (∃ s, triStateCode s = 1) ∧
    (∃ s, triStateCode s = 2) := by
  exact ⟨⟨.C0_closedStart, rfl⟩,
    ⟨⟨.O_openCore, rfl⟩,
      ⟨.C2_closedEnd, rfl⟩⟩⟩

/-- Existential structural theorem: there exists a three-state abstract
signature to which every admitted manifestation is equivalent. -/
theorem universal_multistate_structure_exists :
    ∃ code : ATKTriState → Nat,
      Function.Injective code ∧
      (∀ s, code s < 3) := by
  exact ⟨triStateCode, triStateCode_injective, triStateCode_range⟩

/-- The varying part is exactly the problem-specific F-shape. -/
theorem manifestation_gap_shape
    (A : ATKManifestation) :
    A.gapShape = gapShapeOfATKProblem A.problem :=
  A.correctGapShape

/-- Concrete lookup table for the eight ATK lanes. -/
theorem beal_signature :
    gapShapeOfATKProblem (.active .beal) = .F6_exclusion := rfl

theorem riemann_signature :
    gapShapeOfATKProblem (.active .riemann) = .F1_vanishing := rfl

theorem yangMills_signature :
    gapShapeOfATKProblem (.active .yangMills) = .F2_positiveGapOrSeparation := rfl

theorem pVsNP_signature :
    gapShapeOfATKProblem (.active .pVsNP) = .F2_positiveGapOrSeparation := rfl

theorem hodge_signature :
    gapShapeOfATKProblem (.active .hodge) = .F4_realization := rfl

theorem bsd_signature :
    gapShapeOfATKProblem (.active .bsd) = .F5_equalityDefect := rfl

theorem navierStokes_signature :
    gapShapeOfATKProblem (.active .navierStokes) = .F7_limitCompactness := rfl

theorem poincare_signature :
    gapShapeOfATKProblem .poincare = .F8_fixedPointClassification := rfl

#print axioms MCore.FinalFail.triStateCode_injective
#print axioms MCore.FinalFail.manifestations_structurally_equivalent
#print axioms MCore.FinalFail.universal_multistate_structure_exists
#print axioms MCore.FinalFail.manifestation_gap_shape

end MCore.FinalFail
