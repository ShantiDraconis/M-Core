# Os sete enunciados oficiais no kernel

Arquivo único: `atk-kernel/ATK/EnunciadosOficiais.lean` (`Sete C Corr` = os sete juntos).

| Problema | Definição Lean | Sobre o quê | Fidelidade |
|---|---|---|---|
| Riemann | `RH := RiemannHypothesis` | `riemannZeta` da Mathlib | **REAL** |
| Beal | `Beal := BealConjecture` | ℕ, primos | **REAL** |
| Navier–Stokes | `NS := NSReal` | Clay (A): `ℝ³ = EuclideanSpace ℝ (Fin 3)`, dado de Schwartz com divergência nula, solução `C^∞` global com energia limitada (`ATK.LigacaoNS`) | **REAL** |
| P vs NP | `PNP := classeP ≠ classeNP` | `Turing.FinTM2` em tempo polinomial (`ATK.LigacaoPNP`) | **REAL** |
| BSD | `BSD := ClayBSDCompleto` | posto de Mordell–Weil e fórmula refinada, `WeierstrassCurve.LFunction` (`ATK.LigacaoBSD`, `ATK.BSDRefinada`) | **REAL** |
| Hodge | `Hodge C := HodgeOficial C` | `ATK/HodgeOficial.lean` | **REAL relativo a 3 construções ausentes** |
| Yang–Mills | `YM Corr := YMClay Corr` | `ATK/YMOficial.lean` | **núcleo REAL + correspondência como parâmetro** |

## Hodge (`ATK/HodgeOficial.lean`)

Real, com objetos da Mathlib:
- **Variedade projetiva não singular sobre ℂ:** um esquema `X → Spec ℂ`, liso de dimensão relativa `n` (`SmoothOfRelativeDimension`), com imersão fechada em `ℙᴺ_ℂ = Proj ℂ[x₀,…,x_N]`.
- **Ciclos algébricos:** `AlgebraicCycle X ℚ`, em codimensão `p` (`dim 𝒪_{X,x} = p`).
- **Cohomologia:** `H^{2p}(T, ℚ) = Hom(H_{2p}(T; ℚ), ℚ)`, com a homologia singular da Mathlib.
- **Classe de Hodge:** vetor racional em `H^{p,p}` de uma estrutura de Hodge pura de peso `2p`.

Ausente da Mathlib v4.34.1, e por isso dado explícito em `ConstrucoesHodge`:
1. analitificação `X ↦ X(ℂ)`;
2. decomposição de Hodge (teoria de Kähler);
3. classe de ciclo.

Teste: com `cl = 0`, o enunciado vira "toda classe de Hodge é 0" (`hodge_cl_zero_iff`). O enunciado só é a conjectura de Hodge com as construções genuínas.

## Yang–Mills (`ATK/YMOficial.lean`)

Real:
- **`CompactaSimples 𝔤`:** álgebra de Lie real simples (`LieAlgebra.IsSimple`) de tipo compacto (forma de Killing negativa definida).
- **Teoria de Wightman em ℝ⁴:** `ATK.L5Base`.
- **`GapMassa W Δ`:** espectro de energia-momento em `{0} ∪ {p⁰ ≥ 0, p² ≥ Δ²}`.
- **`NaoTrivial`:** o campo centrado não obedece à fórmula de Wick, ou seja, não é um campo livre generalizado.
- **`tr F²`:** invariante de calibre (`trF2_invariante`).

O texto do Clay **não define formalmente** "os campos correspondem a Yang–Mills", por isso esse critério (`Corr`) é um parâmetro. Sem ele, `𝔤` não entra na teoria (`nucleo_sem_g`).

Testes:
- `trivial_gap`: a teoria trivial tem lacuna de massa.
- `trivial_gaussiana`: a teoria trivial é gaussiana.

Logo, cada cláusula é necessária.

## Estado

`sete_condicional` deriva `Sete C Corr` das lacunas reais (`ClosedMathReal.Lacunas`), das lacunas de Hodge no modelo `C` e de YM como hipótese. Não há teorema `Sete` sem hipóteses: **CLOSED_MATH = false**, OPEN_MATH inalterado.
