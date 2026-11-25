import Mathlib

namespace MCore.ClosureCalculus

theorem transport {P Q : Prop} (h : P ↔ Q) (p : P) : Q := h.mp p
theorem discharge {H P Q : Prop} (f : H → P) (g : P → Q) : H → Q :=
  fun h => g (f h)
theorem witness {α : Type*} {P : α → Prop} (x : α) (h : P x) : ∃ y, P y :=
  ⟨x, h⟩
theorem refute {α : Type*} {P Q : α → Prop} (x : α)
    (hp : P x) (hq : ¬ Q x) : ¬ (∀ y, P y → Q y) :=
  fun h => hq (h x hp)

def Fails {α : Type*} (A S : α → Bool) (y : α) : Prop := A y ≠ S y
def Aligns {α : Type*} (A : α → Bool) (r : α → α) (x : α) : Prop :=
  A (r x) = A x
def Cover {α : Type*} (A S : α → Bool) (r : α → α) : Prop :=
  (∃ y, Fails A S y) → ∃ x, Fails A S (r x)

theorem align_iff_fail_image {α : Type*} (A S : α → Bool) (r : α → α)
    (h : ∀ x, S (r x) = !A x) (x : α) :
    Aligns A r x ↔ Fails A S (r x) := by
  unfold Aligns Fails
  rw [h x]
  cases A x <;> cases A (r x) <;> decide

theorem cover_iff_failure_to_alignment {α : Type*}
    (A S : α → Bool) (r : α → α) (h : ∀ x, S (r x) = !A x) :
    Cover A S r ↔ ((∃ y, Fails A S y) → ∃ x, Aligns A r x) := by
  constructor
  · intro hc hf
    obtain ⟨x, hx⟩ := hc hf
    exact ⟨x, (align_iff_fail_image A S r h x).mpr hx⟩
  · intro hc hf
    obtain ⟨x, hx⟩ := hc hf
    exact ⟨x, (align_iff_fail_image A S r h x).mp hx⟩

theorem empty_input_fuel (clock : Nat → Nat) (n : Nat)
    (h : Monotone clock) : clock 0 ≤ clock n := h (Nat.zero_le n)

-- Infinite domain: reduction flips parity and avoids zero.
def counterA (n : Nat) : Bool := n % 2 == 1
def counterS (n : Nat) : Bool := if n = 0 then true else counterA n
def counterR (n : Nat) : Nat := if n % 2 = 0 then 1 else 2

theorem counter_semantics (n : Nat) :
    counterS (counterR n) = !counterA n := by
  have h : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases h with h | h <;> simp [counterS, counterR, counterA, h]

theorem counter_failure : ∃ y, Fails counterA counterS y := ⟨0, by simp [Fails, counterA, counterS]⟩

theorem counter_no_alignment (n : Nat) : ¬ Aligns counterA counterR n := by
  have h : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases h with h | h <;> simp [Aligns, counterA, counterR, h]

theorem counter_no_cover : ¬ Cover counterA counterS counterR := by
  intro hc
  obtain ⟨x, hx⟩ := hc counter_failure
  exact counter_no_alignment x
    ((align_iff_fail_image counterA counterS counterR counter_semantics x).mpr hx)

#print axioms align_iff_fail_image
#print axioms cover_iff_failure_to_alignment
#print axioms empty_input_fuel
#print axioms counter_semantics
#print axioms counter_no_cover


/-! Rate-sensitive division: retain paths and their filter, not only a scalar. -/
structure RateDivision where
  numerator : ℝ → ℝ
  denominator : ℝ → ℝ
  approach : Filter ℝ

def RateDivision.realizes (d : RateDivision) (a : ℝ) : Prop :=
  Filter.Tendsto (fun t => d.numerator t / d.denominator t)
    d.approach (nhds a)

def RateDivision.admissible (d : RateDivision) : Prop :=
  ∀ᶠ t in d.approach, d.denominator t ≠ 0

def RateDivision.limits (d : RateDivision) : Set ℝ :=
  {a | d.realizes a}

