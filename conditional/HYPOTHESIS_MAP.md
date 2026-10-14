# Mapa de descarga de hipóteses (13/10/2026)

Pergunta: das hipóteses que os teoremas condicionais recebem, quais já estão provadas em algum
repositório ou branch? Cada hipótese provada cai, e a obrigação encolhe de verdade.

## Método

1. Indexei todas as declarações `theorem`/`lemma`/`def`/`instance` dos 32 repositórios, em todos os branches.
2. Peguei os teoremas **condicionais limpos** (sem `sorry`/`?_`/`axiom` no arquivo) que concluem um dos sete
   enunciados, um terminal ou uma obrigação, e extraí o tipo de cada hipótese explícita.
3. Uma hipótese conta como **descarregada** se existe uma declaração limpa, sem hipóteses, cuja conclusão é
   exatamente o mesmo tipo. Cada descarga foi lida à mão. Script: `conditional/scripts/hyp_map.py`.

## Números

| Teoremas condicionais limpos | Hipóteses distintas | Casaram com uma prova | Descargas genuínas |
|---|---|---|---|
| 491 | 334 | 8 | 6 |

## Descargas genuínas

| Hipótese | Usada em | Provada por | Efeito |
|---|---|---|---|
| `SATInNPGap circuitBitEncoding` | 21 teorema(s) | `m-core-p-vs-np` · `atk/p01-post-mincut-advance-20261001` · `canonical_sat_in_np_closed` | cadeia do P01: SAT ∈ NP no modelo do lane (ponte B4, parte 1) |
| `T59AllFourEliminator` | 2 teorema(s) | `m-core-beal` · `atk/beal-parity-to-t59-partition-20261001` · `T59_allFourEliminator_proved` | Beal: ramo do expoente 4 fechado pelo FLT(4) da Mathlib |
| `P01PrepPhase` | 2 teorema(s) | `m-core-p-vs-np` · `atk/p01-core-decode-physical-reject-20260930` · `prep_phase_inhabited` | cadeia do P01 |
| `CoreDecodeFailurePhysicalReject` | 2 teorema(s) | `m-core-p-vs-np` · `atk/p01-core-decode-physical-reject-20260930` · `core_decode_failure_physical_reject` | cadeia do P01 |
| `InNP CanonicalSAT` | 2 teorema(s) | `m-core-p-vs-np` · `atk/p02-equality-composition-unified` · `canonicalSAT_inNP` | cadeia do P01 |
| `P01ConstructionGap` | 1 teorema(s) | `m-core-p-vs-np` · `atk/p01-material-inhabitant-frontier-20260930` · `p01ConstructionGap` | cadeia do P01 (fecha o P01) |

### Falsos positivos descartados

| Hipótese | Por que não conta |
|---|---|
| `Type` | parâmetro de dado (`Type`), não hipótese matemática |
| `RiemannHypothesis` | a "prova" usa `axiom collapse_law` + `axiom I_ne_one` (= RH reescrita) e uma definição local de RH |

### Condicionais que ficam sem nenhuma hipótese aberta

Só a cadeia do P01 (`p01_of_core_decode_failure_physical_reject : P01ConstructionGap`). A outra ocorrência,
`hodge_material_vacuous`, é uma auditoria de vacuidade com parâmetro `Type`.

## Avanço novo encontrado: redução de Beal no lane (T59)

Branch `atk/beal-parity-to-t59-partition-20261001` do `m-core-beal` (sem `axiom`, sem `sorry`):

```
T59_beyondThree_and_residual_close_beal :
  T59FLTBeyondThree → T59ResidualEliminator → BealConjecture
```

- FLT(3) e FLT(4) vêm da Mathlib (`T50_mathlib_flt3`, `T50_mathlib_flt4`); `T59_allFourEliminator_proved` fecha o
  ramo do expoente 4.
- Sobram duas peças: **FLT para primos > 3** (teorema de Wiles, ainda não formalizado — ponte B2 estreitada) e
  **`T59ResidualEliminator`** (domínio residual misto — a parte aberta de Beal, obrigação O2 na forma do lane).

## O que continua aberto, na linguagem dos seus repositórios

As hipóteses mais usadas e ainda sem prova em lugar nenhum, por problema:

**beal**: `Beal` (6×); `FirstRealOpenMath` (6×); `CommonPrimeWitnessContract` (5×); `∀ d:BealData,CommonPrime d.a d.b d.c` (5×); `V0EquationToCommonDivisor` (4×)

**bsd**: `∀ E,Realizable E → AnalyticOrder E = MordellWeilRank E` (2×); `∀ E,Realizable E → RefinedFormula E` (2×); `GrossZagierKolyvagin M` (2×); `RankOpen M` (2×); `RefinedOpen M` (1×)

