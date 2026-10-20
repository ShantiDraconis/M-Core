# ATK-O1 — Source recovery and unconditionality gate (2026-10-19)

## Identification
O1 in the M-Core minimum-obligations framework is the Riemann-hypothesis lane. The original O1 is `UniformLogBound`; the weakened/minimal O1 is `Tendsto DN atTop (𝓝 0)`, equivalent in the framework to `⨅ N, DN N = 0`. The verified source theorem *states* that the minimal obligation implies RH. **This report does not independently compile that theorem.**

## Source files and blob SHA
- `atk-kernel/ATK/ObrigacoesMinimas.lean` — `4ea96f0d00172263d38b48ff89f3bff6cc46c5aa` — `O1_implica_minima`, `rh_obrigacao_suficiente`, `rh_obrigacao_iff_iInf`.
- `atk-kernel/ATK/NecessidadeBD.lean` — `d1d8a15768b8b4eef14df56d03d4f6bda5ed5763` — analytic reduction; necessity remains conditional on `EntradasNecessidade`.
- `atk-kernel/ATK/FinalRoot.lean` — `7de2a563a989c25f2dc422dc3d3833ed666491e2` — terminal producers and bridges; root conditional on their proofs.
- `atk-kernel/scripts/terminal_gates.json` — `8ff92484bc28d6fd02eb4b38bd45be9e76b03cce` — fail-closed terminal gate policy.
- `conditional/FECHAMENTO.md` — `b338407fa3e5058ba382d599424bb3cf9b4e2ab0` — conditional status and exact open gap.
- `conditional/HYPOTHESIS_MAP.md` — `1787e73a9e3b76a8b47c61f8f6e126cd6e3fa174` — hypothesis discharge index.
- `conditional/LACUNAS.md` — `7d3428e560a6e77b01fb546e23a1f03b55af5ea9` — mathematical frontier.
- `conditional/SOURCES.md` — `39a68ff2b7c03a038a90d4085e6e88c05713b58b` — historical provenance and source commit links.

These are file **blob SHAs**, not necessarily repository commit IDs.

## Logical status
1. `UniformLogBound → Tendsto DN atTop (𝓝 0) → RiemannHypothesis` is the documented sufficient chain.
2. `Tendsto DN atTop (𝓝 0) ↔ ⨅ N, DN N = 0` is the documented minimum-obligation equivalence.
3. The analytic direction `RiemannHypothesis → Tendsto DN atTop (𝓝 0)` is described as conditional on the necessary classical analytic inputs; the converse does not itself establish RH.
4. To certify O1 unconditionally, supply a theorem term for the **genuine** minimal obligation (or a faithful direct RH proof) without open mathematical premises, with exact statement alignment, imports and transitive axiom audit.
5. Grammar, semantics, operators, quantifiers and temporal phases may be defined, but their existence does not discharge the analytic obligation.
6. A conditional theorem `H → O1` is not an unconditional theorem `O1`. Seven certificates under H do not imply seven unconditional certificates.

## Operational gates
- `SOURCE`: VERIFIED for the cited files.
- `BLOCK_THEOREM`: SOURCE_PRESENT (source inspected, kernel compilation not run in this audit).
- `GRAMMAR/SEMANTICS/OPERATORS/QUANTIFIERS/TEMPORAL_PHASES`: REPORTED_DEFINED; not independently audited for semantic fidelity.
- `CONCRETE_BLOCKS`: ASSUMED_IN_HYPOTHESIS.
- `TERMINAL_O1`: CONDITIONAL_CLOSED only.
- `CERTIFICATES`: 7/7 UNDER_HYPOTHESIS is a user-reported status; each individual certificate still requires source and kernel evidence.
- `KERNEL`: NOT_EXECUTED in this audit.
- `UNCONDITIONAL`: NOT_ESTABLISHED.

## Next reproducible checks
- At a pinned repository commit, run `cd atk-kernel && lake build` and preserve logs.
- Elaborate the exact target `_root_.RiemannHypothesis` and the actual terminal theorem.
- Execute `#print axioms` on the theorem and its dependency chain.
- Verify no `sorry`, `admit`, untrusted axioms, renamed targets or false models.
- Seek the missing uniform analytic argument for `D_N → 0` independently of RH; finite numerical samples do not establish it.

**Result:** `ATK-O1: SOURCE_VERIFIED | CONDITIONAL_CLOSED | KERNEL_NOT_EXECUTED | UNCONDITIONAL_NOT_ESTABLISHED`.
