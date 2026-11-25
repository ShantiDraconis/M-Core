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


/-- A normalized gain bounded below by a positive constant cannot persist
    indefinitely when the residual has a positive lower bound. -/
theorem uniform_gain_excludes_residual (D : ℕ → ℝ) (L c : ℝ)
    (hL : 0 < L) (hc : 0 < c)
    (lower : ∀ n, L ≤ D n)
    (gain : ∀ n, c ≤ 1 - D (n+1) / D n) : False := by
  have dec : ∀ n, D (n+1) ≤ D n := by
    intro n
    have hp : 0 < D n := lt_of_lt_of_le hL (lower n)
    have hratio : D (n+1) / D n ≤ 1 := by linarith [gain n]
    have hmul := (div_le_iff₀ hp).mp hratio
    simpa only [one_mul] using hmul
  have bound : ∀ N : ℕ, (N : ℝ) * c ≤
      ∑ n ∈ Finset.range N, (1 - D (n+1) / D n) := by
    intro N
    induction N with
    | zero => simp
    | succ N ih =>
      rw [Finset.sum_range_succ, Nat.cast_succ, add_mul, one_mul]
      exact add_le_add ih (gain N)
  obtain ⟨N, hN⟩ := exists_nat_gt (D 0 / (L*c))
  have hmul := (div_lt_iff₀ (mul_pos hL hc)).mp hN
  have h := accumulated_loss_bound D L hL lower dec N
  have hh := mul_le_mul_of_nonneg_left (bound N) hL.le
  have hlow := lower N
  nlinarith [show (N : ℝ) * (L*c) = L * ((N : ℝ)*c) by ring]

/-- Strict decrease alone is insufficient: a positive floor can persist. -/
theorem positive_floor_counterexample :
    ∃ D : ℕ → ℝ, (∀ n, D (n+1) < D n) ∧ (∀ n, 1 ≤ D n) := by
  refine ⟨fun n => 1 + 1 / ((n : ℝ)+1), ?_, ?_⟩
  · intro n
    push_cast
    have h : (0 : ℝ) < (n : ℝ)+1 := by positivity
    have h' : (n : ℝ)+1 < (n : ℝ)+1+1 := by linarith
    have hh := one_div_lt_one_div_of_lt h h'
    linarith
  · intro n
    have h : 0 ≤ 1 / ((n : ℝ)+1) := by positivity
    linarith

#print axioms uniform_gain_excludes_residual
#print axioms positive_floor_counterexample


/-- A correction at index j cancels the reciprocal-weighted coefficient sum.
    This is an algebraic identity, not an L² convergence claim. -/
theorem reciprocal_tail_cancel (S j : ℝ) (hj : j ≠ 0) :
    S + (-j * S) / j = 0 := by
  field_simp [hj] <;> ring

/-- Exact energy cost of a correction along a direction with squared norm G. -/
theorem correction_energy (S j G : ℝ) :
    (-j * S)^2 * G = j^2 * S^2 * G := by ring

#print axioms reciprocal_tail_cancel
#print axioms correction_energy


/-- The positive-floor obstruction survives every monotone block selection. -/
theorem block_relative_loss_bound (D : ℕ → ℝ) (K : ℕ → ℕ)
    (hK : Monotone K) (hD : Antitone D) (L : ℝ) (hL : 0 < L)
    (floor : ∀ n, L ≤ D n) (N : ℕ) :
    L * (∑ n ∈ Finset.range N, (1 - D (K (n+1)) / D (K n))) ≤
      D (K 0) - D (K N) := by
  exact accumulated_loss_bound (fun n => D (K n)) L hL
    (fun n => floor (K n)) (fun n => hD (hK (Nat.le_succ n))) N

#print axioms block_relative_loss_bound


/-- Exact finite product of relative rates, before the first zero. -/
theorem relative_rate_product (D : ℕ → ℝ) (N : ℕ)
    (hn : ∀ n < N, D n ≠ 0) :
    D 0 * (∏ n ∈ Finset.range N, (D (n+1) / D n)) = D N := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Finset.prod_range_succ, ← mul_assoc, ih (fun n h => hn n (Nat.lt.step h))]
    field_simp [hn N (Nat.lt_succ_self N)]

