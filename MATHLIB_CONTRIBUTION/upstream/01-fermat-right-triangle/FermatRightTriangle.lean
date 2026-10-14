/-
Copyright (c) 2026 Tiago Paschoalatto Fagliari. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Tiago Paschoalatto Fagliari
-/
module

public import Mathlib.NumberTheory.PythagoreanTriples
public import Mathlib.RingTheory.Int.Basic
import Mathlib.Data.Int.Lemmas
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Fermat's right triangle theorem

There are no integers `a`, `b`, `c` with `b ≠ 0`, `c ≠ 0` and `a ^ 4 - b ^ 4 = c ^ 2`.
Equivalently, the area of a right triangle with integer (or rational) sides is never a square;
in particular `1` is not a congruent number.

The proof is Fermat's infinite descent on `|a|`. Take a solution with `|a|` minimal. Then `a` and
`b` are coprime and `(b ^ 2, c, a ^ 2)` is a primitive Pythagorean triple.
* If `b` is odd, then `b ^ 2 = m ^ 2 - n ^ 2`, `c = 2 * m * n`, `a ^ 2 = m ^ 2 + n ^ 2`, and
  `(m, n, a * b)` is a smaller solution.
* If `b` is even, then `c = m ^ 2 - n ^ 2`, `b ^ 2 = 2 * m * n`, `a ^ 2 = m ^ 2 + n ^ 2`. A second
  Pythagorean triple gives coprime `r`, `s` with `(b / 2) ^ 2 = r * s * (r ^ 2 - s ^ 2)`, so
  `r = j ^ 2`, `s = k ^ 2`, `r ^ 2 - s ^ 2 = d ^ 2`, and `(j, k, d)` is a smaller solution.

## Main results

* `Int.fourth_pow_sub_fourth_pow_ne_sq`: `a ^ 4 - b ^ 4 ≠ c ^ 2` when `b ≠ 0` and `c ≠ 0`.
* `Int.fourth_pow_add_sq_ne_fourth_pow`: `a ^ 4 + b ^ 2 ≠ c ^ 4` when `a ≠ 0` and `b ≠ 0`.
* `Int.not_isSquare_sq_add_sq_and_sq_sub_sq`: `a ^ 2 + b ^ 2` and `a ^ 2 - b ^ 2` are not both
  squares when `b ≠ 0`.
* `PythagoreanTriple.mul_ne_two_mul_sq`: the area of a nondegenerate Pythagorean triangle is not a
  square.
* `Rat.mul_ne_two_of_sq_add_sq_eq_sq`: no right triangle with rational sides has area `1`.

## References

* <https://en.wikipedia.org/wiki/Fermat%27s_right_triangle_theorem>
-/

@[expose] public section

/-- Shorthand for integers `a`, `b`, `c` with `b ≠ 0`, `c ≠ 0` and `a ^ 4 - b ^ 4 = c ^ 2`.
We show that no such integers exist. -/
def FermatRightTriangle (a b c : ℤ) : Prop :=
  b ≠ 0 ∧ c ≠ 0 ∧ a ^ 4 - b ^ 4 = c ^ 2

namespace FermatRightTriangle

theorem ne_zero {a b c : ℤ} (h : FermatRightTriangle a b c) : a ≠ 0 := by
  rintro rfl
  obtain ⟨hb, -, heq⟩ := h
  have hb4 : 0 < b ^ 4 := by positivity
  nlinarith [sq_nonneg c]

theorem neg {a b c : ℤ} (h : FermatRightTriangle a b c) : FermatRightTriangle (-a) b c := by
  obtain ⟨hb, hc, heq⟩ := h
  exact ⟨hb, hc, by rw [← heq]; ring⟩

