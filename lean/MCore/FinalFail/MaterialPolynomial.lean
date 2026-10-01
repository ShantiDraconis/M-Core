import MCore.FinalFail.MaterialField
import MCore.FinalFail.MaterialGeometry

namespace MCore.FinalFail.MaterialPolynomial

open MCore.FinalFail.MaterialAlgebra
open MCore.FinalFail.MaterialDerived

abbrev TState := MCore.FinalFail.MaterialAlgebra.TriState
abbrev LaneVector := MCore.FinalFail.MaterialAlgebra.SevenLaneVector

/-!
# Polynomial and affine dynamics over the three-state material algebra

All results here are internal consequences of the explicit three-element field
table already kernel-checked in MaterialField.

They do not assert that any external mathematical conjecture has been solved,
and they do not identify ordinary indeterminate expressions such as 0/0 with
TriState values.
-/

namespace TriState

/-- Subtraction in the explicit additive group. -/
def sub (x y : TState) : TState := x + (-y)

@[simp] theorem sub_self (x : TState) :
    sub x x = 0 := by
  exact MCore.FinalFail.MaterialAlgebra.TriState.add_neg x

/-- Square. -/
def sq (x : TState) : TState := x * x

/-- Kronecker/Lagrange basis at 0. -/
def basis0 (x : TState) : TState :=
  1 + (-(sq x))

/-- Kronecker/Lagrange basis at 1. -/
def basis1 (x : TState) : TState :=
  (.manifest : TState) * x * (x + 1)

/-- Kronecker/Lagrange basis at 2 (= -1). -/
def basis2 (x : TState) : TState :=
  (.manifest : TState) * x * (x + .manifest)

@[simp] theorem basis0_seed : basis0 .seed = 1 := by rfl
@[simp] theorem basis0_transit : basis0 .transit = 0 := by rfl
@[simp] theorem basis0_manifest : basis0 .manifest = 0 := by rfl

@[simp] theorem basis1_seed : basis1 .seed = 0 := by rfl
@[simp] theorem basis1_transit : basis1 .transit = 1 := by rfl
@[simp] theorem basis1_manifest : basis1 .manifest = 0 := by rfl

@[simp] theorem basis2_seed : basis2 .seed = 0 := by rfl
@[simp] theorem basis2_transit : basis2 .transit = 0 := by rfl
@[simp] theorem basis2_manifest : basis2 .manifest = 1 := by rfl

/-- Lagrange partition of unity on the three-element carrier. -/
theorem basis_partition (x : TState) :
    basis0 x + basis1 x + basis2 x = 1 := by
  cases x <;> rfl

/-- Pairwise orthogonality of the three point idempotents. -/
theorem basis01_orthogonal (x : TState) :
    basis0 x * basis1 x = 0 := by
  cases x <;> rfl

theorem basis02_orthogonal (x : TState) :
    basis0 x * basis2 x = 0 := by
  cases x <;> rfl

theorem basis12_orthogonal (x : TState) :
    basis1 x * basis2 x = 0 := by
  cases x <;> rfl

/-- Point idempotence. -/
theorem basis0_idem (x : TState) :
    basis0 x * basis0 x = basis0 x := by
  cases x <;> rfl

theorem basis1_idem (x : TState) :
    basis1 x * basis1 x = basis1 x := by
  cases x <;> rfl

theorem basis2_idem (x : TState) :
    basis2 x * basis2 x = basis2 x := by
  cases x <;> rfl

/-- Lagrange interpolant for an arbitrary unary operator. -/
def interpolate (f : TState → TState) (x : TState) : TState :=
  f .seed * basis0 x +
  f .transit * basis1 x +
  f .manifest * basis2 x

/-- Every unary operator on the three-element carrier is represented by the
explicit degree-at-most-two Lagrange formula. -/
theorem interpolate_exact (f : TState → TState) :
    ∀ x, interpolate f x = f x := by
  intro x
  cases x <;> rfl

/-- Functional extensional form: every endomorphism is its quadratic
interpolant. -/
theorem every_unary_operator_is_quadratic
    (f : TState → TState) :
    interpolate f = f := by
  funext x
  exact interpolate_exact f x

/-- An affine operator x ↦ a*x+b. -/
def affine (a b x : TState) : TState :=
  a * x + b

@[simp] theorem affine_zero_scale (b x : TState) :
    affine 0 b x = b := by
  cases b <;> cases x <;> rfl

@[simp] theorem affine_one_scale (b x : TState) :
    affine 1 b x = x + b := by
  cases b <;> cases x <;> rfl

/-- Composition law for affine operators. -/
theorem affine_comp
    (a b c d x : TState) :
    affine a b (affine c d x) =
      affine (a * c) (a * d + b) x := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases x <;> rfl

/-- Translation by 1 is exactly the certified three-cycle rotation. -/
theorem affine_one_one_eq_rotate (x : TState) :
    affine 1 1 x = x.rotate := by
  cases x <;> rfl

