import ATK.FracoesMalha
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

/-!
# ATK — A lei de linearização perto dos zeros triviais (rodada 106)

Perto de cada zero trivial `−2m`, a equação funcional dá `|ζ|` **exatamente**:

`|ζ(−2m − δ)| = 2·|sin(πδ/2)|·K_m(δ)`, `K_m(δ) = (2π)^{−(2m+1+δ)}·Γ(2m+1+δ)·|ζ(2m+1+δ)|` (`formula_exata`),

e daí, para `0 < δ < 1`, a **lei linear de dois lados** (`linearizacao`):

`2δ·K_m(δ) ≤ |ζ(−2m − δ)| ≤ πδ·K_m(δ)`.

Os quase-zeros da malha de 16 direções (rodada 105) são esta lei com `δ = γ₁ − 14`: a distância `δ` ao zero
trivial, vezes um fator que só depende de `m`. Quando `δ → 0`, `πK_m(0) = (2m)!ζ(2m+1)/(2(2π)^{2m}) = |ζ′(−2m)|`
(clássico; a identificação com a derivada não está formalizada aqui). `K_pos`: o fator é positivo.

Classificação: **consequência** (equação funcional). RH continua `OPEN_MATH`.
-/

open Complex

namespace ATK.Fracoes.Linearizacao

open ATK.Fracoes.Malha

/-- O fator `K_m(δ) = (2π)^{−(2m+1+δ)}·Γ(2m+1+δ)·|ζ(2m+1+δ)|`. -/
noncomputable def K (m : ℕ) (δ : ℝ) : ℝ :=
  (2 * Real.pi) ^ (-(2 * (m : ℝ) + 1 + δ)) * Real.Gamma (2 * m + 1 + δ) * a (2 * m + 1 + δ)

theorem K_pos (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) : 0 < K m δ := by
  have hm : (0 : ℝ) ≤ m := m.cast_nonneg
  unfold K
  have h1 : 0 < (2 * Real.pi) ^ (-(2 * (m : ℝ) + 1 + δ)) := Real.rpow_pos_of_pos (by positivity) _
  have h2 : 0 < Real.Gamma (2 * m + 1 + δ) := Real.Gamma_pos_of_pos (by linarith)
  have h3 : 0 < a (2 * m + 1 + δ) := by
    unfold a
    exact norm_pos_iff.mpr (riemannZeta_ne_zero_of_one_lt_re (by rw [ofReal_re]; linarith))
  positivity

/-- **Fórmula exata**: `|ζ(−2m − δ)| = 2·|sin(πδ/2)|·K_m(δ)`. -/
theorem formula_exata (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    a (-(2 * m + δ)) = 2 * |Real.sin (Real.pi * δ / 2)| * K m δ := by
  have hm : (0 : ℝ) ≤ m := m.cast_nonneg
  set σ : ℝ := 2 * m + 1 + δ with hσ
  have h0 : ∀ n : ℕ, (σ : ℂ) ≠ -n := by
    intro n h
    have := congrArg Complex.re h
    simp at this
    linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
  have h1 : (σ : ℂ) ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    simp at this
    linarith
  have e := riemannZeta_one_sub h0 h1
  have ec : (1 - (σ : ℂ)) = ((-(2 * m + δ) : ℝ) : ℂ) := by rw [hσ]; push_cast; ring
  rw [ec] at e
  unfold K a
  rw [← hσ, e]
  have hb : (2 * (Real.pi : ℂ)) = ((2 * Real.pi : ℝ) : ℂ) := by push_cast; ring
  have hc : (Real.pi : ℂ) * (σ : ℂ) / 2 = ((Real.pi * σ / 2 : ℝ) : ℂ) := by push_cast; ring
  rw [hb, hc, ← Complex.ofReal_cos, Complex.Gamma_ofReal, norm_mul, norm_mul, norm_mul, norm_mul,
    Complex.norm_cpow_eq_rpow_re_of_pos (by positivity), Complex.norm_real, Complex.norm_real,
    Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos (Real.Gamma_pos_of_pos (by linarith : (0 : ℝ) < σ))]
  have hre : (-(σ : ℂ)).re = -σ := by simp
  rw [hre]
  have hcos : |Real.cos (Real.pi * σ / 2)| = |Real.sin (Real.pi * δ / 2)| := by
    have e1 : Real.pi * σ / 2 = (Real.pi * δ / 2 + Real.pi / 2) + m * Real.pi := by rw [hσ]; ring
    rw [e1, Real.cos_add_nat_mul_pi, Real.cos_add_pi_div_two, abs_mul, abs_pow, abs_neg, abs_neg,
      abs_one, one_pow, one_mul]
  rw [hcos, show ‖(2 : ℂ)‖ = 2 by simp]
  ring

/-- **Lei linear de dois lados**: `2δ·K_m(δ) ≤ |ζ(−2m − δ)| ≤ πδ·K_m(δ)` para `0 < δ < 1`. -/
theorem linearizacao (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    2 * δ * K m δ ≤ a (-(2 * m + δ)) ∧ a (-(2 * m + δ)) ≤ Real.pi * δ * K m δ := by
  rw [formula_exata m hδ0 hδ1]
  have hK := (K_pos m hδ0).le
  have hx0 : 0 ≤ Real.pi * δ / 2 := by positivity
  have hx1 : Real.pi * δ / 2 ≤ Real.pi / 2 := by nlinarith [Real.pi_pos]
  have hs0 : 0 ≤ Real.sin (Real.pi * δ / 2) :=
    Real.sin_nonneg_of_nonneg_of_le_pi hx0 (by linarith [Real.pi_pos])
  rw [abs_of_nonneg hs0]
  have l := Real.mul_le_sin hx0 hx1
  have u := Real.sin_le hx0
  have e : 2 / Real.pi * (Real.pi * δ / 2) = δ := by field_simp
  rw [e] at l
  constructor
  · nlinarith
  · nlinarith

/-- A lei aplicada à malha (rodada 105): com `δ ∈ [0,13; 0,14]`, no ponto `−6 − δ` (anel de centro 8),
`0,26·K₃(δ) ≤ |ζ| ≤ 0,45·K₃(δ)`. -/
theorem anel_oito_linear {δ : ℝ} (h0 : 13 / 100 ≤ δ) (h1 : δ ≤ 14 / 100) :
    26 / 100 * K 3 δ ≤ a (-(2 * ((3 : ℕ) : ℝ) + δ)) ∧ a (-(2 * ((3 : ℕ) : ℝ) + δ)) ≤ 45 / 100 * K 3 δ := by
  obtain ⟨l, u⟩ := linearizacao 3 (by linarith) (by linarith)
  have hK := (K_pos 3 (by linarith : (0 : ℝ) < δ)).le
  have hπ := Real.pi_lt_d2
  have hπ' := Real.pi_gt_three
  generalize a (-(2 * ((3 : ℕ) : ℝ) + δ)) = A at l u ⊢
  generalize K 3 δ = k at l u hK ⊢
  have hpd : Real.pi * δ ≤ 45 / 100 := by nlinarith
  have hd2 : 26 / 100 ≤ 2 * δ := by linarith
  constructor
  · nlinarith [mul_le_mul_of_nonneg_right hd2 hK]
  · nlinarith [mul_le_mul_of_nonneg_right hpd hK]

end ATK.Fracoes.Linearizacao

#print axioms ATK.Fracoes.Linearizacao.K_pos
#print axioms ATK.Fracoes.Linearizacao.formula_exata
#print axioms ATK.Fracoes.Linearizacao.linearizacao
#print axioms ATK.Fracoes.Linearizacao.anel_oito_linear
