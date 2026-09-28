import MCore.FinalFail.Semantic.BSD
import Mathlib.AlgebraicGeometry.EllipticCurve.LFunction

namespace MCore.FinalFail.Semantic

/-!
# BSD canonical domain binding

This file closes only the domain-binding part of the BSD semantic frontier.
A BSD object here is an actual Weierstrass elliptic curve over Q, using the
Mathlib ellipticity predicate, and its analytic side is anchored to Mathlib's
actual WeierstrassCurve.LSeries.

No Mordell--Weil rank, analytic order at s=1, regulator, Tamagawa product,
Tate--Shafarevich order, or refined BSD identity is manufactured here.
-/

/-- Genuine elliptic-curve domain over Q.  Unlike the old pair-of-naturals
audit interface, an inhabitant carries an actual Mathlib Weierstrass curve and
a proof that its discriminant is a unit. -/
structure BSDCanonicalCurveQ where
  curve : WeierstrassCurve ℚ
  elliptic : curve.IsElliptic

/-- The genuine L-series attached by Mathlib to the same curve object. -/
noncomputable def BSDCanonicalCurveQ.lSeries
    (E : BSDCanonicalCurveQ) (s : ℂ) : ℂ :=
  E.curve.LSeries s

/-- Remaining arithmetic/analytic invariant binding.  These fields are kept
separate precisely because Mathlib currently supplies the curve and L-series
objects but not an integrated Mordell--Weil/analytic-rank/Sha/Tamagawa package
for BSD.  Inhabiting this structure is therefore still material work. -/
structure BSDInvariantBinding where
  analyticOrderAtOne : BSDCanonicalCurveQ → Nat
  mordellWeilRank : BSDCanonicalCurveQ → Nat
  refinedFormula : BSDCanonicalCurveQ → Prop
  shaFinite : BSDCanonicalCurveQ → Prop

/-- Once genuine invariant bindings are supplied, the remaining BSD producer is
exactly rank equality plus refined identity and Sha finiteness on every actual
elliptic curve in the same domain. -/
structure BSDCanonicalProducer (B : BSDInvariantBinding) where
  rankEquality :
    ∀ E : BSDCanonicalCurveQ,
      B.analyticOrderAtOne E = B.mordellWeilRank E
  refined :
    ∀ E : BSDCanonicalCurveQ, B.refinedFormula E
  shaFiniteness :
    ∀ E : BSDCanonicalCurveQ, B.shaFinite E

/-- Administrative projection to the generic semantic target.  This does not
create the missing binding or producer; it only ties the generic target to the
canonical Q-elliptic domain. -/
def BSDCanonicalProducer.toGenericTarget
    (B : BSDInvariantBinding)
    (P : BSDCanonicalProducer B) :
    BSDRealizableTarget BSDCanonicalCurveQ
      (fun _ => True)
      (fun E => Int.ofNat (B.analyticOrderAtOne E))
      (fun E => Int.ofNat (B.mordellWeilRank E))
      (fun E => B.refinedFormula E ∧ B.shaFinite E) := {
  rankEquality := by
    intro E _
    exact congrArg Int.ofNat (P.rankEquality E)
  refined := by
    intro E _
    exact ⟨P.refined E, P.shaFiniteness E⟩
}

end MCore.FinalFail.Semantic
