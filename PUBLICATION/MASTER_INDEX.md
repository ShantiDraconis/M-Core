# MASTER_INDEX — programa ATK (M-Core)

Atualizado em 2026-10-09 · branch `atk/global-audit-20261008` (PR #15) ·
pacote atual: [`certs/final_global/v2/`](../certs/final_global/v2/)
(`bash certs/final_global/v2/verify.sh`) · errata: [`ERRATA.md`](ERRATA.md)

> **Estado em uma linha:** a infraestrutura formal passa no kernel (CLOSED_MATH),
> o lado **SAT ∈ NP (P01) está fechado e verificado**, e **nenhuma** das sete
> conjecturas tem prova terminal: `final_proof = 0/7`. FINAL_EXTERNAL **não** foi
> emitido.

## 1. Certificados

| Arquivo | Estado |
|---|---|
| [`CLOSED_MATH_GLOBAL_CERTIFICATE.json`](../certs/final_global/v2/CLOSED_MATH_GLOBAL_CERTIFICATE.json) | `GREEN_FROZEN_CERTIFIED`. Parte A: biblioteca M-Core, 620 teoremas, 0 axiomas proibidos (run `37914524820`, `frozen/closed-math-global-green-33983a4c`). Parte B: P01 (SAT ∈ NP), run `37913791428`. |
| [`OPEN_MATH_GLOBAL_STATUS.json`](../certs/final_global/v2/OPEN_MATH_GLOBAL_STATUS.json) | 7 lanes, 10 obrigações; 1 demonstrada (P01), 0 lanes fechadas |
| [`FINAL_GLOBAL_CERTIFICATE.json`](../certs/final_global/v2/FINAL_GLOBAL_CERTIFICATE.json) | `INTEGRATION_STATE_CERTIFICATE`: estrutural GREEN, terminal OPEN, TwoGap 1/2, 0/7 |
| `FINAL_EXTERNAL_CERTIFICATE.json` | **não emitido** |
| [`certs/final_external/v3`](../certs/final_external/v3/) | preparatório (`SUPERSEDES v2`). Bloqueios: `G21Pointwise`, `human_review`, `app`, `crypto` |
| [`FINAL_EXTERNAL_BLOCKERS.md`](../certs/final_global/v2/FINAL_EXTERNAL_BLOCKERS.md) | lista exata dos bloqueios e de quem pode fechar cada um |
| [`GLOBAL_AXIOM_AUDIT.md`](../certs/final_global/v2/GLOBAL_AXIOM_AUDIT.md) · [`GLOBAL_KERNEL_RUNS.md`](../certs/final_global/v2/GLOBAL_KERNEL_RUNS.md) | auditorias |
| [`ERRATUM_v1.md`](../certs/final_global/v2/ERRATUM_v1.md) | o que o v1 errou e por quê |

## 2. Estado por conjectura

Formato: `ATK-[LANE]: ESTADO | SHA (origem) | RUN | CLOSED_MATH | OPEN_MATH | CERTIFICATE | DOI_READY`

```
ATK-PVSNP: OPEN_MATH | b406b806 (redução) · 0dd09383 (P01) | 37913791428 · 37914524820 | P01 = SAT∈NP fechado; redução TwoGap; G3 contrato | G21Pointwise ≡ P≠NP | FINAL_GLOBAL v2; FINAL_EXTERNAL v3 preparatório | P01 sim (como formalização de SAT∈NP); lane não
ATK-RH:    OPEN_MATH | d6a291b4 | 37914524820 | RiemannDual: ¬RH ⇔ zero em 1/2<Re s<1; simetria s↔1−s | provar ou refutar | FINAL_GLOBAL v2 | NÃO
ATK-BEAL:  OPEN_MATH | d6fe130c | 37914524820 | alvo concreto em ℕ | ∀d, 1<gcd(a,gcd(b,c)) | FINAL_GLOBAL v2 | NÃO
ATK-NS:    OPEN_MATH | df808543 | 37914524820 | enunciados (A)/(C) de Fefferman em ℝ³ | (A) ou (C) | FINAL_GLOBAL v2 | NÃO
ATK-HODGE: OPEN_MATH | 42eaf7d4 | 37914524820 | interface paramétrica (firewall) | ConcreteAlgebraicityPayload | FINAL_GLOBAL v2 | NÃO
ATK-BSD:   OPEN_MATH | a3edf620 | 37914524820 | interface paramétrica (firewall) | BSDTerminal | FINAL_GLOBAL v2 | NÃO
ATK-YM:    OPEN_MATH | cd4bbfd3 | 37914524820 | interface paramétrica (firewall) | B60ConcretePhysicalAdapter | FINAL_GLOBAL v2 | NÃO
```

## 3. Lacunas matemáticas restantes

| Lane | Lacuna | Natureza |
|---|---|---|
| P vs NP | `G21Pointwise` ≡ SAT ∉ P | o próprio problema P vs NP |
| Riemann | um zero em `1/2 < Re s < 1`, ou a prova de que não existe nenhum | equivalente à RH |
| Beal | `∀ d, 1 < gcd(a, gcd(b, c))` | a conjectura de Beal |
| Navier–Stokes | (A) ou (C) de Fefferman | o problema do Milênio |
| Hodge / BSD / Yang–Mills | antes de qualquer prova, falta o próprio enunciado oficial: os objetos não existem no Mathlib v4.19 | definição + problema |

## 4. PRs abertos (merge é decisão do mantenedor)

| Repositório | PR | Conteúdo |
|---|---|---|
| M-Core | #15 | conserta o build do `main` (quebrado desde `32981d6`); auditoria do kernel; FINAL_GLOBAL v1/v2; FINAL_EXTERNAL v2/v3 preparatórios |
| navier-stokes-critical-barrier-audit | #41 | remove 34 axiomas; refuta os 5 que eram falsos |
| millennium-riemann-I | #10 | rotula a "prova" de RH como circular |

Fechado por redundância: `m-core-p-vs-np#41` (decomposição de um verificador que já existia).

## 5. Ressalva sobre um certificado já publicado

`PUBLICATION/DUAL_ENDPOINT_STATE_STRUCTURAL_CERTIFICATE.md` (commit `465cc65`)
descreve como "estruturalmente certificada" a estrutura RPA, mas
`RPAConfirmation.lean` e `RPALattice.lean` não compilavam naquele commit. A base
Lean dessa estrutura só passa no kernel a partir de `8b7099e`. O arquivo foi
preservado sem alterações.
