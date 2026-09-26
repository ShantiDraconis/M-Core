import MCore.ProofEngine.Pattern

namespace MCore.ProofEngine

/-- Only source-authored facts belong in the canonical node payload. -/
structure NodePrimitive where
  id : String
  area : String
  kind : String
  formalStatement : String
  semanticStatement : String
  sourceFiles : List String
  theoremNames : List String
  repo : String
  branch : String
  commit : String
  version : Nat
  supersededBy : Option String := none
  deriving Repr, DecidableEq

/-- Append-only evidence.  Mutable derived states are deliberately absent. -/
structure EvidenceEvent where
  sequence : Nat
  eventKind : String
  artifact : String
  digest : String
  detail : String
  deriving Repr, DecidableEq

inductive OpenMathClass where
  | attackable
  | research
  | external
  deriving Repr, DecidableEq

structure OpenMathEvent where
  sequence : Nat
  classification : OpenMathClass
  reason : String
  deriving Repr, DecidableEq

structure ProvenanceEvent where
  sequence : Nat
  source : String
  sourceRef : String
  digest : String
  deriving Repr, DecidableEq

/-- Persisted canonical node. Dependencies, consumers, replacement paths,
build/kernel/semantic/certificate states are views computed from the graph. -/
structure CanonicalNode where
  primitive : NodePrimitive
  evidence : List EvidenceEvent := []
  openMath : List OpenMathEvent := []
  provenance : List ProvenanceEvent := []
  deriving Repr, DecidableEq

/-- Replacement routes are graph edges, never free-form strings. -/
structure RouteEdge where
  fromId : String
  toId : String
  adapterId : Option String := none
  deriving Repr, DecidableEq

structure CanonicalGraph where
  nodes : List CanonicalNode
  dependencyEdges : List RouteEdge
  replacementEdges : List RouteEdge
  deriving Repr, DecidableEq

def CanonicalGraph.nodeIds (g : CanonicalGraph) : List String :=
  g.nodes.map (fun n => n.primitive.id)

def CanonicalGraph.dependencies (g : CanonicalGraph) (id : String) : List String :=
  (g.dependencyEdges.filter (fun e => e.toId == id)).map (fun e => e.fromId)

def CanonicalGraph.consumers (g : CanonicalGraph) (id : String) : List String :=
  (g.dependencyEdges.filter (fun e => e.fromId == id)).map (fun e => e.toId)

def CanonicalGraph.replacementSuccessors (g : CanonicalGraph) (id : String) : List String :=
  (g.replacementEdges.filter (fun e => e.fromId == id)).map (fun e => e.toId)

/-- Fail-closed edge validity: every endpoint and adapter must be a real node. -/
def CanonicalGraph.edgeValid (g : CanonicalGraph) (e : RouteEdge) : Bool :=
  let ids := g.nodeIds
  ids.contains e.fromId &&
  ids.contains e.toId &&
  match e.adapterId with
  | none => true
  | some a => ids.contains a

def CanonicalGraph.routesValid (g : CanonicalGraph) : Bool :=
  g.dependencyEdges.all g.edgeValid && g.replacementEdges.all g.edgeValid

/-- OPEN_MATH is a classification view, not a promotion state. -/
def CanonicalNode.currentOpenMathClass (n : CanonicalNode) : Option OpenMathClass :=
  (n.openMath.reverse.head?).map (fun e => e.classification)

def CanonicalNode.attackable (n : CanonicalNode) : Bool :=
  n.currentOpenMathClass == some .attackable

end MCore.ProofEngine
