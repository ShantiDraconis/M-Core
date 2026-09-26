import MCore.ProofEngine.CanonicalGraph

namespace MCore.ProofEngine

structure CostSample where
  nodeKind : String
  cycles : Nat
  failedAttempts : Nat
  downstreamUnlocked : Nat
  deriving Repr, DecidableEq

structure CostEstimate where
  estimatedCycles : Nat
  failurePermille : Nat
  downstreamUnlock : Nat
  deriving Repr, DecidableEq

def cutValue (e : CostEstimate) : Nat :=
  (e.estimatedCycles * (1000 + e.failurePermille)) / (e.downstreamUnlock + 1)

def estimateFromHistory (history : List CostSample) (kind : String) :
    Option CostEstimate :=
  let xs := history.filter (fun s => s.nodeKind == kind)
  if xs.isEmpty then
    none
  else
    let count := xs.length
    let cycles := xs.foldl (fun a s => a + s.cycles) 0
    let fails := xs.foldl (fun a s => a + s.failedAttempts) 0
    let unlock := xs.foldl (fun a s => a + s.downstreamUnlocked) 0
    some {
      estimatedCycles := cycles / count
      failurePermille := (1000 * fails) / count
      downstreamUnlock := unlock / count
    }

def activeCutCandidates (g : CanonicalGraph) : List CanonicalNode :=
  g.nodes.filter CanonicalNode.attackable

end MCore.ProofEngine
