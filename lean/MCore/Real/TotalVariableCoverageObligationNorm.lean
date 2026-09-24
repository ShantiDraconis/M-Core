import MCore.Real.Claim4NormalizedProgress
import MCore.Real.Claim7VariableCoverage

namespace MCore
namespace Real
namespace P02Lane4TotalVariableCoverageNorm

open CircuitK1
open P02BoundedComputationEncoding
open Claim4NormalizedProgress
open Claim7VariableCoverage

/-- Every payload variable is copied into the total-variable coverage core. -/
theorem payload_var_mem_coverageCore
    {payload : CNF} {v : Nat}
    (hv : v ∈ cnfVarList payload) :
    v ∈ cnfVarList (coverageCore payload) := by
  have hi : ∃ i : Nat, (v, i) ∈ (cnfVarList payload).zipIdx := by
    simpa using (List.mem_zipIdx.mpr hv)
  rcases hi with ⟨i, hi⟩
  apply Claim7VariableCoverage.mem_eraseDups_iff.mpr
  simp only [coverageCore, List.mem_flatMap]
  refine ⟨(v, i), hi, ?_⟩
  simp [coverageClauses, cnfVarList]

#print axioms MCore.Real.P02Lane4TotalVariableCoverageNorm.payload_var_mem_coverageCore

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
