import ATK.Terminal.HodgeModelo

/-!
# Portão de REFUTAÇÃO de Hodge — MODELO (vira `ATK/Terminal/HodgeRefutacao.lean`)

A resolução do problema também pode ser a refutação: uma classe de Hodge racional não algébrica. Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.HodgeRefutacao

open ATK.Conditional.Hodge ATK.Terminal.HodgeModelo

theorem refutacao : ¬ (HodgeConjecture modeloGenuino) := PROVA_DA_REFUTACAO

end ATK.Terminal.HodgeRefutacao

#print axioms ATK.Terminal.HodgeRefutacao.refutacao
