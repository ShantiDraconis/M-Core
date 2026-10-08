# FINAL_EXTERNAL — relatório de pré-emissão (NÃO TERMINAL)

> **Estado: `PREPARATORY_NOT_ISSUED`. Este documento não é um certificado
> FINAL_EXTERNAL e não afirma a resolução de nenhum problema.**
> `FINAL_EXTERNAL_CERTIFICATE.json` **não foi emitido**, porque os gates terminais
> não estão satisfeitos. Nenhum gate foi alterado.

## 1. Auditoria do gate `certs/final_external/v1/freeze.sh`

`freeze.sh` (ELYON_FINAL_EXTERNAL v1.0.0, revisão `v1.3.1-preparatory`) é, por
desenho, um congelamento **preparatório** fail-closed: o próprio cabeçalho diz que
ele "Never emits FINAL_ROOT or ISSUED". Os 8 passos:

| Passo | O que verifica | Resultado (run `37819802090` e cópia local) |
|---|---|---|
| 1 | sintaxe dos 7 JSON | OK |
| 2 | ausência de `sorry`/`admit`/`sorryAx` em `.lean` do pacote | OK (o pacote não contém `.lean`) |
| 3 | estado normativo: `PREPARATORY`, `FINAL_EXTERNAL_ISSUED=false`, `FINAL_ROOT=null`, `final_proof="0/7"`, âncoras ELYON | OK |
| 4 | classes de bloqueio exatas = `[P01ConstructionGap, G21Pointwise, human_review, app, crypto, hardware]`; `G3 = CLOSED_GREEN_FROZEN_CERTIFIED`; `TWO_GAP = 0/2`; `P_VS_NP_ENDPOINT = OPEN`; `GLOBAL_7 = 0/7` | OK |
| 5–7 | gera `SHA256SUMS` e `PREPARATORY_ROOT`, reverifica | **idênticos** aos commitados |
| 8 | `FINAL_ROOT` continua `null`, emissão continua `false` | OK |

`PREPARATORY_ROOT` reproduzido: `1651ac0cf58b81ce2038019c548fbd7132487aa0ad3a2e29b934adf6e3bf88d9`.

Observação importante sobre o passo 4: ele **exige** que os seis bloqueios estejam
abertos (`assert blockers == [...]`). Quando um gate fechar de verdade, o pacote v1
deixa de passar e será preciso uma nova revisão (v2) com `SUPERSEDES`, conforme a
política de versionamento do próprio manifesto. Isso é correto: o v1 é um registro
preparatório imutável, não um emissor.

## 2. Condição de emissão (de `manifest.json → issuance_gate.condition`)

```
P01ConstructionGap closed AND G21Pointwise closed AND G3 CLOSED
AND human_review != UNSET AND production.app != UNSET
AND production.crypto != UNSET AND hardware_attestation != UNSET
AND all required infra GREEN+FROZEN
```

## 3. Bloqueios restantes — lista exata

### 3.1 Matemáticos (terminais)

| # | Obrigação | Estado | Equivalente a | Menor lacuna identificada |
|---|---|---|---|---|
| M1 | `P01ConstructionGap` = `Nonempty P01MachineConstruction` | OPEN_IMPLEMENTATION | SAT ∈ NP via MTN concreta de controle finito, com parada, cota polinomial e correção | Um único objeto: `P01VerifierPhase prepPhase.layout` concreto. O `prepPhase` já existe sem `sorry` em `m-core-p-vs-np@ffd06cc6` (`atk/direct-p01-terminal-close-v2-20260930`), e `p01_of_verifier` fecha P01 a partir dele. Nenhuma das 686 branches contém um `P01VerifierPhase` concreto. |
| M2 | `G21Pointwise` | OPEN_MATH | `P02Target` ≃ `Nonempty (FailureGenerator (SATBits circuitBitEncoding))` ≃ `¬ InP SAT` — isto é, **P ≠ NP** | É o próprio problema P vs NP. Única tentativa direta (`G21PointwiseAttempt.lean`) termina em `sorry`. |

M1 é matemática conhecida (Cook, 1971) e está aberta só como engenharia de
formalização. M2 é um problema do Milênio em aberto.

Mesmo com M1 e M2 fechados, o efeito é `P_VS_NP_ENDPOINT = CLOSED` e
`GLOBAL_7 = 1/7` (regra `transition_rules.p01_and_g21` do
`MATH_TERMINAL_BOUNDARY_20260922.json`). As outras seis lanes
(`OPEN_MATH_GLOBAL_STATUS.json`) continuam abertas e não fazem parte da condição
de emissão do v1, que cobre apenas a cadeia P vs NP.

### 3.2 Não matemáticos (governança/produção)

| # | Gate | Valor atual | Quem pode fechar |
|---|---|---|---|
| H1 | `human_review.authority` / `quorum` / `evidence_policy` | `UNSET` | Autoridade humana; o manifesto proíbe que um validador técnico escolha |
| H2 | `production.app.app_repository` | `UNSET` (`NOT_CONNECTED`) | Mantenedor |
| H3 | `production.crypto.crypto_provider` | `UNSET` | Mantenedor (GPG/Sigstore) |
| H4 | `production.hardware_attestation.status` | `UNSET` | Mantenedor (`OUT_OF_SCOPE_FOR_V1`, `TPM2_ATTESTED` ou `SECURE_BOOT_ATTESTED`) |

H1–H4 são decisões humanas; esta auditoria não as preenche.

## 4. Inconsistências encontradas no pacote congelado (não corrigidas — pacote FROZEN)

1. `manifest.json → root.linked_preparatory_root = 4cdaf7b6…`, mas o
   `PREPARATORY_ROOT` atual reproduzido por `freeze.sh` é `1651ac0c…`. A referência
   ficou desatualizada após a revisão v1.3.1.
2. `gate_ledger.json → G3.status = "OPEN_SOURCE_FIDELITY"` / `endpoint = "OPEN"`,
   enquanto `manifest.json` e `status.json` dizem `G3 = CLOSED_GREEN_FROZEN_CERTIFIED`.
   O próprio manifesto ressalva que a fidelidade a cada convenção do texto
   Cook/CMI "is a separate audit statement and is not endpoint proof credit".
   Leitura correta: o **contrato normalizado** G3 está certificado; a
   **fidelidade de fonte** externa não.
3. `axiom_footprint.json → current_footprint = "UNSET"`. Preenchido fora do
   pacote em [`GLOBAL_AXIOM_AUDIT.md`](GLOBAL_AXIOM_AUDIT.md).

Correções desses três pontos pertencem a uma revisão v2 do pacote, com `SUPERSEDES`.

## 5. Conclusão

`FINAL_EXTERNAL_ISSUED = false`. `FINAL_ROOT = null`.
Bloqueios: **2 matemáticos (M1, M2) + 4 de governança (H1–H4)**.
