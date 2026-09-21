import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral

noncomputable section
open MeasureTheory

namespace MCore.Attack.NS.G5Corrected

structure TimeFuncs where
  y : ℝ → ℝ
  z : ℝ → ℝ
  stretch : ℝ → ℝ

structure BalanceIdentity (f : TimeFuncs) (nu : ℝ) where
  identity : ∀ t, (1 / 2 : ℝ) * deriv f.y t + nu * f.z t = f.stretch t

structure G5Raw (f : TimeFuncs) (nu t0 T : ℝ) where
  theta : ℝ
  a : ℝ → ℝ
  htheta_nonneg : 0 ≤ theta
  hineq : ∀ t, t ∈ Set.Ioo t0 T →
    f.stretch t ≤ theta * nu * f.z t + a t * f.y t

def ThetaSubcritical {f : TimeFuncs} {nu t0 T : ℝ}
    (g : G5Raw f nu t0 T) : Prop := g.theta < 1

def DefectL1 {f : TimeFuncs} {nu t0 T : ℝ}
    (g : G5Raw f nu t0 T) : Prop :=
  IntervalIntegrable g.a volume t0 T

structure G5Witness (f : TimeFuncs) (nu t0 T : ℝ)
    extends G5Raw f nu t0 T where
  htheta_lt_one : theta < 1
  haL1 : IntervalIntegrable a volume t0 T

/-- The algebraic G5-3 step only. No claim about z' is used. -/
theorem G5_to_Gronwall
    {f : TimeFuncs} {nu t0 T : ℝ}
    (bal : BalanceIdentity f nu)
    (g : G5Witness f nu t0 T) :
    ∀ t, t ∈ Set.Ioo t0 T →
      deriv f.y t + 2 * (1 - g.theta) * nu * f.z t
        ≤ 2 * g.a t * f.y t := by
  intro t ht
  have h1 := bal.identity t
  have h2 := g.hineq t ht
  linarith

/--
Semantic adapter to the real M-Navier-Stokes definitions.
This M-Core repository does not pretend that its abstract TimeFuncs are already
the concrete maximal-solution trajectory.
-/
structure SemanticAdapter where
  actualNS : Prop
  terminalFlexibleG1 : Prop
  actual_to_balance : actualNS → ∃ (f : TimeFuncs) (nu t0 T : ℝ), BalanceIdentity f nu
  witness_to_terminal :
    (∃ (f : TimeFuncs) (nu t0 T : ℝ), G5Witness f nu t0 T) →
      terminalFlexibleG1

def adapterStatus : String :=
  "OPEN_EXTERNAL_SEMANTIC_MATCH_TO_PINNED_M-NAVIER-STOKES"

def failClosed : List String := [
  "G5-1 theta<1 OPEN_MATH",
  "G5-2 terminal a in L1 OPEN_MATH",
  "G5-3 balance+G5 -> differential inequality PROVED",
  "G5-4 exact Gronwall theorem/match pending",
  "G5-5 critical-control semantic match pending",
  "G5-6 ESS exact hypothesis match pending",
  "M-Core -> real M-Navier-Stokes semantic adapter OPEN"
]

#print axioms G5_to_Gronwall

end MCore.Attack.NS.G5Corrected
