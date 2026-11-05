import ATK.OSTransferencia
import ATK.FracoesMalha

/-!
# ATK — O "gás de primos": `ζ(σ)` como traço de `e^{−σH}` com lacuna `log 2` (rodada 106)

Ponte RH ↔ Yang–Mills no nível que é teorema. Os modos `n = 1, …, N + 1` com energias `log n` formam dados
de Osterwalder–Schrader (`primons N`): forma `B(f, g) = Σ conj fᵢ gᵢ` (positiva por reflexão), translações
`S(t) = diag(n^{−t}) = e^{−tH}`, vácuo `Ω = e₁` (energia `log 1 = 0`).

* `primons`: os axiomas de `ATK.OSTransferencia.DadosOS` valem.
* `conexa_le`, **`lacuna_primons`**: a correlação conexa decai como `e^{−(log 2)t}` e, pela reconstrução
  OS (`lacuna_OS`, rodada 104), `‖P(t)w‖ ≤ e^{−(log 2)t}‖w‖` para `w ⊥ Ω`: **a massa é `log 2`**.
* **`lacuna_atingida`**: o modo `n = 2` atinge a cota; `log 2` é a massa exata, não só uma cota.
* `diagonal`, **`traco_tende_zeta`**: `B(eₙ, S(σ)eₙ) = n^{−σ}` e o traço `Σ_{n ≤ N+1} n^{−σ}` tende a `ζ(σ)`
  (`σ > 1`): **`ζ(σ) = Tr e^{−σH}`**.
* **`traco_conexo_le`**: o traço conexo (sem o vácuo) é `≤ 2^{2−σ}(π²/6 − 1)` para `σ ≥ 2`, uniforme em `N`:
  é a cauda `|ζ − 1|` da rodada 105 vista como lacuna.

O que **não** é: um teorema sobre Yang–Mills em ℝ⁴. O gás de primos é um sistema de modos livres; a
lacuna `log 2` é a distância entre `log 1` e `log 2`. A ponte mostra que a forma "cauda `e^{−mt}` ⟺ lacuna `m`"
é a mesma lei nos dois lados. Classificação: **ferramenta/consequência**. RH e YM continuam `OPEN_MATH`.
-/

open scoped ComplexConjugate InnerProductSpace
open Finset Filter Topology

namespace ATK.Fracoes.Primons

open ATK.OSTransferencia

/-! ## 1. Os pesos `(i + 1)^{−t}` -/

/-- Peso do modo `i` (número `n = i + 1`, energia `log n`): `n^{−t} = e^{−t log n}`. -/
noncomputable def peso (t : ℝ) (i : ℕ) : ℝ := ((i : ℝ) + 1) ^ (-t)

theorem peso_pos (t : ℝ) (i : ℕ) : 0 < peso t i := Real.rpow_pos_of_pos (by positivity) _

theorem peso_zero (i : ℕ) : peso 0 i = 1 := by simp [peso]

theorem peso_add (s t : ℝ) (i : ℕ) : peso (s + t) i = peso s i * peso t i := by
  unfold peso
  rw [neg_add, Real.rpow_add (by positivity)]

theorem peso_vacuo (t : ℝ) : peso t 0 = 1 := by simp [peso]

theorem peso_le_um {t : ℝ} (ht : 0 ≤ t) (i : ℕ) : peso t i ≤ 1 :=
  Real.rpow_le_one_of_one_le_of_nonpos (by linarith [(i.cast_nonneg : (0 : ℝ) ≤ i)]) (by linarith)

/-- Fora do vácuo, `n^{−t} ≤ 2^{−t} = e^{−(log 2)t}`. -/
theorem peso_le_lacuna {t : ℝ} (ht : 0 ≤ t) {i : ℕ} (hi : 1 ≤ i) :
    peso t i ≤ Real.exp (-(Real.log 2 * t)) := by
  have hi' : (1 : ℝ) ≤ i := by exact_mod_cast hi
  have h : peso t i ≤ (2 : ℝ) ^ (-t) :=
    Real.rpow_le_rpow_of_nonpos (by norm_num) (by linarith) (by linarith)
  rw [Real.rpow_def_of_pos (by norm_num)] at h
  rw [show -(Real.log 2 * t) = Real.log 2 * -t by ring]
  exact h

