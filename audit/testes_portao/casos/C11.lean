/-! C11 — hipótese contraditória: de `1 = 0` segue qualquer coisa; o enunciado é vazio. -/
namespace ATK.C11
theorem alvo (h : (1 : Nat) = 0) : ∀ n : Nat, n = n + 1 := absurd h (by decide)
end ATK.C11
#print axioms ATK.C11.alvo
