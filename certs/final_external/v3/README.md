# ELYON_FINAL_EXTERNAL v3.0.0 — PREPARATORY (SUPERSEDES v2)
## PREPARATORY_NOT_ISSUED

Status público: registro preparatório, **não é certificado emitido**.
`FINAL_EXTERNAL_ISSUED = false`, `FINAL_ROOT = null`, `final_proof = 0/7`.

v1 (`../v1`) e v2 (`../v2`) são preservados byte a byte; `freeze.sh` v3 verifica
os hashes de ambos.

### O que muda em relação ao v2
- **P01 fechado.** `P01RawTotalizationProducer.p01ConstructionGap_closed :
  P01ConstructionGap`, em `m-core-p-vs-np@0dd09383`
  (`frozen/p01-t5-poly-halting-green-0dd09383`), é um habitante incondicional:
  uma MTN concreta, de controle finito e tempo polinomial, que decide a linguagem
  CNF-SAT canônica (lado SAT ∈ NP).
  - Auditoria independente: `frozen/p01-closure-audit-green-d97a56e1`, run
    `37913791428`.
  - O tipo é exatamente `P01ConstructionGap`; os axiomas são
    `propext`, `Classical.choice`, `Quot.sound`.
  - Os 42 arquivos que definem o enunciado são idênticos ao `main`.
- O v2 listava P01 como aberto porque o scanner de 2026-10-08 não reconhecia
  tipos qualificados por namespace nem tipos na linha seguinte da declaração.
  Esse erro está corrigido.
- TwoGap: **1/2**. Pela regra `p01_only`, `P_VS_NP_ENDPOINT` continua OPEN e o
  placar global continua 0/7.

### Bloqueios atuais (derivados por `freeze.sh` v3)
1. `G21Pointwise` — equivalente a SAT ∉ P (P ≠ NP). Problema em aberto.
2. `human_review` — UNSET; só uma autoridade humana pode definir.
3. `app` — UNSET.
4. `crypto` — UNSET. A assinatura Sigstore está preparada em
   `.github/workflows/final-external-sign.yml`, mas não foi executada. Executá-la
   grava a identidade do workflow, incluindo o nome do repositório, no log
   público Rekor.

Continua fechado: `hardware_attestation = OUT_OF_SCOPE_FOR_V1`.

Mesmo com todos fechados, o v3 continua preparatório: a emissão exige um v4
assinado e aprovação humana registrada.
