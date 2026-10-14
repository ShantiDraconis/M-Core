import ATK.Terminal.RH
import ATK.Terminal.Beal
import ATK.Terminal.NS
import ATK.Terminal.PNP
import ATK.Terminal.Hodge
import ATK.Terminal.BSD
import ATK.Terminal.YM

/-!
# Raiz final (`CLOSED_MATH`) — MODELO (vira `ATK/ClosedMathGate.lean`)

Não falta nada além dos sete portões: com os sete certificados, este arquivo compila como está e o
auditor calcula `UNIVERSAL_GREEN = true` e o hash de `FINAL_ROOT`.
-/

namespace ATK.ClosedMathGate

/-- Os modelos genuínos das cinco linhas paramétricas (ligações L1–L5). -/
noncomputable def modelos : ATK.ClosedMath.Models where
  ns := ATK.Terminal.NSModelo.modeloGenuino
  cx := ATK.Terminal.PNPModelo.modeloGenuino
  sat := ATK.Terminal.PNPModelo.sat
  hodge := ATK.Terminal.HodgeModelo.modeloGenuino
  bsd := ATK.Terminal.BSDModelo.modeloGenuino
  ym := ATK.Terminal.YMModelo.modeloGenuino

theorem closed_math : ATK.FinalRoot.Raiz modelos :=
  ⟨ATK.Terminal.RH.terminal, ATK.Terminal.Beal.terminal, ATK.Terminal.NS.terminal,
   ATK.Terminal.PNP.terminal, ATK.Terminal.Hodge.terminal, ATK.Terminal.BSD.terminal,
   ATK.Terminal.YM.terminal⟩

end ATK.ClosedMathGate

#print axioms ATK.ClosedMathGate.closed_math
