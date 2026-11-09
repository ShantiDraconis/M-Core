import Mathlib.NumberTheory.LSeries.Dirichlet
import Mathlib.NumberTheory.LSeries.Nonvanishing
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.Analysis.Complex.RemovableSingularity
import Mathlib.Analysis.Convex.PathConnected

/-!
# ATK — O gás de primos fermiônico: `1/ζ` como traço e o critério de continuação (rodada 107)

A rodada 106 escreveu `ζ(σ) = Tr e^{−σH}` (o gás de primos bosônico, `ATK.Fracoes.Primons`). Aqui entra o
gás **fermiônico**: o mesmo espaço com o sinal `(−1)^F = μ(n)` (cada primo é um férmion; `n` com primo repetido
não existe).

* `indice_witten`: `Σ_{d ∣ n} μ(d) = [n = 1]` — o índice de Witten do gás: só o vácuo sobrevive.
* `traco_fermionico`: `Σ μ(n) n^{−s} = 1/ζ(s)` em `Re s > 1` (como soma convergente).
* **`semZeros_iff_continuaAte`**: para todo `θ`, `ζ` não tem zeros em `Re s > θ` **se e só se** a função de
  partição fermiônica `1/ζ` tem continuação holomorfa a `Re s > θ` (`ContinuaAte θ`). A ida usa a
  singularidade removível em `s = 1` (o polo de `ζ` vira zero de `1/ζ`); a volta usa o princípio de identidade
  no semiplano superior convexo, a simetria `ζ(s̄) = conj ζ(s)` e a continuidade na reta real.
* `continuaAte_iff_traco`: a mesma coisa dita com o traço: existe `F` holomorfa em `Re s > θ` igual a
  `Σ μ(n) n^{−s}` em `Re s > 1`.

Com `θ = ½` isto é uma reformulação de RH (`ATK.FracoesFermionsRH`). Nada aqui prova a continuação: a série
`Σ μ(n) n^{−s}` só converge absolutamente em `Re s > 1`, e levar a convergência até `Re s > ½` é RH.
Classificação: **reformulação**. RH continua `OPEN_MATH`.
-/

open Complex Filter Topology Set
open scoped ComplexConjugate LSeries.notation ArithmeticFunction.Moebius

namespace ATK.Fracoes.Fermions

/-! ## 1. O índice de Witten e o traço fermiônico -/

/-- **Índice de Witten**: `Σ_{d ∣ n} μ(d) = 1` se `n = 1` e `0` caso contrário. -/
theorem indice_witten (n : ℕ) :
    ∑ d ∈ n.divisors, ArithmeticFunction.moebius d = if n = 1 then 1 else 0 := by
  rw [← ArithmeticFunction.coe_mul_zeta_apply, ArithmeticFunction.moebius_mul_coe_zeta,
    ArithmeticFunction.one_apply]

/-- **Traço fermiônico**: `L(μ, s) = 1/ζ(s)` em `Re s > 1`. -/
theorem traco_fermionico_eq {s : ℂ} (hs : 1 < s.re) : LSeries ↗μ s = (riemannZeta s)⁻¹ := by
  have h := ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius hs
  rw [ArithmeticFunction.LSeries_zeta_eq_riemannZeta hs] at h
  exact eq_inv_of_mul_eq_one_right h

/-- O traço fermiônico como soma convergente: `Σ μ(n) n^{−s} = 1/ζ(s)` em `Re s > 1`. -/
theorem traco_fermionico {s : ℂ} (hs : 1 < s.re) : LSeriesHasSum ↗μ s (riemannZeta s)⁻¹ := by
  rw [← traco_fermionico_eq hs]
  exact (ArithmeticFunction.LSeriesSummable_moebius_iff.mpr hs).LSeriesHasSum

/-! ## 2. O critério -/

/-- `ζ` sem zeros em `Re s > θ`. -/
def SemZeros (θ : ℝ) : Prop := ∀ s : ℂ, θ < s.re → riemannZeta s ≠ 0

