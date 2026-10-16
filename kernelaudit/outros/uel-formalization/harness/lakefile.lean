import Lake
open Lake DSL

/-! Harness de auditoria (não é a configuração original do repositório): Lean 4.34.1 e a Mathlib
fixada do M-Core (atk-kernel). Só muda a configuração de build; os arquivos .lean são cópias
verbatim do ramo auditado. -/
package auditoria

require mathlib from git "https://github.com/leanprover-community/mathlib4.git" @ "d13f23b723b8a846827a245b89c10fc7d3f11612"

lean_lib UELFormal where
  srcDir := "formalization/lean"
  roots := #[`UETheta_Axioms, `UETheta_to_RH]
