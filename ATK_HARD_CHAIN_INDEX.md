# ATK HARD Chain Index

Status: CANONICAL LINK MAP
Date: 2026-09-21
Source of truth for HARD accounting: `MCCS_STATUS.json`.

## Global accounting

- HARD composite remaining: **10**
- HARD atomic remaining: **11**
- Total tracked HARD obligations: **21**
- Material producer slots: **8**
- Terminal certificates: **7/7 GREEN_FROZEN**
- Canonical HARD bases: **7/7 GREEN_FROZEN incorporated**
- FINAL_PROOF: **0/7**
- Progress metric: `FROZEN_HARD/TOTAL_HARD`
- Frozen prefixes do **not** decrement the historical HARD counters until the corresponding HARD producer itself closes.

## Canonical HARD bases incorporated

| Chain | Canonical GREEN_FROZEN base | SHA | Uncovered HARD delta |
|---|---|---|---|
| RH | `frozen/vanishing-upper-bound-green-5c66f8dc` | `5c66f8dca03834f24a61a9b1219e7af9d4892dd6` | unconditional BCF/zero-residue control yielding `VanishingUpperBound` |
| BEAL | `frozen/b01-conductor-level-interface-green-b6667e63` | `b6667e63a2c28c32cee0ab17714f9d772a0b4768` | exact local conductor exponent + exact lowered level → universal `CommonPrime` |
| NS | `frozen/prefix-n01-uniformity-b7caecc2` | `b7caecc2db571679af4b6ee64829253dcd97cea2` | uniform parameter-independent signed depletion from `ActualNS` |
| PNP | `frozen/material-orientation-green-969408f2` | `969408f2d84121667319da04680893dd2978e9a6` | construct genuine `MaterialOrientation` |
| BSD | `frozen/d01-universal-firewall-v2-green-c1e7b245` | `c1e7b245726c4c65f5f9f878acefb86460746f4a` | realizable elliptic-curve domain + rank equality + refined formula |
| HODGE | `frozen/h01-minimal-forward-payload-green-42eaf7d4` | `42eaf7d4d639871f82eceb121ee525a6c4f30d84` | construct `H01MinimalForwardPayload` universally |
| YM | `frozen/prefix-y01-b3b5-hardening-cd4bbfd` | `cd4bbfd348b607bd24ed0c6d605207b764286f58` | B6 genuine 4D realization + IR/limit + spectral transfer |

These seven SHAs are now the canonical reusable HARD bases. Older weaker heads remain provenance only and must not be used as the default continuation point.

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

## Compressed producer queue

1. **RH-P1** — construct unconditional BCF/zero-residue control. Reuse the frozen theorem `VanishingUpperBound → DNToZero → DNLimit=0`.
2. **BEAL-P1** — derive exact conductor exponent/lowered level and close the remaining universal `CommonPrime` families.
3. **HODGE-P1** — construct the certified minimal forward payload for every rational Hodge class.
4. **YM-P1** — construct B6: genuine 4D physical realization, continuum/IR control, and spectral transfer yielding a positive gap.
5. **PNP-P1** — construct a material orientation: either a genuine polynomial SAT route or a genuine lower-bound witness.
6. **BSD-P1** — prove universal rank equality on realizable elliptic-curve data.
7. **BSD-P2** — prove the refined leading-coefficient/regulator/height/Ш identity on the same realizable domain.
8. **NS-P1** — derive a single positive parameter-independent signed-depletion constant from `ActualNS`.

## Scheduling

- Never restart from a weaker historical head when a compatible canonical GREEN_FROZEN base exists.
- Never rerun a frozen compatible prefix.
- Run independent producers in parallel.
- On GREEN producer: compatibility audit → certificate → SHA256 → freeze → discharge linked consumers → decrement HARD ledger.
- On RED_INFRA: repair and rerun the same producer.
- On RED_MATH: isolate the smallest noncircular missing lemma and preserve every prior GREEN artifact.
- Numerical evidence can guide an attack but cannot close a universal producer.

## Fail-closed rule

This index incorporates certified prefixes; it does not promote unresolved mathematics. A HARD closes only after the exact producer is kernel-checked with zero `sorry`, zero `admit`, no hidden oracle/axiom, no circularity, no trivial witness, and no semantic weakening.
