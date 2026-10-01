# OPEN_MATH CONVERGENCE MASTER — 2026-10-01

Status: FORWARD_ONLY / EXACT_RESIDUALS / NO_DUPLICATE_SCAFFOLD

This ledger separates:
- PROVED: kernel-checked theorem or certified reduction;
- REFUTED: route formally countered or logically invalid for the endpoint;
- OPEN: exact missing mathematical inhabitant;
- CANDIDATE: useful mechanism that does not yet produce the terminal object.

## Global invariant

The seven-lane root is structurally assembled. No global wrapper is missing.
The only legitimate remaining work is problem-specific material extraction.

The tri-state material kernel is now wired by:
- `MCore.MaterialMath.TriStateTerminalClosure`
- `triState_closes_global_root`

This theorem is exact: a `TriNumber ℝ` closes the global root only when accompanied by the seven problem-specific `TriStateTerminalAdapters`.
The tri-state algebra itself does not erase the OPEN_MATH obligations.

## RIEMANN — F1 / VANISHING

### PROVED
- concrete NB carrier and `concreteGeneratorFamily`;
- `FiniteSpanApproximatesChi ↔ DNLimit = 0`;
- every finite-span vector has an exact finite coefficient vector;
- optimal finite coefficients exist at every finite N;
- explicit coefficient error -> 0 implies `DNLimit = 0`;
- BCF residue identity is available as an unconditional external identity.

Strongest reuse:
- `frozen/rh-direct-density-integration-green-b239b00c`
- `frozen/rh-direct-coefficient-endpoint-green-0b2720d`
- `frozen/rh-explicit-coefficient-producer-green-c994a84d`
- `frozen/concrete-final-36793021586-20261001`

### REFUTED / PRUNED
- undamped natural Möbius full sequence as the critical L2 convergent approximant;
- finite-N numerical extrapolation to the asymptotic theorem;
- zero-density alone as universal off-line-zero elimination;
- zero-free-region estimates that leave 1/2 < beta < 1;
- functional-equation symmetry alone as residue cancellation;
- RH-conditional negative zeta-derivative moment arguments as unconditional closure.

### OPEN
`ZERO_RESIDUE_SUM_UNCONDITIONAL_CONTROL`

Equivalent concrete attack form:
construct one explicit coefficient family c_N such that
`||chi - Σ_{n<N} c_N(n) rho_n||_2 -> 0`.

Mellin form:
`∫ |1 - zeta(1/2+it) P_N(1/2+it)|^2 /(1/4+t^2) dt -> 0`.

### TRI-STATE CONNECTION
A tri-state F1 `VanishingLaw` is useful only after proving an adapter identifying its phase-energy trajectory with the concrete DN error. That adapter remains OPEN.

---

## P VS NP — F2 / GAP

### PROVED
P01 mechanical construction is CLOSED/FROZEN/CERTIFIED:
- frozen SHA `720596c0bd3900b5de25eab57b7b979d2a6aaf68`;
- run `36862291065`;
- SAT-in-NP side follows.

P02 infrastructure proved:
- candidate coding;
- declared polynomial clocks;
- operator kernel;
- Kleene/fixed-point infrastructure;
- failure normal forms;
- final compression;
- same-input hardened semantics.

Strongest reuse:
- `atk/p02-only-20261001`
- `atk/pnp-rigorous-terminal-decomposition-20261001`

### REFUTED
- arbitrary encoder model;
- literal same-string fixed-point route;
- finite failure -> universal lower bound;
- supplied lower-bound field disguised as a producer.

### OPEN
`CandidateFailureFamily`

Equivalent:
`EncodedP02Target`
`EncodedSATNotInP`

Concrete content:
for every encoded deterministic polynomial-time SAT candidate, construct a canonical circuit on which it fails.

### TRI-STATE CONNECTION
A tri-state F2 `GapLaw` does not imply P≠NP unless an explicit reduction maps every polynomial-time candidate to an admissible tri-state whose positive phase gap yields a canonical SAT failure witness. That reduction is OPEN.

---

## NAVIER-STOKES — F7 / LIMIT

