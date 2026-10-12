# ATK — Terminal Certificates (fail-closed)

## Contents
- `ATK/UniversalContracts.lean`: conditional contracts for all seven problems.
- `ATK/TerminalCertificate.lean`: typed proof certificate and conjunction theorem.
- `terminal_manifest.json`: seven independent certification gates.
- `certificates/{RH,NS,YM,BSD,HODGE,BEAL,PNP}.json`: explicit missing proof obligations.
- `tools/certify.py`: source hashes, marker scan, optional `lake build`, audit output.
- `.github/workflows/terminal-audit.yml`: GitHub workflow for kernel build and artifacts.

## Certification policy
No `TERMINAL_CERTIFIED` claim unless the exact original mathematical statement is imported, the universal inhabitant and bridge are implemented, `lake build` succeeds, transitive axioms are checked, and evidence is tied to immutable source and run identifiers. This package does not yet provide those seven proofs.

Run `python3 tools/certify.py` locally. If Lake is unavailable, the audit records `NOT_RUN`. The audit always fails closed for mathematical terminal claims. The GitHub workflow is a template and has not been executed.
