import MCore.MaterialMath.TriState.Dynamics

namespace MCore.MaterialMath

open Phase3
open TriNumber

namespace TriArithmetic

/-- Arithmetic mean of the three phase values. -/
def phaseMean
    {α : Type*} [LinearOrderedField α]
    (x : TriNumber α) : α :=
  phaseSum x / 3

theorem phaseMean_rotate
    {α : Type*} [LinearOrderedField α]
    (x : TriNumber α) :
    phaseMean (rotate x) = phaseMean x := by
  simp [phaseMean, phaseSum_rotate]

/-- Remove the common mean component from every phase. -/
def center
    {α : Type*} [LinearOrderedField α]
    (x : TriNumber α) : TriNumber α :=
  fun p => x p - phaseMean x

/-- Centering always produces a balanced tri-number. -/
theorem center_balanced
    {α : Type*} [LinearOrderedField α]
    (x : TriNumber α) :
    Balanced (center x) := by
  unfold Balanced phaseSum center phaseMean
  field_simp
  ring

/-- Centering commutes with cyclic phase rotation. -/
theorem center_rotate
    {α : Type*} [LinearOrderedField α]
    (x : TriNumber α) :
    center (rotate x) = rotate (center x) := by
  funext p
  simp [center, rotate, phaseMean_rotate]

/-- Pairwise phase-spread energy. -/
def spreadEnergy
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) : α :=
  (x .seed - x .passage)^2 +
  (x .passage - x .manifest)^2 +
  (x .manifest - x .seed)^2

theorem spreadEnergy_rotate
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) :
    spreadEnergy (rotate x) = spreadEnergy x := by
  simp [spreadEnergy, rotate, Phase3.rotate]
  ring

theorem spreadEnergy_nonneg
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) :
    0 ≤ spreadEnergy x := by
  unfold spreadEnergy
  positivity

/-- Zero spread is exactly phase coherence. -/
theorem spreadEnergy_eq_zero_iff_coherent
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) :
    spreadEnergy x = 0 ↔ Coherent x := by
  constructor
  · intro h
    have h1 : (x .seed - x .passage)^2 = 0 := by
      nlinarith [sq_nonneg (x .passage - x .manifest),
        sq_nonneg (x .manifest - x .seed)]
    have h2 : (x .passage - x .manifest)^2 = 0 := by
      nlinarith [sq_nonneg (x .seed - x .passage),
        sq_nonneg (x .manifest - x .seed)]
    constructor
    · nlinarith
    · nlinarith
  · rintro ⟨hSP, hPM⟩
    simp [spreadEnergy, hSP, hPM]

/-- Three-way sign class for an ordered coefficient type. -/
inductive Sign3 where
  | negative
  | zero
  | positive
  deriving DecidableEq, Repr

def sign3
    {α : Type*} [LinearOrderedRing α]
    (a : α) : Sign3 :=
  if a < 0 then .negative
  else if a = 0 then .zero
  else .positive

/-- Sign signature of the three phases. -/
def signSignature
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) : Phase3 → Sign3 :=
  fun p => sign3 (x p)

theorem signSignature_rotate
    {α : Type*} [LinearOrderedRing α]
    (x : TriNumber α) :
    signSignature (rotate x) =
      fun p => signSignature x (Phase3.rotate p) := by
  rfl

end TriArithmetic

namespace TriTopology

/-- Combinatorial open neighborhood in the 3-cycle: a point and its two
distinct cyclic neighbors. On three states this is the entire phase space. -/
def closedNeighborhood (p : Phase3) : Set Phase3 :=
  {q | q = p ∨ Phase3.Adjacent p q}

theorem mem_closedNeighborhood_self (p : Phase3) :
    p ∈ closedNeighborhood p := by
  exact Or.inl rfl

/-- Because the phase graph is a triangle, every point lies in every closed
one-step neighborhood. -/
theorem closedNeighborhood_eq_univ (p : Phase3) :
    closedNeighborhood p = Set.univ := by
  ext q
  constructor
  · intro _
    trivial
  · intro _
    by_cases h : q = p
    · exact Or.inl h
    · exact Or.inr (Phase3.adjacent_of_ne h.symm)

/-- A phase path is a finite sequence whose successive states are adjacent
or equal. This recursive form avoids index arithmetic in downstream proofs. -/
def IsPhasePath : List Phase3 → Prop
  | [] => True
  | [_] => True
  | p :: q :: rest =>
      (p = q ∨ Phase3.Adjacent p q) ∧ IsPhasePath (q :: rest)

/-- Every length-two list of phase states is a valid path on the triangle. -/
theorem pair_isPhasePath (p q : Phase3) :
    IsPhasePath [p, q] := by
  simp [IsPhasePath]
  by_cases h : p = q
  · exact Or.inl h
  · exact Or.inr (Phase3.adjacent_of_ne h)

end TriTopology

end MCore.MaterialMath
