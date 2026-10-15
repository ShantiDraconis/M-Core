import ATK.FinalRoot
import ATK.Terminal.BSDModelo

/-!
# Portão BSD_CLAY — MODELO (não compilado; vira `ATK/Terminal/BSDClay.lean`)

A parte do posto de BSD, que é o enunciado oficial do Clay (`ATK.BSDPortoes.clay_fiel`):

1. **Ligação L4**: `modeloGenuino` (ver `BSDModelo.lean.tpl`).
2. **Ponte B6**: Gross–Zagier–Kolyvagin (posto analítico ≤ 1).
3. **Produtor O6**: igualdade dos postos quando o posto analítico é ≥ 2.

Este portão sozinho **não** acende a linha BSD: ela exige BSD_FULL = BSD_CLAY ∧ BSD_REFINED.
-/

namespace ATK.Terminal.BSDClay

open ATK.Conditional.BSD ATK.Terminal.BSDModelo

theorem ponte : GrossZagierKolyvagin modeloGenuino := PROVA_DA_PONTE_B6

theorem produtorPosto : RankOpen modeloGenuino := PROVA_DO_PRODUTOR_O6

theorem terminal : BSDRank modeloGenuino := bsd_rank_conditional ponte produtorPosto

end ATK.Terminal.BSDClay

#print axioms ATK.Terminal.BSDClay.terminal
