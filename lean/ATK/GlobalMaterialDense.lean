/-! ATK global kernel entrypoint. No terminal conjecture is asserted without proof. -/
namespace ATK.Global
inductive CertificationState where
  | buildPending
  | verified
  deriving DecidableEq, Repr

def state : CertificationState := .buildPending
theorem state_pending : state = .buildPending := rfl
end ATK.Global
