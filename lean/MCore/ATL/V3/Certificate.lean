import MCore.ATL.V3.Promotion
import MCore.ATL.V3.Mining

namespace MCore.ATL.V3

inductive CertificateKind where
  | theorem | mined | infrastructure
  deriving DecidableEq, Repr

inductive CertificateStatus where
  | conditional | proved | open | invalid
  deriving DecidableEq, Repr

structure ExternalCertificate where
  id : String
  kind : CertificateKind
  statementNode : String
  statementHash : String
  termHash : Option String
  axiomsUsed : List String
  conditionalOn : List String
  promotion : PromotionEvidence
  mined : Option MinedEvidence
  deriving Repr

def ExternalCertificate.status (c : ExternalCertificate) : CertificateStatus :=
  if c.statementHash.isEmpty then .invalid
  else if !mayReach c.promotion .scientific then .open
  else match c.kind with
    | .mined =>
        match c.mined with
        | some m => if m.emittable then .conditional else .invalid
        | none => .invalid
    | .theorem =>
        if c.termHash.isSome then
          if c.conditionalOn.isEmpty then .proved else .conditional
        else .open
    | .infrastructure => .conditional

theorem theorem_without_term_not_proved (c : ExternalCertificate)
    (hk : c.kind = .theorem) (ht : c.termHash = none) :
    c.status ≠ .proved := by
  simp [ExternalCertificate.status, hk, ht]
  split <;> simp
  split <;> simp

end MCore.ATL.V3
