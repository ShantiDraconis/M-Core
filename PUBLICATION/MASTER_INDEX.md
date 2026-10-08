# MASTER_INDEX — programa ATK (M-Core)

Auditoria de 2026-10-08 · branch `atk/global-audit-20261008` ·
pacote verificável em [`certs/final_global/v1/`](../certs/final_global/v1/)
(`bash certs/final_global/v1/verify.sh`).

> **Estado em uma linha:** a infraestrutura formal está íntegra e certificada
> pelo kernel (CLOSED_MATH estrutural); **nenhuma** das sete conjecturas tem prova
> terminal (`final_proof = 0/7`); FINAL_EXTERNAL **não** foi emitido.

## 1. Certificados

| Arquivo | Estado | SHA-256 / raiz |
|---|---|---|
| [`CLOSED_MATH_GLOBAL_CERTIFICATE.json`](../certs/final_global/v1/CLOSED_MATH_GLOBAL_CERTIFICATE.json) | `GREEN_FROZEN_CERTIFIED` — 41/41 módulos, 582 teoremas, 0 axiomas proibidos; 0 endpoints terminais | `f172934d…` · congelado em `frozen/closed-math-global-green-9a7f1f04` |
| [`OPEN_MATH_GLOBAL_STATUS.json`](../certs/final_global/v1/OPEN_MATH_GLOBAL_STATUS.json) | `OPEN_MATH` — 8 obrigações terminais, 0 demonstradas | `13abfd6b…` |
| [`FINAL_GLOBAL_CERTIFICATE.json`](../certs/final_global/v1/FINAL_GLOBAL_CERTIFICATE.json) | `INTEGRATION_STATE_CERTIFICATE` — estrutural GREEN, terminal OPEN | `2be78e68…` · `FINAL_GLOBAL_ROOT` no próprio pacote |
| `FINAL_EXTERNAL_CERTIFICATE.json` | **não emitido** | — |
| [`FINAL_EXTERNAL_BLOCKERS.md`](../certs/final_global/v1/FINAL_EXTERNAL_BLOCKERS.md) | pré-emissão, não terminal: 2 bloqueios matemáticos + 4 de governança | `1985ca44…` |
| [`GLOBAL_AXIOM_AUDIT.md`](../certs/final_global/v1/GLOBAL_AXIOM_AUDIT.md) | M-Core PASS; NS com axiomas; prova circular de RH sinalizada | `be683e14…` |
| [`GLOBAL_KERNEL_RUNS.md`](../certs/final_global/v1/GLOBAL_KERNEL_RUNS.md) | runs `37819802090`, `37824483365`, `37825452119` | `b7018a67…` |
| [`SOURCE_INVENTORY.json`](../certs/final_global/v1/SOURCE_INVENTORY.json) | 24 repositórios, 2.138 branches (511 `frozen/`, 306 `cert/`) | `77176845…` |

## 2. Estado por conjectura

Formato pedido: `ATK-[LANE]: ESTADO | SHA | RUN | CLOSED_MATH | OPEN_MATH | CERTIFICATE | DOI_READY`.
"SHA" é o `main` do repositório de origem; "RUN" é a execução do kernel do M-Core
que verificou a integração.

```
ATK-PVSNP:  OPEN_MATH | 382de6a7 (registro a3386d52) | 37825452119 | redução TwoGap, wiring G2.2, contrato G3 e sub-gates P01 (por referência) | 2: P01ConstructionGap, G21Pointwise≡P≠NP | FINAL_GLOBAL (estado); FINAL_EXTERNAL não emitido | NÃO
ATK-RH:     OPEN_MATH | a30d95f7 (registro d6a291b4) | 37825452119 | equivalência ¬RH ⇔ zero fora da reta; Re<1 | 1: FiniteSpanApproximatesChi (Nyman–Beurling) + conflito de orientação | FINAL_GLOBAL (estado) | NÃO
ATK-BEAL:   OPEN_MATH | d79343f2 (registro d6fe130c) | 37825452119 | interface concreta em ℕ | 1: GCDLowerBoundProducer (a própria conjectura) | FINAL_GLOBAL (estado) | NÃO
ATK-NS:     OPEN_MATH | 3904224e (registro df808543) | 37825452119 | interface paramétrica | 1: ActualNSToSignedGainCore; origem usa axiomas | FINAL_GLOBAL (estado) | NÃO
ATK-HODGE:  OPEN_MATH | d06d5fca (registro 42eaf7d4) | 37825452119 | interface paramétrica | 1: ConcreteAlgebraicityPayload | FINAL_GLOBAL (estado) | NÃO
ATK-BSD:    OPEN_MATH | 12be69bc (registro c1e7b245) | 37825452119 | interface; domínio Weierstrass do Mathlib | 1: igualdade de posto + fórmula refinada | FINAL_GLOBAL (estado) | NÃO
ATK-YM:     OPEN_MATH | b4a5cff1 (registro cd4bbfd3) | 37825452119 | interface paramétrica | 1: B60ConcretePhysicalAdapter | FINAL_GLOBAL (estado) | NÃO
```

