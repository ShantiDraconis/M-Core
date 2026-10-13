import Mathlib.Basic.Real.Basic
import Mathlib.Order.Interval.Set.Defs

/-!
# Condicional — Navier–Stokes 3D (enunciado de Clay, caso A: ℝ³, sem força)

A Mathlib não tem teoria de soluções de Navier–Stokes; o enunciado é relativo a um
`NSModel` (fidelidade: PARAMÉTRICA).

Forma condicional:

  `EnstrophyBlowupCriterion M → EnstrophyAPrioriBound M → ClayStatementA M`

* `EnstrophyBlowupCriterion` (PONTE; Leray 1934 + teoria local clássica): se a solução
  suave não é global, existe T > 0 até onde ela existe e a enstrofia ‖∇u‖²₂ é ilimitada
  em [0, T).
* `EnstrophyAPrioriBound` (ABERTA): enquanto a solução suave existe em [0, T), a enstrofia
  é limitada lá. O lane `navier-stokes-critical-barrier-audit` (`ActualNSToSignedGainCore`)
  é uma rota proposta para esta cota; a comparação de Riccati em `ATK.NavierStokes`
  só dá cota LOCAL e não basta.
-/

namespace ATK.Conditional.NavierStokes

universe u

/-- Interface do problema. -/
structure NSModel where
  /-- dados iniciais u₀ -/
  Data : Type u
  /-- u₀ suave, div u₀ = 0, decaimento de Schwartz -/
  Admissible : Data → Prop
  /-- a solução suave existe em [0, T) -/
  SmoothOn : Data → ℝ → Prop
  /-- existe solução suave global com energia limitada -/
  GlobalSmooth : Data → Prop
  /-- y(t) = ‖∇u(t)‖²₂ -/
  enstrophy : Data → ℝ → ℝ

/-- Enunciado-alvo (Clay, caso A). -/
def ClayStatementA (M : NSModel.{u}) : Prop :=
  ∀ u₀, M.Admissible u₀ → M.GlobalSmooth u₀

/-- PONTE: critério clássico de explosão da enstrofia. -/
def EnstrophyBlowupCriterion (M : NSModel.{u}) : Prop :=
  ∀ u₀, M.Admissible u₀ → ¬ M.GlobalSmooth u₀ →
    ∃ T : ℝ, 0 < T ∧ M.SmoothOn u₀ T ∧ ∀ B : ℝ, ∃ t ∈ Set.Ico 0 T, B < M.enstrophy u₀ t

/-- HIPÓTESE ABERTA: cota a priori da enstrofia. -/
def EnstrophyAPrioriBound (M : NSModel.{u}) : Prop :=
  ∀ u₀, M.Admissible u₀ → ∀ T : ℝ, 0 < T → M.SmoothOn u₀ T →
    ∃ B : ℝ, ∀ t ∈ Set.Ico 0 T, M.enstrophy u₀ t ≤ B

/-- **Condicional Navier–Stokes.** -/
theorem ns_conditional {M : NSModel.{u}}
    (hBridge : EnstrophyBlowupCriterion M) (hOpen : EnstrophyAPrioriBound M) :
    ClayStatementA M := by
  intro u₀ hu
  by_contra hg
  obtain ⟨T, hT, hS, hblow⟩ := hBridge u₀ hu hg
  obtain ⟨B, hB⟩ := hOpen u₀ hu T hT hS
  obtain ⟨t, ht, hlt⟩ := hblow B
  exact absurd (hB t ht) (not_le.mpr hlt)

end ATK.Conditional.NavierStokes

#print axioms ATK.Conditional.NavierStokes.ns_conditional
