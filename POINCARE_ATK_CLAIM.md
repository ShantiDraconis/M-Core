# POINCARE-ATK — F8 + F7

## Canonical claim

POINCARE-ATK: CLOSED_UNCONDITIONAL

- CORE_STATE: CLOSED_UNCONDITIONAL
- GAP_SHAPE: F8_FIXED_POINT + F7_LIMIT
- CORE_FORMAL_GAPS: 0
- MATERIAL_PRODUCER_GAPS: 0
- FORMAL_IMPORT_GAPS: 1
- MATHEMATICAL_FINAL_PROOF: PROVEN
- LEAN_KERNEL_FINAL_PROOF: EXTERNAL_CLASSICAL_PENDING
- POINCARE_CLAIMS: 1

## C0 -> O -> C2

- C0: closed simply-connected 3-manifold.
- O: Ricci flow with surgery / singularity control.
- C2: diffeomorphism with the 3-sphere.

The mathematical OPEN_MATH producer is closed historically by Perelman's
2002–2003 work. M-Core therefore records no unresolved mathematical producer
for Poincaré.

The remaining item is not OPEN_MATH. It is a formal-import obligation:
the complete theorem-level Ricci-flow/geometrization dependency chain has not
yet been reconstructed or imported as a kernel-verified Lean proof.

## Fail-closed rule

`CLOSED_UNCONDITIONAL` describes the established mathematical theorem.
It must not be used to claim a new Lean proof. Kernel promotion requires an
explicit `PerelmanClassicalCertificate` or a future theorem-level formal import.

## Formal endpoint

```lean
def PoincareClassification : Prop :=
  ∀ M : Closed3Manifold,
    SimplyConnected M → Diffeomorphic M S3
```

Transport:

```text
Topology -> RicciFlow -> Surgery -> Extinction -> Perelman monotonicity/geometrization -> S3 classification
```
