import ATK.FinalRoot

/-!
# Portão de REFUTAÇÃO de RH — MODELO (vira `ATK/Terminal/RHRefutacao.lean`)

A resolução do problema também pode ser a refutação: um zero não trivial fora da reta crítica. Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.RHRefutacao

theorem refutacao : ¬ RiemannHypothesis := PROVA_DA_REFUTACAO

end ATK.Terminal.RHRefutacao

#print axioms ATK.Terminal.RHRefutacao.refutacao
