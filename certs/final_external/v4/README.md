# ELYON_FINAL_EXTERNAL v4.0.0 — PREPARATORY (SUPERSEDES v3)
## PREPARATORY_NOT_ISSUED

Status público: registro preparatório, **não é certificado emitido**.
`FINAL_EXTERNAL_ISSUED = false`, `FINAL_ROOT = null`, `final_proof = 0/7`.

v1, v2 e v3 são preservados byte a byte; `freeze.sh` v4 verifica os hashes dos três.

### O que muda em relação ao v3: o gate `crypto` foi fechado
O payload do v3 (`../v3/SHA256SUMS`, sha256 `61219f71…54795d` = `PREPARATORY_ROOT`
do v3) foi assinado com **Sigstore keyless**:
- run `37922203677`, disparado pela branch `sign/final-external-v3`;
- certificado Fulcio com a identidade
  `https://github.com/ShantiDraconis/M-Core/.github/workflows/final-external-sign.yml@refs/heads/sign/final-external-v3`;
- entrada Rekor `hashedrekord`, **logIndex 3163404491**, 2026-10-09T11:11:38Z.

O bundle está em `signature_v3/`.

Verificação:
- **Online**, dentro do run: `cosign verify-blob` (identidade, emissor OIDC, cadeia Fulcio, inclusão no Rekor).
- **Offline**, em `freeze.sh` v4, passo 3b:
  - assinatura ECDSA válida sob a chave do certificado (openssl);
  - SAN igual à identidade esperada;
  - hash da entrada Rekor igual ao sha256 do payload.
  - A cadeia Fulcio e o SET do Rekor não são reverificados offline.
- Controles negativos: alterar um byte da assinatura, ou trocar o hash da entrada Rekor, faz o gate falhar.

**Tornou-se público e permanente no Rekor:**
- o nome do repositório `ShantiDraconis/M-Core` e o dono;
- o commit `798be087`, a branch e a URL do run;
- a visibilidade "private".

O conteúdo do pacote não foi publicado, apenas o hash.

### Bloqueios atuais (derivados por `freeze.sh` v4)
1. `G21Pointwise` — equivalente a SAT ∉ P (P ≠ NP). Problema em aberto.
2. `human_review` — UNSET; só uma autoridade humana pode definir.
3. `app` — UNSET.

A assinatura não muda nada matemático. Ela só atesta que o pacote v3 é este,
byte a byte.
