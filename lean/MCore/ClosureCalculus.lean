import Mathlib

namespace MCore.ClosureCalculus

theorem transport {P Q : Prop} (h : P ↔ Q) (p : P) : Q := h.mp p
theorem discharge {H P Q : Prop} (f : H → P) (g : P → Q) : H → Q :=
  fun h => g (f h)
theorem witness {α : Type*} {P : α → Prop} (x : α) (h : P x) : ∃ y, P y :=
  ⟨x, h⟩
theorem refute {α : Type*} {P Q : α → Prop} (x : α)
    (hp : P x) (hq : ¬ Q x) : ¬ (∀ y, P y → Q y) :=
  fun h => hq (h x hp)

def Fails {α : Type*} (A S : α → Bool) (y : α) : Prop := A y ≠ S y
def Aligns {α : Type*} (A : α → Bool) (r : α → α) (x : α) : Prop :=
  A (r x) = A x
def Cover {α : Type*} (A S : α → Bool) (r : α → α) : Prop :=
  (∃ y, Fails A S y) → ∃ x, Fails A S (r x)

theorem align_iff_fail_image {α : Type*} (A S : α → Bool) (r : α → α)
    (h : ∀ x, S (r x) = !A x) (x : α) :
    Aligns A r x ↔ Fails A S (r x) := by
  unfold Aligns Fails
  rw [h x]
  cases A x <;> cases A (r x) <;> decide

theorem cover_iff_failure_to_alignment {α : Type*}
    (A S : α → Bool) (r : α → α) (h : ∀ x, S (r x) = !A x) :
    Cover A S r ↔ ((∃ y, Fails A S y) → ∃ x, Aligns A r x) := by
  constructor
  · intro hc hf
    obtain ⟨x, hx⟩ := hc hf
    exact ⟨x, (align_iff_fail_image A S r h x).mpr hx⟩
  · intro hc hf
    obtain ⟨x, hx⟩ := hc hf
    exact ⟨x, (align_iff_fail_image A S r h x).mp hx⟩

theorem empty_input_fuel (clock : Nat → Nat) (n : Nat)
    (h : Monotone clock) : clock 0 ≤ clock n := h (Nat.zero_le n)

-- Infinite domain: reduction flips parity and avoids zero.
def counterA (n : Nat) : Bool := n % 2 == 1
def counterS (n : Nat) : Bool := if n = 0 then true else counterA n
def counterR (n : Nat) : Nat := if n % 2 = 0 then 1 else 2

theorem counter_semantics (n : Nat) :
    counterS (counterR n) = !counterA n := by
  have h : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases h with h | h <;> simp [counterS, counterR, counterA, h]

theorem counter_failure : ∃ y, Fails counterA counterS y := ⟨0, by simp [Fails, counterA, counterS]⟩

theorem counter_no_alignment (n : Nat) : ¬ Aligns counterA counterR n := by
  have h : n % 2 = 0 ∨ n % 2 = 1 := by omega
  rcases h with h | h <;> simp [Aligns, counterA, counterR, h]

theorem counter_no_cover : ¬ Cover counterA counterS counterR := by
  intro hc
  obtain ⟨x, hx⟩ := hc counter_failure
  exact counter_no_alignment x
    ((align_iff_fail_image counterA counterS counterR counter_semantics x).mpr hx)

#print axioms align_iff_fail_image
#print axioms cover_iff_failure_to_alignment
#print axioms empty_input_fuel
#print axioms counter_semantics
#print axioms counter_no_cover

end MCore.ClosureCalculus
