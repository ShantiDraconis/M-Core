import MCore.ATK.StructuralDefect

namespace MCore.ATK.UniversalProducer

open MCore.ATK.StructuralDefect

/--
Canonical structural taxonomy used by the current seven-lane program.

This is classification metadata only. It does not identify the concrete
mathematics of two lanes merely because they share a shape.
-/
def canonicalGapShape : ProblemKind → GapShape
  | .riemann => .F1
  | .pnp => .F2
  | .yangMills => .F2
  | .navierStokes => .F7
  | .bsd => .F5
  | .hodge => .F4
  | .beal => .F6

/--
One producer-first lane.

defect, step, and contract are the shared structural mechanism.
extract is deliberately problem-specific: zero structural defect is not
allowed to count as a mathematical solution until it constructs the exact
terminal inhabitant. certify is the final transport from that inhabitant to
the lane certificate type.

freeze prevents a terminal state from being reopened by the structural
dynamics.
-/
structure ProducerLane where
  State : Type
  Inhabitant : Type
  Certificate : Type
  step : State → State
  defect : State → Nat
  contract : ∀ x, 0 < defect x → defect (step x) < defect x
  freeze : ∀ x, defect x = 0 → step x = x
  extract : ∀ x, defect x = 0 → Inhabitant
  certify : Inhabitant → Certificate

namespace ProducerLane

variable (L : ProducerLane)

/-- Every nonterminal structural step is genuinely forward: it cannot be a
self-loop. -/
theorem step_ne_self_of_positive
    (x : L.State) (hpos : 0 < L.defect x) :
    L.step x ≠ x := by
  intro hfix
  have hdec := L.contract x hpos
  rw [hfix] at hdec
  exact (Nat.lt_irrefl (L.defect x)) hdec

/-- Conversely, every fixed point of a valid producer lane has zero defect. -/
theorem defect_eq_zero_of_fixed
    (x : L.State) (hfix : L.step x = x) :
    L.defect x = 0 := by
  by_contra hzero
  have hpos : 0 < L.defect x := Nat.pos_of_ne_zero hzero
  exact (L.step_ne_self_of_positive x hpos) hfix

/-- The lane dynamics form a StructuralCore. -/
def toStructuralCore : StructuralCore where
  State := L.State
  step := L.step
  defect := L.defect
  contract := L.contract

/--
Fuel-bounded normalizer for one producer lane.

The fuel will be instantiated by the current defect.  A zero-defect state is
frozen; otherwise the unique forward structural step is taken.
-/
def normalizeFuel : Nat → L.State → L.State
  | 0, x => x
  | n + 1, x =>
      if h : L.defect x = 0 then
        x
      else
        L.normalizeFuel n (L.step x)

/-- Sufficient fuel forces the normalizer to a zero-defect state. -/
theorem normalizeFuel_defect_zero
    (n : Nat) (x : L.State)
    (hbound : L.defect x ≤ n) :
    L.defect (L.normalizeFuel n x) = 0 := by
  induction n generalizing x with
  | zero =>
      have hz : L.defect x = 0 := Nat.eq_zero_of_le_zero hbound
      simp [normalizeFuel, hz]
  | succ n ih =>
      by_cases hz : L.defect x = 0
      · simp [normalizeFuel, hz]
      · have hpos : 0 < L.defect x := Nat.pos_of_ne_zero hz
        have hdec : L.defect (L.step x) < L.defect x :=
          L.contract x hpos
        have hnext : L.defect (L.step x) ≤ n := by
          omega
        simp [normalizeFuel, hz, ih (L.step x) hnext]

/-- Canonical normal form reached using exactly the initial defect as fuel. -/
def normalize (x : L.State) : L.State :=
  L.normalizeFuel (L.defect x) x

theorem normalize_defect_zero
    (x : L.State) :
    L.defect (L.normalize x) = 0 := by
  unfold normalize
  exact L.normalizeFuel_defect_zero (L.defect x) x (Nat.le_refl _)

/-- The canonical normal form is frozen under the lane step. -/
theorem normalize_fixed
    (x : L.State) :
    L.step (L.normalize x) = L.normalize x :=
  L.freeze (L.normalize x) (L.normalize_defect_zero x)

/--
Constructive terminal inhabitant producer.

Unlike inhabitant_after_steps below, this definition returns the actual
inhabitant term rather than only proving Nonempty.
-/
def produceInhabitant
    (x : L.State) : L.Inhabitant :=
  L.extract (L.normalize x) (L.normalize_defect_zero x)

