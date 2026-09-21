import MCore.ResolutionPredicate

namespace MCore.SigmaClass

structure Sigma where
  idx : String
  kerC : String
  fib : String
  fixCR : String
  deriving Repr

def table : List Sigma := [
  ⟨"BEAL", "primitivity loss", "primitive fiber", "CR=m"⟩,
  ⟨"NS", "same energy/different transfer", "k-shell", "0"⟩,
  ⟨"YM", "same correlator/different gap", "corr fiber", "Delta>0"⟩
]

def derive3to9 : String :=
  "Classification is downstream of proved Sigma distinctions; no digit is preassigned."

end MCore.SigmaClass
