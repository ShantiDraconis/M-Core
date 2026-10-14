import ATK.FinalRoot

/-!
# Ligação de PNP — MODELO (vira `ATK/Terminal/PNPModelo.lean`)

Ligação L2 — parte 1 no kernel (`ATK.LigacaoPNP`: P e NP sobre `Turing.FinTM2`); falta a instância `ComplexityModel` (composição de máquinas em tempo polinomial) e a linguagem SAT.
O portão de prova (`PNP.lean`) e o de refutação (`PNPRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.PNPModelo

open ATK.Conditional.PvsNP

noncomputable def modeloGenuino : ComplexityModel.{0} := LIGACAO_L2

noncomputable def sat : modeloGenuino.Lang := LIGACAO_L2_SAT

end ATK.Terminal.PNPModelo
