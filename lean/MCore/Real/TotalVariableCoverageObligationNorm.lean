import MCore.Real.Claim4NormalizedProgress
import MCore.Real.Claim7VariableCoverage

namespace MCore
namespace Real
namespace P02Lane4TotalVariableCoverageNorm

open CircuitK1
open P02BoundedComputationEncoding
open Claim4NormalizedProgress
open Claim7VariableCoverage

private theorem mem_zipIdx_of_mem
    {α : Type} (x : α) :
    ∀ (l : List α) (n : Nat), x ∈ l → ∃ i : Nat, (x, i) ∈ l.zipIdx n := by
  intro l
  induction l with
  | nil =>
      intro n hx
      simp at hx
  | cons a as ih =>
      intro n hx
      simp only [List.mem_cons] at hx
      rcases hx with rfl | hx
      · exact ⟨n, by simp⟩
      · obtain ⟨i, hi⟩ := ih (n + 1) hx
        exact ⟨i, by simp [hi]⟩

/-- Every payload variable is copied into the total-variable coverage core. -/
theorem payload_var_mem_coverageCore
    {payload : CNF} {v : Nat}
    (hv : v ∈ cnfVarList payload) :
    v ∈ cnfVarList (coverageCore payload) := by
  obtain ⟨i, hi⟩ :=
    mem_zipIdx_of_mem v (cnfVarList payload) 0 hv
  have hclause :
      [pos v, pos (cnfVarBound payload + 2 * i)] ∈ coverageCore payload := by
    simp only [coverageCore, List.mem_flatMap]
    refine ⟨(v, i), hi, ?_⟩
    simp [coverageClauses]
  apply Claim7VariableCoverage.mem_eraseDups_iff.mpr
  simp only [List.mem_flatMap]
  refine ⟨[pos v, pos (cnfVarBound payload + 2 * i)], hclause, ?_⟩
  simp [pos]

#print axioms MCore.Real.P02Lane4TotalVariableCoverageNorm.payload_var_mem_coverageCore

/-- Restricting a literal whose variable is free leaves its normalized circuit unchanged. -/
private theorem restrict_literalCircuit_of_none
    (ρ : Restriction) (l : Literal)
    (hρ : ρ l.var = none) :
    MCore.CircuitK1.restrict ρ (literalCircuit l) = literalCircuit l := by
  cases l with
  | mk v p =>
      cases p <;> simp [literalCircuit, MCore.CircuitK1.restrict, hρ]

private theorem restrict_smartOr_of_fixed
    (ρ : Restriction) (x y : Circuit)
    (hx : MCore.CircuitK1.restrict ρ x = x)
    (hy : MCore.CircuitK1.restrict ρ y = y) :
    MCore.CircuitK1.restrict ρ (smartOr x y) = smartOr x y := by
  cases x <;> cases y <;>
    simp_all [smartOr, MCore.CircuitK1.restrict] <;>
    split <;> simp_all [MCore.CircuitK1.restrict]

private theorem restrict_smartAnd_of_fixed
    (ρ : Restriction) (x y : Circuit)
    (hx : MCore.CircuitK1.restrict ρ x = x)
    (hy : MCore.CircuitK1.restrict ρ y = y) :
    MCore.CircuitK1.restrict ρ (smartAnd x y) = smartAnd x y := by
  cases x <;> cases y <;>
    simp_all [smartAnd, MCore.CircuitK1.restrict] <;>
    split <;> simp_all [MCore.CircuitK1.restrict]

/-- A restriction free on every variable of a clause fixes its normalized circuit. -/
private theorem restrict_clauseCircuitNorm_id
    (ρ : Restriction) (c : Clause)
    (hfree : ∀ l : Literal, l ∈ c → ρ l.var = none) :
    MCore.CircuitK1.restrict ρ (clauseCircuitNorm c) = clauseCircuitNorm c := by
  induction c with
  | nil => rfl
  | cons l ls ih =>
      cases ls with
      | nil =>
          have hl : ρ l.var = none := hfree l (by simp)
          simpa [clauseCircuitNorm] using restrict_literalCircuit_of_none ρ l hl
      | cons l2 ls2 =>
          have hl : ρ l.var = none := hfree l (by simp)
          have htail : ∀ x : Literal, x ∈ (l2 :: ls2) → ρ x.var = none := by
            intro x hx
            exact hfree x (by simp [hx])
          exact restrict_smartOr_of_fixed ρ
            (literalCircuit l) (clauseCircuitNorm (l2 :: ls2))
            (restrict_literalCircuit_of_none ρ l hl)
            (ih htail)

