# NO-OPEN-MATH-AS-ARGUMENT POLICY — 2026-10-01

This policy is normative for forward-only terminal-producer work.

## Forbidden as producer premises

A producer theorem may not assume, directly or through an equivalent wrapper,
any unresolved terminal statement such as:
- RiemannHypothesis / DNLimit=0 / FiniteSpanApproximatesChi;
- SAT notin P / UniversalFailure SAT;
- universal Navier-Stokes regularity or official breakdown endpoint;
- universal Hodge algebraicity/surjectivity;
- BSD rank/refined formula endpoint;
- BealConjecture / universal common-prime conclusion;
- Yang-Mills 4D construction + positive mass gap.

Equivalent hypotheses, renamed endpoints, existential packages storing the
target, and fail-closed wrappers do not count as producers.

## Allowed premises

Only:
1. definitions of the official objects;
2. previously proved unconditional theorems;
3. concrete finite calculations with certified error/control;
4. standard mathematical theorems with explicit provenance;
5. explicitly constructed data;
6. local hypotheses strictly weaker than the terminal statement and discharged
   before endpoint promotion.

## Required producer shape

TYPE(E)
  -> MINIMAL_INHABITANT(E)
  -> EXACT_PRODUCER
  -> CANONICAL_OBSERVABLE
  -> OFFICIAL_ENDPOINT.

The open endpoint itself may appear only as the conclusion of the final
transport, never as an input to the producer.

## Bilateral rule

For endpoint P:
- positive producer A must be constructed without assuming P;
- negative producer B must be constructed without assuming not-P;
- A -> P and B -> not-P may be proved;
- P or not-P from excluded middle is not a resolution certificate;
- inhabitants of both A and B imply an inconsistency that must be audited.

## Current unconditional examples

### Material kernel
- C3 algebra and R^3=I;
- equilibrium/transverse decomposition;
- L=-3 P_tr;
- energy/spread identities;
- scalar-defect embedding;
- arbitrary profile energy law;
- torsion-energy Lagrange identity.

### RH
Unconditional:
- concrete DN sequence definitions;
- finite-span/projection geometry;
- Gram normal equations;
- coefficient Pythagoras identity;
- scalar/tri-state representation of a real defect.
Not unconditional:
- DN -> 0 or a positive persistent lower barrier.

### Beal
Unconditional:
- T59 residual reduction;
- parity/signature reductions;
- mod-16 restrictions;
- exact quartic factorizations;
- complete odd-prime block-support decomposition on quartic residual branches.
Not unconditional:
- elimination of every residual candidate or construction of one concrete
  residual counterexample.

### P vs NP
Unconditional:
- certified P01 construction;
- semantic equivalences and Kleene firewall.
Not unconditional:
- same-language universal SAT failure producer or polynomial SAT decider.

### Hodge / BSD / Yang-Mills
Only unconditional reductions and endpoint interfaces may be used.
Universal realization/equality/physical-gap endpoints remain conclusions, not
arguments.

### Navier-Stokes
A verified external theorem may be imported as a theorem source only after
exact statement/toolchain/axiom audit. The official endpoint itself may not be
postulated.

## Promotion rule

SOURCE -> BUILD_PENDING -> GREEN -> FROZEN -> CERTIFIED.

No source-only theorem may be called GREEN.
