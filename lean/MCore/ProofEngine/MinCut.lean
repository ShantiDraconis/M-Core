import MCore.ProofEngine.CanonicalNode
namespace MCore.ProofEngine
structure CostSample where nodeId : String; cycles : Nat; failed : Bool deriving Repr
structure CostEstimate where cycles : Nat; failurePermille : Nat deriving Repr
def cutValue (cost : CostEstimate) (downstreamUnlock : Nat) : Option Nat :=
  if downstreamUnlock = 0 then none else some ((cost.cycles * (1000 + cost.failurePermille)) / downstreamUnlock)
def routable (log : NodeLog) (downstreamUnlock : Nat) : Bool :=
  eligibleForAttackCut log && downstreamUnlock > 0
end MCore.ProofEngine
