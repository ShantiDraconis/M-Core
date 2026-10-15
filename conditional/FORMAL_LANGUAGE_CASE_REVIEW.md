# ATK — Casos de linguagem formal em branches históricas

Estado: REVIEW. Este arquivo documenta a terminologia correta sem editar ou validar os fontes nas branches de origem.

## 1. atk-kernel/ATK/LogicAudit.lean

- Branch: `atk-kernel-check`
- Arquivo: `atk-kernel/ATK/LogicAudit.lean`
- Formulação: A cota no modelo D_N ≡ 0 é um teste de vacuidade, não uma prova para o defeito genuíno.
- Certificação: classificar o teorema exato e verificar hipóteses e axiomas transitivos; não promover ao problema terminal.

## 2. lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean

- Branch: `atk/global-material-frontier-20261001`
- Arquivo: `lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean`
- Formulação: O teorema é implicação condicionada por RH, não prova de RH.
- Certificação: classificar o teorema exato e verificar hipóteses e axiomas transitivos; não promover ao problema terminal.

## 3. atk-kernel/ATK/ObrigacoesMinimas.lean

- Branch: `atk/hypothesis-ports-20261014`
- Arquivo: `atk-kernel/ATK/ObrigacoesMinimas.lean`
- Formulação: A implicação UniformLogBound → DN→0 está provada sob a hipótese de cota uniforme; essa cota permanece aberta.
- Certificação: classificar o teorema exato e verificar hipóteses e axiomas transitivos; não promover ao problema terminal.

