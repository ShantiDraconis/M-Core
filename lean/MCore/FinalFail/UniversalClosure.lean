import MCore.FinalFail.MaterialOnlyFinalRoot

namespace MCore.FinalFail.Universal

open MCore.FinalFail
open MCore.FinalFail.Semantic

/-!
# Universal closure kernel

This file formalizes composition only. It does not inhabit any open producer.

SevenInhabitants Core is deliberately field-wise: a proof of the bundle must
supply one proof for each of the seven material cores. No aggregate Boolean,
count, wrapper, or accepted hypothesis can manufacture a field.

UniversalKernel contains only already-proved consumer maps Core -> Endpoint.
If a lane is claimed to be an exact reduction, ExactUniversalKernel.reflect
must also reconstruct Core from Endpoint.
-/

structure SevenInhabitants (Core : ProblemId → Prop) : Prop where
  beal : Core .beal
  navierStokes : Core .navierStokes
  hodge : Core .hodge
  pVsNP : Core .pVsNP
  bsd : Core .bsd
  riemann : Core .riemann
  yangMills : Core .yangMills

structure SevenEndpoints (Endpoint : ProblemId → Prop) : Prop where
  beal : Endpoint .beal
  navierStokes : Endpoint .navierStokes
  hodge : Endpoint .hodge
  pVsNP : Endpoint .pVsNP
  bsd : Endpoint .bsd
  riemann : Endpoint .riemann
  yangMills : Endpoint .yangMills

def SevenInhabitants.at
    {Core : ProblemId → Prop}
    (h : SevenInhabitants Core) :
    ∀ p, Core p
  | .beal => h.beal
  | .navierStokes => h.navierStokes
  | .hodge => h.hodge
  | .pVsNP => h.pVsNP
  | .bsd => h.bsd
  | .riemann => h.riemann
  | .yangMills => h.yangMills

def SevenEndpoints.at
    {Endpoint : ProblemId → Prop}
    (h : SevenEndpoints Endpoint) :
    ∀ p, Endpoint p
  | .beal => h.beal
  | .navierStokes => h.navierStokes
  | .hodge => h.hodge
  | .pVsNP => h.pVsNP
  | .bsd => h.bsd
  | .riemann => h.riemann
  | .yangMills => h.yangMills

def SevenInhabitants.ofForall
    {Core : ProblemId → Prop}
    (h : ∀ p, Core p) :
    SevenInhabitants Core :=
  { beal := h .beal
    navierStokes := h .navierStokes
    hodge := h .hodge
    pVsNP := h .pVsNP
    bsd := h .bsd
    riemann := h .riemann
    yangMills := h .yangMills }

def SevenEndpoints.ofForall
    {Endpoint : ProblemId → Prop}
    (h : ∀ p, Endpoint p) :
    SevenEndpoints Endpoint :=
  { beal := h .beal
    navierStokes := h .navierStokes
    hodge := h .hodge
    pVsNP := h .pVsNP
    bsd := h .bsd
    riemann := h .riemann
    yangMills := h .yangMills }

theorem sevenInhabitants_iff_forall
    (Core : ProblemId → Prop) :
    SevenInhabitants Core ↔ ∀ p, Core p := by
  constructor
  · exact SevenInhabitants.at
  · exact SevenInhabitants.ofForall

theorem sevenEndpoints_iff_forall
    (Endpoint : ProblemId → Prop) :
    SevenEndpoints Endpoint ↔ ∀ p, Endpoint p := by
  constructor
  · exact SevenEndpoints.at
  · exact SevenEndpoints.ofForall

/-- Consumer-only kernel. No field is allowed to assert a Core. -/
structure UniversalKernel where
  Core : ProblemId → Prop
  Endpoint : ProblemId → Prop
  consume : ∀ p, Core p → Endpoint p

/-- Exact reduction kernel: equivalence requires a checked reverse map. -/
structure ExactUniversalKernel extends UniversalKernel where
  reflect : ∀ p, Endpoint p → Core p

/-- The universal composition theorem. It is powerful only to the extent that
all seven genuinely independent material inhabitants have been supplied. -/
theorem universal_closure
    (K : UniversalKernel)
    (h : SevenInhabitants K.Core) :
    SevenEndpoints K.Endpoint := by
  exact SevenEndpoints.ofForall (fun p => K.consume p (h.at p))

/-- Exact universal closure is logically equivalent to the seven material
inhabitants when every lane has a checked reflection map. -/
theorem exact_universal_closure_iff
    (K : ExactUniversalKernel) :
    SevenEndpoints K.Endpoint ↔ SevenInhabitants K.Core := by
  constructor
  · intro h
    exact SevenInhabitants.ofForall (fun p => K.reflect p (h.at p))
  · exact universal_closure K.toUniversalKernel

/-- One external-release gate is kept separate from mathematics and from the
mechanical P01 min-cut. -/
structure FinalRootInputs (K : UniversalKernel) : Prop where
  material : SevenInhabitants K.Core
  Mechanical : Prop
  Release : Prop
  mechanical_ok : Mechanical
  release_ok : Release

structure FinalRootResult (K : UniversalKernel) : Prop where
  endpoints : SevenEndpoints K.Endpoint
  Mechanical : Prop
  Release : Prop
  mechanical_ok : Mechanical
  release_ok : Release

/-- Universal FINAL_ROOT composition law. This theorem still cannot fire until
the caller supplies all seven material proofs plus mechanical and release
proofs. -/
theorem universal_final_root
    (K : UniversalKernel)
    (h : FinalRootInputs K) :
    FinalRootResult K :=
  { endpoints := universal_closure K h.material
    Mechanical := h.Mechanical
    Release := h.Release
    mechanical_ok := h.mechanical_ok
    release_ok := h.release_ok }

/-- Projection firewall: a universal result cannot erase the fact that seven
endpoint proofs are required. -/
theorem universal_final_root_has_all_endpoints
    (K : UniversalKernel)
    (h : FinalRootResult K) :
    ∀ p, K.Endpoint p :=
  h.endpoints.at

#print axioms MCore.FinalFail.Universal.universal_closure
#print axioms MCore.FinalFail.Universal.exact_universal_closure_iff
#print axioms MCore.FinalFail.Universal.universal_final_root

end MCore.FinalFail.Universal
