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

### P01 source inhabitant found
Branch:
`atk/p01-raw-closure-final-20261001`

SHA:
`4cc78949ca812817627d3867b1328cd950156353`

Theorem:
`p01ConstructionGap_closed : P01ConstructionGap`

Status:
SOURCE_PRODUCED; not promoted here as a current global certified inhabitant until exact dependency/build alignment is independently certified.

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
```lean
∀ M : PolyDTMCandidate,
  ∃ x : BitString,
    CanonicalSATValid x ∧
    (SATTarget x ↔ ¬ AcceptsAtDeclaredBound M x)
```

State:
P01 SOURCE FOUND; P02 OPEN_MATH.

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

Source-level partial material inhabitant found:
- P-vs-NP P01: `p01ConstructionGap_closed`

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