/-- Once a nonnegative antitone residual reaches zero, it stays zero. -/
theorem zero_residual_absorbing (D : ℕ → ℝ) (hD : Antitone D)
    (hn : ∀ n, 0 ≤ D n) (k : ℕ) (hk : D k = 0) :
    ∀ n, k ≤ n → D n = 0 := by
  intro n h
  exact le_antisymm (hk ▸ hD h) (hn n)

#print axioms relative_rate_product
#print axioms zero_residual_absorbing


/-- Exact cancellation criterion for a Schur residual step. -/
theorem schur_zero_iff (D u s : ℝ) (hs : 0 < s) :
    D - u^2 / s = 0 ↔ u^2 = s * D := by
  constructor
  · intro h
    have he : u^2 / s = D := by linarith
    have hm := (div_eq_iff (ne_of_gt hs)).mp he
    simpa [mul_comm] using hm
  · intro h
    have he : u^2 / s = D :=
      (div_eq_iff (ne_of_gt hs)).mpr (by simpa [mul_comm] using h)
    linarith

#print axioms schur_zero_iff


/-- A divergent lower rate certificate excludes every positive residual floor. -/
theorem rate_minorant_excludes_floor (D a : ℕ → ℝ)
    (dec : ∀ n, D (n+1) ≤ D n)
    (minorant : ∀ n, a n ≤ 1 - D (n+1) / D n)
    (diverges : ∀ B : ℝ, ∃ N : ℕ, B < ∑ n ∈ Finset.range N, a n) :
    ∀ L : ℝ, 0 < L → ¬ (∀ n, L ≤ D n) := by
  apply no_positive_residual_of_unbounded_loss D dec
  intro B
  obtain ⟨N, hN⟩ := diverges B
  refine ⟨N, lt_of_lt_of_le hN ?_⟩
  exact Finset.sum_le_sum (fun n _ => minorant n)

#print axioms rate_minorant_excludes_floor


/-- A positive floor bounds the accumulated loss even along arbitrary monotone blocks. -/
theorem block_minorant_excludes_floor (D a : ℕ → ℝ) (K : ℕ → ℕ)
    (hK : Monotone K) (hD : Antitone D)
    (minorant : ∀ n, a n ≤ 1 - D (K (n+1)) / D (K n))
    (diverges : ∀ B : ℝ, ∃ N : ℕ, B < ∑ n ∈ Finset.range N, a n) :
    ∀ L : ℝ, 0 < L → ¬ (∀ n, L ≤ D n) := by
  intro L hL floor
  exact rate_minorant_excludes_floor (fun n => D (K n)) a
    (fun n => hD (hK (Nat.le_succ n))) minorant diverges L hL
    (fun n => floor (K n))

#print axioms block_minorant_excludes_floor


/-- Triangular jump equations force every coefficient to vanish. -/
theorem triangular_jump_zero (c : ℕ → ℝ)
    (h : ∀ n, c n + ∑ k ∈ Finset.range n, (if (k+1) ∣ (n+1) then c k else 0) = 0) :
    ∀ n, c n = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    have hz : (∑ k ∈ Finset.range n, (if (k+1) ∣ (n+1) then c k else 0)) = 0 := by
      apply Finset.sum_eq_zero
      intro k hk
      rw [ih k (Finset.mem_range.mp hk)]
      split <;> rfl
    simpa [hz] using h n

#print axioms triangular_jump_zero


/-- Finite triangular jump equations suffice for finite coefficient elimination. -/
theorem finite_triangular_jump_zero (c : ℕ → ℝ) (N : ℕ)
    (h : ∀ n < N, c n + ∑ k ∈ Finset.range n,
      (if (k+1) ∣ (n+1) then c k else 0) = 0) :
    ∀ n < N, c n = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    have hz : (∑ k ∈ Finset.range n,
        (if (k+1) ∣ (n+1) then c k else 0)) = 0 := by
      apply Finset.sum_eq_zero
      intro k hk
      have hkn := Finset.mem_range.mp hk
      rw [ih k hkn (lt_trans hkn hn)]
      split <;> rfl
    simpa [hz] using h n hn

