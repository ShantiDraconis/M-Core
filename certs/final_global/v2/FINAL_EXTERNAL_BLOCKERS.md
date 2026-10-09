# FINAL_EXTERNAL — relatório de pré-emissão v3 (NÃO TERMINAL)

> **`FINAL_EXTERNAL_ISSUED = false`, `FINAL_ROOT = null`. Isto não é um
> certificado FINAL_EXTERNAL e não afirma a resolução de nenhum problema.**

Pacote: [`certs/final_external/v3`](../../final_external/v3/) (preparatório,
`SUPERSEDES v2`). Gate: `freeze.sh` v3, reproduzido no run `37914524820`.

- `PREPARATORY_ROOT` v3 = `61219f71a7ff9408810d6c96df5114e55b758ab67650f6e9a0d11ec14854795d`.
- A condição de emissão é idêntica à do v1 (o próprio `freeze.sh` verifica isso).
  Nenhum gate foi afrouxado.

## Bloqueios restantes (derivados dos dados por `freeze.sh` v3)

| # | Gate | Estado | Natureza | Quem fecha |
|---|---|---|---|---|
| 1 | `G21Pointwise` | OPEN_MATH | ≡ `P02Target` ≡ `¬ InP SAT` — **é o problema P ≠ NP** | ninguém sabe hoje |
| 2 | `human_review` | UNSET | autoridade, quórum e política de evidência | autoridade humana; o manifesto proíbe que um validador técnico escolha |
| 3 | `app` | UNSET | repositório e commit do app | mantenedor |
| 4 | `crypto` | UNSET | assinatura do pacote | mantenedor: rodar `final-external-sign.yml` com `version=v3` e digitar `PUBLISH` (o log Rekor é público) |

## Fechados

| Gate | Evidência |
|---|---|
| `P01ConstructionGap` | `P01RawTotalizationProducer.p01ConstructionGap_closed` @`0dd09383`; auditoria `frozen/p01-closure-audit-green-d97a56e1`, run `37913791428` |
| `G3` (contrato normalizado) | `cook_normalized_g3_contract_closed` @`f2cafea7`, run `35719428075`. A fidelidade ao texto Cook/CMI é um item separado e não conta como crédito de endpoint. |
| `hardware_attestation` | `OUT_OF_SCOPE_FOR_V1`, um valor permitido pelo manifesto que não faz nenhuma alegação de hardware. **Foi escolhido na sessão de 2026-10-08 e é reversível; confirme ou troque.** |

## Efeito de cada fechamento futuro

- **Fechar G21** daria TwoGap 2/2, `P_VS_NP_ENDPOINT` fechado e placar global 1/7.
  Só isso já seria uma prova de P ≠ NP.
- **Fechar `human_review`, `app` e `crypto`** não muda nada matemático. Habilita
  apenas a emissão de um v4 assinado, *se* G21 também estiver fechado.
