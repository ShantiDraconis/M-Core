# ATK Global Material Master — 2026-10-01

Status: FORWARD-ONLY MATERIAL CONSOLIDATION

This file preserves the complete current distinction between:
- kernel-checked reductions and transports;
- source-level produced inhabitants;
- conditional producers;
- formally refuted / invalidated routes;
- genuine OPEN_MATH terminal inhabitants.

No GREEN transport is promoted to a proof of an open conjecture.

## Global theorem layer

Positive formal frontier:
- `lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean`
- `GlobalPositiveMaterialRoot`
- `global_positive_root_iff_components`
- positive RH orientation firewall:
  - `rh_excludes_offCriticalZero`
  - `positive_rh_incompatible_with_negative_lane`
  - `positive_root_excludes_mixed_negative_root`

Legacy mixed-orientation theorem retained as evidence:
- `GlobalConditionalFinalRoot`
- this contains the negative Riemann/off-critical-zero orientation;
- it MUST NOT be promoted as the positive seven-problem final theorem.

## 1. RIEMANN

### Exact positive terminal
`FiniteSpanApproximatesChi concreteGeneratorFamily`

Certified equivalent/forward forms:
- `DNLimit = 0`
- `DNToZero`
- sufficient route: `VanishingUpperBound`
- sufficient route: BCF / zero-residue control

### Certified evidence
- SHA `d6a291b4563f9021f74ab63cc983d44f079472da`
  - theorem `finiteSpanApproximatesChi_iff_DNLimit_eq_zero`
- SHA `5c66f8dca03834f24a61a9b1219e7af9d4892dd6`
  - scope: `VanishingUpperBound -> DNToZero -> DNLimit=0`
- historical K8 GREEN:
  - SHA `ad3011f14bdab32161205e053fa925bc8c851ad4`
  - run `35565114760`

### New global law
Positive RH excludes any inhabitant of the off-critical-zero semantic target:
`RiemannHypothesis -> ¬ Nonempty RiemannOffCriticalZero`.

### Rejected as closure
- off-critical-zero target as positive RH;
- transport-only RH wrappers;
- scoped certificate without the material terminal inhabitant.

### Exact remaining inhabitant
`FiniteSpanApproximatesChi concreteGeneratorFamily`

State: OPEN_MATH.

---

## 2. BEAL

### Exact terminal
`GCDLowerBoundProducer := ∀ d : BealData, 1 < Nat.gcd d.a (Nat.gcd d.b d.c)`

### Certified laws
- `bealConjecture_iff_gcdLowerBoundProducer`
- `bealConjecture_iff_commonDivisorProducer`
- CommonDivisor -> prime divisor -> CommonPrime
- global semantic law:
  `Nonempty BealUniversalGCDTarget ↔ ∀ d, 1 < gcd(d.a,gcd(d.b,d.c))`

### Certified evidence
- direct producer SHA `d6fe130c44ef91e0f8ceb6b15a6548f186e381fd`
- runs `36493742792`, `36493742928` SUCCESS
- K6: `434d6b7bba82298e7f90e13817f147011bef5b1e`, run `35092395821`
- K9 frozen: `e3b8598a2513b539b285dfb31dc383b770ab840f`

### Formal open-status evidence
- `bealWithoutOracleClosed = false`
- theorem `beal_without_oracle_still_open`

### Rejected as closure
- conductor bookkeeping alone;
- renamed CommonPrime/CommonDivisor wrappers without universal witness.

### Exact remaining inhabitant
A function proving the scalar gcd lower bound for every admissible Beal datum.

State: OPEN_MATH.

---

## 3. P VS NP

### Canonical material split
P01:
`Nonempty P01MachineConstruction`

P02:
`G21Pointwise`

Equivalent P02 forms:
- `P02Target`
- `SAT ∉ P`
- `UniversalFailure SATTarget`
- `Nonempty FailureGenerator SATTarget`
- `Nonempty CanonicalSATP02Producer`
- `Nonempty SemanticDiagonalFamily`

### P01 mechanical construction — CLOSED / FROZEN / CERTIFIED
Authoritative frozen branch:
`frozen/p01-verifier-phase-mincut-green-720596c0`

Certificate ref:
`cert/p01-verifier-phase-mincut-green-720596c0`

