# ATK — Unified proof compilation plan

State: SOURCE; NOT BUILT; NOT TERMINALLY CERTIFIED.

## Scope
All 16 coordinated repositories; collect branch refs including cert/, frozen/, audit/, atk/, attack/, main. Paginate branch inventory to exhaustion, and pin each chosen source commit SHA.

## Execution
1. Extract Lean modules and theorem signatures from branch snapshots; preserve immutable original refs.
2. Build an exact declaration-level dependency graph: namespace, theorem type, implicit assumptions, imports, Lean version, mathlib revision, and #print axioms.
3. Deduplicate only propositionally identical compatible lemmas; do not conflate conditional implications with material inhabitants.
4. Create versioned source namespaces and Lake packages/adapters for incompatible modules. Do not overwrite originals.
5. Compile leaf packages independently, then compile aggregate imports and audit axioms.
6. Promote verified structural lemmas only. Terminal endpoints remain OPEN_MATH until concrete terms inhabit their original propositions.
7. Publish a machine-readable manifest of repo/branch/commit/path/blob/declaration/type/build run and failures.

## Known terminal requirements
- PNP: P01ConstructionGap := Nonempty P01MachineConstruction; G21Pointwise is a separate requirement.
- Seven-lane global kernel: 7 CLOSED_MATH catalogs, 7 structural bridges, 9 material atoms (reported snapshot), green=false, buildVerified=false.
- FINAL_EXTERNAL requires math closure and separate review/issuance gates.

## Integrity constraints
FORWARD-ONLY; never edit main, frozen or certified refs. No sorry/admit/axiom for terminal claims, no false-to-true manual edits. No successful compilation or mathematical closure is asserted by this plan.
