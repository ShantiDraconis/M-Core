import ATK.TresZeros
import ATK.FracoesMalha

/-!
# ATK — A malha com `h = γ₁`: o mínimo do eixo de 180° está no anel de centro 8 (rodada 105)

Com `γ₁` o primeiro zero certificado (`ATK.TresZeros.tres_zeros`, `|γ₁ − 14,1347251417| ≤ 10⁻⁶`), o raio da
malha é `h = γ₁` e `δ = γ₁ − 14 ∈ [0,13; 0,14]`. A direção `k = 8` (180°) do anel de centro `c` é o ponto real
`c − γ₁` (`ponto_oito`). Entre todos os centros pares `c = 14 − 2m ≤ 12`, `|ζ(c − γ₁)|` é mínimo em `c = 8`
(`anel_oito_minimo`), pela lei de `ATK.Fracoes.Malha.minimo_global`. Incondicional.

Classificação: **consequência**. O ponto `8 − γ₁ ≈ −6,1347` está a `δ` do zero trivial `−6`; não é zero.
-/

namespace ATK.Fracoes.MalhaZeros

open ATK.Fracoes.Malha Complex

/-- A direção `k = 8` (180°) do anel de centro `c` é o ponto real `c − h`. -/
theorem ponto_oito (c h : ℝ) : ponto c h 8 = ((c - h : ℝ) : ℂ) := by
  unfold ponto
  have e : (((8 : ℕ) : ℝ) * Real.pi / 8 : ℝ) = Real.pi := by push_cast; ring
  rw [e, Complex.exp_pi_mul_I]
  push_cast
  ring

/-- **O anel de centro 8 dá o menor `|ζ|` na direção de 180°**, entre todos os centros pares `c ≤ 12`. -/
theorem anel_oito_minimo :
    ∃ γ₁ : ℝ, riemannZeta ((1 / 2 : ℂ) + (γ₁ : ℂ) * I) = 0 ∧ |γ₁ - 141347251417 / 10 ^ 10| ≤ 1 / 10 ^ 6 ∧
      ∀ m : ℕ, 1 ≤ m → m ≠ 3 →
        ‖riemannZeta (ponto 8 γ₁ 8)‖ < ‖riemannZeta (ponto (14 - 2 * m) γ₁ 8)‖ := by
  obtain ⟨γ₁, -, -, z1, e1, -⟩ := ATK.TresZeros.tres_zeros
  refine ⟨γ₁, z1, e1, fun m hm h3 => ?_⟩
  rw [abs_le] at e1
  obtain ⟨l1, u1⟩ := e1
  norm_num at l1 u1
  have hd0 : 13 / 100 ≤ γ₁ - 14 := by linarith
  have hd1 : γ₁ - 14 ≤ 14 / 100 := by linarith
  have key := minimo_global hd0 hd1 m hm h3
  unfold a at key
  rw [ponto_oito, ponto_oito]
  have ea : ((8 - γ₁ : ℝ) : ℂ) = ((-(2 * ((3 : ℕ) : ℝ) + (γ₁ - 14)) : ℝ) : ℂ) := by push_cast; ring
  have eb : ((14 - 2 * (m : ℝ) - γ₁ : ℝ) : ℂ) = ((-(2 * (m : ℝ) + (γ₁ - 14)) : ℝ) : ℂ) := by push_cast; ring
  rw [ea, eb]
  exact key

end ATK.Fracoes.MalhaZeros

#print axioms ATK.Fracoes.MalhaZeros.ponto_oito
#print axioms ATK.Fracoes.MalhaZeros.anel_oito_minimo
