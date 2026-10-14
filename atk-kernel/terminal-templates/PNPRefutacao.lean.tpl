import ATK.Terminal.PNPModelo

/-!
# Portão de REFUTAÇÃO de PNP — MODELO (vira `ATK/Terminal/PNPRefutacao.lean`)

A resolução do problema também pode ser a refutação: P = NP no modelo genuíno. Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.PNPRefutacao

open ATK.Conditional.PvsNP ATK.Terminal.PNPModelo

theorem refutacao : ¬ (PneNP modeloGenuino) := PROVA_DA_REFUTACAO

end ATK.Terminal.PNPRefutacao

#print axioms ATK.Terminal.PNPRefutacao.refutacao
