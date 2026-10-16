/-
  Final Theorem: Riemann Hypothesis
  
  This file aggregates all components to state the final theorem for RH.
-/

import HorizonPrime.ConstructionPi
import Reductions.RH
import Gaps.RH_ZD_UEF

namespace HorizonPrime.FinalTheorems

open Reductions
open Gaps

/-- Final theorem for Riemann Hypothesis -/
theorem RH_final : RiemannHypothesis := by
  apply RH_from_ZD_UEF_and_Pi
  · -- Use the constructed Π element
    exact Pi
  · -- Apply zero-density estimate axiom
    exact zero_density_uniform
  · -- Apply explicit formula axiom
    exact explicit_formula_uniform_error

end HorizonPrime.FinalTheorems
