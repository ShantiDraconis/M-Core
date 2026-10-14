import ATK.FinalRoot

/-!
# Portão de REFUTAÇÃO de Beal — MODELO (vira `ATK/Terminal/BealRefutacao.lean`)

A resolução do problema também pode ser a refutação: um contraexemplo de Beal (bases coprimas, expoentes > 2). Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.BealRefutacao

theorem refutacao : ¬ ATK.Conditional.Beal.BealConjecture := PROVA_DA_REFUTACAO

end ATK.Terminal.BealRefutacao

#print axioms ATK.Terminal.BealRefutacao.refutacao
