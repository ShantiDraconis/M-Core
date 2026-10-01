# MATERIAL PRODUCER EVIDENCE MATRIX — 2026-10-01

Status: RESEARCH EVIDENCE / NO ENDPOINT PROMOTION

This ledger records why each current material producer is mathematically motivated.
External literature is evidence for the route or downstream implication only.
No citation below is treated as an inhabitant of an OPEN_MATH producer.

## Riemann

Formal producer:
- ConcreteLogMajorantCertificate
- exact residue: exists K >= 0 such that for every N,
  DN(N) <= K / log(N+2)
- formal closure: log majorant -> VanishingUpperBound -> DNToZero -> DNLimit=0 -> FINAL_ROOT
- concrete specialization commit: 38509bc8171af702baacc4503f52134db05709bf

Evidence:
- Bettin–Conrey–Farmer, "An optimal choice of Dirichlet polynomials for the Nyman-Beurling criterion",
  arXiv:1211.5191.
  Their sharp asymptotic result is conditional on RH plus a negative zeta-derivative moment hypothesis.
  Therefore it supports the shape of the route but cannot inhabit the producer.
- Maier–Rassias, Canadian Math. Bulletin 61 (2018), 622–627, DOI 10.4153/CMB-2017-070-3.
  Off-critical zeros produce a genuine obstruction in the same Nyman–Beurling/Baez-Duarte approximation regime.
- Internal R2 audit isolates ZERO_RESIDUE_SUM_UNCONDITIONAL_CONTROL as the strongest current analytic residue.

Classification:
ROUTE_SUPPORTED / MATERIAL_INHABITANT_OPEN.

## P versus NP

Formal producer:
- UniversalSATLowerBound / UniversalFailure canonical SAT
- equivalent to Nonempty CanonicalSATP02Producer and SAT not in P
- P01/SAT-in-NP side is already closed and frozen
- effective/Kleene adapter closure commit: 72149cc18b144260c41681da9c972e6d09e2e77f

Evidence:
- Cook–Levin establishes SAT as the canonical NP-complete language.
- The official problem remains whether a polynomial deterministic solver exists; no known theorem supplies the universal counterexample producer.

Classification:
CANONICAL_TARGET_SUPPORTED / LOWER_BOUND_INHABITANT_OPEN.

## Navier–Stokes

Formal producer:
- canonical target: ActualNSToSignedGainCore
- deeper analytic route:
  BulkAbsorption + ExceptionalTailControl + SubcriticalBudget -> strict signed depletion
- representation bridge commit:
  03ad152dc61c65542003a257cbdc17399b73d948
- this bridge produces the canonical SignedGainCore with C=0 from the richer G1 data

Evidence:
- Escauriaza–Seregin–Sverak endpoint regularity implies that bounded L^infinity_t L^3_x control excludes first-time blowup.
- Modern regularity literature supports critical-norm and concentration routes, but does not derive the required universal bulk/tail/subcritical estimate from arbitrary smooth 3D NSE evolution.
- Internal audit isolates three genuine analytic obligations:
  O1 joint coherence from ActualNS;
  O2 singular-kernel weighted exceptional-tail control;
  O3 nonlinear gain yielding an energy-integrable coefficient / strict budget.

Classification:
DOWNSTREAM_REGULARITY_SUPPORTED / G1_MATERIAL_ESTIMATE_OPEN.

## Hodge

Formal producer:
- ConcreteHodgeMaterialTarget:
  nonempty geometry + CycleSpanAdapter + ConcreteAlgebraicityPayload
- hardening commit: f1f0f848d97c32221c2d929451b0f05b907a1ee0
- current factorization:
  R0 concrete model binding + R1 spread + R2 algebraic point/cycle production + R3 specialization/variational algebraicity

Evidence:
- Cattani–Deligne–Kaplan proves algebraicity of Hodge loci in smooth projective families.
- This does not by itself prove that every rational Hodge class is represented by an algebraic cycle, so it supports R1/R2 geometry but does not inhabit the terminal payload.
- Official Hodge statement requires rational combinations of algebraic cycles on smooth projective varieties.

Classification:
SPREAD/HODGE_LOCUS_GEOMETRY_SUPPORTED / GENERAL_ALGEBRAICITY_OPEN.

## Birch–Swinnerton-Dyer

Formal producer:
- genuine elliptic-curve realizability semantics
- rank equality on that same curve
- refined leading coefficient identity using the same normalized period, regulator, Sha, Tamagawa and torsion data
- abstract BSDArithmeticAnalyticData blanket route is formally refuted
- with a valid low-rank theorem, the rank part compresses to the analytic-rank >= 2 residual

Evidence:
- Gross–Zagier/Kolyvagin establish the rank conclusion in analytic ranks 0 and 1 for modular elliptic curves; all elliptic curves over Q are modular.
- Existing rank-0/rank-1 results do not supply the all-rank statement or the full refined leading coefficient identity in general.
- Internal architecture correctly keeps Sha finiteness and normalization provenance explicit.

Classification:
LOW_RANK_DOMAIN_SUPPORTED / HIGH_RANK_AND_REFINED_FORMULA_OPEN.

## Yang–Mills

Formal producer:
- B60FieldBundle
- bundle commit: 119ba78a2feb442c33ae08b3a8639e841ff83705
- fields:
  physical state/observable maps;
  K23 constructive YM4 inputs;
  K25 clustering/infrared bridge;
  K27 regulated positive gap and limit control;
  non-vacuum excitation;
  K30 spectral transfer witness
- downstream K22 blocks and FINAL_ROOT are constructed from these fields

Evidence:
- Official Yang–Mills problem requires both construction of a nontrivial 4D quantum Yang–Mills theory and a positive mass gap.
- Constructive QFT / Osterwalder–Schrader machinery motivates regulated Euclidean construction, reflection positivity, Hilbert reconstruction, infinite-volume/continuum control and spectral gap transfer.
- The official description explicitly notes that the 4D construction and uniform mass-gap/infinite-volume control remain open.

Classification:
PHYSICAL_ARCHITECTURE_SUPPORTED / B60_FIELD_INHABITANT_OPEN.

## Beal

Formal producer:
- UniversalTripleGCDLowerBound:
  for every admissible Beal datum,
  1 < gcd(a, gcd(b,c))
- exact equivalence with BealConjecture is already formalized

Evidence:
- The standard formulation of Beal says any solution A^x+B^y=C^z with x,y,z>2 has a common prime factor.
- Therefore the triple-gcd lower bound is not merely analogous: it is the scalar canonical form of the same common-factor claim.

Classification:
EXACT_ENDPOINT_REFORMULATION / INHABITANT_OPEN.

## Global rule

Evidence may justify:
- choice of producer;
- correctness of downstream operators;
- known special cases;
- rejection of vacuous or circular routes.

Evidence may not be promoted to:
- a universal inhabitant;
- a missing asymptotic estimate;
- a theorem outside its stated hypotheses;
- a final certificate for an unsolved endpoint.
