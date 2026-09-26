namespace MCore.ProofEngine
inductive ReuseStage | exactHash | alphaEquiv | normalFormEquiv | boundedUnfold | registeredEquiv | strongerLocal | composition | crossArea deriving DecidableEq, Repr
def defaultUnfoldBound : Nat := 5
structure ReusePolicy where unfoldBound : Nat := defaultUnfoldBound; strongerOnlyInsideRepo : Bool := true deriving Repr
end MCore.ProofEngine
