import ATK.FinalRoot
import ATK.LigacaoNS

/-!
# Ligação de NS — MODELO (vira `ATK/Terminal/NSModelo.lean`)

Ligação L1 — **construída** (`ATK.LigacaoNS.modeloNS`; `clayA_iff`: enunciado paramétrico ⟺ enunciado (A) do Clay). **Fechada** (`CLOSED`) pela revisão humana do titular em 14/10/2026 (`obligations.json`, `revisao_humana`).
O portão de prova (`NS.lean`) e o de refutação (`NSRefutacao.lean`) usam este mesmo modelo.
-/

namespace ATK.Terminal.NSModelo

open ATK.Conditional.NavierStokes

noncomputable def modeloGenuino : NSModel.{0} := ATK.LigacaoNS.modeloNS

end ATK.Terminal.NSModelo
