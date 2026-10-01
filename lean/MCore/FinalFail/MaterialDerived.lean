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


/-! ## 1b. Symbolic constants and subtraction -/

/-- Canonical symbolic names for the three structural states. -/
abbrev SeedConstant : TriState := .seed
abbrev TransitConstant : TriState := .transit
abbrev ManifestConstant : TriState := .manifest

/-- Subtraction in the cyclic additive group. -/
def sub (x y : TriState) : TriState := x + (-y)

instance : Sub TriState where
  sub := sub

@[simp] theorem sub_self (x : TriState) :
    x - x = .seed := by
  cases x <;> rfl

@[simp] theorem sub_seed (x : TriState) :
    x - .seed = x := by
  cases x <;> rfl

theorem sub_eq_add_neg (x y : TriState) :
    x - y = x + (-y) := rfl

/-- One rotation is the discrete +1 translation. -/
theorem orbit_step (x : TriState) :
    x.rotate - x = .transit := by
  cases x <;> rfl

/-- Two successive rotations accumulate the manifest (=2 mod 3) displacement. -/
theorem orbit_two_step (x : TriState) :
    x.rotate.rotate - x = .manifest := by
  cases x <;> rfl

/-- Three rotations have zero net displacement. -/
theorem orbit_three_step (x : TriState) :
    x.rotate.rotate.rotate - x = .seed := by
  rw [TriState.rotate_three]
  exact sub_self x

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
  apply SevenLaneVector.extensionality
  · change a * (x.riemann + y.riemann) = a * x.riemann + a * y.riemann
    exact TriState.left_distrib _ _ _
  · change a * (x.beal + y.beal) = a * x.beal + a * y.beal
    exact TriState.left_distrib _ _ _
  · change a * (x.pvsnp + y.pvsnp) = a * x.pvsnp + a * y.pvsnp
    exact TriState.left_distrib _ _ _
  · change a * (x.navierStokes + y.navierStokes) =
      a * x.navierStokes + a * y.navierStokes
    exact TriState.left_distrib _ _ _
  · change a * (x.hodge + y.hodge) = a * x.hodge + a * y.hodge
    exact TriState.left_distrib _ _ _
  · change a * (x.bsd + y.bsd) = a * x.bsd + a * y.bsd
    exact TriState.left_distrib _ _ _
  · change a * (x.yangMills + y.yangMills) =
      a * x.yangMills + a * y.yangMills
    exact TriState.left_distrib _ _ _

theorem add_smul (a b : TriState) (x : SevenLaneVector) :
    smul (a + b) x = smul a x + smul b x := by
  apply SevenLaneVector.extensionality
  · change (a + b) * x.riemann = a * x.riemann + b * x.riemann
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.beal = a * x.beal + b * x.beal
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.pvsnp = a * x.pvsnp + b * x.pvsnp
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.navierStokes =
      a * x.navierStokes + b * x.navierStokes
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.hodge = a * x.hodge + b * x.hodge
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.bsd = a * x.bsd + b * x.bsd
    exact TriState.right_distrib _ _ _
  · change (a + b) * x.yangMills =
      a * x.yangMills + b * x.yangMills
    exact TriState.right_distrib _ _ _

theorem smul_assoc (a b : TriState) (x : SevenLaneVector) :
    smul (a * b) x = smul a (smul b x) := by
  apply SevenLaneVector.extensionality
  · change (a * b) * x.riemann = a * (b * x.riemann)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.beal = a * (b * x.beal)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.pvsnp = a * (b * x.pvsnp)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.navierStokes = a * (b * x.navierStokes)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.hodge = a * (b * x.hodge)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.bsd = a * (b * x.bsd)
    exact TriState.mul_assoc _ _ _
  · change (a * b) * x.yangMills = a * (b * x.yangMills)
    exact TriState.mul_assoc _ _ _

