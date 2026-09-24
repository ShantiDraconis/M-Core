import MCore.Real.E
import MCore.Real.RealProducer

namespace MCore.Real

def half : ℝ := (1 : ℝ) / 2

theorem half_bounds : 0 < half ∧ half < 1 := by
  norm_num [half]

/-- Explicit evidence-gated path:
    indeterminate -> resolving(1,1/2) -> resolved(1). -/
def path_I_to_one :
    ResolutionPath E
      .indeterminate
      (.resolved 1) := by
  apply Relation.ReflTransGen.tail
  · exact Relation.ReflTransGen.single
      (ResolutionStep.begin E_one half_bounds)
  · exact ResolutionStep.finish E_one

/-- First genuine inhabitant of the producer type for the concrete criterion E. -/
def realProducer_one : RealProducer E where
  endpoint := 1
  evidence := E_one
  path := path_I_to_one

end MCore.Real
