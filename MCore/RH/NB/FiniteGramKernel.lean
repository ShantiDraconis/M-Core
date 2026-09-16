import Mathlib
import MCore.RH.NB.FiniteGramIndependence

open scoped InnerProductSpace

namespace MCore.RH.NB

/-- If the finite generators are linearly independent, the Gram matrix has trivial
right kernel. This is a pointwise finite-dimensional statement; it carries no
uniform lower bound in the family size. -/
theorem gram_mulVec_eq_zero_imp_coeff_zero_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) (c : Fin n → ℝ)
    (hc : Matrix.mulVec (gramMatrix S) c = 0) : c = 0 := by
  apply (gram_quadratic_eq_zero_iff_of_linearIndependent S hLI c).mp
  have hq :
      (∑ i, ∑ j, c i * gramMatrix S i j * c j) =
        ∑ i, c i * (Matrix.mulVec (gramMatrix S) c) i := by
    simp only [Matrix.mulVec, dotProduct]
    congr 1
    funext i
    rw [Finset.mul_sum]
    congr 1
    funext j
    ring
  rw [hq, hc]
  simp

/-- The Gram matrix has trivial right kernel under finite linear independence. -/
theorem gram_mulVec_kernel_trivial_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) :
    ∀ c : Fin n → ℝ, Matrix.mulVec (gramMatrix S) c = 0 → c = 0 := by
  intro c hc
  exact gram_mulVec_eq_zero_imp_coeff_zero_of_linearIndependent S hLI c hc

end MCore.RH.NB
