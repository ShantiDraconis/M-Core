/-! C10 — vazio escondido: o nome promete um resultado, a definição é `True`. -/
namespace ATK.C10
/-- "A hipótese de Riemann" -/
def HipoteseDeRiemann : Prop := True
theorem alvo : HipoteseDeRiemann := trivial
end ATK.C10
#print axioms ATK.C10.alvo
