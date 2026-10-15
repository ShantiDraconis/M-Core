# ATK — Pontes, ligações e fechamentos: estado de cada um

Este arquivo responde, item por item, à pergunta "o que falta para provar todas as pontes,
ligações e fechamentos". Três categorias, que não devem ser confundidas:

* **Ponte**: teorema publicado que entra no kernel como hipótese com nome (nunca `axiom`).
  Prová-la é formalizar matemática conhecida — às vezes semanas, às vezes décadas de teoria.
* **Ligação**: construção, sobre objetos da Mathlib, do modelo genuíno de um problema (a prova de
  que o enunciado formal é o enunciado do Clay).
* **Fechamento**: as obrigações O1–O8 — os próprios problemas em aberto. Provar um fechamento é
  resolver o problema; nenhuma formalização faz isso sozinha.

`OPEN_MATH = true`, `CLOSED_MATH = false`.

## Fechamentos (O1–O8) — problemas em aberto

| Id | Enunciado | Estado |
|---|---|---|
| O1 | `D_N → 0` (família de Báez-Duarte) — equivalente a RH | aberto |
| O2 | resíduo de Beal (`ExclusaoResidualDescida`) — equivalente a Beal | aberto |
| O3 | cota a priori da enstrofia (Navier–Stokes, enunciado A) | aberto (rota G5 refutada) |
| O4 | SAT ∉ P — equivalente a P ≠ NP dada B4 | aberto |
| O5 | Hodge em codimensão média | aberto |
| O6 | BSD para posto analítico ≥ 2 | aberto |
| O7 | Ш finito e fórmula do termo líder | aberto |
| O8 | Yang–Mills 4D construtivo com lacuna | aberto |

Nenhum destes é atacável por formalização apenas. O programa de ataque (`ATAQUE.md`) trabalha em
volta deles.

## Pontes do teorema-mestre (B1–B8)

| Id | Teorema | Estado | O que falta | Escala |
|---|---|---|---|---|
| B1 | Nyman–Beurling–Báez-Duarte | ✅ provada (`ObligationsClosed.B1`) | a recíproca RH ⇒ `D_N → 0` precisa de Littlewood/Lindelöf sob RH e do produto de Hadamard (`NecessidadeBD`) | meses |
| B2 | FLT para `p ≥ 5` | 🟡 primos regulares, `p ∈ {5, 7, 11, 13, 17}`, caso I para `p < 300` (`FermatRegular`, `GermainLegendre`); dispensada no teorema-mestre mínimo | Wiles–Taylor (projeto FLT do Imperial College) | anos |
| B3 | critério de explosão de Leray + teoria local | ⬜ (`NSExplosao` dá a taxa de Leray a partir da desigualdade cúbica) | existência local de soluções suaves em ℝ³, unicidade, continuação; desigualdade de enstrofia (Sobolev) | meses–anos |
| B4 | Cook–Levin | ✅ provada (`CookLevinNP.cookLevin`) | — | — |
| B5 | Lefschetz (1,1) | ⬜ (metade linear: `HodgeFiltracao`) | cohomologia de variedades projetivas, sequência exponencial | anos |
| B6 | Gross–Zagier–Kolyvagin | ⬜ | formas modulares, pontos de Heegner, sistemas de Euler | décadas de teoria |
| B7 | reconstrução de Osterwalder–Schrader | ⬜ (miniatura 2D: `YMReconstrucao`; positividade abstrata: `BasePositividadeReflexao`) | medidas em `S′(ℝ⁴)`, reconstrução do espaço de Hilbert | anos |
| B8 | Darmon–Merel | ⬜ (caso `n = 6` via FLT(3): `DarmonMerelSeis`) | modularidade de curvas de Frey | anos |

## Ligações (L1–L5)

