import ATK.FinalRoot

/-!
# Portão terminal de BSD — MODELO (não compilado; vira `ATK/Terminal/BSD.lean`)

1. **Ligação L4**: `modeloGenuino` com curvas elípticas sobre ℚ (`WeierstrassCurve` da Mathlib), suas
   L-funções, regulador, Sha, fatores de Tamagawa e torção — as L-funções ainda não estão na Mathlib.
2. **Ponte B6**: Gross–Zagier–Kolyvagin.
3. **Produtores O6, O7**: igualdade de postos e fórmula refinada.
-/

namespace ATK.Terminal.BSD

open ATK.Conditional.BSD

noncomputable def modeloGenuino : BSDModel.{0} := LIGACAO_L4

theorem ponte : GrossZagierKolyvagin modeloGenuino := PROVA_DA_PONTE_B6

theorem produtorPosto : RankOpen modeloGenuino := PROVA_DO_PRODUTOR_O6

theorem produtorRefinado : RefinedOpen modeloGenuino := PROVA_DO_PRODUTOR_O7

theorem terminal : BSDFull modeloGenuino := bsd_conditional ponte produtorPosto produtorRefinado

end ATK.Terminal.BSD

#print axioms ATK.Terminal.BSD.terminal
