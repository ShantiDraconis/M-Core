import MCore.Real.P01ParserWitnessComposition
import MCore.Real.P01VerifierComposition
import MCore.Real.P02SemanticMismatchAlgebra
import MCore.Real.P01FullVerifierPhysical
import MCore.Real.P01IntegratedMachine

namespace MCore.FinalFail.RecoveredClosedFragments

open MCore.Real
open MCore.Real.CanonicalFinalProof
open MCore.Real.CanonicalCircuitBits
open MCore.Real.CanonicalSATWitness
open MCore.Real.CanonicalSATVerifier

theorem witness_guess_phase_polynomial :=
  MCore.Real.P01ParserWitnessComposition.witness_guess_phase_polynomial

theorem verifier_correct
    (phi : CircuitK1.Circuit)
    (w : SATWitness phi) :
    verifyWitness phi w = true ↔ SATWitnessAccepts phi w :=
  MCore.Real.P01VerifierComposition.verifier_correct phi w

theorem decode_verify_iff_satBits
    (x : BitString) :
    (∃ phi : CircuitK1.Circuit,
        decodeCircuit x = some phi ∧
        ∃ w : SATWitness phi, verifyWitness phi w = true) ↔
      MCore.Real.CanonicalSATBoundary.SATBits circuitBitEncoding x :=
  MCore.Real.P01VerifierComposition.decode_verify_iff_satBits x

theorem no_semanticMismatch_iff_match :=
  MCore.Real.P02SemanticMismatchAlgebra.no_semanticMismatch_iff_match

theorem declaredSATCorrect_iff_no_semanticMismatch :=
  MCore.Real.P02SemanticMismatchAlgebra.declaredSATCorrect_iff_no_semanticMismatch

theorem physical_read_witness_correct :=
  MCore.Real.P01FullVerifierPhysical.readWitnessIndexed_correct

theorem physical_source_end_preserved :=
  MCore.Real.P01FullVerifierPhysical.source_end_preserves_witness_and_source

theorem integrated_phase_bridge :=
  MCore.Real.P01IntegratedMachine.integratedPhaseBridgeCertificate

#print axioms MCore.FinalFail.RecoveredClosedFragments.physical_read_witness_correct
#print axioms MCore.FinalFail.RecoveredClosedFragments.physical_source_end_preserved
#print axioms MCore.FinalFail.RecoveredClosedFragments.integrated_phase_bridge
#print axioms MCore.FinalFail.RecoveredClosedFragments.witness_guess_phase_polynomial
#print axioms MCore.FinalFail.RecoveredClosedFragments.verifier_correct
#print axioms MCore.FinalFail.RecoveredClosedFragments.decode_verify_iff_satBits
#print axioms MCore.FinalFail.RecoveredClosedFragments.no_semanticMismatch_iff_match
#print axioms MCore.FinalFail.RecoveredClosedFragments.declaredSATCorrect_iff_no_semanticMismatch

end MCore.FinalFail.RecoveredClosedFragments
