# ATK — Exact G21 versus historical fixed witness

Status: SOURCE_EXACT_TEXT_CHECKED; CROSS_MODEL_TYPE_MATCH_PENDING; KERNEL_NOT_RUN.

Source A: imports/pnp/c102d9d4/lean/MCore/Real/P02G21G22Attack.lean (blob ffd00b23cbbf4cb09f1f8c2ded111c32dbf62571)

`G21Pointwise := ∀ candidate : PolyDTMCandidate, ∃ x : BitString, ¬ candidate.CorrectAt SATTarget x`.
The existing `g21_pointwise_iff_p02_target` and `g21_iff_g22` are equivalences, not inhabitants of G21.

Source B: imports/pnp/recovery/7abed945/audit/EndpointCompression.lean (blob 41f18931c0d4f106067fc61200713903933164a7)

`FixedWitness C` contains a single language witness in NP and not in P, relative to an abstract `ClassicalComplexityInterface Language`. `fixed_witness_implies_final` additionally requires `OfficialModelMatch C officialP officialNP`.

## Critical mismatch
- G21 quantifies over **every polynomial-time deterministic candidate** for a specific SAT bit-language.
- FixedWitness supplies **one language** separated relative to a potentially different classical interface.
- A bridge requires identifying that interface with the exact SAT target and proving model equivalence; the historical conditional theorem alone does not provide such an inhabitant.
- Even if a fixed NP\\P witness were supplied, transferring it to SAT requires the correct reduction and closure theorems.

## Next material checks
- [ ] Compare source definitions of PolyDTMCandidate, CorrectAt, SATTarget, ClassicalComplexityInterface and OfficialModelMatch in Lean.
- [ ] Search immutable snapshots for an unconditional FixedWitness or G21Pointwise term.
- [ ] Audit assumptions and #print axioms; compile under pinned toolchain.

No status promotion; no proof of P != NP asserted.
