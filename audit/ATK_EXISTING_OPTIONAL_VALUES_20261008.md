# ATK — existing values vs optional fields (2026-10-08)

This ledger records confirmed existing data without modifying frozen mathematical artifacts.

| Consumer | Field | Available source | Resolution |
|---|---|---|---|
| scripts/global_final_proof_linker.py | pnp_reuse fallback None | final-proof/pnp_reuse_chain.json | Present on main; the loader already reads it. Keep None as a legitimate missing-file fallback. |
| certs/final_external/v1/manifest.json | root.value, FINAL_ROOT_MATH | partial source SHA and certificates | Keep null: a material final root has not been demonstrated. |
| certs/final_external/v1/manifest.json | human_review UNSET | none validated | Preserve UNSET pending human approval. |
| certs/final_external/v1/manifest.json | production UNSET | none validated | Preserve UNSET pending production evidence. |
| P01 tape machines | Option Bool none | blank tape semantics | Keep none, not a missing proof value. |

## Synchronization rule

Existing structural evidence may be linked by SHA, but no `None`/`null` may be replaced with a mathematical witness or final root without a matching typed producer and kernel/axiom audit. This ledger is metadata only, not a final certificate.
