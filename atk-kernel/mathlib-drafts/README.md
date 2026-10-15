# Rascunhos para a Mathlib (ligações L3–L5)

Cinco arquivos no estilo da Mathlib, na ordem combinada para os PRs: **L4 → L3 PR1 → L3 PR2 → L5**.
Cada um compila sozinho contra a Mathlib v4.34.1 (conferido com `lake env lean` neste ambiente),
sem `sorry`, `admit` nem `axiom`. Os PRs na Mathlib são abertos pelo titular. Neste repositório os
mesmos conteúdos, com teoremas auditados, estão em `ATK/L4Base.lean`, `ATK/L3Base.lean` e
`ATK/L5Base.lean`.

| ordem | arquivo | caminho sugerido na Mathlib | conteúdo | exemplo / teste |
|---|---|---|---|---|
| 1 (L4) | `BSD.lean` | `Mathlib/AlgebraicGeometry/EllipticCurve/BSD.lean` | `WeierstrassCurve.LFunctionContinued` (inteira, igual a `LSeries` em `Re s > 3/2`), unicidade (`Subsingleton`), `analyticRank`, `mordellWeilRank`, `BSDConjecture`, `L_one_eq_zero_iff`, `bsdConjecture_iff_of_mordellWeilRank_eq_zero` | `y² = x³ − x` é elíptica (`Δ = 64`) |
| 2 (L3 PR1) | `Kahler.lean` | `Mathlib/Analysis/Complex/Kahler.lean` | `HermitianStructure` (produto interno real invariante por `I`), forma fundamental alternada e `I`-invariante, `LocalKahlerMetric` (forma fundamental fechada pela `extDerivWithin` da Mathlib) | métrica plana de `ℂ`: `ω(1, I) = 1` e é de Kähler |
| 3 (L3 PR2) | `HodgeStructure.lean` | `Mathlib/LinearAlgebra/HodgeStructure.lean` | `HodgeStructure V n` (`ℂ ⊗[ℚ] V = ⨁ H^{p,n−p}`, simetria de Hodge), `IsHodgeClass`, `hodgeClasses` (subespaço racional), `pure`, `tate` | `ℚ(−1)`: `1` é classe de Hodge, `H^{2,0} = 0` |
| 4 (L5) | `Wightman.lean` | `Mathlib/Analysis/Distribution/Wightman.lean` | Minkowski, cone futuro, Lorentz restrito, `QFT.WightmanQFT H` (representação unitária, vácuo, domínio, campo temperado, hermiticidade, covariância, localidade, condição espectral via `𝓕`, ciclicidade) | a teoria trivial satisfaz os axiomas; `∫ 𝓕 g = g 0` |
| 5 (L4, 15/10) | `CanonicalHeight.lean` | `Mathlib/NumberTheory/Height/CanonicalHeight.lean` | `Point.canonicalHeight` (`ĥ = lim h(2ⁿP)/4ⁿ`) sobre qualquer corpo com `AdmissibleAbsValues`: existência do limite, `ĥ − h` limitada, `ĥ ≥ 0`, paralelogramo exato, `ĥ(nP) = n²ĥ(P)`, `ĥ(P) = 0 ↔` torção (com Northcott), emparelhamento de Néron–Tate simétrico e aditivo | é o passo natural depois de `approx_parallelogram_law` (já na Mathlib); no repositório, `ATK/BSDInvariantes.lean` |

Observações:

* L4: o semiplano é `3/2`, não `1` — `LSeries` da Mathlib vale `0` fora da somabilidade absoluta, e
  com `1` a estrutura seria vazia para as curvas elípticas verdadeiras.
* L3 PR1: a versão global (variedade de Kähler) depende de formas diferenciais em variedades, que a
  Mathlib ainda não tem; o arquivo dá o modelo local (cartas).
* L5: a teoria trivial mostra que os axiomas são consistentes; o problema do Clay pede uma teoria
  de Yang–Mills não trivial com lacuna de massa, que ainda não está expressa.

Nada aqui prova Hodge, BSD ou Yang–Mills. CLOSED_MATH continua false.
