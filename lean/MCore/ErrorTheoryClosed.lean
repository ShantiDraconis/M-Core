import Mathlib

namespace MCore.ErrorClosed

noncomputable def E_total (ws gs : List ℝ) : ℝ :=
  (ws.zip gs).foldl (fun a p => a + p.1 * p.2) 0

noncomputable def C_i (w gd E : ℝ) : ℝ := 100 * w * gd / E

structure ErrorInvarianceTargets where
  normInv : Prop
  reparamInv : Prop
  E_zero : Prop
  stability : Prop
  counterexamples : Prop

def status : String := "OPEN_FORMALIZATION_NO_PROMOTION"

end MCore.ErrorClosed
