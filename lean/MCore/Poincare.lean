import Mathlib

namespace MCore.Poincare

/--
Poincaré is mathematically closed, but this M-Core module does not pretend that
Perelman's proof has been reconstructed inside Lean. The theorem-level import is
tracked separately from the historical mathematical status.
-/
inductive MathematicalState where
  | closedUnconditional
  deriving DecidableEq, Repr

inductive FormalImportState where
  | externalClassicalPending
  | kernelVerified
  deriving DecidableEq, Repr

/-- Abstract endpoint interface for the closed 3-manifold problem. -/
constant Closed3Manifold : Type
constant S3 : Closed3Manifold
constant SimplyConnected : Closed3Manifold → Prop
constant Diffeomorphic : Closed3Manifold → Closed3Manifold → Prop

/-- Abstract Ricci-flow-with-surgery interface used only to type the route. -/
constant RicciFlowWithSurgery : Closed3Manifold → ℝ → Closed3Manifold
constant FiniteTimeExtinction : Closed3Manifold → ℝ → Prop

/-- C0: the topological input condition. -/
def SimplyConnectedCertificate (M : Closed3Manifold) : Prop :=
  SimplyConnected M

/-- F7: finite-time Ricci-flow/surgery extinction and spherical endpoint. -/
def ExtinctionCertificate (M : Closed3Manifold) : Prop :=
  ∃ T : ℝ,
    0 < T ∧
    FiniteTimeExtinction M T ∧
    Diffeomorphic (RicciFlowWithSurgery M T) S3

/-- F8: the terminal classification statement. -/
def PoincareClassification : Prop :=
  ∀ M : Closed3Manifold,
    SimplyConnected M → Diffeomorphic M S3

/--
A faithful imported classical certificate must supply the historical endpoint
itself and the Ricci-flow route. This is the only allowed inhabitant source for
the route below until a kernel reconstruction is added.
-/
structure PerelmanClassicalCertificate where
  classification : PoincareClassification
  extinction :
    ∀ M : Closed3Manifold,
      SimplyConnected M → ExtinctionCertificate M

/-- C0 -> O -> C2 transport once the classical certificate is supplied. -/
def PoincareRouteSolution (cert : PerelmanClassicalCertificate) :
    ∀ M : Closed3Manifold,
      SimplyConnectedCertificate M → Diffeomorphic M S3 :=
  cert.classification

/-- There is no unresolved mathematical producer: the historical theorem is closed. -/
abbrev OpenMathProducerPoincare := PerelmanClassicalCertificate

def coreState : MathematicalState := .closedUnconditional
def formalImportState : FormalImportState := .externalClassicalPending

/--
The ATK distinction is intentional:
* zero OPEN_MATH gaps,
* zero material-producer gaps,
* one formal-import obligation before Lean can call the endpoint kernel-verified.
-/
def CORE_FORMAL_GAPS : Nat := 0
def MATERIAL_PRODUCER_GAPS : Nat := 0
def FORMAL_IMPORT_GAPS : Nat := 1
def POINCARE_CLAIMS : Nat := 1

theorem core_formal_gaps_zero : CORE_FORMAL_GAPS = 0 := rfl
theorem material_producer_gaps_zero : MATERIAL_PRODUCER_GAPS = 0 := rfl
theorem formal_import_gap_one : FORMAL_IMPORT_GAPS = 1 := rfl
theorem poincare_claims_one : POINCARE_CLAIMS = 1 := rfl

/--
Fail-closed promotion rule: mathematical closure alone does not manufacture a
Lean proof. Kernel promotion requires the imported certificate explicitly.
-/
theorem promote_to_kernel_endpoint
    (cert : PerelmanClassicalCertificate) :
    PoincareClassification :=
  cert.classification

end MCore.Poincare