@[simp] theorem one_smul (x : SevenLaneVector) :
    smul 1 x = x := by
  apply SevenLaneVector.extensionality
  · change (1 : TriState) * x.riemann = x.riemann
    exact TriState.one_mul _
  · change (1 : TriState) * x.beal = x.beal
    exact TriState.one_mul _
  · change (1 : TriState) * x.pvsnp = x.pvsnp
    exact TriState.one_mul _
  · change (1 : TriState) * x.navierStokes = x.navierStokes
    exact TriState.one_mul _
  · change (1 : TriState) * x.hodge = x.hodge
    exact TriState.one_mul _
  · change (1 : TriState) * x.bsd = x.bsd
    exact TriState.one_mul _
  · change (1 : TriState) * x.yangMills = x.yangMills
    exact TriState.one_mul _

@[simp] theorem zero_smul (x : SevenLaneVector) :
    smul 0 x = SevenLaneVector.zero := by
  apply SevenLaneVector.extensionality
  · change (0 : TriState) * x.riemann = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.beal = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.pvsnp = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.navierStokes = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.hodge = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.bsd = (0 : TriState)
    exact TriState.zero_mul _
  · change (0 : TriState) * x.yangMills = (0 : TriState)
    exact TriState.zero_mul _

/-- Coordinatewise cubic law inherited from TriState. -/
theorem cubic_scalar_identity (a : TriState) (x : SevenLaneVector) :
    smul ((a * a) * a) x = smul a x := by
  rw [TriState.cubic_idempotence]

end SevenLaneVector

/-! ## 3. Evidence order, closure, interior, and boundary -/

namespace EvidenceState

private abbrev ecode : MaterialCalculus.EvidenceState → Int :=
  MaterialCalculus.EvidenceState.code

/-- The order used by the evidence topology is exactly the imported code order. -/
theorem le_iff_code_le (a b : MaterialCalculus.EvidenceState) :
    a ≤ b ↔ ecode a ≤ ecode b := Iff.rfl

/-- Downward closure associated with the upward-open evidence topology. -/
def closure (S : MaterialCalculus.EvidenceState → Prop) :
    MaterialCalculus.EvidenceState → Prop :=
  fun x => ∃ y, S y ∧ ecode x ≤ ecode y

/-- Interior associated with the upward-open evidence topology. -/
def interior (S : MaterialCalculus.EvidenceState → Prop) :
    MaterialCalculus.EvidenceState → Prop :=
  fun x => S x ∧ ∀ y, ecode x ≤ ecode y → S y

/-- Boundary = closure minus interior. -/
def boundary (S : MaterialCalculus.EvidenceState → Prop) :
    MaterialCalculus.EvidenceState → Prop :=
  fun x => closure S x ∧ ¬ interior S x

theorem subset_closure
    (S : MaterialCalculus.EvidenceState → Prop) :
    ∀ x, S x → closure S x := by
  intro x hx
  exact ⟨x, hx, le_rfl⟩

theorem interior_subset
    (S : MaterialCalculus.EvidenceState → Prop) :
    ∀ x, interior S x → S x := by
  intro x hx
  change S x ∧ (∀ y, ecode x ≤ ecode y → S y) at hx
  exact hx.1

theorem closure_monotone
    {S T : MaterialCalculus.EvidenceState → Prop}
    (hST : ∀ x, S x → T x) :
    ∀ x, closure S x → closure T x := by
  intro x hx
  rcases hx with ⟨y, hy, hxy⟩
  exact ⟨y, hST y hy, hxy⟩

theorem interior_monotone
    {S T : MaterialCalculus.EvidenceState → Prop}
    (hST : ∀ x, S x → T x) :
    ∀ x, interior S x → interior T x := by
  intro x hx
  change S x ∧ (∀ y, ecode x ≤ ecode y → S y) at hx
  change T x ∧ (∀ y, ecode x ≤ ecode y → T y)
  refine ⟨hST x hx.1, ?_⟩
  intro y hxy
  exact hST y (hx.2 y hxy)

