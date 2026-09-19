# Provenance correction — 2026-09-19

This record corrects an ambiguity in earlier progress summaries.

## Rule

A file, theorem, or GREEN workflow observed only on an `attack/*` branch or
draft PR MUST NOT be reported as the state of the repository default branch.
Candidate evidence and main-line evidence are distinct.

## Verified state

| Problem | Main contains candidate artifact? | Candidate branch | Candidate head | Candidate CI | Mathematical status |
|---|---|---|---|---|---|
| Hodge | NO | `attack/witness-kernel-v1` | `860f329f20cb7393013981b8ef5074deb8ae2050` | run 35434622519 SUCCESS | OPEN |
| BSD | NO | `attack/witness-kernel-v1` | `fd9401e7c05b5fcb2a84e6ea22418c596e55b650` | run 35434624015 SUCCESS | OPEN |
| Beal | NO | `attack/witness-kernel-v1` | `a8da5b8c89d00c6b2369c867d748d0d3855dc509` | run 35434625441 SUCCESS | OPEN |
| P vs NP | NO | `attack/material-orientation-v1` | `f14c2e1854d6b62dc3e5b567a6769a04075f76d5` | run 35434631321 SUCCESS | OPEN |
| Riemann | NO | `attack/typed-final-endpoint-v1` | `7f482b6e19fc73dffe319fa1e0716a9b634b5211` | run 35434627621 SUCCESS | OPEN |
| Yang–Mills | NO | `attack/typed-final-endpoint-v1` | `bf51318ce56b9fcb3c67c692104a37ab98661666` | run 35434630249 SUCCESS | OPEN |
| Navier–Stokes | NO | `attack/g1-uniformity-v1` | `7e4f8d1bd149132d7fd00f3e2de84ee2599dc9f8` | G1 run 35436856529 SUCCESS; audit run 35436856528 FAILURE; multiprover 35436856547 not globally certified at audit time | OPEN |

All seven PRs were verified as OPEN, DRAFT, and NOT MERGED at the time of this audit.

## Navier–Stokes SHA check

Commit `7e4f8d1bd149132d7fd00f3e2de84ee2599dc9f8` exists in GitHub on
`attack/g1-uniformity-v1`. Its diff in
`formal/millennium/lean/MillenniumAudit/HypothesesComplete_v3.lean` replaces

`linarith`

in the positivity proof with

`exact sub_pos.mpr hBudget'`.

`formal/millennium/lean/MillenniumAudit/G1Uniformity.lean` also exists on that
candidate branch and contains the pointwise/uniform separation and toy
countermodel. Neither artifact is present on `main`.

## Interpretation of GREEN

For these candidate branches, GREEN means only that the branch's stated
formal/CI gates passed. It does NOT mean:
- the candidate is merged to main;
- the conjecture is solved;
- the abstract semantic interface has been instantiated with the accepted
  mathematical objects;
- an OPEN_BRIDGE has been mathematically discharged.

## Fail-closed policy

Any future report must include:
- repository;
- main SHA;
- candidate branch;
- candidate SHA;
- artifact path;
- workflow run;
- integration status;
- mathematical proof state.

If `integration = candidateBranch`, the result cannot be described as the
state of `main`.