Frozen SHA:
`720596c0bd3900b5de25eab57b7b979d2a6aaf68`

Authoritative run / job:
`36862291065 / 110369170512`

Producer theorem:
`P01RawTotalizationProducer.p01ConstructionGap_closed : P01ConstructionGap`

Derived canonical consequence:
`P01PostMinCutClosure.canonical_sat_in_np_closed : SATInNPGap circuitBitEncoding`

Status:
`CLOSED_KERNEL_GREEN_FROZEN_CERTIFIED`.

Forward-only rule:
DO NOT reopen or reconstruct P01. Reuse the frozen certificate and attack only the same-language universal deterministic lower-bound producer.

### P02 certified kernel
- validated SHA `fa83d082fe219a772aa41c981e6b0fa420ff2aac`
- run `36831482480` SUCCESS
- frozen `frozen/p02-kernel-green-fa83d082`
- certificate branch `cert/p02-kernel-fa83d082-run36831482480`

Validated:
- P02OperatorKernel
- P02FinalCompression
- P02UniversalLowerBound
- P02UniversalKernel
- P02KleeneKernel
- P02EffectiveAlignment

### Exact semantic law
`Nonempty (PvsNPSeparationTarget Language InP InNP SAT) ↔ (InNP SAT ∧ ¬ InP SAT)`

### Refuted / invalidated routes
1. Arbitrary encoder model:
   `every_language_inP_under_arbitrary_encode`
   and `current_SATNotInP_refuted`.
2. Literal same-string G2.1 fixed-point route.
3. Finite-failure evidence -> universal lower bound:
   `finite_to_universal_principle_refuted`.

### Exact remaining P02 inhabitant
Canonical form:
```lean
UniversalFailure
  (CanonicalSATBoundary.SATBits CanonicalCircuitBits.circuitBitEncoding)
```

Equivalent pointwise producer form:
```lean
∀ M : PolyDTMCandidate,
  ∃ x : BitString,
    CanonicalSATValid x ∧
    (SATTarget x ↔ ¬ AcceptsAtDeclaredBound M x)
```

State:
P01 CLOSED/FROZEN/CERTIFIED; P02 OPEN_MATH.

---

## 4. NAVIER–STOKES

### Exact terminal producer
`ActualNSToSignedGainCore`

Signature:
```text
(u : State) -> ActualNS u -> SignedGainCore ν (data u)
```

### Material certificate fields
- `theta < 1`
- `stretch(t) ≤ theta * nu * z(t) + C * y(t)^2`

### Certified downstream
- normalization to nonnegative theta/C;
- `SignedGainCore ↔ SignedGainCertificate` at Nonempty level for nonnegative viscosity;
- `SignedGainCertificate -> FlexibleStretchingBound`;
- Leray-energy-compatible lower-order budget;
- `signedGain_implies_differential`:
  `y' + 2(1-theta)nu z <= 2 C y^2`;
- `signedGain_dissipation_margin_pos` for `nu > 0`.

### Certified evidence
- core SHA `df808543535d34d4e8c46096b3455d76b0151fa2`
- run `36496747228`
- downstream SHA `6e67a01173e2364c85bc341d95b229623272f7b0`
- run `36493553756`
- certificate `CERTIFICATES/NS_SIGNED_GAIN_CORE_GREEN_df808543.md`

### Nontriviality firewall
`signedGainCertificate_not_trivially_inhabited`

### Invalidated interfaces
- DynamicCriticalGeometry
- FullChain
- nonnegativity bookkeeping without PDE-derived producer

### Exact remaining inhabitant
Construct the signed-gain core from genuine 3D Navier–Stokes dynamics.

State: OPEN_MATH.

---

## 5. HODGE

### Exact terminal
`ConcreteAlgebraicityPayload`

Certified equivalent regression target:
`TrivialQbarR2Payload`

Certified theorem:
`trivial_qbar_r2_payload_iff_concrete_payload`

Sufficient forward producer strategy:
`H01MinimalForwardPayload`

### Certified base
SHA:
`42eaf7d4d639871f82eceb121ee525a6c4f30d84`

Scope:
H01MinimalForwardPayload is sufficient for the concrete pointwise Hodge endpoint.

### Exact semantic law
`Nonempty HodgeRealizationTarget ↔`
for every smooth-projective X and rational Hodge class alpha,
there exists a cycle Z realizing alpha.

