import ATK.Terminal.RH
import ATK.Terminal.Beal

/-!
# Portão do verde fiel (RH ∧ Beal) — MODELO (vira `ATK/Terminal/VerdeFiel.lean`)

Não falta nada além dos dois portões: assim que `ATK/Terminal/RH.lean` e `ATK/Terminal/Beal.lean`
existirem e forem certificados, este arquivo compila como está.
-/

namespace ATK.Terminal.VerdeFiel

theorem verde_fiel : ATK.FinalRoot.VerdeFiel := ⟨ATK.Terminal.RH.terminal, ATK.Terminal.Beal.terminal⟩

end ATK.Terminal.VerdeFiel

#print axioms ATK.Terminal.VerdeFiel.verde_fiel
