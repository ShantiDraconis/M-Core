# M-Core minimal audit — four standalone Lean files

This directory isolates exactly four mathematical audit propositions.
Each Lean file imports only `Mathlib` and uses the namespace
`MCoreMinimal`. No local project modules, `Contaminated/`, `S`,
`Omega_I`, empirical calibration, or Millennium bridge is imported.

- `A1.lean`: no fixed amplitude gap under explicit homogeneity assumptions.
- `A2.lean`: the specified graph cycle is rejected by a *defined* gate.
- `G1Fix.lean`: conditional real-number energy inequality only; **does not**
  establish that a Navier–Stokes coefficient belongs to `L¹`.
- `A3.lean`: distinct specified limits have no common extension value.

The files are intentionally separate and preserve the original modules.
They do **not** prove global 3D Navier–Stokes regularity.

## Verification

Use the repository's Lean 4.19.0 / Mathlib toolchain. The dedicated workflow
`.github/workflows/mcore-minimal.yml` compiles each file independently.
Only mark this snapshot CI-certified after that workflow succeeds for the
final commit. No branch protection, release tag, or merge is implied.
