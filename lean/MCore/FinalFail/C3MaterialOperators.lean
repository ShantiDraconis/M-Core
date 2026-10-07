import MCore.FinalFail.TopologyOperatorCore
namespace MCore.FinalFail
structure SectorOperator (X : Type) where
  op : X → X
  rotation : X → X
  commutes : ∀ x, rotation (op x) = op (rotation x)

structure SevenOperatorFamily (X : Type) where
  T S E Q delta gamma C : SectorOperator X

def MaterialC3Family (X : Type) : Prop := Nonempty (SevenOperatorFamily X)
end MCore.FinalFail
