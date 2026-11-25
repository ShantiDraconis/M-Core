import Mathlib

namespace MCore.RiemannIsolation

theorem isolation_bounds {m t : ℝ} (hm : 1 ≤ m)
    (hl : 1 / (m + 1) < t) (hu : t < 1 / m) :
    1 < 1 / (m * t) ∧ 1 / (m * t) < 2 := by
  have hm0 : 0 < m := by linarith
  have hp : 0 < m + 1 := by linarith
  have ht : 0 < t := lt_trans (div_pos zero_lt_one hp) hl
  have hlow : 1 < t * (m + 1) := (div_lt_iff₀ hp).mp hl
  have hhigh : t * m < 1 := (lt_div_iff₀ hm0).mp hu
  have hmt : 0 < m * t := mul_pos hm0 ht
  constructor
  · apply (lt_div_iff₀ hmt).2
    nlinarith
  · apply (div_lt_iff₀ hmt).2
    nlinarith [mul_nonneg (sub_nonneg.mpr hm) ht.le]

theorem later_generator_bound {m k t : ℝ} (hm : 1 ≤ m)
    (hk : m + 1 ≤ k) (hl : 1 / (m + 1) < t) :
    0 < 1 / (k * t) ∧ 1 / (k * t) < 1 := by
  have hp : 0 < m + 1 := by linarith
  have hk0 : 0 < k := by linarith
  have ht : 0 < t := lt_trans (div_pos zero_lt_one hp) hl
  have hlow := (div_lt_iff₀ hp).mp hl
  have hkt := mul_pos hk0 ht
  refine ⟨div_pos zero_lt_one hkt, (div_lt_iff₀ hkt).2 ?_⟩
  nlinarith [mul_nonneg (sub_nonneg.mpr hk) ht.le]

#print axioms isolation_bounds
#print axioms later_generator_bound
theorem isolated_fract {m t : ℝ} (hm : 1 ≤ m)
    (hl : 1 / (m + 1) < t) (hu : t < 1 / m) :
    Int.fract (1 / (m * t)) = 1 / (m * t) - 1 := by
  obtain ⟨h₁, h₂⟩ := isolation_bounds hm hl hu
  have hf : ⌊1 / (m * t)⌋ = (1 : ℤ) := by
    apply Int.floor_eq_iff.mpr
    exact ⟨by simpa using h₁.le, by simpa using h₂⟩
  simp [Int.fract, hf]

theorem later_fract {m k t : ℝ} (hm : 1 ≤ m)
    (hk : m + 1 ≤ k) (hl : 1 / (m + 1) < t) :
    Int.fract (1 / (k * t)) = 1 / (k * t) := by
  obtain ⟨h₁, h₂⟩ := later_generator_bound hm hk hl
  have hf : ⌊1 / (k * t)⌋ = (0 : ℤ) := by
    apply Int.floor_eq_iff.mpr
    exact ⟨by simpa using h₁.le, by simpa using h₂⟩
  simp [Int.fract, hf]

#print axioms isolated_fract
#print axioms later_fract

theorem triangular_sum {N : ℕ} (v a r : Fin N → ℝ) (m : Fin N)
    (hprev : ∀ k : Fin N, k < m → v k = 0)
    (hdiag : r m = a m - 1)
    (hlater : ∀ k : Fin N, m < k → r k = a k) :
    (∑ k, v k * r k) = (∑ k, v k * a k) - v m := by
  classical
  have h : ∀ k : Fin N, v k * r k =
      v k * a k - (if k = m then v m else 0) := by
    intro k
    rcases lt_trichotomy k m with hk | hk | hk
    · simp [hprev k hk, ne_of_lt hk]
    · subst k
      simp [hdiag] <;> ring
    · simp [hlater k hk, ne_of_gt hk]
  calc
    _ = ∑ k : Fin N, (v k * a k - (if k = m then v m else 0)) :=
      Finset.sum_congr rfl (fun k _ => h k)
    _ = _ := by rw [Finset.sum_sub_distrib]; simp

#print axioms triangular_sum

end MCore.RiemannIsolation
