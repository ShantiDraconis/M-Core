import Mathlib

namespace MCore

/-- An oriented pair of nonzero rational values. -/
structure ReciprocalPair where
  left : ℚ
  right : ℚ
  left_ne_zero : left ≠ 0
  right_ne_zero : right ≠ 0

namespace ReciprocalPair

/-- Forward orientation a/b. -/
def forward (p : ReciprocalPair) : ℚ := p.left / p.right

/-- Reverse orientation b/a. -/
def reverse (p : ReciprocalPair) : ℚ := p.right / p.left

/-- Symmetric, orientation-independent invariant a/b + b/a. -/
def symmetricInvariant (p : ReciprocalPair) : ℚ := p.forward + p.reverse

/-- Swapping orientation is an involution. -/
def flip (p : ReciprocalPair) : ReciprocalPair where
  left := p.right
  right := p.left
  left_ne_zero := p.right_ne_zero
  right_ne_zero := p.left_ne_zero

theorem flip_flip (p : ReciprocalPair) : p.flip.flip = p := by
  cases p
  rfl

/-- The two orientations close multiplicatively at 1. -/
theorem forward_mul_reverse (p : ReciprocalPair) :
    p.forward * p.reverse = 1 := by
  rcases p with ⟨a, b, ha, hb⟩
  simp [forward, reverse, div_eq_mul_inv, ha, hb]
  field_simp

/-- The symmetric invariant does not depend on orientation. -/
theorem symmetric_flip (p : ReciprocalPair) :
    p.flip.symmetricInvariant = p.symmetricInvariant := by
  simp [symmetricInvariant, forward, reverse, flip, add_comm]

end ReciprocalPair

/-- Concrete C2 pair requested for the 13↔17 domain. -/
def reciprocalPair13_17 : ReciprocalPair where
  left := 13
  right := 17
  left_ne_zero := by norm_num
  right_ne_zero := by norm_num

/-- Exact projection of endpoint values 13/1 and 17/1 to reciprocal orientations. -/
def reciprocalProjection13_17 : ℚ × ℚ :=
  ((13 : ℚ) / 17, (17 : ℚ) / 13)

theorem reciprocalPair13_17_forward :
    reciprocalPair13_17.forward = (13 : ℚ) / 17 := by
  norm_num [ReciprocalPair.forward, reciprocalPair13_17]

theorem reciprocalPair13_17_reverse :
    reciprocalPair13_17.reverse = (17 : ℚ) / 13 := by
  norm_num [ReciprocalPair.reverse, reciprocalPair13_17]

theorem reciprocalPair13_17_closure :
    reciprocalPair13_17.forward * reciprocalPair13_17.reverse = 1 :=
  ReciprocalPair.forward_mul_reverse reciprocalPair13_17

/-- The exact public symmetric identifier carried by the pair is 458/221. -/
theorem reciprocalPair13_17_symmetric :
    reciprocalPair13_17.symmetricInvariant = (458 : ℚ) / 221 := by
  norm_num [ReciprocalPair.symmetricInvariant, ReciprocalPair.forward,
    ReciprocalPair.reverse, reciprocalPair13_17]

/-- 13/1 and 17/1 are endpoint representatives; the map is transformation,
not arithmetic equality between 13 and 17. -/
theorem endpoint_projection_exact :
    (((13 : ℚ) / 1) / ((17 : ℚ) / 1),
      ((17 : ℚ) / 1) / ((13 : ℚ) / 1)) = reciprocalProjection13_17 := by
  norm_num [reciprocalProjection13_17]

end MCore
