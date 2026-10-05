# M-Core Research OS — Quickstart

## Requirements

- Lean 4.19.0
- Mathlib 4.19.0

The repository pins these versions through `lean-toolchain` and `lakefile.lean`.

## Build

```bash
lake update
lake build
```

A successful build verifies the included Lean targets for this release. It does not by itself prove any OPEN_MATH endpoint.

## Research status

Use the repository's explicit status vocabulary:

- PROVED
- CONDITIONAL
- DEFINITION / INTERFACE
- NUMERICAL_EVIDENCE
- OPEN

Millennium-problem adapters and terminal-gap documents are research artifacts unless a specific endpoint theorem is separately established.
