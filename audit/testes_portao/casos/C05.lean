/-! C05 — axioma privado: `private axiom`. -/
namespace ATK.C05
private axiom ax_privado : 2 + 2 = 5
theorem alvo : 2 + 2 = 5 := ax_privado
end ATK.C05
#print axioms ATK.C05.alvo
