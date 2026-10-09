# GLOBAL_KERNEL_RUNS — v2

Toolchain: Lean **4.19.0** (`6caaee842e94`), Lake 5.0.0-6caaee8, Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`, GitHub Actions `ubuntu-24.04`
(24.04.5 LTS). Evidência bruta em `audit-results/<sha>` (ver `../v1` para os
runs de 2026-10-08 18:00–19:00).

## M-Core (`atk/global-audit-20261008`, PR #15)

| Run | Commit | Concluído (UTC) | Módulos `lean/` | Proveniência | Teoremas / proibidos | Gates |
|---|---|---|---|---|---|---|
| `37847421955` | `ecb5f513` | 2026-10-08T21:37:59Z | 44/44 | 6/6 | 620 / 0 | FE v1 ✅ |
| `37851084289` | `ae70fb74` | 2026-10-08T22:12:18Z | 44/44 | 6/6 | 620 / 0 | FE v1, v2 ✅ |
| `37912560620` | `e1a3b4ab` (merge com `main`) | 2026-10-09 | ✅ | ✅ | — | também `m-core-commercial-release` ✅, que falha no `main` |
| **`37914524820`** | **`33983a4c`** | **2026-10-09T10:03:55Z** | **44/44** | **6/6** | **620 / 0** | FE v1, v2, v3 ✅; FINAL_GLOBAL v1 `verify.sh` ✅ |

`33983a4c` está congelado em `frozen/closed-math-global-green-33983a4c`. O TSV
de axiomas desse run está em [`axiom_audit_run37914524820.tsv`](axiom_audit_run37914524820.tsv),
com 489 teoremas sem axiomas e 131 só com axiomas permitidos.

## m-core-p-vs-np — P01 (SAT ∈ NP)

| Run | Commit | Resultado |
|---|---|---|
| **`37913791428`** | `d97a56e1` (`frozen/p01-closure-audit-green-d97a56e1`, base `0dd09383`) | `lake build MCore.Real.P01RawTotalizationProducer` ✅; auditoria fail-closed PASS: tipo `P01ConstructionGap`, axiomas `[propext, Classical.choice, Quot.sound]`; 42/42 arquivos do enunciado idênticos a `main@9efeb9b7` |
| **`37915584427`** | `9614fc19` (`atk/p01-closure-audit-20261009`) | mesma auditoria + **separação**: o fecho (4.452 constantes) não alcança `InP`, `PneqNP`, `G21Pointwise` etc.; o controle positivo alcança 3 |
| local | `0dd09383` | fecho de 151 módulos compilado com Lean 4.19.0 sem Mathlib; controle negativo falha como esperado |
| `36897479263` | `15b6c360` | registrado por outra sessão (arquivos idênticos); não reexecutado aqui |

## Outros repositórios

| Repositório | PR | Run | Resultado |
|---|---|---|---|
| navier-stokes-critical-barrier-audit | #41 | `37852799729` (`atk-axiom-free-targets.yml`) | ✅ os 12 arquivos TARGET compilam com `axiom_decls=0`. Os checks vermelhos `Audit integrity` e `Millennium multiprover` falham também no `main` (último run no `main`: `37866982404`). |
| millennium-riemann-I | #10 | `policy-guard` | ✅ |
