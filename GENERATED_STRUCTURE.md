# GENERATED STRUCTURE FROM THE SINGLE LAW

## Primitive objects

- `0/1`
- `1/1`

## Single law

```text
0/1 -> 1/1
```

No other primitive law is assumed.

## Canonically generated operations

### Identity

Every state has a zero-step path to itself:

```text
id(0/1) : 0/1 ->* 0/1
id(1/1) : 1/1 ->* 1/1
```

### Composition

If `a ->* b` and `b ->* c`, then the paths compose:

```text
(a ->* b) ; (b ->* c) = (a ->* c)
```

### Reachability

```text
0/1 ->* 0/1
0/1 ->* 1/1
1/1 ->* 1/1
```

There is no generated path `1/1 ->* 0/1`.

## Generated laws

- identity-left for path composition
- identity-right for path composition
- associativity of path composition
- reflexivity of reachability
- transitivity of reachability
- antisymmetry on these two states
- monotonicity along the single transition
- termination at `1/1`

## Generated order

The reachability relation induces the two-element order:

```text
0/1 <= 1/1
```

with reflexive cases:

```text
0/1 <= 0/1
1/1 <= 1/1
```

and not:

```text
1/1 <= 0/1
```

## Generated classes

```text
Initial  = {0/1}
Terminal = {1/1}
ReachableFromInitial = {0/1, 1/1}
FixedUnderReachability = {1/1}
```

## Generated behavior

```text
start      : 0/1
evolve     : 0/1 -> 1/1
terminate  : 1/1
normalForm : 1/1
```

Every nontrivial evolution from the initial state terminates after one primitive step.

## Arithmetic and algebra boundary

From the single transition alone, the generated algebra is the algebra of paths/reachability.

The following are NOT generated without adding further definitions:

- addition
- multiplication
- subtraction
- division
- successor
- natural numbers
- integers
- rationals
- reals
- semiring
- ring
- field

If any of those are introduced later, they must be marked as definitions/constructions and then their laws must be proved from those definitions; they are not primitive consequences of `0/1 -> 1/1`.

## Protocol state

```text
OPEN_MATH: CLOSED
PRIMITIVE_LAWS: 1
EXTRA_AXIOMS: 0
BYPASS: NONE
```
