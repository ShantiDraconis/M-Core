import MCore.CircuitC2
import MCore.Real.P02BoundedComputationEncoding

namespace MCore.Real.Claim4NormalizedProgress

open MCore
open MCore.CircuitK1
open MCore.Real.P02BoundedComputationEncoding

def smartAnd : Circuit → Circuit → Circuit
  | .const true, y => y
  | x, .const true => x
  | .const false, _ => .const false
  | _, .const false => .const false
  | x, y => .and x y

def smartOr : Circuit → Circuit → Circuit
  | .const false, y => y
  | x, .const false => x
  | .const true, _ => .const true
  | _, .const true => .const true
  | x, y => .or x y

def clauseCircuitNorm : Clause → Circuit
  | [] => .const false
  | [l] => literalCircuit l
  | l :: ls => smartOr (literalCircuit l) (clauseCircuitNorm ls)

def cnfCircuitNorm : CNF → Circuit
  | [] => .const true
  | [clause] => clauseCircuitNorm clause
  | clause :: rest => smartAnd (clauseCircuitNorm clause) (cnfCircuitNorm rest)

def DNorm (ρ : Restriction) (t : FormulaTree) : FormulaTree :=
  MCore.CircuitC2.simplify
    (MCore.CircuitK1.restrict ρ (MCore.CircuitC2.simplify t))

def RestrictionProgressNorm (ρ : Restriction) (t : FormulaTree) : Prop :=
  DNorm ρ t ≠ MCore.CircuitC2.simplify t

theorem simplify_cnfCircuitNorm_idem (f : CNF) :
    MCore.CircuitC2.simplify (cnfCircuitNorm f) = cnfCircuitNorm f := by
  induction f with
  | nil => rfl
  | cons c cs ih =>
      cases cs with
      | nil =>
          cases c with
          | nil => rfl
          | cons l ls =>
              cases ls with
              | nil =>
                  cases l with
                  | mk v p =>
                      cases p <;> rfl
              | cons l2 ls2 =>
                  simp [cnfCircuitNorm, clauseCircuitNorm, smartOr, smartAnd,
                    MCore.CircuitC2.simplify]
      | cons c2 cs2 =>
          simp [cnfCircuitNorm, smartAnd, ih, MCore.CircuitC2.simplify]

theorem leavesZeroFree_no_progress_norm (f : CNF) :
    ¬ RestrictionProgressNorm MCore.CircuitK1.leavesZeroFree (cnfCircuitNorm f) := by
  intro h
  apply h
  unfold RestrictionProgressNorm DNorm
  rw [simplify_cnfCircuitNorm_idem]
  induction cnfCircuitNorm f with
  | input i => rfl
  | const b => rfl
  | not t ih =>
      simp [MCore.CircuitK1.restrict, MCore.CircuitC2.simplify, ih,
        MCore.CircuitK1.leavesZeroFree]
  | and a b iha ihb =>
      simp [MCore.CircuitK1.restrict, MCore.CircuitC2.simplify, iha, ihb,
        MCore.CircuitK1.leavesZeroFree]
  | or a b iha ihb =>
      simp [MCore.CircuitK1.restrict, MCore.CircuitC2.simplify, iha, ihb,
        MCore.CircuitK1.leavesZeroFree]

#print axioms MCore.Real.Claim4NormalizedProgress.leavesZeroFree_no_progress_norm

end MCore.Real.Claim4NormalizedProgress
