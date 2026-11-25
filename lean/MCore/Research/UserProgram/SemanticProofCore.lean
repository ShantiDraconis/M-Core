import Mathlib
import MCore.Research.UserProgram.C3LinearSectors

namespace MCore.Research.UserProgram

/-! Typed semantic/proof layer for the user research program.
    An inhabitant carries an actual proof of its proposition; no assumed bridge is created here. -/

inductive NumericClass
  | natural | integer | rational | real | complex | cyclic3 | indeterminate
  deriving DecidableEq, Repr

structure SemanticCarrier where
  Carrier : Type
  numericClass : NumericClass

def ComplexCarrier : SemanticCarrier :=
  ⟨ℂ, .complex⟩

def I3Carrier : SemanticCarrier :=
  ⟨I3State, .cyclic3⟩

structure SemanticMap (A B : SemanticCarrier) where
  run : A.Carrier → B.Carrier

def SemanticMap.id (A : SemanticCarrier) : SemanticMap A A :=
  ⟨fun x => x⟩

def SemanticMap.comp {A B C : SemanticCarrier}
    (g : SemanticMap B C) (f : SemanticMap A B) : SemanticMap A C :=
  ⟨g.run ∘ f.run⟩

theorem SemanticMap.comp_apply {A B C : SemanticCarrier}
    (g : SemanticMap B C) (f : SemanticMap A B) (x : A.Carrier) :
    (g.comp f).run x = g.run (f.run x) := rfl

structure Law (α : Type) where
  statement : α → Prop

structure Habitant {α : Type} (L : Law α) where
  witness : α
  proof : L.statement witness

structure Inhabitant (P : Prop) where
  proof : P

def Inhabitant.ofProof {P : Prop} (h : P) : Inhabitant P :=
  ⟨h⟩

theorem Inhabitant.sound {P : Prop} (h : Inhabitant P) : P :=
  h.proof

theorem Inhabitant.nonempty_iff (P : Prop) :
    Nonempty (Inhabitant P) ↔ P := by
  constructor
  · rintro ⟨h⟩
    exact h.proof
  · intro h
    exact ⟨⟨h⟩⟩

structure ProvenLaw (α : Type) where
  law : Law α
  inhabitant : Habitant law

def RotationLaw : Law I3State where
  statement s := s.next.next.next = s

def rotationHabitant : Habitant RotationLaw where
  witness := .manifesto
  proof := by rfl

def RotationGlobalLaw : Prop :=
  ∀ s : I3State, s.next.next.next = s

def rotationGlobalInhabitant : Inhabitant RotationGlobalLaw :=
  ⟨I3State.next_three⟩

theorem rotationGlobalInhabitant_sound :
    RotationGlobalLaw :=
  rotationGlobalInhabitant.sound

structure SemanticFlow (A : SemanticCarrier) where
  step : SemanticMap A A

def SemanticFlow.iterate {A : SemanticCarrier}
    (F : SemanticFlow A) : ℕ → A.Carrier → A.Carrier
  | 0 => id
  | n + 1 => F.step.run ∘ F.iterate n

def I3Flow : SemanticFlow I3Carrier :=
  ⟨⟨I3State.next⟩⟩

theorem I3Flow_three (s : I3State) :
    I3Flow.iterate 3 s = s := by
  cases s <;> rfl

def I3FlowThreeInhabitant :
    Inhabitant (∀ s : I3State, I3Flow.iterate 3 s = s) :=
  ⟨I3Flow_three⟩

/-- Exact proposition points with evidence-bearing trivalent states. -/
inductive PointEvidence (P : Prop) where
  | unknown
  | positive (proof : P)
  | negative (refutation : ¬ P)

def PointEvidence.map {P Q : Prop} (f : P → Q) :
    PointEvidence P → PointEvidence Q
  | .positive h => .positive (f h)
  | .unknown => .unknown
  | .negative _ => .unknown

def PointEvidence.transport {P Q : Prop} (h : P ↔ Q) :
    PointEvidence P → PointEvidence Q
  | .positive hp => .positive (h.mp hp)
  | .negative hn => .negative (fun hq => hn (h.mpr hq))
  | .unknown => .unknown