/-- A função de partição fermiônica `1/ζ` continua holomorfa até `Re s > θ`. -/
def ContinuaAte (θ : ℝ) : Prop :=
  ∃ F : ℂ → ℂ, DifferentiableOn ℂ F {s | θ < s.re} ∧ ∀ s : ℂ, 1 < s.re → F s * riemannZeta s = 1

/-- `1/ζ(s) → 0` quando `s → 1` (o polo vira zero). -/
theorem inv_zeta_tende_zero : Tendsto (fun s => (riemannZeta s)⁻¹) (𝓝[≠] 1) (𝓝 0) := by
  have h1 : Tendsto (fun s : ℂ => s - 1) (𝓝[≠] 1) (𝓝 0) := by
    have := ((tendsto_id (x := 𝓝 (1 : ℂ))).sub_const (1 : ℂ)).mono_left
      (nhdsWithin_le_nhds (s := {(1 : ℂ)}ᶜ))
    simpa using this
  have h2 := riemannZeta_residue_one.inv₀ one_ne_zero
  have h3 := h1.mul h2
  rw [zero_mul] at h3
  refine h3.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with s hs
  have hs1 : s - 1 ≠ 0 := sub_ne_zero.mpr hs
  rw [mul_inv, ← mul_assoc, mul_inv_cancel₀ hs1, one_mul]

/-- A continuação explícita: `1/ζ` com o valor `0` em `s = 1`. -/
noncomputable def inversa : ℂ → ℂ := Function.update (fun s => (riemannZeta s)⁻¹) 1 0

theorem inversa_de_ne {s : ℂ} (hs : s ≠ 1) : inversa s = (riemannZeta s)⁻¹ :=
  Function.update_of_ne hs _ _

/-- **Ida**: sem zeros em `Re s > θ` ⇒ `1/ζ` continua até `Re s > θ`. -/
theorem continuaAte_of_semZeros {θ : ℝ} (h : SemZeros θ) : ContinuaAte θ := by
  have hopen : IsOpen {s : ℂ | θ < s.re} := isOpen_lt continuous_const continuous_re
  have hdiff : ∀ z : ℂ, θ < z.re → z ≠ 1 → DifferentiableAt ℂ inversa z := by
    intro z hz hz1
    have hd : DifferentiableAt ℂ (fun s => (riemannZeta s)⁻¹) z :=
      (differentiableAt_riemannZeta hz1).inv (h z hz)
    refine hd.congr_of_eventuallyEq ?_
    filter_upwards [isOpen_ne.mem_nhds hz1] with w hw
    exact inversa_de_ne hw
  refine ⟨inversa, fun z hz => ?_, fun s hs => ?_⟩
  · refine DifferentiableAt.differentiableWithinAt ?_
    rcases eq_or_ne z 1 with rfl | hz1
    · have hc : ContinuousAt inversa 1 := by
        unfold inversa
        rw [continuousAt_update_same]
        exact inv_zeta_tende_zero
      have hd : ∀ᶠ w in 𝓝[≠] (1 : ℂ), DifferentiableAt ℂ inversa w := by
        filter_upwards [self_mem_nhdsWithin, nhdsWithin_le_nhds (hopen.mem_nhds hz)] with w hw hwθ
        exact hdiff w hwθ hw
      exact (Complex.analyticAt_of_differentiable_on_punctured_nhds_of_continuousAt hd hc).differentiableAt
    · exact hdiff z hz hz1
  · have hs1 : s ≠ 1 := by
      rintro rfl
      simp at hs
    rw [inversa_de_ne hs1]
    exact inv_mul_cancel₀ (riemannZeta_ne_zero_of_one_le_re hs.le)

/-- O semiplano superior `{Re s > θ, Im s > 0}`. -/
def U (θ : ℝ) : Set ℂ := {s | θ < s.re ∧ 0 < s.im}

theorem U_aberto (θ : ℝ) : IsOpen (U θ) :=
  (isOpen_lt continuous_const continuous_re).inter (isOpen_lt continuous_const continuous_im)

