# RH LC coercivity route — fail-closed semantic audit

Source snapshot audited:
ShantiDraconis/lc-rh-coercivity @ 5283a63651a53c57fc3e8d11972f2169e38de3c6

## Result

The repository index labels `Contradiction_lemma` and `LC_implies_RH` as
`kernel`, but the actual Lean declarations are axioms.

- `formal/lean/LcRh/Spectral/ApproxEigenvectors.lean`
  declares `axiom contradiction_lemma`.
- `formal/lean/LcRh/AnalysisKernel/Coercivity.lean`
  declares `axiom coercivity_threshold`.
- the same file declares `axiom lc_implies_rh`, requiring
  `WeilExplicitGate`, `TrivialTermsNormalized`, and
  `coercivity_threshold L`.
- `formal/lean/LcRh/AxiomGates/WeilExplicitGate.lean`
  declares `axiom WeilExplicitGate : Prop`.

Therefore the route is NOT an admissible theorem producer and must not be
ported into the current RH proof chain.

## What survives

The route provides a useful decomposition only:

1. define the genuine coercive form on the intended BT/VT spaces;
2. prove the coercivity threshold;
3. prove the operational Weil explicit-formula statement;
4. prove trivial-term cancellation/normalization;
5. prove off-critical zero -> genuine spectral-instability sequence;
6. derive contradiction with coercivity;
7. only then prove LC -> RH.

No current DNLimit theorem implies these obligations merely by interface
matching. A DNLimit -> LC bridge would itself require new mathematics and does
not reduce the current OPEN_MATH unless one of the above producers is proved.

## Promotion decision

LC_ROUTE_PRODUCER = REJECTED_AXIOMATIC
LC_ROUTE_DECOMPOSITION = PRESERVED
DN_TO_LC = NOT_CREATED
RH_OPEN_MATH = UNCHANGED
SORRY_PROMOTED = 0
AXIOM_PROMOTED = 0
FAKE_PROMOTION = 0
