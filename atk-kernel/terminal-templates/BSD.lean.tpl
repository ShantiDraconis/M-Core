import ATK.FinalRoot
import ATK.Terminal.BSDClay
import ATK.Terminal.BSDRefinada

/-!
# Portão terminal de BSD (BSD_FULL) — MODELO (não compilado; vira `ATK/Terminal/BSD.lean`)

**BSD_FULL = BSD_CLAY ∧ BSD_REFINED** (`ATK.BSDPortoes.full_iff`). As peças ficam nos dois
subportões, cada um auditável por si:

1. `BSDClay.lean.tpl`: ligação L4, ponte B6 (Gross–Zagier–Kolyvagin) e produtor O6 (posto) —
   a parte do posto, que é o enunciado oficial do Clay;
2. `BSDRefinada.lean.tpl`: produtor O7 (Ш finito e fórmula refinada).

Este portão não tem peças próprias: só compõe os dois.
-/

namespace ATK.Terminal.BSD

open ATK.Conditional.BSD ATK.Terminal.BSDModelo

theorem terminal : BSDFull modeloGenuino :=
  ⟨ATK.Terminal.BSDClay.terminal, ATK.Terminal.BSDRefinada.terminal⟩

end ATK.Terminal.BSD

#print axioms ATK.Terminal.BSD.terminal
