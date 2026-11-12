/-! C04 — axioma com atributo na mesma linha: a declaração não começa por `axiom`. -/
namespace ATK.C04
@[simp] axiom ax_atributo : 2 + 2 = 5
theorem alvo : 2 + 2 = 5 := ax_atributo
end ATK.C04
#print axioms ATK.C04.alvo
