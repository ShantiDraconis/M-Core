import MCore.FinalProofRegistry
import MCore.FinalFail.DirectProducerCuts

namespace MCore.Habitants

inductive HabitantId where
  | rh | beal | ns | hodge | bsd | ym | pnp
  deriving DecidableEq, Repr

inductive HabitantStage where
  | openMath | habitant | endpoint | closedMath | green | frozen | certified
  deriving DecidableEq, Repr

structure Habitant where
  id : HabitantId
  target : String
  atoms : List String
  domain : String
  laws : List String
  operators : List String
  endpointMap : String
  stage : HabitantStage
  deriving Repr

def rh : Habitant := {
  id := .rh
  target := "FiniteSpanApproximatesChi concreteGeneratorFamily"
  atoms := ["FiniteSpanApproximatesChi concreteGeneratorFamily"]
  domain := "concrete Nyman-Beurling generator family / DN residual semantics"
  laws := ["finiteSpanApproximatesChi_iff_DNLimit_eq_zero", "certified DNToZero transport"]
  operators := ["approximate", "bound", "limit", "transport"]
  endpointMap := "FiniteSpanApproximatesChi -> DNLimit=0 -> RH endpoint bridge"
  stage := .habitant }

def beal : Habitant := {
  id := .beal
  target := "GCDLowerBoundProducer"
  atoms := ["GCDLowerBoundProducer"]
  domain := "positive BealData"
  laws := ["bealConjecture_iff_gcdLowerBoundProducer", "commonDivisor/commonPrime projections"]
  operators := ["gcd", "project", "transport"]
  endpointMap := "GCDLowerBoundProducer -> BealConjecture"
  stage := .habitant }

def ns : Habitant := {
  id := .ns
  target := "ActualNSToSignedGainCore"
  atoms := ["ActualNSToSignedGainCore"]
  domain := "ActualNS genuine flow-derived EnstrophyData"
  laws := ["theta < 1", "signed stretching bound", "signedGain downstream differential transport"]
  operators := ["decompose", "absorb", "deplete", "transport"]
  endpointMap := "ActualNSToSignedGainCore -> NS endpoint"
  stage := .habitant }

def hodge : Habitant := {
  id := .hodge
  target := "ConcreteAlgebraicityPayload"
  atoms := ["ConcreteAlgebraicityPayload"]
  domain := "smooth projective varieties / rational (p,p) classes"
  laws := ["trivial_qbar_r2_payload_iff_concrete_payload", "K26 minimal-cut transport"]
  operators := ["realize", "specialize", "span", "transport"]
  endpointMap := "ConcreteAlgebraicityPayload -> Hodge endpoint"
  stage := .habitant }

def bsd : Habitant := {
  id := .bsd
  target := "realizable elliptic-curve domain + rank equality + refined identity"
  atoms := ["BSDRealizableMaterialPayload"]
  domain := "genuine elliptic-curve arithmetic/analytic data"
  laws := ["same-domain binding", "rank equality", "refined leading coefficient identity", "Sha finiteness where required"]
  operators := ["bind", "rank", "normalize", "compare", "transport"]
  endpointMap := "BSD realizable material payload -> BSD endpoint"
  stage := .habitant }

def ym : Habitant := {
  id := .ym
  target := "Nonempty (B60ConcretePhysicalAdapter C F D H G O)"
  atoms := ["B60ConcretePhysicalAdapter"]
  domain := "regulated 4D construction bound to physical Hilbert/Hamiltonian/K30 data"
  laws := ["constructionFromA1", "infraredBlock", "limitBlock", "transferWitness", "non-vacuum excitation firewall"]
  operators := ["mapState", "reconstruct", "removeRegulator", "spectralTransfer"]
  endpointMap := "B60ConcretePhysicalAdapter -> mass-gap endpoint"
  stage := .habitant }

def pnp : Habitant := {
  id := .pnp
  target := "Nonempty P01MachineConstruction ∧ G21Pointwise"
  atoms := ["Nonempty P01MachineConstruction", "G21Pointwise"]
  domain := "canonical SAT bit-language and hardened polynomial machine models"
  laws := ["integrated parser+witness+verifier", "polynomial HaltsWithin", "AcceptsWithin iff SATBits", "G21Pointwise iff P02Target"]
  operators := ["parse", "guess", "verify", "simulate", "separate", "transport"]
  endpointMap := "P01MachineConstruction + G21Pointwise -> P != NP"
  stage := .habitant }

def globalHabitants : List Habitant := [rh, beal, ns, hodge, bsd, ym, pnp]

def atomCount : Nat :=
  globalHabitants.foldl (fun n h => n + h.atoms.length) 0

theorem globalHabitants_count : globalHabitants.length = 7 := by decide
theorem globalHabitants_atomCount : atomCount = 8 := by decide

theorem all_terminal_objects_are_habitants :
    ∀ h ∈ globalHabitants, h.stage = .habitant := by
  intro h hh
  simp [globalHabitants] at hh
  rcases hh with rfl | rfl | rfl | rfl | rfl | rfl | rfl
  all_goals rfl

end MCore.Habitants
