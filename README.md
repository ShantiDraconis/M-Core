# M-Core v1

A minimal formal audit core for obstruction functionals and downstream dependency rules.

## Frozen core

\[
M\text{-core}=(\mathcal I,S_0,\mathrm{DAG\_rule})
\]

with

\[
S_0=(u_0,I_0^*,\nu_0,\chi_0,N_0,T_0)
\]

and `S0` is immutable after initialization.

`DAG_rule = downstream_of_G1_only`.

**Non-circularity invariant:** any coefficient `a(t)` used downstream of G1 must be constructed exclusively from data available at or upstream of G1. In particular it may not read the target quantity `Y(t)=||ω(t)||` (or an equivalent encoding of the conclusion it is used to prove).

## Rigid admissibility tests for `I ∈ S`

### A1 — AMPLITUDE

For amplitude scaling `u ↦ A u`, require the audit to track

\[
I(Au)=A\,I(u).
\]

Hence, whenever `I(u₀)>0`,

\[
\sup_{A>0} I(Au_0)=\infty.
\]

Therefore an amplitude-homogeneous functional of degree one cannot satisfy a universal fixed gap `I ≤ 1-δ` over an amplitude-unbounded admissible class without an additional normalization/restriction.

### A2 — SELFREF

If

\[
I(u)=G(u)/H(u),
\]

the dependency graph must be acyclic. A construction is rejected when evaluating `I` requires `a(t)`, while `a(t)` requires `Y`, and `Y` is itself established only through a bound involving `I`.

Forbidden dependency cycle:

`I → a(t) → Y → I`.

### A3 — ZERO

If a proposed quotient degenerates to `0/0` on the zero-vorticity locus `ω=0` (including quantities such as `K0`, `RHO`, `ETA`), it is not total until a regularization/extension is specified and proved path-independent. Two admissible approaches to `ω→0` yielding different limits constitute failure of the unregularized definition.

### A4 — SCALE

The intended class is scale-critical: under the problem-specific critical rescaling `u ↦ u_λ`, the audit requires

\[
I(u_\lambda)=I(u).
\]

Numerical constants or thresholds are **not axioms merely because they were observed numerically**. In particular the working values `Φ≈0.6`, `ε₀≈0.6`, and the sequence `0.309 → 0.594 → 0.609` are recorded as calibration/test data until derived from explicit definitions and hypotheses.

A candidate stopping-time form may be audited as

\[
\tau_{max}=\inf\{T^*-t:Q_j(t)>\varepsilon_0\},
\]

but its rigidity requires a separate theorem proving scale invariance and the claimed threshold.

## M-Core v1 test budget

Exactly **24 tests**:

- `META/` — 5 tests. Audit whether the stated hypotheses can imply a universal fixed gap `I ≤ 1-δ`; distinguish an actual impossibility theorem from failure of a particular proof architecture.
- `BOUNDARY/` — 12 tests. Amplitude, scaling, zero-locus and path-limit edge cases, including finite representatives for the formal `A→∞` and `λ→∞` regimes.
- `MEMBERSHIP/` — 7 tests. Separate adapters for NS, YM, RH, BSD, P-vs-NP, Hodge and Poincaré.

## Scientific-status rule

A membership test means only that a **precisely defined adapter** satisfies the M-Core interface and its proved axioms. It does not imply that the corresponding Millennium problem is solved, equivalent to another problem, or governed by the same PDE quantities. Cross-problem membership claims must therefore supply problem-specific definitions and proofs rather than reuse `ω`, `Y`, `a(t)`, or Navier–Stokes scaling by analogy.

## Planned tree

```text
M-Core/
├── README.md
├── lakefile.lean
├── lean-toolchain
├── MCore/
│   ├── Core.lean
│   ├── State.lean
│   ├── DAG.lean
│   ├── Admissible.lean
│   ├── A1Amplitude.lean
│   ├── A2SelfRef.lean
│   ├── A3Zero.lean
│   └── A4Scale.lean
├── Tests/
│   ├── Meta.lean
│   ├── Boundary.lean
│   └── Membership.lean
└── Membership/
    ├── NS.lean
    ├── YM.lean
    ├── RH.lean
    ├── BSD.lean
    ├── PvsNP.lean
    ├── Hodge.lean
    └── Poincare.lean
```

The formal development must keep theorem status explicit: `PROVED`, `CONDITIONAL`, `DEFINITION/INTERFACE`, `NUMERICAL_EVIDENCE`, or `OPEN`.

## DOI / Scientific record

- DOI: [10.6084/m9.figshare.33990856](https://doi.org/10.6084/m9.figshare.33990856)
- Author ORCID: [0009-0006-6874-3910](https://orcid.org/0009-0006-6874-3910)
