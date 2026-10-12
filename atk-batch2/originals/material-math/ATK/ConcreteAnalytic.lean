import Mathlib

namespace ATK.ConcreteAnalytic

/-- Monotonicity of approximation error under nested feasible sets. -/
theorem infimum_antitone
    {α : Type*} (cost : α → Real) (A B : Set α)
    (hAB : A ⊆ B) (hA : (cost '' A).BddBelow)
    (hAn : (cost '' A).Nonempty) :
    sInf (cost '' B) ≤ sInf (cost '' A) := by
  apply csInf_le_csInf hA hAn
  exact Set.image_mono hAB

/-- Uniform O(1/log N) implies convergence, when the bound is established. -/
-- The concrete Riemann obligation is to PROVE this bound for the actual DN.
-- No assumption is hidden in a theorem claiming RH.
end ATK.ConcreteAnalytic
