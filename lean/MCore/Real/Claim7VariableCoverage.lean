import MCore.Real.P02BoundedComputationEncoding

namespace MCore.Real.Claim7VariableCoverage

open MCore
open MCore.CircuitK1
open MCore.Real.P02BoundedComputationEncoding

/-- Canonical CNF variable list from the Claim7 source state. -/
def cnfVarList (f : CNF) : List Nat :=
  (f.flatMap fun clause => clause.map Literal.var).eraseDups

/-- Canonical CNF variable bound from the Claim7 source state. -/
def clauseVarBound (c : Clause) : Nat :=
  c.foldl (fun acc l => max acc (l.var + 1)) 0

def cnfVarBound (f : CNF) : Nat :=
  f.foldl (fun acc c => max acc (clauseVarBound c)) 0

/-- Symmetric coupling gadget from the Claim7 source state. -/
def coverageClauses (base i v : Nat) : CNF :=
  [ [pos v, pos (base + 2 * i)]
  , [neg v, pos (base + 2 * i + 1)] ]

def coverageCore (payload : CNF) : CNF :=
  let base := cnfVarBound payload
  ((cnfVarList payload).enum.flatMap
    (fun vi => coverageClauses base vi.1 vi.2))

/-- Every literal variable occurring in a payload is recorded by cnfVarList. -/
theorem literal_var_mem_cnfVarList
    {f : CNF} {c : Clause} {l : Literal}
    (hc : c ∈ f) (hl : l ∈ c) :
    l.var ∈ cnfVarList f := by
  simp [cnfVarList]
  exact ⟨c, hc, l, hl, rfl⟩

/-- cnfVarList is monotone under append. -/
theorem cnfVarList_left_subset_append
    (a b : CNF) :
    ∀ v, v ∈ cnfVarList a → v ∈ cnfVarList (a ++ b) := by
  intro v hv
  simp [cnfVarList] at hv ⊢
  rcases hv with ⟨c, hc, l, hl, hvar⟩
  exact ⟨c, by simp [hc], l, hl, hvar⟩

theorem cnfVarList_right_subset_append
    (a b : CNF) :
    ∀ v, v ∈ cnfVarList b → v ∈ cnfVarList (a ++ b) := by
  intro v hv
  simp [cnfVarList] at hv ⊢
  rcases hv with ⟨c, hc, l, hl, hvar⟩
  exact ⟨c, by simp [hc], l, hl, hvar⟩

#print axioms MCore.Real.Claim7VariableCoverage.literal_var_mem_cnfVarList
#print axioms MCore.Real.Claim7VariableCoverage.cnfVarList_left_subset_append
#print axioms MCore.Real.Claim7VariableCoverage.cnfVarList_right_subset_append

end MCore.Real.Claim7VariableCoverage
