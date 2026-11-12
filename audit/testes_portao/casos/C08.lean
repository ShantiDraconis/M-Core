/-! C08 — limpo, com a palavra dentro de uma string. -/
namespace ATK.C08
def aviso : String := "nenhum sorry e nenhum admit neste arquivo"
theorem alvo : aviso.length > 0 := by decide
end ATK.C08
#print axioms ATK.C08.alvo