theorem U_convexo (θ : ℝ) : Convex ℝ (U θ) := by
  have h1 : Convex ℝ {s : ℂ | θ < s.re} := convex_halfSpace_re_gt θ
  have h2 : Convex ℝ {s : ℂ | 0 < s.im} := convex_halfSpace_im_gt 0
  exact h1.inter h2

/-- **Chave**: se `F·ζ = 1` em `Re s > 1` e `F` é holomorfa em `Re s > θ`, então `F·ζ = 1` em todo ponto
`s ≠ 1` com `Re s > θ` e `Im s ≥ 0`. -/
theorem chave {θ : ℝ} {F : ℂ → ℂ} (hF : DifferentiableOn ℂ F {s | θ < s.re})
    (h1 : ∀ s : ℂ, 1 < s.re → F s * riemannZeta s = 1) {s : ℂ} (hs : θ < s.re) (him : 0 ≤ s.im)
    (hs1 : s ≠ 1) : F s * riemannZeta s = 1 := by
  have hopen : IsOpen {s : ℂ | θ < s.re} := isOpen_lt continuous_const continuous_re
  set G : ℂ → ℂ := fun z => F z * riemannZeta z - 1 with hG
  -- G holomorfa no semiplano superior
  have hGd : DifferentiableOn ℂ G (U θ) := by
    intro z hz
    have hz1 : z ≠ 1 := by
      rintro rfl
      simp [U] at hz
    have hFz : DifferentiableAt ℂ F z := (hF z hz.1).differentiableAt (hopen.mem_nhds hz.1)
    exact ((hFz.mul (differentiableAt_riemannZeta hz1)).sub_const 1).differentiableWithinAt
  have hGa : AnalyticOnNhd ℂ G (U θ) := hGd.analyticOnNhd (U_aberto θ)
  -- um ponto de U com Re > 1
  set z₀ : ℂ := ((max θ 1 + 1 : ℝ) : ℂ) + I with hz₀
  have hz₀re : z₀.re = max θ 1 + 1 := by simp [hz₀]
  have hz₀im : z₀.im = 1 := by simp [hz₀]
  have hz₀U : z₀ ∈ U θ := ⟨by rw [hz₀re]; linarith [le_max_left θ 1], by rw [hz₀im]; norm_num⟩
  have hev : G =ᶠ[𝓝 z₀] 0 := by
    have hmem : {z : ℂ | 1 < z.re} ∈ 𝓝 z₀ :=
      (isOpen_lt continuous_const continuous_re).mem_nhds
        (by show 1 < z₀.re; rw [hz₀re]; linarith [le_max_right θ 1])
    filter_upwards [hmem] with z hz
    simp [hG, h1 z hz]
  have hzero : EqOn G 0 (U θ) :=
    hGa.eqOn_zero_of_preconnected_of_eventuallyEq_zero (U_convexo θ).isPreconnected hz₀U hev
  -- s está no fecho de U
  have hcl : s ∈ closure (U θ) := by
    rw [Metric.mem_closure_iff]
    intro ε hε
    refine ⟨s + ((ε / 2 : ℝ) : ℂ) * I, ⟨?_, ?_⟩, ?_⟩
    · simpa using hs
    · simp; linarith
    · rw [dist_eq_norm, sub_add_cancel_left, norm_neg, norm_mul, Complex.norm_I, mul_one,
        Complex.norm_real, Real.norm_of_nonneg (by linarith)]
      linarith
  -- G contínua em s
  have hFs : DifferentiableAt ℂ F s := (hF s hs).differentiableAt (hopen.mem_nhds hs)
  have hGc : ContinuousAt G s :=
    ((hFs.mul (differentiableAt_riemannZeta hs1)).sub_const 1).continuousAt
  have himg := hGc.continuousWithinAt.mem_closure_image hcl
  have hsub : G '' U θ ⊆ {0} := by
    rintro _ ⟨z, hz, rfl⟩
    exact hzero hz
  have hGs : G s = 0 := by
    have := closure_mono hsub himg
    rwa [closure_singleton, mem_singleton_iff] at this
  simpa [hG, sub_eq_zero] using hGs

