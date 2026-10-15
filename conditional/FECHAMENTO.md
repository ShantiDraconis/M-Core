# Fechamento — estado certificado e proposta (14/10/2026)

`CLOSED_MATH = false`. Este documento registra o que foi fechado no kernel, mede o que falta e
propõe a ordem de ataque. Nada aqui usa `sorry`, `axiom` ou modelos de brinquedo.

## 1. Teorema-mestre mínimo (`ATK/ObrigacoesMinimas.lean`)

```
closedMath_minimo : PontesParametricas M → Obrigacoes M → SevenStatements M
```

| Item | Antes | Agora |
|---|---|---|
| B1 Nyman–Beurling–Báez-Duarte | ponte | **provada** (`ObligationsClosed.B1`) |
| B2 FLT | ponte (`FermatLastTheorem`) | **dispensada**: Beal entra pela forma residual, sem ponte |
| B3–B7 | pontes paramétricas | continuam (dependem de L1–L5) |
| O1 | `D_N ≤ K/log(N+2)` (mais forte que RH) | `D_N → 0` ⟺ `inf D_N = 0`; ⇒ RH provado |
| O2 | forma gcd + ponte FLT | `ExclusaoResidualDescida` ⟺ Beal (provado) |
| O4 / O5 / O6–O7 | — | ⟺ P≠NP / Hodge / BSD, dadas as pontes (provado) |

`minimas_de_originais` mostra que as obrigações antigas implicam as novas: o teorema-mestre ficou
estritamente mais fraco nas hipóteses. As obrigações agora têm o tamanho exato dos problemas.

## 2. Varredura das 120 hipóteses abertas mais usadas (`hypothesis_map.json`)

Definição de cada uma lida no branch de origem.

| Categoria | Qtde | Exemplos | Situação |
|---|---|---|---|
| Descarregada agora | 1 | `Tendsto bdDistSq atTop (𝓝 0) → RiemannHypothesis` | `ATK.BDDistSqPort.criterio_bd` |
| Redundante (P01 já fechado por outra rota) | 5 | `P01VerifierPhase …`, `RawVerifierMaterialCore`, `P01Side` | sem efeito no alvo |
| Teorema publicado não formalizado (ponte) | 6 | `GrossZagierKolyvagin`, `T59FLTBeyondThree` (= FLT p ≥ 5), `P.CookLevin`, `Lefschetz11ConcreteLaw` | ver §3 |
| Ligação / modelo (L1–L5) | 8 | `CycleSpanAdapter`, `HodgeCertificationBoundary`, `Genuine4D theory` | ver §3 |
| Tipo ou parâmetro (não é hipótese) | 7 | `CycleSpanMechanics G`, `HodgeTerminalNode`, `Fin 3` | falso positivo |
| Equivalente ao problema aberto | 93 | `G21Pointwise` (= SAT ∉ P), `HodgeOpenMath ∨ …` (= payload de Hodge), `FirstRealOpenMath` (= Beal), `ConcreteLogRate` (= O1) | pesquisa |

Leitura aproximada para as famílias de diagonalização de P vs NP: todas foram lidas como formas
de SAT ∉ P. As disjunções "open/closed/negative" de Hodge **não** são tautologias: os três lados
são equivalentes ao mesmo payload.

## 3. Proposta de fechamento, em ordem

