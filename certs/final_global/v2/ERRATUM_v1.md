# ERRATUM — FINAL_GLOBAL v1 (2026-10-08)

O pacote `../v1` é preservado byte a byte. Este v2 o substitui. Correções:

## 1. P01ConstructionGap estava fechado, e o v1 o declarou aberto

**O v1 disse:** "Nenhuma das 686 branches contém um `P01VerifierPhase` concreto",
`OPEN_MATH_GLOBAL_STATUS.json → pVsNP → P01ConstructionGap: OPEN_IMPLEMENTATION`.

**Correto:** `MCore.Real.P01RawTotalizationProducer.p01ConstructionGap_closed :
P01FinalCertificate.P01ConstructionGap` existe, sem hipóteses, em
`ShantiDraconis/m-core-p-vs-np@0dd09383932446ba67e673f69cd8740f85a80b87`
(`frozen/p01-t5-poly-halting-green-0dd09383`). É uma MTN concreta, de controle
finito e tempo polinomial, sobre o alfabeto `Option Bool`, que decide a linguagem
CNF-SAT canônica: o lado SAT ∈ NP.

**Causa do erro:** o scanner de 2026-10-08 só reconhecia o tipo quando ele
aparecia sem qualificação de namespace e na mesma linha do nome. Ele não pegava
`P01FinalCertificate.P01ConstructionGap` nem tipos escritos na linha seguinte.
O scanner novo (`scan_decl_headers.py`, que junta o cabeçalho até `:=`) encontra
o teorema. Outra sessão do Claude já o tinha registrado em
`atk/pnp-recovery-integration-20261008`.

**Verificação independente (2026-10-09):**
- Local, Lean 4.19.0 (`6caaee842e94`):
  - o fecho de 151 módulos compila;
  - o tipo é exatamente `P01ConstructionGap`;
  - axiomas `[propext, Classical.choice, Quot.sound]`;
  - nenhum `implemented_by`, `extern`, `unsafe`, `native_decide`, `opaque` ou `axiom` no fecho;
  - os 42 arquivos que definem o enunciado são idênticos aos do `main`.
- CI: run `37913791428` em `frozen/p01-closure-audit-green-d97a56e1`, com
  auditoria fail-closed de tipo e axiomas mais um controle negativo.

**Efeito:** TwoGap 0/2 → **1/2**. `P_VS_NP_ENDPOINT` continua OPEN e o placar
global continua **0/7** (regra `p01_only`). O PR `m-core-p-vs-np#41`, que decompunha
um verificador já desnecessário, foi fechado.

## 2. Pins do registro (já corrigidos em `ecb5f51`, registrados aqui)
- pVsNP: `a3386d52` não definia `G21Pointwise` nem `P01MachineConstruction`.
  Novo pin: `b406b806`.
- BSD: `c1e7b245` não tinha o terminal nomeado. Novo pin: `a3edf620`.

## 3. Contagem de obrigações
O v1 contava 8 obrigações (uma por terminal). O v2 conta **10**:
- Riemann e Navier–Stokes passam a ter duas orientações cada, provar e refutar.
  Basta uma delas para fechar a lane.
- P vs NP exige as duas obrigações dela.
