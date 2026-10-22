import ATK.FinalRoot
import ATK.NecessidadeRH

/-!
# Portão terminal de RH — MODELO (não compilado; vira `ATK/Terminal/RH.lean`)

Falta só o PRODUTOR: uma prova, sem hipóteses, de que `D_N → 0` (a distância de Báez-Duarte).
Desde 22/10/2026 este é o produtor mínimo: é equivalente ao `RiemannHypothesis` da Mathlib pelo
teorema certificado `ATK.NecessidadeRH.rh_iff_DN`. (A O1, `UniformLogBound`, é mais forte que RH e
não é mais o alvo da linha.)
Para instalar: troque `PROVA_DO_PRODUTOR`, salve como `ATK/Terminal/RH.lean` e rode
`python3 scripts/instalar_portao.py RH`.
-/

namespace ATK.Terminal.RH

theorem produtor : Filter.Tendsto ATK.Conditional.Riemann.DN Filter.atTop (nhds 0) :=
  PROVA_DO_PRODUTOR

theorem terminal : RiemannHypothesis := ATK.NecessidadeRH.rh_iff_DN.mpr produtor

end ATK.Terminal.RH

#print axioms ATK.Terminal.RH.produtor
#print axioms ATK.Terminal.RH.terminal
