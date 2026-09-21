# Cross-Problem Gap Taxonomy

Status: STRUCTURAL CLASSIFICATION / NO MATHEMATICAL PROMOTION
Date: 2026-09-21

This map groups certified, reusable, discarded, and open material by logical shape.
Similarity never implies theorem transfer. An edge is admissible only after exact
statement/hypothesis/domain/quantifier/axiom/circularity/semantic compatibility.

## Similarity levels

- EXACT: same logical object/interface modulo definitional renaming or an already-proved equivalence.
- STRUCTURAL: same proof shape and same failure mode, but problem-specific mathematics differs.
- ANALOGICAL: useful heuristic/test pattern only; no theorem transport.
- DISJOINT: no justified cross-problem reuse beyond generic certification infrastructure.

## Global status classes

- CERTIFIED: kernel-checked and frozen/reproducible.
- REUSE: certified material admissible after compatibility check.
- OPEN: genuine remaining mathematical producer.
- DISCARDED: invalid as producer because of axiom, sorry/admit, trivialization, circularity, semantic mismatch, or finite-to-universal shortcut.
- NEGATIVE_CONTROL: discarded as proof but retained because it certifies a failure mode.

## Group A — EXACT / near-exact reusable infrastructure

### A1. Fail-closed certification firewall — EXACT across all seven
Shared shape:
  zero sorry/admit/sorryAx
  explicit axiom footprint
  circularity audit
  semantic exact-match
  nontriviality/adversarial check
  clean rebuild
  freeze by exact SHA

Status: CERTIFIED/REUSE.
Applies to: BEAL, RH, PNP, HODGE, YM, BSD, NS.
This is genuinely the same infrastructure and should exist once in M-Core.

### A2. Certified-consumer pattern — EXACT
Shared shape:
  producer -> already-certified consumer chain -> endpoint

Status: CERTIFIED/REUSE.
Current abstraction: MCore.UnifiedTerminalLogic.TerminalChain.
The producer is problem-specific; the consumer pattern is identical.

### A3. Reuse compatibility edge — EXACT
Shared shape:
  old theorem + explicit exactTransfer -> new local theorem

Status: CERTIFIED/REUSE.
Current abstraction: ReuseCompatibility.

## Group B — STRUCTURAL equivalence: same proof/failure shape, different mathematics

### B1. NONTRIVIAL WITNESS
Problems:
  BEAL: produce a universal nontrivial common divisor / TripleGCD > 1.
  PNP: produce a concrete official-model language in NP with genuine not-in-P / UniversalFailure.

Common logical form:
  exists/construct W, Valid(W) and Nontrivial(W), then certified consumer closes endpoint.

Shared reusable material:
  witness nontriviality firewall
  trivial-witness adversarial tests
  semantic identity of the witness
  no oracle/circular construction

What is NOT shared:
  number-theoretic proof for Beal
  complexity lower-bound proof for PNP

Similarity: STRUCTURAL, not theorem-level.

### B2. VANISHING / ASYMPTOTIC CONTROL
Problems:
  RH: DN_N <= eps_N with eps_N -> 0 / zero-residue control.
  NS: terminal integrability/uniform depletion parameters required to close critical control.

Common failure mode:
  finite/local evidence does not imply universal/asymptotic control.

Shared reusable material:
  finite-to-limit firewall
  uniformity checks
  quantifier-order audit
  explicit dependence on parameters
  compactness/tightness conditions must be proved, not inferred

Differences:
  RH is an approximation/limit vanishing problem.
  NS is PDE coercive/integrability control with time-dependent coefficients.

Similarity: STRUCTURAL at the audit level; mathematical transfer is absent.

### B3. REALIZATION / SURJECTIVITY
Problems:
  HODGE: every rational Hodge class is realized by algebraic cycles.
  YM: abstract/regulated objects must realize a genuine 4D physical theory/Hilbert-spectrum object.

Common failure mode:
  a formally inhabited interface can be too weak, phantom, or equivalent to the desired conclusion.

Shared reusable material:
  realization must carry scientific content
  no Prop := True placeholders
  no endpoint hidden in constructor fields
  no circular reformulation
  domain/quantifier exactness

Differences:
  Hodge realization is algebraic-cycle surjectivity.
  YM realization is physical QFT reconstruction and spectral identification.

Similarity: STRUCTURAL, high-value negative-control reuse.

### B4. ARITHMETIC-ANALYTIC / COERCIVE TRANSFER
Problems:
  BSD: analytic order / leading coefficient must match arithmetic invariants.
  RH adjacent LC route: coercivity + WEF compatibility -> RH.
  NS: analytic control must transfer to endpoint regularity.

Common shape:
  source invariant/control + compatibility bridge -> target invariant/endpoint.

Shared reusable material:
  compatibility morphism must be explicit
  no hidden normalization changes
  exact domains/constants
  transfer theorem separated from producer theorem

Differences:
  BSD arithmetic-analytic equality is number theoretic.
  RH WEF/LC is spectral/explicit-formula analytic.
  NS transfer is PDE regularity/coercivity.

Similarity: STRUCTURAL/ANALOGICAL depending the exact edge.

## Group C — SAME FAILURE MODE discovered in discarded material

