import ATK.FinalRoot
import ATK.ModeloPNP

/-!
# Ligação de PNP — MODELO (vira `ATK/Terminal/PNPModelo.lean`)

Ligação L2 — **construída** no kernel: `ATK.ModeloPNP.modeloPNP` (P e NP sobre `Turing.FinTM2`, reduções de Karp; `P ⊆ NP` e P fechada por reduções provados com a composição de máquinas em tempo polinomial, `ATK.ComposicaoTM2.comp`) e `ATK.ModeloPNP.SAT` (fórmulas CNF codificadas em binário, satisfatíveis). Fidelidade: `ATK.ModeloPNP.fiel : PneNP modeloPNP ↔ ATK.LigacaoPNP.PneNP` (por definição). **Fechada** (`CLOSED`) pelo titular em 14/10/2026.
O portão de prova (`PNP.lean`) e o de refutação (`PNPRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.PNPModelo

open ATK.Conditional.PvsNP

noncomputable def modeloGenuino : ComplexityModel.{0} := ATK.ModeloPNP.modeloPNP

noncomputable def sat : modeloGenuino.Lang := ATK.ModeloPNP.SAT

end ATK.Terminal.PNPModelo
