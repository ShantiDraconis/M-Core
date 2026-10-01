# ATK Material Mathematics Master — 2026-10-01

## Scope firewall

This master distinguishes two layers:

1. **Internal material mathematics** — finite algebra/calculus/topology formally
   defined inside M-Core and eligible for Lean certification.
2. **External terminal mathematics** — the genuine mathematical producers for
   RH, Beal, P vs NP, Navier–Stokes, Hodge, BSD, and Yang–Mills.

Internal laws never manufacture an external terminal inhabitant.

## Canonical positive frontier

- `GlobalPositiveMaterialRoot`
- `global_positive_root_iff_components`
- positive Riemann orientation:
  `RiemannHypothesis`
- mixed negative-RH root is protected by:
  `positive_root_excludes_mixed_negative_root`

## Material algebra

Module:
`MCore.FinalFail.MaterialAlgebra`

Carrier:
`TriState = {seed, transit, manifest}`

Interpretation of the explicit finite table:
- seed = additive zero
- transit = multiplicative one
- manifest = the second nonzero element

Certified finite laws include:
- commutative/associative addition
- additive inverse
- commutative/associative multiplication
- distributivity
- nonzero inverse
- nonzero square = one
- cubic identity x^3 = x
- threefold additive transit = zero

Seven-lane carrier:
`SevenLaneVector = TriState^7`
with coordinates:
- Riemann
- Beal
- P vs NP
- Navier–Stokes
- Hodge
- BSD
- Yang–Mills

## Producer calculus

Module:
`MCore.FinalFail.MaterialProducerCalculus`

Typed objects:
- `MaterialProducer P`
- `MaterialRefuter P`

Operators:
- pure
- map
- tensor
- left/right projections
- iff transport
- refuter contramap
- producer/refuter incompatibility

Evidence states:
- refuted
- open
- proved

Evidence operations:
- dual
- conjunction
- disjunction
- code in {-1,0,1}
- first discrete derivative

Laws:
- involutive duality
- De Morgan laws
- associative/commutative/idempotent conjunction and disjunction
- derivative bounds

## Derived arithmetic and order topology

Module:
`MCore.FinalFail.MaterialDerived`

TriState:
- code arithmetic modulo three
- no zero divisors
- nonzero cancellation
- characteristic three
- inverse/self-inverse laws
- rotate = add one

SevenLaneVector:
- componentwise negation
- scalar multiplication
- distributivity
- scalar associativity
- unit/zero scalar laws

Evidence topology/order calculus:
- closure
- interior
- boundary
- monotonicity
- closure idempotence
- interior idempotence
- proved-neighborhood boundary theorem
- two-step derivative telescoping

## Geometry

Module:
`MCore.FinalFail.MaterialGeometry`

TriState:
- phase rotation rho
- rho^3 = identity
- algebraic delta
- support

SevenLaneVector:
- coordinatewise rotation
- support count
- Hamming distance
- hamming(x,x)=0
- symmetry
- bound <= 7
- zero distance iff equality
- rotation isometry

Evidence:
- second discrete derivative
- jump magnitude
- bounded second derivative

## Three-element field certificate

Module:
`MCore.FinalFail.MaterialField`

The explicit table is certified as a three-element finite field table:
- characteristic 3
- Frobenius x^3=x
- nonzero inverses
- field-table certificate

This is finite modular algebra. It is not an assertion that an indeterminate
classical expression such as 0/0 equals a TriState value.

## Asymmetric/directed calculus

Module:
`MCore.FinalFail.MaterialAsymmetry`

Status:
GREEN in run `36867699222`.

TriState operators:
- reflection = additive negation
- directed difference
- orientation coordinate

Laws:
- reflection involution
- directed-difference reversal
- translation invariance
- cocycle/chain law
- constant rotation increment
- D3/dihedral relation
- orientation reversal
- orientation chain additivity

SevenLaneVector:
- componentwise reflection
- componentwise directed difference
- D3 action
- rotation isometry
- reflection isometry

## Polynomial/affine dynamics

Module:
`MCore.FinalFail.MaterialPolynomial`

Current state:
REPAIR/VALIDATION IN PROGRESS.

Objects:
- three point Lagrange basis
- quadratic interpolant
- affine map x -> a*x+b
- Frobenius map

Target laws:
- every unary TriState endomorphism has a degree <=2 interpolation formula
- affine composition law
- nonzero affine slope is bijective
- translation by one equals rotation
- common nonzero affine coordinate change preserves seven-lane Hamming geometry

The implementation now uses structural additive and multiplicative
cancellation rather than brute-force simp enumeration.

## Synthesis laws

Module:
`MCore.FinalFail.MaterialSynthesis`

Status:
GREEN in run `36869911222`.

Laws:
- delta translation invariance
- delta rotation invariance
- nonzero state = +1 or -1
- global rotation = translation by the all-ones vector
- nonzero scalar action is injective on all seven lanes
- Hamming invariance under repeated rotation
- evidence duality negates first derivative
- evidence duality negates second derivative
- jump magnitude is duality invariant

## Arithmetic constants

Module:
`MCore.FinalFail.MaterialArithmetic`

Current state:
SOURCE / MASTER-VALIDATION PENDING.

Named constants:
- zero
- one
- two
- minusOne

Laws:
- two = -one
- 1+1=2
- 2+1=0
- 2*2=1
- natural embedding by repeated unit addition
- ofNat(n+3)=ofNat(n)
- characteristic three
- successor cycle

## Linear/topological seven-lane layer

Module:
`MCore.FinalFail.MaterialLinearTopology`

Current state:
SOURCE / MASTER-VALIDATION PENDING.

Canonical basis:
- eRiemann
- eBeal
- ePvsNP
- eNavierStokes
- eHodge
- eBSD
- eYangMills

Target laws:
- each basis vector has support one
- every LaneVector decomposes into its seven scalar coordinates
- support count equals Hamming distance to zero
- nonzero scalar multiplication preserves support
- nonzero scalar multiplication is a Hamming isometry

## Global assembly

Module:
`MCore.FinalFail.MaterialGlobalAssembly`

Objects:
`SevenMaterialProducers`

Laws:
- seven genuine semantic producers -> GlobalPositiveMaterialRoot
- positive root -> seven producer bundle
- roundtrip equivalence
- all seven producers force aggregate evidence state = proved

This is a composition theorem. It does not construct any of the seven external
material producers.

## External terminal frontier — unchanged by internal algebra

The actual open mathematical inhabitants remain:

- RIEMANN:
  `FiniteSpanApproximatesChi concreteGeneratorFamily`
  (equiv. certified DNLimit=0/DNToZero chain)
- BEAL:
  `GCDLowerBoundProducer`
- P VS NP:
  P01 source-produced separately; P02 exact open atom
  `G21Pointwise / SemanticDiagonalFamily / SAT not in P`
- NAVIER–STOKES:
  `ActualNSToSignedGainCore`
- HODGE:
  `ConcreteAlgebraicityPayload`
- BSD:
  genuine realizable elliptic-curve binding + rank equality + refined identity
- YANG–MILLS:
  `Nonempty (B60ConcretePhysicalAdapter ...)`

## Certification rule

A material module is promoted to GREEN only if:
- source hygiene finds no sorry/admit/new axiom/new constant escape;
- targeted `lake build` succeeds;
- key `#print axioms` results contain no `sorryAx`.

The prepared master workflow is:
`.github/workflows/material-master-strict-run-once.yml`.
It is intentionally not triggered while other targeted runs are active.
