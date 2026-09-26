import MCore.ATL.V3.Core
import MCore.ATL.V3.Promotion
import MCore.ATL.V3.Mining
import MCore.ATL.V3.Certificate

namespace MCore.ATL.V3

/-- The control plane certifies exactly the evidence supplied to it.
    It cannot manufacture an unresolved endpoint term. -/
theorem fail_closed_without_term (c : ExternalCertificate)
    (hk : c.kind = .theorem) (ht : c.termHash = none) :
    c.status ≠ .proved :=
  theorem_without_term_not_proved c hk ht

end MCore.ATL.V3
