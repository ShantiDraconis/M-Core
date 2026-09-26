# ATL v3 — canonical control plane

ATL v3 is an infrastructure/control layer. It does **not** promote any open problem or imported literature result.

## Canonicality

Only primitives in `graph.json` plus append-only log events are persisted. Dependencies, consumers, promotion states, replacement routes, cut rankings, mining applicability and certificate readiness are derived views.

Hard invariants:

- `GREEN_INFRA != GREEN_MATH`.
- `OPEN_MATH` is a classification, not a promotion state.
- `FORMULATION_FALSIFIED` is router evidence, not theorem promotion.
- Regression creates a new version and `superseded_by`; it never rewrites history.
- `REPLACES` is an edge path, never a free-form route string.
- `EGC_MINED` requires a kernel-audited extraction theorem.
- FINAL_PROOF / FINAL_ROOT / EXTERNAL_CERTIFICATE are views of one certificate object, not independent mutable states.

## Five roles

PLANNER -> RECOVERY -> PROVER -> AUDITOR -> CERTIFIER.

PROVER retry policy: at most 3 implementation retries, then planner escalation. Reclassification to RESEARCH/EXTERNAL must be an append-only event with reason/evidence.

## Five firewalls

1. AXIOM — kernel axiom footprint and forbidden proof escapes.
2. CIRCULARITY — canonical DAG and statement-hash dependency graph.
3. SEMANTIC — frozen statement identity.
4. INTERFACE — no abstract Prop/interface presented as computational realization.
5. VACUOUS — reject empty-domain/trivial-hypothesis shortcuts unless explicitly justified.

The Python firewall performs structural/static checks. Kernel axiom checking remains a Lean/CI responsibility and cannot be replaced by Python.

## Min-cut

Primary heuristic:

`sum(cost(node) / downstream_unlock(node))`

Only `OPEN_MATH_ATTACKABLE` participates. RESEARCH and EXTERNAL are excluded and flow to explicit certificate conditions.

Before 20 empirical samples, costs are heuristic and must be labeled as such.

## Proof mining

Mining is orthogonal to theorem promotion. Applicability is a classification. A mined certificate is emitted only after an extraction theorem exists and survives the same kernel/semantic firewalls.

## Publication boundary

A conditional certificate proves only the formal implication actually inhabited. A reproducible pipeline is evidence about the method. Neither is a proof of an unresolved endpoint unless the endpoint term itself is present and audited.