theorem closure_idempotent
    (S : MaterialCalculus.EvidenceState → Prop) :
    ∀ x, closure (closure S) x ↔ closure S x := by
  intro x
  constructor
  · rintro ⟨y, ⟨z, hz, hyz⟩, hxy⟩
    exact ⟨z, hz, le_trans hxy hyz⟩
  · rintro ⟨y, hy, hxy⟩
    exact ⟨y, ⟨y, hy, le_rfl⟩, hxy⟩

theorem interior_idempotent
    (S : MaterialCalculus.EvidenceState → Prop) :
    ∀ x, interior (interior S) x ↔ interior S x := by
  intro x
  constructor
  · intro hx
    change interior S x ∧
      (∀ y, ecode x ≤ ecode y → interior S y) at hx
    exact hx.1
  · intro hx
    change S x ∧ (∀ y, ecode x ≤ ecode y → S y) at hx
    change interior S x ∧
      (∀ y, ecode x ≤ ecode y → interior S y)
    refine ⟨?_, ?_⟩
    · exact hx
    · intro y hxy
      change S y ∧ (∀ z, ecode y ≤ ecode z → S z)
      refine ⟨hx.2 y hxy, ?_⟩
      intro z hyz
      exact hx.2 z (le_trans hxy hyz)

private def ProvenNeighborhood :
    MaterialCalculus.EvidenceState → Prop :=
  fun s => s = .proved

theorem proven_closure_all
    (x : MaterialCalculus.EvidenceState) :
    closure ProvenNeighborhood x := by
  refine ⟨.proved, rfl, ?_⟩
  cases x <;> decide

theorem proven_interior_iff
    (x : MaterialCalculus.EvidenceState) :
    interior ProvenNeighborhood x ↔ x = .proved := by
  cases x <;>
    simp [interior, ProvenNeighborhood, ecode, MaterialCalculus.EvidenceState.code]

theorem proven_boundary_iff_not_proved
    (x : MaterialCalculus.EvidenceState) :
    boundary ProvenNeighborhood x ↔ x ≠ .proved := by
  unfold boundary
  constructor
  · intro h hx
    subst x
    exact h.2 ((proven_interior_iff .proved).2 rfl)
  · intro hx
    exact ⟨proven_closure_all x,
      fun hi => hx ((proven_interior_iff x).1 hi)⟩


/-! ## 3b. Sign laws for the discrete evidence derivative -/

theorem derivative_pos_iff_code_increases
    (f : Nat → EvidenceState) (n : Nat) :
    0 < derivative f n ↔ code (f n) < code (f (n + 1)) := by
  unfold derivative
  omega

theorem derivative_neg_iff_code_decreases
    (f : Nat → EvidenceState) (n : Nat) :
    derivative f n < 0 ↔ code (f (n + 1)) < code (f n) := by
  unfold derivative
  omega

theorem derivative_nonneg_of_monotone_step
    (f : Nat → EvidenceState) (n : Nat)
    (h : code (f n) ≤ code (f (n + 1))) :
    0 ≤ derivative f n := by
  unfold derivative
  omega

theorem derivative_nonpos_of_antitone_step
    (f : Nat → EvidenceState) (n : Nat)
    (h : code (f (n + 1)) ≤ code (f n)) :
    derivative f n ≤ 0 := by
  unfold derivative
  omega

/-- Two-step telescoping law for the evidence derivative. -/
theorem derivative_two_step
    (f : Nat → EvidenceState) (n : Nat) :
    derivative f n + derivative f (n + 1) =
      code (f (n + 2)) - code (f n) := by
  unfold derivative
  omega

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
#print axioms MCore.FinalFail.MaterialDerived.TriState.orbit_three_step
#print axioms MCore.FinalFail.MaterialDerived.SevenLaneVector.smul_add
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.closure_idempotent
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.interior_idempotent
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.proven_boundary_iff_not_proved
#print axioms MCore.FinalFail.MaterialDerived.EvidenceState.derivative_two_step
#print axioms MCore.FinalFail.MaterialDerived.negateProducer

end MCore.FinalFail.MaterialDerived
