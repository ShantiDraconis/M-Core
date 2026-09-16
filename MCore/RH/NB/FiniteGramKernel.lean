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
    (hc : gramMatrix S *ᵥ c = 0) : c = 0 := by
  apply (gram_quadratic_eq_zero_iff_of_linearIndependent S hLI c).mp
  have hq :
      (∑ i, ∑ j, c i * gramMatrix S i j * c j) =
        ∑ i, c i * (gramMatrix S *ᵥ c) i := by
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
    ∀ c : Fin n → ℝ, gramMatrix S *ᵥ c = 0 → c = 0 := by
  intro c hc
  exact gram_mulVec_eq_zero_imp_coeff_zero_of_linearIndependent S hLI c hc

/-- Symmetry plus trivial right kernel makes the finite Gram bilinear form
nondegenerate. -/
theorem gram_nondegenerate_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) :
    (gramMatrix S).Nondegenerate := by
  rw [Matrix.nondegenerate_iff_forall_vecMul_and_mulVec_eq_zero]
  constructor
  · intro c hc
    have hct : (gramMatrix S)ᵀ *ᵥ c = 0 := by
      simpa [Matrix.vecMul_transpose] using hc
    have hs : (gramMatrix S)ᵀ = gramMatrix S := (gramMatrix_symmetric S)
    rw [hs] at hct
    exact gram_mulVec_eq_zero_imp_coeff_zero_of_linearIndependent S hLI c hct
  · exact gram_mulVec_kernel_trivial_of_linearIndependent S hLI

/-- For each fixed finite system, LI implies a nonzero Gram determinant.
No statement about `inf_n` or uniform conditioning is made. -/
theorem gram_det_ne_zero_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) :
    (gramMatrix S).det ≠ 0 := by
  rw [← Matrix.nondegenerate_iff_det_ne_zero]
  exact gram_nondegenerate_of_linearIndependent S hLI

end MCore.RH.NB
