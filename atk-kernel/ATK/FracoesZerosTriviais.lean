import ATK.FracoesLinearizacao
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.NumberTheory.LSeries.Nonvanishing

/-!
# ATK — Os zeros triviais são simples: `|ζ′(−2m)| = (2m)!·ζ(2m+1)/(2(2π)^{2m})` (rodada 107)

A rodada 106 provou a lei exata `|ζ(−2m−δ)| = 2|sin(πδ/2)|·K_m(δ)` (`formula_exata`). Dividindo por `δ` e
fazendo `δ → 0⁺`, os dois lados têm limite:

* o lado esquerdo vai a `|ζ′(−2m)|` (derivada complexa, lida na direção real: `zeta_real_hasDerivAt`);
* `2|sin(πδ/2)|/δ → π` (`seno_sobre`, por sanduíche `x − x³/6 < sin x ≤ x`) e `K_m(δ) → K_m(0)`
  (`K_tende`, continuidade de `rpow`, `Γ` e `ζ` longe de `1`; precisa de `m ≥ 1`).

Daí **`derivada_exata`**: `‖ζ′(−2m)‖ = π·K_m(0)` e **`derivada_fatorial`**:
`‖ζ′(−2m)‖ = (2m)!·|ζ(2m+1)|/(2(2π)^{2m})` — a identificação que a rodada 106 deixou fora do kernel. Como
`ζ(2m+1) ≠ 0`, **`zero_trivial_simples`**: `ζ′(−2m) ≠ 0` para todo `m ≥ 1`: todo zero trivial é simples.

Ponte com RH: para os zeros **não triviais** a simplicidade é conjectura (aberta, independente de RH); para os
triviais ela sai da equação funcional, e o quase-zero da malha (rodada 105) é a reta tangente
`|ζ(−2m−δ)| ≈ δ·|ζ′(−2m)|` com o erro controlado de dois lados (`linearizacao`).
Classificação: **consequência**. RH continua `OPEN_MATH`.
-/

open Filter Topology Set
open ATK.Fracoes.Malha ATK.Fracoes.Linearizacao

namespace ATK.Fracoes.ZerosTriviais

/-! ## 1. Os dois limites do lado direito -/

/-- `2|sin(πδ/2)|/δ → π` quando `δ → 0⁺`. -/
theorem seno_sobre :
    Tendsto (fun δ : ℝ => 2 * |Real.sin (Real.pi * δ / 2)| / δ) (𝓝[>] 0) (𝓝 Real.pi) := by
  have hlo : Tendsto (fun δ : ℝ => Real.pi - Real.pi ^ 3 * δ ^ 2 / 24) (𝓝[>] 0) (𝓝 Real.pi) := by
    have h : Tendsto (fun δ : ℝ => Real.pi - Real.pi ^ 3 * δ ^ 2 / 24) (𝓝 0)
        (𝓝 (Real.pi - Real.pi ^ 3 * 0 ^ 2 / 24)) :=
      ((continuous_const.sub ((continuous_const.mul (continuous_id.pow 2)).div_const 24)).tendsto 0)
    rw [show Real.pi - Real.pi ^ 3 * 0 ^ 2 / 24 = Real.pi by ring] at h
    exact h.mono_left nhdsWithin_le_nhds
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlo tendsto_const_nhds ?_ ?_
  · filter_upwards [self_mem_nhdsWithin] with δ (hδ : 0 < δ)
    have hx : 0 < Real.pi * δ / 2 := by positivity
    have hs := Real.sin_gt_sub_cube hx
    rw [le_div_iff₀ hδ]
    calc (Real.pi - Real.pi ^ 3 * δ ^ 2 / 24) * δ
        = 2 * (Real.pi * δ / 2 - (Real.pi * δ / 2) ^ 3 / 6) := by ring
      _ ≤ 2 * Real.sin (Real.pi * δ / 2) := by linarith
      _ ≤ 2 * |Real.sin (Real.pi * δ / 2)| := by linarith [le_abs_self (Real.sin (Real.pi * δ / 2))]
  · filter_upwards [self_mem_nhdsWithin] with δ (hδ : 0 < δ)
    have hx : 0 ≤ Real.pi * δ / 2 := by positivity
    have h1 : |Real.sin (Real.pi * δ / 2)| ≤ Real.pi * δ / 2 := by
      have := Real.abs_sin_le_abs (x := Real.pi * δ / 2)
      rwa [abs_of_nonneg hx] at this
    rw [div_le_iff₀ hδ]
    linarith

