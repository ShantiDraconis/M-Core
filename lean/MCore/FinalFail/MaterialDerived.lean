import MCore.FinalFail.MaterialAlgebra
import MCore.FinalFail.MaterialProducerCalculus

namespace MCore.FinalFail.MaterialDerived

open MCore.FinalFail.MaterialAlgebra
open MCore.FinalFail.MaterialCalculus

/-!
# Derived material arithmetic and topology

Everything in this file is derived from the already-kernel-checked finite
algebras in MaterialAlgebra and MaterialProducerCalculus.

No theorem here constructs an inhabitant of RH, Beal, P vs NP, Navier--Stokes,
Hodge, BSD, or Yang--Mills.  These are internal algebraic laws of the ATK
bookkeeping/material calculus.
-/

/-! ## 1. TriState arithmetic laws -/

namespace TriState

/-- Canonical finite code 0,1,2. -/
def code : TriState → Nat
  | .seed => 0
  | .transit => 1
  | .manifest => 2

theorem code_lt_three (x : TriState) : code x < 3 := by
  cases x <;> decide

theorem code_injective : Function.Injective code := by
  intro x y h
  cases x <;> cases y <;> simp [code] at h ⊢

/-- Addition agrees with addition modulo three at the level of the code. -/
theorem code_add_mod_three (x y : TriState) :
    code (x + y) = (code x + code y) % 3 := by
  cases x <;> cases y <;> decide

/-- Multiplication agrees with multiplication modulo three at the level of the code. -/
theorem code_mul_mod_three (x y : TriState) :
    code (x * y) = (code x * code y) % 3 := by
  cases x <;> cases y <;> decide

@[simp] theorem transit_add_transit :
    (.transit : TriState) + .transit = .manifest := rfl

@[simp] theorem manifest_add_transit :
    (.manifest : TriState) + .transit = .seed := rfl

@[simp] theorem manifest_add_manifest :
    (.manifest : TriState) + .manifest = .transit := rfl

/-- Additive characteristic three. -/
theorem characteristic_three (x : TriState) :
    (x + x) + x = .seed := by
  cases x <;> rfl

/-- Frobenius identity in the three-element table. -/
theorem frobenius_three (x : TriState) :
    (x * x) * x = x :=
  cubic_idempotence x

/-- There are no nonzero zero divisors. -/
theorem mul_eq_zero_iff (x y : TriState) :
    x * y = 0 ↔ x = 0 ∨ y = 0 := by
  cases x <;> cases y <;> simp [TriState.mul]

/-- Cancellation by a nonzero factor. -/
theorem mul_left_cancel_nonzero
    {a b c : TriState} (ha : a ≠ 0)
    (h : a * b = a * c) :
    b = c := by
  cases a <;> cases b <;> cases c <;> simp [TriState.mul] at ha h ⊢

/-- Every nonzero element is its own inverse. -/
theorem inv_eq_self (x : TriState) :
    x⁻¹ = x := by
  cases x <;> rfl

/-- The multiplicative group of nonzero states has exponent two. -/
theorem nonzero_mul_self
    (x : TriState) (hx : x ≠ 0) :
    x * x = 1 :=
  nonzero_square_eq_one x hx

/-- Rotation is translation by one state. -/
theorem rotate_eq_add_one (x : TriState) :
    x.rotate = x + .transit := by
  cases x <;> rfl

/-- Two rotations translate by manifest (=2 mod 3). -/
theorem rotate_twice_eq_add_manifest (x : TriState) :
    x.rotate.rotate = x + .manifest := by
  cases x <;> rfl

/-- Rotation commutes with additive translation. -/
theorem rotate_add (x y : TriState) :
    (x + y).rotate = x.rotate + y := by
  cases x <;> cases y <;> rfl

end TriState

/-! ## 2. Seven-lane vector arithmetic -/

namespace SevenLaneVector

def neg (x : SevenLaneVector) : SevenLaneVector where
  riemann := -x.riemann
  beal := -x.beal
  pvsnp := -x.pvsnp
  navierStokes := -x.navierStokes
  hodge := -x.hodge
  bsd := -x.bsd
  yangMills := -x.yangMills

instance : Neg SevenLaneVector where
  neg := neg

def smul (a : TriState) (x : SevenLaneVector) : SevenLaneVector where
  riemann := a * x.riemann
  beal := a * x.beal
  pvsnp := a * x.pvsnp
  navierStokes := a * x.navierStokes
  hodge := a * x.hodge
  bsd := a * x.bsd
  yangMills := a * x.yangMills

@[simp] theorem add_neg (x : SevenLaneVector) :
    x + (-x) = SevenLaneVector.zero := by
  apply SevenLaneVector.extensionality <;>
    simp [SevenLaneVector.neg, SevenLaneVector.add, TriState.add_neg]

theorem smul_add (a : TriState) (x y : SevenLaneVector) :
    smul a (x + y) = smul a x + smul a y := by
  apply SevenLaneVector.extensionality <;>
    simp [smul, SevenLaneVector.add, TriState.left_distrib]

theorem add_smul (a b : TriState) (x : SevenLaneVector) :
    smul (a + b) x = smul a x + smul b x := by
  apply SevenLaneVector.extensionality <;>
    simp [smul, SevenLaneVector.add, TriState.right_distrib]

theorem smul_assoc (a b : TriState) (x : SevenLaneVector) :
    smul (a * b) x = smul a (smul b x) := by
  apply SevenLaneVector.extensionality <;>
    simp [smul, TriState.mul_assoc]

@[simp] theorem one_smul (x : SevenLaneVector) :
    smul 1 x = x := by
  apply SevenLaneVector.extensionality <;>
    simp [smul]

