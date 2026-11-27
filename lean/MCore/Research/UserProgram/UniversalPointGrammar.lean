import MCore.Research.UserProgram.RecursiveExactPoints

namespace MCore.Research.UserProgram.Recursive

/-- Domain tags preserve identity, not a claim of numerical membership. -/
inductive DomainTag where
  | natural | integer | rational | real | complex | quaternion
  | padic | finiteField | vector | matrix | tensor | extended
  | other (name : String)
  deriving Repr, DecidableEq

inductive OperatorTag where
  | add | sub | mul | div | neg | pow | root | factorial
  | doubleFactorial | gamma | mod | rem | congruence
  | log | exp | derivative | integral | limit | sum | product
  | other (name : String)
  deriving Repr, DecidableEq

def inDomain (d : DomainTag) (p : Point) : Point :=
  .annotated p "domain" (.atom "domain" (reprStr d))

def applyExact (d : DomainTag) (op : OperatorTag) (args : List Point) : Point :=
  .node (reprStr d) (reprStr op) args

def directed (p : Point) (direction : Point) : Point :=
  .approach p direction

def rawExact (s : String) : Point := .atom "raw-syntax" s

/-- Syntactic closure for every finite list of operands. -/
theorem grammar_closed (d : DomainTag) (op : OperatorTag) (args : List Point) :
    ∃ p : Point, p = applyExact d op args :=
  ⟨applyExact d op args, rfl⟩

/-- A domain annotation never supplies an evaluation witness. -/
def DomainMembership {A : Type*} (p : Realization Unit A) : Prop :=
  ∃ a : A, a ∈ p.results

theorem membership_requires_value {A : Type*} (p : Realization Unit A) :
    DomainMembership p ↔ ∃ a : A, p.admissible () ∧ p.value () = some a := by
  constructor
  · rintro ⟨a, h⟩
    rcases (results_exact p a).mp h with ⟨u, hu, hv⟩
    cases u
    exact ⟨a, hu, hv⟩
  · rintro ⟨a, ha, hv⟩
    exact ⟨a, (results_exact p a).mpr ⟨(), ha, hv⟩⟩

#print axioms grammar_closed
#print axioms membership_requires_value

end MCore.Research.UserProgram.Recursive
