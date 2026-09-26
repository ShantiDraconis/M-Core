import MCore.FinalFail.SevenProblemSignatures

namespace MCore.FinalFail

/-!
UNIVERSAL MULTISTATE ATK SIGNATURE

This file formalizes the common state architecture found across the ATK lanes.

Important semantic firewall:
* it does NOT assert that all problems share the same mathematical scalar;
* it asserts that all listed ATK problems share the same three-state index
  C0 -> O -> C2;
* the problem-specific mathematical content is carried by the gap shape F1-F8.

Thus the universal "number with multiple states" is the canonical ternary
state code 0/1/2, while each problem has its own terminal gap signature.
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

/-- Full structural signature: common 0/1/2 skeleton plus problem-specific F-shape. -/
structure ATKMultistateSignature where
  problem : ATKProblem
  stageCode : ATKTriState → Nat
  canonicalStageCode : stageCode = triStateCode
  gapShape : ATKGapShape
  correctGapShape : gapShape = gapShapeOfATKProblem problem

/-- Canonical signature assigned to every listed ATK problem. -/
def multistateSignatureOf (p : ATKProblem) : ATKMultistateSignature :=
  { problem := p
    stageCode := triStateCode
    canonicalStageCode := rfl
    gapShape := gapShapeOfATKProblem p
    correctGapShape := rfl }

/-- Every listed problem has the same numerical 0/1/2 state carrier. -/
theorem all_ATK_problems_share_tristate_code
    (p q : ATKProblem) :
    (multistateSignatureOf p).stageCode =
      (multistateSignatureOf q).stageCode := by
  rfl

/-- The common state code is genuinely three-state: 0, 1 and 2 are all hit. -/
theorem tristate_code_hits_zero_one_two :
    (∃ s, triStateCode s = 0) ∧
    (∃ s, triStateCode s = 1) ∧
    (∃ s, triStateCode s = 2) := by
  exact ⟨⟨.C0_closedStart, rfl⟩,
    ⟨⟨.O_openCore, rfl⟩,
      ⟨.C2_closedEnd, rfl⟩⟩⟩

/-- Existential theorem requested by the ATK architecture:
there exists one canonical numerical multistate signature used by every listed
problem, namely the injective state encoding 0/1/2. -/
theorem universal_multistate_number_exists :
    ∃ code : ATKTriState → Nat,
      Function.Injective code ∧
      (∀ s, code s < 3) ∧
      (∀ p : ATKProblem, (multistateSignatureOf p).stageCode = code) := by
  refine ⟨triStateCode, triStateCode_injective, triStateCode_range, ?_⟩
  intro p
  rfl

/-- The invariant part and the varying part are cleanly separated:
all problems share 0/1/2, while F1-F8 identifies the mathematical closure mode. -/
theorem signature_decomposition
    (p : ATKProblem) :
    (multistateSignatureOf p).stageCode = triStateCode ∧
    (multistateSignatureOf p).gapShape = gapShapeOfATKProblem p := by
  exact ⟨rfl, rfl⟩

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
#print axioms MCore.FinalFail.all_ATK_problems_share_tristate_code
#print axioms MCore.FinalFail.universal_multistate_number_exists
#print axioms MCore.FinalFail.signature_decomposition

end MCore.FinalFail
