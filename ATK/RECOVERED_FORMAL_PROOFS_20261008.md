# ATK — Recovered formal proof index (2026-10-08)

Status: SOURCE_INDEXED / EXACT_TYPE_CHECK_PENDING / KERNEL_NOT_RUN.

## Previously indexed material and structural files
- M-Core/final-proof/cross_repository_certificate_registry.json (conditional endpoint compression, ThreeTracks, FinalEndpoint, integrated candidate)
- M-Core/final-proof/structural_certificate_discovery_20261008.json (14 source candidates, default-branch only)
- M-Core/imports/pnp/recovery/7abed945/audit/EndpointCompression.lean — fixed_witness_implies_final, endpoint_compression, endpoint_from_c12_open_bridge; requires OfficialModelMatch and FixedK10WitnessExistence.
- M-Core/imports/pnp/recovery/7abed945/audit/ThreeTracks.lean — conditional equality/separation/approximation routes.
- M-Core/imports/pnp/c102d9d4/lean/MCore/Real/FinalExternalCertificate.lean — final_external_certificate requires FinalExternalInputs.
- M-Core/imports/pnp/30707e68/lean/MCore/Real/P02BoundedComputationClose.lean — certificates_close_boundedExecCorrectness requires TransitionSoundnessCertificate and TableauCompletenessCertificate.
- m-core-p-vs-np/lean/MCore/Real/P01FinalCertificate.lean — construction_closes_p01 requires Nonempty P01MachineConstruction.
- m-core-p-vs-np/lean/MCore/Material/P01Adapter.lean — conditional adapter.
- m-core-riemann/lean/MCore/Material/Closure.lean — ConcreteUniformLogDNBound := Nonempty (RHClosure DN), not yet inhabited.
- m-core-beal/lean/MCore/K8.lean — noCommonPrime_is_counterexample.
- m-core-hodge/lean/MCore/Frontier/CandidateBridge.lean — conditional geometric transport lemmas.
- axiomatic-millenium/AxiomaticMillenium/SevenLaneClosureKernel.lean — seven_lane_kernel_exact (structural counts).

## Branch recovery protocol
1. Paginate every branch list; scan cert/, frozen/, audit/, atk/, attack/ refs without modifying historical refs.
2. Record repo, ref, immutable commit SHA, path, blob SHA, declaration, elaborated theorem type, hypotheses, axioms and Lean/mathlib versions.
3. De-duplicate declarations by exact type and assumptions, never by theorem name alone.
4. Assemble compatible source snapshots as Lake packages; build each and then an aggregate root.
5. Keep terminal flags false until unconditional inhabitants and external gates are verified.

No claim that all branches were traversed or proofs globally compiled.
