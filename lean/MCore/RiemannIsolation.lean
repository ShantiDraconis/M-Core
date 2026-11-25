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
    constructor
    · simpa only [Int.cast_one] using h₁.le
    · simpa only [Int.cast_one, one_add_one_eq_two] using h₂
  simp only [Int.fract, hf, Int.cast_one]

theorem later_fract {m k t : ℝ} (hm : 1 ≤ m)
    (hk : m + 1 ≤ k) (hl : 1 / (m + 1) < t) :
    Int.fract (1 / (k * t)) = 1 / (k * t) := by
  obtain ⟨h₁, h₂⟩ := later_generator_bound hm hk hl
  have hf : ⌊1 / (k * t)⌋ = (0 : ℤ) := by
    apply Int.floor_eq_iff.mpr
    constructor
    · simpa only [Int.cast_zero] using h₁.le
    · simpa only [Int.cast_zero, zero_add] using h₂
  simp only [Int.fract, hf, Int.cast_zero, sub_zero]

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

theorem triangular_zero {N : ℕ} (v a r : Fin N → ℝ) (m : Fin N)
    (hprev : ∀ k : Fin N, k < m → v k = 0)
    (hdiag : r m = a m - 1)
    (hlater : ∀ k : Fin N, m < k → r k = a k)
    (ha : (∑ k, v k * a k) = 0)
    (hr : (∑ k, v k * r k) = 0) : v m = 0 := by
  have h := triangular_sum v a r m hprev hdiag hlater
  rw [ha, hr] at h
  linarith

#print axioms triangular_zero

theorem triangular_all_zero {N : ℕ} (v : Fin N → ℝ)
    (a r : Fin N → Fin N → ℝ)
    (hdiag : ∀ m, r m m = a m m - 1)
    (hlater : ∀ m k, m < k → r m k = a m k)
    (ha : ∀ m, (∑ k, v k * a m k) = 0)
    (hr : ∀ m, (∑ k, v k * r m k) = 0) :
    ∀ m, v m = 0 := by
  have h : ∀ n : ℕ, ∀ m : Fin N, m.val = n → v m = 0 := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro m hm
      apply triangular_zero v (a m) (r m) m
      · intro k hk
        apply ih k.val
        · have hlt : k.val < m.val := hk
          rw [hm] at hlt
          exact hlt
        · rfl
      · exact hdiag m
      · exact hlater m
      · exact ha m
      · exact hr m
  exact fun m => h m.val m rfl

#print axioms triangular_all_zero

/-- A relation is an exact object, independently of its truth. -/
structure RelationalNumber where
  sentence : Prop

def zeroEndpoint (d : ℝ) : RelationalNumber := ⟨d = 0⟩

def RelationalNumber.Valid (r : RelationalNumber) : Prop := r.sentence

theorem endpoint_valid_iff (d : ℝ) :
    (zeroEndpoint d).Valid ↔ d = 0 := Iff.rfl

theorem endpoint_exists (d : ℝ) : Nonempty RelationalNumber :=
  ⟨zeroEndpoint d⟩

theorem endpoint_not_automatically_valid :
    ¬ (zeroEndpoint 1).Valid := by
  change ¬ (1 : ℝ) = 0
  exact one_ne_zero

theorem endpoint_discrete_close (d : ℝ)
    (hn : 0 ≤ d) (hu : d < 1) (hz : ∃ z : ℤ, d = (z : ℝ)) :
    (zeroEndpoint d).Valid := by
  obtain ⟨z, rfl⟩ := hz
  have h0 : (0 : ℤ) ≤ z := by exact_mod_cast hn
  have h1 : z < (1 : ℤ) := by exact_mod_cast hu
  have he : z = 0 := by omega
  change (z : ℝ) = 0
  simp [he]

#print axioms endpoint_valid_iff
#print axioms endpoint_exists
#print axioms endpoint_not_automatically_valid
#print axioms endpoint_discrete_close

/-- Exact syntactic points; identity does not imply evaluation. -/
inductive IndeterminatePoint where
  | limitZero
  | finiteZero (n : ℕ)
  | zeroOverZero
  | zeroOverInfinity
  | infinityOverInfinity
  | millennium (i : Fin 8)
  deriving DecidableEq

inductive EpistemicValue where
  | negative
  | undetermined
  | positive
  deriving DecidableEq

/-- Positive and negative evaluations require evidence. -/
def EvaluationSound (p : Prop) : EpistemicValue → Prop
  | .positive => p
  | .negative => ¬ p
  | .undetermined => True

theorem positive_requires_proof (p : Prop)
    (h : EvaluationSound p .positive) : p := h

theorem negative_requires_refutation (p : Prop)
    (h : EvaluationSound p .negative) : ¬ p := h

theorem unknown_does_not_assert (p : Prop) :
    EvaluationSound p .undetermined := True.intro

theorem finite_limit_distinct (n : ℕ) :
    IndeterminatePoint.finiteZero n ≠ IndeterminatePoint.limitZero := by
  decide

theorem division_points_distinct :
    IndeterminatePoint.zeroOverZero ≠ IndeterminatePoint.infinityOverInfinity := by
  decide

/-- All eight obligations close exactly when all have positive evidence. -/
theorem all_points_close (P : Fin 8 → Prop) :
    (∀ i, EvaluationSound (P i) .positive) ↔ (∀ i, P i) := Iff.rfl

/-- Numeric sign is separate from epistemic truth. -/
noncomputable def NumericSign (x : ℝ) : EpistemicValue :=
  if x < 0 then .negative else if 0 < x then .positive else .undetermined

#print axioms positive_requires_proof
#print axioms negative_requires_refutation
#print axioms unknown_does_not_assert
#print axioms finite_limit_distinct
#print axioms division_points_distinct
#print axioms all_points_close

end MCore.RiemannIsolation
