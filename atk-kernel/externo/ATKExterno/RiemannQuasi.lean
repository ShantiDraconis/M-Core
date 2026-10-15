import ATK.QuasiRiemann
import OAI.NumberTheory.DirichletL.Nonvanishing

/-!
# ATK — a quasi-hipótese de Riemann dentro do ATK, e o resíduo de RH

A OpenAI provou em Lean que `ζ(s) ≠ 0` para `Re s > 7/8`
(`OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`, `openai/math`, família 003, commit
`1581d4c`). O pacote dela usa **a mesma Mathlib do atk-kernel** (`d13f23b`, a tag `v4.34.1`),
então o teorema é importado e compilado aqui, junto com o atk-kernel, pelo mesmo kernel.

Com ele, a hipótese `QuasiRH` de `ATK.QuasiRiemann` deixa de ser hipótese:

* `quasiRH`: a quasi-RH, como teorema do ATK;
* **`rh_iff_faixa`**: `RiemannHypothesis ⟺ FaixaLivre (1/2) (7/8)`, sem hipóteses;
* `rh_de_faixa`: a faixa dá RH.

O que falta para RH é exatamente `FaixaLivre (1/2) (7/8)`: nenhum zero com `1/2 < Re s ≤ 7/8`.
Isso é o problema aberto. **Nada aqui prova RH.**
-/

namespace ATK.Externo.RiemannQuasi

open ATK.QuasiRiemann

/-- **A quasi-RH** (OpenAI), como teorema do ATK. -/
theorem quasiRH : QuasiRH :=
  fun _ hs => OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re hs

/-- **RH ⟺ não há zeros na faixa `1/2 < Re s ≤ 7/8`**, sem hipóteses. -/
theorem rh_iff_faixa : RiemannHypothesis ↔ FaixaLivre (1 / 2) (7 / 8) :=
  rh_iff_faixa_sete_oitavos quasiRH

/-- A faixa dá RH. -/
theorem rh_de_faixa (h : FaixaLivre (1 / 2) (7 / 8)) : RiemannHypothesis :=
  rh_iff_faixa.mpr h

end ATK.Externo.RiemannQuasi

#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#print axioms ATK.Externo.RiemannQuasi.quasiRH
#print axioms ATK.Externo.RiemannQuasi.rh_iff_faixa
#print axioms ATK.Externo.RiemannQuasi.rh_de_faixa
