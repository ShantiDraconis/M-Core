import Mathlib

/-!
# ATK — O critério de Li truncado (rodada 108)

Li (1997): `λₙ = Σ_ρ [1 − (1 − 1/ρ)ⁿ]` e **RH ⟺ λₙ ≥ 0 para todo n ≥ 1**. A soma infinita (com a ordem de
Keiper–Li e as multiplicidades) não está no Mathlib. Aqui ficam as somas **finitas**, que o Mathlib já sabe
definir para ζ: os zeros num disco `‖ρ‖ ≤ T` formam um conjunto finito (`IsCompact.inter_riemannZetaZeros_finite`).
Só Mathlib; nenhum `sorry`, nenhum axioma novo.

## Leis

* **Lei 1 — sinal no círculo** (`re_um_sub_pow_nonneg`, `liS_nao_negativo`): se `Re ρ ≥ ½`, cada parcela tem
  `Re(1 − w(ρ)ⁿ) ≥ 0`, com `w(ρ) = 1 − 1/ρ`; `|w(ρ)|² − 1 = (1 − 2 Re ρ)/|ρ|²` (`norm_w_sq_sub_one`).
* **Lei 2 — um zero fora domina** (`re_soma_pot_ilimitada`, `liS_ilimitado`): numa família finita qualquer, se
  um ponto tem `Re ρ < ½`, então `λₙ(S)` fica abaixo de qualquer `−M` para `n` arbitrariamente grande.
  Nenhuma quantidade finita de zeros na reta compensa um zero fora dela. (Aproximação de Dirichlet simultânea,
  `dirichlet_simultaneo`, por casas de pombo.)
* **Lei 3 — critério de Li finito** (`liS_criterio`): `(∀ n, λₙ(S) ≥ 0) ⟺ ∀ ρ ∈ S, Re ρ ≥ ½`.
* **Lei 4 — RH em somas finitas** (`rh_iff_liT`): `RiemannHypothesis ⟺ ∀ T ∀ n, λₙ^{(T)} ≥ 0`, onde
  `λₙ^{(T)}` soma sobre os zeros não triviais com `‖ρ‖ ≤ T` (sem multiplicidade). Se RH falhar,
  `liT_ilimitado`: a partir da altura do zero fora, **todas** as truncagens descem a `−∞`. Sob RH elas
  crescem com `T` (`liT_mono`).
* **Lei 5 — o fator arquimediano sozinho não tem sinal** (`principal_negativo`): o termo principal
  `(n/2)(log n − 1 + γ − log 2π)` de `λₙ` é negativo para `1 ≤ n ≤ 6`, embora `λₙ > 0` ali (Keiper–Li
  certificado no Arb, `pesquisa/li/`). O sinal de `λₙ` não sai de `π`, `Γ` e convexidade.
* **Lei 6 — Davenport–Heilbronn** (`dh_taxa`, `dh_obstrucao`): para a bola certificada do zero
  `0,8085171824… + 85,6993484853…i` (Newton intervalar no Arb; aqui é hipótese, nada de `f`), o refletido
  `σ = 1 − β + iγ` tem `|w(σ)|² − 1 ∈ (8,4014·10⁻⁵; 8,4015·10⁻⁵)`; toda soma de Li finita que contém `σ`
  é ilimitada para baixo. Mesma equação funcional, mesmo `Γ`, mesmo `π` de `L(s, χ mod 5)`: a positividade
  não pode vir só do fator arquimediano.

Classificação: **reformulação** (Lei 4) e **consequência** (as demais). RH continua `OPEN_MATH`: a passagem
`λₙ = lim_T λₙ^{(T)}` (com multiplicidades e a ordem de soma) não está formalizada.
-/

open Complex Filter Topology

namespace ATK.LiTrunc

/-! ### `w(ρ) = 1 − 1/ρ` -/

/-- `w(ρ) = 1 − 1/ρ`. -/
noncomputable def w (ρ : ℂ) : ℂ := 1 - 1 / ρ

theorem w_eq {ρ : ℂ} (h : ρ ≠ 0) : w ρ = (ρ - 1) / ρ := by
  unfold w; field_simp

theorem normSq_pos_re_im {ρ : ℂ} (h : ρ ≠ 0) : 0 < ρ.re ^ 2 + ρ.im ^ 2 := by
  have := Complex.normSq_pos.mpr h
  rw [Complex.normSq_apply] at this
  nlinarith