#print axioms finite_triangular_jump_zero


open scoped RealInnerProductSpace in
theorem geometric_schur {H : Type*} [NormedAddCommGroup H]
    [InnerProductSpace ℝ H] (R v : H) (hv : v ≠ 0) :
    ‖R - (@inner ℝ H _ R v / ‖v‖^2) • v‖^2 =
      ‖R‖^2 - (@inner ℝ H _ R v)^2 / ‖v‖^2 := by
  have hs : 0 < ‖v‖^2 := sq_pos_of_pos (norm_pos_iff.mpr hv)
  rw [norm_sub_sq_real, norm_smul, Real.norm_eq_abs, mul_pow, sq_abs,
    real_inner_smul_right]
  convert quadratic_rate_gain (‖R‖^2) (@inner ℝ H _ R v) (‖v‖^2) hs using 1 <;> ring

#print axioms geometric_schur


/-- Distinguish exact zero, asymptotic zero and admissible rate division. -/
structure AdmissibleRate where
  numerator : ℝ → ℝ
  denominator : ℝ → ℝ
  approach : Filter ℝ
  nontrivial : approach.NeBot
  denominator_ne : ∀ᶠ t in approach, denominator t ≠ 0

def AdmissibleRate.realizes (p : AdmissibleRate) (a : ℝ) : Prop :=
  Filter.Tendsto (fun t => p.numerator t / p.denominator t) p.approach (nhds a)

theorem admissible_rate_unique (p : AdmissibleRate) {a b : ℝ}
    (ha : p.realizes a) (hb : p.realizes b) : a = b := by
  letI : p.approach.NeBot := p.nontrivial
  exact tendsto_nhds_unique ha hb

#print axioms admissible_rate_unique


/-- A positive triple with gcd one cannot admit a common prime divisor. -/
theorem common_prime_excluded_of_gcd_one (a b c p : ℕ)
    (hg : Nat.gcd a (Nat.gcd b c) = 1)
    (hp : Nat.Prime p) (ha : p ∣ a) (hb : p ∣ b) (hc : p ∣ c) : False := by
  have hd : p ∣ Nat.gcd a (Nat.gcd b c) :=
    Nat.dvd_gcd ha (Nat.dvd_gcd hb hc)
  rw [hg] at hd
  exact hp.not_dvd_one hd

/-- Extract a material prime witness from a strict gcd lower bound. -/
theorem common_prime_of_gcd_lower (a b c : ℕ)
    (h : 1 < Nat.gcd a (Nat.gcd b c)) :
    ∃ p : ℕ, Nat.Prime p ∧ p ∣ a ∧ p ∣ b ∧ p ∣ c := by
  obtain ⟨p, hp, hd⟩ := Nat.ne_one_iff_exists_prime_dvd.mp (ne_of_gt h)
  have hbc := dvd_trans hd (Nat.gcd_dvd_right a (Nat.gcd b c))
  exact ⟨p, hp, dvd_trans hd (Nat.gcd_dvd_left a (Nat.gcd b c)),
    dvd_trans hbc (Nat.gcd_dvd_left b c), dvd_trans hbc (Nat.gcd_dvd_right b c)⟩

#print axioms common_prime_excluded_of_gcd_one
#print axioms common_prime_of_gcd_lower


/-- Structural identity is independent of the numerical realization. -/
inductive RateExpression where
  | atom : Nat → RateExpression
  | zero : RateExpression
  | quotient : RateExpression → RateExpression → RateExpression
  | product : RateExpression → RateExpression → RateExpression
  | difference : RateExpression → RateExpression → RateExpression
  deriving DecidableEq, Repr

/-- A family of admissible paths retains all realizable finite limits. -/
def familyRateLimits (paths : Set AdmissibleRate) : Set ℝ :=
  {a | ∃ p ∈ paths, p.realizes a}

theorem familyRateLimits_mono {P Q : Set AdmissibleRate} (h : P ⊆ Q) :
    familyRateLimits P ⊆ familyRateLimits Q := by
  rintro a ⟨p, hp, ha⟩
  exact ⟨p, h hp, ha⟩

