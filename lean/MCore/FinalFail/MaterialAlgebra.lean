import MCore.FinalFail.GlobalPositiveMaterialFrontier

namespace MCore.FinalFail.MaterialAlgebra

open MCore.FinalFail.Semantic

universe u uL uF uS uV uC uZ uE uT

/--
A producer status is semantic metadata only.  It never manufactures a proof.
The order is intentionally monotone: OPEN_MATH < CONDITIONAL < PROVED.
-/
inductive ProducerState where
  | openMath
  | conditional
  | proved
  deriving DecidableEq, Repr

def ProducerState.rank : ProducerState → Nat
  | .openMath => 0
  | .conditional => 1
  | .proved => 2

instance : LE ProducerState where
  le a b := a.rank ≤ b.rank

theorem producerState_le_refl (s : ProducerState) : s ≤ s := by
  exact Nat.le_refl _

theorem producerState_le_trans
    {a b c : ProducerState}
    (hab : a ≤ b) (hbc : b ≤ c) : a ≤ c := by
  exact Nat.le_trans hab hbc

/-- Generic typed producer: a concrete object together with a proof that it
satisfies the target predicate. -/
structure Producer (α : Type u) (Target : α → Prop) where
  value : α
  cert : Target value

/-- A producer transports along implication. -/
def Producer.map
    {α : Type u} {P Q : α → Prop}
    (h : ∀ x, P x → Q x)
    (p : Producer α P) :
    Producer α Q :=
  ⟨p.value, h p.value p.cert⟩

@[simp] theorem Producer.map_value
    {α : Type u} {P Q : α → Prop}
    (h : ∀ x, P x → Q x)
    (p : Producer α P) :
    (p.map h).value = p.value := rfl

/-- Composition law for producer transport. -/
theorem Producer.map_comp
    {α : Type u} {P Q R : α → Prop}
    (hPQ : ∀ x, P x → Q x)
    (hQR : ∀ x, Q x → R x)
    (p : Producer α P) :
    p.map (fun x hx => hQR x (hPQ x hx)) =
      (p.map hPQ).map hQR := by
  rfl

/--
A residual is the exact proposition still missing after all certified
downstream transport has been factored out.
-/
structure Residual where
  proposition : Prop
  state : ProducerState
  description : String

/-- Residual conjunction: both mathematical atoms are required. -/
def Residual.and (a b : Residual) : Residual where
  proposition := a.proposition ∧ b.proposition
  state :=
    if a.state = .proved ∧ b.state = .proved then .proved
    else if a.state = .openMath ∨ b.state = .openMath then .openMath
    else .conditional
  description := "(" ++ a.description ++ ") AND (" ++ b.description ++ ")"

/-- Residual disjunction: either route is sufficient. -/
def Residual.or (a b : Residual) : Residual where
  proposition := a.proposition ∨ b.proposition
  state :=
    if a.state = .proved ∨ b.state = .proved then .proved
    else if a.state = .conditional ∨ b.state = .conditional then .conditional
    else .openMath
  description := "(" ++ a.description ++ ") OR (" ++ b.description ++ ")"

theorem Residual.and_proposition
    (a b : Residual) :
    (a.and b).proposition ↔
      (a.proposition ∧ b.proposition) := by
  rfl

theorem Residual.or_proposition
    (a b : Residual) :
    (a.or b).proposition ↔
      (a.proposition ∨ b.proposition) := by
  rfl

/--
A defect is a Boolean-valued diagnostic attached to a mathematical object.
It is useful for finite/certified diagnostics but is never promoted to a
universal theorem without a separate bridge.
-/
structure Defect (α : Type u) where
  eval : α → Bool

def Defect.zero {α : Type u} : Defect α :=
  ⟨fun _ => false⟩

def Defect.join {α : Type u} (d₁ d₂ : Defect α) : Defect α :=
  ⟨fun x => d₁.eval x || d₂.eval x⟩

