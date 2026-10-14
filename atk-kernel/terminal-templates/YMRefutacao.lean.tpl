import ATK.Terminal.YMModelo

/-!
# Portão de REFUTAÇÃO de YM — MODELO (vira `ATK/Terminal/YMRefutacao.lean`)

A resolução do problema também pode ser a refutação: a negação do enunciado de Yang–Mills no modelo genuíno. Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.YMRefutacao

open ATK.Conditional.YangMills ATK.Terminal.YMModelo

theorem refutacao : ¬ (ClayYM modeloGenuino) := PROVA_DA_REFUTACAO

end ATK.Terminal.YMRefutacao

#print axioms ATK.Terminal.YMRefutacao.refutacao
