# ATK terminal endpoint mapping — material-only

Source: `final-proof/global_sources.json` (M-Core). This is a dependency ledger, not proof credit.

| Lane | Required material proposition / producer | Canonical source repository |
|---|---|---|
| BEAL | `∀ d : BealData, CommonPrime d.a d.b d.c` | `m-core-beal` |
| HODGE | `RationalHodgeConjecture D` | `m-core-hodge` |
| YANG_MILLS | genuine 4D realization, OS/Hamiltonian reconstruction, positive spectral gap | `m-core-yang-mills` |
| RIEMANN | unconditional DN vanishing, DNLimit=0, R1ExternalBridge | `m-core-riemann` |
| P_VS_NP | `P01ConstructionGap` and `G21Pointwise` | `m-core-p-vs-np` |
| BSD | universal rank equality plus refined leading coefficient | `m-core-bsd` |
| NAVIER_STOKES | independent quantitative compensator, signed cancellation and positive scale gain | `navier-stokes-critical-barrier-audit` |

## Linking requirement

The seven generic propositions in `lean/ATK/TerminalSevenInterfaces.lean` are not canonical endpoints until each is instantiated by the exact Lean proposition from its source repository. A string label, alias, equivalence, conditional lemma, or `Nonempty` field without an inhabitant is insufficient.

For each lane, record source commit, fully qualified theorem, `#print axioms` output, `lake env lean` result, semantic-fidelity check, and the consumer theorem that uses the producer. Preserve all frozen/certified branches; perform integration on this isolated branch.

Status: SOURCE / BUILD_PENDING. No seven-conjecture closure claimed.