/-- A restriction free on every CNF variable fixes the normalized CNF circuit. -/
private theorem restrict_cnfCircuitNorm_id
    (ρ : Restriction) (f : CNF)
    (hfree : ∀ v : Nat, v ∈ cnfVarList f → ρ v = none) :
    MCore.CircuitK1.restrict ρ (cnfCircuitNorm f) = cnfCircuitNorm f := by
  induction f with
  | nil => rfl
  | cons c cs ih =>
      have hcfree : ∀ l : Literal, l ∈ c → ρ l.var = none := by
        intro l hl
        exact hfree l.var
          (literal_var_mem_cnfVarList (f := c :: cs) (c := c) (l := l) (by simp) hl)
      cases cs with
      | nil =>
          simpa [cnfCircuitNorm] using restrict_clauseCircuitNorm_id ρ c hcfree
      | cons c2 cs2 =>
          have htail : ∀ v : Nat, v ∈ cnfVarList (c2 :: cs2) → ρ v = none := by
            intro v hv
            exact hfree v
              (cnfVarList_right_subset_append [c] (c2 :: cs2) v hv)
          exact restrict_smartAnd_of_fixed ρ
            (clauseCircuitNorm c) (cnfCircuitNorm (c2 :: cs2))
            (restrict_clauseCircuitNorm_id ρ c hcfree)
            (ih htail)

/-- TARGET2a: if the restriction fixes none of the CNF variables, normalized progress is impossible. -/
theorem no_restricted_var_implies_no_progress_norm
    (ρ : Restriction) (f : CNF)
    (hfree : ∀ v : Nat, v ∈ cnfVarList f → ρ v = none) :
    ¬ RestrictionProgressNorm ρ (cnfCircuitNorm f) := by
  intro hprogress
  apply hprogress
  simp [DNorm, simplify_cnfCircuitNorm_idem,
    restrict_cnfCircuitNorm_id ρ f hfree]

#print axioms MCore.Real.P02Lane4TotalVariableCoverageNorm.no_restricted_var_implies_no_progress_norm


/-- TARGET2b: normalized progress exposes at least one restricted CNF variable. -/
theorem progressNorm_implies_restricted_var
    (ρ : Restriction) (f : CNF)
    (hprogress : RestrictionProgressNorm ρ (cnfCircuitNorm f)) :
    ∃ v : Nat, v ∈ cnfVarList f ∧ ρ v ≠ none := by
  by_contra hnone
  have hfree : ∀ v : Nat, v ∈ cnfVarList f → ρ v = none := by
    intro v hv
    by_contra hne
    exact hnone ⟨v, hv, hne⟩
  exact (no_restricted_var_implies_no_progress_norm ρ f hfree) hprogress

#print axioms MCore.Real.P02Lane4TotalVariableCoverageNorm.progressNorm_implies_restricted_var

/-- Normalized core-aware progress. Both payload+core and core are measured only
after canonical normalization, so representation-only simplification is excluded. -/
def CoreAwareProgressNorm
    (ρ : Restriction)
    (payload core : CNF) : Prop :=
  RestrictionProgressNorm ρ (cnfCircuitNorm (payload ++ core)) ∧
  RestrictionProgressNorm ρ (cnfCircuitNorm core)

/-- Exact normalized coverage obligation for a payload/core pair. -/
def CoreAwareProgressCoverageNorm
    (payload core : CNF) : Prop :=
  ∀ ρ : Restriction,
    RestrictionProgressNorm ρ (cnfCircuitNorm (payload ++ core)) →
      CoreAwareProgressNorm ρ payload core

/-- Terminal normalized coverage obligation for the total-variable gadget.
This is deliberately a proposition only: this file does not postulate or
manufacture an inhabitant. -/
def TotalVariableCoverageObligationNorm
    (payload : CNF) : Prop :=
  CoreAwareProgressCoverageNorm payload (coverageCore payload)

theorem totalVariableCoverageObligationNorm_unfold
    (payload : CNF) :
    TotalVariableCoverageObligationNorm payload ↔
      ∀ ρ : Restriction,
        RestrictionProgressNorm ρ
          (cnfCircuitNorm (payload ++ coverageCore payload)) →
        CoreAwareProgressNorm ρ payload (coverageCore payload) := by
  rfl

#print axioms MCore.Real.P02Lane4TotalVariableCoverageNorm.totalVariableCoverageObligationNorm_unfold

end P02Lane4TotalVariableCoverageNorm
end Real
end MCore
