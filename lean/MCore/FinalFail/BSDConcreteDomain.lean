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

/-- Counter-audit object: merely attaching two natural numbers to a genuine
curve is still too weak to represent BSD rank data. -/
structure BSDNaiveRankPair (E : EllipticCurveQ) where
  analyticOrderAtOne : Nat
  mordellWeilRank : Nat

/-- The naive rank-pair interface is trivially inhabited for every genuine
curve, so its inhabitance cannot count as BSD progress. -/
def trivialBSDNaiveRankPair (E : EllipticCurveQ) : BSDNaiveRankPair E where
  analyticOrderAtOne := 0
  mordellWeilRank := 0

theorem naiveRankPair_is_trivially_inhabited (E : EllipticCurveQ) :
    Nonempty (BSDNaiveRankPair E) :=
  ⟨trivialBSDNaiveRankPair E⟩

/-!
Remaining material BSD binding:

* define/certify the actual Mordell--Weil rank of E(Q);
* construct/certify analytic continuation of E.LSeries to s = 1 and its
  order of vanishing there;
* bind the refined arithmetic factors (period, regulator, Sha, Tamagawa,
  torsion) to the same curve and convention;
* then prove the rank and refined identities.

No structure in this file supplies those facts.
-/


end MCore.FinalFail.Semantic
