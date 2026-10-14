import ATK.Terminal.NSModelo

/-!
# Portão de REFUTAÇÃO de NS — MODELO (vira `ATK/Terminal/NSRefutacao.lean`)

A resolução do problema também pode ser a refutação: ¬(A) implica o enunciado (C) do Clay (colapso, com f = 0). Mesmas exigências do portão de
prova (sem hipóteses, axiomas padrão, tipo elaborado = negação do enunciado oficial). Uma linha
refutada conta como RESOLVIDA, não como verde.
-/

namespace ATK.Terminal.NSRefutacao

open ATK.Conditional.NavierStokes ATK.Terminal.NSModelo

theorem refutacao : ¬ (ClayStatementA modeloGenuino) := PROVA_DA_REFUTACAO

end ATK.Terminal.NSRefutacao

#print axioms ATK.Terminal.NSRefutacao.refutacao