### C1. TRIVIAL INTERFACE / TRUE PLACEHOLDER
Observed:
  HODGE classical artifacts: predicates/theorems collapsing to True.
  YM old physical interfaces: phantom/trivial interfaces.
  structural historical repos: True placeholders.

Classification:
  DISCARDED as producer.
  NEGATIVE_CONTROL retained.

Cross-problem rule:
  any interface whose inhabitability does not force scientific content is rejected.

Strength of connection: EXACT failure mode.

### C2. AXIOM-GATE MASQUERADING AS THEOREM
Observed:
  RH lc-rh-coercivity: WEF_gate remains axiom gate.
  HODGE classical: standardConjectureD axiom.
  YM classical/Coq: assumed continuum/gap content.
  historical structural repos: explicit LRE axioms.

Classification:
  DISCARDED as unconditional producer.
  NEGATIVE_CONTROL retained.

Cross-problem rule:
  downstream theorem from an unproved axiom gate cannot promote endpoint.

Strength: EXACT failure mode.

### C3. CIRCULAR REFORMULATION
Observed:
  HODGE K26: equivalent payload reformulations do not reduce the open mathematics.
  PNP wrappers that merely restate not-in-P are not lower bounds.
  BSD aliases like BSDOpenCore := BSDRankPart do not add proof.
  Beal CommonPrime/CommonDivisor equivalence alone does not produce the divisor.

Classification:
  NEGATIVE_CONTROL.

Cross-problem rule:
  if proposed producer is equivalent to endpoint/open payload with no independent theorem, count zero progress.

Strength: EXACT failure mode.

### C4. FINITE -> UNIVERSAL / ASYMPTOTIC LEAP
Observed:
  RH finite DN ladders do not prove DN_N -> 0.
  PNP finite SAT experiments do not prove asymptotic lower bounds.
  BSD curve-specific certificates do not prove universal BSD.
  NS finite/local numerical control does not prove universal regularity.
  Beal checked exponent families do not prove universal Beal unless residual families are exhausted.

Classification:
  NEGATIVE_CONTROL.

Cross-problem rule:
  finite evidence may guide search, never close a universal quantifier.

Strength: EXACT failure mode.

### C5. SEMANTIC / DOMAIN / QUANTIFIER MISMATCH
Observed across all chains.

Examples:
  official computational model mismatch in PNP;
  arbitrary-codimension vs known-case Hodge;
  physical vs formal spectral interfaces in YM;
  exact ESS hypothesis matching in NS;
  normalizations/leading coefficient conventions in BSD;
  concrete DN family vs adjacent coercivity interface in RH.

Classification:
  NEGATIVE_CONTROL + global firewall.

Strength: EXACT infrastructure-level failure mode.

## Group D — ANALOGICAL only

### D1. RH <-> BSD
Both compare analytic data to deep arithmetic/spectral structure.
No currently certified theorem transports the RH producer into BSD or vice versa.
Use only shared audit patterns: normalization, order of vanishing, compatibility.

### D2. HODGE <-> BSD
Both contain realization/comparison aspects involving algebraic/arithmetic invariants.
No exact producer is shared.

### D3. YM <-> NS
Both are field/PDE-adjacent and use analytic control, scales, spectra/regularity.
But YM constructive QFT/mass gap and NS classical fluid regularity are distinct endpoints.
Shared only: uniformity/coercivity/limit firewalls.

### D4. BEAL <-> BSD
Both number-theoretic, but current terminal producers are fundamentally different:
divisibility witness vs analytic-rank/leading-coefficient equality.
No direct mathematical reuse currently justified.

## Group E — DISJOINT problem-specific kernels

These should NOT be forcibly unified:

BEAL:
  Frey/local arithmetic, exponent signatures, gcd/common-prime production.

RH:
  Nyman-Beurling/Baez-Duarte family, DN limit, BCF residue analysis, WEF compatibility.

PNP:
  Turing-machine/circuit/complexity model and genuine asymptotic lower bounds.

HODGE:
  algebraic cycles, Hodge classes, Chow/Hilbert/specialization geometry.

YM:
  constructive 4D QFT, Osterwalder-Schrader reconstruction, physical Hilbert space, spectral gap.

BSD:
  elliptic/abelian arithmetic, analytic order, Mordell-Weil rank, Sha/regulator/period/leading coefficient.

NS:
  Navier-Stokes PDE, vorticity/stretching, Campanato/CZ control, critical regularity, Gronwall.

These kernels share certification infrastructure but not substantive theorem content.

## Maximum predicted organization

Layer 0 — ONE common certification kernel
  hygiene + axiom + circularity + semantic + nontriviality + clean rebuild.

Layer 1 — FIVE reusable failure firewalls
  trivial-interface
  axiom-gate
  circular-reformulation
  finite-to-universal
  semantic/domain/quantifier mismatch

Layer 2 — FOUR producer shapes
  witness
  vanishing/asymptotic
  realization/surjectivity
  control/transfer

Layer 3 — SEVEN problem-specific terminal payloads
  BEAL, RH, PNP, HODGE, YM, BSD, NS.

Layer 4 — SEVEN already-certified consumer/endpoints
  each activated only by an exact local producer proof.

This is the maximal safe compression predicted from the current corpus.
