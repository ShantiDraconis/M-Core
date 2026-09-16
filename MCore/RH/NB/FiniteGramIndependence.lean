import Mathlib
import MCore.RH.NB.FiniteGram

open scoped InnerProductSpace

namespace MCore.RH.NB

/-- The synthesis map associated with a finite generator family. -/
def synthesis {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n) (c : Fin n → ℝ) : E :=
  ∑ i, c i • S.generator i

/-- The Gram quadratic form is exactly the squared norm of the synthesis vector. -/
theorem gram_quadratic_eq_norm_sq {E : Type} [NormedAddCommGroup E]
    [InnerProductSpace ℝ E] {n : ℕ} (S : FiniteApproximationSystem E n)
    (c : Fin n → ℝ) :
    ∑ i, ∑ j, c i * gramMatrix S i j * c j = ‖synthesis S c‖ ^ 2 := by
  have hinner :
      ⟪synthesis S c, synthesis S c⟫_ℝ =
        ∑ i, ∑ j, c i * gramMatrix S i j * c j := by
    simp only [synthesis, gramMatrix, inner_sum, sum_inner, real_inner_smul_left,
      real_inner_smul_right]
    congr 1
    funext i
    congr 1
    funext j
    rw [real_inner_comm]
    ring
  rw [← hinner]
  exact (real_inner_self_eq_norm_sq _).symm

/-- Linear independence of the finite generators makes the synthesis map injective.
This is pointwise in `n`; it asserts no uniform conditioning as `n → ∞`. -/
theorem synthesis_eq_zero_iff_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) (c : Fin n → ℝ) :
    synthesis S c = 0 ↔ c = 0 := by
  constructor
  · intro h
    exact Fintype.linearCombination_injective hLI (by simpa [synthesis] using h)
  · intro h
    simp [h, synthesis]

/-- A zero Gram quadratic form forces all coefficients to vanish under finite LI.
This is the coercivity/nondegeneracy fact needed before any determinant theorem. -/
theorem gram_quadratic_eq_zero_iff_of_linearIndependent
    {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    {n : ℕ} (S : FiniteApproximationSystem E n)
    (hLI : LinearIndependent ℝ S.generator) (c : Fin n → ℝ) :
    (∑ i, ∑ j, c i * gramMatrix S i j * c j = 0) ↔ c = 0 := by
  rw [gram_quadratic_eq_norm_sq]
  rw [sq_eq_zero_iff, norm_eq_zero]
  exact synthesis_eq_zero_iff_of_linearIndependent S hLI c

end MCore.RH.NB
