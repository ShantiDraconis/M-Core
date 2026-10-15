# Os 21 registros da auditoria de linguagem no kernel (15/10/2026)

Ramo `atk/kernel-21-registros`, workflow `Kernel 21 registros`, runs 38815095065, 38815956454 e
38816632489. Cada registro foi compilado no seu próprio projeto, na versão de Lean do ramo
(4.34.1 no M-Core, 4.19.0 nos outros), e os teoremas críticos passaram por `#print axioms`.
Detalhes em `ATK_KERNEL_BUILD_RESULTS.csv` e `ATK_AXIOM_AUDIT.csv`.

## Resultado: nenhum registro fecha um problema

| Registro | Build | Axiomas | O que é |
|---|---|---|---|
| R01 LogicAudit (M-Core) | verde | os 3 padrão | firewall: `D_N ≡ 0` satisfaz a cota |
| R02 GlobalPositiveMaterialFrontier (M-Core) | verde | os 3 padrão | implicação `RH → ¬ Nonempty RiemannInterpretation` |
| R03 ObrigacoesMinimas (M-Core) | verde | os 3 padrão | `O1 → D_N → 0`; O1 aberta |
| R04 P01 falha esperada (P vs NP) | base verde, sonda falha | — | `Nonempty P01MachineConstruction` sem prova |
| R05 P01TerminalCertificate | **falha** (31 erros) | — | não compila |
| R06 P01TerminalMaterialCertificate | **falha** (31 erros) | — | não compila |
| R07 PNPMaterialAtoms | **falha** (2 metas abertas) | — | átomos em aberto |
| R08–R21 | não rodados | — | 6 repositórios não anexados a esta sessão |

## Correções feitas

* As cópias anotadas de R02 e R03 em `audit/language-corrected/` não compilavam: o cabeçalho de
  proveniência era `/-! … -/` antes do `import`. Virou comentário comum `/- … -/`; enunciados,
  provas e imports idênticos. Agora compilam (run 38816632489).

## Achado: lema falso na cadeia P01 (P vs NP)

`P01DecodeCoreLaws.decodeCircuitCore_size_lt` afirma `size phi < fuel` para todo circuito
decodificado. É falso: `decodeCircuitCore 1 [false, false, false, false] = some (.input 0, [])` e
`size (.input 0) = 1`. A refutação está no kernel sem nenhum axioma
(`kernelaudit/pnp/contraexemplos/DecodeSizeLtFalso.lean`). O combustível limita a profundidade,
não o tamanho. Os outros erros de R05/R06 estão em `P01FiniteCodec` (usa `nlinarith` sem Mathlib),
`P01InputNodeCompositeRun`, `P01NeedExprTagDecode` e `P01IntegratedAssembly` (referências a
`seqMachine`, `V.blank_none`, `verifierFinMachine_blank` que não elaboram). O CI do próprio
m-core-p-vs-np também falha nesses ramos (runs 36792394294 e 36791737141). Mesmo corrigida, P01
seria `SAT ∈ NP`, não `P ≠ NP`.

`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`, `OPEN_MATH = true`.
