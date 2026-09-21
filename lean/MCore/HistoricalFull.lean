namespace MCore.HistoricalFull

inductive DeclClass
  | THEOREM | DEFINITION | AXIOM | HYPOTHESIS | NUMERICAL | DOCUMENTATION
  deriving DecidableEq, Repr

def promotionEligible : DeclClass → Bool
  | .THEOREM => true
  | _ => false

end MCore.HistoricalFull
