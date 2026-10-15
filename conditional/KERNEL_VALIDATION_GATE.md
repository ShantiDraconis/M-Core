# ATK — Kernel validation gate (language audit)

This audit branch records source copies; it does not automatically compile them as Lean modules. The actual kernel must check each original project under its own dependency lockfile and Lean version.

## Reproducible commands

From the root of each checked-out repository:

```bash
lake env lean --version
lake build
```

For each module that belongs to the configured Lean source tree, create an audit module that imports it and prints axioms:

```lean
import ATK.FinalRoot
import ATK.ClosedMath

#print axioms ATK.FinalRoot.raiz_de_produtores
#print axioms ATK.FinalRoot.verde_fiel_iff
#print axioms ATK.ClosedMath.closedMath_of_obligations
```

Use `lake env lean <audit-file>.lean` for the inspection. Do not treat `#print axioms` as an automated proof of semantic faithfulness; check target definitions, imported axioms, typeclass instances, universe parameters, and any model-to-original bridge.

## Acceptance states

- `SOURCE`: source file retrieved.
- `LANGUAGE_REVIEWED`: terminology annotated without changing the proof.
- `BUILD_GREEN`: a recorded build command exited successfully.
- `KERNEL_PROVEN`: a specific declaration has a checked proof term, with all dependencies disclosed.
- `TERMINAL_CERTIFIED`: the original mathematical statement is proved without extra conjectural assumptions.

## Pending

No kernel run has been performed as part of this language-audit batch. No terminal theorem is certified by these file copies. Files under `audit/language-corrected/` are audit artifacts and may not be part of the Lean module path. Intentionally failing probe files must be excluded from success builds and tested separately as negative tests.

Current state: `BUILD_PENDING`; `OPEN_MATH=true`; `CLOSED_MATH=false`.
