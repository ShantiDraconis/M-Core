import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.NumberTheory.ZetaValues
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta

/-!
# ATK — A malha de 16 direções em torno de `γ₁`: o que é lei e o que não é (rodada 105)

A malha `s_{c,k} = c + h·e^{ikπ/8}` (`k = 0, …, 15`, centros pares `c`, raio `h = γ₁ ≈ 14,1347`) foi usada
para procurar quase-zeros de `ζ`. Aqui fica o que dela é teorema.

* **Geometria** (`translacao`, `espelho`, `re_ponto`, `im_ponto`): trocar `c` por `c + 2` desloca cada ponto
  de `2`; a direção `16 − k` é o conjugado da direção `k`. **Só o espelho é simetria de `|ζ|`**
  (`norm_espelho`, reflexão de Schwarz); a translação não é (`ζ(s + 2) ≠ ζ(s)`).
* **Os anéis à direita** (`anel_direita`, `zeta_sub_um_le`, `anel_perto_de_um`, `centro_600270`): para
  `c ≥ 16` o anel inteiro está em `Re s > 1`, onde `ζ ≠ 0`; e para `Re s = σ ≥ 2`,
  `|ζ(s) − 1| ≤ 2^{2−σ}(π²/6 − 1)`. No centro `600 270` isso dá `|ζ − 1| ≤ 2^{−600 253}`. É uma cauda
  exponencial `e^{−(log 2)σ}`: a "lacuna" da série de Dirichlet é `log 2` (entre `n = 1` e `n = 2`).
* **O operador de deslocamento** (`deslocamento`): da equação funcional,
  `ζ(−1 − s)·ζ(s)·4π² = −(s + 1)s·ζ(s + 2)·ζ(1 − s)`. Em `s = 2m + 1 + δ` (`recorrencia`):
  `|ζ(−2(m+1) − δ)|·|ζ(2m+1+δ)|·4π² = (2m+2+δ)(2m+1+δ)·|ζ(2m+3+δ)|·|ζ(−2m−δ)|`.
* **O mínimo está no anel de centro 8** (`minimo_em_tres`, `minimo_global`): para `δ ∈ [0,13; 0,14]`,
  `|ζ(−2m − δ)|` decresce de `m = 1` a `m = 3` e cresce para `m ≥ 3`, porque `(2m+1+δ)(2m+2+δ)` cruza
  `4π² ≈ 39,48` entre `m = 2` e `m = 3`. Com `δ = γ₁ − 14` isso é o ponto `8 − γ₁ ≈ −6,1347` da malha
  (`ATK.Fracoes.MalhaZeros`). **Não é um quase-zero novo**: é o zero trivial `−6` visto a distância `δ`.

Classificação: **consequência** (equação funcional, série de Dirichlet). RH continua `OPEN_MATH`.
-/

open Complex

namespace ATK.Fracoes.Malha

/-- Ponto da malha: centro `c`, raio `h`, direção `k` (ângulo `kπ/8`). -/
noncomputable def ponto (c h : ℝ) (k : ℕ) : ℂ := (c : ℂ) + h * exp (((k * Real.pi / 8 : ℝ) : ℂ) * I)

/-! ## 1. Geometria -/

theorem translacao (c h : ℝ) (k : ℕ) : ponto (c + 2) h k = ponto c h k + 2 := by
  unfold ponto
  push_cast
  ring

theorem re_ponto (c h : ℝ) (k : ℕ) : (ponto c h k).re = c + h * Real.cos (k * Real.pi / 8) := by
  unfold ponto
  rw [add_re, ofReal_re, re_ofReal_mul, exp_ofReal_mul_I_re]

theorem im_ponto (c h : ℝ) (k : ℕ) : (ponto c h k).im = h * Real.sin (k * Real.pi / 8) := by
  unfold ponto
  rw [add_im, ofReal_im, im_ofReal_mul, exp_ofReal_mul_I_im, zero_add]

/-- **Espelho**: a direção `16 − k` é a conjugada da direção `k`. -/
theorem espelho (c h : ℝ) {k : ℕ} (hk : k ≤ 16) : ponto c h (16 - k) = (starRingEnd ℂ) (ponto c h k) := by
  unfold ponto
  have e : (((16 - k : ℕ) : ℝ) * Real.pi / 8 : ℝ) = 2 * Real.pi - k * Real.pi / 8 := by
    rw [Nat.cast_sub hk]
    push_cast
    ring
  rw [e, map_add, map_mul, Complex.conj_ofReal, Complex.conj_ofReal, ← Complex.exp_conj, map_mul,
    Complex.conj_ofReal, Complex.conj_I]
  congr 2
  push_cast
  rw [show ((2 * Real.pi - k * Real.pi / 8 : ℂ)) * I = 2 * Real.pi * I + (-(k * Real.pi / 8) * I) by ring,
    Complex.exp_add, Complex.exp_two_pi_mul_I, one_mul]
  congr 1
  ring