/-- `K_m` é contínua em `δ = 0` para `m ≥ 1`. -/
theorem K_tende (m : ℕ) (hm : 1 ≤ m) : Tendsto (K m) (𝓝[>] 0) (𝓝 (K m 0)) := by
  have hm' : (1 : ℝ) ≤ m := by exact_mod_cast hm
  have hc : ContinuousAt (K m) 0 := by
    unfold K
    have h1 : ContinuousAt (fun δ : ℝ => (2 * Real.pi) ^ (-(2 * (m : ℝ) + 1 + δ))) 0 :=
      ContinuousAt.rpow continuousAt_const (by fun_prop) (Or.inl (by positivity))
    have h2 : ContinuousAt (fun δ : ℝ => Real.Gamma (2 * m + 1 + δ)) 0 := by
      have hg : ContinuousAt Real.Gamma (2 * m + 1 + 0) := by
        refine (Real.differentiableAt_Gamma fun n => ?_).continuousAt
        have : (0 : ℝ) ≤ n := n.cast_nonneg
        intro h
        linarith
      exact hg.comp (f := fun δ : ℝ => 2 * (m : ℝ) + 1 + δ) (by fun_prop)
    have h3 : ContinuousAt (fun δ : ℝ => a (2 * m + 1 + δ)) 0 := by
      unfold a
      have hz : ContinuousAt riemannZeta (((2 * m + 1 + 0 : ℝ)) : ℂ) := by
        refine (differentiableAt_riemannZeta ?_).continuousAt
        intro h
        have := congrArg Complex.re h
        simp at this
        linarith
      have hz' : ContinuousAt (fun δ : ℝ => riemannZeta ((2 * m + 1 + δ : ℝ) : ℂ)) 0 :=
        hz.comp (f := fun δ : ℝ => ((2 * m + 1 + δ : ℝ) : ℂ)) (by fun_prop)
      exact hz'.norm
    exact (h1.mul h2).mul h3
  exact hc.tendsto.mono_left nhdsWithin_le_nhds

/-! ## 2. O lado esquerdo: a derivada na direção real -/

/-- `ζ(−2m) = 0` para `m ≥ 1`, com o argumento real. -/
theorem zeta_menos_dois_m (m : ℕ) (hm : 1 ≤ m) : riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ) = 0 := by
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  have := riemannZeta_neg_two_mul_nat_add_one k
  convert this using 2
  push_cast
  ring

theorem nao_um (m : ℕ) : ((-(2 * m : ℝ) : ℝ) : ℂ) ≠ 1 := by
  intro h
  have := congrArg Complex.re h
  simp at this
  have : (0 : ℝ) ≤ m := m.cast_nonneg
  linarith

/-- A derivada complexa em `−2m`, lida pela função real `x ↦ ζ(x)`. -/
theorem zeta_real_hasDerivAt (m : ℕ) :
    HasDerivAt (fun x : ℝ => riemannZeta (x : ℂ)) (deriv riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ))
      (-(2 * m : ℝ)) :=
  ((differentiableAt_riemannZeta (nao_um m)).hasDerivAt).comp_ofReal

/-- `a(−(2m + δ))/δ → ‖ζ′(−2m)‖` quando `δ → 0⁺`. -/
theorem quociente_tende (m : ℕ) (hm : 1 ≤ m) :
    Tendsto (fun δ : ℝ => a (-(2 * m + δ)) / δ) (𝓝[>] 0)
      (𝓝 ‖deriv riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ)‖) := by
  have h := (zeta_real_hasDerivAt m).tendsto_slope_zero_left
  have hneg : Tendsto (fun δ : ℝ => -δ) (𝓝[>] 0) (𝓝[<] 0) := by
    refine tendsto_nhdsWithin_iff.mpr ⟨?_, ?_⟩
    · have := ((continuous_neg (G := ℝ)).tendsto 0).mono_left (nhdsWithin_le_nhds (s := Ioi (0 : ℝ)))
      simpa using this
    · filter_upwards [self_mem_nhdsWithin] with δ (hδ : 0 < δ)
      show -δ < 0
      linarith
  have h2 := (h.comp hneg).norm
  refine h2.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with δ (hδ : 0 < δ)
  simp only [Function.comp_apply]
  rw [zeta_menos_dois_m m hm, sub_zero, norm_smul, norm_inv, Real.norm_eq_abs, abs_neg,
    abs_of_pos hδ, a, inv_mul_eq_div]
  congr 3
  push_cast
  ring

/-! ## 3. A derivada exata e a simplicidade -/

