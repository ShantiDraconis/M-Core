import MCore.Research.UserProgram.SemanticProofCore

namespace MCore.Research.UserProgram.Recursive

/-- Every operand is itself an exact point; metadata does not assert convergence. -/
inductive Point where
  | atom (domain name : String)
  | node (domain op : String) (args : List Point)
  | approach (base trajectory : Point)
  | annotated (base : Point) (kind : String) (data : Point)
  deriving Repr

/-- Partial evaluation is separate from syntax and evidence. -/
structure Realization (A B : Type*) where
  point : Point
  admissible : A → Prop
  value : A → Option B

def Realization.results {A B : Type*} (p : Realization A B) : Set B :=
  {b | ∃ a, p.admissible a ∧ p.value a = some b}

theorem results_exact {A B : Type*} (p : Realization A B) (b : B) :
    b ∈ p.results ↔ ∃ a, p.admissible a ∧ p.value a = some b := Iff.rfl

def zero : Point := .atom "real" "0"
def pi : Point := .atom "real" "pi"
def two : Point := .atom "real" "2"
def divPoint (a b : Point) : Point := .node "real" "div" [a,b]

theorem zero_div_distinct : divPoint zero two ≠ divPoint zero pi := by
  intro h
  simp [divPoint, zero, two, pi] at h

theorem add_residue (a b x y : ℝ) :
    (a+x)+(b+y)-(a+b) = x+y := by ring

theorem sub_residue (a b x y : ℝ) :
    (a+x)-(b+y)-(a-b) = x-y := by ring

theorem mul_residue (a b x y : ℝ) :
    (a+x)*(b+y)-a*b = a*y+b*x+x*y := by ring

theorem div_residue (a b x y : ℝ) (hb : b ≠ 0) (hy : b+y ≠ 0) :
    (a+x)/(b+y)-a/b = (b*x-a*y)/(b*(b+y)) := by
  field_simp <;> ring

theorem pi_approach_residue (a x y : ℝ) (hy : Real.pi-y ≠ 0) :
    (a+x)/(Real.pi-y)-a/Real.pi =
      (Real.pi*x+a*y)/(Real.pi*(Real.pi-y)) := by
  field_simp [Real.pi_ne_zero] <;> ring

#print axioms results_exact
#print axioms zero_div_distinct
#print axioms add_residue
#print axioms sub_residue
#print axioms mul_residue
#print axioms div_residue
#print axioms pi_approach_residue

end MCore.Research.UserProgram.Recursive
