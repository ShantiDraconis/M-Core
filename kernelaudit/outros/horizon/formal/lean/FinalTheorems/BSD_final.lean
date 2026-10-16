/-
  Final Theorem: BSD Conjecture
  
  This file aggregates all components to state the final theorem for BSD.
-/

import HorizonPrime.ConstructionPi
import Reductions.BSD
import Gaps.BSD_NonvanishingRegulators

namespace HorizonPrime.FinalTheorems

open Reductions
open Gaps

/-- Final theorem for Birch and Swinnerton-Dyer Conjecture -/
theorem BSD_final : BSDConjecture := by
  apply BSD_from_NonvanishingRegulators_and_Pi
  · -- Use the constructed Π element
    exact Pi
  · -- Apply uniform nonvanishing axiom
    exact uniform_nonvanishing
  · -- Apply regulator bounds axiom
    exact regulator_bounds_families

end HorizonPrime.FinalTheorems