theorem peso_um (t : ℝ) : peso t 1 = Real.exp (-(Real.log 2 * t)) := by
  unfold peso
  rw [show ((1 : ℕ) : ℝ) + 1 = 2 by norm_num, Real.rpow_def_of_pos (by norm_num)]
  ring_nf

/-! ## 2. Os dados de Osterwalder–Schrader -/

/-- `S(t) = diag(n^{−t})`. -/
noncomputable def Sp (N : ℕ) (t : ℝ) : (Fin (N + 1) → ℂ) →ₗ[ℂ] (Fin (N + 1) → ℂ) where
  toFun f := fun i => (peso t i : ℂ) * f i
  map_add' f g := by funext i; simp only [Pi.add_apply]; ring
  map_smul' c f := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem Sp_apply (N : ℕ) (t : ℝ) (f : Fin (N + 1) → ℂ) (i : Fin (N + 1)) :
    Sp N t f i = (peso t i : ℂ) * f i := rfl

theorem re_conj_mul_self (z : ℂ) : 0 ≤ (conj z * z).re := by
  simp only [Complex.mul_re, Complex.conj_re, Complex.conj_im]
  nlinarith [sq_nonneg z.re, sq_nonneg z.im]

/-- O vácuo `e₁` (o número `n = 1`, energia 0). -/
def vacuo (N : ℕ) : Fin (N + 1) → ℂ := fun i => if (i : ℕ) = 0 then 1 else 0

theorem soma_vacuo_dir (N : ℕ) (f : Fin (N + 1) → ℂ) : ∑ i, conj (vacuo N i) * f i = f 0 := by
  rw [Fin.sum_univ_succ]
  simp [vacuo, Fin.val_succ]

theorem soma_vacuo_esq (N : ℕ) (f : Fin (N + 1) → ℂ) : ∑ i, conj (f i) * vacuo N i = conj (f 0) := by
  rw [Fin.sum_univ_succ]
  simp [vacuo, Fin.val_succ]

/-- **O gás de primos** com `N + 1` modos. -/
noncomputable def primons (N : ℕ) : DadosOS (Fin (N + 1) → ℂ) where
  B f g := ∑ i, conj (f i) * g i
  conj_symm f g := by
    simp only [map_sum, map_mul, Complex.conj_conj]
    exact sum_congr rfl fun i _ => mul_comm _ _
  pos f := by
    rw [Complex.re_sum]
    exact sum_nonneg fun i _ => re_conj_mul_self (f i)
  add_left f f' g := by simp only [Pi.add_apply, map_add, add_mul, sum_add_distrib]
  smul_left c f g := by simp only [Pi.smul_apply, smul_eq_mul, map_mul, mul_sum, mul_assoc]
  S := Sp N
  S_zero := by
    refine LinearMap.ext fun f => funext fun i => ?_
    simp [Sp_apply, peso_zero]
  S_add s t _ _ := by
    refine LinearMap.ext fun f => funext fun i => ?_
    simp only [LinearMap.comp_apply, Sp_apply, peso_add]
    push_cast
    ring
  S_symm t _ f g := by
    simp only [Sp_apply, map_mul, Complex.conj_ofReal]
    exact sum_congr rfl fun i _ => by ring
  S_bdd f := by
    refine ⟨∑ i, (conj (f i) * f i).re, 0, fun t ht => ?_⟩
    rw [pow_zero, mul_one, Complex.re_sum]
    refine sum_le_sum fun i _ => ?_
    simp only [Sp_apply, map_mul, Complex.conj_ofReal]
    have e : (peso t i : ℂ) * conj (f i) * ((peso t i : ℂ) * f i) =
        ((peso t i ^ 2 : ℝ) : ℂ) * (conj (f i) * f i) := by push_cast; ring
    rw [e, Complex.re_ofReal_mul]
    have h1 := peso_le_um ht i
    have h0 := (peso_pos t i).le
    have hz := re_conj_mul_self (f i)
    have : peso t i ^ 2 ≤ 1 := by nlinarith
    nlinarith
  Ω := vacuo N
  S_Ω t _ := by
    funext i
    simp only [Sp_apply, vacuo]
    split_ifs with h
    · have : peso t i = 1 := by rw [h]; exact peso_vacuo t
      rw [this]; simp
    · simp
  B_ΩΩ := by
    show ∑ i, conj (vacuo N i) * vacuo N i = 1
    rw [soma_vacuo_dir]
    simp [vacuo]

