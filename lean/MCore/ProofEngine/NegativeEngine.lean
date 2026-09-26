import MCore.ProofEngine.Registry

namespace MCore.ProofEngine

/-- Classification used by the negative-search engine. -/
inductive NegativePattern
  | formulation
  | transfer
  | identification
  | realization
  deriving DecidableEq, Repr

/-- A negative producer carries the contradiction-producing map itself.
Similarity scores or metadata are insufficient to inhabit this structure. -/
structure NegativeProducer (A A' : Prop) where
  pattern : NegativePattern
  reject : A → ¬ A'
  sourceRepo : String
  sourceRef : String
  theoremName : String

def NegativeProducer.contradiction {A A' : Prop}
    (p : NegativeProducer A A') (hA : A) (hA' : A') : False :=
  p.reject hA hA'

/-- A candidate transfer is intentionally fail-closed.  It becomes executable
only after the target supplies an exact implication into the source premise
and an exact implication from the source rejected proposition. -/
structure NegativeInstantiation
    {A A' T T' : Prop} (p : NegativeProducer A A') where
  targetToSource : T → A
  sourceRejectedFromTarget : T' → A'

def NegativeInstantiation.rejectTarget
    {A A' T T' : Prop} {p : NegativeProducer A A'}
    (i : NegativeInstantiation p) : T → ¬ T' :=
  fun hT hT' => p.reject (i.targetToSource hT) (i.sourceRejectedFromTarget hT')

/-- Provenance record for the certified P-vs-NP G2.1 literal fixed-point
countermodel.  This record deliberately does not recreate the theorem in
M-Core: the proof remains owned by m-core-p-vs-np. -/
def G21LiteralFixedPointProvenance : String × String × String :=
  ("ShantiDraconis/m-core-p-vs-np",
   "cert/p02-literal-fixed-point-countermodel-9d6dd957-run35721311898",
   "MCore.Real.P02LiteralFixedPointCountermodel.no_universal_literal_fixed_point")

end MCore.ProofEngine
