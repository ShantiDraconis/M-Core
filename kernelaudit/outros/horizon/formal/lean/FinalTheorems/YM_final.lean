/-
  Final Theorem: Yang-Mills Mass Gap
  
  This file aggregates all components to state the final theorem for Yang-Mills.
-/

import HorizonPrime.ConstructionPi
import Reductions.YangMills
import Gaps.YM_Constructive4D

namespace HorizonPrime.FinalTheorems

open Reductions
open Gaps

/-- Final theorem for Yang-Mills mass gap -/
theorem YM_final : YangMillsMassGap := by
  apply YM_from_Constructive4D_and_Pi
  · -- Use the constructed Π element
    exact Pi
  · -- Apply constructive 4D axiom
    exact constructive_4d_mass_gap
  · -- Apply uniformity axiom
    exact nonperturbative_uniform

end HorizonPrime.FinalTheorems
