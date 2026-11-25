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
  | negativeInfinity
  | directedZero (positive : Bool)
  | variable (name : String)
  | add (x y : ExactExpr)
  | sub (x y : ExactExpr)
  | log (x : ExactExpr)
  | exp (x : ExactExpr)
  | sin (x : ExactExpr)
  | cos (x : ExactExpr)
  | tan (x : ExactExpr)
  | apply (name : String) (x : ExactExpr)
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

-- A typed relation describes every admissible interpretation of an exact point.
structure ExactPoint (A : Type*) where
  expression : ExactExpr
  constraint : A → Prop

def ExactPoint.solutions {A : Type*} (p : ExactPoint A) : Set A :=
  admissibleParameters p.constraint

def ExactPoint.combine {A B : Type*} (op : ExactExpr → ExactExpr → ExactExpr)
    (p : ExactPoint A) (q : ExactPoint B) (joint : A → B → Prop) :
    ExactPoint (A × B) :=
  ⟨op p.expression q.expression, fun x =>
    p.constraint x.1 ∧ q.constraint x.2 ∧ joint x.1 x.2⟩

theorem combine_exact {A B : Type*} (op : ExactExpr → ExactExpr → ExactExpr)
    (p : ExactPoint A) (q : ExactPoint B) (joint : A → B → Prop)
    (a : A) (b : B) :
    (a, b) ∈ (ExactPoint.combine op p q joint).solutions ↔
      p.constraint a ∧ q.constraint b ∧ joint a b := Iff.rfl

theorem exact_zero_syntax_distinct :
    ExactExpr.integer 0 ≠ ExactExpr.div (.integer 0) (.integer 0) := by
  decide

#print axioms combine_exact
#print axioms exact_zero_syntax_distinct


-- Expanded syntax: preserve constants, association, binding and operator arity.
inductive ExpandedExpr where
  | atom (x : ExactExpr)
  | constant (name : String)
  | angularZero (angle : ExpandedExpr)
  | unary (op : String) (x : ExpandedExpr)
  | binary (op : String) (x y : ExpandedExpr)
  | binder (op boundName : String) (domain body : ExpandedExpr)
  deriving DecidableEq, Repr

def expandedExamples : List ExpandedExpr :=
  [.binary "div" (.atom (.integer 0)) (.atom (.integer 2)),
   .binary "div" (.atom (.integer 0)) (.constant "pi"),
   .binary "pow" (.atom (.integer 0)) (.atom (.integer 1)),
   .binary "pow" (.atom (.integer 0))
     (.binary "pow" (.atom .infinity) (.unary "sqrt" (.atom .infinity)))]

-- Realizations retain joint constraints, not merely marginal limit sets.
structure ExpandedPoint (A B : Type*) where
  expression : ExpandedExpr
  domain : Set A
  direction : A → Prop
  rates : A → Prop
  constraints : A → Prop
  limitRelation : A → B → Prop
  accumulationRelation : A → B → Prop
  singularity : A → Prop
  branch : A → Prop

def ExpandedPoint.Admissible {A B : Type*} (p : ExpandedPoint A B) (a : A) : Prop :=
  a ∈ p.domain ∧ p.direction a ∧ p.rates a ∧ p.constraints a ∧ p.branch a

def ExpandedPoint.limits {A B : Type*} (p : ExpandedPoint A B) : Set B :=
  {b | ∃ a, p.Admissible a ∧ p.limitRelation a b}

theorem expanded_limits_exact {A B : Type*} (p : ExpandedPoint A B) (b : B) :
    b ∈ p.limits ↔ ∃ a, p.Admissible a ∧ p.limitRelation a b := Iff.rfl

theorem expanded_zero_div (c : ℝ) (_hc : c ≠ 0) : (0 : ℝ) / c = 0 := zero_div c

theorem expanded_zero_pow_one : (0 : ℝ) ^ (1 : ℕ) = 0 := by simp

theorem expanded_distinct_constants :
    ExpandedExpr.binary "div" (.atom (.integer 0)) (.atom (.integer 2)) ≠
    ExpandedExpr.binary "div" (.atom (.integer 0)) (.constant "pi") := by
  decide

#print axioms expanded_limits_exact
#print axioms expanded_zero_div
#print axioms expanded_zero_pow_one
#print axioms expanded_distinct_constants


-- Material identities for exact points; domain restrictions are explicit.
theorem point_zero_div_complex (c : ℂ) (_hc : c ≠ 0) :
    (0 : ℂ) / c = 0 := zero_div c

theorem point_zero_div_pi : (0 : ℝ) / Real.pi = 0 :=
  expanded_zero_div Real.pi Real.pi_ne_zero

theorem point_zero_pow_positive (n : ℕ) (hn : n ≠ 0) :
    (0 : ℝ) ^ n = 0 := zero_pow hn

theorem point_ratio_realization (a t : ℝ) (ht : t ≠ 0) :
    (a * t) / t = a := by
  field_simp

theorem point_product_realization (a t : ℝ) (ht : t ≠ 0) :
    (a * t) * t⁻¹ = a := by
  field_simp

theorem point_difference_realization (a t : ℝ) :
    (t + a) - t = a := by ring

theorem point_path_ratio (k t : ℝ) (ht : t ≠ 0) (hk : 1 + k ≠ 0) :
    t / (t + k * t) = 1 / (1 + k) := by
  have h : t + k * t = (1 + k) * t := by ring
  rw [h]
  field_simp

theorem point_power_log_realization (a t : ℝ) (ht : t ≠ 0) :
    (a / t) * t = a := by field_simp

#print axioms point_zero_div_complex
#print axioms point_zero_div_pi
#print axioms point_zero_pow_positive
#print axioms point_ratio_realization
#print axioms point_product_realization
#print axioms point_difference_realization
#print axioms point_path_ratio
#print axioms point_power_log_realization

end MCore.Research.UserProgram