theorem B_def (N : ℕ) (f g : Fin (N + 1) → ℂ) : (primons N).B f g = ∑ i, conj (f i) * g i := rfl

/-! ## 3. A lacuna `log 2` -/

/-- A correlação conexa é a soma sobre os modos excitados `n ≥ 2`. -/
theorem conexa (N : ℕ) (f : Fin (N + 1) → ℂ) (t : ℝ) :
    (primons N).B f ((primons N).S t f) - (primons N).B f (primons N).Ω * (primons N).B (primons N).Ω f =
      ∑ j : Fin N, (peso t (j + 1) : ℂ) * (conj (f j.succ) * f j.succ) := by
  show ∑ i, conj (f i) * Sp N t f i - (∑ i, conj (f i) * vacuo N i) * (∑ i, conj (vacuo N i) * f i) = _
  rw [soma_vacuo_dir, soma_vacuo_esq, Fin.sum_univ_succ]
  simp only [Sp_apply, Fin.val_zero, peso_vacuo, Complex.ofReal_one, one_mul, Fin.val_succ]
  rw [add_sub_cancel_left]
  exact sum_congr rfl fun j _ => by ring

theorem conexa_le (N : ℕ) (f : Fin (N + 1) → ℂ) : ∃ C, ∀ t, 0 ≤ t →
    ‖(primons N).B f ((primons N).S t f) - (primons N).B f (primons N).Ω * (primons N).B (primons N).Ω f‖ ≤
      C * Real.exp (-(Real.log 2 * t)) := by
  refine ⟨∑ j : Fin N, ‖conj (f j.succ) * f j.succ‖, fun t ht => ?_⟩
  rw [conexa, sum_mul]
  refine (norm_sum_le _ _).trans (sum_le_sum fun j _ => ?_)
  rw [norm_mul, Complex.norm_real, Real.norm_of_nonneg (peso_pos _ _).le, mul_comm]
  exact mul_le_mul_of_nonneg_left (peso_le_lacuna ht (by omega)) (norm_nonneg _)

/-- **Lacuna `log 2`**: `‖P(t)w‖ ≤ e^{−(log 2)t}‖w‖` para todo `w ⊥ Ω` (reconstrução OS). -/
theorem lacuna_primons (N : ℕ) (w : (primons N).Hil) (hw : ⟪(primons N).ι (primons N).Ω, w⟫_ℂ = 0)
    (t : ℝ) (ht : 0 ≤ t) : ‖(primons N).P t w‖ ≤ Real.exp (-(Real.log 2 * t)) * ‖w‖ :=
  (primons N).lacuna_OS (conexa_le N) w hw t ht

/-- O modo `n = 2`. -/
def modo2 (N : ℕ) : Fin (N + 2) → ℂ := fun i => if (i : ℕ) = 1 then 1 else 0

theorem norm_ι_sq (N : ℕ) (g : Fin (N + 1) → ℂ) :
    ‖(primons N).ι g‖ ^ 2 = (∑ i, conj (g i) * g i).re :=
  (norm_sq_eq_re_inner (𝕜 := ℂ) ((primons N).ι g)).trans (by rw [DadosOS.inner_ι]; rfl)