### PROVED
- bulk/tail algebra;
- strict signed depletion from `BulkAbsorption + ExceptionalTailControl + SubcriticalBudget`;
- `SignedGainCore ↔ SignedGainCertificate` at the certified interface;
- differential coercive consequence;
- downstream stabilization wiring.

Strongest reuse:
- `frozen/ns-signed-gain-core-green-df808543`
- `frozen/ns-signed-gain-differential-green-6e67a011`
- `attack/ns003-strict-signed-producer-v1`

### REFUTED / PRUNED
- amplitude-invariant fixed-delta shortcut;
- legacy dynamic interfaces that do not derive from the PDE;
- purely algebraic nonnegativity bookkeeping as a substitute for NSE estimates.

### OPEN / EXTERNAL UPDATE
Positive regularity route remains:
`ActualNSToSignedGainCore`.

However, the official problem also admits a breakdown orientation. On 2026-09-08
OpenAI released a Lean formalization of forced finite-time breakdown, and on
2026-09-11 Clay stated that the problem had "apparently been settled" while
evaluation remains ongoing.

External Lean declarations:
- `NavierStokes.Comparator.navier_stokes_breakdown_R3`
- `NavierStokes.Comparator.navier_stokes_breakdown_periodic`

Local architecture now includes:
- `NavierStokesBreakdownTarget`
- `NavierStokesResolutionTarget = positive ⊕ negative`

Integration state:
`EXTERNAL_FORMAL_CLOSURE_CANDIDATE / PORT_REQUIRED`.

Reason:
external toolchain is Lean 4.34.0-rc2; M-Core is Lean 4.19.0. Do not break the
central kernel by direct import. Port or independently comparator-check the
exact statements first.

Thus `ActualNSToSignedGainCore` is no longer the only route to the official
Navier-Stokes endpoint; it remains the live positive/unforced regularity route.

### TRI-STATE CONNECTION
A tri-state F7 limit law must be derived from actual NSE observables, with phase variables explicitly defined from the velocity/vorticity field and with a proof that the phase dissipation gives the strict signed-gain budget. That PDE-to-tristate adapter is OPEN.

---

## HODGE — F4 / REALIZATION

### PROVED
- HodgeHabitant type;
- concrete payload equivalences;
- codimension trisection;
- R1/R2/R3 transport;
- low-codimension conditional machinery;
- final conditional transport to the Hodge endpoint.

Strongest reuse:
- `cert/hodge-all-green-c5ad87d0-run36271922378`
- `cert/hodge-habitant-type-3dc8a3de-run36271922378`
- `frozen/openmath-residual-36792765735-20261001`

### REFUTED / PRUNED
- empty/trivial geometry payloads;
- generic abstract interface with no cycle-valued realization;
- assumed-complete closure as an unconditional proof;
- transport that presupposes the cycle as a producer of the cycle.

### OPEN
`UniversalMiddleCodimensionRealization`

Equivalent operationally to a genuine `HodgeHabitant`:
for every admissible rational Hodge class, construct an algebraic cycle realizing it.

### TRI-STATE CONNECTION
A tri-state F4 `RealizationLaw` closes Hodge only if its source type is mapped to genuine algebraic cycles on each smooth projective variety and the realization relation is proved to be the cycle-class map. This geometry adapter is OPEN.

---

## BSD — F5 / EQUALITY

### PROVED
- same-carrier grounded state model;
- rank/refined composition interfaces;
- rigorous Sha carrier interface;
- final transport from a rigorous grounded habitant.

Strongest reuse:
- `atk/bsd-grounded-habitant`
- `frozen/openmath-residual-36792769076-20261001`
- `BSDRigorousFrontier.lean`

### REFUTED
- universalization of arbitrary `BSDRankData`;
- a bare natural number `shaOrder` as a proof of Sha finiteness;
- cross-curve/cross-normalization promotion;
- finite curve tables as a universal proof.

### OPEN
A genuine `RigorousGroundedBSDHabitant`:
1. analytic order = Mordell-Weil rank;
2. actual finite Sha carrier with cardinality tied to the state;
3. refined leading coefficient identity;
all on the same elliptic curve.