/-- **`‖ζ′(−2m)‖ = π·K_m(0)`** para `m ≥ 1`. -/
theorem derivada_exata (m : ℕ) (hm : 1 ≤ m) :
    ‖deriv riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ)‖ = Real.pi * K m 0 := by
  have hR : Tendsto (fun δ : ℝ => a (-(2 * m + δ)) / δ) (𝓝[>] 0) (𝓝 (Real.pi * K m 0)) := by
    have := (seno_sobre.mul (K_tende m hm))
    refine this.congr' ?_
    filter_upwards [self_mem_nhdsWithin, Ioo_mem_nhdsGT (show (0 : ℝ) < 1 by norm_num)] with δ
      (hδ : 0 < δ) hδ1
    rw [formula_exata m hδ hδ1.2]
    field_simp
  exact tendsto_nhds_unique (quociente_tende m hm) hR

/-- `K_m(0) = (2m)!·|ζ(2m+1)|/(2π)^{2m+1}`. -/
theorem K_zero (m : ℕ) :
    K m 0 = (Nat.factorial (2 * m) : ℝ) * a (2 * m + 1) / (2 * Real.pi) ^ (2 * m + 1) := by
  unfold K
  have hpos : (0 : ℝ) < 2 * Real.pi := by positivity
  have e1 : (2 * Real.pi) ^ (-(2 * (m : ℝ) + 1 + 0)) = ((2 * Real.pi) ^ (2 * m + 1))⁻¹ := by
    rw [Real.rpow_neg hpos.le, add_zero, ← Real.rpow_natCast]
    push_cast
    ring_nf
  have e2 : Real.Gamma (2 * (m : ℝ) + 1 + 0) = (Nat.factorial (2 * m) : ℝ) := by
    rw [add_zero, ← Real.Gamma_nat_eq_factorial]
    push_cast
    ring_nf
  rw [e1, e2, add_zero]
  field_simp

/-- **`‖ζ′(−2m)‖ = (2m)!·|ζ(2m+1)|/(2(2π)^{2m})`** para `m ≥ 1` (a fórmula clássica). -/
theorem derivada_fatorial (m : ℕ) (hm : 1 ≤ m) :
    ‖deriv riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ)‖ =
      (Nat.factorial (2 * m) : ℝ) * a (2 * m + 1) / (2 * (2 * Real.pi) ^ (2 * m)) := by
  rw [derivada_exata m hm, K_zero, pow_succ]
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp

/-- `|ζ(2m+1)| > 0`. -/
theorem a_impar_pos (m : ℕ) (hm : 1 ≤ m) : 0 < a (2 * m + 1) := by
  unfold a
  refine norm_pos_iff.mpr (riemannZeta_ne_zero_of_one_le_re ?_)
  have : (1 : ℝ) ≤ m := by exact_mod_cast hm
  rw [Complex.ofReal_re]
  linarith

/-- **Os zeros triviais são simples**: `ζ′(−2m) ≠ 0` para todo `m ≥ 1`. -/
theorem zero_trivial_simples (m : ℕ) (hm : 1 ≤ m) :
    deriv riemannZeta ((-(2 * m : ℝ) : ℝ) : ℂ) ≠ 0 := by
  intro h
  have := derivada_fatorial m hm
  rw [h, norm_zero] at this
  have hp : 0 < (Nat.factorial (2 * m) : ℝ) * a (2 * m + 1) / (2 * (2 * Real.pi) ^ (2 * m)) := by
    have := a_impar_pos m hm
    positivity
  linarith

/-- Exemplo: `|ζ′(−2)| = ζ(3)/(4π²)`. -/
theorem derivada_menos_dois :
    ‖deriv riemannZeta ((-(2 * (1 : ℕ) : ℝ) : ℝ) : ℂ)‖ = a 3 / (4 * Real.pi ^ 2) := by
  rw [derivada_fatorial 1 le_rfl]
  norm_num
  ring

end ATK.Fracoes.ZerosTriviais

#print axioms ATK.Fracoes.ZerosTriviais.seno_sobre
#print axioms ATK.Fracoes.ZerosTriviais.K_tende
#print axioms ATK.Fracoes.ZerosTriviais.zeta_menos_dois_m
#print axioms ATK.Fracoes.ZerosTriviais.nao_um
#print axioms ATK.Fracoes.ZerosTriviais.zeta_real_hasDerivAt
#print axioms ATK.Fracoes.ZerosTriviais.quociente_tende
#print axioms ATK.Fracoes.ZerosTriviais.derivada_exata
#print axioms ATK.Fracoes.ZerosTriviais.K_zero
#print axioms ATK.Fracoes.ZerosTriviais.derivada_fatorial
#print axioms ATK.Fracoes.ZerosTriviais.a_impar_pos
#print axioms ATK.Fracoes.ZerosTriviais.zero_trivial_simples
#print axioms ATK.Fracoes.ZerosTriviais.derivada_menos_dois
