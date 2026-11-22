import Mathlib

namespace MCoreMinimal

structure TwoPathLimitFailure where
  limit₁ : ℝ
  limit₂ : ℝ
  distinct : limit₁ ≠ limit₂

theorem A3_NoCommonExtension (h : TwoPathLimitFailure) :
    ¬ ∃ L : ℝ, L = h.limit₁ ∧ L = h.limit₂ := by
  rintro ⟨L, h1, h2⟩
  apply h.distinct
  rw [← h1, ← h2]

end MCoreMinimal
