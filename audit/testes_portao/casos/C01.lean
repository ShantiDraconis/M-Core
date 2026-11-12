/-! C01 — limpo: teorema verdadeiro, prova completa. Nenhum verificador deve marcar. -/
namespace ATK.C01
theorem alvo (a b : Nat) : a + b = b + a := Nat.add_comm a b
end ATK.C01
#print axioms ATK.C01.alvo
