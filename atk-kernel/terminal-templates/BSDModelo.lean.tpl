import ATK.FinalRoot

/-!
# Ligação de BSD — MODELO (vira `ATK/Terminal/BSDModelo.lean`)

Ligação L4 — L-funções de curvas elípticas com continuação analítica, Ш, regulador, períodos, Tamagawa (ausentes da Mathlib).
O portão de prova (`BSD.lean`) e o de refutação (`BSDRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.BSDModelo

open ATK.Conditional.BSD

noncomputable def modeloGenuino : BSDModel.{0} := LIGACAO_L4

end ATK.Terminal.BSDModelo
