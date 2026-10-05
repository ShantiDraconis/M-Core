import MCore.FinalProofFirewall
import MCore.Audit.MasterCertificate

/-!
Root module for the Lake library declared with `srcDir := "lean"`.

The master claim inventory is imported here so the default `lake build` validates
its administrative state machine, reuse layer, terminal frontier registry,
dependency DAG, work queue, and audit certificate together with the existing core.
-/
