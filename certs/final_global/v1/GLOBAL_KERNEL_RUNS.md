# GLOBAL_KERNEL_RUNS

Toolchain em todas as execuções: Lean **4.19.0** (`6caaee842e94`, Release),
Lake 5.0.0-6caaee8, Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` (tag v4.19.0),
runner GitHub Actions `ubuntu-24.04` (Ubuntu 24.04.5 LTS).

Workflow: `.github/workflows/atk-global-kernel-audit.yml`. Ele compila **cada**
módulo de `lean/MCore` individualmente (não só o alvo padrão, que cobre 19 dos 41),
roda o auditor genérico de axiomas, compila a árvore de proveniência da raiz,
reexecuta `freeze.sh` numa cópia e publica a evidência bruta numa branch
`audit-results/<sha>` (logs e artefatos do Actions não são baixáveis pelo proxy
desta sessão, então a evidência é lida via git).

## Execuções desta auditoria

| Run | Commit fonte | Concluído (UTC) | Biblioteca `lean/` | Proveniência `MCore/` | Axiomas | `freeze.sh` | Evidência |
|---|---|---|---|---|---|---|---|
| `37819802090` | `8b7099e7bb86bd305812ad57503469d5c1c027f3` | 2026-10-08T17:57:12Z | 41/41 + alvo padrão ✅ | 1/6 (defeito do harness: ordem do `LEAN_PATH`) | 582 teoremas, 0 proibidos | rc 0, hashes idênticos | `audit-results/8b7099e7…` |
| `37824483365` | `5cb7cd7c85836eaf19ab9511cd040bb826f2eb0a` | 2026-10-08T18:33:12Z | 41/41 + alvo padrão ✅ | 4/6 (`A4Scale`: `λ` reservado; `Admissible` importa `A4Scale`) | idêntico ao anterior | rc 0, idêntico | `audit-results/5cb7cd7c…` |
| `37825452119` | `9a7f1f04b718dfbe931e07599ab1d34272804fcd` | 2026-10-08T18:41:22Z | 41/41 + alvo padrão ✅ | **6/6** ✅ | idêntico ao anterior | rc 0, idêntico | `audit-results/9a7f1f04…` (commit `d7810b86…`) |

A árvore `lean/` é a mesma nas três execuções (`34bbe53c6fb1558539c62cf70cbe2aeeab810f00`);
o TSV de axiomas é byte a byte idêntico nas três.
`9a7f1f04` foi congelado como `frozen/closed-math-global-green-9a7f1f04`.

## Verificação local cruzada (sandbox da auditoria)

Lean 4.19.0 (release oficial do GitHub) sem Mathlib — o cache do Mathlib e o
`reservoir.lean-lang.org` não são acessíveis daqui.

| Etapa | Resultado |
|---|---|
| `main@53d58bce`, cadeia RPA | `RPAConfirmation` falha ("field must be a proof"); `RPALattice` e `RPALatticeCube3` não compilam por dependência |
| Após correções, 13 módulos livres de Mathlib | 13/13 compilam |
| Auditor de axiomas sobre esses 13 | 259 teoremas, 229 sem axiomas, 30 só `propext`/`Quot.sound`, 0 proibidos |
| Teste do renomeamento `∀ «λ» u, …` | aceito; `#print` mostra o mesmo enunciado |

## Estado do `main` antes da auditoria (para registro)

No SHA `53d58bceed3424a435eb54e01cd6d3f17324a630` todos os workflows que compilam
Lean falharam: `M-Core Final Proof Integrated` (run `37693290993`),
`M-Core Full Chain Archive Audit` (`37693290911`), `m-core-commercial-release`
(`37693291169`) e o `Final Proof Miner` agendado (20 falhas seguidas, a mais recente
`37816791089`). O último commit do `main` com `lake build` verde é `c71bbc0`; a
quebra começa em `32981d6`. Os commits RPA posteriores (`4c4d22d` … `d4ae1f2`)
foram documentados como "kernel-linked" sem que o kernel os tivesse aceitado.

O `Final Proof Miner` também não baixava o cache do Mathlib; foi corrigido em
`5cb7cd7c` (`lake exe cache get`).
