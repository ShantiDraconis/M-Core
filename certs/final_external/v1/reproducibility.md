# Reproducibility — ELYON_FINAL_EXTERNAL v1.0.0

## Toolchain lock

Lean 4.19 is normative. Exact Lake, runner, and any additional tools actually used in the final package must be recorded in `provenance.json`.

## Freeze policy

Every GREEN component used by the final package must be pinned by exact SHA and have immutable freeze/certificate references according to the repository policy.

## Axiom audit

Forbidden: `sorryAx`, `sorry`, `admit`, theorem-carrying custom axioms, hidden oracles, and circular proof dependencies.

Allowed when genuinely required and reported: `propext`, `Classical.choice`, `Quot.sound`.

## Package hashes

`freeze.sh` generates `SHA256SUMS` over the preparatory package after all required UNSET release fields have been resolved.

## Root derivation

The final root must be computed deterministically from the exact frozen anchors of MCORE, AINUM, OS, HUB, BRAIN, APP, ELYON and the included certificate hashes. No placeholder anchor may participate in an issued root.

## Timestamps

`created_at`, `approved_at`, and `published_at` are independent timestamps.