/-- **A cota é atingida pelo modo `n = 2`**: `log 2` é a massa exata. -/
theorem lacuna_atingida (N : ℕ) (t : ℝ) (ht : 0 ≤ t) :
    ⟪(primons (N + 1)).ι (primons (N + 1)).Ω, (primons (N + 1)).ι (modo2 N)⟫_ℂ = 0 ∧
      (primons (N + 1)).ι (modo2 N) ≠ 0 ∧
      ‖(primons (N + 1)).P t ((primons (N + 1)).ι (modo2 N))‖ =
        Real.exp (-(Real.log 2 * t)) * ‖(primons (N + 1)).ι (modo2 N)‖ := by
  set D := primons (N + 1) with hD
  have s1 : ∑ i, conj (modo2 N i) * modo2 N i = 1 := by
    rw [Fin.sum_univ_succ, Fin.sum_univ_succ]
    simp [modo2, Fin.val_succ]
  have hn2 : ‖D.ι (modo2 N)‖ ^ 2 = 1 := by rw [hD, norm_ι_sq, s1]; simp
  have hn : ‖D.ι (modo2 N)‖ = 1 := by
    have h0 := norm_nonneg (D.ι (modo2 N))
    nlinarith [sq_nonneg (‖D.ι (modo2 N)‖ - 1)]
  refine ⟨?_, ?_, ?_⟩
  · rw [DadosOS.inner_ι]
    show ∑ i, conj (vacuo (N + 1) i) * modo2 N i = 0
    rw [soma_vacuo_dir]
    simp [modo2]
  · intro h0
    rw [h0, norm_zero] at hn
    exact zero_ne_one hn
  · rw [DadosOS.P_ι D ht, hn, mul_one]
    have hS : D.S t (modo2 N) = ((peso t 1 : ℝ) : ℂ) • modo2 N := by
      funext i
      show Sp (N + 1) t (modo2 N) i = _
      rw [Sp_apply]
      simp only [modo2, Pi.smul_apply, smul_eq_mul]
      split_ifs with h
      · rw [h]
      · simp
    have hsum : ∑ i, conj ((((peso t 1 : ℝ) : ℂ) • modo2 N) i) * ((((peso t 1 : ℝ) : ℂ) • modo2 N) i) =
        ((peso t 1 : ℝ) : ℂ) * ((peso t 1 : ℝ) : ℂ) * ∑ i, conj (modo2 N i) * modo2 N i := by
      simp only [Pi.smul_apply, smul_eq_mul, map_mul, Complex.conj_ofReal, mul_sum]
      exact sum_congr rfl fun i _ => by ring
    have hsq : ‖D.ι (D.S t (modo2 N))‖ ^ 2 = Real.exp (-(Real.log 2 * t)) ^ 2 := by
      rw [hS, hD, norm_ι_sq, hsum, s1, mul_one, ← Complex.ofReal_mul, Complex.ofReal_re, peso_um, sq]
    exact (pow_left_inj₀ (norm_nonneg _) (Real.exp_pos _).le two_ne_zero).mp hsq

/-! ## 4. O traço: `ζ(σ) = Tr e^{−σH}` -/

/-- `B(eₙ, S(σ)eₙ) = n^{−σ}`. -/
theorem diagonal (N : ℕ) (σ : ℝ) (i : Fin (N + 1)) :
    (primons N).B (Pi.single i 1) ((primons N).S σ (Pi.single i 1)) = (peso σ i : ℂ) := by
  show ∑ j, conj (Pi.single (M := fun _ => ℂ) i 1 j) * Sp N σ (Pi.single i 1) j = _
  rw [sum_eq_single i]
  · simp [Sp_apply]
  · intro j _ hj
    simp [hj]
  · intro h
    exact absurd (mem_univ i) h

/-- **O traço tende a `ζ(σ)`**: `Σ_{n ≤ N+1} n^{−σ} → ζ(σ)` para `σ > 1`. -/
theorem traco_tende_zeta {σ : ℝ} (hσ : 1 < σ) :
    Tendsto (fun N : ℕ => ((∑ i ∈ range (N + 1), peso σ i : ℝ) : ℂ)) atTop (𝓝 (riemannZeta σ)) := by
  have hre : 1 < (σ : ℂ).re := by rw [Complex.ofReal_re]; exact hσ
  have hsum : Summable (fun n : ℕ => 1 / ((n : ℂ) + 1) ^ (σ : ℂ)) := by
    have := (Complex.summable_one_div_nat_cpow (p := (σ : ℂ))).mpr hre
    exact (summable_nat_add_iff 1).mpr this |>.congr fun n => by push_cast; ring_nf
  have hterm : ∀ n : ℕ, 1 / ((n : ℂ) + 1) ^ (σ : ℂ) = ((peso σ n : ℝ) : ℂ) := by
    intro n
    unfold peso
    rw [Real.rpow_neg (by positivity), Complex.ofReal_inv, Complex.ofReal_cpow (by positivity),
      one_div]
    push_cast
    ring_nf
  rw [zeta_eq_tsum_one_div_nat_add_one_cpow hre]
  have h := hsum.hasSum.tendsto_sum_nat
  have h2 := h.comp (tendsto_add_atTop_nat 1)
  refine h2.congr fun N => ?_
  simp only [Function.comp_apply, Complex.ofReal_sum, hterm]