theorem norm_w_sq {ρ : ℂ} (h : ρ ≠ 0) :
    ‖w ρ‖ ^ 2 = ((ρ.re - 1) ^ 2 + ρ.im ^ 2) / (ρ.re ^ 2 + ρ.im ^ 2) := by
  rw [w_eq h, norm_div, div_pow, Complex.sq_norm, Complex.sq_norm, Complex.normSq_apply,
    Complex.normSq_apply]
  simp only [sub_re, sub_im, one_re, one_im, sub_zero]
  ring_nf

/-- `|w|² − 1 = (1 − 2 Re ρ)/|ρ|²`. -/
theorem norm_w_sq_sub_one {ρ : ℂ} (h : ρ ≠ 0) :
    ‖w ρ‖ ^ 2 - 1 = (1 - 2 * ρ.re) / (ρ.re ^ 2 + ρ.im ^ 2) := by
  rw [norm_w_sq h]
  have := normSq_pos_re_im h
  field_simp
  ring

theorem w_fora_iff {ρ : ℂ} (h : ρ ≠ 0) : 1 < ‖w ρ‖ ↔ ρ.re < 1 / 2 := by
  have hp := normSq_pos_re_im h
  have key := norm_w_sq_sub_one h
  have h0 := norm_nonneg (w ρ)
  constructor
  · intro h1
    have : 0 < ‖w ρ‖ ^ 2 - 1 := by nlinarith
    rw [key] at this
    have := (div_pos_iff.mp this)
    rcases this with ⟨a, _⟩ | ⟨_, b⟩
    · linarith
    · linarith
  · intro h1
    have : 0 < ‖w ρ‖ ^ 2 - 1 := by rw [key]; exact div_pos (by linarith) hp
    nlinarith

theorem w_le_one_iff {ρ : ℂ} (h : ρ ≠ 0) : ‖w ρ‖ ≤ 1 ↔ 1 / 2 ≤ ρ.re := by
  rw [← not_lt, ← not_lt, w_fora_iff h]

/-! ### Lei 1: o sinal de cada parcela -/

theorem re_um_sub_pow_nonneg {z : ℂ} (hz : ‖z‖ ≤ 1) (n : ℕ) : 0 ≤ (1 - z ^ n).re := by
  have h1 : ‖z ^ n‖ ≤ 1 := by rw [norm_pow]; exact pow_le_one₀ (norm_nonneg _) hz
  have := Complex.re_le_norm (z ^ n)
  simp only [sub_re, one_re]
  linarith

/-- A soma de Li sobre um conjunto finito: `λₙ(S) = Σ_{ρ∈S} Re(1 − w(ρ)ⁿ)`. -/
noncomputable def liS (S : Finset ℂ) (n : ℕ) : ℝ := ∑ ρ ∈ S, (1 - w ρ ^ n).re

theorem liS_eq (S : Finset ℂ) (n : ℕ) : liS S n = S.card - (∑ ρ ∈ S, w ρ ^ n).re := by
  unfold liS
  rw [Complex.re_sum]
  simp [Finset.sum_sub_distrib]

/-- **Lei 1.** Se todo ponto tem `Re ρ ≥ ½`, todas as somas de Li são `≥ 0`. -/
theorem liS_nao_negativo {S : Finset ℂ} (h : ∀ ρ ∈ S, ρ ≠ 0 ∧ 1 / 2 ≤ ρ.re) (n : ℕ) :
    0 ≤ liS S n :=
  Finset.sum_nonneg fun ρ hρ =>
    re_um_sub_pow_nonneg ((w_le_one_iff (h ρ hρ).1).mpr (h ρ hρ).2) n

/-! ### Lei 2: aproximação de Dirichlet simultânea e o zero que domina -/

