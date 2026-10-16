/-
  Final Theorem: P vs NP
  
  This file aggregates all components to state the final theorem for P ≠ NP.
-/

import HorizonPrime.ConstructionPi
import Reductions.PvsNP
import Gaps.PvsNP_CircuitLB

namespace HorizonPrime.FinalTheorems

open Reductions
open Gaps

/-- Final theorem for P ≠ NP -/
theorem PneqNP_final : PneqNP := by
  apply PneqNP_from_CircuitLB_and_Pi
  · -- Use the constructed Π element
    exact Pi
  · -- Apply circuit lower bound axiom
    exact circuit_lower_bound_strong

end HorizonPrime.FinalTheorems
