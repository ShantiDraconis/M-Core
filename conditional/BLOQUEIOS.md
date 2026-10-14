# Bloqueios — L3, L5 (`BLOQUEADA_POR_MATHLIB`) e a parte refinada de L4

Conferido em 14/10/2026 contra a Mathlib pinada do kernel (`v4.34.1`, rev `d13f23b7`).

Uma ligação só fecha seguindo o mesmo padrão de L1 e L2:

1. modelo construído só com objetos da Mathlib;
2. testes de sanidade que mostram que o modelo não é de brinquedo;
3. teorema de fidelidade em relação ao enunciado oficial;
4. CI verde, só os 3 axiomas padrão e revisão humana registrada.

Enquanto a fundação não existir, a ligação fica bloqueada. **Nenhum `axiom` é acrescentado para
"desbloquear":** o detector é o próprio CI, que exige 100 % dos teoremas com
`{propext, Classical.choice, Quot.sound}`.

## L3 — Hodge

**O que a Mathlib já tem**

* variedades sobre `ℂ` (`Geometry/Manifold/Complex.lean`), com só dois teoremas: funções
  holomorfas em variedades compactas são constantes;
* formas diferenciais e `extDeriv` em espaços normados (`Analysis/Calculus/DifferentialForm/Basic.lean`);
* esquemas, `Proj` (`AlgebraicGeometry/ProjectiveSpectrum/`), morfismos lisos e próprios;
* ciclos algébricos num esquema (`AlgebraicGeometry/AlgebraicCycle/Basic.lean`).

**O que falta, em ordem**

1. Cohomologia com coeficientes racionais de uma variedade: de Rham em variedades ou singular com
   `ℚ`, sem a qual `H^{2p}(X, ℚ)` não existe.
2. Métricas de Kähler e a estrutura complexa nas formas: tipos `(p, q)` e cohomologia de Dolbeault.
3. Decomposição de Hodge `H^n(X, ℂ) = ⊕_{p+q=n} H^{p,q}` para `X` projetiva lisa (um teorema profundo).
4. Variedade analítica associada a um esquema projetivo liso sobre `ℂ` (GAGA, pelo menos a parte
   de objetos).
5. Mapa de classe de ciclo: ciclos algébricos → `H^{2p}(X, ℚ) ∩ H^{p,p}`.

**Primeiro passo formalizável**: só depois de 1 e 2. Antes disso nem `HodgeConjecture : Prop` pode
ser escrita com os objetos reais.

## L4 — BSD

**O que a Mathlib já tem** (mais do que se supunha)

* curvas de Weierstrass, modelos minimais, redução e o grupo de pontos
  (`AlgebraicGeometry/EllipticCurve/`);
* **a função L de Hasse–Weil como série de Dirichlet formal**, com fatores de Euler locais sobre
  corpos de números (`WeierstrassCurve.LFunction`, `WeierstrassCurve.LSeries` em
  `EllipticCurve/LFunction.lean`);
* formas modulares e **suas funções L inteiras** (`ModularForm.L`, `differentiable_L` em
  `NumberTheory/ModularForms/LFunction.lean`);
* altura ingênua, Northcott e torção finita (`NumberTheory/Height/EllipticCurve.lean`), além do
  lema de descida usado no teorema de Mordell–Weil (`GroupTheory/Descent.lean`).

**O que falta**

1. O teorema de Mordell–Weil (fraco e completo). O posto pode ser definido sem ele, mas a sua
   finitude, não.
2. A modularidade (Wiles; Breuil–Conrad–Diamond–Taylor): `L(E, s) = L(f, s)`, que dá a continuação
   analítica até `s = 1`.
3. Para a parte refinada: altura de Néron–Tate e regulador, período real `Ω_E`, números de
   Tamagawa `c_p` e o grupo de Tate–Shafarevich `Ш` (cohomologia de Galois). Nada disso existe.

**Feito**: a parte do posto já está no kernel (`ATK/LigacaoBSD.lean`, status
`PARTE_DO_POSTO_NO_KERNEL`). `ClayBSD` exige que exista uma continuação inteira de
`WeierstrassCurve.LSeries E` com ordem em `1` igual ao posto. A modularidade e Mordell–Weil
entram como hipóteses explícitas.

**Bloqueada**: a fórmula refinada (item 3 acima). Como o portão exige `BSDFull` (posto e fórmula
refinada), L4 não fecha antes dela.

## L5 — Yang–Mills

**O que a Mathlib já tem**

* grupos de Lie, fibrados vetoriais e fibrados (`Geometry/Manifold/Algebra/LieGroup.lean`,
  `VectorBundle`, `FiberBundle`);
* distribuições temperadas e espaços de Sobolev (`Analysis/Distribution/TemperedDistribution.lean`,
  `Sobolev.lean`), a matéria-prima dos axiomas de Wightman e de Osterwalder–Schrader.

**O que falta**

1. Fibrados principais com conexão e curvatura; ação de Yang–Mills `∫ |F_A|²`.
2. Axiomas de Wightman e de Osterwalder–Schrader (QFT em ℝ⁴) e o teorema de reconstrução (ponte B7).
3. Uma teoria quântica de Yang–Mills construída para `G` compacto simples, com Hamiltoniano e gap
   de massa. Isto é o próprio problema do milênio, não uma fundação.

**Primeiro passo formalizável**: os axiomas de Wightman/OS como estruturas sobre as distribuições
temperadas da Mathlib, com a teoria livre como teste de sanidade (gap 0, rejeitada pelo enunciado).
Isso permite *escrever* `ClayYM`, mas não construir o modelo genuíno: a ligação L5 exige a teoria
de Yang–Mills quântica, que não existe em lugar nenhum.

## Resumo

| Ligação | Estado | Primeiro passo possível hoje |
|---|---|---|
| L3 Hodge | `BLOQUEADA_POR_MATHLIB` | nenhum antes da cohomologia racional e dos tipos `(p, q)` |
| L4 BSD | `PARTE_DO_POSTO_NO_KERNEL`; a fórmula refinada está bloqueada | Néron–Tate e regulador, Ω, Tamagawa, Ш |
| L5 Yang–Mills | `BLOQUEADA_POR_MATHLIB` | axiomas de Wightman/OS sobre distribuições temperadas |

`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`. Estes bloqueios são o estado da biblioteca, não
uma falha do processo.