theorem caixa {q : ℕ} (hq : 0 < q) {x y : ℝ}
    (h : ⌊(q : ℝ) * Int.fract x⌋₊ = ⌊(q : ℝ) * Int.fract y⌋₊) :
    |Int.fract x - Int.fract y| < 1 / q := by
  have hq' : (0 : ℝ) < q := by exact_mod_cast hq
  have hx0 : 0 ≤ (q : ℝ) * Int.fract x := mul_nonneg hq'.le (Int.fract_nonneg x)
  have hy0 : 0 ≤ (q : ℝ) * Int.fract y := mul_nonneg hq'.le (Int.fract_nonneg y)
  have a1 := Nat.floor_le hx0
  have a2 := Nat.lt_floor_add_one ((q : ℝ) * Int.fract x)
  have b1 := Nat.floor_le hy0
  have b2 := Nat.lt_floor_add_one ((q : ℝ) * Int.fract y)
  rw [h] at a1 a2
  have hd : |(q : ℝ) * Int.fract x - (q : ℝ) * Int.fract y| < 1 := by
    rw [abs_lt]; constructor <;> linarith
  rw [← mul_sub, abs_mul, abs_of_pos hq'] at hd
  rw [lt_div_iff₀ hq']
  linarith

/-- **Aproximação de Dirichlet simultânea**: para `θ_i`, `i ∈ D`, e `q > 0`, existe `1 ≤ k ≤ q^{|D|}` com
`k·θ_i` a menos de `1/q` de um inteiro para todo `i`. -/
theorem dirichlet_simultaneo {ι : Type*} (D : Finset ι) (θ : ι → ℝ) {q : ℕ} (hq : 0 < q) :
    ∃ k : ℕ, 0 < k ∧ k ≤ q ^ D.card ∧ ∀ i ∈ D, ∃ j : ℤ, |(k : ℝ) * θ i - j| < 1 / q := by
  classical
  have hq' : (0 : ℝ) < q := by exact_mod_cast hq
  let f : ℕ → (D → Fin q) := fun k i =>
    ⟨⌊(q : ℝ) * Int.fract ((k : ℝ) * θ i)⌋₊, by
      have h1 : (q : ℝ) * Int.fract ((k : ℝ) * θ i) < q := by
        have := Int.fract_lt_one ((k : ℝ) * θ i)
        nlinarith
      exact (Nat.floor_lt (mul_nonneg hq'.le (Int.fract_nonneg _))).mpr h1⟩
  have hc : (Finset.univ : Finset (D → Fin q)).card < (Finset.range (q ^ D.card + 1)).card := by
    simp [Finset.card_univ, Fintype.card_fin]
  obtain ⟨a, ha, b, hb, hab, hfab⟩ :=
    Finset.exists_ne_map_eq_of_card_lt_of_maps_to hc (f := f) (fun x _ => Finset.mem_univ _)
  -- de `f a = f b` com `a < b`, o salto `b − a` serve
  have chave : ∀ a b : ℕ, a < b → b ≤ q ^ D.card → f a = f b →
      ∃ k : ℕ, 0 < k ∧ k ≤ q ^ D.card ∧ ∀ i ∈ D, ∃ j : ℤ, |(k : ℝ) * θ i - j| < 1 / q := by
    intro a b hlt hbq he
    refine ⟨b - a, Nat.sub_pos_of_lt hlt, le_trans (Nat.sub_le b a) hbq, fun i hi => ?_⟩
    have hfi := congrArg (fun g => (g ⟨i, hi⟩ : ℕ)) he
    simp only [f] at hfi
    have hcx := caixa hq hfi.symm
    refine ⟨⌊(b : ℝ) * θ i⌋ - ⌊(a : ℝ) * θ i⌋, ?_⟩
    have eb := Int.floor_add_fract ((b : ℝ) * θ i)
    have ea := Int.floor_add_fract ((a : ℝ) * θ i)
    rw [Nat.cast_sub hlt.le]
    push_cast
    have : ((b : ℝ) - a) * θ i - (⌊(b : ℝ) * θ i⌋ - ⌊(a : ℝ) * θ i⌋) =
        Int.fract ((b : ℝ) * θ i) - Int.fract ((a : ℝ) * θ i) := by linarith
    rw [this]
    exact hcx
  have ha' : a ≤ q ^ D.card := Nat.lt_succ_iff.mp (Finset.mem_range.mp ha)
  have hb' : b ≤ q ^ D.card := Nat.lt_succ_iff.mp (Finset.mem_range.mp hb)
  rcases lt_or_gt_of_ne hab with h | h
  · exact chave a b h hb' hfab
  · exact chave b a h ha' hfab.symm

/-- Perto de um múltiplo de `2π` (a menos de `π/3`), o cosseno passa de `½`. -/
theorem cos_ge_meio {t : ℝ} {j : ℤ} (h : |t - j * (2 * Real.pi)| < Real.pi / 3) :
    1 / 2 ≤ Real.cos t := by
  have e : Real.cos t = Real.cos |t - j * (2 * Real.pi)| := by
    rw [Real.cos_abs, Real.cos_sub_int_mul_two_pi]
  rw [e, ← Real.cos_pi_div_three]
  exact Real.cos_le_cos_of_nonneg_of_le_pi (abs_nonneg _) (by linarith [Real.pi_pos]) h.le

/-- `Re(zⁿ) = |z|ⁿ cos(n·arg z)`. -/
theorem re_pow_eq (z : ℂ) (n : ℕ) : (z ^ n).re = ‖z‖ ^ n * Real.cos (n * Complex.arg z) := by
  have h : z ^ n = ((‖z‖ ^ n : ℝ) : ℂ) * Complex.exp (((n * Complex.arg z : ℝ) : ℂ) * Complex.I) := by
    conv_lhs => rw [← Complex.norm_mul_exp_arg_mul_I z]
    rw [mul_pow, ← Complex.exp_nat_mul]
    push_cast
    ring_nf
  rw [h, Complex.re_ofReal_mul, Complex.exp_ofReal_mul_I_re]

/-- **Lei 2 (forma de potências).** Numa soma finita de potências, se algum termo tem `|z| > 1`, a parte
real sobe acima de qualquer `M` para `n` arbitrariamente grande. -/
theorem re_soma_pot_ilimitada {ι : Type*} (S : Finset ι) (z : ι → ℂ) (h : ∃ i ∈ S, 1 < ‖z i‖) :
    ∀ M : ℝ, ∀ N : ℕ, ∃ n ≥ N, M < (∑ i ∈ S, z i ^ n).re := by
  classical
  intro M N
  obtain ⟨i₁, hi₁, h₁⟩ := h
  obtain ⟨i₀, hi₀, hmax⟩ := Finset.exists_max_image S (fun i => ‖z i‖) ⟨i₁, hi₁⟩
  set r := ‖z i₀‖ with hr
  have hr1 : 1 < r := lt_of_lt_of_le h₁ (hmax i₁ hi₁)
  have hr0 : 0 < r := by linarith
  set D := S.filter (fun i => ‖z i‖ = r) with hD
  set O := S.filter (fun i => ¬ ‖z i‖ = r) with hO
  -- os termos menores, normalizados, somem
  have hOlim : Tendsto (fun n : ℕ => ∑ i ∈ O, (‖z i‖ / r) ^ n) atTop (𝓝 0) := by
    have hcada : ∀ i ∈ O, Tendsto (fun n : ℕ => (‖z i‖ / r) ^ n) atTop (𝓝 0) := by
      intro i hi
      rw [hO, Finset.mem_filter] at hi
      apply tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg (norm_nonneg _) hr0.le)
      rw [div_lt_one hr0]
      exact lt_of_le_of_ne (hmax i hi.1) hi.2
    simpa using tendsto_finsetSum O hcada
  obtain ⟨N₀, hN₀⟩ := Filter.eventually_atTop.mp
    (hOlim.eventually (gt_mem_nhds (by norm_num : (0 : ℝ) < 1 / 4)))
  obtain ⟨N₁, hN₁⟩ := Filter.eventually_atTop.mp
    ((tendsto_pow_atTop_atTop_of_one_lt hr1).eventually (eventually_gt_atTop (4 * M)))
  set m := max (max N N₀) (max N₁ 1) with hm
  have hm1 : 1 ≤ m := le_trans (le_max_right _ _) (le_max_right _ _)
  obtain ⟨k, hk0, -, hk⟩ := dirichlet_simultaneo D
    (fun i => (m : ℝ) * Complex.arg (z i) / (2 * Real.pi)) (by norm_num : 0 < 6)
  refine ⟨m * k, ?_, ?_⟩
  · calc N ≤ m := le_trans (le_max_left _ _) (le_max_left _ _)
      _ ≤ m * k := Nat.le_mul_of_pos_right m hk0
  set n := m * k with hn
  have hmn : m ≤ n := Nat.le_mul_of_pos_right m hk0
  have hnN₀ : N₀ ≤ n := le_trans (le_trans (le_max_right _ _) (le_max_left _ _)) hmn
  have hrn : r ^ m ≤ r ^ n := pow_le_pow_right₀ hr1.le hmn
  have hrm : 4 * M < r ^ m := hN₁ m (le_trans (le_max_left _ _) (le_max_right _ _))
  -- os dominantes: parte real ≥ rⁿ/2 cada
  have hDre : ∀ i ∈ D, r ^ n / 2 ≤ (z i ^ n).re := by
    intro i hi
    have hiD := hi
    rw [hD, Finset.mem_filter] at hiD
    obtain ⟨j, hj⟩ := hk i hi
    rw [re_pow_eq, hiD.2]
    have hpi := Real.pi_pos
    have hcos : 1 / 2 ≤ Real.cos (n * Complex.arg (z i)) := by
      apply cos_ge_meio (j := j)
      have e : (n : ℝ) * Complex.arg (z i) - j * (2 * Real.pi) =
          (2 * Real.pi) * ((k : ℝ) * ((m : ℝ) * Complex.arg (z i) / (2 * Real.pi)) - j) := by
        rw [hn]; push_cast; field_simp
      rw [e, abs_mul, abs_of_pos (by positivity)]
      calc 2 * Real.pi * |(k : ℝ) * ((m : ℝ) * Complex.arg (z i) / (2 * Real.pi)) - j|
          < 2 * Real.pi * (1 / (6 : ℕ)) := by
            apply mul_lt_mul_of_pos_left _ (by positivity)
            exact_mod_cast hj
        _ = Real.pi / 3 := by push_cast; ring
    have hrpos : 0 ≤ r ^ n := by positivity
    nlinarith
  have hDsum : r ^ n / 2 ≤ ∑ i ∈ D, (z i ^ n).re := by
    have hi₀D : i₀ ∈ D := by rw [hD, Finset.mem_filter]; exact ⟨hi₀, rfl⟩
    have hnn : ∀ i ∈ D, 0 ≤ (z i ^ n).re := fun i hi =>
      le_trans (by positivity) (hDre i hi)
    calc r ^ n / 2 ≤ (z i₀ ^ n).re := hDre i₀ hi₀D
      _ ≤ ∑ i ∈ D, (z i ^ n).re := Finset.single_le_sum hnn hi₀D
  -- os outros: |soma| ≤ rⁿ/4
  have hOsum : -(r ^ n / 4) ≤ ∑ i ∈ O, (z i ^ n).re := by
    have h1 : ∀ i ∈ O, -(r ^ n * (‖z i‖ / r) ^ n) ≤ (z i ^ n).re := by
      intro i _
      have e : r ^ n * (‖z i‖ / r) ^ n = ‖z i ^ n‖ := by
        rw [norm_pow, div_pow, mul_div_cancel₀ _ (pow_ne_zero n hr0.ne')]
      rw [e]
      exact neg_le_of_abs_le (Complex.abs_re_le_norm _)
    have h2 := Finset.sum_le_sum h1
    rw [Finset.sum_neg_distrib, ← Finset.mul_sum] at h2
    have h3 := hN₀ n hnN₀
    have hrpos : 0 ≤ r ^ n := by positivity
    nlinarith
  have hsplit : (∑ i ∈ S, z i ^ n).re = ∑ i ∈ D, (z i ^ n).re + ∑ i ∈ O, (z i ^ n).re := by
    rw [Complex.re_sum, hD, hO, Finset.sum_filter_add_sum_filter_not]
  rw [hsplit]
  linarith

/-- **Lei 2.** Numa família finita, um único ponto com `Re ρ < ½` leva `λₙ(S)` abaixo de qualquer `−M`. -/
theorem liS_ilimitado {S : Finset ℂ} (h0 : ∀ ρ ∈ S, ρ ≠ 0) (hfora : ∃ ρ ∈ S, ρ.re < 1 / 2) :
    ∀ M : ℝ, ∀ N : ℕ, ∃ n ≥ N, liS S n < -M := by
  intro M N
  obtain ⟨σ, hσ, hre⟩ := hfora
  obtain ⟨n, hn, hlt⟩ := re_soma_pot_ilimitada S w ⟨σ, hσ, (w_fora_iff (h0 σ hσ)).mpr hre⟩
    (M + S.card) N
  exact ⟨n, hn, by rw [liS_eq]; linarith⟩

/-- **Lei 3 — critério de Li finito.** -/
theorem liS_criterio {S : Finset ℂ} (h0 : ∀ ρ ∈ S, ρ ≠ 0) :
    (∀ n : ℕ, 0 ≤ liS S n) ↔ ∀ ρ ∈ S, 1 / 2 ≤ ρ.re := by
  constructor
  · intro h ρ hρ
    by_contra hlt
    push Not at hlt
    obtain ⟨n, -, hn⟩ := liS_ilimitado h0 ⟨ρ, hρ, hlt⟩ 0 0
    linarith [h n]
  · intro h n
    exact liS_nao_negativo (fun ρ hρ => ⟨h0 ρ hρ, h ρ hρ⟩) n

/-! ### Lei 4: RH em somas finitas -/

/-- Zero não trivial de ζ, exatamente como na `RiemannHypothesis` do Mathlib. -/
def NaoTrivial (s : ℂ) : Prop := riemannZeta s = 0 ∧ (¬∃ n : ℕ, s = -2 * (n + 1)) ∧ s ≠ 1

theorem ne_zero_of_naoTrivial {s : ℂ} (h : NaoTrivial s) : s ≠ 0 := by
  rintro rfl
  have := h.1
  rw [riemannZeta_zero] at this
  norm_num at this

/-- Os zeros não triviais no disco `‖s‖ ≤ T` são finitos (Mathlib). -/
theorem finito (T : ℝ) : {s : ℂ | NaoTrivial s ∧ ‖s‖ ≤ T}.Finite := by
  apply ((isCompact_closedBall (0 : ℂ) T).inter_riemannZetaZeros_finite).subset
  intro s hs
  refine ⟨?_, hs.1.1⟩
  simpa [Metric.mem_closedBall, dist_zero_right] using hs.2

/-- Os zeros não triviais com `‖ρ‖ ≤ T`. -/
noncomputable def zerosAte (T : ℝ) : Finset ℂ := (finito T).toFinset

theorem mem_zerosAte {T : ℝ} {s : ℂ} : s ∈ zerosAte T ↔ NaoTrivial s ∧ ‖s‖ ≤ T := by
  unfold zerosAte
  rw [Set.Finite.mem_toFinset]
  rfl

/-- `λₙ^{(T)}`: a soma de Li sobre os zeros não triviais com `‖ρ‖ ≤ T`. -/
noncomputable def liT (T : ℝ) (n : ℕ) : ℝ := liS (zerosAte T) n

/-- Se RH falha, existe um zero não trivial com `Re σ < ½` (o refletido `1 − s`, se preciso). -/
theorem existe_zero_esquerda (h : ¬RiemannHypothesis) : ∃ σ : ℂ, NaoTrivial σ ∧ σ.re < 1 / 2 := by
  simp only [RiemannHypothesis, not_forall] at h
  obtain ⟨s, hz, hnt, h1, hre⟩ := h
  rcases lt_or_gt_of_ne hre with hlt | hgt
  · exact ⟨s, ⟨hz, hnt, h1⟩, hlt⟩
  · have hs1 : s.re < 1 := by
      by_contra hge
      push Not at hge
      exact riemannZeta_ne_zero_of_one_le_re hge hz
    have hsn : ∀ n : ℕ, s ≠ -n := by
      intro n hn
      have := congrArg Complex.re hn
      simp at this
      have : (0 : ℝ) ≤ n := Nat.cast_nonneg n
      linarith
    refine ⟨1 - s, ⟨?_, ?_, ?_⟩, ?_⟩
    · rw [riemannZeta_one_sub hsn h1, hz, mul_zero]
    · rintro ⟨n, hn⟩
      have := congrArg Complex.re hn
      simp at this
      have : (0 : ℝ) ≤ n := Nat.cast_nonneg n
      linarith
    · intro h01
      have hs0 : s = 0 := by linear_combination -h01
      rw [hs0, riemannZeta_zero] at hz
      norm_num at hz
    · simp only [sub_re, one_re]
      linarith

/-- **Lei 4 (direção RH ⟹).** Sob RH, todas as truncagens são `≥ 0`. -/
theorem liT_nao_negativo (hRH : RiemannHypothesis) (T : ℝ) (n : ℕ) : 0 ≤ liT T n := by
  apply liS_nao_negativo
  intro ρ hρ
  rw [mem_zerosAte] at hρ
  obtain ⟨⟨hz, hnt, h1⟩, -⟩ := hρ
  exact ⟨ne_zero_of_naoTrivial ⟨hz, hnt, h1⟩, (hRH ρ hz hnt h1).ge⟩

/-- **Lei 4 (direção ⟸, forte).** Se RH falha, a partir da altura do zero fora, toda truncagem desce a `−∞`. -/
theorem liT_ilimitado (h : ¬RiemannHypothesis) :
    ∃ T₀ : ℝ, ∀ T ≥ T₀, ∀ M : ℝ, ∀ N : ℕ, ∃ n ≥ N, liT T n < -M := by
  obtain ⟨σ, hσ, hre⟩ := existe_zero_esquerda h
  refine ⟨‖σ‖, fun T hT => ?_⟩
  apply liS_ilimitado
  · intro ρ hρ
    exact ne_zero_of_naoTrivial (mem_zerosAte.mp hρ).1
  · exact ⟨σ, mem_zerosAte.mpr ⟨hσ, hT⟩, hre⟩

/-- Sob RH, as truncagens crescem com `T`: `λₙ^{(T)} ≤ λₙ^{(T')}` para `T ≤ T'`. -/
theorem liT_mono (hRH : RiemannHypothesis) {T T' : ℝ} (hT : T ≤ T') (n : ℕ) : liT T n ≤ liT T' n := by
  unfold liT liS
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro ρ hρ
    rw [mem_zerosAte] at hρ ⊢
    exact ⟨hρ.1, le_trans hρ.2 hT⟩
  · intro ρ hρ _
    rw [mem_zerosAte] at hρ
    obtain ⟨⟨hz, hnt, h1⟩, -⟩ := hρ
    exact re_um_sub_pow_nonneg
      ((w_le_one_iff (ne_zero_of_naoTrivial ⟨hz, hnt, h1⟩)).mpr (hRH ρ hz hnt h1).ge) n

/-- **Lei 4 — RH em somas finitas de Li.** -/
theorem rh_iff_liT : RiemannHypothesis ↔ ∀ T : ℝ, ∀ n : ℕ, 0 ≤ liT T n := by
  constructor
  · exact fun hRH T n => liT_nao_negativo hRH T n
  · intro h
    by_contra hRH
    obtain ⟨T₀, hT₀⟩ := liT_ilimitado hRH
    obtain ⟨n, -, hn⟩ := hT₀ T₀ le_rfl 0 0
    linarith [h T₀ n]

/-! ### Lei 5: o termo arquimediano sozinho é negativo no começo -/

/-- **Lei 5.** `(n/2)(log n − 1 + γ − log 2π) < 0` para `1 ≤ n ≤ 6`. -/
theorem principal_negativo {n : ℕ} (h1 : 1 ≤ n) (h6 : n ≤ 6) :
    (n / 2 : ℝ) * (Real.log n - 1 + Real.eulerMascheroniConstant - Real.log (2 * Real.pi)) < 0 := by
  have hn : (1 : ℝ) ≤ n := by exact_mod_cast h1
  have hn6 : (n : ℝ) ≤ 6 := by exact_mod_cast h6
  have hpi := Real.pi_gt_three
  have hlog : Real.log n < Real.log (2 * Real.pi) :=
    Real.log_lt_log (by linarith) (by linarith)
  have hg := Real.eulerMascheroniConstant_lt_two_thirds
  have hpos : (0 : ℝ) < n / 2 := by positivity
  have : Real.log n - 1 + Real.eulerMascheroniConstant - Real.log (2 * Real.pi) < 0 := by linarith
  exact mul_neg_of_pos_of_neg hpos this

/-! ### Lei 6: Davenport–Heilbronn -/

/-- **Lei 6 (taxa).** Bola certificada do zero de Davenport–Heilbronn `β + iγ` (Arb, Newton intervalar:
`β = 0,80851718245663738555 ± 3,4·10⁻²¹`, `γ = 85,699348485377592172 ± 7,1·10⁻²⁰`). O refletido
`σ = (1 − β) + iγ` tem `|w(σ)|² − 1 ∈ (84014·10⁻⁹; 84015·10⁻⁹)`: a parcela de Li dele cresce como
`e^{4,2·10⁻⁵ n}`. -/
theorem dh_taxa {β γ : ℝ} (hβ : |β - 80851718245663738555 / 10 ^ 20| ≤ 1 / 10 ^ 20)
    (hγ : |γ - 85699348485377592172 / 10 ^ 18| ≤ 1 / 10 ^ 18) :
    (84014 / 10 ^ 9 : ℝ) < ‖w ⟨1 - β, γ⟩‖ ^ 2 - 1 ∧ ‖w ⟨1 - β, γ⟩‖ ^ 2 - 1 < 84015 / 10 ^ 9 := by
  rw [abs_le] at hβ hγ
  obtain ⟨b1, b2⟩ := hβ
  obtain ⟨g1, g2⟩ := hγ
  have hne : (⟨1 - β, γ⟩ : ℂ) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
    norm_num at g1
    linarith
  rw [norm_w_sq_sub_one hne]
  simp only
  have hγ0 : 0 < γ := by norm_num at g1; linarith
  have hden : 0 < (1 - β) ^ 2 + γ ^ 2 := by nlinarith [sq_nonneg (1 - β), mul_pos hγ0 hγ0]
  constructor
  · rw [lt_div_iff₀ hden]
    nlinarith
  · rw [div_lt_iff₀ hden]
    nlinarith

/-- **Lei 6 (obstrução).** Toda soma de Li finita que contém o refletido `σ` do zero de Davenport–Heilbronn
desce abaixo de qualquer `−M`. `f` tem a mesma equação funcional, o mesmo `Γ((s+1)/2)` e a mesma potência de
`π` que `L(s, χ mod 5)`; logo nenhuma prova de `λₙ ≥ 0` que use só o fator arquimediano pode funcionar. -/
theorem dh_obstrucao {β γ : ℝ} (hβ : |β - 80851718245663738555 / 10 ^ 20| ≤ 1 / 10 ^ 20)
    {S : Finset ℂ} (hσ : (⟨1 - β, γ⟩ : ℂ) ∈ S) (h0 : ∀ ρ ∈ S, ρ ≠ 0) :
    ∀ M : ℝ, ∀ N : ℕ, ∃ n ≥ N, liS S n < -M := by
  apply liS_ilimitado h0
  refine ⟨⟨1 - β, γ⟩, hσ, ?_⟩
  rw [abs_le] at hβ
  show 1 - β < 1 / 2
  linarith [hβ.1]

end ATK.LiTrunc

#print axioms ATK.LiTrunc.w_eq
#print axioms ATK.LiTrunc.normSq_pos_re_im
#print axioms ATK.LiTrunc.norm_w_sq
#print axioms ATK.LiTrunc.norm_w_sq_sub_one
#print axioms ATK.LiTrunc.w_fora_iff
#print axioms ATK.LiTrunc.w_le_one_iff
#print axioms ATK.LiTrunc.re_um_sub_pow_nonneg
#print axioms ATK.LiTrunc.liS_eq
#print axioms ATK.LiTrunc.liS_nao_negativo
#print axioms ATK.LiTrunc.caixa
#print axioms ATK.LiTrunc.dirichlet_simultaneo
#print axioms ATK.LiTrunc.cos_ge_meio
#print axioms ATK.LiTrunc.re_pow_eq
#print axioms ATK.LiTrunc.re_soma_pot_ilimitada
#print axioms ATK.LiTrunc.liS_ilimitado
#print axioms ATK.LiTrunc.liS_criterio
#print axioms ATK.LiTrunc.ne_zero_of_naoTrivial
#print axioms ATK.LiTrunc.finito
#print axioms ATK.LiTrunc.mem_zerosAte
#print axioms ATK.LiTrunc.existe_zero_esquerda
#print axioms ATK.LiTrunc.liT_nao_negativo
#print axioms ATK.LiTrunc.liT_ilimitado
#print axioms ATK.LiTrunc.liT_mono
#print axioms ATK.LiTrunc.rh_iff_liT
#print axioms ATK.LiTrunc.principal_negativo
#print axioms ATK.LiTrunc.dh_taxa
#print axioms ATK.LiTrunc.dh_obstrucao