**hodge**: `BackwardAudit.Lefschetz11ConcreteLaw M` (12×); `CodimZeroConcretePayload M` (9×); `HigherCodimConcretePayload M` (9×); `HodgeMaterialMincut G M` (9×); `CycleSpanMechanics G` (9×)

**navier-stokes**: `Stabilizer` (3×); `∀ u,ActualNS u → Stabilizes component u` (2×); `Type u` (2×); `EnstrophyBlowupCriterion M` (1×); `EnstrophyAPrioriBound M` (1×)

**pvsnp**: `G21Pointwise` (12×); `D3KleeneSATBridge` (11×); `KleeneUniversalBridge` (10×); `G22Contradiction` (7×); `FailureGenerator language` (6×)

**riemann**: `MCoreRHCertificate` (6×); `RHClosure DN` (4×); `RHAdapterObligations` (3×); `¬ RiemannHypothesis` (3×); `D.GeneratorFamily` (3×)

**yang-mills**: `Producer Theory Physical MassGap` (2×); `Theory` (2×); `Genuine4D theory` (2×); `OSReconstructs theory` (2×); `PositiveMassGap theory` (2×)

## Segunda lista do inventário (8 arquivos e 6 branches)

| Repositório | Arquivo / branch | Resultado |
|---|---|---|
| `millennium-riemann-i` | `MillenniumRiemann/Theorems.lean` (main) | não conclui nenhum alvo/terminal; tem `sorry`/`?_`; 246 axiomas no branch |
| `millennium-p-vs-np-i` | `FinalProof.lean` (main) | não conclui nenhum alvo/terminal |
| `millennium-navier-stokes-i` | `src/lean/global_existence.lean` (main) | não conclui nenhum alvo/terminal; tem `sorry`/`?_`; 33 axiomas no branch |
| `millennium-bsd` | `formal/DirectEndpointRule.lean` (main) | não conclui nenhum alvo/terminal |
| `millennium-hodge` | `formal/HodgeMaterialProgram.lean` (main) | não conclui nenhum alvo/terminal |
| `millennium-yang-mills` | `formal/DirectEndpointRule.lean` (main) | não conclui nenhum alvo/terminal |
| `universal-proof-hub` | `src/lean/collapse-numerical-classical.lean` (main) | não conclui nenhum alvo/terminal; axiom no arquivo: `collapse_classical_limit`; 1 axiomas no branch |
| `proofs-multiprover` | `lean4/ProofsMultiprover/Basic.lean` (main) | não conclui nenhum alvo/terminal; tem `sorry`/`?_` |
| `m-core` | `atk/external-reference-bridges-20261013` | 1 arquivos próprios; 0 condicionais, 0 equivalências, 0 sem hipóteses; 0 arquivos com buraco |
| `m-core` | `atk/public-millennium-interface-20261013` | 1 arquivos próprios; 0 condicionais, 0 equivalências, 0 sem hipóteses; 0 arquivos com buraco |
| `m-core-p-vs-np` | `atk/g21-final-integration-clean-20260930` | 163 arquivos próprios; 35 condicionais, 7 equivalências, 0 sem hipóteses; 8 arquivos com buraco |
| `m-core-riemann` | `atk/rh-zero-residue-unconditional-producer-20260927` | 31 arquivos próprios; 3 condicionais, 0 equivalências, 0 sem hipóteses; 0 arquivos com buraco |
| `m-core-yang-mills` | `atk/ym-b60-concrete-physical-producer-20260927` | 42 arquivos próprios; 0 condicionais, 0 equivalências, 0 sem hipóteses; 0 arquivos com buraco |
| `axiomatic-millenium` | `formal/official-model-obligation-v1` | 2 arquivos próprios; 0 condicionais, 0 equivalências, 0 sem hipóteses; 0 arquivos com buraco |

Nenhum desses fecha uma obrigação. `CLOSED_MATH` segue `false`.

## Descarga por port (14/10/2026)

| Hipótese | Usada em | Provada por | Efeito |
|---|---|---|---|
| `Tendsto bdDistSq atTop (𝓝 0) → RiemannHypothesis` | 2 teorema(s): `ATK.Riemann.rh_of_bd_bound` (`m-core-riemann` e `M-Core`, branches `atk-kernel-check`, `fix/ns-scaling-false`) | `M-Core` · `atk/hypothesis-ports-20261014` · `ATK.BDDistSqPort.criterio_bd` | `bdDistSq = DN` por `rfl`; transporte da prova de B1. Não fecha O1 |

Fica aberta a forma `Tendsto bdDistSq atTop (𝓝 0) ↔ RiemannHypothesis` (`ATK.RHConvergence.rh_iff_limit_zero_of_criterion`):
a direção RH ⇒ `D_N → 0` (necessidade de Báez-Duarte) não está formalizada.
