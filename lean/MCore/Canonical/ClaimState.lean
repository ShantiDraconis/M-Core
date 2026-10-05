namespace MCore.Canonical

inductive ClaimKind
  | definition
  | theorem
  | conjecture
  | numericalObservation
  | interpretation
  | interface
  deriving Repr, DecidableEq

inductive ClaimState
  | certified
  | frozen
  | green
  | buildPending
  | sourceReady
  | openMath
  | falsified
  | superseded
  | duplicate
  deriving Repr, DecidableEq

def ClaimState.isClosed : ClaimState → Bool
  | .certified => true
  | .frozen => true
  | .green => true
  | _ => false

def ClaimState.needsMaterialProducer : ClaimState → Bool
  | .openMath => true
  | _ => false

end MCore.Canonical
