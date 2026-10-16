# M-Core v2 — 24-test gate

The gate separates executable witnesses from mathematical theorems. A green Python test never upgrades an OPEN obligation to PROVED.

## Python audit — 12 gates
1–3 A1 witnesses for δ=.1,.01,.001.
4 A1 increasing/unbounded witness family.
5 A2 G1↔G4 cycle detected.
6 A2 downstream rule rejects target feedback.
7–9 A3 explicit same quotient G/H along K0/RHO/ETA paths; G,H→0 and ratios differ.
10–11 A4 scale fixture at λ=1e-3 and 1e3.
12 A4 calibration firewall: Φ samples may be recorded, but ε0/tau rigidity remain unset until proved.

`test_S0_frozen` is an invariant gate run alongside the 12 and does not consume a mathematical slot.

## Lean/spec — 12 obligations
13 `A1Amplitude.amplitude_unbounded` — PROVED in core.
14 `A1Amplitude.no_fixed_delta_gap` — PROVED in core.
15 canonical self-reference cycle — formal graph theorem required.
16 `downstream_of_G1_only` — formal dependency theorem required.
17 same-quotient zero-locus construction — explicit G,H and paths required.
18 incompatible path limits imply no total continuous extension — core theorem exists; connect to #17.
19 problem-specific critical scaling invariance — adapter obligation.
20 Φ/ε0/τmax theorem — OPEN; no numerical substitution permitted.
21 NS membership — OPEN until NS functional/domain/scaling/zero extension are formalized.
22 YM membership — OPEN; independent definitions required.
23 RH/BSD membership — OPEN; independent definitions required, no reuse of NS variables by analogy.
24 S0 immutability — DEFINITION/INTERFACE; prove downstream functions take S0 read-only.

## Acceptance
A release may say `HARNESS PASS` when executable tests pass. It may say `FORMAL CORE PASS` only when Lean builds without `sorry`/new axioms for the claimed core theorem set. It may say neither `Millennium problem solved` nor `submission ready` unless the problem-specific open bridge has independently been proved and externally checked.
