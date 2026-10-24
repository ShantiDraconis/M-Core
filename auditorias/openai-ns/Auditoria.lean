import NavierStokes.ComparatorSolution

/-!
# Auditoria independente: mini-comparador e axiomas

Reescreve **literalmente** os enunciados (C) e (D) do desafio (Formal Conjectures, commit `8bf45ed`, copiados em
`ComparatorChallenges/NavierStokes.lean` do repositório da OpenAI) e os fecha com os teoremas da OpenAI.
Se o tipo do teorema entregue diferir do enunciado do desafio, este arquivo não compila.
-/

open ContDiff Set InnerProductSpace MeasureTheory
open scoped Laplacian

namespace AuditoriaATK

local notation "ℝ³" => EuclideanSpace ℝ (Fin 3)

open NavierStokes.Comparator in
/-- (C) Breakdown of Navier–Stokes solutions on ℝ³ — enunciado do desafio, sem alteração. -/
theorem enunciado_C (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionDecay u₀ ∧ ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p) :=
  NavierStokes.Comparator.navier_stokes_breakdown_R3 nu hnu

open NavierStokes.Comparator in
/-- (D) Breakdown of Navier–Stokes Solutions on ℝ³/ℤ³ — enunciado do desafio, sem alteração. -/
theorem enunciado_D (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionPeriodic u₀ ∧ ForceConditionPeriodic f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ f v p) :=
  NavierStokes.Comparator.navier_stokes_breakdown_periodic nu hnu

end AuditoriaATK

#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3
#print axioms NavierStokes.Comparator.navier_stokes_breakdown_periodic
#print axioms AuditoriaATK.enunciado_C
#print axioms AuditoriaATK.enunciado_D
