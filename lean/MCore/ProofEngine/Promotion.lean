import MCore.ProofEngine.CanonicalGraph

namespace MCore.ProofEngine

/-- Promotion is monotone. OPEN_MATH is intentionally not present here. -/
inductive PromotionLayer where
  | source
  | build
  | kernel
  | semantic
  | scientific
  deriving Repr, DecidableEq

def PromotionLayer.rank : PromotionLayer → Nat
  | .source => 0
  | .build => 1
  | .kernel => 2
  | .semantic => 3
  | .scientific => 4

def PromotionLayer.next : PromotionLayer → Option PromotionLayer
  | .source => some .build
  | .build => some .kernel
  | .kernel => some .semantic
  | .semantic => some .scientific
  | .scientific => none

def CanPromote (from to : PromotionLayer) : Prop :=
  from.next = some to

theorem promotion_strict {a b : PromotionLayer} (h : CanPromote a b) :
    a.rank < b.rank := by
  cases a <;> cases b <;> simp_all [CanPromote, PromotionLayer.next, PromotionLayer.rank]

inductive FirewallKind where
  | axiom
  | circularity
  | semantic
  | interface
  | vacuous
  deriving Repr, DecidableEq

structure FirewallResult where
  kind : FirewallKind
  passed : Bool
  detail : String
  deriving Repr, DecidableEq

def allFirewallsPass (rs : List FirewallResult) : Bool :=
  rs.length == 5 && rs.all (fun r => r.passed)

/-- Semantic promotion is fail-closed: all five independent firewalls pass. -/
def SemanticPromotable (rs : List FirewallResult) : Prop :=
  allFirewallsPass rs = true

end MCore.ProofEngine