def Defect.meet {α : Type u} (d₁ d₂ : Defect α) : Defect α :=
  ⟨fun x => d₁.eval x && d₂.eval x⟩

@[simp] theorem defect_zero_eval
    {α : Type u} (x : α) :
    (Defect.zero : Defect α).eval x = false := rfl

@[simp] theorem defect_join_eval
    {α : Type u} (d₁ d₂ : Defect α) (x : α) :
    (d₁.join d₂).eval x =
      (d₁.eval x || d₂.eval x) := rfl

@[simp] theorem defect_meet_eval
    {α : Type u} (d₁ d₂ : Defect α) (x : α) :
    (d₁.meet d₂).eval x =
      (d₁.eval x && d₂.eval x) := rfl

/--
Tri-state numeric carrier for ATK bookkeeping.

This is an algebraic datatype, not a new classical number system claim.
The three states are structural labels and the operations below are explicitly
defined finite algebra.
-/
inductive TriState where
  | seed
  | transit
  | manifest
  deriving DecidableEq, Repr

def TriState.toNat : TriState → Nat
  | .seed => 0
  | .transit => 1
  | .manifest => 2

def TriState.rotate : TriState → TriState
  | .seed => .transit
  | .transit => .manifest
  | .manifest => .seed

@[simp] theorem TriState.rotate_three (x : TriState) :
    x.rotate.rotate.rotate = x := by
  cases x <;> rfl

/-- Addition modulo the three structural states. -/
def TriState.add : TriState → TriState → TriState
  | .seed, y => y
  | .transit, .seed => .transit
  | .transit, .transit => .manifest
  | .transit, .manifest => .seed
  | .manifest, .seed => .manifest
  | .manifest, .transit => .seed
  | .manifest, .manifest => .transit

instance : Add TriState where
  add := TriState.add

@[simp] theorem TriState.seed_add (x : TriState) :
    .seed + x = x := by cases x <;> rfl

@[simp] theorem TriState.add_seed (x : TriState) :
    x + .seed = x := by cases x <;> rfl

theorem TriState.add_comm (x y : TriState) :
    x + y = y + x := by
  cases x <;> cases y <;> rfl

theorem TriState.add_assoc (x y z : TriState) :
    (x + y) + z = x + (y + z) := by
  cases x <;> cases y <;> cases z <;> rfl

/-- Negation in the cyclic three-state additive group. -/
def TriState.neg : TriState → TriState
  | .seed => .seed
  | .transit => .manifest
  | .manifest => .transit

instance : Neg TriState where
  neg := TriState.neg

@[simp] theorem TriState.add_neg (x : TriState) :
    x + (-x) = .seed := by
  cases x <;> rfl

/--
Finite cyclic additive law: TriState is an explicit copy of Z/3Z at the level
of the additive table.  We do not identify it with any analytic quantity.
-/
theorem TriState.threefold_transit :
    (.transit + .transit : TriState) + .transit = .seed := by
  rfl

/-- Product carrier of all seven material lanes. -/
structure SevenLaneVector where
  riemann : TriState
  beal : TriState
  pvsnp : TriState
  navierStokes : TriState
  hodge : TriState
  bsd : TriState
  yangMills : TriState
  deriving DecidableEq, Repr

def SevenLaneVector.zero : SevenLaneVector where
  riemann := .seed
  beal := .seed
  pvsnp := .seed
  navierStokes := .seed
  hodge := .seed
  bsd := .seed
  yangMills := .seed

def SevenLaneVector.add
    (a b : SevenLaneVector) : SevenLaneVector where
  riemann := a.riemann + b.riemann
  beal := a.beal + b.beal
  pvsnp := a.pvsnp + b.pvsnp
  navierStokes := a.navierStokes + b.navierStokes
  hodge := a.hodge + b.hodge
  bsd := a.bsd + b.bsd
  yangMills := a.yangMills + b.yangMills

instance : Add SevenLaneVector where
  add := SevenLaneVector.add

