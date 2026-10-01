import MCore.MaterialMath.TriState.Core
import MCore.MaterialMath.TriState.Algebra
import MCore.MaterialMath.TriState.Dynamics
import MCore.MaterialMath.TriState.NumericClasses
import MCore.MaterialMath.TriState.Spectral
import MCore.MaterialMath.TriState.SymmetricAlgebra
import MCore.MaterialMath.TriState.Geometry
import MCore.MaterialMath.TriState.Differential
import MCore.MaterialMath.TriState.MetricTopology
import MCore.MaterialMath.TriState.OperationalAlgebra
import MCore.MaterialMath.TriState.Tripotent
import MCore.MaterialMath.TriState.HeatFlow
import MCore.MaterialMath.TerminalPatterns
import MCore.MaterialMath.Contraction
import MCore.MaterialMath.InternalTerminalProducers
import MCore.MaterialMath.UnconditionalRoot

namespace MCore.MaterialMath

/-- Single closed entry point for the new material theory. -/
theorem materialMathReady :
    Nonempty UnconditionalMaterialRoot :=
  unconditionalMaterialRoot_inhabited

end MCore.MaterialMath