/-- Constructive terminal certificate producer. -/
def produceCertificate
    (x : L.State) : L.Certificate :=
  L.certify (L.produceInhabitant x)

/--
Finite-time exact producer theorem for one lane.

The result is not merely structural vanishing: the lane-specific extract
field must construct an inhabitant at the zero-defect state.
-/
theorem inhabitant_after_steps
    (x : L.State) :
    ∃ k : Nat,
      k ≤ L.defect x ∧
      Nonempty L.Inhabitant := by
  let C := L.toStructuralCore
  obtain ⟨k, hk, hz⟩ := C.intrinsic_vanishing x
  exact ⟨k, hk, ⟨L.extract ((L.step^[k]) x) hz⟩⟩

/--
Finite-time certificate theorem for one lane.

The certificate is downstream of a genuinely constructed inhabitant; no
certificate is manufactured directly from the structural defect.
-/
theorem certificate_after_steps
    (x : L.State) :
    ∃ k : Nat,
      k ≤ L.defect x ∧
      Nonempty L.Certificate := by
  obtain ⟨k, hk, hI⟩ := L.inhabitant_after_steps x
  rcases hI with ⟨I⟩
  exact ⟨k, hk, ⟨L.certify I⟩⟩

/-- Terminal states are frozen. -/
theorem terminal_is_fixed
    (x : L.State) (hz : L.defect x = 0) :
    L.step x = x :=
  L.freeze x hz

/--
For a valid lane, fixed point and zero defect are equivalent. This is the
formal no-loop law used by the forward-only workflow.
-/
theorem fixed_iff_zero
    (x : L.State) :
    L.step x = x ↔ L.defect x = 0 := by
  constructor
  · exact L.defect_eq_zero_of_fixed x
  · exact L.terminal_is_fixed x

end ProducerLane

/--
A universal producer kernel is a dependent family of seven exact lanes.

The family shares one theorem schema but not one concrete state carrier,
inhabitant type, or certificate type. This prevents cross-problem type
identification from being smuggled into the universal layer.
-/
structure UniversalProducerKernel where
  lane : ProblemKind → ProducerLane

/-- One concrete starting state for every problem lane. -/
structure UniversalSeed (K : UniversalProducerKernel) where
  state : (p : ProblemKind) → (K.lane p).State

/-- Concrete inhabitant term for every lane. -/
structure UniversalInhabitantBundle (K : UniversalProducerKernel) where
  inhabitant : (p : ProblemKind) → (K.lane p).Inhabitant

/-- Concrete certificate term for every lane: the abstract universal final root. -/
structure UniversalFinalRoot (K : UniversalProducerKernel) where
  certificate : (p : ProblemKind) → (K.lane p).Certificate

/-- Build all seven concrete inhabitants by running each lane normalizer. -/
def buildInhabitantBundle
    (K : UniversalProducerKernel)
    (S : UniversalSeed K) :
    UniversalInhabitantBundle K where
  inhabitant := fun p =>
    (K.lane p).produceInhabitant (S.state p)

/-- Build the abstract universal final root from the same exact producers. -/
def buildFinalRoot
    (K : UniversalProducerKernel)
    (S : UniversalSeed K) :
    UniversalFinalRoot K where
  certificate := fun p =>
    (K.lane p).produceCertificate (S.state p)

/--
External issuance is intentionally a separate interface.

The universal mathematical kernel may build the final-root payload, but an
external certificate format/authority must provide its own issuance map.
-/
structure ExternalCertificateInterface
    (K : UniversalProducerKernel) where
  ExternalCertificate : Type
  issue : UniversalFinalRoot K → ExternalCertificate

/-- Generic external certificate issuance after the universal final root exists. -/
def issueExternalCertificate
    (K : UniversalProducerKernel)
    (S : UniversalSeed K)
    (E : ExternalCertificateInterface K) :
    E.ExternalCertificate :=
  E.issue (buildFinalRoot K S)

/-- All seven exact terminal inhabitant types are inhabited. -/
def AllInhabitants
    (K : UniversalProducerKernel) : Prop :=
  ∀ p : ProblemKind, Nonempty (K.lane p).Inhabitant

/-- All seven exact certificate types are inhabited. -/
def AllCertificates
    (K : UniversalProducerKernel) : Prop :=
  ∀ p : ProblemKind, Nonempty (K.lane p).Certificate

/--
Universal producer theorem.

