import MCore.FinalFail.MaterialDerived

namespace MCore.FinalFail.MaterialGeometry

open MCore.FinalFail.MaterialAlgebra
open MCore.FinalFail.MaterialCalculus
open MCore.FinalFail.MaterialDerived

/-!
# Discrete material geometry

This module derives geometry and higher discrete calculus from the already
kernel-checked three-state algebra and seven-lane vector carrier.

It is internal mathematics of the ATK material calculus.  It does not assert
or manufacture an inhabitant of any external open problem.
-/

namespace TriState

/-- Distinguished constants of the three-state carrier. -/
abbrev zeroPhase : TriState := .seed
abbrev unitPhase : TriState := .transit
abbrev conjugatePhase : TriState := .manifest

/-- Rotation operator rho. -/
def rho (x : TriState) : TriState := x.rotate

@[simp] theorem rho_three (x : TriState) :
    rho (rho (rho x)) = x := by
  exact TriState.rotate_three x

theorem rho_ne_self (x : TriState) :
    rho x ≠ x := by
  cases x <;> decide

theorem rho_injective : Function.Injective rho := by
  intro x y h
  cases x <;> cases y <;> simp [rho, TriState.rotate] at h ⊢

theorem rho_surjective : Function.Surjective rho := by
  intro y
  refine ⟨rho (rho y), ?_⟩
  exact rho_three y

/-- Phase difference in the additive three-state group. -/
def delta (x y : TriState) : TriState := x + (-y)

@[simp] theorem delta_self (x : TriState) :
    delta x x = 0 := by
  exact TriState.add_neg x

theorem delta_eq_zero_iff (x y : TriState) :
    delta x y = 0 ↔ x = y := by
  cases x <;> cases y <;> decide

/-- Binary support indicator of a phase. -/
def support : TriState → Nat
  | .seed => 0
  | .transit => 1
  | .manifest => 1

theorem support_le_one (x : TriState) :
    support x ≤ 1 := by
  cases x <;> decide

theorem support_eq_zero_iff (x : TriState) :
    support x = 0 ↔ x = 0 := by
  cases x <;> decide

theorem support_delta_eq_zero_iff (x y : TriState) :
    support (delta x y) = 0 ↔ x = y := by
  rw [support_eq_zero_iff, delta_eq_zero_iff]

end TriState

namespace SevenLaneVector

/-- Coordinatewise phase rotation. -/
def rotate (x : SevenLaneVector) : SevenLaneVector where
  riemann := TriState.rho x.riemann
  beal := TriState.rho x.beal
  pvsnp := TriState.rho x.pvsnp
  navierStokes := TriState.rho x.navierStokes
  hodge := TriState.rho x.hodge
  bsd := TriState.rho x.bsd
  yangMills := TriState.rho x.yangMills

@[simp] theorem rotate_three (x : SevenLaneVector) :
    rotate (rotate (rotate x)) = x := by
  apply SevenLaneVector.extensionality <;>
    simp [rotate, TriState.rho, TriState.rotate_three]

/-- Number of non-seed coordinates. -/
def supportCount (x : SevenLaneVector) : Nat :=
  TriState.support x.riemann +
  TriState.support x.beal +
  TriState.support x.pvsnp +
  TriState.support x.navierStokes +
  TriState.support x.hodge +
  TriState.support x.bsd +
  TriState.support x.yangMills

theorem supportCount_le_seven (x : SevenLaneVector) :
    supportCount x ≤ 7 := by
  have hR := TriState.support_le_one x.riemann
  have hB := TriState.support_le_one x.beal
  have hP := TriState.support_le_one x.pvsnp
  have hN := TriState.support_le_one x.navierStokes
  have hH := TriState.support_le_one x.hodge
  have hD := TriState.support_le_one x.bsd
  have hY := TriState.support_le_one x.yangMills
  unfold supportCount
  omega

@[simp] theorem supportCount_zero :
    supportCount SevenLaneVector.zero = 0 := by
  rfl

/-- Hamming distance on the seven coordinate states. -/
def hamming (x y : SevenLaneVector) : Nat :=
  (if x.riemann = y.riemann then 0 else 1) +
  (if x.beal = y.beal then 0 else 1) +
  (if x.pvsnp = y.pvsnp then 0 else 1) +
  (if x.navierStokes = y.navierStokes then 0 else 1) +
  (if x.hodge = y.hodge then 0 else 1) +
  (if x.bsd = y.bsd then 0 else 1) +
  (if x.yangMills = y.yangMills then 0 else 1)

