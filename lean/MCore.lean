import MCore.FinalProofFirewall

/-!
Root module for the Lake library declared with `srcDir := "lean"`.

Keeping this file inside `lean/` makes the default `lake build` target resolve
correctly while the repository-level `MCore.lean` remains provenance.
-/

import MCore.MaterialMath.TriStateTerminalClosure

import MCore.MaterialMath.TransverseContraction

import MCore.MaterialMath.ScalarDefectEmbedding

import MCore.MaterialMath.ProfiledTransverseDecay

import MCore.MaterialMath.TwoSidedMaterialResolution

import MCore.MaterialMath.GlobalMaterialTheorem
import MCore.MaterialMath.GlobalOpenMathLogic
import MCore.MaterialMath.TorsionEnergyLaw