# Cross-prover terminal closure

This directory defines one semantic contract in Lean, Coq and Isabelle.

## Shared closure rule

The common mathematical pipeline is:

```
fixed terminal type
      ^
      |
ExactMaterializer
      ^
      |
zero-defect material state
      ^
      |
certified strict reduction
```

A structural reduction, a zero defect, a wrapper, or an equivalent
reformulation is not a terminal proof by itself.

## Language roles

**Lean** is the canonical implementation in this repository.  It contains the
seven-lane dependent family and the named projections back to RH, P-vs-NP,
Yang-Mills, Navier-Stokes, BSD, Hodge and Beal.

**Coq** mirrors the foundational closure algebra:
- open/closed composition;
- strict defect reduction;
- fixed terminal specification;
- exact materializer;
- zero-defect firewall;
- torsion/nonprogress law.

**Isabelle/HOL** mirrors the same gate algebra and operator laws through
locales.  Because HOL is not dependently typed in the same way as Lean/Coq,
the terminal extractor is represented as a locale parameter tied to the same
reduction locale instead of being encoded by dependent record projection.

## What connects the languages

There is no automatic proof-object conversion and no transitive trust between
kernels.

The connection is a theorem crosswalk in
`formal/CROSS_PROVER_CLOSURE_MANIFEST.json`.

For every cross-prover theorem key:
1. the proposition must have the same mathematical meaning;
2. each prover must verify its own implementation independently;
3. no language may add an axiom that supplies an OPEN_MATH inhabitant;
4. lane-specific terminals must preserve domain, quantifiers, constants,
   scaling, semantics and provenance.

## Seven-lane rule

Global closure is accepted only after the exact lane terminal is inhabited in
all seven lanes.

Thus:

```
GLOBAL_CLOSED
  iff
RH_CLOSED
and PNP_CLOSED
and BEAL_CLOSED
and NS_CLOSED
and HODGE_CLOSED
and BSD_CLOSED
and YM_CLOSED
```

The current repository does not yet contain those seven mathematical
inhabitants.  The cross-prover layer specifies and verifies the closure
machinery; it does not assert solutions to the open problems.

## Validation state

The newly added Lean, Coq and Isabelle files are BUILD_PENDING until their
respective kernels/toolchains have compiled them.
