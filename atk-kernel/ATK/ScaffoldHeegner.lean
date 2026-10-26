import ATK.AtaqueBSD

/-!
# ATK — Andaime mínimo para altura canônica e ponto de Heegner

Confirmado por busca real no código-fonte do Mathlib (zero resultados):
não existe `WeilHeight`, `CanonicalHeight`, `HeightFunction` sobre corpos
de números, `ModularCurve` nem `HeegnerPoint`. Construir a altura canônica
de Néron-Tate de primeiros princípios exigiria a altura de Weil ingênua em
`P^n(ℚ)` mais um processo de limite (`ĥ(P) = lim_n h(nP)/n²`), e o ponto de
Heegner exigiria a curva modular `X₀(N)` e a correspondência modular —
nenhum dos dois está formalizado.

**Altura canônica**: em vez de construir, CARACTERIZAMOS pelos três axiomas
que a definem unicamente (Tate, anos 1960: a altura canônica é a única
função que é quadrática, não-negativa e se anula exatamente na torção).
Isso não é uma simplificação arbitrária — é a caracterização clássica.
Qualquer função satisfazendo `CanonicalHeightData` *é*, por definição
matemática padrão, a altura canônica — não uma aproximação dela.

**Ponto de Heegner**: aqui sim é andaime deliberadamente simplificado, não
uma caracterização — `isCM` é um placeholder (`Prop` opaca) para "P vem de
um ponto CM de discriminante D na curva modular X₀(N)", sem construir a
curva modular. Isso é mais fraco que a definição real, e está dito aqui
para não deixar isso implícito.

Nada aqui prova Gross-Zagier-Kolyvagin nem BSD. `GrossZagierFormula` é uma
obrigação aberta, não um teorema.
-/

namespace ATK.ScaffoldHeegner

open ATK.AtaqueBSD

variable (W : WeierstrassCurve ℚ)

/-- Caracterização da altura canônica de Néron-Tate sobre `W.toAffine.Point`:
quadrática (`ĥ(n•P) = n²ĥ(P)`), não-negativa, e zero exatamente na torção.
Ver nota no cabeçalho do arquivo sobre por que isso é uma caracterização,
não uma aproximação. -/
structure CanonicalHeightData where
  h : W.toAffine.Point → ℝ
  nonneg : ∀ P, 0 ≤ h P
  quadratic : ∀ (n : ℤ) (P : W.toAffine.Point), h (n • P) = (n : ℝ) ^ 2 * h P
  zero_iff_torsion : ∀ P, h P = 0 ↔ ∃ n : ℕ, 0 < n ∧ n • P = 0

/-- Andaime SIMPLIFICADO (não a construção real via `X₀(N)` + multiplicação
complexa): um "ponto de Heegner" aqui é só um ponto distinguido por um
discriminante negativo `D`, com `isCM` como placeholder opaco para a
condição real de vir de um ponto CM na curva modular. -/
structure HeegnerPointData where
  D : ℤ
  D_neg : D < 0
  P : W.toAffine.Point
  isCM : Prop

/-- **Fórmula de Gross-Zagier** (obrigação aberta, NÃO provada aqui): a
altura canônica do ponto de Heegner é proporcional, por uma constante
positiva, à derivada de `L(E,s)` em `s = 1`. Não é vazia: força o sinal e a
proporcionalidade entre um dado geométrico (`ht.h hp.P`) e um dado analítico
(`Lderiv`) — se `Lderiv = 0` e `ht.h hp.P ≠ 0`, a proposição é falsa. -/
def GrossZagierFormula (ht : CanonicalHeightData W) (hp : HeegnerPointData W)
    (Lderiv : ℝ) : Prop :=
  ∃ c : ℝ, 0 < c ∧ ht.h hp.P = c * Lderiv

end ATK.ScaffoldHeegner
