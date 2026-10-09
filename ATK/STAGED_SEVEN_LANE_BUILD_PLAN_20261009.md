# ATK — staged seven-lane Lean build plan

STATUS: BUILD_PENDING. Existing workflows inspected; no run dispatched.

## Build policy
- Run each repository's existing certificate workflow independently; do not edit frozen branches.
- Cap concurrency at two active builds across lanes.
- Cache Lake and pin exact toolchain and dependency revisions.
- On success, capture workflow run ID, commit SHA, imported theorem types, and axiom audit.
- Global integration imports only verified modules; fail closed for missing material inhabitants.

## Existing workflow entry points
- m-core-p-vs-np: [certificate.yml](https://github.com/ShantiDraconis/m-core-p-vs-np/blob/HEAD/.github/workflows/certificate.yml)
- m-core-riemann: [certificate.yml](https://github.com/ShantiDraconis/m-core-riemann/blob/HEAD/.github/workflows/certificate.yml)
- m-core-beal: [certificate.yml](https://github.com/ShantiDraconis/m-core-beal/blob/HEAD/.github/workflows/certificate.yml)
- m-core-hodge: [certificate.yml](https://github.com/ShantiDraconis/m-core-hodge/blob/HEAD/.github/workflows/certificate.yml)
- m-core-bsd: [certificate.yml](https://github.com/ShantiDraconis/m-core-bsd/blob/HEAD/.github/workflows/certificate.yml)
- m-core-yang-mills: [certificate.yml](https://github.com/ShantiDraconis/m-core-yang-mills/blob/HEAD/.github/workflows/certificate.yml)
- navier-stokes-critical-barrier-audit: [producer-first.yml](https://github.com/ShantiDraconis/navier-stokes-critical-barrier-audit/blob/HEAD/.github/workflows/producer-first.yml)

## Non-claims
No Lean kernel build or proof certification was run as part of this plan.