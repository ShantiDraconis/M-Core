import ATK.BaezDuarteBridge

/-!
# ATK — Obrigações fechadas por teoremas certificados

Cada teorema aqui tem **literalmente** a proposição Lean da obrigação correspondente em
`scripts/obligations.json` (campo `lean`) como enunciado. O auditor (`scripts/check_axioms.py`)
só marca uma obrigação como `CLOSED` se o teorema listado em `proof_theorem` estiver certificado
(axiomas padrão, sem `sorry`/`admit`/`axiom`) **e** se esta fonte declarar
`theorem <nome> : <proposição da obrigação>`. Nenhum estado é escrito à mão.
-/

namespace ATK.ObligationsClosed

/-- **B1** (ponte de Riemann, Nyman–Beurling–Báez-Duarte): `D_N → 0 ⇒ RH`. -/
theorem B1 : ATK.Conditional.Riemann.BaezDuarteCriterion :=
  ATK.BaezDuarteBridge.baezDuarteCriterion

end ATK.ObligationsClosed

#print axioms ATK.ObligationsClosed.B1