/-- **O espelho é simetria de `|ζ|`** (reflexão de Schwarz). -/
theorem norm_espelho (c h : ℝ) {k : ℕ} (hk : k ≤ 16) :
    ‖riemannZeta (ponto c h (16 - k))‖ = ‖riemannZeta (ponto c h k)‖ := by
  rw [espelho c h hk, riemannZeta_conj, Complex.norm_conj]

/-- Os pontos reais do anel de centro `2n`: `2n + h = 2(n + 7) + δ`, `2n − h = 2(n − 7) − δ` com `h = 14 + δ`. -/
theorem pontos_reais (n : ℤ) (δ : ℝ) :
    (2 * n : ℝ) + (14 + δ) = 2 * ((n : ℝ) + 7) + δ ∧ (2 * n : ℝ) - (14 + δ) = 2 * ((n : ℝ) - 7) - δ := by
  constructor <;> ring

/-! ## 2. Os anéis à direita: `ζ ≠ 0` e `|ζ − 1| ≤ 2^{2−σ}(π²/6 − 1)` -/

/-- Para `c ≥ 16` e `0 ≤ h < 15`, todo o anel está em `Re s > 1`, onde `ζ ≠ 0`. -/
theorem anel_direita {c h : ℝ} (hc : 16 ≤ c) (h0 : 0 ≤ h) (h15 : h < 15) (k : ℕ) :
    1 < (ponto c h k).re ∧ riemannZeta (ponto c h k) ≠ 0 := by
  have hcos := Real.neg_one_le_cos (k * Real.pi / 8)
  have hre : 1 < (ponto c h k).re := by
    rw [re_ponto]
    nlinarith
  exact ⟨hre, riemannZeta_ne_zero_of_one_lt_re hre⟩

theorem hasSum_inv_sq_desde_dois :
    HasSum (fun n : ℕ => 1 / ((n : ℝ) + 2) ^ 2) (Real.pi ^ 2 / 6 - 1) := by
  have h := (hasSum_nat_add_iff' 2).mpr hasSum_zeta_two
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, Nat.cast_zero, Nat.cast_one] at h
  norm_num at h
  convert h using 1
  funext n
  ring