For every indexed lane, strict Nat-valued defect descent reaches a zero-defect
state in finite time, the problem-specific extractor builds the exact
inhabitant, and the certifier builds the lane certificate.

The theorem therefore isolates the only admissible universal mechanism:
STRUCTURAL DESCENT -> EXACT TERMINAL EXTRACTION -> CERTIFICATION.
It does not remove the obligation to prove each lane contract, extract,
and certify fields.
-/
theorem universal_inhabitant_theorem
    (K : UniversalProducerKernel)
    (S : UniversalSeed K) :
    AllInhabitants K := by
  intro p
  obtain ⟨k, hk, hI⟩ :=
    (K.lane p).inhabitant_after_steps (S.state p)
  exact hI

/-- Certificate form of universal_inhabitant_theorem. -/
theorem universal_certificate_theorem
    (K : UniversalProducerKernel)
    (S : UniversalSeed K) :
    AllCertificates K := by
  intro p
  obtain ⟨k, hk, hC⟩ :=
    (K.lane p).certificate_after_steps (S.state p)
  exact hC

/--
A lane-local quantitative witness of the universal theorem: each lane receives
an explicit finite step bound no larger than its initial defect.
-/
theorem universal_bounded_production
    (K : UniversalProducerKernel)
    (S : UniversalSeed K)
    (p : ProblemKind) :
    ∃ k : Nat,
      k ≤ (K.lane p).defect (S.state p) ∧
      Nonempty (K.lane p).Certificate :=
  (K.lane p).certificate_after_steps (S.state p)

/-- A zero-defect structural core used to state the materialization firewall. -/
def zeroStructuralCore : StructuralCore where
  State := Unit
  step := id
  defect := fun _ => 0
  contract := by
    intro x h
    omega

/--
Materialization firewall.

Structural descent alone cannot manufacture an inhabitant of an arbitrary
target type.  The proof instantiates the alleged universal constructor at the
empty type.  Therefore every real application of the universal producer
theorem must supply a problem-specific extraction map from zero defect to the
exact terminal inhabitant type.
-/
theorem no_target_from_structure_alone :
    ¬ (∀ (C : StructuralCore) (x : C.State) (Target : Type),
        Nonempty Target) := by
  intro h
  have hempty : Nonempty Empty :=
    h zeroStructuralCore () Empty
  rcases hempty with ⟨e⟩
  exact nomatch e

/--
No structural shortcut theorem.

A proposed universal lane whose step leaves a positive-defect state unchanged
cannot satisfy the producer contract. In particular, renaming an OPEN_MATH
obligation while keeping the state fixed cannot instantiate this kernel.
-/
theorem no_positive_defect_self_loop
    (K : UniversalProducerKernel)
    (p : ProblemKind)
    (x : (K.lane p).State)
    (hpos : 0 < (K.lane p).defect x) :
    (K.lane p).step x ≠ x :=
  (K.lane p).step_ne_self_of_positive x hpos

#print axioms MCore.ATK.UniversalProducer.ProducerLane.step_ne_self_of_positive
#print axioms MCore.ATK.UniversalProducer.ProducerLane.defect_eq_zero_of_fixed
#print axioms MCore.ATK.UniversalProducer.ProducerLane.normalizeFuel_defect_zero
#print axioms MCore.ATK.UniversalProducer.ProducerLane.normalize_defect_zero
#print axioms MCore.ATK.UniversalProducer.ProducerLane.produceInhabitant
#print axioms MCore.ATK.UniversalProducer.ProducerLane.produceCertificate
#print axioms MCore.ATK.UniversalProducer.ProducerLane.inhabitant_after_steps
#print axioms MCore.ATK.UniversalProducer.ProducerLane.certificate_after_steps
#print axioms MCore.ATK.UniversalProducer.ProducerLane.fixed_iff_zero
#print axioms MCore.ATK.UniversalProducer.buildInhabitantBundle
#print axioms MCore.ATK.UniversalProducer.buildFinalRoot
#print axioms MCore.ATK.UniversalProducer.issueExternalCertificate
#print axioms MCore.ATK.UniversalProducer.universal_inhabitant_theorem
#print axioms MCore.ATK.UniversalProducer.universal_certificate_theorem
#print axioms MCore.ATK.UniversalProducer.universal_bounded_production
#print axioms MCore.ATK.UniversalProducer.no_target_from_structure_alone
#print axioms MCore.ATK.UniversalProducer.no_positive_defect_self_loop

end MCore.ATK.UniversalProducer
