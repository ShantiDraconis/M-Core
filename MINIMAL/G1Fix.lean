import Mathlib

namespace MCoreMinimal

/-- Purely algebraic conditional bound. The actual Navier–Stokes coefficient
and dissipation integral have NOT been identified or estimated here. -/
theorem G1Fix_ConditionalEnergyBound
    (C E0 D aIntegral : ℝ)
    (hE0 : 0 ≤ E0)
    (hD : D ≤ E0)
    (hC : C ^ 2 ≤ 36)
    (ha : aIntegral = C ^ 2 * D) :
    aIntegral ≤ 36 * E0 := by
  rw [ha]
  calc
    C ^ 2 * D ≤ C ^ 2 * E0 :=
      mul_le_mul_of_nonneg_left hD (sq_nonneg C)
    _ ≤ 36 * E0 := mul_le_mul_of_nonneg_right hC hE0

end MCoreMinimal
