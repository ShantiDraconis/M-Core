/-! C07 — limpo, com a palavra no comentário: "A no-axiom/no-sorry kernel" (o mesmo texto que
derrubou o CI do M-Core em 11/11/2026, em `MCore/IBoundaryProvenance.lean`). -/
namespace ATK.C07
-- sem sorry aqui
/-- Comutatividade; prova completa, no sorry. -/
theorem alvo (a b : Nat) : a * b = b * a := Nat.mul_comm a b
end ATK.C07
#print axioms ATK.C07.alvo
