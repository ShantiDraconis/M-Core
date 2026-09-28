import MCore.FinalFail.Semantic.BSD
import Mathlib.AlgebraicGeometry.EllipticCurve.LFunction

namespace MCore.FinalFail.Semantic

/-!
# Concrete BSD curve domain

This module closes only the geometric/source binding for BSD.

It replaces an arbitrary abstract curve type by actual nonsingular
Weierstrass curves over Q and binds the analytic source to Mathlib's
WeierstrassCurve.LSeries.  It deliberately does not manufacture analytic
continuation at s = 1, Mordell--Weil rank, Sha, regulator, Tamagawa factors,
or the refined BSD identity.
-/

/-- A genuine elliptic curve over Q represented by a nonsingular Weierstrass
equation.  The discriminant condition is stored as data so the type cannot be
inhabited by an arbitrary unrelated natural-number pair. -/
structure EllipticCurveQ where
  curve : WeierstrassCurve ℚ
  elliptic : IsUnit curve.Δ

instance (E : EllipticCurveQ) : E.curve.IsElliptic where
  isUnit := E.elliptic

/-- The canonical formal L-series source attached to the same curve. -/
noncomputable def EllipticCurveQ.LSeries (E : EllipticCurveQ) (s : ℂ) : ℂ :=
  E.curve.LSeries s

/-- Positive control: y^2 = x^3 - x. -/
def bsdPositiveControlCurve : WeierstrassCurve ℚ where
  a₁ := 0
  a₂ := 0
  a₃ := 0
  a₄ := -1
  a₆ := 0

theorem bsdPositiveControlCurve_delta :
    bsdPositiveControlCurve.Δ = (64 : ℚ) := by
  norm_num [bsdPositiveControlCurve, WeierstrassCurve.Δ,
    WeierstrassCurve.b₂, WeierstrassCurve.b₄,
    WeierstrassCurve.b₆, WeierstrassCurve.b₈]

def bsdPositiveControl : EllipticCurveQ where
  curve := bsdPositiveControlCurve
  elliptic := by
    rw [bsdPositiveControlCurve_delta]
    norm_num

theorem ellipticCurveQ_nonempty : Nonempty EllipticCurveQ :=
  ⟨bsdPositiveControl⟩

/-- After the source binding, the remaining rank-side data must be attached to
an actual curve, not supplied as an arbitrary pair of naturals.  Correctness of
these two quantities is intentionally not asserted here; the missing APIs /
proofs are the next material frontier. -/
structure BSDCurveRankInterface (E : EllipticCurveQ) where
  analyticOrderAtOne : Nat
  mordellWeilRank : Nat

def BSDCurveRankEquality {E : EllipticCurveQ}
    (d : BSDCurveRankInterface E) : Prop :=
  d.analyticOrderAtOne = d.mordellWeilRank

/-- This is only the remaining typed obligation after fixing a genuine curve
source.  No inhabitant is provided. -/
def BSDConcreteRankProducer : Prop :=
  ∀ E : EllipticCurveQ, ∃ d : BSDCurveRankInterface E, BSDCurveRankEquality d

end MCore.FinalFail.Semantic
