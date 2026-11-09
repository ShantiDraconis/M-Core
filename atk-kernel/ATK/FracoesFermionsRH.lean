import ATK.ZeroClasses.PontesRH
import ATK.FracoesFermions

/-!
# ATK — RH no gás de primos fermiônico (rodada 107)

Junta o critério de `ATK.FracoesFermions` com a abscissa `c` da rodada 102 (`ATK.ZeroClasses.PontesRH`):

* `semZeros_iff`: as duas definições de "sem zeros em `Re s > θ`" coincidem.
* **`rh_iff_continuaAte`**: **RH ⟺ a função de partição fermiônica `1/ζ` continua holomorfa até `Re s > ½`**.
* `rh_iff_traco`: RH ⟺ existe `F` holomorfa em `Re s > ½` igual a `Σ μ(n) n^{−s}` em `Re s > 1`.
* **`c_eq_continua`**: `c = inf {θ : 1/ζ continua até Re s > θ}` — a abscissa sem zeros é a abscissa de
  holomorfia do traço fermiônico; `continuaAte_iff_c`: `1/ζ` continua até `θ` ⟺ `c ≤ θ`.

Classificação: **reformulação**. RH continua `OPEN_MATH`: provar a continuação até `½` é provar RH.
-/

open Complex
open scoped LSeries.notation ArithmeticFunction.Moebius

namespace ATK.Fracoes.FermionsRH

open ATK.Fracoes.Fermions

/-- As duas definições de "sem zeros em `Re s > θ`" coincidem. -/
theorem semZeros_iff (θ : ℝ) : ATK.ZeroClasses.PontesRH.SemZeros θ ↔ SemZeros θ := Iff.rfl

/-- **RH ⟺ `1/ζ` continua holomorfa até `Re s > ½`.** -/
theorem rh_iff_continuaAte : RiemannHypothesis ↔ ContinuaAte (1 / 2) :=
  ATK.ZeroClasses.PontesRH.semZeros_meio_iff_rh.symm.trans
    ((semZeros_iff _).trans (semZeros_iff_continuaAte _))

/-- RH dita com o traço fermiônico `Σ μ(n) n^{−s}`. -/
theorem rh_iff_traco : RiemannHypothesis ↔
    ∃ F : ℂ → ℂ, DifferentiableOn ℂ F {s | 1 / 2 < s.re} ∧ ∀ s : ℂ, 1 < s.re → F s = LSeries ↗μ s :=
  rh_iff_continuaAte.trans (continuaAte_iff_traco _)

/-- `1/ζ` continua até `θ` ⟺ `c ≤ θ`. -/
theorem continuaAte_iff_c (θ : ℝ) : ContinuaAte θ ↔ ATK.ZeroClasses.PontesRH.c ≤ θ :=
  (semZeros_iff_continuaAte θ).symm.trans ((semZeros_iff θ).symm.trans
    (ATK.ZeroClasses.PontesRH.semZeros_iff θ))

/-- **A abscissa sem zeros é a abscissa de holomorfia do traço fermiônico.** -/
theorem c_eq_continua : ATK.ZeroClasses.PontesRH.c = sInf {θ : ℝ | ContinuaAte θ} := by
  unfold ATK.ZeroClasses.PontesRH.c
  congr 1
  ext θ
  exact (semZeros_iff θ).trans (semZeros_iff_continuaAte θ)

end ATK.Fracoes.FermionsRH

#print axioms ATK.Fracoes.FermionsRH.semZeros_iff
#print axioms ATK.Fracoes.FermionsRH.rh_iff_continuaAte
#print axioms ATK.Fracoes.FermionsRH.rh_iff_traco
#print axioms ATK.Fracoes.FermionsRH.continuaAte_iff_c
#print axioms ATK.Fracoes.FermionsRH.c_eq_continua