@[simp] theorem SevenLaneVector.zero_add
    (x : SevenLaneVector) :
    SevenLaneVector.zero + x = x := by
  cases x with
  | mk r b p n h d y =>
      rfl

theorem SevenLaneVector.add_comm
    (x y : SevenLaneVector) :
    x + y = y + x := by
  cases x with
  | mk xr xb xp xn xh xd xy =>
    cases y with
    | mk yr yb yp yn yh yd yy =>
      simp only [HAdd.hAdd, Add.add, SevenLaneVector.add]
      congr <;> apply TriState.add_comm

theorem SevenLaneVector.add_assoc
    (x y z : SevenLaneVector) :
    (x + y) + z = x + (y + z) := by
  cases x with
  | mk xr xb xp xn xh xd xy =>
    cases y with
    | mk yr yb yp yn yh yd yy =>
      cases z with
      | mk zr zb zp zn zh zd zy =>
        simp only [HAdd.hAdd, Add.add, SevenLaneVector.add]
        congr <;> apply TriState.add_assoc

/--
Global frontier residual.  This theorem intentionally exposes the exact seven
components already formalized in GlobalPositiveMaterialFrontier.
-/
theorem global_frontier_is_seven_component_product
    (Language : Type uL)
    (InP InNP : Language → Prop)
    (SAT : Language)
    (Flow : Type uF)
    (Stabilizer : Type uS)
    (ActualNS : Flow → Prop)
    (Stabilizes : Stabilizer → Flow → Prop)
    (Variety : Type uV)
    (Class : Variety → Type uC)
    (Cycle : Variety → Type uZ)
    (SmoothProjective : Variety → Prop)
    (RationalHodge : {X : Variety} → Class X → Prop)
    (Realizes : {X : Variety} → Cycle X → Class X → Prop)
    (Curve : Type uE)
    (Realizable : Curve → Prop)
    (AnalyticOrder MordellWeilRank : Curve → Int)
    (RefinedFormula : Curve → Prop)
    (Theory : Type uT)
    (Genuine4D OSReconstructs PositiveMassGap : Theory → Prop) :
    Nonempty
        (GlobalPositiveMaterialRoot
          Language InP InNP SAT
          Flow Stabilizer ActualNS Stabilizes
          Variety Class Cycle SmoothProjective RationalHodge Realizes
          Curve Realizable AnalyticOrder MordellWeilRank RefinedFormula
          Theory Genuine4D OSReconstructs PositiveMassGap) ↔
      (RiemannHypothesis ∧
       Nonempty BealUniversalGCDTarget ∧
       Nonempty (PvsNPSeparationTarget Language InP InNP SAT) ∧
       Nonempty
         (NavierStokesStabilizationTarget
           Flow Stabilizer ActualNS Stabilizes) ∧
       Nonempty
         (HodgeRealizationTarget
           Variety Class Cycle SmoothProjective RationalHodge Realizes) ∧
       Nonempty
         (BSDRealizableTarget
           Curve Realizable AnalyticOrder MordellWeilRank RefinedFormula) ∧
       Nonempty
         (YangMills4DGapTarget
           Theory Genuine4D OSReconstructs PositiveMassGap)) :=
  global_positive_root_iff_components
    Language InP InNP SAT
    Flow Stabilizer ActualNS Stabilizes
    Variety Class Cycle SmoothProjective RationalHodge Realizes
    Curve Realizable AnalyticOrder MordellWeilRank RefinedFormula
    Theory Genuine4D OSReconstructs PositiveMassGap

#print axioms MCore.FinalFail.MaterialAlgebra.Producer.map_comp
#print axioms MCore.FinalFail.MaterialAlgebra.TriState.rotate_three
#print axioms MCore.FinalFail.MaterialAlgebra.TriState.add_assoc
#print axioms MCore.FinalFail.MaterialAlgebra.SevenLaneVector.add_assoc
#print axioms MCore.FinalFail.MaterialAlgebra.global_frontier_is_seven_component_product

end MCore.FinalFail.MaterialAlgebra
