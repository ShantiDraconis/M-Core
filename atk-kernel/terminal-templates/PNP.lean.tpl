import ATK.FinalRoot
import ATK.Terminal.PNPModelo

/-!
# Portão terminal de P ≠ NP — MODELO (não compilado; vira `ATK/Terminal/PNP.lean`)

1. **Ligação L2** — fechada (titular, 14/10/2026): `modeloGenuino := ATK.ModeloPNP.modeloPNP`
   (P e NP sobre `Turing.FinTM2`, reduções de Karp; `P ⊆ NP` e P fechada por reduções provados com
   `ATK.ComposicaoTM2.comp`) e `sat := ATK.ModeloPNP.SAT`; `ATK.ModeloPNP.fiel`.
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
