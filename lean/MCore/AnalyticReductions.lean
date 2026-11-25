import Mathlib

namespace MCore.AnalyticReductions

-- Exact finite-dimensional scalar Gram identity.
theorem gram_completion (g b c : ℝ) (hg : g ≠ 0) :
    1 - 2*b*c + g*c^2 = 1 - b^2/g + g*(c-b/g)^2 := by
  field_simp
  <;> ring

theorem gram_lower (g b c : ℝ) (hg : 0 < g) :
    1 - b^2/g ≤ 1 - 2*b*c + g*c^2 := by
  rw [gram_completion g b c hg.ne']
  linarith [mul_nonneg hg.le (sq_nonneg (c-b/g))]

-- Exact logarithmic gain criterion, at the scalar level.
theorem signed_gain {y z s nu delta R : ℝ}
    (h : s ≤ (1-delta)*nu*z + R*y) :
    2*s - 2*nu*z + 2*delta*nu*z ≤ 2*R*y := by
  linarith

-- Failure decomposition does not require coverage.
theorem failure_partition {α : Type*} (F I : α → Prop) :
    (∃ x, F x) ↔ (∃ x, F x ∧ I x) ∨ (∃ x, F x ∧ ¬ I x) := by
  classical
  constructor
  · rintro ⟨x,hx⟩
    by_cases hi : I x
    · exact Or.inl ⟨x,hx,hi⟩
    · exact Or.inr ⟨x,hx,hi⟩
  · rintro (⟨x,hx,_⟩ | ⟨x,hx,_⟩) <;> exact ⟨x,hx⟩

theorem rank_two_sided (a b : ℕ) (h₁ : a ≤ b) (h₂ : b ≤ a) : a = b :=
  le_antisymm h₁ h₂

#print axioms gram_completion
#print axioms gram_lower
#print axioms signed_gain
#print axioms failure_partition
#print axioms rank_two_sided

end MCore.AnalyticReductions
