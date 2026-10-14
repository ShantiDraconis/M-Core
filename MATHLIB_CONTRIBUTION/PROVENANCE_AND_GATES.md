# ATK → Mathlib: provenance and contribution register

Date: 2026-10-14
Owner/source namespace: ShantiDraconis
Canonical source: ShantiDraconis/M-Core
Status: SOURCE / AUDIT_PENDING / UPSTREAM_NOT_SUBMITTED

## Scope
Track original mathematical statements, reusable Lean proofs, and independent verification for eventual contributions to Mathlib. This register is NOT evidence that the seven terminal conjectures have been proved.

## Provenance policy
For each candidate record: source repository, exact commit SHA, file path, Lean declaration name, statement (including hypotheses), dependencies, original author attribution where supported, license, Mathlib overlap, kernel build result, #print axioms result, and upstream review status.

Preserve original source files and commit history. Do not disclose private source code or assert priority beyond documentary evidence. No upstream submission without verifying compatibility, license, mathematical relevance and provenance.

## Initial source evidence (read from GitHub)
- M-Core/lean/MCore/FinalProofRegistry.lean — blob da146e9aff03211b4a0eba3257bc8ca162773133. The registry explicitly marks all seven terminal lanes openMath; local theorems registry_length_eq_seven, provedCount_eq_zero and openMathCount_eq_seven are proved by decide. These are internal registry invariants, not upstream Mathlib priorities.
- m-core-riemann/atk-kernel/README.md — blob 7c4fe35bf242157057350a3e69d69a56a3ec90c8. Documents four auxiliary lemmas covering majorant-to-limit, Schur step and Gram identity/bound; inspect full Lean sources and CI logs before classifying each as certified.
- m-core-beal/atk-kernel/README.md — blob 9d548f66fd914eed6eb81f3a04bbcd379692e23e. Documents one conditional gcd lemma under an FLT hypothesis; not an unconditional Beal proof.
- M-Core/conditional/CATALOG.md — blob c91b5abb3bbe1d8861a5ed4a83c75a038675f3d9. Historical inventory of 251 repositories; completeness and current state unverified.

## Candidate tiers
A. Generalizable Mathlib candidates: Gram matrix identities, Schur complement, general convergence lemmas, general divisibility lemmas, finite automata and encoding infrastructure — only after statement-by-statement review.
B. ATK library: domain-specific reductions, interfaces, conjecture-specific bridges, custom semantics, registry machinery.
C. Exclude from proof claims: hypotheses posed as assumptions, opaque axiom declarations, sorry/admit, false-target equivalences, unverified numerical extrapolations, conditional proof passed off as unconditional.

## Acceptance gates
1. Exact declaration and source SHA recorded.
2. Check for duplicate or equivalent Mathlib theorem.
3. Rebuild under pinned Lean/Mathlib toolchain.
4. Audit #print axioms and all explicit hypotheses.
5. Confirm theorem states the intended mathematical fact.
6. Add documentation, examples and tests.
7. Review license and attribution requirements.
8. Prepare upstream PR only for broadly reusable material.

## Terminal status
UNIVERSAL_GREEN: false (source registry)
FINAL_PROOF: not established
OPEN_MATH: true
MATHLIB_UPSTREAM_ACCEPTED: not verified / no claim
