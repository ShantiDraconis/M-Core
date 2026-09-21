# Triadic compression/retraction interpretation

Formal source: lean/MCore/FinalFail/TriadicObstructionCalculus.lean

The core distinguishes three closed sites: start, middle and finish.

Compression sends start -> middle, middle -> middle, finish -> middle. The middle
is therefore the meeting point and an idempotent fixed point.

Retraction is directional: middle -> start or middle -> finish. Thus the middle
is the meeting point of inward compression and branch point of outward
retraction.

RigidNucleus and ObstructionPresentation refine an open bridge into a concrete
obstruction object whose closure is equivalent to an endpoint, when that
equivalence is actually supplied.

Complexification explicitly separates realPart and imagPart and requires a
faithfulness law for zero.

Digits 0..9 are only an interpretation layer. A named open problem cannot be
assigned to a digit as a theorem without an invariant-preserving correspondence.

There are seven digits 3..9. They can cardinally index the seven Clay problems.
Adding Beal makes eight objects, so Beal must either be the rigid nucleus rather
than another digit, or the encoding must be enlarged. No arbitrary assignment
is promoted by the formal core.
