# ATK — Seven-lane build and material-proof gate (2026-10-09)

Status: SOURCE / BUILD_PENDING. This document is a build contract, not a proof certificate.

## Immutable inputs
- Read previous GREEN/FROZEN/CERTIFIED branches only; never rewrite them.
- Resolve each lane at an explicit commit SHA. Record toolchain, lake manifest, Mathlib revision, run ID, and job conclusion.
- Deduplicate historical source snapshots by Git blob SHA; do not assume copied Lean modules compile under their archival names.

## Independent lane order
1. P≠NP — ShantiDraconis/m-core-p-vs-np — certificate.yml.
2. RH — ShantiDraconis/m-core-riemann — certificate.yml.
3. Beal — ShantiDraconis/m-core-beal — certificate.yml.
4. BSD — ShantiDraconis/m-core-bsd — certificate.yml.
5. Yang–Mills — ShantiDraconis/m-core-yang-mills — certificate.yml.
6. Hodge — ShantiDraconis/m-core-hodge — certificate.yml. RED K25: missing MCore.K25.olean before #print axioms; verify explicit lake build MCore.K25 and MCore.K26 on a new working branch.
7. Navier–Stokes — ShantiDraconis/navier-stokes-critical-barrier-audit — millennium-multiprover.yml. Working branch atk/build-repair-20261009; first commit 01492f609394 corrected hδ unfolding, second commit 6748404a2eeb corrected relative G1 paths. Await fresh jobs.

## Fail-closed sequence per lane
SOURCE → BUILD_PENDING → GREEN (build and selected axiom checks pass) → FROZEN (immutable SHA) → CERTIFIED (explicit target type and axiom provenance audited).
A successful conditional theorem is NOT a material terminal proof. Do not promote OPEN_MATH to CLOSED_MATH from workflow success alone.

## Controlled resources
- No more than two lane builds concurrently; keep Mathlib cache scoped to exact Lean toolchain and lake manifest.
- Prefer existing lane workflows; never concatenate 661 sources into one Lean file.
- Retry only changed or failed jobs; avoid duplicate CI launches.
- Save concise run summary: lane, commit SHA, run ID, status, failed step, material endpoint obligations.

## Integration gate
- Build each repo in its own Lake project.
- Export a machine-readable registry of exact theorem names, statement types, axioms, SHA, build outcome, and open obligations.
- Import a theorem into global M-Core only if namespace, types, dependencies and toolchain match; otherwise use an explicit bridge and compile it.
- Require concrete material inhabitants and unconditional terminal proofs for any global theorem claiming conjecture resolution.
- Seven-lane global build fails closed when any lane is RED or any terminal material witness remains unproved.

## Known unresolved mathematics
RH uniform logarithmic DN bound; P≠NP integrated P01 machine and pointwise separation; Hodge general algebraicity payload; Beal universal common-prime bound; BSD rank/leading-coefficient obligations; Yang–Mills physical 4D construction and mass gap; Navier–Stokes nontrivial signed depletion G1. Do not infer these from structural adapters.