### Rejected as closure
- empty-variety payload;
- abstract geometry shell without genuine cycle binding.

### Exact remaining inhabitant
Universal concrete algebraicity realization in arbitrary codimension.

State: OPEN_MATH.

---

## 6. BSD

### Correct terminal
The producer MUST be bound to a genuine realizable elliptic-curve domain and provide simultaneously:
1. analytic order = Mordell–Weil rank;
2. refined leading-coefficient identity;
3. Sha finiteness wherever required by the refined statement.

### Exact semantic law
`Nonempty BSDRealizableTarget ↔ (rank equality on realizable domain ∧ refined formula on same domain)`

### Certified architecture
K7–K14 and TOTAL chain are reusable architectural evidence.

Universal-promotion firewall:
- SHA `c1e7b245726c4c65f5f9f878acefb86460746f4a`

### Formally rejected abstraction
`∀ d : BSDArithmeticAnalyticData, BSDRankPart d`

Reason:
the abstract data interface admits unrelated natural-number data and is counter-audited.

Additional rejected closure:
- `BSDOpenCore` alias;
- curve-specific evidence promoted universally;
- finite evidence promoted universally.

### Formal open-status evidence
`bsdRankPartWithoutOracleClosed = false`

### Exact remaining inhabitants
- genuine elliptic-curve model binding;
- universal rank equality;
- refined identity;
- required Sha finiteness.

State: OPEN_MATH (two mathematical subparts after model binding).

---

## 7. YANG–MILLS

### Exact sufficient material producer
`Nonempty (B60ConcretePhysicalAdapter C F D H G O)`

Downstream:
`B60ConcretePhysicalAdapter -> ∃ gap, K14MassGap`

Certified theorem:
`b60_adapter_closes_conditional_chain`

### Certified evidence
- B3–B5 hardening SHA `cd4bbfd348b607bd24ed0c6d605207b764286f58`
- K21 SHA `0352c6afb7e9255bf0fc777269984a2def047080`
- run `35170322803`

### Exact semantic law
`Nonempty YangMills4DGapTarget ↔`
there exists one theory satisfying:
- Genuine4D;
- OSReconstructs;
- PositiveMassGap.

### Refuted / invalidated
- legacy B3–B5 phantom interfaces;
- degenerate Unit/True physical model;
- spectral-gap wrapper without genuine regulated 4D binding.

### Exact remaining inhabitant
One genuine concrete physical adapter binding regulated 4D construction,
physical Hilbert/Hamiltonian reconstruction and the same positive-gap data.

State: OPEN_MATH.

---

# Global mathematical laws now formalized

1. Beal target iff universal scalar gcd lower bound.
2. P-vs-NP target iff SAT in NP and SAT not in P.
3. NS target iff there exists one universal stabilizer.
4. Hodge target iff every admissible rational Hodge class has a cycle realizer.
5. BSD target iff rank equality and refined formula hold on the same realizable domain.
6. YM target iff a genuine 4D reconstructed positive-gap theory exists.
7. Positive RH excludes an off-critical-zero inhabitant.
8. Positive global root excludes the older mixed negative-RH root.
9. Global positive root iff all seven material components are inhabited.

# Current inhabitant inventory

Unconditional semantic terminal inhabitants verified in the seven positive lanes:
**0 / 7**

Closed certified infrastructure component:
- P-vs-NP P01: `p01ConstructionGap_closed` / frozen SHA `720596c0bd3900b5de25eab57b7b979d2a6aaf68` / run `36862291065`

All other currently located objects are one of:
- certified reductions;
- equivalences;
- conditional producers;
- downstream transports;
- refutations/firewalls;
- historical provenance.

# Exact global frontier

The final positive root is now represented by:

`GlobalPositiveMaterialRoot`

and flattened exactly by:

`global_positive_root_iff_components`.

No information is discarded by the flattening theorem.

The remaining work is therefore not another global wrapper.  It is the seven
problem-specific material producers listed above (with P01 already source-produced
and P02 remaining the genuine P-vs-NP mathematical atom).


# Exact strongest-reuse index — 2026-10-01

Forward-only rule: these artifacts are the current maximum reusable frontiers. Do not recreate their internal reductions. Attack only the residual listed for each lane.