@[simp] theorem zero_smul (x : SevenLaneVector) :
    smul 0 x = SevenLaneVector.zero := by
  apply SevenLaneVector.extensionality <;>
    simp [smul, SevenLaneVector.zero]

/-- Coordinatewise cubic law inherited from TriState. -/
theorem cubic_scalar_identity (a : TriState) (x : SevenLaneVector) :
    smul ((a * a) * a) x = smul a x := by
  rw [TriState.cubic_idempotence]

end SevenLaneVector

/-! ## 3. Evidence order, closure, interior, and boundary -/

namespace EvidenceState

/-- The order used by the evidence topology is exactly the code order. -/
theorem le_iff_code_le (a b : EvidenceState) :
    a ≤ b ↔ code a ≤ code b := Iff.rfl

/-- Downward closure associated with the upward-open evidence topology. -/
def closure (S : EvidenceState → Prop) : EvidenceState → Prop :=
  fun x => ∃ y, S y ∧ code x ≤ code y

/-- Interior associated with the upward-open evidence topology. -/
def interior (S : EvidenceState → Prop) : EvidenceState → Prop :=
  fun x => S x ∧ ∀ y, code x ≤ code y → S y

/-- Boundary = closure minus interior. -/
def boundary (S : EvidenceState → Prop) : EvidenceState → Prop :=
  fun x => closure S x ∧ ¬ interior S x

theorem subset_closure (S : EvidenceState → Prop) :
    ∀ x, S x → closure S x := by
  intro x hx
  exact ⟨x, hx, le_rfl⟩

theorem interior_subset (S : EvidenceState → Prop) :
    ∀ x, interior S x → S x := by
  intro x hx
  exact hx.1

theorem closure_monotone
    {S T : EvidenceState → Prop}
    (hST : ∀ x, S x → T x) :
    ∀ x, closure S x → closure T x := by
  intro x hx
  rcases hx with ⟨y, hy, hxy⟩
  exact ⟨y, hST y hy, hxy⟩

theorem interior_monotone
    {S T : EvidenceState → Prop}
    (hST : ∀ x, S x → T x) :
    ∀ x, interior S x → interior T x := by
  intro x hx
  refine ⟨hST x hx.1, ?_⟩
  intro y hxy
  exact hST y (hx.2 y hxy)

theorem closure_idempotent (S : EvidenceState → Prop) :
    ∀ x, closure (closure S) x ↔ closure S x := by
  intro x
  constructor
  · rintro ⟨y, ⟨z, hz, hyz⟩, hxy⟩
    exact ⟨z, hz, le_trans hxy hyz⟩
  · intro hx
    rcases hx with ⟨y, hy, hxy⟩
    exact ⟨y, ⟨y, hy, le_rfl⟩, hxy⟩

theorem interior_idempotent (S : EvidenceState → Prop) :
    ∀ x, interior (interior S) x ↔ interior S x := by
  intro x
  constructor
  · intro hx
    exact hx.1
  · intro hx
    refine ⟨hx, ?_⟩
    intro y hxy
    refine ⟨hx.2 y hxy, ?_⟩
    intro z hyz
    exact hx.2 z (le_trans hxy hyz)

theorem proven_closure_all (x : EvidenceState) :
    closure ProvenNeighborhood x := by
  refine ⟨.proved, rfl, ?_⟩
  cases x <;> decide

theorem proven_interior_iff (x : EvidenceState) :
    interior ProvenNeighborhood x ↔ x = .proved := by
  cases x <;> simp [interior, ProvenNeighborhood, code]

theorem proven_boundary_iff_not_proved (x : EvidenceState) :
    boundary ProvenNeighborhood x ↔ x ≠ .proved := by
  rw [boundary]
  constructor
  · intro h hx
    subst x
    exact h.2 ((proven_interior_iff .proved).2 rfl)
  · intro hx
    exact ⟨proven_closure_all x, fun hi => hx ((proven_interior_iff x).1 hi)⟩

end EvidenceState

/-! ## 4. Producer/refuter polarity operators -/

/-- Negation swaps producer and refuter roles exactly. -/
def negateProducer {P : Prop}
    (p : MaterialProducer P) : MaterialRefuter (¬ P) :=
  ⟨fun hNot => hNot p.produce⟩

def negateRefuter {P : Prop}
    (r : MaterialRefuter P) : MaterialProducer (¬ P) :=
  ⟨r.refute⟩

theorem negate_refuter_producer_roundtrip
    {P : Prop} (r : MaterialRefuter P) :
    (negateRefuter r).produce = r.refute := rfl

/-- A proved proposition maps to proved evidence; a refuter maps to refuted evidence.
Open is deliberately not synthesized from absence of either object. -/
def evidenceOfProducer {P : Prop} (_ : MaterialProducer P) : EvidenceState :=
  .proved

def evidenceOfRefuter {P : Prop} (_ : MaterialRefuter P) : EvidenceState :=
  .refuted

@[simp] theorem evidenceOfProducer_eq_proved
    {P : Prop} (p : MaterialProducer P) :
    evidenceOfProducer p = .proved := rfl

@[simp] theorem evidenceOfRefuter_eq_refuted
    {P : Prop} (r : MaterialRefuter P) :
    evidenceOfRefuter r = .refuted := rfl

#print axioms MCore.FinalFail.MaterialDerived.TriState.code_add_mod_three
#print axioms MCore.FinalFail.MaterialDerived.TriState.mul_eq_zero_iff
#print axioms MCore.FinalFail.MaterialDerived.TriState.rotate_eq_add_one
#print axioms MCore.FinalFail.MaterialDerived.SevenLaneVector.smul_add
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.closure_idempotent
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.interior_idempotent
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.proven_boundary_iff_not_proved
#print axioms MCore.FinalFail.MaterialDerived.negateProducer

end MCore.FinalFail.MaterialDerived
