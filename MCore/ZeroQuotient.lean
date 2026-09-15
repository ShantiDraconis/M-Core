import MCore.A3Zero
import Mathlib

namespace MCore

/-- One explicit quotient G/H. Both functions are fixed globally; only the
approach path changes. -/
def zeroG (p : ℝ × ℝ) : ℝ := p.1
def zeroH (p : ℝ × ℝ) : ℝ := p.2

def zeroPath (c : ℝ) (n : ℕ) : ℝ × ℝ :=
  if n = 0 then (0, 1) else (c / n, 1 / n)

/-- Along every fixed-c path, both numerator and denominator converge to zero. -/
theorem zeroG_tendsto (c : ℝ) :
    Filter.Tendsto (fun n : ℕ => zeroG (zeroPath c n)) Filter.atTop (nhds 0) := by
  simpa [zeroG, zeroPath] using
    (tendsto_const_nhds.div_atTop (tendsto_natCast_atTop_atTop.comp tendsto_id)).comp tendsto_id

/-- Algebraic core of the path computation: for n>0 the same quotient G/H is c. -/
theorem quotient_zeroPath {c : ℝ} {n : ℕ} (hn : 0 < n) :
    zeroG (zeroPath c n) / zeroH (zeroPath c n) = c := by
  simp [zeroG, zeroH, zeroPath, Nat.ne_of_gt hn]
  field_simp

/-- K0 and RHO are two paths through the same G/H with incompatible ratios. -/
theorem K0_RHO_incompatible {n : ℕ} (hn : 0 < n) :
    zeroG (zeroPath 0 n) / zeroH (zeroPath 0 n) ≠
    zeroG (zeroPath (1/2 : ℝ) n) / zeroH (zeroPath (1/2 : ℝ) n) := by
  rw [quotient_zeroPath hn, quotient_zeroPath hn]
  norm_num

/-- Obligation 18, abstractly: distinct candidate path limits cannot define a
single path-independent extension. -/
theorem explicit_no_common_extension :
    ¬ ∃ L : ℝ, L = 0 ∧ L = (1/2 : ℝ) := by
  exact no_path_independent_extension
    { limit₁ := 0, limit₂ := 1/2, distinct := by norm_num }

end MCore
