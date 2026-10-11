# PUBLICATION/MASTER

One structure for every proof in the M-Core programme, built from the Lean kernel.

| File | What it is |
| --- | --- |
| `FINAL_PROOF_STRUCTURE.md` / `.json` | The final structure: for each of the seven problems, the checked tree, the kernel results, the closed mathematics and bridges recorded in the lane catalog, and the exact open producer. Generated; do not edit. |
| `sources.json` | The exact tree (repository, branch, commit, CI run) whose inventory feeds each problem. |
| `lanes.json` | `AxiomaticMillenium.sevenLaneArchitectures`, dumped with `#eval` from axiomatic-millenium. |
| `inventories/<id>/PROOF_INVENTORY.json` | Snapshot of `scripts/proof_inventory.py` output for each checked tree, as committed by CI on its evidence branch. |

Regenerate with `python3 scripts/build_master_dossier.py` from the repository root.

## Reading it correctly

- A green tree means: every module the root imports compiles, and every theorem uses only `propext`, `Classical.choice` and `Quot.sound`. It is build state, not endpoint credit.
- The final statement is the conjunction of seven endpoints. Each closes only through its exact open producer or one genuine counterexample. None is inhabited: **0/7**, `FINAL_EXTERNAL_ISSUED = false`.
- The gap lists come from the kernel: PROVED means a theorem has exactly that proposition as its type and uses only standard axioms.
