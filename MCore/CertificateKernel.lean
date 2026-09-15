import Mathlib

namespace MCore

/-- Status carried by certificate-DAG nodes.  Only `proved` may inhabit
`ProofCertificate`; computational/numerical evidence remains a separate status. -/
inductive NodeStatus where
  | proved
  | provedConditional
  | refuted
  | definitionInterface
  | numericalEvidence
  | openBridge
  deriving DecidableEq, Repr

/-- A proposition together with its audit identity, dependency names, and
scientific status. -/
structure CertNode where
  id : String
  statement : Prop
  deps : List String
  status : NodeStatus

/-- Kernel certificate.  Construction requires both a proof term of the exact
node proposition and an equality witnessing that the node is `proved`. -/
inductive ProofCertificate : CertNode → Type where
  | mk (n : CertNode) (hstatus : n.status = .proved)
      (proof : n.statement) : ProofCertificate n

/-- K0-K5 firewall: an OPEN_BRIDGE node cannot have a proof certificate. -/
theorem no_open (n : CertNode) (hopen : n.status = .openBridge) :
    ¬ Nonempty (ProofCertificate n) := by
  rintro ⟨c⟩
  cases c with
  | mk _ hproved _ =>
      rw [hopen] at hproved
      cases hproved

/-- K14 kernel half: every status other than PROVED is un-certifiable. -/
theorem no_promotion (n : CertNode) (h : n.status ≠ .proved) :
    ¬ Nonempty (ProofCertificate n) := by
  rintro ⟨c⟩
  cases c with
  | mk _ hproved _ =>
      exact h hproved

/-- Explicit names accepted by the later K15 environment audit.  This list is
a policy datum, not a proof that the environment contains no other axioms. -/
def allowedAxioms : List String :=
  ["propext", "Quot.sound", "Classical.choice"]

/-- Typed derivation rule.  Dependencies are nodes, not statuses; a derivation
must consume certificates for every listed dependency. -/
structure DerivedNode where
  node : CertNode
  dependencies : List CertNode
  derive : (∀ d, d ∈ dependencies → ProofCertificate d) → node.statement

/-- A derived node can be certified only after the caller separately proves
that its declared status is PROVED and supplies certificates for all deps. -/
def certifyDerived (d : DerivedNode)
    (hstatus : d.node.status = .proved)
    (hdeps : ∀ dep, dep ∈ d.dependencies → ProofCertificate dep) :
    ProofCertificate d.node :=
  ProofCertificate.mk d.node hstatus (d.derive hdeps)

/-- Regression fixture: an ordinary proved proposition is certifiable. -/
def kernelTrueNode : CertNode where
  id := "KERNEL_TRUE"
  statement := True
  deps := []
  status := .proved

example : ProofCertificate kernelTrueNode :=
  ProofCertificate.mk kernelTrueNode rfl True.intro

/-- Regression fixtures for every illegal-promotion status. -/
def kernelConditionalNode : CertNode :=
  { kernelTrueNode with id := "KERNEL_CONDITIONAL", status := .provedConditional }
def kernelRefutedNode : CertNode :=
  { kernelTrueNode with id := "KERNEL_REFUTED", status := .refuted }
def kernelDefinitionNode : CertNode :=
  { kernelTrueNode with id := "KERNEL_DEFINITION", status := .definitionInterface }
def kernelNumericalNode : CertNode :=
  { kernelTrueNode with id := "KERNEL_NUMERICAL", status := .numericalEvidence }
def kernelOpenNode : CertNode :=
  { kernelTrueNode with id := "KERNEL_OPEN", status := .openBridge }

example : ¬ Nonempty (ProofCertificate kernelConditionalNode) := by
  apply no_promotion
  decide
example : ¬ Nonempty (ProofCertificate kernelRefutedNode) := by
  apply no_promotion
  decide
example : ¬ Nonempty (ProofCertificate kernelDefinitionNode) := by
  apply no_promotion
  decide
example : ¬ Nonempty (ProofCertificate kernelNumericalNode) := by
  apply no_promotion
  decide
example : ¬ Nonempty (ProofCertificate kernelOpenNode) := by
  exact no_open kernelOpenNode rfl

end MCore
