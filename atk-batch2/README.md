# atk-batch2 — kernel Lean dos pacotes de 12/10/2026 (lote 2)

Pacotes rodados **sem alteração** (`originals/`, conteúdo byte-idêntico aos zips; hashes em `ORIGINALS.sha256`):

| Pasta | Zip | SHA-256 do zip |
|---|---|---|
| `originals/terminal-certificates` | ATK_TERMINAL_CERTIFICATES_20261012 | ver `ORIGINALS.sha256` (arquivos) |
| `originals/exact-gate` | ATK_EXACT_GATE_20261012 | idem |
| `originals/formal-operators` | ATK_FORMAL_OPERATORS_20261012 | idem |
| `originals/material-math` | ATK_MATERIAL_MATH_20261012 | `3a769360…fa25` |

`patched/` contém cópias com correções **mínimas e rotuladas** (diff contra `originals/`):
- terminal-certificates: fechamento de comentário `-!/` → `-/`; `import` movido para antes do `/-! … -/`.
- formal-operators: `add_zero/add_comm/add_assoc` (nomes de Mathlib, ausente no projeto) → `Int.add_zero/…`.
- material-math: hipóteses que faltavam (`BddBelow (cost '' B)`; `0 < x`, `0 < y`) e `/--` solto → `/-`.
  `ATK/Refutations.lean` prova no kernel que os dois enunciados **como escritos** são falsos.

`appendix/` contém teoremas de auditoria (`ATK.Audit.*`) anexados ao texto na hora da compilação, sem
tocar nos arquivos: cada portão (`Lane`, `TerminalGate`, `ProofCertificate`, `SevenGates`, `Producer`)
é habitado **se e somente se** a meta correspondente vale — o portão não reduz a obrigação.

Workflow: `.github/workflows/atk-batch2.yml` (toolchains v4.21.0 declarada e v4.34.1; Mathlib v4.34.1
para material-math). Estado global inalterado: OPEN_MATH=true · TERMINAL_CERTIFIED=0/7.
