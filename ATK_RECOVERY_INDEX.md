# ATK Recovery Index

Canonical recovery map for the seven-problem ATK workflow.
Updated: 2026-09-21.

## Rules
1. Search this file before recreating any mathematical attack.
2. Frozen/certified artifacts are immutable provenance.
3. Reuse requires statement + hypotheses + quantifiers + domain + constants + dependencies + axioms + SHA compatibility.
4. A GREEN audit/build is not a proof of the official problem.
5. No sorry/admit/sorryAx, hidden axioms, oracle leakage, circular dependencies, trivial/empty witnesses, or semantic weakening.
6. Superseded branches are provenance only; do not cherry-pick them blindly.
7. Progress means reduction/proof of OPEN_MATH, not additional adapters or microtests.

## Canonical chain
CERTIFIED/FROZEN HISTORY
→ FAIL-PROOF / SEMANTIC AUDIT
→ RECOVER COMPATIBLE PRIOR MATERIAL
→ MINIMAL OPEN_MATH
→ PROVE | DISPROVE | REDUCE
→ KERNEL + AXIOM + CIRCULARITY + SEMANTIC CHECK
→ CERTIFY/FREEZE
→ NEXT OPEN_MATH
→ OFFICIAL ENDPOINT

## Riemann
Active proof line: research/pure-math-final-proof-v1.
Recovered branches:
- research/r2-dnlimit-zero — material delta: research/r2/BackwardDenseEndpoint.lean + .github/workflows/r2-formal-endpoint.yml; compared to active line: +6/-22.
- attack/r01-zero-residue-parallel-20260921 — BackwardDenseEndpoint.lean + RH/K9_RiemannHypothesis.lean + workflow; +12/-22.
- research/r2-zero-residue-probe — superseded (+0/-13).
- attack/typed-final-endpoint-v1 — old semantic source; -211 from active line, reuse only by exact semantic comparison.
Recovery chain:
typed faithful RH endpoint
→ audit/recover BackwardDenseEndpoint
→ ZERO_RESIDUE_SUM_UNCONDITIONAL_CONTROL
→ DNLimit=0
→ prove exact implication to classical critical-line endpoint.
Never treat GATE_LEDGER text as an existing theorem.

## Hodge
Active line: attack/h01-general-algebraicity-parallel-20260921.
Historical R3a branches are already behind active line and must not be reattacked:
- attack/r3-specialization-geometry-v1
- attack/r3a-hilbert-properness-v1
- attack/r3a-semantic-relative-cycle-v3
- attack/r3a-valuative-relative-cycle-v4
- attack/r3a-minimal-bridge-valuative-v5
Frozen provenance:
- frozen/hodge-r3-relative-cycle-cut-v4-8ba37af1
- cert/hodge-r3-relative-cycle-cut-v4-8ba37af1-run35525478618
Current material endpoint:
forall smooth projective X and rational Hodge alpha,
rationalSpanOfCycles alpha.
Equivalently O_Hodge(X,p)=0 universally.
R3a is provenance/reusable reduction, not the final algebraicity theorem.

## Yang-Mills
Active line used for comparison: attack/y01-4d-gap-parallel-20260921.
Recovered material:
- attack/y01-harden-physical-interfaces-20260921
  - lean/MCore/YangMills/A1/HardenedPhysicalInterfaces.lean
  - SEMANTIC_GATE.json
- attack/y01-uniform-clustering-from-gap-20260921
  - HardenedPhysicalInterfaces.lean
  - UniformIntegerClustering.lean
- attack/y01-k14-clustering-adapter-20260921
  - HardenedPhysicalInterfaces.lean
  - UniformIntegerClustering.lean
  - K14ClusteringAdapter.lean
- attack/hard-ym-4d-gap-theoremkernel — same material family.
- attack/B6-k30-concrete-realization-v1 — superseded/behind; provenance only.
Recovery chain:
HardenedPhysicalInterfaces
→ UniformIntegerClustering
→ K14ClusteringAdapter
→ audit hypotheses/axioms/trivial witnesses
→ isolate genuine 4D construction/reconstruction delta
→ rigorously define H, vacuum, spectrum
→ Delta_YM = inf(Spec(H)\{E0})-E0 > 0
→ official QYM existence + positive mass-gap endpoint.
Do not reuse the old A1 zero-estimate/trivial witness path.

## Beal
Do not reattack K8/K9/K10.
Certified/reusable logic:
CommonDivisor(nontrivial) → prime divisor → CommonPrime → endpoint wiring.
Minimal OPEN_MATH:
for every admissible BealData,
1 < gcd(A,gcd(B,C)).
Equivalent counterexample obstruction:
equation + x,y,z>2 + gcd(A,gcd(B,C))=1.
Attack only elimination of that residual case.

## P vs NP
Reuse:
- audit/EndpointCompression.lean
- audit/repro_PNP.lean
- lean/MCore/BackwardAudit/OrientedWitnessBoundary.lean
OfficialModelMatch and LowerBoundWitness wiring already exist.
Minimal OPEN_MATH:
genuine asymptotic not_in_p for SAT in the fixed official model.
Canonical chain:
SAT operational NTM/model
→ genuine lower-bound theorem
→ LowerBoundWitness.not_in_p
→ FixedWitness on OfficialModelMatch
→ official P != NP.
C12 finite data, PaysOff, costBits/Potential, and arbitrary existential interfaces do not discharge this.

## BSD
Reuse K12/K13/K14 only as fail-closed audit/wiring.
Exact rank-part target:
forall d : BSDArithmeticAnalyticData,
d.analyticOrderAtOne = d.mordellWeilRank.
RankPartWitnessContract consumes exactly this universal witness.
After rank part, full BSD still requires the universal leading-coefficient formula and arithmetic factors; do not promote rank equality alone to full BSD.
Historical curve-specific computations are evidence only, not universalization.

## Navier-Stokes
Repository: ShantiDraconis/navier-stokes-critical-barrier-audit.
Mutation rule: no commits/issues/releases without explicit user approval.
Known state:
- FAILPROOF GREEN: run 35565581964, job 106226618089.
- audit run 35565581962: RED around G1C axiom-footprint stage.
- run 35565581973: Lean RED at executable proof-escape hygiene; Coq GREEN; Agda GREEN; Isabelle cancelled.
Canonical chain:
proof-escape hygiene
→ G1C axiom footprint
→ ActualNS → XiEpsPDE → signed depletion
→ N02 endpoint regularity.
Do not roll back to N00.

## Recovery protocol
When ATK resumes:
1. Read this index.
2. Read each repo GATE_LEDGER/FRONTIER only as status metadata.
3. Search branches before concluding a file/theorem is absent.
4. Compare candidate branch against active branch.
5. Mark candidate as RECOVER, ALREADY_ABSORBED, SUPERSEDED, or INCOMPATIBLE.
6. Fetch exact files from the candidate ref.
7. Audit semantic identity and axioms.
8. Port only uncovered mathematical delta.
9. Never reduce OPEN_MATH counts merely because a branch/file exists.
