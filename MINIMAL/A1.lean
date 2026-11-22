import Mathlib

namespace MCoreMinimal

def AmplitudeHomogeneous {U : Type*} [AddCommGroup U] [Module ℝ U]
    (I : U → ℝ) : Prop :=
  ∀ (A : ℝ) (u : U), I (A • u) = A * I u

theorem amplitude_unbounded
    {U : Type*} [AddCommGroup U] [Module ℝ U]
    (I : U → ℝ) (hhom : AmplitudeHomogeneous I)
    {u : U} (hu : 0 < I u) :
    ∀ B : ℝ, ∃ A : ℝ, B < I (A • u) := by
  intro B
  let A : ℝ := (|B| + 1) / I u
  refine ⟨A, ?_⟩
  rw [hhom]
  dsimp [A]
  field_simp
  linarith [le_abs_self B]

theorem A1_NoFixedGap
    {U : Type*} [AddCommGroup U] [Module ℝ U]
    (I : U → ℝ) (hhom : AmplitudeHomogeneous I)
    {u : U} (hu : 0 < I u) :
    ¬ ∃ δ : ℝ, 0 < δ ∧ ∀ A : ℝ, I (A • u) ≤ 1 - δ := by
  rintro ⟨δ, hδ, hgap⟩
  obtain ⟨A, hA⟩ := amplitude_unbounded I hhom hu (1 - δ)
  exact (not_lt_of_ge (hgap A)) hA

end MCoreMinimal
