# ELYON_FINAL_EXTERNAL v2.0.0 — PREPARATORY (SUPERSEDES v1)
## PREPARATORY_NOT_ISSUED

Status público: registro preparatório, **não é certificado emitido**.
`FINAL_EXTERNAL_ISSUED = false`, `FINAL_ROOT = null`, `final_proof = 0/7`.

O v1 (`../v1`) é preservado byte a byte; este pacote o substitui com razões
explícitas (`manifest.json → supersedes.reasons`).

### Correções em relação ao v1
- `linked_preparatory_root` desatualizado removido; o `PREPARATORY_ROOT` reproduzido do v1 fica registrado em `supersedes`.
- G3 separado em `G3_CONTRACT` (CLOSED_GREEN_FROZEN_CERTIFIED) e `G3_SOURCE_FIDELITY` (OPEN), conciliando manifest/status com o gate_ledger.
- `axiom_footprint.json` preenchido pela auditoria do kernel.
- Produtor P01 recuperado: `prepPhase` concreto (m-core-p-vs-np@ffd06cc6). P01 passa a faltar um único `P01VerifierPhase prepPhase.layout`.
- Pins do registro corrigidos (P vs NP → `b406b806`; BSD → `a3edf620`).
- `hardware_attestation = OUT_OF_SCOPE_FOR_V1` (valor permitido; nenhuma alegação de hardware).
- `freeze.sh` v2 calcula os bloqueios a partir dos dados e exige que a condição de emissão seja idêntica à do v1.

### Bloqueios atuais (derivados por `freeze.sh`)
1. `P01ConstructionGap` — falta `Nonempty (P01VerifierPhase prepPhase.layout)`.
2. `G21Pointwise` — equivalente a SAT ∉ P (P ≠ NP).
3. `human_review` — UNSET; só uma autoridade humana pode definir.
4. `app` — UNSET.
5. `crypto` — UNSET; assinatura Sigstore preparada em `.github/workflows/final-external-v2-sign.yml`, não executada (grava a identidade do workflow, incluindo o nome do repositório, no log público Rekor).

Mesmo com todos fechados, o v2 continua preparatório: a emissão exige um v3
assinado e aprovação humana registrada.