theorem rate_division_constant_path (a : ℝ) :
    (⟨fun t => a * t, id, nhdsWithin 0 {t : ℝ | t ≠ 0}⟩ :
      RateDivision).realizes a := by
  change Filter.Tendsto (fun t : ℝ => (a * t) / t)
    (nhdsWithin 0 {t : ℝ | t ≠ 0}) (nhds a)
  apply tendsto_const_nhds.congr'
  filter_upwards [self_mem_nhdsWithin] with t ht
  exact (mul_div_cancel_right₀ a ht).symm

theorem universal_producer_bridge {α : Type*}
    (F : α → Prop) (r : α → α)
    (coverage : (∃ y, F y) → ∃ x, F (r x))
    (exclusion : ∀ x, ¬ F (r x)) : ∀ y, ¬ F y := by
  intro y hy
  obtain ⟨x, hx⟩ := coverage ⟨y, hy⟩
  exact exclusion x hx

#print axioms rate_division_constant_path
#print axioms universal_producer_bridge


/-- A positive residual converts relative losses into absolute losses. -/
theorem relative_loss_bound (a b L : ℝ)
    (hL : 0 < L) (hla : L ≤ a) (hab : b ≤ a) :
    L * (1 - b / a) ≤ a - b := by
  have ha : 0 < a := lt_of_lt_of_le hL hla
  have he : a * (1 - b / a) = a - b := by
    field_simp
    <;> ring
  have hn : 0 ≤ 1 - b / a := by
    have h := (div_le_iff₀ ha).2 (show b ≤ 1 * a by simpa using hab)
    linarith
  calc
    L * (1 - b / a) ≤ a * (1 - b / a) :=
      mul_le_mul_of_nonneg_right hla hn
    _ = a - b := he

/-- Finite accumulated losses cannot exceed the initial residual. -/
theorem accumulated_loss_bound (D : ℕ → ℝ) (L : ℝ)
    (hL : 0 < L) (lower : ∀ n, L ≤ D n)
    (decrease : ∀ n, D (n+1) ≤ D n) (N : ℕ) :
    L * (∑ n ∈ Finset.range N, (1 - D (n+1) / D n)) ≤ D 0 - D N := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Finset.sum_range_succ, mul_add]
    have h := relative_loss_bound (D N) (D (N+1)) L hL (lower N) (decrease N)
    linarith

#print axioms relative_loss_bound
#print axioms accumulated_loss_bound


/-- Unbounded finite relative losses exclude every positive uniform residual. -/
theorem no_positive_residual_of_unbounded_loss
    (D : ℕ → ℝ) (decrease : ∀ n, D (n+1) ≤ D n)
    (unbounded : ∀ B : ℝ, ∃ N : ℕ,
      B < ∑ n ∈ Finset.range N, (1 - D (n+1) / D n)) :
    ∀ L : ℝ, 0 < L → ¬ (∀ n, L ≤ D n) := by
  intro L hL lower
  obtain ⟨N, hN⟩ := unbounded (D 0 / L)
  have h := accumulated_loss_bound D L hL lower decrease N
  have hm := (div_lt_iff₀ hL).mp hN
  have hp := lower N
  rw [mul_comm L] at h
  linarith

#print axioms no_positive_residual_of_unbounded_loss


/-- Exact scalar optimization of the quadratic residual along a new direction.
    E is the old squared residual, C its correlation, and G the squared norm
    of the new direction. -/
theorem quadratic_rate_gain (E C G : ℝ) (hG : 0 < G) :
    E - 2 * (C / G) * C + (C / G)^2 * G = E - C^2 / G := by
  field_simp [ne_of_gt hG] <;> ring

theorem quadratic_rate_gain_nonneg (C G : ℝ) (hG : 0 < G) :
    0 ≤ C^2 / G := div_nonneg (sq_nonneg C) hG.le

theorem quadratic_rate_gain_strict (C G : ℝ) (hG : 0 < G)
    (hC : C ≠ 0) : 0 < C^2 / G :=
  div_pos (sq_pos_of_ne_zero hC) hG

#print axioms quadratic_rate_gain
#print axioms quadratic_rate_gain_nonneg
#print axioms quadratic_rate_gain_strict

end MCore.ClosureCalculus
