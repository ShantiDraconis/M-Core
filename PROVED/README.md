# PROVED — formal audit results

This directory is a navigation index, not a replacement for Lean source files.
The source of truth is `MCore/Proof.lean` and its imported dependencies.
**Verification gate:** all entries remain *formalized, CI pending* until the
specific root-module compilation passes on the frozen commit.

| Result | Source | Precisely established |
| --- | --- | --- |
| A1 | [A1Amplitude](../MCore/A1Amplitude.lean), [Proof](../MCore/Proof.lean) | No universal fixed upper gap for a degree-one homogeneous functional with a positive witness along an unbounded amplitude ray |
| A2 | [A2SelfRef](../MCore/A2SelfRef.lean), [DAG](../MCore/DAG.lean), [Proof](../MCore/Proof.lean) | The specified cycle fails the declared audit gate; no general impossibility of solving cyclic systems |
| A3 | [A3Zero](../MCore/A3Zero.lean), [Proof](../MCore/Proof.lean) | Incompatible prescribed path limits preclude a single common extension value; concrete invariant paths are not supplied |
| G1Fix (conditional) | [Proof](../MCore/Proof.lean) | Algebraic estimate assuming energy and coefficient bounds; does not derive the Navier–Stokes estimate |

## Acceptance rules

- Check the `M-Core audit proof verification` GitHub Actions workflow.
- Review hypotheses and `#print axioms` before marking a theorem kernel-verified.
- A theorem about an abstract audit model is not automatically a theorem
  about physical Navier–Stokes solutions.
- The root `MCore/` tree is compiled separately from the `lean/` library.
- No theorem is promoted merely by changing a status flag or folder name.

See [freeze](../FREEZE_v1.md) and [proof ledger](../MCore/PROOF_STATUS.md).