/-- Translation by 2 is the inverse/two-step rotation. -/
theorem affine_one_manifest_eq_rotate_twice (x : TState) :
    affine 1 .manifest x = x.rotate.rotate := by
  cases x <;> rfl

/-- Every nonzero affine slope yields an injective operator. -/
theorem affine_injective
    (a b : TState) (ha : a ≠ 0) :
    Function.Injective (affine a b) := by
  intro x y h
  cases a <;> cases b <;> cases x <;> cases y <;> simp [affine] at ha h ⊢

/-- Every nonzero affine slope yields a surjective operator. -/
theorem affine_surjective
    (a b : TState) (ha : a ≠ 0) :
    Function.Surjective (affine a b) := by
  intro y
  cases a <;> cases b <;> cases y <;> simp [affine] at ha ⊢ <;>
    first | exact ⟨.seed, rfl⟩ | exact ⟨.transit, rfl⟩ | exact ⟨.manifest, rfl⟩

theorem affine_bijective
    (a b : TState) (ha : a ≠ 0) :
    Function.Bijective (affine a b) :=
  ⟨affine_injective a b ha, affine_surjective a b ha⟩

/-- Frobenius fixes every point, hence is the identity endomorphism. -/
def frobenius (x : TState) : TState := (x * x) * x

theorem frobenius_eq_id :
    frobenius = id := by
  funext x
  exact MCore.FinalFail.MaterialField.TriState.frobenius_identity x

end TriState

namespace SevenLaneVector

/-- Componentwise affine action with a shared scalar and shift. -/
def affine
    (a : TState) (b x : LaneVector) : LaneVector where
  riemann := TriState.affine a b.riemann x.riemann
  beal := TriState.affine a b.beal x.beal
  pvsnp := TriState.affine a b.pvsnp x.pvsnp
  navierStokes := TriState.affine a b.navierStokes x.navierStokes
  hodge := TriState.affine a b.hodge x.hodge
  bsd := TriState.affine a b.bsd x.bsd
  yangMills := TriState.affine a b.yangMills x.yangMills

/-- Shared nonzero affine slope preserves equality of seven-lane states. -/
theorem affine_injective
    (a : TState) (b : LaneVector) (ha : a ≠ 0) :
    Function.Injective (affine a b) := by
  intro x y h
  apply MCore.FinalFail.MaterialAlgebra.SevenLaneVector.extensionality
  · exact TriState.affine_injective a b.riemann ha (congrArg LaneVector.riemann h)
  · exact TriState.affine_injective a b.beal ha (congrArg LaneVector.beal h)
  · exact TriState.affine_injective a b.pvsnp ha (congrArg LaneVector.pvsnp h)
  · exact TriState.affine_injective a b.navierStokes ha (congrArg LaneVector.navierStokes h)
  · exact TriState.affine_injective a b.hodge ha (congrArg LaneVector.hodge h)
  · exact TriState.affine_injective a b.bsd ha (congrArg LaneVector.bsd h)
  · exact TriState.affine_injective a b.yangMills ha (congrArg LaneVector.yangMills h)

/-- Hamming geometry is invariant under a common nondegenerate affine change
of coordinates. -/
theorem hamming_affine
    (a : TState) (b x y : LaneVector) (ha : a ≠ 0) :
    MCore.FinalFail.MaterialGeometry.SevenLaneVector.hamming
        (affine a b x) (affine a b y) =
      MCore.FinalFail.MaterialGeometry.SevenLaneVector.hamming x y := by
  unfold MCore.FinalFail.MaterialGeometry.SevenLaneVector.hamming affine
  have hR := TriState.affine_injective a b.riemann ha
  have hB := TriState.affine_injective a b.beal ha
  have hP := TriState.affine_injective a b.pvsnp ha
  have hN := TriState.affine_injective a b.navierStokes ha
  have hH := TriState.affine_injective a b.hodge ha
  have hD := TriState.affine_injective a b.bsd ha
  have hY := TriState.affine_injective a b.yangMills ha
  simp [hR.eq_iff, hB.eq_iff, hP.eq_iff, hN.eq_iff, hH.eq_iff, hD.eq_iff, hY.eq_iff]

end SevenLaneVector

#print axioms MCore.FinalFail.MaterialPolynomial.TriState.every_unary_operator_is_quadratic
#print axioms MCore.FinalFail.MaterialPolynomial.TriState.affine_comp
#print axioms MCore.FinalFail.MaterialPolynomial.TriState.affine_bijective
#print axioms MCore.FinalFail.MaterialPolynomial.TriState.frobenius_eq_id
#print axioms MCore.FinalFail.MaterialPolynomial.SevenLaneVector.affine_injective
#print axioms MCore.FinalFail.MaterialPolynomial.SevenLaneVector.hamming_affine

end MCore.FinalFail.MaterialPolynomial
