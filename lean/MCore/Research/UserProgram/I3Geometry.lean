import Mathlib
import MCore.Research.UserProgram.ThreeChannel

namespace MCore.Research.UserProgram

/-- A primitive cube root represented algebraically. -/
noncomputable def omega3 : ℂ := (-1 + Real.sqrt 3 * Complex.I) / 2

theorem sqrt_three_sq : (Real.sqrt 3)^2 = 3 := by
  norm_num

theorem omega3_sq_add_omega3_add_one :
    omega3^2 + omega3 + 1 = 0 := by
  have hre : omega3.re = -1 / 2 := by
    norm_num [omega3, Complex.div_re, Complex.mul_re]
  have him : omega3.im = Real.sqrt 3 / 2 := by
    norm_num [omega3, Complex.div_im, Complex.mul_im]
  apply Complex.ext
  · simp only [pow_two, Complex.add_re, Complex.mul_re, Complex.one_re,
      Complex.zero_re, hre, him]
    nlinarith [sqrt_three_sq]
  · simp only [pow_two, Complex.add_im, Complex.mul_im, Complex.one_im,
      Complex.zero_im, hre, him]
    ring

theorem omega3_cube : omega3^3 = 1 := by
  have h := omega3_sq_add_omega3_add_one
  apply sub_eq_zero.mp
  calc
    omega3^3 - 1 = (omega3 - 1) * (omega3^2 + omega3 + 1) := by ring
    _ = 0 := by rw [h, mul_zero]

noncomputable def I3State.phase : I3State → ℂ
  | .manifesto => 1
  | .travessia => omega3
  | .semente => omega3^2

theorem phase_sum_zero :
    I3State.phase .manifesto +
    I3State.phase .travessia +
    I3State.phase .semente = 0 := by
  simpa [I3State.phase, add_assoc, add_comm, add_left_comm] using
    omega3_sq_add_omega3_add_one

theorem phase_next (s : I3State) :
    I3State.phase s.next = omega3 * I3State.phase s := by
  cases s
  · change omega3 = omega3 * 1
    simp
  · change omega3 ^ 2 = omega3 * omega3
    ring
  · change (1 : ℂ) = omega3 * omega3 ^ 2
    calc
      1 = omega3 ^ 3 := omega3_cube.symm
      _ = omega3 * omega3 ^ 2 := by ring

structure ComplexThreeChannel where
  manifesto : ℂ
  travessia : ℂ
  semente : ℂ

noncomputable def ComplexThreeChannel.mean (x : ComplexThreeChannel) : ℂ :=
  (x.manifesto + x.travessia + x.semente) / 3

noncomputable def ComplexThreeChannel.centered (x : ComplexThreeChannel) : ComplexThreeChannel where
  manifesto := x.manifesto - x.mean
  travessia := x.travessia - x.mean
  semente := x.semente - x.mean

theorem ComplexThreeChannel.centered_sum_zero (x : ComplexThreeChannel) :
    x.centered.manifesto + x.centered.travessia + x.centered.semente = 0 := by
  simp [ComplexThreeChannel.centered, ComplexThreeChannel.mean]
  ring

end MCore.Research.UserProgram
