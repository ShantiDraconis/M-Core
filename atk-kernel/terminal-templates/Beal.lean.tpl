import ATK.FinalRoot

/-!
# Portão terminal de Beal — MODELO (não compilado; vira `ATK/Terminal/Beal.lean`)

Rota sem pontes (recomendada): provar `ExclusaoResidualDescida`; a equivalência com Beal já está
certificada sem hipóteses (`ATK.BealCompleto.beal_incondicional`).
Rota com pontes: provar `FermatLastTheorem` (B2), `DarmonMerel` (B8) **e** `ExclusaoResidualFinal`;
usar `ATK.BealCompleto.beal_de_pontes_e_residual`. Pontes também precisam ser teoremas, não hipóteses.
-/

namespace ATK.Terminal.Beal

theorem produtor : ATK.BealFermatDescent.ExclusaoResidualDescida := PROVA_DO_PRODUTOR

theorem terminal : ATK.Conditional.Beal.BealConjecture :=
  ATK.BealCompleto.beal_incondicional.mpr produtor

end ATK.Terminal.Beal

#print axioms ATK.Terminal.Beal.produtor
#print axioms ATK.Terminal.Beal.terminal