## RIEMANN
Reuse:
- `frozen/rh-direct-density-integration-green-b239b00c`
- `frozen/rh-direct-coefficient-endpoint-green-0b2720d`
- `frozen/rh-explicit-coefficient-producer-green-c994a84d`
- `frozen/concrete-final-36793021586-20261001`

Already closed:
- concrete NB carrier and `concreteGeneratorFamily`;
- finite-span / `DNLimit = 0` equivalence;
- exact coefficient-vector realization of every finite-span vector;
- explicit-coefficient-convergence -> `DNLimit = 0`.

Attack only:
`ZERO_RESIDUE_SUM_UNCONDITIONAL_CONTROL`, or equivalently an unconditional explicit coefficient family with critical-L2 error -> 0.

Do not retry:
- undamped natural Möbius full sequence (L2 route refuted);
- finite-N numerical extrapolation;
- RH-conditional BCF estimates;
- zero-density/zero-free estimates that do not eliminate every off-line residue.

## P VS NP
Reuse:
- frozen P01 SHA `720596c0bd3900b5de25eab57b7b979d2a6aaf68`, run `36862291065`;
- `atk/p02-only-20261001`;
- `atk/pnp-rigorous-terminal-decomposition-20261001`.

Already closed:
P01, SAT-in-NP construction, candidate coding, clocks, operator/Kleene/universal kernels, and final composition.

Attack only:
`CandidateFailureFamily` / `EncodedP02Target` / `EncodedSATNotInP`.

Do not retry:
literal same-string fixed points, arbitrary encoders, finite-failure -> universal-lower-bound promotion.

## NAVIER-STOKES
Reuse:
- `frozen/ns-signed-gain-core-green-df808543`;
- `frozen/ns-signed-gain-differential-green-6e67a011`;
- strict bulk/tail -> signed-depletion producer in `attack/ns003-strict-signed-producer-v1`.

Already closed:
bulk/tail-to-depletion algebra once `BulkAbsorption`, `ExceptionalTailControl`, and `SubcriticalBudget` are supplied; SignedGainCore downstream.

Attack only:
derive the strict signed-gain/bulk-tail hypotheses uniformly from genuine 3D NSE, i.e. inhabit `ActualNSToSignedGainCore`.

## HODGE
Reuse:
- `cert/hodge-all-green-c5ad87d0-run36271922378`;
- `cert/hodge-habitant-type-3dc8a3de-run36271922378`;
- `frozen/openmath-residual-36792765735-20261001`;
- `atk/next-hodge-genuine-geometry-binding-20260929`.

Already closed:
habitant type, payload equivalences, codimension trisection, R1/R2/R3 transport, low-codimension conditional machinery.

Attack only:
`UniversalMiddleCodimensionRealization` / genuine `HodgeHabitant`.

Do not promote `HodgeAssumedCompleteClosure`: it is an assumed-complete route, not an unconditional inhabitant.

## BSD
Reuse:
- `atk/bsd-grounded-habitant`;
- `frozen/openmath-residual-36792769076-20261001`;
- `BSDRigorousFrontier.lean`.

Already closed:
same-carrier data model, final composition, rigorous Sha carrier interface.

Attack only:
a genuine `RigorousGroundedBSDHabitant`: rank equality + finite Sha realization + refined leading coefficient law on the same elliptic curve.

## BEAL
Reuse:
- `frozen/openmath-residual-36792772606-20261001`;
- scalar nested-gcd frontier;
- atomic B01/B02/endpoint decomposition.

Already closed:
all endpoint compression and final composition.

Attack only:
`GCDLowerBoundProducer` (logical minimum), optionally through the 12 atomic scientific obligations.

## YANG-MILLS
Reuse:
- `frozen/ym-physical-inhabitant-frontier-green-ecf745b2`;
- `frozen/b60-validate-36792578767-20261001`;
- `frozen/physical-residual-36792907807-20261001`;
- K23/K25/K27/K30 composition.

Already closed:
hardened nontrivial B3/B4/B5 interfaces and B60 -> conditional mass-gap composition.

Attack only:
the genuine `PhysicalResidual` / `B60ConcretePhysicalAdapter` inhabitant tying the regulated 4D construction to the same physical Hilbert/Hamiltonian theory and uniform positive spectral gap.
