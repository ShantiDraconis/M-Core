# MASTER CLAIM INVENTORY

Canonical inventory branch: `atk/master-claim-inventory-20261005`.

## Purpose

This layer inventories, deduplicates, reuses and schedules existing formal work.
It MUST NOT turn metadata, reductions, equivalences, fail-closed wrappers, numerical evidence,
or certificates into a mathematical inhabitant.

## Canonical states

- `CERTIFIED`: audited terminal artifact; reuse only.
- `FROZEN`: immutable GREEN source; reuse only.
- `GREEN`: kernel/build gate passed; next action is freeze.
- `BUILD_PENDING`: source exists; kernel validation remains.
- `SOURCE_READY`: statement/source recovered; formalization remains.
- `OPEN_MATH`: the exact material producer is absent.
- `FALSIFIED`: this formulation is dead and must not be reopened.
- `SUPERSEDED`: replaced by a stronger/canonical statement.
- `DUPLICATE`: points to a canonical claim.

## Forward-only rule

`OPEN_MATH -> SOURCE_READY -> BUILD_PENDING -> GREEN -> FROZEN -> CERTIFIED`.

No earlier stage is reopened merely to create activity.
A reduction/equivalence may be reused but cannot replace the producer.

## Terminal material slots

1. RH: concrete vanishing/density producer.
2. P vs NP: genuine asymptotic SAT lower-bound / CanonicalNotInPWitness.
3. Navier-Stokes: strict NSE budget / BulkTailProducer.
4. BSD rank: GenuineP1Material.
5. BSD refined: GenuineP2Material.
6. Hodge: ConcreteAlgebraicityPayload.
7. Yang-Mills: physical 4D uniform positive-gap producer surviving the limit.
8. Beal: universal primitive gcd-one exclusion / TripleGCD lower bound.

Poincare is a control lane, not counted as an open material slot here.

## Producer-first rule

For every open terminal:

`TYPE -> MINIMAL_INHABITANT -> EXACT_PRODUCER -> TERMINAL_CLAIM`.

Forbidden substitutes include a renamed hypothesis, equivalent wrapper, extra unconstrained
parameter, administrative certificate, numerical fit, or fail-closed branch.

## Historical queue

The I/Phi/J tristable object, Horizon Prime, Pi Border, Delta/Gap, local-global and
Non-Unification are kept outside the Millennium terminal count until their literal statements
are canonicalized and classified.

## Directory contract

- `Canonical/`: state machine and claim metadata only.
- `Reuse/`: generic proved transports only.
- `Problems/`: problem identifiers and reusable validated mathematics.
- `OpenMath/`: exact uninhabited material frontiers.
- `Audit/`: inventory, dependency DAG, work queue and no-axiom certificate.
