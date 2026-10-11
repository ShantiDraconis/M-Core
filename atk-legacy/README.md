# atk-legacy

Os arquivos Lean da sessão anterior, **sem modificação** (`src/`), compilados no kernel com o mesmo
toolchain e a mesma Mathlib que eles declaram (v4.21.0). O workflow `atk-legacy.yml` gera
`reports/legacy_report.json` com o veredito teorema a teorema.

| Arquivo | SHA-256 |
|---|---|
| `src/VerifiedAuxiliary.lean` (14 teoremas) | `06a504f9a44b2eebcadfb4446482f2081d91b4f6ad79a9431a98f4035783e4cc` (igual ao `certificate_status.json` original) |
| `src/ATK_ExactValues.lean` (7 `example` + `absorption`) | `87a5232d46bcf7126f3ae86a5e36aea1dfeae5741eaeafc1369ba2101346c502` |

`src/lakefile.original.toml` é o lakefile original, mantido como referência.

`src/VerifiedAuxiliary_patched.lean` é uma cópia com **apenas** `hodge_linear_realization` corrigido
(o original não compila: faltava `open Matrix` para a notação `*ᵥ`, e a reescrita estava invertida).
O relatório certifica o original e a cópia corrigida separadamente.