theorem evidence_no_conflict {P : Prop} (hp : P) (hn : ¬ P) : False :=
  hn hp

#print axioms evidence_no_conflict

inductive GapKind where
  | sorryGap | missingParameter | analyticGap | bridgeGap | buildGap
  deriving DecidableEq, Repr

structure GapPoint where
  repository : String
  branch : String
  path : String
  declaration : String
  ordinal : Nat
  kind : GapKind
  statement : Prop

def GapPoint.Evidence (g : GapPoint) := PointEvidence g.statement

def GapPoint.unresolved (g : GapPoint) : g.Evidence :=
  .unknown

def GapPoint.resolve (g : GapPoint) (h : g.statement) : g.Evidence :=
  .positive h

def GapPoint.refute (g : GapPoint) (h : ¬ g.statement) : g.Evidence :=
  .negative h

def AllResolved (gaps : List GapPoint) : Prop :=
  ∀ g ∈ gaps, g.statement

theorem allResolved_cons (g : GapPoint) (gs : List GapPoint) :
    AllResolved (g :: gs) ↔ g.statement ∧ AllResolved gs := by
  simp only [AllResolved, List.mem_cons]
  constructor
  · intro h
    exact ⟨h g (Or.inl rfl), fun x hx => h x (Or.inr hx)⟩
  · intro h x hx
    rcases hx with he | hm
    · subst x
      exact h.1
    · exact h.2 x hm

theorem resolve_producer (gs : List GapPoint) (P : Prop)
    (compose : AllResolved gs → P) (h : AllResolved gs) : P :=
  compose h

#print axioms allResolved_cons
#print axioms resolve_producer

structure VectorGap where
  target : GapPoint
  dimension : Nat
  component : Fin dimension → GapPoint

def VectorGap.Composition (g : VectorGap) : Prop :=
  (∀ i, (g.component i).statement) → g.target.statement

def VectorGap.Evidence (g : VectorGap) :=
  ∀ i, PointEvidence (g.component i).statement

theorem closeVector (g : VectorGap)
    (compose : g.Composition)
    (evidence : ∀ i, (g.component i).statement) :
    g.target.statement :=
  compose evidence

theorem refuted_component_blocks_vector (g : VectorGap)
    (i : Fin g.dimension) (h : ¬ (g.component i).statement) :
    ¬ (∀ j, (g.component j).statement) :=
  fun hp => h (hp i)

#print axioms closeVector
#print axioms refuted_component_blocks_vector

-- Exact syntax is independent of numerical interpretation.
inductive ExactExpr where
  | integer (n : Int)
  | infinity
  | neg (x : ExactExpr)
  | sqrt (x : ExactExpr)
  | mul (x y : ExactExpr)
  | div (x y : ExactExpr)
  | pow (x y : ExactExpr)
  deriving DecidableEq, Repr

def exactIndeterminateExamples : List ExactExpr :=
  [.sqrt .infinity, .div (.integer 0) .infinity,
   .mul (.neg (.integer 0)) .infinity,
   .div (.integer 2) (.integer 0),
   .div (.neg (.integer 0)) (.integer 4),
   .pow (.integer 0) .infinity,
   .div (.integer 0) (.integer 0), .div .infinity .infinity]

-- Retain the entire solution set, rather than choosing an arbitrary witness.
def admissibleParameters {A : Type*} (constraint : A → Prop) : Set A :=
  {a | constraint a}

theorem admissible_exact {A : Type*} (C : A → Prop) (a : A) :
    a ∈ admissibleParameters C ↔ C a := Iff.rfl

theorem parameter_exists_iff {A : Type*} (C : A → Prop) :
    (admissibleParameters C).Nonempty ↔ ∃ a, C a := Iff.rfl

theorem parameter_uniform_discharge {A : Type*} (C : A → Prop)
    (P : A → Prop) (h : ∀ a ∈ admissibleParameters C, P a) :
    ∀ a, C a → P a :=
  fun a ha => h a ha

#print axioms admissible_exact
#print axioms parameter_exists_iff
#print axioms parameter_uniform_discharge

end MCore.Research.UserProgram