| Id | Modelo | Estado | O que falta |
|---|---|---|---|
| L1 | Navier–Stokes em ℝ³ | ✅ fechada (`LigacaoNS.modeloNS`) | — |
| L2 | P/NP sobre `Turing.FinTM2` | ✅ fechada (`ModeloPNP`) | — |
| L3 | cohomologia de Hodge de variedades projetivas | ⬜ não existe na Mathlib | de Rham/Betti de variedades, decomposição de Hodge |
| L4 | BSD sobre `WeierstrassCurve.LSeries` | 🟡 posto ✅ (`LigacaoBSD`); fórmula refinada enunciada (`BSDRefinada`); hipóteses `Modularidade` e `MordellWeil` | `MordellWeil` geral = Mordell–Weil fraco para toda `E/ℚ` (feito para 2-torsão completa, `MordellWeilDois`); `Modularidade` = Wiles/BCDT |
| L5 | Wightman/OS em ℝ⁴ | 🟡 axiomas e lacuna definidos (`L5Base`, `L5Lacuna`) | campos de calibre, `IsQuantumYM` |

## Pontes do programa de ataque

| Id | Teorema | Estado | O que falta |
|---|---|---|---|
| **P1** | modularidade de `y² = x³ − x` com sinal `+1`: `g(1/x) = x² g(x)` | ✅ **provada** (`PonteModularCurva32.ponteModular_curva32`): caráter de Hecke de `ℚ(i)` (`BaseGaussPrimario`), `a_p = π + π̄` (`BaseGaussCurva32`), duas fatorações da soma dupla e as equações funcionais dos núcleos de Hurwitz da Mathlib | — |
| **P2** | `\|aₙ\| ≤ n` para `y² = x³ − x` | ✅ **provada** (`PonteFatoresCurva32.cotaCoef_curva32`): cota de Hasse–Gauss (`BaseHasseCurva32`), recursão de Hecke e multiplicatividade (`PonteCoefCurva32`), fatores locais da Mathlib (P2a) | — |
| P2a | os coeficientes `WeierstrassCurve.LFunction` da Mathlib são os padrão (`a_{2^k} = 0`; `a_{p^k} = c_k(a_p, p)`, `a_p = p + 1 − #E(𝔽_p)`) | ✅ **provada** (`PonteFatoresCurva32.fatoresPadrao`) | — |
| **PemPpoly** | `P ⊆ P/poly` (Savage 1972) | ✅ **provada** (`PemPpoly.pemPpoly`): tableau determinístico em camadas sobre `Turing.FinTM2` (`CircuitoCamadas`, lema de moldura de `CookLevinBase`), tamanho polinomial | — |
| — | ponte de Leray em `AtaqueNS` | = B3 | — |

Com P1 e P2 provadas, **a parte do posto de BSD para `y² = x³ − x` não depende de nenhuma
ponte**: `PonteModularCurva32.bsdConjecture_E32 : L4Base.BSDConjecture L4Base.E32` —
`L(E, s)` converge em `Re s > 3/2`, tem continuação inteira (existe e é única), `L(E, 1) ≠ 0` e a
ordem `0` é o posto de Mordell–Weil. É o enunciado do Clay (`L4Base.clayBSD_iff`) restrito a uma
curva; o problema do milênio (todas as curvas) continua aberto. P2a foi desdobrada sem matemática
nova: corpo residual `ℤ_v/𝔪 ≅ 𝔽_p` (via `ℤ_v ≅ ℤ_p`), produto de Euler da Mathlib em `p^k`
(Northcott), descida do modelo minimal a `ℤ_v` em `p` ímpar com `#Ẽ(𝔽_p) = p + 1 + Σ χ(x³ − x)`,
e redução aditiva em `2` (`2` uniformizador de `ℤ_2`, paridade de `v(Δ_min) = 6 − 12 v(u)`,
`c₄³ = 1728 Δ` com `c₆ = 0`).

## Ordem proposta

1. ~~**P2a**~~, ~~**P1**~~ ✅ provadas: BSD (posto) para `y² = x³ − x` sem pontes.
2. ~~**PemPpoly**~~ ✅ provada: `NP ⊄ P/poly ⇒ P ≠ NP` no modelo genuíno, sem pontes (`PemPpoly.p_ne_np_de_naoPpoly`).
3. **`MordellWeil` geral** via 2-descida sobre a álgebra cúbica (meses; a Mathlib tem grupo de
   classes finito e o teorema das unidades de Dirichlet): fecha uma das duas hipóteses de L4.
4. **B1 recíproca** (RH ⇒ `D_N → 0`; meses).
5. B3, B5–B8, L3, L5: anos de teoria; acompanhar os projetos externos (FLT, cohomologia).
