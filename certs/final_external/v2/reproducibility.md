# Reproducibility — v2.0.0 — PREPARATORY_NOT_ISSUED

```bash
bash certs/final_external/v2/freeze.sh     # reproduz SHA256SUMS e PREPARATORY_ROOT do v2
bash certs/final_external/v1/freeze.sh     # (numa cópia) reproduz o v1 inalterado
bash certs/final_global/v1/verify.sh       # pacote FINAL_GLOBAL
```

Canonicalização: `SHA256SUMS` cobre os 10 arquivos de payload (inclui `freeze.sh`,
exclui `SHA256SUMS` e `PREPARATORY_ROOT`); `PREPARATORY_ROOT = SHA256(bytes de SHA256SUMS)`.

Toolchain e execuções do kernel: `provenance.json`. Pegada de axiomas: `axiom_footprint.json`.
