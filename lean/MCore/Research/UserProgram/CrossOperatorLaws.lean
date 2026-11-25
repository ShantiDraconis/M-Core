import Mathlib
import MCore.Research.UserProgram.ConcreteOperators

namespace MCore.Research.UserProgram

noncomputable def I3Vector.scale (z : ℂ) (x : I3Vector) : I3Vector := z • x

theorem opGamma_eq_three_C (x : I3Vector) :
    opGamma x = I3Vector.scale 3 (opC x) := by
  apply I3Vector.ext <;> change (_ + _) + _ = (3 : ℂ) * (_ / 3) <;> simp only [I3Vector.rotate, I3Vector.sum] <;> ring

theorem opC_delta_zero (x : I3Vector) :
    opC (opDelta x) = 0 := by
  apply I3Vector.ext <;> change (x.travessia + -x.manifesto + (x.semente + -x.travessia) + (x.manifesto + -x.semente)) / 3 = (0 : ℂ) <;> ring

theorem opDelta_C_zero (x : I3Vector) :
    opDelta (opC x) = 0 := by
  apply opDelta_zero_of_fixed
  exact opC_fixed x

theorem delta_cycle_telescopes (x : I3Vector) :
    opDelta x + opDelta x.rotate + opDelta x.rotate.rotate = 0 := by
  apply I3Vector.ext <;> change (_ + -_) + (_ + -_) + (_ + -_) = (0 : ℂ) <;> simp only [I3Vector.rotate] <;> ring

noncomputable def oscillatoryPart (x : I3Vector) : I3Vector :=
  x + (-(opC x))

theorem oscillatoryPart_sum_zero (x : I3Vector) :
    (oscillatoryPart x).sum = 0 := by
  change (x.manifesto + -((x.manifesto + x.travessia + x.semente) / 3) + (x.travessia + -((x.manifesto + x.travessia + x.semente) / 3)) + (x.semente + -((x.manifesto + x.travessia + x.semente) / 3))) = (0 : ℂ)
  ring

theorem reconstruct_C_osc (x : I3Vector) :
    opC x + oscillatoryPart x = x := by
  apply I3Vector.ext <;> change ((x.manifesto + x.travessia + x.semente) / 3) + (_ + -((x.manifesto + x.travessia + x.semente) / 3)) = _ <;> ring

theorem opC_oscillatory_zero (x : I3Vector) :
    opC (oscillatoryPart x) = 0 := by
  apply I3Vector.ext <;> change (x.manifesto + -((x.manifesto + x.travessia + x.semente) / 3) + (x.travessia + -((x.manifesto + x.travessia + x.semente) / 3)) + (x.semente + -((x.manifesto + x.travessia + x.semente) / 3))) / 3 = (0 : ℂ) <;> ring

noncomputable def CrossOperatorLaw : Prop :=
  (∀ x, opGamma x = I3Vector.scale 3 (opC x)) ∧
  (∀ x, opC (opDelta x) = 0) ∧
  (∀ x, opDelta (opC x) = 0) ∧
  (∀ x, opDelta x + opDelta x.rotate + opDelta x.rotate.rotate = 0) ∧
  (∀ x, (oscillatoryPart x).sum = 0) ∧
  (∀ x, opC x + oscillatoryPart x = x) ∧
  (∀ x, opC (oscillatoryPart x) = 0)

noncomputable def crossOperatorInhabitant : Inhabitant CrossOperatorLaw :=
  ⟨opGamma_eq_three_C, opC_delta_zero, opDelta_C_zero,
    delta_cycle_telescopes, oscillatoryPart_sum_zero,
    reconstruct_C_osc, opC_oscillatory_zero⟩

end MCore.Research.UserProgram
