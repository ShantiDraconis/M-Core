# ELYON_FINAL_EXTERNAL v1.0.0 — MATERIAL-ONLY PREPARATORY

## Status

This directory is a **preparatory, non-issued** certificate package.

```text
package_state          PREPARATORY
freeze_state           FROZEN_PREPARATORY
FINAL_EXTERNAL_ISSUED  false
FINAL_ROOT             null
GLOBAL FINAL_PROOF     0/7
```

No `FINAL_ROOT` may be generated while a material, mechanical, or release blocker remains open.

## P vs NP terminal boundary

The former "two mathematical gaps" description is superseded.

There are exactly two **operational inputs**, of different classes:

```text
MATERIAL:
  G21Pointwise
  ↔ P02Target
  ↔ ¬ InP SATTarget

MECHANICAL:
  Nonempty (P01VerifierPhase P01WitnessPrepGlobal.prepPhase.layout)
  → P01ConstructionGap
```

Only `G21Pointwise` counts as `OPEN_MATH`.

`P01VerifierPhase ...` is executable/formal machine construction. It may block the endpoint, but it is not a mathematical lower-bound conjecture.

The following downstream wiring is already closed and must not be reopened:

- G2.2 consequence/equivalence wiring;
- G3 normalized external contract;
- FinalExternal integration;
- FinalExternalTwoGap reduction.

Thus the exact consumer chain is:

```text
P01VerifierPhase
  → P01ConstructionGap
                         ┐
G21Pointwise             ├→ FinalExternalGap
                         ┘
  → OfficialPneqNP
  → FINAL_ROOT_MATH[P_VS_NP]
```

## Seven material slots

The global `FINAL_PROOF` count remains `0/7`. Wiring does not create extra slots. The seven material targets are recorded in:

- `MATERIAL_ONLY_BOUNDARY_20260930.json`
- `FINAL_ROOT_CLOSURE_PLAN_20260930.json`
- `lean/MCore/FinalFail/MaterialProducerNormalForms.lean`

## Hash levels

`freeze.sh` validates and hashes the preparatory package and generates `PREPARATORY_ROOT`.

`finalize_root.sh` is the fail-closed final-root gate. It refuses to compute `FINAL_ROOT` unless:

1. `FINAL_ROOT_MATH` is populated;
2. the P01 mechanical blocker is closed;
3. `G21Pointwise` is closed for the P-vs-NP external lane;
4. human review authority, quorum and evidence policy are set;
5. production app, crypto and hardware fields are set;
6. the final payload passes deterministic hash verification.

Even after `FINAL_ROOT` is computed, `FINAL_EXTERNAL_ISSUED=true` remains a separate approval/issuance action governed by the recorded human-review policy.
