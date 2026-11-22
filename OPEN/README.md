# OPEN — mathematical bridges and research obligations

This directory is a navigation index, not a Lean module asserting conjectures.

## Primary research target: 3D incompressible Navier–Stokes

1. State the exact official PDE domain, admissible initial data and desired
   global smoothness/continuation conclusion.
2. Derive the enstrophy evolution inequality with vortex stretching treated
   rigorously, including all boundary conditions.
3. Derive the coefficient `a(t)` independently of the target quantity
   `Y(t) = ‖ω(t)‖²`, avoiding self-reference.
4. Prove the proposed `L¹` coefficient estimate analytically, including
   the constant, not merely as a hypothesis of an algebraic lemma.
5. Apply Grönwall and a valid continuation criterion to the actual PDE class.

**Unresolved key bridge:** standard energy dissipation does not alone provide
the desired universal integrable bound for vortex stretching. Assuming it
would assume the central difficulty away.

## Outside the focused manuscript

- Beal surgery adequacy — OPEN
- Omega_I / seven interpretations — OPEN
- Universal Millennium bridge — OPEN
- Riemann, Yang–Mills, Hodge, BSD, P vs NP — not part of this focused release

See [open specification](../MCore/OpenProblems.lean) and
[freeze](../FREEZE_v1.md).

These labels do not erase or change earlier research, and do not assert that
no proofs exist elsewhere. Any candidate evidence must be inspected and
independently verified before changing status.
