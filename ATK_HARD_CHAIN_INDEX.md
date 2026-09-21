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