## 3. Inventário e recuperação

- **Encontrado:** 24 repositórios, 2.138 branches; varredura de todos os tips
  (shallow) atrás de habitantes incondicionais dos alvos terminais e de
  `sorry`/`admit`/`axiom` com remoção correta de comentários.
- **Provas recuperadas e integradas:** nenhuma prova terminal existia para integrar.
  Foram integrados os reparos que fazem a biblioteca existente voltar a passar no
  kernel (seção 5).
- **Produtor material recuperado, não integrado:** `prepPhase : P01PrepPhase`
  concreto e sem `sorry` (`m-core-p-vs-np@ffd06cc6`). Reduz `P01ConstructionGap` a
  um único `P01VerifierPhase prepPhase.layout`. Não foi promovido porque continua
  condicional à fase verificadora.
- **Habitantes materiais confirmados de alvos terminais:** 0.
- **Rejeitados:** `falsified_*` (axiomas de controle negativo, rotulados),
  `MCORE_LHOSPITAL_AXIOM` (suposição temporária), tentativas com `sorry`, e
  `millennium-riemann-i/…/Contradiction.lean` (prova circular de RH — ver
  `GLOBAL_AXIOM_AUDIT.md §4`).

## 4. Lacunas matemáticas restantes (menores lacunas identificadas)

| Lane | Lacuna | Natureza |
|---|---|---|
| P vs NP / P01 | `P01VerifierPhase prepPhase.layout` concreto | engenharia de formalização de um resultado conhecido (SAT ∈ NP) |
| P vs NP / G21 | `G21Pointwise` ≡ SAT ∉ P | o problema P vs NP |
| Riemann | `FiniteSpanApproximatesChi` (critério de Báez-Duarte) — e escolher **uma** orientação | equivalente à RH |
| Beal | `∀ d, 1 < gcd(a, gcd(b, c))` | a conjectura de Beal |
| Navier–Stokes | `ActualNSToSignedGainCore` — e remover axiomas `…_TARGET` do caminho certificado | equivalente ao problema |
| Hodge | `ConcreteAlgebraicityPayload` | equivalente ao problema |
| BSD | posto + fórmula refinada no domínio realizável | equivalente ao problema |
| Yang–Mills | `B60ConcretePhysicalAdapter` | equivalente ao problema |

Cinco alvos semânticos (P vs NP, NS, Hodge, BSD, YM) são paramétricos em
predicados abstratos; um habitante só conta depois que esses predicados forem
ligados ao enunciado oficial.

## 5. Correções feitas nesta auditoria

O `main` não compilava desde `32981d6`. Reparados, sem enfraquecer enunciados:
`RPAConfirmation`, `RPALattice`, `ProblemSignature`, `C3MaterialOperators`,
`TypedCompressionCore` e o arquivo de proveniência `MCore/A4Scale.lean`. Adicionados
o auditor genérico de axiomas (`audit/kernel/AxiomAudit.lean`) e o workflow
`atk-global-kernel-audit.yml`; corrigido o `Final Proof Miner` (cache do Mathlib).

**Ressalva sobre um certificado já publicado:**
`PUBLICATION/DUAL_ENDPOINT_STATE_STRUCTURAL_CERTIFICATE.md` (commit `465cc65`)
descreve como "estruturalmente certificada" a estrutura RPA, mas
`RPAConfirmation.lean`/`RPALattice.lean` não compilavam naquele commit. A base Lean
dessa estrutura só passa no kernel a partir de `8b7099e` nesta branch. O arquivo
foi preservado como está.

## 6. Publicação e DOI

Ver [`DOI_READY_INDEX.md`](DOI_READY_INDEX.md). Resumo: nenhuma das sete lanes
está apta a ser publicada como resolução. O que é publicável com honestidade é o
**sistema de certificação fail-closed** e este pacote de auditoria, como registro de
software/dados, declarando `final_proof = 0/7`.

Itens da ordem MASTER cobertos por este índice em vez de arquivos separados:
`PROOF_INVENTORY` e `CERTIFICATE_REGISTRY` (§1–3 e `SOURCE_INVENTORY.json`),
`BRANCH_PROVENANCE` (`SOURCE_INVENTORY.json`), `OPEN_MATH_BLOCKERS` (§4 e
`OPEN_MATH_GLOBAL_STATUS.json`), `CLOSED_MATH_CERTIFIED` / `FINAL_GLOBAL_STATUS` /
`FINAL_EXTERNAL_STATUS` (§1), `ORIGINAL_RESULTS` e `EXTERNAL_REVIEW_PACKAGE`
(`DOI_READY_INDEX.md`). Nenhum artigo foi redigido como resolução de conjectura.
