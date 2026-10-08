import Lean

/-!
# ATK global axiom audit (meta-program, not part of the certified library)

`#atk_axiom_audit` walks every *imported* constant whose name starts with
`MCore`, and for each theorem prints one tab-separated line

    THEOREM <name> <axioms>

using `Lean.collectAxioms`, i.e. the same traversal that backs `#print axioms`.
It also prints every `axiom` declaration found under `MCore` (there should be
none) and a final summary line.  It never adds declarations, axioms or proofs.

Usage: generate a driver file that `import`s the modules to audit followed by
`import ATKAudit.AxiomAudit` and the single command `#atk_axiom_audit`.
-/

open Lean Elab Command

def atkAllowedAxioms : List Name := [``propext, ``Classical.choice, ``Quot.sound]

elab "#atk_axiom_audit" : command => do
  let env ← getEnv
  let mut thms : Array (String × List Name) := #[]
  let mut userAxioms : Array String := #[]
  for (n, ci) in env.constants.map₁.toList do
    if (`MCore).isPrefixOf n && !n.isInternal then
      match ci with
      | .thmInfo _ =>
          let axs ← Lean.collectAxioms n
          thms := thms.push (n.toString, axs.toList)
      | .axiomInfo _ => userAxioms := userAxioms.push n.toString
      | _ => pure ()
  let sorted := thms.qsort (fun a b => a.1 < b.1)
  let mut clean := 0
  let mut allowedOnly := 0
  let mut forbidden := 0
  for (n, axs) in sorted do
    let bad := axs.filter (fun a => !atkAllowedAxioms.contains a)
    if axs.isEmpty then clean := clean + 1
    else if bad.isEmpty then allowedOnly := allowedOnly + 1
    else forbidden := forbidden + 1
    let tag := if bad.isEmpty then "OK" else "FORBIDDEN"
    IO.println s!"THEOREM\t{tag}\t{n}\t{axs}"
  for a in userAxioms.qsort (· < ·) do
    IO.println s!"USER_AXIOM\t{a}"
  IO.println s!"SUMMARY\ttheorems={sorted.size}\tno_axioms={clean}\tallowed_only={allowedOnly}\tforbidden={forbidden}\tuser_axioms={userAxioms.size}"
