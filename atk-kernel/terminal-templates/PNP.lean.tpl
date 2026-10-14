import ATK.FinalRoot
import ATK.Terminal.PNPModelo

/-!
# Portão terminal de P ≠ NP — MODELO (não compilado; vira `ATK/Terminal/PNP.lean`)

1. **Ligação L2**: `modeloGenuino` com linguagens sobre um alfabeto finito, P e NP definidos por
   máquinas de Turing de tempo polinomial (a Mathlib tem `Turing.TM2ComputableInPolyTime`, mas ainda
   não a composição de máquinas, necessária para `P_closed_under_red`), e `sat` = SAT.
2. **Ponte B4**: Cook–Levin sobre esse modelo.
3. **Produtor O4**: SAT ∉ P.
-/

namespace ATK.Terminal.PNP

open ATK.Conditional.PvsNP ATK.Terminal.PNPModelo

theorem ponte : CookLevin modeloGenuino sat := PROVA_DA_PONTE_B4

theorem produtor : SATNotInP modeloGenuino sat := PROVA_DO_PRODUTOR_O4

theorem terminal : PneNP modeloGenuino := pvsnp_conditional ponte produtor

end ATK.Terminal.PNP

#print axioms ATK.Terminal.PNP.terminal
