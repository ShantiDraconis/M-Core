import ATK.BaezDuarteBridge
import ATK.CookLevinFinal

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

/-- **B4** (ponte de P vs NP, Cook–Levin): no modelo genuíno `modeloPNP` (ligação L2), SAT ∈ NP e
toda linguagem de NP se reduz a SAT por uma `FinTM2` em tempo polinomial. -/
theorem B4 : ATK.Conditional.PvsNP.CookLevin ATK.ModeloPNP.modeloPNP ATK.ModeloPNP.SAT :=
  ATK.CookLevinFinal.cookLevin

end ATK.ObligationsClosed

#print axioms ATK.ObligationsClosed.B1
#print axioms ATK.ObligationsClosed.B4
