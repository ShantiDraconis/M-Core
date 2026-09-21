# M-Core Formulation V2 — GREEN Certificate

source_sha: fcdaaab2093afa5e0c973057a00a610039d5ff0f
frozen_ref: frozen/mcore-formulation-v2-green-fcdaaab2
certificate_ref: cert/mcore-formulation-v2-fcdaaab2-run35668594575
workflow: M-Core formulation v2
run_id: 35668594575
run_number: 11
conclusion: SUCCESS

classification: FROZEN_FORMULATION_SOURCE
promotion_scope: relational closed-center formulation only

verified:
- fail-closed source hygiene: PASS
- Lean build: PASS
- axiom audit: PASS
- sorryAx in audited terminal theorems: ABSENT

audited_theorems:
- MCore.FinalFail.RelationalHardAtom.failAt_iff_fundamentalIndeterminacy
- MCore.FinalFail.RelationalHardAtom.determinedAt_iff_centerDetermined
- MCore.FinalFail.RelationalHardAtom.failAt_iff_IFail
- MCore.FinalFail.RelationalHardAtom.determinedAt_not_failAt
- MCore.FinalFail.RelationalTotality.toClosedCenterHard
- MCore.FinalFail.RelationalTotality.closedCenterHard_coexists_with_failAt
- MCore.FinalFail.RelationalFunctionalWitness.toClosedCenterHard

boundary:
- This certificate does not assert closure of any Millennium Prize Problem or Beal endpoint.
- Open mathematical producers remain open unless independently certified.
