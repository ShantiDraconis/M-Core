import ATK.FinalRoot
import ATK.LigacaoNS

/-!
# Ligação de NS — MODELO (vira `ATK/Terminal/NSModelo.lean`)

Ligação L1 — **construída** (`ATK.LigacaoNS.modeloNS`; `clayA_iff`: enunciado paramétrico ⟺ enunciado (A) do Clay). Falta só a revisão humana para o status `CLOSED`.
O portão de prova (`NS.lean`) e o de refutação (`NSRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.NSModelo

open ATK.Conditional.NavierStokes

noncomputable def modeloGenuino : NSModel.{0} := ATK.LigacaoNS.modeloNS

end ATK.Terminal.NSModelo
