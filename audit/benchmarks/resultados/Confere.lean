import Mathlib
open BigOperators Real Nat Topology Rat

/-! Conferência independente dos três defeitos certificados, com provas escritas à mão (Lean v4.19.0, Mathlib v4.19.0):
`#print axioms` mostra só `propext`, `Classical.choice`, `Quot.sound`. Ver RESUMO.md. -/

-- miniF2F mathd_algebra_208: o enunciado é falso
theorem m208_falso : ¬ (Real.sqrt 1000000 - 1000000^(1/3) = 900) := by
  have h : Real.sqrt 1000000 = 1000 := by
    rw [show (1000000 : ℝ) = 1000 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  norm_num [h]

-- miniF2F mathd_algebra_275: as hipóteses são contraditórias
theorem m275_vazio (x : ℝ) (h : ((11:ℝ)^(1 / 4))^(3 * x - 3) = 1 / 5) : False := by
  norm_num at h

-- ProofNet exercise_4_4_9: falso em p = 2
theorem pn449_falso : ¬ ∀ (p : ℕ) (hp : Nat.Prime p),
    (∃ S : Finset (ZMod p), S.card = (p-1)/2 ∧ ∃ x : ZMod p, x^2 = p) ∧
    (∃ S : Finset (ZMod p), S.card = (p-1)/2 ∧ ¬ ∃ x : ZMod p, x^2 = p) := by
  intro h
  obtain ⟨-, S, -, hS⟩ := h 2 Nat.prime_two
  exact hS ⟨0, by decide⟩

#print axioms m208_falso
#print axioms m275_vazio
#print axioms pn449_falso
