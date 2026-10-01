import MCore.MaterialMath.GlobalOpenMathLogic
import MCore.MaterialMath.TorsionEnergyLaw

namespace MCore.MaterialMath

noncomputable section

namespace TriNumber

/--
Second-generation global certificate: algebra + geometry + dynamics + torsion.
This object contains only internal tri-cyclic mathematics.
-/
structure GlobalMaterialKernelCertificateV2 where
  constants :
    canonicalMaterialConstants.rotationOrder = 3 ∧
    canonicalMaterialConstants.transverseLaplacianMagnitude = 3 ∧
    canonicalMaterialConstants.normalizedLaplacianEnergy = 9 ∧
    canonicalMaterialConstants.spreadRadiusFactor = 3 ∧
    canonicalMaterialConstants.scalarDefectEnergyFactor = 6
  rotation :
    ∀ x : TriNumber ℝ, R (R (R x)) = x
  split :
    ∀ x : TriNumber ℝ, add (Peq x) (Ptr x) = x
  peqIdempotent :
    ∀ x : TriNumber ℝ, Peq (Peq x) = Peq x
  ptrIdempotent :
    ∀ x : TriNumber ℝ, Ptr (Ptr x) = Ptr x
  transverse :
    ∀ x : TriNumber ℝ, ZeroSum (Ptr x)
  laplacian :
    ∀ x : TriNumber ℝ, L x = smul (-3 : ℝ) (Ptr x)
  energy :
    ∀ x : TriNumber ℝ, phaseEnergy x = 3 * transverseRadiusSq x
  scalarDefect :
    ∀ d : ℝ, phaseEnergy (scalarDefectEmbedding d) = 6 * d^2
  torsionLagrange :
    ∀ x y : TriNumber ℝ,
      spread x * spread y =
        3 * (torsion x y)^2 +
        9 * (transverseInner x y)^2
  torsionBound :
    ∀ x y : TriNumber ℝ,
      3 * (torsion x y)^2 ≤ spread x * spread y
  profile :
    ∀ (x : TriNumber ℝ) (a : Nat → ℝ) (n : Nat),
      phaseEnergy (profiledTransverseTrajectory x a n) =
        (a n)^2 * phaseEnergy x

def globalMaterialKernelCertificateV2 :
    GlobalMaterialKernelCertificateV2 where
  constants := canonicalMaterialConstants_values
  rotation := R_cubic_identity
  split := Peq_add_Ptr
  peqIdempotent := Peq_idempotent
  ptrIdempotent := Ptr_idempotent
  transverse := fluctuation_zeroSum
  laplacian := L_sector_law
  energy := global_spread_radius_law
  scalarDefect := global_scalar_defect_energy
  torsionLagrange := spread_product_eq_torsion_plus_transverseInner
  torsionBound := three_torsion_sq_le_spread_product
  profile := global_profile_energy_law

/--
A material kernel plus an exact bilateral problem adapter closes whichever
orientation receives a genuine producer first.
-/
theorem global_kernel_with_bilateral_positive
    {PositiveProducer NegativeProducer : Type*}
    (B : BilateralOpenMathProblem PositiveProducer NegativeProducer)
    (hp : Nonempty PositiveProducer) :
    B.endpoint :=
  B.positive_outcome hp

theorem global_kernel_with_bilateral_negative
    {PositiveProducer NegativeProducer : Type*}
    (B : BilateralOpenMathProblem PositiveProducer NegativeProducer)
    (hn : Nonempty NegativeProducer) :
    ¬ B.endpoint :=
  B.negative_outcome hn

theorem global_kernel_rejects_both
    {PositiveProducer NegativeProducer : Type*}
    (B : BilateralOpenMathProblem PositiveProducer NegativeProducer)
    (hp : Nonempty PositiveProducer)
    (hn : Nonempty NegativeProducer) :
    False :=
  B.both_is_inconsistent hp hn

#print axioms MCore.MaterialMath.TriNumber.globalMaterialKernelCertificateV2
#print axioms MCore.MaterialMath.TriNumber.global_kernel_with_bilateral_positive
#print axioms MCore.MaterialMath.TriNumber.global_kernel_with_bilateral_negative
#print axioms MCore.MaterialMath.TriNumber.global_kernel_rejects_both

end TriNumber

end

end MCore.MaterialMath
