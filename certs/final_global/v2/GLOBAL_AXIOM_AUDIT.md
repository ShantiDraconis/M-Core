# GLOBAL_AXIOM_AUDIT — v2 (2026-10-09)

Política de `certs/final_external/v*/manifest.json → axiom_policy`:
- permitidos: `propext`, `Classical.choice`, `Quot.sound`;
- proibidos: `sorry`, `admit`, `sorryAx`, axiomas portadores de teorema, oráculos ocultos e circularidade.

## 1. M-Core

| Item | Valor |
|---|---|
| Commit | `33983a4cc7d1fa4869f08e453f39fc51f3d1b7f4` (`frozen/closed-math-global-green-33983a4c`) |
| Run | `37914524820` |
| Método | `Lean.collectAxioms` sobre **todas** as constantes-teorema `MCore.*` (`audit/kernel/AxiomAudit.lean`) |
| Teoremas | 620; 489 sem axiomas e 131 só com axiomas permitidos |
| Axiomas proibidos / declarações `axiom` / `sorry` | **0 / 0 / 0** |

Desde o v1 entraram `Semantic/RiemannDual.lean`, `Semantic/NavierStokesClay.lean`
e o firewall de vinculação no registro. Todos usam só os axiomas permitidos;
`Classical.choice` vem do Mathlib (ζ, cálculo em ℝ³).

## 2. P01 (m-core-p-vs-np)

`P01RawTotalizationProducer.p01ConstructionGap_closed`:
- axiomas `[propext, Classical.choice, Quot.sound]`;
- nenhum `implemented_by`, `extern`, `unsafe`, `native_decide`, `opaque` ou `axiom` no fecho de 151 módulos;
- verificado localmente e no run `37913791428`.

**Separação (BFS sobre o fecho completo de constantes):** são 4.452 constantes e
nenhuma é `PneqNP`, `InP`, `G21Pointwise`, `UniversalFailure`, `FailureGenerator`,
`P02Target`, `SATFailGap`, `PolyDTMCandidate` ou `sorryAx`. O controle positivo
(`failure_generator_iff_universal_failure`) alcança 3 dessas constantes, então o
detector funciona. Código: `audit/P01SeparationAudit.lean` na branch
`atk/p01-closure-audit-20261009`, run `37915584427`. Uma auditoria equivalente de outra sessão está em
`atk/pnp-recovery-integration-20261008`.

## 3. Repositórios de origem — situação após os PRs desta auditoria

| Repositório | Antes | PR | Depois do merge |
|---|---|---|---|
| navier-stokes-critical-barrier-audit | 34 declarações `axiom` em 12 arquivos TARGET, em `main`, `frozen/*` e `cert/*` | #41 (aberto) | 0 axiomas. **5 desses axiomas eram falsos**, e todo ambiente que os importasse era inconsistente. Um exemplo: `Alignment_Bound_TARGET` afirmava `alignment ≤ 0.9` para *todo* real `alignment`. Agora são teoremas `…_statement_false`. |
| millennium-riemann-I | `riemann_hypothesis` circular (`collapse_law` + `I_ne_one`; ζ axiomatizada) | #10 (aberto) | rotulado como **não é prova**; nenhuma declaração removida |
| m-core-bsd | 3 arquivos `open_math/` com `sorry`, fora do `srcDir` | — | sem mudança (rascunhos declarados fora da árvore certificada) |
| demais repositórios do registro | branches protegidas limpas | — | — |

Os `frozen/*` e `cert/*` do NS continuam com os axiomas antigos. Branches
congeladas não são reescritas; o PR corrige o `main`.

## 4. Circularidade

- M-Core: sem axiomas locais, logo nenhuma circularidade via axioma. Os
  "habitantes aceitos" recebem o conteúdo como argumento.
- P01: o fecho não menciona `G21Pointwise`, `PneqNP`, `InP` nem candidatos DTM.
- `millennium-riemann-I`: circular (ver §3).
