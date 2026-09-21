# ATK HARD Chain Index

Status: CANONICAL LINK MAP
Date: 2026-09-21
Source of truth for historical HARD accounting: `MCCS_STATUS.json`.

## Global accounting

- HARD composite remaining: **10**
- HARD atomic remaining: **11**
- Total tracked HARD obligations: **21**
- Progress metric: `FROZEN_HARD/TOTAL_HARD`
- Frozen prefixes do not decrement these historical remaining counters until the corresponding HARD itself is closed.

## Exact 21-HARD queue

| Repo | Composite | Atomic | Active chain |
|---|---:|---:|---|
| m-core-beal | 2 | 2 | B01_CONDUCTOR_EXACT_LEVEL → B02_RESIDUAL_ELIMINATION |
| navier-stokes-critical-barrier-audit | 2 | 2 | N01_SIGNED_DEPLETION → N02_ENDPOINT_REGULARITY |
| m-core-riemann | 1 | 1 | R01_ZERO_RESIDUE_DNLIMIT |
| m-core-hodge | 1 | 1 | H01_GENERAL_ALGEBRAICITY |
| m-core-yang-mills | 1 | 1 | Y01_4D_IR_CLUSTERING_GAP |
| m-core-p-vs-np | 2 | 2 | P01_SAT_OPERATIONAL_NTM → P02_SAT_NOT_IN_P |
| m-core-bsd | 1 | 2 | D01_RANK + D01_REFINED_LEADING_SHA → D01_COMPOSITE |

Totals: 10 composite + 11 atomic = 21.

## Reuse links / current continuation points

### Riemann R01
Do not restart R01. Continue the existing chain:
- `research/r2-dnlimit-zero`
- `research/r2-zero-residue-probe`
- `research/nb-zero-limit-frontier`
- `attack/r01-quantitative-zero-criterion-20260921`
- `attack/r01-zero-residue-parallel-20260921`
- `attack/r01-finite-limit-firewall-20260921`
- `attack/next-r2-from-43d7c060`
- highest located frozen reduction: `frozen/nb-zero-limit-density-reduction-green-4cf864e3`

Verified existing zero-limit logic in `lean/MCore/RH/NB/ZeroLimitFrontier.lean`:
`FiniteSpanApproximatesChi → DNLimit = 0 → DNToZero`.
Verified analytic development in `research/r2/DNLimitZeroAttack.md`: exact b_a, Gram/Vasyunin machinery, finite optimal projection and rigorous finite DN ladder through N=256. The remaining producer is an unconditional quantitative approximation/density estimate for the concrete generator family. Downstream zero-limit logic is REUSE.

### Other queues
Each problem repository has `audit/ATK_TERMINAL_PRODUCER_INDEX.md`, which is the canonical per-repository producer/reuse map. Frozen/certified artifacts listed there are reused before recomputation.

## Fail-closed rule

This file links work; it does not promote mathematics. A HARD closes only after the exact producer is proved with zero `sorry`, zero `admit`, no hidden oracle/axiom, no circularity, no trivial witness, and no semantic weakening. Existing GREEN/FROZEN consumers and infrastructure are REUSE, not final-proof evidence.


## Maximum compression / shortest-path scheduler

The 21 historical counters are retained for provenance. Execution is compressed by terminal producer, not by wrapper count.

### Deduplication rule
If multiple HARD labels are downstream consumers of the same unresolved producer, attack the producer once and discharge all compatible consumers by exact local reproving/import after it closes.

### Compressed producer queue

1. **RH-P1 — concrete NB quantitative approximation**
   Producer: unconditional theorem yielding `FiniteSpanApproximatesChi concreteGeneratorFamily`.
   Reuse immediately: `FiniteSpanApproximatesChi → DNLimit=0 → DNToZero` and the existing R1 endpoint chain.
   Do not rerun finite DN ladders or zero-limit logic.

2. **BEAL-P1 — universal CommonPrime producer**
   Producer: `∀ d : BealData, CommonPrime d.a d.b d.c`.
   B01/B02 wrappers and certified local/exponent families are consumers/reductions. Reuse T/K frozen material; attack only uncovered residual families.

3. **HODGE-P1 — general algebraicity producer**
   Producer: `RationalHodgeConjecture D` / arbitrary-codimension algebraicity-surjectivity.
   R3/R3a and three-residue material remain reusable reductions; no transport assumption may substitute for the producer.

4. **YM-P1 — physical 4D reconstruction/gap producer**
   Producer: genuine 4D construction + continuum/IR control + uniform clustering sufficient for positive spectral gap.
   Reuse K/Spectral/A1/B60 firewalls; reject phantom/trivial physical interfaces.

5. **PNP-P1 — orientation producer**
   Equality lane: genuine `PolySATCertificate + SATCompletenessTransfer`.
   Separation lane: genuine `LowerBoundWitness.not_in_p`.
   P01/P02 are attacked through whichever producer is actually established; finite SAT evidence is not promotion evidence.

6. **BSD-P1/P2 — universal arithmetic-analytic producers**
   P1: universal `BSDRankPart`.
   P2: refined leading-coefficient / height-Sha arithmetic obligation needed by the full endpoint.
   Reuse K0–K14 TOTAL/FINAL_REPRO and curve-specific certificates only as compatible lemmas/evidence.

7. **NS-P1 — signed-depletion producer**
   Continue existing N01 chain, reusing XiEps/Campanato geometry:
   `ActualNS → hDynamic_eps → WeightedLow_eps → WeightedAbsorption_eps (γ<1, parameter-independent) → ε→0/tightness → SignedDepletion`.
   The independence certificate and Constantin–Fefferman/CZ signed far-field gain are the active analytic subproducers.
   N02 is a downstream consumer after N01 if its exact hypotheses match.

### Scheduling
- Never attack a downstream wrapper while its sole producer is open.
- Never rerun a frozen compatible prefix.
- Run independent producers in parallel.
- On GREEN producer: local compatibility proof → certify → freeze → discharge every linked consumer → decrement canonical HARD ledger.
- On RED_INFRA: repair/rerun same producer.
- On RED_MATH: reduce to the smallest noncircular missing lemma; preserve all previous GREEN artifacts.
- Numerical evidence may guide attacks but cannot close a universal producer.

### Current shortest-path interpretation
The historical queue remains **10 composite + 11 atomic = 21**, but execution is now organized around the **8 material producer slots** above (RH 1, Beal 1, Hodge 1, YM 1, PNP 1 orientation slot with two alternative lanes, BSD 2, NS 1). This is an execution compression only; it does not claim that any of the 21 HARD obligations has been mathematically closed.
