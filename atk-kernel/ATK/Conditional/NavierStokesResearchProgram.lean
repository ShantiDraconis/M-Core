import ATK.Conditional.NavierStokes

/-!
# Research-structure decomposition of `EnstrophyAPrioriBound` (O3)

This module adds **no new mathematical content**. It decomposes the open obligation into the
two steps a real a priori estimate for Navier–Stokes actually has: a differential/Grönwall-type
inequality (classical energy-estimate technique) and a bound on a single scalar "controlling
quantity" (the genuinely open step). Nothing here is inhabited.

* **Energy inequality (classical form).** The standard route to an enstrophy bound is a
  Grönwall-type estimate `enstrophy(t) ≤ enstrophy(0) · exp(Φ(t))`, where `Φ` is built from a
  controlling quantity such as `∫₀ᵗ ‖ω(s)‖_∞ ds` (Beale–Kato–Majda, 1984) or
  `∫₀ᵗ ‖u(s)‖_{L^q}^p ds` with `2/p + 3/q = 1`, `q > 3` (Ladyzhenskaya–Prodi–Serrin). Deriving
  *this* inequality from the equations is classical PDE technique.
* **Boundedness of the controlling quantity (open).** Showing `Φ` stays finite on `[0, T)` is
  already equivalent in strength to global regularity itself (that is the content of the
  Beale–Kato–Majda / Prodi–Serrin criteria): no a priori bound on `Φ` independent of already
  knowing the solution stays smooth is known. `M-Core`'s own `ATK.NSExplosao.explosao_comparacao`
  records that the naive Riccati comparison `y' = -a y + b y³` with `b y₀² > a` blows up in finite
  time — confirming that a weaker differential inequality alone cannot be substituted for an
  actual bound on `Φ`.
-/

namespace ATK.Conditional.NavierStokes

universe u

/-- The two-step shape of a real `EnstrophyAPrioriBound` producer, for one admissible datum `u₀`
and one time horizon `T`. -/
structure EnstrophyControlProgram (M : NSModel.{u}) (u₀ : M.Data) (T : ℝ) where
  /-- The abstract quantity carries no sign information on its own; the physical quantity
  (enstrophy at time `0`) is nonnegative, which the Grönwall step below needs. -/
  enstrophy_zero_nonneg : 0 ≤ M.enstrophy u₀ 0
  /-- The controlling quantity `Φ(t)` (e.g. the BKM or Prodi–Serrin integral). -/
  controlling : ℝ → ℝ
  /-- Classical step: the Grönwall-type energy inequality. -/
  energyInequality : ∀ t ∈ Set.Ico (0 : ℝ) T,
    M.enstrophy u₀ t ≤ M.enstrophy u₀ 0 * Real.exp (controlling t)
  /-- Open step: the controlling quantity stays bounded on `[0, T)`. -/
  controlling_bounded : ∃ C, ∀ t ∈ Set.Ico (0 : ℝ) T, controlling t ≤ C

/-- The decomposition still supplies exactly the enstrophy bound this `u₀`, `T` needs. -/
theorem EnstrophyControlProgram.toBound {M : NSModel.{u}} {u₀ : M.Data} {T : ℝ}
    (P : EnstrophyControlProgram M u₀ T) :
    ∃ B : ℝ, ∀ t ∈ Set.Ico (0 : ℝ) T, M.enstrophy u₀ t ≤ B := by
  obtain ⟨C, hC⟩ := P.controlling_bounded
  refine ⟨M.enstrophy u₀ 0 * Real.exp C, fun t ht => ?_⟩
  calc M.enstrophy u₀ t
      ≤ M.enstrophy u₀ 0 * Real.exp (P.controlling t) := P.energyInequality t ht
    _ ≤ M.enstrophy u₀ 0 * Real.exp C :=
        mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr (hC t ht)) P.enstrophy_zero_nonneg

/-- A full producer, supplying the program for every admissible datum and horizon. -/
theorem enstrophyAPrioriBound_of_researchPrograms {M : NSModel.{u}}
    (P : ∀ u₀, M.Admissible u₀ → ∀ T : ℝ, 0 < T → M.SmoothOn u₀ T →
      EnstrophyControlProgram M u₀ T) : EnstrophyAPrioriBound M :=
  fun u₀ hu T hT hS => (P u₀ hu T hT hS).toBound

end ATK.Conditional.NavierStokes

#print axioms ATK.Conditional.NavierStokes.EnstrophyControlProgram.toBound
#print axioms ATK.Conditional.NavierStokes.enstrophyAPrioriBound_of_researchPrograms