theorem structural_zero_distinct :
    RateExpression.quotient .zero (.atom 2) ≠
      RateExpression.quotient .zero (.atom 3) := by decide

#print axioms familyRateLimits_mono
#print axioms structural_zero_distinct


/-- Every finite real limit is realized by an admissible zero-over-zero path. -/
theorem zero_over_zero_realizes_all (a : ℝ) :
    ∃ p : AdmissibleRate, p.realizes a ∧
      Filter.Tendsto p.numerator p.approach (nhds 0) ∧
      Filter.Tendsto p.denominator p.approach (nhds 0) := by
  let F := nhdsWithin (0 : ℝ) {t : ℝ | t ≠ 0}
  have hF : F.NeBot := by
    dsimp [F]
    infer_instance
  have hd : ∀ᶠ t in F, t ≠ 0 := self_mem_nhdsWithin
  let p : AdmissibleRate := ⟨fun t => a * t, id, F, hF, hd⟩
  have ht : Filter.Tendsto (fun t : ℝ => t) F (nhds 0) :=
    nhdsWithin_le_nhds
  refine ⟨p, ?_, ?_, ht⟩
  · exact rate_division_constant_path a
  · simpa [p] using tendsto_const_nhds.mul ht

#print axioms zero_over_zero_realizes_all


/-- Exact relative loss of the reciprocal model. -/
theorem reciprocal_model_loss (n : ℕ) :
    1 - (1 / ((n : ℝ) + 2)) / (1 / ((n : ℝ) + 1)) =
      1 / ((n : ℝ) + 2) := by
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  have h1 : (n : ℝ) + 1 ≠ 0 := by linarith
  have h2 : (n : ℝ) + 2 ≠ 0 := by linarith
  field_simp [h1, h2] <;> ring

#print axioms reciprocal_model_loss


/-- A zero squared residual is equivalent to exact equality in any normed group. -/
theorem exact_residual_zero {H : Type*} [NormedAddCommGroup H] (x y : H) :
    ‖x - y‖^2 = 0 ↔ x = y := by
  constructor
  · intro h
    have hn : ‖x - y‖ = 0 := by nlinarith [norm_nonneg (x-y)]
    exact sub_eq_zero.mp (norm_eq_zero.mp hn)
  · rintro rfl
    simp

/-- Nonnegative residuals with arbitrarily small values have no positive floor. -/
theorem arbitrary_small_excludes_floor (D : ℕ → ℝ)
    (small : ∀ ε : ℝ, 0 < ε → ∃ n, D n < ε) :
    ∀ L : ℝ, 0 < L → ¬ (∀ n, L ≤ D n) := by
  intro L hL floor
  obtain ⟨n, hn⟩ := small L hL
  exact (not_lt_of_ge (floor n)) hn

#print axioms exact_residual_zero
#print axioms arbitrary_small_excludes_floor


/-- Exact semantic points include unresolved expressions without assigning fake values. -/
inductive SemanticPoint where
  | determined : ℝ → SemanticPoint
  | structural : RateExpression → SemanticPoint

def semanticRepresentation (valuation : RateExpression → Option ℝ)
    (e : RateExpression) : SemanticPoint :=
  match valuation e with
  | some v => .determined v
  | none => .structural e

theorem semantic_representation_total
    (valuation : RateExpression → Option ℝ) (e : RateExpression) :
    ∃! p, semanticRepresentation valuation e = p := by
  exact ⟨semanticRepresentation valuation e, rfl, fun _ h => h.symm⟩

theorem canonical_numeric_identity
    (valuation : RateExpression → Option ℝ) (e f : RateExpression)
    (v : ℝ) (he : valuation e = some v) (hf : valuation f = some v) :
    semanticRepresentation valuation e = semanticRepresentation valuation f := by
  simp [semanticRepresentation, he, hf]

theorem unresolved_structural_identity
    (valuation : RateExpression → Option ℝ) (e : RateExpression)
    (h : valuation e = none) :
    semanticRepresentation valuation e = .structural e := by
  simp [semanticRepresentation, h]

#print axioms semantic_representation_total
#print axioms canonical_numeric_identity
#print axioms unresolved_structural_identity

end MCore.ClosureCalculus
