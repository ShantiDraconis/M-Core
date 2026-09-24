import MCore.Real.SevenRealProducer

namespace MCore.Real.SevenCertificateBridge

/-- The external chain is type-identical to a genuine producer.
    These aliases do not manufacture an inhabitant. -/
abbrev EXTERNAL_GAP (C : CertificateClaims) : Type :=
  RealProducer C

abbrev EXTERNAL_CERTIFICATE (C : CertificateClaims) : Type :=
  EXTERNAL_GAP C

abbrev FINAL_ROOT (C : CertificateClaims) : Type :=
  EXTERNAL_CERTIFICATE C

abbrev FINAL_PROOF (C : CertificateClaims) : Type :=
  FINAL_ROOT C

def issueExternalCertificate
    {C : CertificateClaims}
    (p : RealProducer C) :
    EXTERNAL_CERTIFICATE C :=
  p

def toFinalRoot
    {C : CertificateClaims}
    (c : EXTERNAL_CERTIFICATE C) :
    FINAL_ROOT C :=
  c

def toFinalProof
    {C : CertificateClaims}
    (r : FINAL_ROOT C) :
    FINAL_PROOF C :=
  r

end MCore.Real.SevenCertificateBridge
