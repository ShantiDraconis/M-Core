# ATK — Verified textual terminal dependency chain (2026-10-08)

State: SOURCE / EXACT SOURCE TYPES READ / KERNEL NOT RUN.

## Immutable source blobs inspected
- `imports/pnp/c102d9d4/lean/MCore/Real/FinalExternalCertificate.lean` blob `12c9dbd5fd2fca8e2c1634d6cc5cec87fdefe1a3`
- `imports/pnp/c102d9d4/lean/MCore/Real/P02G21G22Attack.lean` blob `ffd00b23cbbf4cb09f1f8c2ded111c32dbf62571`
- `imports/pnp/b406b806/lean/MCore/Real/FinalExternalTwoGap.lean` blob `e69542b077ccd7b375c47fbc14a72fd03e9bf2ac`
- `imports/pnp/recovery/7abed945/audit/EndpointCompression.lean` blob `41f18931c0d4f106067fc61200713903933164a7`

## Actual types and logical graph
```text
P01MachineConstruction
    -> P01ConstructionGap := Nonempty P01MachineConstruction
G21Pointwise := forall candidate : PolyDTMCandidate,
  exists x : BitString, not (candidate.CorrectAt SATTarget x)
    <-> P02Target <-> G22Contradiction <-> not (InP SATTarget)
P01ConstructionGap AND G21Pointwise
    = FinalExternalTwoGap
    -> FinalExternalGap := Nonempty FinalExternalInputs
    -> exists S : OfficialModelSelection,
         OfficialPneqNP S.model.P S.model.NP
```

The final theorem is explicitly conditional on `FinalExternalTwoGap`; the final certificate is explicitly conditional on `FinalExternalInputs`. None of the inspected source files supplies an unconditional inhabitant of `P01ConstructionGap` or `G21Pointwise`.

## Historical branch comparison
`BackwardCompression.fixed_witness_implies_final` takes `OfficialModelMatch` and `FixedWitness`; it is a different classical interface from the canonical SAT-target `PolyDTMCandidate`. The cross-interface bridge must be proved, not inferred from the theorem names.

## Next exact verification
- [ ] Pin imports and Lean/mathlib versions, run `lake build`.
- [ ] Audit `#print axioms` output and inspect concrete inhabitants, not merely structure declarations.
- [ ] Search frozen/cert/atk branches for compatible unconditional lemmas, preserving immutable refs.
- [ ] Add compatible imports into a new aggregate Lake module only after type equality is established.