@[simp] theorem hamming_self (x : SevenLaneVector) :
    hamming x x = 0 := by
  simp [hamming]

theorem hamming_comm (x y : SevenLaneVector) :
    hamming x y = hamming y x := by
  simp [hamming, eq_comm]

theorem hamming_le_seven (x y : SevenLaneVector) :
    hamming x y ≤ 7 := by
  unfold hamming
  split <;> split <;> split <;> split <;> split <;> split <;> split <;> decide

theorem hamming_eq_zero_iff (x y : SevenLaneVector) :
    hamming x y = 0 ↔ x = y := by
  constructor
  · intro h
    unfold hamming at h
    have hr : x.riemann = y.riemann := by
      by_contra hn
      simp [hn] at h
    have hb : x.beal = y.beal := by
      by_contra hn
      simp [hr, hn] at h
    have hp : x.pvsnp = y.pvsnp := by
      by_contra hn
      simp [hr, hb, hn] at h
    have hn : x.navierStokes = y.navierStokes := by
      by_contra hne
      simp [hr, hb, hp, hne] at h
    have hh : x.hodge = y.hodge := by
      by_contra hne
      simp [hr, hb, hp, hn, hne] at h
    have hd : x.bsd = y.bsd := by
      by_contra hne
      simp [hr, hb, hp, hn, hh, hne] at h
    have hy : x.yangMills = y.yangMills := by
      by_contra hne
      simp [hr, hb, hp, hn, hh, hd, hne] at h
    exact SevenLaneVector.extensionality hr hb hp hn hh hd hy
  · intro h
    subst y
    exact hamming_self x

/-- Global phase rotation preserves Hamming distance. -/
theorem hamming_rotate (x y : SevenLaneVector) :
    hamming (rotate x) (rotate y) = hamming x y := by
  unfold hamming rotate
  simp only [TriState.rho]
  have hiff : ∀ a b : TriState, a.rotate = b.rotate ↔ a = b := by
    intro a b
    constructor
    · exact TriState.rho_injective
    · intro h
      rw [h]
  simp [hiff]

end SevenLaneVector

namespace EvidenceState

/-- Second discrete derivative of a time-indexed evidence trajectory. -/
def secondDerivative (f : Nat → EvidenceState) (n : Nat) : Int :=
  derivative f (n + 1) - derivative f n

theorem secondDerivative_bounds
    (f : Nat → EvidenceState) (n : Nat) :
    -4 ≤ secondDerivative f n ∧ secondDerivative f n ≤ 4 := by
  have h1 := derivative_bounds f (n + 1)
  have h0 := derivative_bounds f n
  unfold secondDerivative
  omega

/-- A locally constant three-point evidence trajectory has zero second derivative. -/
theorem secondDerivative_eq_zero_of_local_constant
    (f : Nat → EvidenceState) (n : Nat)
    (h01 : f (n + 1) = f n)
    (h12 : f (n + 2) = f (n + 1)) :
    secondDerivative f n = 0 := by
  unfold secondDerivative
  have h0 : derivative f n = 0 :=
    (derivative_eq_zero_iff_state_stable f n).2 h01
  have h1 : derivative f (n + 1) = 0 := by
    apply (derivative_eq_zero_iff_state_stable f (n + 1)).2
    simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using h12
  rw [h0, h1]
  simp

/-- Evidence jump magnitude. -/
def jumpMagnitude (f : Nat → EvidenceState) (n : Nat) : Nat :=
  Int.natAbs (derivative f n)

theorem jumpMagnitude_le_two
    (f : Nat → EvidenceState) (n : Nat) :
    jumpMagnitude f n ≤ 2 := by
  have h := derivative_bounds f n
  unfold jumpMagnitude
  omega

end EvidenceState

#print axioms MCore.FinalFail.MaterialGeometry.TriState.rho_three
#print axioms MCore.FinalFail.MaterialGeometry.TriState.delta_eq_zero_iff
#print axioms MCore.FinalFail.MaterialGeometry.SevenLaneVector.supportCount_le_seven
#print axioms MCore.FinalFail.MaterialGeometry.SevenLaneVector.hamming_eq_zero_iff
#print axioms MCore.FinalFail.MaterialGeometry.SevenLaneVector.hamming_rotate
#print axioms MCore.FinalFail.MaterialGeometry.EvidenceState.secondDerivative_bounds

end MCore.FinalFail.MaterialGeometry
