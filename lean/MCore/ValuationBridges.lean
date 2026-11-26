import Mathlib
namespace MCoreBridges
def constants : Fin 9 → ℕ := ![63,64,79,92,94,98,103,109,111]
def primes : Fin 9 → ℕ := ![2,3,7,23,37,47,79,103,109]
def V : Matrix (Fin 9) (Fin 9) ℤ :=
  !![0,2,1,0,0,0,0,0,0;
     6,0,0,0,0,0,0,0,0;
     0,0,0,0,0,0,1,0,0;
     2,0,0,1,0,0,0,0,0;
     1,0,0,0,0,1,0,0,0;
     1,0,2,0,0,0,0,0,0;
     0,0,0,0,0,0,0,1,0;
     0,0,0,0,0,0,0,0,1;
     0,1,0,0,1,0,0,0,0]
theorem sumSquares : (∑ i, constants i ^ 2) = 76021 := by decide
theorem gram_sum_nonneg {n : ℕ} (x : Fin n → ℝ) :
    0 ≤ ∑ i, (x i)^2 := by
  exact Finset.sum_nonneg (fun i _ => sq_nonneg (x i))
def moment {n : ℕ} (μ : Fin n → ℝ) (k : ℕ) : ℝ := ∑ i, μ i ^ k
def spectralForm {n m : ℕ} (μ : Fin n → ℝ) (b : Fin m → ℝ) (shift : ℕ) : ℝ :=
  ∑ i, μ i ^ shift * (∑ j, b j * μ i ^ (j : ℕ)) ^ 2
theorem spectralForm_nonneg {n m : ℕ} (μ : Fin n → ℝ) (b : Fin m → ℝ)
    (h : ∀ i, 0 ≤ μ i) (shift : ℕ) : 0 ≤ spectralForm μ b shift := by
  unfold spectralForm
  exact Finset.sum_nonneg (fun i _ => mul_nonneg (pow_nonneg (h i) _) (sq_nonneg _))
def MomentMatch (s t : ℕ → ℝ) : Prop := ∀ k, s k = t k
theorem transfer_nonneg (s t : ℕ → ℝ) (h : MomentMatch s t)
    (ht : ∀ k, 0 ≤ t k) : ∀ k, 0 ≤ s k := by
  intro k
  rw [h k]
  exact ht k
#print axioms sumSquares
#print axioms gram_sum_nonneg
#print axioms spectralForm_nonneg
#print axioms transfer_nonneg
end MCoreBridges
