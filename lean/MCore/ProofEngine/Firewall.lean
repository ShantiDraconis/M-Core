namespace MCore.ProofEngine
inductive FirewallKind | axiom | circularity | semanticStatement | interface | vacuity deriving DecidableEq, Repr
structure FirewallResult where kind : FirewallKind; passed : Bool; detail : String deriving Repr
def allFirewallsPass (rs : List FirewallResult) : Bool := rs.all (fun r => r.passed)
end MCore.ProofEngine
