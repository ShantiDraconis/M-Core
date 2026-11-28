import Std

namespace O7.FinitePointCount

/-- Affine solutions of y² + x = x³ modulo p, plus the point at infinity.
The callers below use odd primes of good reduction for y² = x³ - x. -/
def pointCount (p : Nat) : Nat :=
  1 + ((List.range p).map fun x =>
    ((List.range p).filter fun y => (y*y + x) % p == x^3 % p).length).sum

def traceAt (p : Nat) : Int :=
  (p : Int) + 1 - (pointCount p : Int)

def sampledPrimes : List Nat := [3, 5, 7, 11, 13, 17, 19]

theorem sampled_counts :
    sampledPrimes.map pointCount = [4, 8, 8, 12, 8, 16, 20] := by decide

theorem sampled_traces :
    sampledPrimes.map traceAt = [0, -2, 0, 0, 6, 2, 0] := by decide

#print axioms sampled_counts
#print axioms sampled_traces

end O7.FinitePointCount
