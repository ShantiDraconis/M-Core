# Certificação mínima — Riemann scoped final

R0 6 GREEN: 93982ae, 6905ef3, be25ead, 67c9055, c0fe29a, 66a9b18

NB 7 GREEN: 40b45b6, 49c511f, 5ed1df6, 7c2d8d3, b2ef9ba, 9d6c36d, e7e36d6

AGREG 3 GREEN: 38aad03, d6a291b4, 5c66f8dc

R2 2 GREEN: 43d7c060, dual-frontier

FINAL:
- FinalProof.lean: intentionally empty
- FinalClaim.lean: VanishingUpperBound -> DNLimit = 0

EXTERNAL:
- 27ac66f4: fail-closed witness, not imported
- A14: 3 countermodel-closed non-implication theorems

Expected scoped result after kernel build:
- 0 x RiemannHypothesis
- 1 x FINAL_SCOPED_CLAIM
- 3 x A14 refuted-route theorems
- 1 x fail-closed witness
