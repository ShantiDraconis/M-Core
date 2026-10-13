# ATK ↔ LeanMillenniumPrizeProblems — integration map (2026-10-13)

Upstream: https://github.com/lean-dojo/LeanMillenniumPrizeProblems
Upstream README blob SHA: 8f3ea4863ca578380089065b49c0e35ec0dec856
ATK source: lean/MCore/FinalFail/DirectProducerCuts.lean
ATK source blob SHA: ad0e6ae8061b81745f49bc8757f815071466ced0

## Rule
This is a mapping, NOT a proof, a Lean import, or an upstream contribution.
Only an exact typed, sorry-free proof of the faithful official statement with audited axioms can count as terminal. No wrapper/assumption-based promotion.

| ATK lane | ATK direct material target | Upstream target / path | Status |
|---|---|---|---|
| RH | FiniteSpanApproximatesChi concreteGeneratorFamily | Problems/RiemannHypothesis/Millennium.lean; Millennium.ClayRiemannHypothesis | OPEN: bridge from finite span to exact upstream proposition unverified |
| P != NP | P01ConstructionGap and G21Pointwise | Problems/PVersusNP/Millennium.lean; Millennium.ClayPVersusNP.Formulations.NegativeBranch | OPEN: SAT encoding and machine-model equivalence unverified |
| NS | NSProducerFirst.ActualNSToSignedGainCore | Problems/NavierStokes/Millennium.lean; MillenniumNavierStokes.FeffermanA/B/C/D | OPEN: signed-gain argument to one faithful case unverified |
| YM | Nonempty (B60ConcretePhysicalAdapter C F D H G O) | Problems/YangMills/Millennium.lean | BLOCKED: upstream statement incomplete; not a valid terminal target |
| BSD | genuine elliptic curve domain + rank equality + leading coefficient | Problems/BirchSwinnertonDyer/Millennium.lean; MillenniumBirchSwinnertonDyer.ClayBirchSwinnertonDyer | OPEN: genuine arithmetic/analytic domain and target equivalence unverified |
| Hodge | ConcreteAlgebraicityPayload | Problems/Hodge/Millennium.lean | BLOCKED: upstream statement incomplete/vacuity risk |
| Beal | GCDLowerBoundProducer | No upstream file: Beal is not a Clay Millennium Prize Problem | LOCAL ONLY: universal proof open |

## Integration gates
1. Pin upstream commit and Lean/Mathlib toolchain.
2. Compare exact declaration types and quantifiers, not only names.
3. Check that all data structures are realizable, nonempty where needed, and cannot be made vacuous.
4. Construct explicit bridge lemmas in a separate namespace without axioms equivalent to the goal.
5. Run lake build and #print axioms for every bridge; verify sorry-free source closure.
6. Only after all gates pass, open an upstream PR for appropriate independently useful changes.

Current result: MAPPING_ONLY. No kernel run; no universal proof claimed.