theorem of_mul {a b c k : ℤ} (hk : k ≠ 0)
    (h : FermatRightTriangle (k * a) (k * b) (k ^ 2 * c)) : FermatRightTriangle a b c := by
  obtain ⟨hb, hc, heq⟩ := h
  refine ⟨right_ne_zero_of_mul hb, right_ne_zero_of_mul hc, ?_⟩
  apply (mul_right_inj' (pow_ne_zero 4 hk)).mp
  linear_combination heq

/-- A solution of `a ^ 4 - b ^ 4 = c ^ 2` is minimal if no other solution has a smaller `|a|`. -/
def Minimal (a b c : ℤ) : Prop :=
  FermatRightTriangle a b c ∧
    ∀ a₁ b₁ c₁ : ℤ, FermatRightTriangle a₁ b₁ c₁ → Int.natAbs a ≤ Int.natAbs a₁

theorem exists_minimal {a b c : ℤ} (h : FermatRightTriangle a b c) :
    ∃ a₀ b₀ c₀, Minimal a₀ b₀ c₀ := by
  classical
  have hex : ∃ n : ℕ, ∃ s : ℤ × ℤ × ℤ, FermatRightTriangle s.1 s.2.1 s.2.2 ∧ n = s.1.natAbs :=
    ⟨a.natAbs, (a, b, c), h, rfl⟩
  obtain ⟨s₀, hs₀, hs₁⟩ := Nat.find_spec hex
  refine ⟨s₀.1, s₀.2.1, s₀.2.2, hs₀, fun a₁ b₁ c₁ h₁ => ?_⟩
  rw [← hs₁]
  exact Nat.find_min' hex ⟨(a₁, b₁, c₁), h₁, rfl⟩

/-- In a minimal solution, `a` and `b` are coprime. -/
theorem coprime_of_minimal {a b c : ℤ} (h : Minimal a b c) : IsCoprime a b := by
  apply Int.isCoprime_iff_gcd_eq_one.mpr
  by_contra hab
  obtain ⟨p, hp, hpa, hpb⟩ := Nat.Prime.not_coprime_iff_dvd.mp hab
  obtain ⟨a₁, rfl⟩ := Int.natCast_dvd.mpr hpa
  obtain ⟨b₁, rfl⟩ := Int.natCast_dvd.mpr hpb
  have hpc : (p : ℤ) ^ 2 ∣ c := by
    rw [← Int.pow_dvd_pow_iff two_ne_zero, ← h.1.2.2]
    exact Dvd.intro (a₁ ^ 4 - b₁ ^ 4) (by ring)
  obtain ⟨c₁, rfl⟩ := hpc
  have hf : FermatRightTriangle a₁ b₁ c₁ := of_mul (Int.natCast_ne_zero.mpr hp.ne_zero) h.1
  apply Nat.le_lt_asymm (h.2 _ _ _ hf)
  rw [Int.natAbs_mul, Int.natAbs_natCast, lt_mul_iff_one_lt_left]
  · exact hp.one_lt
  · exact Nat.pos_of_ne_zero (Int.natAbs_ne_zero.2 hf.ne_zero)

/-- There is a minimal solution with `0 < a`. -/
theorem exists_pos_minimal {a b c : ℤ} (h : FermatRightTriangle a b c) :
    ∃ a₀ b₀ c₀, Minimal a₀ b₀ c₀ ∧ 0 < a₀ := by
  obtain ⟨a₀, b₀, c₀, hf⟩ := exists_minimal h
  rcases lt_trichotomy 0 a₀ with h₁ | h₁ | h₁
  · exact ⟨a₀, b₀, c₀, hf, h₁⟩
  · exact absurd h₁.symm hf.1.ne_zero
  · refine ⟨-a₀, b₀, c₀, ⟨hf.1.neg, fun a₁ b₁ c₁ h₂ => ?_⟩, neg_pos.mpr h₁⟩
    rw [Int.natAbs_neg]
    exact hf.2 a₁ b₁ c₁ h₂

theorem isCoprime_sq_sub_sq_mul {r s : ℤ} (h : IsCoprime r s) :
    IsCoprime (r ^ 2 - s ^ 2) (r * s) := by
  have h₁ : IsCoprime (r ^ 2 - s ^ 2) r := by
    have h' := ((IsCoprime.mul_left h.symm h.symm).neg_left).add_mul_left_left r
    rwa [show -(s * s) + r * r = r ^ 2 - s ^ 2 by ring] at h'
  have h₂ : IsCoprime (r ^ 2 - s ^ 2) s := by
    have h' := (IsCoprime.mul_left h h).add_mul_left_left (-s)
    rwa [show r * r + s * -s = r ^ 2 - s ^ 2 by ring] at h'
  exact h₁.mul_right h₂

/-- The descent step when `b` is odd. -/
theorem exists_smaller_of_odd {a b c : ℤ} (ha : 0 < a) (hb : b ≠ 0) (hc : c ≠ 0)
    (heq : a ^ 4 - b ^ 4 = c ^ 2) (hcop : IsCoprime (b ^ 2) c) (hbodd : b % 2 = 1) :
    ∃ a₁ b₁ c₁, FermatRightTriangle a₁ b₁ c₁ ∧ a₁.natAbs < a.natAbs := by
  have ht : PythagoreanTriple (b ^ 2) c (a ^ 2) := by
    delta PythagoreanTriple
    linear_combination (-1 : ℤ) * heq
  have hb2 : b ^ 2 % 2 = 1 := by
    rw [sq, Int.mul_emod, hbodd]
    decide
  obtain ⟨m, n, h₁, h₂, h₃, -, -, -⟩ :=
    ht.coprime_classification' (Int.isCoprime_iff_gcd_eq_one.mp hcop) hb2 (by positivity)
  have hn : n ≠ 0 := by
    rintro rfl
    apply hc
    rw [h₂]
    ring
  refine ⟨m, n, a * b, ⟨hn, mul_ne_zero ha.ne' hb, ?_⟩, ?_⟩
  · rw [mul_pow, h₃, h₁]
    ring
  · rw [Int.natAbs_lt_iff_sq_lt, h₃]
    have : 0 < n ^ 2 := by positivity
    linarith

/-- The last step of the descent when `b` is even: `b' ^ 2 = r * s * (r ^ 2 - s ^ 2)` with
coprime positive `r`, `s` gives a smaller solution. -/
theorem exists_smaller_of_mul_eq_sq {a b' r s : ℤ} (hr : 0 < r) (hs : 0 < s)
    (hd : 0 < r ^ 2 - s ^ 2) (hrs : Int.gcd r s = 1) (ha : a = r ^ 2 + s ^ 2)
    (hb' : r * s * (r ^ 2 - s ^ 2) = b' ^ 2) :
    ∃ a₁ b₁ c₁, FermatRightTriangle a₁ b₁ c₁ ∧ a₁.natAbs < a.natAbs := by
  have hcop₁ : Int.gcd (r * s) (r ^ 2 - s ^ 2) = 1 :=
    Int.isCoprime_iff_gcd_eq_one.mp
      (isCoprime_sq_sub_sq_mul (Int.isCoprime_iff_gcd_eq_one.mpr hrs)).symm
  have hcop₂ : Int.gcd (r ^ 2 - s ^ 2) (r * s) = 1 := by
    rw [Int.gcd_comm]
    exact hcop₁
  have hrs_pos : 0 < r * s := mul_pos hr hs
  obtain ⟨e, he⟩ := Int.sq_of_gcd_eq_one hcop₁ hb'
  have hrse : r * s = e ^ 2 := by
    rcases he with h | h
    · exact h
    · exfalso
      nlinarith [sq_nonneg e]
  obtain ⟨d, hd'⟩ := Int.sq_of_gcd_eq_one hcop₂ ((mul_comm _ _).trans hb')
  have hdeq : r ^ 2 - s ^ 2 = d ^ 2 := by
    rcases hd' with h | h
    · exact h
    · exfalso
      nlinarith [sq_nonneg d]
  obtain ⟨j, hj⟩ := Int.sq_of_gcd_eq_one hrs hrse
  have hrj : r = j ^ 2 := by
    rcases hj with h | h
    · exact h
    · exfalso
      nlinarith [sq_nonneg j]
  have hsr : Int.gcd s r = 1 := by
    rw [Int.gcd_comm]
    exact hrs
  obtain ⟨k, hk⟩ := Int.sq_of_gcd_eq_one hsr ((mul_comm s r).trans hrse)
  have hsk : s = k ^ 2 := by
    rcases hk with h | h
    · exact h
    · exfalso
      nlinarith [sq_nonneg k]
  refine ⟨j, k, d, ⟨?_, ?_, ?_⟩, ?_⟩
  · rintro rfl
    rw [hsk] at hs
    simp at hs
  · rintro rfl
    rw [hdeq] at hd
    simp at hd
  · rw [← hdeq, hrj, hsk]
    ring
  · rw [Int.natAbs_lt_iff_sq_lt, ← hrj]
    have hr2 : r ≤ r ^ 2 := by nlinarith [sq_nonneg (r - 1)]
    have hs2 : 0 < s ^ 2 := by positivity
    have ha2 : a ≤ a ^ 2 := by nlinarith [sq_nonneg (a - 1)]
    linarith

/-- The parametrization used in the even case: from a primitive triple `(n, m, a)` with `n` odd,
`m * n = 2 * (r * s) * (r ^ 2 - s ^ 2)` with coprime positive `r > s`. -/
theorem exists_param_of_odd {a m n : ℤ} (ha : 0 < a) (hmn : 0 < m * n) (hcop : Int.gcd n m = 1)
    (hn2 : n % 2 = 1) (h₃ : a ^ 2 = n ^ 2 + m ^ 2) (hn : 0 < n) :
    ∃ r s : ℤ, 0 < r ∧ 0 < s ∧ 0 < r ^ 2 - s ^ 2 ∧ Int.gcd r s = 1 ∧
      a = r ^ 2 + s ^ 2 ∧ m * n = 2 * (r * s) * (r ^ 2 - s ^ 2) := by
  have ht : PythagoreanTriple n m a := by
    delta PythagoreanTriple
    linear_combination (-1 : ℤ) * h₃
  obtain ⟨r, s, e₁, e₂, e₃, hrs, -, hr₀⟩ := ht.coprime_classification' hcop hn2 ha
  have hrs_pos : 0 < r * s := by nlinarith
  have hr : 0 < r := by
    rcases hr₀.lt_or_eq with h | h
    · exact h
    · rw [← h] at hrs_pos
      simp at hrs_pos
  have hs : 0 < s := by
    by_contra hs
    have hs' := not_lt.mp hs
    nlinarith
  exact ⟨r, s, hr, hs, by rw [← e₁]; exact hn, hrs, e₃, by rw [e₁, e₂]; ring⟩

/-- The descent step when `b` is even. -/
theorem exists_smaller_of_even {a b c : ℤ} (ha : 0 < a) (hb : b ≠ 0)
    (heq : a ^ 4 - b ^ 4 = c ^ 2) (hcop : IsCoprime (b ^ 2) c) (hbeven : b % 2 = 0) :
    ∃ a₁ b₁ c₁, FermatRightTriangle a₁ b₁ c₁ ∧ a₁.natAbs < a.natAbs := by
  have hcodd : c % 2 = 1 := by
    rcases Int.emod_two_eq_zero_or_one c with h | h
    · exfalso
      have h2b : (2 : ℤ) ∣ b ^ 2 :=
        (Int.dvd_of_emod_eq_zero hbeven).trans (dvd_pow_self b two_ne_zero)
      have hu := hcop.isUnit_of_dvd' h2b (Int.dvd_of_emod_eq_zero h)
      rw [Int.isUnit_iff] at hu
      omega
    · exact h
  have ht : PythagoreanTriple c (b ^ 2) (a ^ 2) := by
    delta PythagoreanTriple
    linear_combination (-1 : ℤ) * heq
  obtain ⟨m, n, -, h₂, h₃, hmn, hpar, hm₀⟩ :=
    ht.coprime_classification' (Int.isCoprime_iff_gcd_eq_one.mp hcop.symm) hcodd (by positivity)
  obtain ⟨b', rfl⟩ := Int.dvd_of_emod_eq_zero hbeven
  have hb' : b' ≠ 0 := right_ne_zero_of_mul hb
  have hmn_pos : 0 < m * n := by
    have : 0 < (2 * b') ^ 2 := by positivity
    nlinarith
  have hm : 0 < m := by
    rcases hm₀.lt_or_eq with h | h
    · exact h
    · rw [← h] at hmn_pos
      simp at hmn_pos
  have hn : 0 < n := by
    by_contra hn
    have hn' := not_lt.mp hn
    nlinarith
  have key : ∃ r s : ℤ, 0 < r ∧ 0 < s ∧ 0 < r ^ 2 - s ^ 2 ∧ Int.gcd r s = 1 ∧
      a = r ^ 2 + s ^ 2 ∧ m * n = 2 * (r * s) * (r ^ 2 - s ^ 2) := by
    rcases hpar with ⟨-, hn2⟩ | ⟨hm2, -⟩
    · rw [Int.gcd_comm] at hmn
      exact exists_param_of_odd ha hmn_pos hmn hn2 (by linear_combination h₃) hn
    · obtain ⟨r, s, hr, hs, hd, hrs, ha', h⟩ :=
        exists_param_of_odd ha (by rwa [mul_comm]) hmn hm2 (by linear_combination h₃) hm
      exact ⟨r, s, hr, hs, hd, hrs, ha', by rw [mul_comm]; exact h⟩
  obtain ⟨r, s, hr, hs, hd, hrs, ha', hmn'⟩ := key
  have h₄ : (4 : ℤ) * (r * s * (r ^ 2 - s ^ 2)) = 4 * b' ^ 2 := by
    linear_combination (-1 : ℤ) * h₂ - 2 * hmn'
  exact exists_smaller_of_mul_eq_sq hr hs hd hrs ha' (mul_left_cancel₀ (by norm_num) h₄)

/-- There is no minimal solution with `0 < a`. -/
theorem not_minimal {a b c : ℤ} (h : Minimal a b c) (ha : 0 < a) : False := by
  have hab : IsCoprime a b := coprime_of_minimal h
  obtain ⟨⟨hb, hc, heq⟩, hmin⟩ := h
  have hcop : IsCoprime (b ^ 2) c := by
    have h₁ : IsCoprime (b ^ 4) (a ^ 4 + b ^ 4 * (-1)) := hab.symm.pow.add_mul_left_right (-1)
    rw [show a ^ 4 + b ^ 4 * (-1) = c ^ 2 by linear_combination heq] at h₁
    exact ((IsCoprime.pow_iff (by norm_num) (by norm_num)).mp h₁).pow_left
  obtain ⟨a₁, b₁, c₁, hf, hlt⟩ : ∃ a₁ b₁ c₁, FermatRightTriangle a₁ b₁ c₁ ∧
      a₁.natAbs < a.natAbs := by
    rcases Int.emod_two_eq_zero_or_one b with hb2 | hb2
    · exact exists_smaller_of_even ha hb heq hcop hb2
    · exact exists_smaller_of_odd ha hb hc heq hcop hb2
  exact absurd (hmin a₁ b₁ c₁ hf) (not_le.mpr hlt)

end FermatRightTriangle

namespace Int

/-- **Fermat's right triangle theorem**: `a ^ 4 - b ^ 4 ≠ c ^ 2` for `b ≠ 0` and `c ≠ 0`. -/
theorem fourth_pow_sub_fourth_pow_ne_sq {a b c : ℤ} (hb : b ≠ 0) (hc : c ≠ 0) :
    a ^ 4 - b ^ 4 ≠ c ^ 2 := by
  intro heq
  obtain ⟨a₀, b₀, c₀, hmin, hpos⟩ := FermatRightTriangle.exists_pos_minimal (a := a) ⟨hb, hc, heq⟩
  exact FermatRightTriangle.not_minimal hmin hpos

/-- `a ^ 4 + b ^ 2 ≠ c ^ 4` for `a ≠ 0` and `b ≠ 0`. -/
theorem fourth_pow_add_sq_ne_fourth_pow {a b c : ℤ} (ha : a ≠ 0) (hb : b ≠ 0) :
    a ^ 4 + b ^ 2 ≠ c ^ 4 := by
  intro h
  exact fourth_pow_sub_fourth_pow_ne_sq (a := c) ha hb (by linear_combination (-1 : ℤ) * h)

/-- `a ^ 2 ≠ 2 * d ^ 2` for `a ≠ 0`. -/
theorem sq_ne_two_mul_sq {a : ℤ} (d : ℤ) (ha : a ≠ 0) : a ^ 2 ≠ 2 * d ^ 2 := by
  suffices h : ∀ n : ℕ, ∀ a d : ℤ, a.natAbs = n → a ≠ 0 → a ^ 2 ≠ 2 * d ^ 2 from
    h _ a d rfl ha
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro a d hn ha heq
    obtain ⟨a', rfl⟩ : (2 : ℤ) ∣ a := Int.prime_two.dvd_of_dvd_pow (n := 2) ⟨d ^ 2, heq⟩
    have ha' : a' ≠ 0 := right_ne_zero_of_mul ha
    have hd : d ^ 2 = 2 * a' ^ 2 := by linarith
    have hd₀ : d ≠ 0 := by
      rintro rfl
      have : 0 < a' ^ 2 := by positivity
      linarith
    have hlt : d.natAbs < n := by
      rw [← hn, Int.natAbs_lt_iff_sq_lt]
      have : 0 < a' ^ 2 := by positivity
      nlinarith
    exact ih _ hlt d a' rfl hd₀ hd

/-- `a ^ 2 + b ^ 2` and `a ^ 2 - b ^ 2` are not both squares when `b ≠ 0`. -/
theorem not_isSquare_sq_add_sq_and_sq_sub_sq {a b : ℤ} (hb : b ≠ 0) :
    ¬ (IsSquare (a ^ 2 + b ^ 2) ∧ IsSquare (a ^ 2 - b ^ 2)) := by
  rintro ⟨⟨u, hu⟩, ⟨v, hv⟩⟩
  have hu0 : u ≠ 0 := by
    rintro rfl
    have : 0 < b ^ 2 := by positivity
    nlinarith [sq_nonneg a]
  by_cases hv0 : v = 0
  · subst hv0
    exact sq_ne_two_mul_sq b hu0 (by linear_combination -hu + hv)
  · refine fourth_pow_sub_fourth_pow_ne_sq (a := a) hb (mul_ne_zero hu0 hv0) ?_
    linear_combination (a ^ 2 - b ^ 2) * hu + u * u * hv

end Int

namespace PythagoreanTriple

/-- **Fermat's right triangle theorem**, geometric form: the area of a Pythagorean triangle with
nonzero legs is not a square, i.e. `a * b ≠ 2 * d ^ 2`. -/
theorem mul_ne_two_mul_sq {a b c : ℤ} (h : PythagoreanTriple a b c) (ha : a ≠ 0) (hb : b ≠ 0)
    (d : ℤ) : a * b ≠ 2 * d ^ 2 := by
  intro hab
  have hd : d ≠ 0 := by
    rintro rfl
    exact mul_ne_zero ha hb (by simpa using hab)
  have key : c ^ 4 - (2 * d) ^ 4 = (a ^ 2 - b ^ 2) ^ 2 := by
    have e : (2 * d) ^ 4 = 4 * (a * b) ^ 2 := by rw [hab]; ring
    rw [e, show c ^ 4 = (c * c) ^ 2 by ring, ← h.eq]
    ring
  by_cases hz : a ^ 2 - b ^ 2 = 0
  · rcases sq_eq_sq_iff_eq_or_eq_neg.mp (sub_eq_zero.mp hz) with h₁ | h₁
    · subst h₁
      exact Int.sq_ne_two_mul_sq d ha (by linear_combination hab)
    · subst h₁
      have : 0 < b ^ 2 := by positivity
      nlinarith [sq_nonneg d]
  · exact Int.fourth_pow_sub_fourth_pow_ne_sq (mul_ne_zero two_ne_zero hd) hz key

end PythagoreanTriple

namespace Rat

/-- No right triangle with rational sides has area `1`: `1` is not a congruent number. -/
theorem mul_ne_two_of_sq_add_sq_eq_sq {a b c : ℚ} (h : a ^ 2 + b ^ 2 = c ^ 2) : a * b ≠ 2 := by
  intro hab
  have ha : a ≠ 0 := by rintro rfl; simp at hab
  have hb : b ≠ 0 := by rintro rfl; simp at hab
  obtain ⟨L, hL⟩ : ∃ L : ℤ, L = (a.den : ℤ) * b.den * c.den := ⟨_, rfl⟩
  have hL0 : (L : ℚ) ≠ 0 := by
    rw [hL]
    push_cast
    exact mul_ne_zero (mul_ne_zero (Nat.cast_ne_zero.mpr a.den_nz) (Nat.cast_ne_zero.mpr b.den_nz))
      (Nat.cast_ne_zero.mpr c.den_nz)
  obtain ⟨A, hAd⟩ : ∃ A : ℤ, A = a.num * b.den * c.den := ⟨_, rfl⟩
  obtain ⟨B, hBd⟩ : ∃ B : ℤ, B = b.num * a.den * c.den := ⟨_, rfl⟩
  obtain ⟨C, hCd⟩ : ∃ C : ℤ, C = c.num * a.den * b.den := ⟨_, rfl⟩
  have hA : (A : ℚ) = a * L := by
    rw [hAd, hL]
    push_cast
    rw [← Rat.mul_den_eq_num a]
    ring
  have hB : (B : ℚ) = b * L := by
    rw [hBd, hL]
    push_cast
    rw [← Rat.mul_den_eq_num b]
    ring
  have hC : (C : ℚ) = c * L := by
    rw [hCd, hL]
    push_cast
    rw [← Rat.mul_den_eq_num c]
    ring
  have htri : PythagoreanTriple A B C := by
    delta PythagoreanTriple
    have : (A : ℚ) * A + B * B = C * C := by
      rw [hA, hB, hC]
      linear_combination (L : ℚ) ^ 2 * h
    exact_mod_cast this
  have hA0 : A ≠ 0 := by
    intro h0
    have : (A : ℚ) = 0 := by exact_mod_cast h0
    rw [hA] at this
    exact mul_ne_zero ha hL0 this
  have hB0 : B ≠ 0 := by
    intro h0
    have : (B : ℚ) = 0 := by exact_mod_cast h0
    rw [hB] at this
    exact mul_ne_zero hb hL0 this
  refine htri.mul_ne_two_mul_sq hA0 hB0 L ?_
  have : (A : ℚ) * B = 2 * (L : ℚ) ^ 2 := by
    rw [hA, hB]
    linear_combination (L : ℚ) ^ 2 * hab
  exact_mod_cast this

end Rat