/-- Termo do traço conexo: `(n + 2)^{−σ} ≤ 2^{2−σ}/(n + 2)²` para `σ ≥ 2`. -/
theorem termo_le {σ : ℝ} (hσ : 2 ≤ σ) (n : ℕ) :
    peso σ (n + 1) ≤ (2 : ℝ) ^ (2 - σ) * (1 / ((n : ℝ) + 2) ^ 2) := by
  unfold peso
  have hx : (2 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) + 1 := by push_cast; linarith [(n.cast_nonneg : (0 : ℝ) ≤ n)]
  have hxpos : (0 : ℝ) < ((n + 1 : ℕ) : ℝ) + 1 := by linarith
  have e2 : ((n : ℝ) + 2) = ((n + 1 : ℕ) : ℝ) + 1 := by push_cast; ring
  rw [e2]
  set x := ((n + 1 : ℕ) : ℝ) + 1 with hxdef
  have hsplit : x ^ (-σ) = x ^ (-(2 : ℝ)) * x ^ (-(σ - 2)) := by
    rw [← Real.rpow_add hxpos]; ring_nf
  have hmono : x ^ (-(σ - 2)) ≤ (2 : ℝ) ^ (-(σ - 2)) :=
    Real.rpow_le_rpow_of_nonpos (by norm_num) hx (by linarith)
  have hneg : (2 : ℝ) ^ (2 - σ) = (2 : ℝ) ^ (-(σ - 2)) := by ring_nf
  have hx2 : x ^ (-(2 : ℝ)) = 1 / x ^ 2 := by
    rw [Real.rpow_neg hxpos.le, Real.rpow_two, one_div]
  rw [hsplit, hneg, hx2]
  have : 0 ≤ 1 / x ^ 2 := by positivity
  nlinarith [mul_le_mul_of_nonneg_left hmono this]

/-- **O traço conexo é `≤ 2^{2−σ}(π²/6 − 1)`**, uniformemente em `N` (`σ ≥ 2`). -/
theorem traco_conexo_le {σ : ℝ} (hσ : 2 ≤ σ) (N : ℕ) :
    ∑ n ∈ range N, peso σ (n + 1) ≤ (2 : ℝ) ^ (2 - σ) * (Real.pi ^ 2 / 6 - 1) := by
  have hs := (ATK.Fracoes.Malha.hasSum_inv_sq_desde_dois).mul_left ((2 : ℝ) ^ (2 - σ))
  calc ∑ n ∈ range N, peso σ (n + 1)
      ≤ ∑ n ∈ range N, (2 : ℝ) ^ (2 - σ) * (1 / ((n : ℝ) + 2) ^ 2) := sum_le_sum fun n _ => termo_le hσ n
    _ ≤ (2 : ℝ) ^ (2 - σ) * (Real.pi ^ 2 / 6 - 1) :=
        sum_le_hasSum (range N) (fun n _ => by positivity) hs

end ATK.Fracoes.Primons

#print axioms ATK.Fracoes.Primons.peso_pos
#print axioms ATK.Fracoes.Primons.peso_zero
#print axioms ATK.Fracoes.Primons.peso_add
#print axioms ATK.Fracoes.Primons.peso_vacuo
#print axioms ATK.Fracoes.Primons.peso_le_um
#print axioms ATK.Fracoes.Primons.peso_le_lacuna
#print axioms ATK.Fracoes.Primons.peso_um
#print axioms ATK.Fracoes.Primons.Sp_apply
#print axioms ATK.Fracoes.Primons.re_conj_mul_self
#print axioms ATK.Fracoes.Primons.soma_vacuo_dir
#print axioms ATK.Fracoes.Primons.soma_vacuo_esq
#print axioms ATK.Fracoes.Primons.B_def
#print axioms ATK.Fracoes.Primons.conexa
#print axioms ATK.Fracoes.Primons.conexa_le
#print axioms ATK.Fracoes.Primons.lacuna_primons
#print axioms ATK.Fracoes.Primons.norm_ι_sq
#print axioms ATK.Fracoes.Primons.lacuna_atingida
#print axioms ATK.Fracoes.Primons.diagonal
#print axioms ATK.Fracoes.Primons.traco_tende_zeta
#print axioms ATK.Fracoes.Primons.termo_le
#print axioms ATK.Fracoes.Primons.traco_conexo_le
