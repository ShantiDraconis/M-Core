import MCore.Real.BridgeSeven

namespace MCore.Real.SevenCertificateBridge

/-- Minimal state space for a fail-closed producer. -/
inductive ResolutionState where
  | indeterminate
  | resolved (r : ℝ)

/-- A step to a real endpoint is available only from actual SevenGreenEvidence. -/
inductive ResolutionStep (C : CertificateClaims) :
    ResolutionState → ResolutionState → Prop where
  | resolve {r : ℝ} (e : E C r) :
      ResolutionStep C .indeterminate (.resolved r)

abbrev ResolutionPath (C : CertificateClaims) :=
  Relation.ReflTransGen (ResolutionStep C)

/-- No default inhabitant exists: both the seven-way evidence and its path are required. -/
structure RealProducer (C : CertificateClaims) where
  endpoint : ℝ
  evidence : E C endpoint
  path : ResolutionPath C .indeterminate (.resolved endpoint)

end MCore.Real.SevenCertificateBridge
