import ATK.FinalRoot

/-!
# Ligação de YM — MODELO (vira `ATK/Terminal/YMModelo.lean`)

Ligação L5 — QFT construtiva de Yang–Mills em ℝ⁴ (Wightman/Osterwalder–Schrader) com grupo de gauge compacto (ausente da Mathlib).
O portão de prova (`YM.lean`) e o de refutação (`YMRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.YMModelo

open ATK.Conditional.YangMills

noncomputable def modeloGenuino : YMModel.{0, 0, 0} := LIGACAO_L5

end ATK.Terminal.YMModelo
