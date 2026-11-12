/-! C06 — `native_decide`: verdadeiro, mas a prova confia no compilador, não no kernel. -/
namespace ATK.C06
theorem alvo : 2 ^ 10 = 1024 := by native_decide
end ATK.C06
#print axioms ATK.C06.alvo