### TRI-STATE CONNECTION
An F5 tri-state `EqualityLaw` must be pulled back from genuine elliptic-curve invariants, not arbitrary real observables. The curve-to-tristate invariant map and the proof that equality is exactly BSD are OPEN.

---

## BEAL — F6 / EXCLUSION

### PROVED
- endpoint compression;
- common-divisor/common-prime/gcd equivalences;
- final composition;
- B01/B02/endpoint atomic decomposition.

Strongest reuse:
- `frozen/openmath-residual-36792772606-20261001`

### REFUTED / PRUNED
- conductor bookkeeping alone;
- renamed common-prime wrappers without a universal witness;
- finite arithmetic search as universal closure.

### OPEN
Logical minimum:
`GCDLowerBoundProducer`

Equivalent endpoint content:
for every admissible Beal datum,
`1 < gcd(a,gcd(b,c))`.

Scientific Frey/level-lowering route currently decomposes into 12 atomic obligations, but these are not logically mandatory if a direct proof of the gcd producer is found.

### TRI-STATE CONNECTION
An F6 `ExclusionLaw` can close Beal only after mapping every admissible triple to a tri-state and proving that coprime triples lie in a forbidden phase-energy configuration. That arithmetic adapter is OPEN.

---

## YANG-MILLS — F2 / GAP

### PROVED
- hardened nontrivial B3/B4/B5 interfaces;
- regulator/volume cofinality;
- regulated transfer operator tied to the same measure/action;
- nonzero uniform regulated mass-scale interface;
- K23/K25/K27/K30 composition;
- B60 adapter -> conditional mass-gap endpoint.

Strongest reuse:
- `frozen/ym-physical-inhabitant-frontier-green-ecf745b2`
- `frozen/b60-validate-36792578767-20261001`
- `frozen/physical-residual-36792907807-20261001`

### REFUTED / PRUNED
- Unit/True physical models;
- spectral gap wrapper unrelated to the regulated construction;
- fixed-regulator gap promoted to continuum mass gap;
- legacy B3/B4/B5 phantom interfaces.

### OPEN
Genuine `PhysicalResidual` / `B60ConcretePhysicalAdapter`:
same regulated 4D construction -> physical Hilbert states -> reconstruction -> uniform continuum/infinite-volume control -> non-vacuum excitation -> K30 spectral transfer.

### TRI-STATE CONNECTION
A tri-state F2 gap can model the spectral geometry only after a proof that the tri-state phase energy is a faithful lower bound for the physical Hamiltonian spectrum and survives regulator/volume limits. This physical spectral adapter is OPEN.

---

# Global convergence

PROVED:
- all structural reductions and final composition layers needed to expose the seven exact terminals;
- the tri-state algebra, order-three rotation, fixed-point characterization, phase energy, F1/F2/F4/F5/F6/F7/F8 abstract laws;
- exact theorem: tri-state kernel + seven exact terminal adapters -> global positive root.

REFUTED:
- structural descent alone -> arbitrary theorem;
- trivial target replacement;
- problem-specific shortcut routes listed above.

OPEN:
exactly the problem-specific adapter/material theorem in each lane.

Therefore the correct interpretation is:

`TriNumber` provides a common algebraic language.
`TerminalMaterialAdapters` are the seven missing mathematical bridges.
No bridge may be replaced by a wrapper, an equivalence, a finite experiment, or an assumption carrying the endpoint itself.


## 2026-10-01 forward-only delta

### NAVIER-STOKES external negative route
Dedicated port branch:
`ShantiDraconis/navier-stokes-critical-barrier-audit@atk/ns-external-breakdown-port-v434-20261001`

