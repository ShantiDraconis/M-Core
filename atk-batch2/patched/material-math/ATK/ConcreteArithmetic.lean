import Mathlib

namespace ATK.ConcreteArithmetic

/-- A strict descent on naturals cannot be defined on a nonempty domain. -/
theorem no_natural_descent {C : Type*} (hC : Nonempty C)
    (measure : C → Nat) (step : C → C)
    (decreases : ∀ c, measure (step c) < measure c) : False := by
  classical
  let m : Nat := Nat.find (show ∃ n : Nat, ∃ c : C, measure c = n from by
    obtain ⟨c⟩ := hC
    exact ⟨measure c, c, rfl⟩)
  obtain ⟨c, hc⟩ := Nat.find_spec (show ∃ n : Nat, ∃ c : C, measure c = n from by
    obtain ⟨c⟩ := hC
    exact ⟨measure c, c, rfl⟩)
  have hlt : measure (step c) < m := by simpa [hc] using decreases c
  have hmin : m ≤ measure (step c) := Nat.find_min' (show ∃ n : Nat, ∃ c : C, measure c = n from by
    obtain ⟨c⟩ := hC
    exact ⟨measure c, c, rfl⟩) ⟨step c, rfl⟩
  exact Nat.not_lt_of_ge hmin hlt

/-- A divisor of both summands of a power equation divides the third base. -/
theorem common_prime_divides_third
    {a b c x y z : Nat} (hx : 0 < x) (hy : 0 < y) (hz : 0 < z)
    (heq : a ^ x + b ^ y = c ^ z)
    {p : Nat} (hp : Nat.Prime p)
    (hpa : p ∣ a) (hpb : p ∣ b) : p ∣ c := by
  have hp_pow : p ∣ c ^ z := by
    rw [← heq]
    exact dvd_add (dvd_pow hpa (by omega)) (dvd_pow hpb (by omega))
  exact hp.dvd_of_dvd_pow hp_pow

end ATK.ConcreteArithmetic
