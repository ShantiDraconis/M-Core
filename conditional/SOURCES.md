# Proveniência

Repositórios lidos em 2026-10-13 (HEAD da branch padrão). Nenhum foi alterado.

| Repositório | Commit | Uso aqui |
|---|---|---|
| `ShantiDraconis/M-Core` | `6df7dfc33a56bb3c7611e173ed1c3483d9ac82c7` | `atk-kernel/` inteiro (ATK/*.lean, scripts, numerics, lakefile) copiado sem alteração; registro dos 7 terminais (`FinalProofRegistry.lean`, `DirectProducerCuts.lean`) |
| `ShantiDraconis/m-core-openai-ns-audit` | `9e845430c14b19308a1a160d2c376ccf828b6c1e` | formato do kernel, `check_axioms.py`, `BACKWARD_ORACLE_PROTOCOL.md` |
| `ShantiDraconis/m-core-riemann` | `193117c973d462f8f18a6edf28ce2f208fc5626e` | hipótese aberta de RH (`ConcreteUniformLogDNBound`) |
| `ShantiDraconis/m-core-beal` | `36dce6e03c080b667773d5b51b9ac01a8a1dee90` | hipótese aberta de Beal (`GCDLowerBoundProducer`) |
| `ShantiDraconis/navier-stokes-critical-barrier-audit` | `3904224e49f7b2256d56ce19a5e11e7ddc93f524` | lane NS (`ActualNSToSignedGainCore`) |
| `ShantiDraconis/m-core-hodge` | `31d96f3dae43aac29393f8502927f5376fffbfa2` | lane Hodge (`ConcreteAlgebraicityPayload`) |
| `ShantiDraconis/m-core-p-vs-np` | `328cb6726222af4ad93e7727737d477640f74f89` | lane P vs NP (`P01MachineConstruction`, `G21Pointwise`) |
| `ShantiDraconis/m-core-bsd` | `a9e1292d13a0fba7da0bde8e082f34c2d5acd0d0` | lane BSD |
| `ShantiDraconis/m-core-yang-mills` | `1c324b533e85bf79cf5b55298fa9f42af4e8f30f` | lane Yang–Mills (`B60ConcretePhysicalAdapter`) |

## Alterações em arquivos copiados

- `atk-kernel/ATK.lean`: passa a importar `ATK.Conditional` e `ATK.Regimes`.
- `atk-kernel/scripts/expected_theorems.txt`: +14 condicionais e +14 de regimes (47 no total).
- `atk-kernel/scripts/check_axioms.py`: lê subpastas de `ATK/` e acrescenta a tabela dos condicionais.
- `.github/workflows/atk-kernel.yml`: audita também `ATK/Conditional/*.lean`.

## Arquivos novos

- `atk-kernel/ATK/Conditional.lean` e `atk-kernel/ATK/Conditional/*.lean` (7 arquivos).
- `atk-kernel/ATK/Regimes.lean` (10 formas do gateway v5.1, a partir do texto enviado em 2026-10-13).
- `atk-kernel/scripts/conditionals.json`.
- `atk-kernel/lake-manifest.json` (fixa Mathlib v4.34.1, commit `d13f23b`).
- `README.md`, `CATALOG.md`, `catalog/`, `scripts/build_catalog.py`, este arquivo.
