import MCore.FinalFail.UniversalTerminalClosure

namespace MCore.FinalProof

inductive ProblemSlot where
  | riemann | beal | navierStokes | hodge | pVsNP | bsd | yangMills
  deriving DecidableEq, Repr

inductive SlotState where
  | linkedReuse
  | openMath
  | proved
  deriving DecidableEq, Repr

structure SlotRecord where
  slot : ProblemSlot
  sourceRepo : String
  sourceRef : String
  terminal : String
  state : SlotState
  deriving Repr

/-!
The registry records the current material terminal producer in each lane.
A GREEN/FROZEN reduction or transport certificate never changes a slot to
`proved`; only an inhabitant of the named terminal target may do that.
-/
def registry : List SlotRecord := [
  { slot := .riemann
    sourceRepo := "ShantiDraconis/m-core-riemann"
    sourceRef := "atk/rh-gram-final-closure-20261001"
    terminal := "LogMajorantCertificate: ∃ K≥0, ∀ N, DN(N) ≤ K/log(N+2)"
    state := .openMath },
  { slot := .beal
    sourceRepo := "ShantiDraconis/m-core-beal"
    sourceRef := "d6fe130c44ef91e0f8ceb6b15a6548f186e381fd"
    terminal := "GCDLowerBoundProducer = ∀ d : BealData, 1 < Nat.gcd d.a (Nat.gcd d.b d.c)"
    state := .openMath },
  { slot := .navierStokes
    sourceRepo := "ShantiDraconis/navier-stokes-critical-barrier-audit"
    sourceRef := "attack/ns003-strict-signed-producer-v1"
    terminal := "ActualNS-derived StretchSplit + BulkAbsorption + ExceptionalTailControl + SubcriticalBudget"
    state := .openMath },
  { slot := .hodge
    sourceRepo := "ShantiDraconis/m-core-hodge"
    sourceRef := "f1f0f848d97c32221c2d929451b0f05b907a1ee0"
    terminal := "Nonempty (ConcreteHodgeMaterialTarget G M): nonempty geometry + CycleSpanAdapter + ConcreteAlgebraicityPayload"
    state := .openMath },
  { slot := .pVsNP
    sourceRepo := "ShantiDraconis/m-core-p-vs-np"
    sourceRef := "frozen/p01-verifier-phase-mincut-green-720596c0 + atk/p02-consolidated-kernel-20261001"
    terminal := "UniversalSATLowerBound / UniversalFailure for canonical SAT (P01 already closed)"
    state := .openMath },
  { slot := .bsd
    sourceRepo := "ShantiDraconis/m-core-bsd"
    sourceRef := "atk/next-bsd-realizable-high-rank-producer-20260928"
    terminal := "genuine elliptic-curve realizability + analytic-rank≥2 residual + refined leading-coefficient identity"
    state := .openMath },
  { slot := .yangMills
    sourceRepo := "ShantiDraconis/m-core-yang-mills"
    sourceRef := "ea22910e5b737d1236fbde7ad129cc5d8c8c0b8a"
    terminal := "A1MaterialWitnessV3 + faithful transfer to the K14/K30 physical spectral layer"
    state := .openMath }
]

def provedCount : Nat :=
  registry.foldl (fun n r => if r.state = .proved then n + 1 else n) 0

def openMathCount : Nat :=
  registry.foldl (fun n r => if r.state = .openMath then n + 1 else n) 0

theorem registry_length_eq_seven : registry.length = 7 := by
  decide

theorem provedCount_eq_zero : provedCount = 0 := by
  decide

theorem openMathCount_eq_seven : openMathCount = 7 := by
  decide

end MCore.FinalProof
