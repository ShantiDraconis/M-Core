# ERRATA

| Data | Documento afetado | Erro | Correção |
|---|---|---|---|
| 2026-10-09 | `certs/final_global/v1`, `certs/final_external/v2`, `MASTER_INDEX.md` (versão de 2026-10-08) | P01 (`P01ConstructionGap`, SAT ∈ NP) declarado aberto: "nenhum `P01VerifierPhase` concreto em 686 branches" | P01 está **fechado** por `P01RawTotalizationProducer.p01ConstructionGap_closed` @`0dd09383`, verificado de novo (run `37913791428`). O scanner não reconhecia tipos qualificados por namespace nem tipos na linha seguinte. Ver `certs/final_global/v2/ERRATUM_v1.md`. |
| 2026-10-09 | `PUBLICATION/DUAL_ENDPOINT_STATE_STRUCTURAL_CERTIFICATE.md` (`465cc65`) | Certifica uma estrutura cuja base Lean não compilava naquele commit | A base compila a partir de `8b7099e` (PR #15). O documento foi preservado sem alterações. |
| 2026-10-08 | `lean/MCore/FinalProofRegistry.lean` | Os pins pVsNP `a3386d52` e BSD `c1e7b245` não continham os terminais nomeados | Corrigidos em `ecb5f51` para `b406b806` e `a3edf620`. |
