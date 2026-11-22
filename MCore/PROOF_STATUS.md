# M-Core audit formalization — 2026-11-22

This ledger separates proved Lean implications from scientific obligations.

| Result | Status | Scope |
| --- | --- | --- |
| A1_Amplitude_NoGap | FORMALIZED; CI PENDING | No fixed gap on a homogeneous positive amplitude ray |
| A2_SelfRef_Cycle_Rejected | FORMALIZED; CI PENDING | A specific cyclic graph fails the declared audit gate; no impossibility of fixed points claimed |
| G1Fix_ConditionalEnergyBound | CONDITIONAL; CI PENDING | Algebraic inequality assuming energy and coefficient bounds; PDE adapter remains OPEN |
| A3_Zero_NotTotal | FORMALIZED; CI PENDING | Two distinct specified limits preclude one common extension value; concrete paths remain OPEN |
| Surgery_Adequacy_Beal | OPEN | No independent semantic bridge certified |
| OmegaI_SevenInterpretations | OPEN | No seven problem-specific bridges certified |
| Millennium_Bridge | OPEN | Analogy does not establish the original problems |

The repository's `lakefile.lean` uses `srcDir := "lean"`; root
`MCore/*.lean` files are compiled separately by the existing K15 audit
step in `.github/workflows/ci.yml`. Verify the run on this PR before
changing any CI-PENDING status to CI-PASS.

Neither compilation nor a proof of a conditional implication by itself
certifies the assumptions or a Millennium Prize Problem.
