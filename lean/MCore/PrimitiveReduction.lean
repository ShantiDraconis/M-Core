import Mathlib

namespace MCore.PrimitiveReduction

theorem prime_dvd_third {p a b c x y z : Nat}
    (hp : p.Prime) (ha : p ∣ a) (hb : p ∣ b)
    (hx : x ≠ 0) (hy : y ≠ 0)
    (he : a ^ x + b ^ y = c ^ z) : p ∣ c := by
  have h : p ∣ c ^ z := by
    rw [← he]
    exact dvd_add (dvd_pow ha hx) (dvd_pow hb hy)
  exact hp.dvd_of_dvd_pow h

theorem signature_transport {a b c x y z d e f r s t : Nat}
    (hx : x = r * d) (hy : y = s * e) (hz : z = t * f)
    (h : a ^ x + b ^ y = c ^ z) :
    (a ^ r) ^ d + (b ^ s) ^ e = (c ^ t) ^ f := by
  simpa only [← pow_mul, ← hx, ← hy, ← hz] using h

theorem no_common_prime_pair {p a b c x y z : Nat}
    (hp : p.Prime) (hx : x ≠ 0) (hy : y ≠ 0)
    (he : a ^ x + b ^ y = c ^ z)
    (hprim : ¬ (p ∣ a ∧ p ∣ b ∧ p ∣ c)) :
    ¬ (p ∣ a ∧ p ∣ b) := by
  rintro ⟨ha, hb⟩
  exact hprim ⟨ha, hb, prime_dvd_third hp ha hb hx hy he⟩

#print axioms prime_dvd_third
#print axioms signature_transport
#print axioms no_common_prime_pair

end MCore.PrimitiveReduction