| # | Alvo | Tipo | O que exige | Efeito |
|---|---|---|---|---|
| 1 | Necessidade de Báez-Duarte: RH ⇒ `D_N → 0` | teorema publicado | **feito**: Plancherel L¹∩L², Plancherel de Mellin, fórmula espectral de `D_N`, convergência dominada, mollificador de Möbius (`NecessidadeBD`). **Falta**: RH ⇒ `EntradasNecessidade` (Littlewood: Σμ(n)n^{-s} converge em Re s > 1/2 com cota polinomial em t; Lindelöf para ζ(½+it); `J(ε) → 0` pelo produto de Hadamard) | obrigação de RH ⟺ RH no kernel; fecha as formas ⟺ de `RHConvergence` |
| 2 | B4 Cook–Levin + L2 | teorema publicado + modelo | P/NP com máquinas de Turing da Mathlib; redução de SAT; portar a prova de SAT ∈ NP do lane (P01) | O4 vira exatamente P ≠ NP com modelo genuíno — **feito em 14/10/2026**: L2 fechada pelo titular; B4 provada no kernel (`ATK.CookLevinNP.cookLevin`) |
| 3 | B3 Leray + L1 | teorema publicado + modelo | espaços de Bochner, projetor de Leray, desigualdade de energia | O3 com modelo genuíno |
| 4 | B6 Gross–Zagier–Kolyvagin + L4 | teorema publicado + modelo | função L de curvas elípticas, posto, pontos de Heegner | O6/O7 com modelo genuíno |
| 5 | B5 Lefschetz (1,1) + L3 | teorema publicado + modelo | cohomologia de Hodge (versão algébrica) | O5 com modelo genuíno |
| 6 | B7 Osterwalder–Schrader + L5 | teorema publicado + modelo | medidas em S′(ℝ⁴), positividade de reflexão | O8 com modelo genuíno |
| 7 | O1–O8 | problemas abertos | matemática nova | `CLOSED_MATH = true` |

O FLT para p ≥ 5 saiu do caminho crítico (B2 dispensada); continua útil para a forma gcd de Beal
e é objeto do projeto FLT do Imperial College.

Avanços de 15/10/2026 nos itens 3–6 (nenhum fecha o item): item 3 — taxa de Leray a partir da
desigualdade cúbica (`NSExplosao.taxa_leray`) e explosão da comparação de Riccati para dados
grandes (`explosao_comparacao`); item 4 — invariantes da fórmula refinada e modelo completo
(`BSDInvariantes`, `BSDRefinada`, `BSDTamagawaE32`), com Mordell–Weil reduzido ao Mordell–Weil fraco; item 5 —
classes de Hodge = `V_ℚ ∩ F^p` (`HodgeFiltracao`) e `H¹` do toro complexo (`HodgeToro`); item 6 —
reconstrução OS no modelo de rede (`YMReconstrucao`) e lacuna de massa sobre Wightman
(`L5Lacuna`). FLT: teorema de Sophie Germain (`SophieGermain`) e o primeiro caso para todo primo ímpar `p < 300`
(`GermainLegendre`); `A⁶ + B⁶ ≠ C²` na ponte B8 (`DarmonMerelSeis`) e Beal incondicional em `(6k, 6l, 2m)`
(`BealSeisSeisDois`); FLT para primos regulares (flt-regular, `ATK/FltRegular/`) e FLT(5), FLT(7),
FLT(11), FLT(13), FLT(17), com B2 reduzida aos primos irregulares `p ≥ 19` (`FermatRegular`); Mordell–Weil para curvas com 2-torção racional completa (`MordellWeilDois`) e cotas inferiores do
posto por 2-descida, com uma curva de posto `≥ 2` (`PostoDois`).

### Estado do item 1 (`ATK/NecessidadeBD.lean`, 18 teoremas, kernel local)

* incondicional: `|ζ(½+iτ)|²/|½+iτ|²` integrável em ℝ (`integrable_zeta_sq`); para todo
  `ε > 1/2`, `inf_N D_N ≤ (1/2π) ∫ |1 − ζ(s)/ζ(s+ε)|²/|s|²` (`iInf_DN_le_J_of_gt_half`);
* `rh_iff_DN_of_entradas`: (RH ⇒ `EntradasNecessidade`) ⇒ (RH ⟺ `D_N → 0`);
* `rh_of_entradas`: `EntradasNecessidade` ⇒ RH — as entradas têm a força de RH; o que falta é
  a análise clássica sob RH (Titchmarsh cap. 14), não um passo de Plancherel.

## 4. O que não conta como fechamento

`axiom`, `sorry`, modelos de brinquedo (`ns_toy_model_vacuous`, `pnp_toy_model_vacuous`),
trocar o enunciado por um mais fraco, e minimização feita dentro do kernel
(`HypothesisCalculus.minimal_basis_eq_empty_of_true`: com alvo verdadeiro a base minimal é ∅).
