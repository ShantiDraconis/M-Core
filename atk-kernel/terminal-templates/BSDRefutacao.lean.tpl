import ATK.Terminal.BSDModelo

/-!
# Portão de REFUTAÇÃO de BSD — MODELO (vira `ATK/Terminal/BSDRefutacao.lean`)

A resolução do problema também pode ser a refutação: uma curva elíptica sobre ℚ que viola BSD. Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.BSDRefutacao

open ATK.Conditional.BSD ATK.Terminal.BSDModelo

theorem refutacao : ¬ (BSDFull modeloGenuino) := PROVA_DA_REFUTACAO

end ATK.Terminal.BSDRefutacao

#print axioms ATK.Terminal.BSDRefutacao.refutacao