/-- **Cauda exponencial de `ζ − 1`** em `Re s ≥ 2`. -/
theorem zeta_sub_um_le {s : ℂ} (hs : 2 ≤ s.re) :
    ‖riemannZeta s - 1‖ ≤ (2 : ℝ) ^ (2 - s.re) * (Real.pi ^ 2 / 6 - 1) := by
  have h1 : 1 < s.re := by linarith
  have hsum : Summable (fun n : ℕ => 1 / ((n : ℂ) + 1) ^ s) := by
    have := (Complex.summable_one_div_nat_cpow (p := s)).mpr h1
    exact (summable_nat_add_iff 1).mpr this |>.congr fun n => by push_cast; ring_nf
  rw [zeta_eq_tsum_one_div_nat_add_one_cpow h1, hsum.tsum_eq_zero_add]
  simp only [Nat.cast_zero, zero_add, one_cpow, div_one, add_sub_cancel_left]
  -- termo geral: `1/(n + 2)^s`
  have hterm : ∀ n : ℕ, ‖1 / (((n + 1 : ℕ) : ℂ) + 1) ^ s‖ ≤
      (2 : ℝ) ^ (2 - s.re) * (1 / ((n : ℝ) + 2) ^ 2) := by
    intro n
    have e : (((n + 1 : ℕ) : ℂ) + 1) = ((n + 2 : ℕ) : ℂ) := by push_cast; ring
    rw [e, norm_div, norm_one, norm_natCast_cpow_of_pos (by omega)]
    have hx : (2 : ℝ) ≤ ((n + 2 : ℕ) : ℝ) := by push_cast; linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
    have hxpos : (0 : ℝ) < ((n + 2 : ℕ) : ℝ) := by linarith
    have hsplit : ((n + 2 : ℕ) : ℝ) ^ s.re = ((n + 2 : ℕ) : ℝ) ^ (2 : ℝ) * ((n + 2 : ℕ) : ℝ) ^ (s.re - 2) := by
      rw [← Real.rpow_add hxpos]; ring_nf
    have hmono : (2 : ℝ) ^ (s.re - 2) ≤ ((n + 2 : ℕ) : ℝ) ^ (s.re - 2) :=
      Real.rpow_le_rpow (by norm_num) hx (by linarith)
    have h2pos : (0 : ℝ) < (2 : ℝ) ^ (s.re - 2) := Real.rpow_pos_of_pos (by norm_num) _
    have hneg : (2 : ℝ) ^ (2 - s.re) = 1 / (2 : ℝ) ^ (s.re - 2) := by
      rw [show (2 : ℝ) - s.re = -(s.re - 2) by ring, Real.rpow_neg (by norm_num), one_div]
    rw [hsplit, hneg, Real.rpow_two]
    have hsq : (0 : ℝ) < ((n + 2 : ℕ) : ℝ) ^ 2 := by positivity
    have e2 : ((n : ℝ) + 2) ^ 2 = ((n + 2 : ℕ) : ℝ) ^ 2 := by push_cast; ring
    rw [e2, div_mul_div_comm, one_mul]
    apply one_div_le_one_div_of_le (by positivity)
    rw [mul_comm]
    exact mul_le_mul_of_nonneg_left hmono hsq.le
  have hS : Summable (fun n : ℕ => (2 : ℝ) ^ (2 - s.re) * (1 / ((n : ℝ) + 2) ^ 2)) :=
    hasSum_inv_sq_desde_dois.summable.mul_left _
  have hnorm : Summable (fun n : ℕ => ‖1 / (((n + 1 : ℕ) : ℂ) + 1) ^ s‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hterm hS
  calc ‖∑' n : ℕ, 1 / (((n + 1 : ℕ) : ℂ) + 1) ^ s‖
      ≤ ∑' n : ℕ, ‖1 / (((n + 1 : ℕ) : ℂ) + 1) ^ s‖ := norm_tsum_le_tsum_norm hnorm
    _ ≤ ∑' n : ℕ, (2 : ℝ) ^ (2 - s.re) * (1 / ((n : ℝ) + 2) ^ 2) :=
        Summable.tsum_le_tsum hterm hnorm hS
    _ = (2 : ℝ) ^ (2 - s.re) * (Real.pi ^ 2 / 6 - 1) := by
        rw [tsum_mul_left, hasSum_inv_sq_desde_dois.tsum_eq]

theorem pi_quad : Real.pi ^ 2 / 6 - 1 < 2 / 3 := by
  have := Real.pi_lt_d2
  nlinarith [Real.pi_pos]

/-- `2^{2−σ} ≤ 4/2^k` para `σ ≥ k`. -/
theorem dois_rpow_le {σ : ℝ} {k : ℕ} (h : (k : ℝ) ≤ σ) : (2 : ℝ) ^ (2 - σ) ≤ 4 / 2 ^ k := by
  calc (2 : ℝ) ^ (2 - σ) ≤ (2 : ℝ) ^ (2 - (k : ℝ)) :=
        Real.rpow_le_rpow_of_exponent_le (by norm_num) (by linarith)
    _ = 4 / 2 ^ k := by
        rw [Real.rpow_sub (by norm_num), Real.rpow_two, Real.rpow_natCast]
        norm_num

/-- **Para `c ≥ 18` o anel inteiro tem `|ζ − 1| ≤ 2^{2−(c−h)}·2/3`.** -/
theorem anel_perto_de_um {c h : ℝ} (hc : 18 ≤ c) (h0 : 0 ≤ h) (h15 : h ≤ 15) (k : ℕ) :
    ‖riemannZeta (ponto c h k) - 1‖ ≤ (2 : ℝ) ^ (2 - (c - h)) * (2 / 3) := by
  have hcos := Real.neg_one_le_cos (k * Real.pi / 8)
  have hre : c - h ≤ (ponto c h k).re := by rw [re_ponto]; nlinarith
  have h2 : 2 ≤ (ponto c h k).re := by linarith
  calc ‖riemannZeta (ponto c h k) - 1‖
      ≤ (2 : ℝ) ^ (2 - (ponto c h k).re) * (Real.pi ^ 2 / 6 - 1) := zeta_sub_um_le h2
    _ ≤ (2 : ℝ) ^ (2 - (c - h)) * (2 / 3) := by
        apply mul_le_mul (Real.rpow_le_rpow_of_exponent_le (by norm_num) (by linarith))
          pi_quad.le (by nlinarith [Real.pi_gt_three]) (by positivity)

/-- **Centro 600 270**: nos 16 pontos, `|ζ(s) − 1| ≤ 2^{−600 253}`. -/
theorem centro_600270 {h : ℝ} (h0 : 0 ≤ h) (h15 : h ≤ 15) (k : ℕ) :
    ‖riemannZeta (ponto 600270 h k) - 1‖ ≤ (2 : ℝ) ^ (-600253 : ℝ) := by
  calc ‖riemannZeta (ponto 600270 h k) - 1‖ ≤ (2 : ℝ) ^ (2 - (600270 - h)) * (2 / 3) :=
        anel_perto_de_um (by norm_num) h0 h15 k
    _ ≤ (2 : ℝ) ^ (-600253 : ℝ) * 1 := by
        apply mul_le_mul (Real.rpow_le_rpow_of_exponent_le (by norm_num) (by linarith)) (by norm_num)
          (by norm_num) (by positivity)
    _ = (2 : ℝ) ^ (-600253 : ℝ) := mul_one _

/-! ## 3. O operador de deslocamento `s ↦ s + 2` -/

/-- **Deslocamento** (equação funcional duas vezes):
`ζ(−1 − s)·ζ(s)·4π² = −(s + 1)s·ζ(s + 2)·ζ(1 − s)`. -/
theorem deslocamento {s : ℂ} (h0 : ∀ n : ℕ, s ≠ -n) (h1 : s ≠ 1) (h2 : ∀ n : ℕ, s + 2 ≠ -n)
    (h3 : s + 2 ≠ 1) :
    riemannZeta (-1 - s) * riemannZeta s * (4 * (Real.pi : ℂ) ^ 2) =
      -((s + 1) * s) * riemannZeta (s + 2) * riemannZeta (1 - s) := by
  have e1 := riemannZeta_one_sub h0 h1
  have e2 := riemannZeta_one_sub h2 h3
  rw [show (1 : ℂ) - (s + 2) = -1 - s by ring] at e2
  have hs0 : s ≠ 0 := by simpa using h0 0
  have hs1 : s + 1 ≠ 0 := by
    intro h
    apply h0 1
    push_cast
    linear_combination h
  have hG : Gamma (s + 2) = (s + 1) * s * Gamma s := by
    rw [show s + 2 = (s + 1) + 1 by ring, Complex.Gamma_add_one _ hs1, Complex.Gamma_add_one _ hs0]
    ring
  have hc : Complex.cos ((Real.pi : ℂ) * (s + 2) / 2) = -Complex.cos ((Real.pi : ℂ) * s / 2) := by
    rw [show (Real.pi : ℂ) * (s + 2) / 2 = (Real.pi : ℂ) * s / 2 + Real.pi by ring, Complex.cos_add_pi]
  have h2π : (2 * (Real.pi : ℂ)) ≠ 0 := by
    have : (Real.pi : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
    exact mul_ne_zero two_ne_zero this
  have hp2 : (2 * (Real.pi : ℂ)) ^ (-(2 : ℂ)) = 1 / (4 * (Real.pi : ℂ) ^ 2) := by
    rw [Complex.cpow_neg, Complex.cpow_ofNat]
    ring
  have hp : (2 * (Real.pi : ℂ)) ^ (-(s + 2)) = (2 * Real.pi) ^ (-s) * (1 / (4 * (Real.pi : ℂ) ^ 2)) := by
    rw [show -(s + 2) = -s + -(2 : ℂ) by ring, Complex.cpow_add _ _ h2π, hp2]
  rw [e2, hG, hc, hp, e1]
  have hπ : (Real.pi : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
  field_simp

/-- `|ζ|` num ponto real. -/
noncomputable def a (x : ℝ) : ℝ := ‖riemannZeta (x : ℂ)‖

/-- **A recorrência no eixo negativo**, em `s = 2m + 1 + δ`, `0 < δ < 1`. -/
theorem recorrencia (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    a (-(2 * m + 2 + δ)) * a (2 * m + 1 + δ) * (4 * Real.pi ^ 2) =
      (2 * m + 2 + δ) * (2 * m + 1 + δ) * a (2 * m + 3 + δ) * a (-(2 * m + δ)) := by
  set s : ℂ := ((2 * m + 1 + δ : ℝ) : ℂ) with hs
  have hre : s.re = 2 * m + 1 + δ := by rw [hs, ofReal_re]
  have hm : (0 : ℝ) ≤ m := m.cast_nonneg
  have h0 : ∀ n : ℕ, s ≠ -n := by
    intro n h
    have := congrArg Complex.re h
    rw [hre] at this
    simp at this
    linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
  have h1 : s ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    rw [hre] at this
    simp at this
    linarith
  have h2 : ∀ n : ℕ, s + 2 ≠ -n := by
    intro n h
    have := congrArg Complex.re h
    rw [add_re, hre] at this
    simp at this
    linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
  have h3 : s + 2 ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    rw [add_re, hre] at this
    simp at this
    linarith
  have ea : (-1 - s) = ((-(2 * m + 2 + δ) : ℝ) : ℂ) := by rw [hs]; push_cast; ring
  have eb : (s + 2) = ((2 * m + 3 + δ : ℝ) : ℂ) := by rw [hs]; push_cast; ring
  have ec : (1 - s) = ((-(2 * m + δ) : ℝ) : ℂ) := by rw [hs]; push_cast; ring
  have ed : s + 1 = ((2 * m + 2 + δ : ℝ) : ℂ) := by rw [hs]; push_cast; ring
  have key := deslocamento h0 h1 h2 h3
  rw [ea, eb, ec, ed, hs] at key
  have key2 := congrArg (fun z : ℂ => ‖z‖) key
  simp only [norm_mul, norm_neg, norm_pow, Complex.norm_ofNat, Complex.norm_real,
    Real.norm_eq_abs] at key2
  rw [abs_of_pos Real.pi_pos, abs_of_pos (by linarith : (0 : ℝ) < 2 * m + 2 + δ),
    abs_of_pos (by linarith : (0 : ℝ) < 2 * m + 1 + δ)] at key2
  unfold a
  linear_combination key2

/-- `ζ ≠ 0` em `−2m − δ`, `0 < δ < 1` (a equação funcional não tem fator nulo ali). -/
theorem a_pos (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) : 0 < a (-(2 * m + δ)) := by
  unfold a
  apply norm_pos_iff.mpr
  set s : ℂ := ((2 * m + 1 + δ : ℝ) : ℂ) with hs
  have hre : s.re = 2 * m + 1 + δ := by rw [hs, ofReal_re]
  have hm : (0 : ℝ) ≤ m := m.cast_nonneg
  have h0 : ∀ n : ℕ, s ≠ -n := by
    intro n h
    have := congrArg Complex.re h
    rw [hre] at this
    simp at this
    linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
  have h1 : s ≠ 1 := by
    intro h
    have := congrArg Complex.re h
    rw [hre] at this
    simp at this
    linarith
  have e := riemannZeta_one_sub h0 h1
  have ec : (1 - s) = ((-(2 * m + δ) : ℝ) : ℂ) := by rw [hs]; push_cast; ring
  rw [ec] at e
  rw [e]
  have h2π : (2 * (Real.pi : ℂ)) ≠ 0 :=
    mul_ne_zero two_ne_zero (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero)
  refine mul_ne_zero (mul_ne_zero (mul_ne_zero (mul_ne_zero two_ne_zero ?_) (Complex.Gamma_ne_zero h0)) ?_) ?_
  · exact (Complex.cpow_ne_zero_iff_of_exponent_ne_zero (by
      intro h; have := congrArg Complex.re h; simp [hre] at this; linarith)).mpr h2π
  · intro hcos
    obtain ⟨k, hk⟩ := Complex.cos_eq_zero_iff.mp hcos
    have hk' := congrArg Complex.re hk
    have hπ : (Real.pi : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
    have e2 : s = 2 * k + 1 := by
      have hz : (Real.pi : ℂ) * (s - (2 * k + 1)) = 0 := by linear_combination 2 * hk
      rcases mul_eq_zero.mp hz with h | h
      · exact absurd h hπ
      · linear_combination h
    have e3 := congrArg Complex.re e2
    rw [hre] at e3
    simp at e3
    -- `δ = 2(k − m)` com `0 < δ < 1`: impossível
    have hk1 : (0 : ℝ) < 2 * ((k : ℝ) - m) := by linarith
    have hk2 : 2 * ((k : ℝ) - m) < 1 := by linarith
    have hj : (0 : ℝ) < ((k - m : ℤ) : ℝ) := by push_cast; linarith
    have hj2 : ((k - m : ℤ) : ℝ) < 1 := by push_cast; linarith
    have i1 : (0 : ℤ) < k - m := by exact_mod_cast hj
    have i2 : (k - m : ℤ) < 1 := by exact_mod_cast hj2
    omega
  · exact riemannZeta_ne_zero_of_one_lt_re (by rw [hre]; linarith)

/-- `1 − ε ≤ |ζ(σ)| ≤ 1 + ε`, `ε = 2^{2−σ}·2/3`, para `σ ≥ 2` real. -/
theorem a_perto_de_um {σ : ℝ} (hσ : 2 ≤ σ) :
    1 - (2 : ℝ) ^ (2 - σ) * (2 / 3) ≤ a σ ∧ a σ ≤ 1 + (2 : ℝ) ^ (2 - σ) * (2 / 3) := by
  have hz := zeta_sub_um_le (s := (σ : ℂ)) (by rw [ofReal_re]; exact hσ)
  rw [ofReal_re] at hz
  have hz' : ‖riemannZeta (σ : ℂ) - 1‖ ≤ (2 : ℝ) ^ (2 - σ) * (2 / 3) :=
    hz.trans (mul_le_mul_of_nonneg_left pi_quad.le (by positivity))
  have t := abs_norm_sub_norm_le (riemannZeta (σ : ℂ)) 1
  rw [norm_one] at t
  unfold a
  constructor <;> linarith [abs_le.mp (t.trans hz')]

/-- `1 − (4/2^k)(2/3) ≤ |ζ(σ)| ≤ 1 + (4/2^k)(2/3)` para `σ ≥ k ≥ 2`. -/
theorem a_cotas {σ : ℝ} {k : ℕ} (hk : 2 ≤ k) (hσ : (k : ℝ) ≤ σ) :
    1 - 4 / 2 ^ k * (2 / 3) ≤ a σ ∧ a σ ≤ 1 + 4 / 2 ^ k * (2 / 3) := by
  have hk' : (2 : ℝ) ≤ k := by exact_mod_cast hk
  obtain ⟨l, u⟩ := a_perto_de_um (σ := σ) (by linarith)
  have e := dois_rpow_le hσ
  constructor <;> nlinarith

/-- Um passo para baixo: se `P·|ζ(2m+3+δ)| < |ζ(2m+1+δ)|·4π²`, então `|ζ(−2(m+1)−δ)| < |ζ(−2m−δ)|`. -/
theorem passo_desce (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) (hZ : 0 < a (2 * m + 1 + δ))
    (h : (2 * m + 2 + δ) * (2 * m + 1 + δ) * a (2 * m + 3 + δ) < a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) :
    a (-(2 * ((m + 1 : ℕ) : ℝ) + δ)) < a (-(2 * m + δ)) := by
  have r := recorrencia m hδ0 hδ1
  have ap := a_pos m hδ0 hδ1
  have eidx : (-(2 * ((m + 1 : ℕ) : ℝ) + δ)) = -(2 * (m : ℝ) + 2 + δ) := by push_cast; ring
  rw [eidx]
  have hK : 0 < a (2 * m + 1 + δ) * (4 * Real.pi ^ 2) := by positivity
  have e : a (-(2 * m + 2 + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) =
      ((2 * m + 2 + δ) * (2 * m + 1 + δ) * a (2 * m + 3 + δ)) * a (-(2 * m + δ)) := by
    linear_combination r
  have : a (-(2 * m + 2 + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) <
      a (-(2 * m + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) := by
    rw [e, mul_comm (a (-(2 * m + δ)))]
    exact mul_lt_mul_of_pos_right h ap
  exact lt_of_mul_lt_mul_right this hK.le

/-- Um passo para cima: se `|ζ(2m+1+δ)|·4π² < P·|ζ(2m+3+δ)|`, então `|ζ(−2m−δ)| < |ζ(−2(m+1)−δ)|`. -/
theorem passo_sobe (m : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) (hZ : 0 < a (2 * m + 1 + δ))
    (h : a (2 * m + 1 + δ) * (4 * Real.pi ^ 2) < (2 * m + 2 + δ) * (2 * m + 1 + δ) * a (2 * m + 3 + δ)) :
    a (-(2 * m + δ)) < a (-(2 * ((m + 1 : ℕ) : ℝ) + δ)) := by
  have r := recorrencia m hδ0 hδ1
  have ap := a_pos m hδ0 hδ1
  have eidx : (-(2 * ((m + 1 : ℕ) : ℝ) + δ)) = -(2 * (m : ℝ) + 2 + δ) := by push_cast; ring
  rw [eidx]
  have hK : 0 < a (2 * m + 1 + δ) * (4 * Real.pi ^ 2) := by positivity
  have e : a (-(2 * m + 2 + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) =
      ((2 * m + 2 + δ) * (2 * m + 1 + δ) * a (2 * m + 3 + δ)) * a (-(2 * m + δ)) := by
    linear_combination r
  have : a (-(2 * m + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) <
      a (-(2 * m + 2 + δ)) * (a (2 * m + 1 + δ) * (4 * Real.pi ^ 2)) := by
    rw [e, mul_comm _ (a (-(2 * m + δ)))]
    exact mul_lt_mul_of_pos_left h ap
  exact lt_of_mul_lt_mul_right this hK.le

/-- **O mínimo em `m = 3`**: para `δ ∈ [0,13; 0,14]`, `|ζ(−2m−δ)|` decresce de `m = 1` a `m = 3` e
cresce para todo `m ≥ 3`. -/
theorem minimo_em_tres {δ : ℝ} (h0 : 13 / 100 ≤ δ) (h1 : δ ≤ 14 / 100) :
    a (-(2 * ((1 + 1 : ℕ) : ℝ) + δ)) < a (-(2 * ((1 : ℕ) : ℝ) + δ)) ∧
      a (-(2 * ((2 + 1 : ℕ) : ℝ) + δ)) < a (-(2 * ((2 : ℕ) : ℝ) + δ)) ∧
      ∀ m : ℕ, 3 ≤ m → a (-(2 * (m : ℝ) + δ)) < a (-(2 * ((m + 1 : ℕ) : ℝ) + δ)) := by
  have hδ0 : 0 < δ := by linarith
  have hδ1 : δ < 1 := by linarith
  have hπ1 := Real.pi_gt_d2
  have hπ2 := Real.pi_lt_d2
  have P1 : (3943 / 100 : ℝ) < 4 * Real.pi ^ 2 := by nlinarith
  have P2 : 4 * Real.pi ^ 2 < (40 : ℝ) := by nlinarith
  refine ⟨?_, ?_, fun m hm => ?_⟩
  · obtain ⟨z1, -⟩ := a_cotas (σ := 2 * ((1 : ℕ) : ℝ) + 1 + δ) (k := 3) (by norm_num) (by push_cast; linarith)
    obtain ⟨-, z2⟩ := a_cotas (σ := 2 * ((1 : ℕ) : ℝ) + 3 + δ) (k := 5) (by norm_num) (by push_cast; linarith)
    rw [show (4 : ℝ) / 2 ^ 3 * (2 / 3) = 1 / 3 by norm_num] at z1
    rw [show (4 : ℝ) / 2 ^ 5 * (2 / 3) = 1 / 12 by norm_num] at z2
    have hZ : 0 < a (2 * ((1 : ℕ) : ℝ) + 1 + δ) := lt_of_lt_of_le (by norm_num) z1
    refine passo_desce 1 hδ0 hδ1 hZ ?_
    have n2 : 0 ≤ a (2 * ((1 : ℕ) : ℝ) + 3 + δ) := norm_nonneg _
    simp only [Nat.cast_one] at z1 z2 n2 hZ ⊢
    have hP : (2 * (1 : ℝ) + 2 + δ) * (2 * 1 + 1 + δ) ≤ 14 := by nlinarith
    have u := mul_le_mul hP z2 n2 (by norm_num)
    have l := mul_le_mul z1 P1.le (by norm_num) hZ.le
    exact lt_of_le_of_lt u (lt_of_lt_of_le (by norm_num) l)
  · obtain ⟨z1, -⟩ := a_cotas (σ := 2 * ((2 : ℕ) : ℝ) + 1 + δ) (k := 5) (by norm_num) (by push_cast; linarith)
    obtain ⟨-, z2⟩ := a_cotas (σ := 2 * ((2 : ℕ) : ℝ) + 3 + δ) (k := 7) (by norm_num) (by push_cast; linarith)
    rw [show (4 : ℝ) / 2 ^ 5 * (2 / 3) = 1 / 12 by norm_num] at z1
    rw [show (4 : ℝ) / 2 ^ 7 * (2 / 3) = 1 / 48 by norm_num] at z2
    have hZ : 0 < a (2 * ((2 : ℕ) : ℝ) + 1 + δ) := lt_of_lt_of_le (by norm_num) z1
    refine passo_desce 2 hδ0 hδ1 hZ ?_
    have n2 : 0 ≤ a (2 * ((2 : ℕ) : ℝ) + 3 + δ) := norm_nonneg _
    simp only [Nat.cast_ofNat] at z1 z2 n2 hZ ⊢
    have hP : (2 * (2 : ℝ) + 2 + δ) * (2 * 2 + 1 + δ) ≤ 3156 / 100 := by nlinarith
    have u := mul_le_mul hP z2 n2 (by norm_num)
    have l := mul_le_mul z1 P1.le (by norm_num) hZ.le
    exact lt_of_le_of_lt u (lt_of_lt_of_le (by norm_num) l)
  · have hm' : (3 : ℝ) ≤ m := by exact_mod_cast hm
    obtain ⟨z0, -⟩ := a_cotas (σ := 2 * (m : ℝ) + 1 + δ) (k := 7) (by norm_num) (by push_cast; linarith)
    obtain ⟨-, z1⟩ := a_cotas (σ := 2 * (m : ℝ) + 1 + δ) (k := 7) (by norm_num) (by push_cast; linarith)
    obtain ⟨z2, -⟩ := a_cotas (σ := 2 * (m : ℝ) + 3 + δ) (k := 9) (by norm_num) (by push_cast; linarith)
    rw [show (4 : ℝ) / 2 ^ 7 * (2 / 3) = 1 / 48 by norm_num] at z0 z1
    rw [show (4 : ℝ) / 2 ^ 9 * (2 / 3) = 1 / 192 by norm_num] at z2
    have hZ : 0 < a (2 * (m : ℝ) + 1 + δ) := lt_of_lt_of_le (by norm_num) z0
    refine passo_sobe m hδ0 hδ1 hZ ?_
    generalize (m : ℝ) = x at hm' z0 z1 z2 hZ ⊢
    have hP : (56 : ℝ) ≤ (2 * x + 2 + δ) * (2 * x + 1 + δ) := by nlinarith
    nlinarith [mul_le_mul hP z2 (by norm_num) (by positivity)]

/-- **Mínimo global** entre os pontos `−2m − δ`, `m ≥ 1`: é `m = 3`. -/
theorem minimo_global {δ : ℝ} (h0 : 13 / 100 ≤ δ) (h1 : δ ≤ 14 / 100) :
    ∀ m : ℕ, 1 ≤ m → m ≠ 3 → a (-(2 * ((3 : ℕ) : ℝ) + δ)) < a (-(2 * (m : ℝ) + δ)) := by
  obtain ⟨d12, d23, inc⟩ := minimo_em_tres h0 h1
  have up : ∀ j : ℕ, a (-(2 * ((3 : ℕ) : ℝ) + δ)) < a (-(2 * ((j + 4 : ℕ) : ℝ) + δ)) := by
    intro j
    induction j with
    | zero => exact inc 3 le_rfl
    | succ j ih => exact ih.trans (inc (j + 4) (by omega))
  intro m hm h3
  rcases (show m = 1 ∨ m = 2 ∨ 4 ≤ m by omega) with rfl | rfl | h4
  · exact d23.trans d12
  · exact d23
  · obtain ⟨j, rfl⟩ : ∃ j, m = j + 4 := ⟨m - 4, by omega⟩
    exact up j

end ATK.Fracoes.Malha

#print axioms ATK.Fracoes.Malha.translacao
#print axioms ATK.Fracoes.Malha.re_ponto
#print axioms ATK.Fracoes.Malha.im_ponto
#print axioms ATK.Fracoes.Malha.espelho
#print axioms ATK.Fracoes.Malha.norm_espelho
#print axioms ATK.Fracoes.Malha.pontos_reais
#print axioms ATK.Fracoes.Malha.anel_direita
#print axioms ATK.Fracoes.Malha.hasSum_inv_sq_desde_dois
#print axioms ATK.Fracoes.Malha.zeta_sub_um_le
#print axioms ATK.Fracoes.Malha.pi_quad
#print axioms ATK.Fracoes.Malha.dois_rpow_le
#print axioms ATK.Fracoes.Malha.anel_perto_de_um
#print axioms ATK.Fracoes.Malha.centro_600270
#print axioms ATK.Fracoes.Malha.deslocamento
#print axioms ATK.Fracoes.Malha.recorrencia
#print axioms ATK.Fracoes.Malha.a_pos
#print axioms ATK.Fracoes.Malha.a_perto_de_um
#print axioms ATK.Fracoes.Malha.a_cotas
#print axioms ATK.Fracoes.Malha.passo_desce
#print axioms ATK.Fracoes.Malha.passo_sobe
#print axioms ATK.Fracoes.Malha.minimo_em_tres
#print axioms ATK.Fracoes.Malha.minimo_global
