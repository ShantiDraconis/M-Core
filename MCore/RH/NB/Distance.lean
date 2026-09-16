import Mathlib.Topology.MetricSpace.Pseudo.Defs
import Mathlib.Topology.Algebra.Order
import MCore.RH.ResearchObligations

namespace MCore.RH.NB

/-- Abstract nested approximation spaces.  This layer deliberately does not identify
these spaces with the Nyman--Beurling spaces until the admissibility bridge is built. -/
structure ApproximationFamily (X : Type) [PseudoMetricSpace X] where
  target : X
  admissible : ℕ → Set X
  nested : ∀ {m n : ℕ}, m ≤ n → admissible m ⊆ admissible n

/-- Squared distance to the N-th admissible approximation set. -/
noncomputable def distanceSq {X : Type} [PseudoMetricSpace X]
    (F : ApproximationFamily X) (N : ℕ) : ℝ :=
  (Metric.infDist F.target (F.admissible N)) ^ 2

/-- Distance is nonnegative without any RH assumption. -/
theorem distanceSq_nonneg {X : Type} [PseudoMetricSpace X]
    (F : ApproximationFamily X) (N : ℕ) :
    0 ≤ distanceSq F N := by
  exact sq_nonneg _

/-- The abstract NB error is exactly a `ResearchObligations.ApproximationDatum`. -/
noncomputable def asDatum {X : Type} [PseudoMetricSpace X]
    (F : ApproximationFamily X) : ApproximationDatum where
  error := distanceSq F

/-- The endpoint remains an explicit convergence obligation, not a theorem smuggled
into the definition. -/
def Converges {X : Type} [PseudoMetricSpace X]
    (F : ApproximationFamily X) : Prop :=
  ApproximationConverges (asDatum F)

end MCore.RH.NB
