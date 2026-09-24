import MCore.Real.RealProducer

namespace MCore.Real

/-- Fail-closed aliases: no certificate exists unless a RealProducer exists. -/
abbrev EXTERNAL_GAP (E : ResolutionEvidence) : Type :=
  RealProducer E

abbrev EXTERNAL_CERTIFICATE (E : ResolutionEvidence) : Type :=
  EXTERNAL_GAP E

abbrev FINAL_ROOT (E : ResolutionEvidence) : Type :=
  EXTERNAL_CERTIFICATE E

abbrev FINAL_PROOF (E : ResolutionEvidence) : Type :=
  FINAL_ROOT E

/-- Promotion is identity on a genuine producer; it creates no new inhabitant. -/
def issueExternalCertificate
    {E : ResolutionEvidence}
    (P : RealProducer E) :
    EXTERNAL_CERTIFICATE E :=
  P

def toFinalRoot
    {E : ResolutionEvidence}
    (C : EXTERNAL_CERTIFICATE E) :
    FINAL_ROOT E :=
  C

def toFinalProof
    {E : ResolutionEvidence}
    (R : FINAL_ROOT E) :
    FINAL_PROOF E :=
  R

end MCore.Real
