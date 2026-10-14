import ATK.FinalRoot

/-!
# Ligação de Hodge — MODELO (vira `ATK/Terminal/HodgeModelo.lean`)

Ligação L3 — cohomologia racional, decomposição de Hodge e classes de ciclos de variedades projetivas complexas lisas (ausentes da Mathlib).
O portão de prova (`Hodge.lean`) e o de refutação (`HodgeRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.HodgeModelo

open ATK.Conditional.Hodge

noncomputable def modeloGenuino : HodgeModel.{0, 0} := LIGACAO_L3

end ATK.Terminal.HodgeModelo
