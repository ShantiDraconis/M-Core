# Frozen scientific certificates

This ledger records durable SHA-based scientific checkpoints for the RH audit branch.
GitHub Actions run history, logs, artifacts, and caches are operational evidence with configurable retention; the repository SHA and versioned source are the durable reference.

## Scientific checkpoints

| Gate | Commit SHA | CI run | Status | Certified scope |
|---|---|---:|---|---|
| Finite Gram determinant gate | `347842be05c90e597963ad643a358fb5e9a9193f` | `35082166447` (#27) | `PROVED_LEAN + CI PASS` | Generic finite real inner-product Gram trivial-kernel/determinant consequence under the stated linear-independence hypothesis. No uniform-in-N coercivity claim. |
| ProjectionDistance gate | `74d3f261bf8d80d7bd8371841966b8f9f837c536` | `35083576289` (#30) | `PROVED_LEAN + CI PASS` | Nested finite spans, nonnegative squared infimum distance, antitonicity/successor monotonicity, and subsequence-to-full zero convergence theorem compiled through the root import. |

## Infrastructure checkpoints (not scientific certificates)

| Commit SHA | CI run | Classification | Note |
|---|---:|---|---|
| `13f43aac9d44a956977216d3f152c3f831261fdc` | `35090371590` (#31) | `INFRASTRUCTURE_ONLY` | Introduced Lean/Lake cache. Lean job passed; Python job failed during `setup-python` because `cache: pip` was enabled without a dependency manifest. No mathematical source change. |
| `83c886577da4b65468b27faf08f024e1232922c2` | #32 | `INFRASTRUCTURE_ONLY / AWAITING_CI` | Removes the invalid pip-cache option while preserving Lean/Lake incremental cache. No mathematical source change. |

## Epistemic status

- `ProjectionDistance`: `PROVED_LEAN + CI PASS` at the frozen #30 SHA above.
- `NymanBeurlingCriterion`: intended as an explicit external literature contract; not a Lean proof in this repository unless separately formalized.
- `CentralBridge`: `OPEN_BRIDGE`.
- `RH_PROVED`: `FALSE`.

## Freeze policy

A SHA is promoted to the scientific checkpoint table only when (1) the commit contains a mathematical/formal change in the certified scope, (2) the complete required CI gates pass at that exact SHA, and (3) the claim recorded here does not exceed the theorem statements actually compiled. Infrastructure-only commits remain separate even when CI is green.
