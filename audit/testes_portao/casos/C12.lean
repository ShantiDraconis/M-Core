/-! C12 — limpo: condicional honesto, com a hipótese nomeada e satisfazível. -/
namespace ATK.C12
theorem alvo (P Q : Prop) (hP : P) (hPQ : P → Q) : Q := hPQ hP
end ATK.C12
#print axioms ATK.C12.alvo