/-- **Volta**: `1/ζ` continua até `Re s > θ` ⇒ sem zeros em `Re s > θ`. -/
theorem semZeros_of_continuaAte {θ : ℝ} (h : ContinuaAte θ) : SemZeros θ := by
  obtain ⟨F, hF, h1⟩ := h
  intro s hs hz
  rcases eq_or_ne s 1 with rfl | hs1
  · exact riemannZeta_one_ne_zero hz
  rcases le_or_gt 0 s.im with him | him
  · have := chave hF h1 hs him hs1
    rw [hz, mul_zero] at this
    exact zero_ne_one this
  · -- o conjugado está no semiplano superior e também é zero
    have hc : riemannZeta (conj s) = 0 := by rw [riemannZeta_conj, hz, map_zero]
    have hcre : θ < (conj s).re := by rwa [conj_re]
    have hcim : 0 ≤ (conj s).im := by rw [conj_im]; linarith
    have hc1 : conj s ≠ 1 := by
      intro he
      have : (conj s).im = 0 := by rw [he]; simp
      rw [conj_im] at this
      linarith
    have := chave hF h1 hcre hcim hc1
    rw [hc, mul_zero] at this
    exact zero_ne_one this

/-- **O critério**: `ζ` não tem zeros em `Re s > θ` ⟺ `1/ζ` continua holomorfa até `Re s > θ`. -/
theorem semZeros_iff_continuaAte (θ : ℝ) : SemZeros θ ↔ ContinuaAte θ :=
  ⟨continuaAte_of_semZeros, semZeros_of_continuaAte⟩

/-- O critério dito com o traço fermiônico `Σ μ(n) n^{−s}`. -/
theorem continuaAte_iff_traco (θ : ℝ) : ContinuaAte θ ↔
    ∃ F : ℂ → ℂ, DifferentiableOn ℂ F {s | θ < s.re} ∧ ∀ s : ℂ, 1 < s.re → F s = LSeries ↗μ s := by
  refine exists_congr fun F => and_congr_right fun _ => forall_congr' fun s => imp_congr_right fun hs => ?_
  rw [traco_fermionico_eq hs]
  have hz := riemannZeta_ne_zero_of_one_le_re hs.le
  constructor
  · intro h; exact eq_inv_of_mul_eq_one_left h
  · intro h; rw [h]; exact inv_mul_cancel₀ hz

/-- Monotonia: continuar até `θ` dá continuação até todo `θ' ≥ θ`. -/
theorem continuaAte_mono {θ θ' : ℝ} (h : θ ≤ θ') (hθ : ContinuaAte θ) : ContinuaAte θ' := by
  obtain ⟨F, hF, h1⟩ := hθ
  exact ⟨F, hF.mono fun s hs => lt_of_le_of_lt h hs, h1⟩

/-- Sempre vale até `θ = 1` (Hadamard–de la Vallée Poussin, Mathlib). -/
theorem continuaAte_um : ContinuaAte 1 :=
  continuaAte_of_semZeros fun _ hs => riemannZeta_ne_zero_of_one_le_re hs.le

end ATK.Fracoes.Fermions

#print axioms ATK.Fracoes.Fermions.indice_witten
#print axioms ATK.Fracoes.Fermions.traco_fermionico_eq
#print axioms ATK.Fracoes.Fermions.traco_fermionico
#print axioms ATK.Fracoes.Fermions.inv_zeta_tende_zero
#print axioms ATK.Fracoes.Fermions.inversa_de_ne
#print axioms ATK.Fracoes.Fermions.continuaAte_of_semZeros
#print axioms ATK.Fracoes.Fermions.U_aberto
#print axioms ATK.Fracoes.Fermions.U_convexo
#print axioms ATK.Fracoes.Fermions.chave
#print axioms ATK.Fracoes.Fermions.semZeros_of_continuaAte
#print axioms ATK.Fracoes.Fermions.semZeros_iff_continuaAte
#print axioms ATK.Fracoes.Fermions.continuaAte_iff_traco
#print axioms ATK.Fracoes.Fermions.continuaAte_mono
#print axioms ATK.Fracoes.Fermions.continuaAte_um
