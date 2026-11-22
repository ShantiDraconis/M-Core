import Mathlib

namespace MCoreMinimal

inductive Node where
  | I | coeffA | targetY
  deriving DecidableEq, Repr

abbrev Graph := List (Node × Node)
def HasEdge (G : Graph) (x y : Node) : Prop := (x, y) ∈ G
def HasCanonicalSelfRef (G : Graph) : Prop :=
  HasEdge G .I .coeffA ∧ HasEdge G .coeffA .targetY ∧ HasEdge G .targetY .I
def PassesSelfRefGate (G : Graph) : Prop := ¬ HasCanonicalSelfRef G

theorem A2_CanonicalCycleRejected :
    ¬ PassesSelfRefGate
      [(.I, .coeffA), (.coeffA, .targetY), (.targetY, .I)] := by
  intro h
  apply h
  simp [HasCanonicalSelfRef, HasEdge]

end MCoreMinimal