Pinned external source:
`openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

Local port commits:
- `54fb5b53e0ccabe4d7e3ae2a9bde80585c9039ec` — toolchain -> Lean 4.34.0-rc2
- `5250a1a971b3fd25baf43566bf79fc7dbc12e0e2` — pin external formalization package
- `afdadd92bb2078f195e97609d4dcb0eb13cc57e9` — local R3/periodic breakdown certificate bridge

Status:
`BUILD_PENDING_NO_ACTIONS`.

Reason:
the current execution container has no external DNS, and GitHub Actions are intentionally not being consumed. The bridge has not yet been promoted to GREEN.

Promotion rule:
GREEN only after independent build/axiom audit of the exact port branch.

### P VS NP — Kleene firewall strengthened
Branch:
`ShantiDraconis/m-core-p-vs-np@atk/p02-only-20261001`

Commits:
- `dc6cc4c877a4abe881978832f97fc4565e40d365` — `P02KleeneFirewall.lean`
- `3e1d9f3efc049f837ba60c3aed790a9025755173` — root import

New proved firewall:
for any candidate correct on every canonical SAT input and any effective
diagonal compiler, `SATFixedPointRealizer` is uninhabited.

Consequence:
Kleene recursion theorem is structural only. The missing
`SATFixedPointRealizer` / `SemanticDiagonalFamily` already contains the
material lower-bound content and cannot be generated by fixed-point packaging
alone.

### BEAL exact-domain audit
`BealData` was rechecked. Its fields are exactly:
positive a,b,c; exponents x,y,z > 2; and a^x+b^y=c^z.

No hidden gcd/common-prime assumption is present.
Therefore `GCDLowerBoundProducer` is not definitionally or structurally
inhabited; it remains genuine arithmetic OPEN_MATH.


### RH multistate hardening — 2026-10-01

Repository:
`ShantiDraconis/m-core-riemann@atk/rh-multistate-decay-hardening-20261001`

Commits:
- `0ab16337c2a0c312a28c81bdc4d66aa4014e13b6` — legacy multistate decay counteraudit + hardened real decay
- `a1495a01440ff469c5c17e493f6cb409fd56bfa4` — root import

Finding:
legacy `WeightedModularBilinearDecay` was structurally trivial because its
`vanishes : Prop` field was unconstrained by `sequence`. Every sequence
could inhabit it by taking `vanishes := True`.

Therefore:
- `MultistateSN` remains valid as presentation/invariance structure;
- `close_0_1_2_from_weighted_decay` must NOT be treated as an RH proof;
- no promotion through the legacy decay interface is allowed.

Hardened replacement:
`RealWeightedModularBilinearDecay` carries
`Filter.Tendsto sequence Filter.atTop (nhds 0)`.

A genuine vanishing majorant now produces the hardened certificate by squeeze.
The mathematical frontier is unchanged: prove a real quantitative decay
estimate for the canonical S_N / DN sequence.


## Tri-cyclic contraction proposal kernel — 2026-10-01

Commits:
- `bc7c8327950e272673cb477c45fba77e3ec2cb41` — exact transverse contraction theorem
- `a4164561fa32e7c48ba2ffdd32ec12ab4628d37f` — root import
- `103fde2894552a19d3e52327b6fece3f82fd7a8f` / hardened by `010be73a2670d47ce013b64f2490723d6c193a85` — scalar defect embedding
- `f1dc2482e903359550d0aef32905d10b37a104e2` — root import
- `370bd5e7edc82fbe01dacfea074c1d7a595b2f86` — scientific proposal document

PROVED:
1. Every real tri-state splits uniquely into balanced + zero-sum fluctuation.
2. The transverse Laplacian has eigenvalue -3 and normalized Laplacian energy 9.
3. For
   `x_n = balancedProjection(x) + q^n * fluctuation(x)`
   with `0 <= q < 1`,
   `phaseEnergy(x_n) = (q^2)^n * phaseEnergy(x)`.
4. Therefore the phase energy tends to zero geometrically.
5. Every scalar defect d has canonical zero-sum embedding `(d,-d,0)`.
6. Its phase energy is exactly `6*d^2`.
7. Embedded phase energy is zero iff d=0.

SCIENTIFIC PROPOSAL:
For scalar-defect lanes, the tri-state representation itself is no longer an
OPEN adapter. The remaining open mathematics is to prove that the official
defect observable obeys a genuine contraction/vanishing estimate and that the
existing official endpoint consumes that defect.

For RH this means the open step is not "find a tri-state representation":
DN/weighted error can be embedded canonically. The open step is prove its
actual asymptotic contraction/vanishing.

For F2 lanes, the internal positive spectral gap is also already proved; the
open step is a faithful semantic/physical identification with the official
lower-bound or mass-gap observable.

No open problem is promoted by this kernel alone.


## Evidence-driven attack delta — 2026-10-01

### RH: logarithmic transverse profile
Certified finite Gram values in m-core-riemann give DN_N * log N approximately:
0.05024, 0.04961, 0.04870, 0.04731, 0.04686, 0.04566 for N=8..256.

Interpretation:
- evidence is compatible with DN_N on a 1/log N energy scale;
- therefore residual norm d_N is on a 1/sqrt(log N) amplitude scale;
- uniform geometric contraction q<1 is not the natural RH model.

Formal response:
- `ProfiledTransverseDecay.lean` now proves
  `phaseEnergy = a_n^2 * phaseEnergy(x)`
  for arbitrary profile a_n;
- any proved a_n -> 0 gives an F1 law;
- this includes a future logarithmic profile without assuming it.

Open analytic target remains:
prove a genuine upper bound for the official DN/Mellin defect.

### BEAL: exact surviving counterexample class
Evidence from T11/T12/T59 in the frozen Beal residual branch proves that any
surviving counterexample can be reduced to a concrete `T59ResidualCandidate`
with all of:
- positive a,b,c;
- reduced exponents x,y,z;
- exact equation a^x+b^y=c^z;
- pairwise primitive bases;
- exactly one of a,b,c even;
- mixed reduced exponent signature;
- exclusion of the all-four branch.

Therefore all earlier non-primitive/parity/equal-prime/all-four branches are
closed reductions and must not be attacked again.

Current scientific target:
eliminate every `T59ResidualCandidate` by genuine local conductor / modularity /
level-lowering / newform arithmetic, or find a direct contradiction from the
residual arithmetic conditions.

### External evidence firewall
A recent preprint claiming a quantitative Beurling-Nyman rate strong enough to
force DN -> 0 is not promoted. A claim of that strength is effectively an RH
closure and requires independent verification of every imported hypothesis.
Published Bettin-Conrey-Farmer asymptotics remain conditional on RH plus a
negative zeta-derivative moment bound.


### RH coefficient Pythagoras frontier — 2026-10-01

Branch:
`ShantiDraconis/m-core-riemann@atk/rh-optimal-coefficient-pythagoras-20261001`

Commits:
- `b993fb9772d8f34f7dace7a362cdbb4d5f83fc70` — exact Pythagorean coefficient-error decomposition
- `e6716fec2c4d906e1fa3227220d5c92d72e2e9cc` — root import
- `6bfbcafd7ece8e3a1da3f2c75454b87652a471cf` — finite excess-energy audit
- `32049f06f7bde908e6e636b6fac1b94d2903cb0d` — coefficient Gram-energy identity
- `b7517526d4a70018580c06f4946c946dd20be3ce` — root import

New exact identities:
1. For every finite coefficient vector c,
   ||chi-v_c||^2 = DN_N + ||P_N chi-v_c||^2.
2. The excess over the optimum is exactly the squared projection gap.
3. For every coefficient correction r,
   ||v_r||^2 = r^T G_N r.
4. Hence for c=c*+r, the correction penalty is exactly the Gram quadratic
   energy of r.

Finite N=256 evidence:
- alpha=3/16 total error is about 3.0024 times the optimum;
- about 66.69% of that finite error is projection-gap/correction energy;
- raw Möbius has about 80.28% correction-energy share;
- linear-log taper about 93.38%.

Interpretation:
simple Möbius/taper families fail mainly because they remain too far from the
finite optimal coefficient vector. The next nontrivial analytic target is not
another blind taper but a provable decomposition

c*_N = -mu * w_N + r_N

with a uniform estimate on r_N^T G_N r_N and a vanishing total residual.

Status of new Lean sources: SOURCE / BUILD_PENDING until independently built.
No RH promotion.


## Two-sided material resolution rule — 2026-10-01

The project now accepts both mathematical orientations for an open endpoint,
but not via the trivial classical proposition P or not-P.

Generic kernel:
`lean/MCore/MaterialMath/TwoSidedMaterialResolution.lean`
commit `41cb453fa7c8dec5f43f026a1840ac9011a1bd96`.

For endpoint P, define concrete producer types A and B together with
A -> P and B -> not P.

Resolution status:
- POSITIVE_RESOLVED iff Nonempty A;
- NEGATIVE_RESOLVED iff Nonempty B;
- BOTH_INCONSISTENT iff both are inhabited;
- OPEN_MATH iff neither producer is inhabited.

Classical excluded middle alone does not inhabit A or B and therefore cannot
promote an endpoint.

### RH two-sided frontier
Branch:
`ShantiDraconis/m-core-riemann@atk/rh-two-sided-resolution-20261001`
commit `0cdeefdc910dad58e92e7930a97aa67da7098380`.

Positive producer:
`VanishingUpperBound concreteNBData concreteGeneratorFamily`.

Negative producer:
`PersistentPositiveLowerBound concreteNBData concreteGeneratorFamily`
with eps>0 and eps <= DN_N for every N.

Consequences:
- positive -> DNLimit=0;
- negative -> DNLimit>0, hence DNLimit != 0;
- both -> False.

Root import was not promoted because the tool mutation was blocked; source
remains BUILD_PENDING.

### Beal two-sided frontier
Branch:
`ShantiDraconis/m-core-beal@atk/beal-two-sided-resolution-20261001`.

Commits:
- `832bd29e24fa4960ee5683886beb85bc5c9d09d0` — two-sided theorem
- `a8efa26c8c67f1066f54346f1e739c3b58f605cc` — root import

Positive producer:
`GCDLowerBoundProducer`.

Negative producer:
one concrete `T59ResidualCandidate`.

New theorem:
every `T59ResidualCandidate` is a genuine Beal counterexample because its
pairwise-primitivity forbids any common prime divisor.

Therefore:
- positive producer -> BealConjecture;
- residual candidate -> not BealConjecture;
- both -> False.

Status remains SOURCE / BUILD_PENDING until compilation.


### Beal residual congruence attack — 2026-10-01

Branch:
`ShantiDraconis/m-core-beal@atk/beal-two-sided-resolution-20261001`

New commits:
- `a21a32c684742f73e172c98fcffad5018d987fd2` — eliminate c-even orientation for x=y=4
- `292c0b0eb0d1dee9bd28a569c8885785c2be1003` — root import
- `3f6d4945bec3cba24730e14529a5ad84e82a9a61` — mod-16 residue constraint
- `f31a5a7819bb1c99b08468d8ef0d38f0e276e77b` — root import

Exact new arithmetic consequences for every residual T59 candidate with x=y=4:
1. c cannot be the unique even base.
2. Therefore the unique even base is a or b.
3. The equation forces c^z mod 16 = 1.

This narrows the T51 twoFourPrime family before any Frey/conductor/level
lowering input. The remaining orientations are not claimed impossible.

Status: SOURCE / BUILD_PENDING until compiled.


### Beal sharp residue frontier — 2026-10-01

Branch:
`ShantiDraconis/m-core-beal@atk/beal-two-sided-resolution-20261001`

New commits:
- `76238ac0483acf53716ca6ce66724f1f3197cbfd` — complete mod-16 residue atlas for all (4,4,p) permutations
- `f2165138850031aa1a793e4e9aff4dd3e36f681a` — sharpen odd-prime-power conditions to base residue classes
- `77cc78e0b04a6afe3d71ad8470723590ecc4ad66` — root import

Exact consequences for T59 residual candidates in the two-four-prime family:

1. x=y=4:
   - c is not even;
   - c^z mod 16 = 1;
   - when z is the odd-prime exponent, c mod 16 = 1.

2. x=z=4:
   - if a is the unique even base, then b mod 16 = 1;
   - if c is the unique even base, then b mod 16 = 15;
   - the b-even orientation retains the automatic odd-fourth constraint.

3. y=z=4:
   - if b is the unique even base, then a mod 16 = 1;
   - if c is the unique even base, then a mod 16 = 15;
   - the a-even orientation retains the automatic odd-fourth constraint.

These are necessary local conditions before any T60/B01 conductor or
level-lowering mathematics. They do not eliminate the whole family.

Status: SOURCE / BUILD_PENDING until compilation.


### Beal quartic prime-support frontier — 2026-10-01

Branch:
`ShantiDraconis/m-core-beal@atk/beal-two-sided-resolution-20261001`

New commits:
- `3bc746ffb109c5e863392e1ac34eef62d89fef78` — exact quartic factorization via existing T21DiffQuot
- `74da7406d44201af71fd26d6849d51e023cb3f8e` — root import
- `ad5d52c7d67b5e39f66e830eb5bf695e0cd588e0` + hardened `3235c9eab572b2e5bc32dee4cbbfa487189f8e63` — odd-prime separation of linear factors
- `4a4c7e761a01859b9b96898f3b849e83122dd803` — candidate-specific odd-prime support packet
- `f3743dd40c29b231260e846265fea7e581c44d62` — root imports

Exact factorization:
- x=z=4:
  b^y = (c-a)(c+a)(c^2+a^2)
- y=z=4:
  a^x = (c-b)(c+b)(c^2+b^2)

New local consequences:
- no odd prime divides both c-a and c+a on x=z=4;
- no odd prime divides both c-b and c+b on y=z=4;
- every odd prime dividing c-a or c+a divides b;
- every odd prime dividing c-b or c+b divides a.

This is candidate-specific arithmetic data upstream of T60/B01 and is not
present in the earlier generic T31-T34 radical-support package.

Next exact target:
prove odd-prime separation of the quadratic factors c^2+a^2 / c^2+b^2 from
the corresponding linear factors. That would decompose the quartic product
into three pairwise odd-prime-disjoint blocks, preparing valuation/conductor
information.

Status: SOURCE / BUILD_PENDING until compilation.


### Global material theorem V2 — 2026-10-01

New central commits:
- `c6c6d8728d80291d65cd8324facbc5e5cb666a1b` — canonical constants, projectors and global material kernel theorem
- `13d927ad195abfc535de1b57c6bb41451a1a39e8` — global open-math behavior classes, bilateral protocol and closure audit
- `ac9d43631fb4029f0cd15668bcac8afc72984683` + wording hardening `782265b6a55f44bc4d0663e910754b6a4a98616c` — exact torsion-energy Lagrange identity
- `b23a25129efc89f677e0342e31095fc48f2c9044` — root imports
- `a2e48b1770bee86080f13d9847e45a3f3a09716e` — global research statement
- `64d6bbe9e20f9f3aaddc50d94c5899a92a421cdb` — V2 global certificate
- `9204f0a08f6461051fd5db20dbede4838c18adc1` — V2 root import

Canonical constants:
- rotation order = 3;
- transverse Laplacian magnitude = 3;
- normalized transverse Laplacian energy = 9;
- spread/radius factor = 3;
- scalar defect energy factor = 6.

Universal operator laws:
- R^3 = I;
- D = R-I;
- L = D^2 + 3D;
- D^3 + 3D^2 + 3D = 0;
- L = -3 P_tr;
- P_eq + P_tr = I;
- P_eq and P_tr are idempotent;
- E(x)=3||P_tr x||^2;
- E(iota(d))=6d^2;
- E(P_eq x + a_n P_tr x)=a_n^2 E(x).

New torsion law:
E(x)E(y) = 3 tau(x,y)^2 + 9 <P_tr x,P_tr y>^2,
hence 3 tau^2 <= E(x)E(y), equality iff transverse fluctuations are orthogonal.

Global logical rule:
material positive producer -> endpoint;
material negative producer -> negated endpoint;
both -> False;
excluded middle alone does not inhabit either producer.

Current status of all new central Lean sources:
SOURCE / BUILD_PENDING until compiled.
No open-problem endpoint is promoted merely by the global theorem.
