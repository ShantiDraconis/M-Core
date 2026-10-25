# ATK — Programa de ataque

`BASES.md` mapeia a infraestrutura que falta na Mathlib. Este arquivo organiza o **ataque**: para
cada problema, uma aposta de pesquisa (a rota que parece mais promissora, com chance baixa) e uma
escada de marcos que o kernel consegue certificar de qualquer jeito. Cada marco é um alvo Lean
com nome; as reduções entre alvos são teoremas certificados no CI.

## Princípios

1. **Reformular não é avançar.** Uma equivalência nova (como `D∞ = 0 ⟺ RH`, `ATKIBagchi`) é uma
   ponte, não progresso sobre o núcleo. Um ataque precisa trazer informação nova sobre o objeto.
2. **Usar o computador onde ele tem vantagem real:** provas assistidas por computador com
   aritmética intervalar certificada (`BaseIntervalar`), busca exaustiva, verificação de casos.
3. **O CI é o juiz.** Sem `sorry`, `admit` ou `axiom` novo; pontes publicadas entram como
   hipóteses com nome (`PonteModular`, `CotaCoef`, `PemPpoly`, …); as flags nunca são editadas à
   mão. `OPEN_MATH = true`, `CLOSED_MATH = false`.

Legenda: ✅ certificado no CI · 🟡 parcial · ⬜ próximo.

---

## Frente 1 — BSD (a que chega mais longe)

**Aposta.** Provar a parte do posto de BSD para curvas concretas, calculando os dois lados de
forma independente: o posto pela descida, `L(E, 1)` pela equação funcional modular.

| Marco | Enunciado | Estado | Alvo Lean |
|---|---|---|---|
| F1.1 | **BSD (posto) para `y² = x³ − x`** — **provada sem pontes** (`PonteModularCurva32.bsdConjecture_E32`: `L4Base.BSDConjecture E32`, com existência e unicidade da continuação); antes, módulo as pontes P1 (modularidade com sinal `+1`, forma `g(1/x) = x² g(x)`) e P2 (`\|aₙ\| ≤ n`, **provada**: F1.3'): toda continuação `G` de `L(E, s)` tem `G(1) ≠ 0` e ordem 0 = posto | ✅ | `AtaqueBSD.bsd_posto_curva32` |
| F1.2 | **Critério de não anulação**: sinal `+1`, `\|aₙ\| ≤ n` e `N < (2π/log 2)² ≈ 82` ⇒ `L(E, 1) ≠ 0` (FE-pair de peso 2, dobra de Mellin, série rápida) | ✅ | `AtaqueBSD.L1_ne_zero` |
| F1.3 | P2 para `y² = x³ − x`: cota de Hasse–Gauss sobre 𝔽_q, recursão de Hecke, multiplicatividade | ✅ | `BaseHasseCurva32.hasse_curva32`, `PonteCoefCurva32.cotaCoef_de_fatores` |
| F1.3'' | **P1 provada**: caráter de Hecke de `ℚ(i)` (`aₙ = Σ_{α primário, Nα = n} α`), `a_p = π + π̄` (Gauss), equação funcional pela soma dupla e núcleos de Hurwitz | ✅ | `BaseGaussCurva32.coef_gauss`, `PonteModularCurva32.ponteModular_curva32` |
| F1.3' | P2a: desdobrar `WeierstrassCurve.LFunction` (corpo residual, modelo minimal, contagem de pontos, produto de Euler) ⇒ **`\|aₙ\| ≤ n` incondicional; BSD (posto) para `y² = x³ − x` módulo só P1** | ✅ | `PonteFatoresCurva32.fatoresPadrao`, `cotaCoef_curva32`, `bsd_posto_curva32_modP1` |
| F1.4 | Fórmula refinada completa para `y² = x³ − x` (`Ω`, `c₂`, `Ш[2] = 0`), com `BSDRefinada` | ⬜ | `formula_E32_iff` |
| F1.5 | Outras curvas de condutor `< 82` e sinal `+1` (posto 0 pela 2-descida de `MordellWeilDois`) | ⬜ | `L1_ne_zero` |
| F1.6 | **Mordell–Weil para toda curva elíptica sobre `ℚ`** (a hipótese `MordellWeil` de L4): `K⟮S, 2⟯` finito para corpos de números, 2-descida sobre o corpo de decomposição da cúbica, descida de Galois | ✅ | `MordellWeilGeral.mordellWeil`, `LigacaoBSDMW.bsdFull_iff_mod` |

## Frente 2 — Navier–Stokes (a aposta de maior retorno)

**Aposta.** Explosão do problema sem força por prova assistida por computador (método de
Chen–Hou: perfil quase autossimilar, estabilidade linear certificada, estabilidade não linear).
A regularidade exigiria usar a estrutura fina do termo não linear (barreira de Tao, 2016).

| Marco | Enunciado | Estado | Alvo Lean |
|---|---|---|---|
| F2.1 | As duas saídas: `Explosao ⟺ ¬ClayA`; o que um certificado de explosão precisa exibir (enstrofia ilimitada antes de `T`, com a ponte de Leray); regularidade ⟺ cota a priori | ✅ | `AtaqueNS.explosao_iff`, `explosao_enstrofia`, `regularidade_de_cota` |
| F2.2 | Aritmética intervalar certificada sobre ℚ (soma, produto, `exp` com resto de Lagrange, `π`) | ✅ | `BaseIntervalar` |
| F2.3 | Galerkin, Poincaré, `L²_σ`, Leray em `L²` (camadas N1–N3b de `BASES.md`) | ✅ | `BaseGalerkin*`, `BaseToroPoincare`, `BaseLerayL2` |
| F2.4 | Equação do perfil autossimilar (Euler com fronteira ou em `T³`) e resíduo certificado | ⬜ | — |
| F2.5 | Estabilidade linear certificada do perfil (cotas espectrais intervalares) | ⬜ | — |
| F2.6 | Soluções fracas de Leray (N4–N5) | ⬜ | — |
| F2.7 | **Existência local de soluções suaves em ℝ³** (Leray; Kato–Fujita) no modelo genuíno: dado de Schwartz de divergência nula ⇒ (u, p) suaves em ℝ³ × [0, T) com energia e enstrofia finitas | ✅ | `NSExistencia.existenciaLocal` |
| F2.8 | **Desigualdade de energia** ∫|u(t)|² ≤ ∫|u₀|² na classe de Fourier (o termo não linear não troca energia: ∫⟪â, N(â, â)⟫ = 0) e redução de B3 com classe dependente do dado | ✅ | `NSEnergia.energia_decresce`, `NSClasse.desigualdadeEnergiaF`, `NSClasse.existenciaLocalF`, `NSClasse.b3_de_classeD` |
| F2.9 | **Continuação com enstrofia limitada** (critério de Leray) na classe de Fourier: estimativas de energia de ordem alta no lado de Fourier (Cauchy–Schwarz trilinear, interpolação L¹, Gronwall), cota pontual uniforme, reinício e colagem | ✅ | `NSContinuacao.continuacaoF` |
| F2.10 | Unicidade fraca–forte (classe de Fourier contra qualquer solução suave; o enunciado que falta para B3). Em curso: formulação fraca sem pressão para qualquer solução suave (U-1) e sua extensão a rotacionais de campos de Schwartz (U-2) | ⬜ | `NSFraca.formulacao_fraca`, `NSCorte.formulacao_fraca_rot` (passos intermediários) |

## Frente 3 — Hipótese de Riemann

**Aposta.** Nenhuma rota conhecida tem alavanca; a constante de de Bruijn–Newman (`0 ≤ Λ ≤ 0,22`,
RH ⟺ `Λ = 0`) é o alvo quantitativo mais honesto. **Escada certificável:** Hardy, zeros
verificados, Levinson.

| Marco | Enunciado | Estado | Alvo Lean |
|---|---|---|---|
| F3.1 | `Ξ(0) > 0`, fórmula de Riemann para Ξ | ✅ | `BaseRiemannXiSinal`, `BaseRiemannTeta` |
| F3.2 | **Redução de Hardy**: infinitas trocas de sinal de Ξ ⇒ infinitos zeros na reta | ✅ | `AtaqueRH.hardy_of_trocas` |
| F3.3 | **Certificado de zero**: cotas para `I(t) = ∫₁^∞ ψ x^{−3/4} cos((t/2) log x)` com sinais opostos em `a < b` ⇒ zero na reta em `(a, b)` | ✅ | `AtaqueRH.zero_de_certificados`, `sinal_de_integral` |
| F3.4 | Certificar `Ξ(t) < 0` num `t ∈ (14,2; 21)` (quadratura intervalar de `I(t)`) ⇒ primeiro zero na reta | ⬜ | `AtaqueRH.SinalNegativo` |
| F3.5 | Forma de Fourier `Ξ(t) = 2∫ Φ(u) cos(ut) du`, `Φ > 0`; depois Hardy | ⬜ | `AtaqueRH.Hardy` |
| F3.6 | de Bruijn–Newman: `H_t` e `Λ` | ⬜ | — |
| F3.7 | **Critério de Báez-Duarte completo** (ponte, não progresso sobre RH): RH ⇒ `D_N → 0` por Perron suavizado, Titchmarsh 14.2, Lindelöf sob RH e Phragmén–Lindelöf; com B1, **RH ⟺ `D_N → 0` sem pontes** | ✅ | `NecessidadeRH.necessidade`, `NecessidadeRH.rh_iff_DN` |

## Frente 4 — P vs NP

**Aposta.** A fronteira real é modesta: a melhor cota inferior explícita para circuitos gerais
é cerca de `3,1·n`. Melhorá-la (eliminação de portas auxiliada por SAT-solvers, certificada) é
contribuição publicável; a técnica de Williams (algoritmos ⇒ cotas inferiores) é a única que já
venceu as barreiras num caso não trivial.

| Marco | Enunciado | Estado | Alvo Lean |
|---|---|---|---|
| F4.1 | Cook–Levin genuíno; Shannon; cota linear explícita | ✅ | `CookLevinNP`, `Shannon`, `CircuitoExplicito` |
| F4.2 | Linguagens ↔ circuitos: fatias, `CotaInferior`, `P/poly`; `P ⊆ P/poly ∧ NP ⊄ P/poly ⇒ P ≠ NP`; fronteira linear monótona | ✅ | `AtaquePvsNP` |
| F4.3 | **Ponte `P ⊆ P/poly` provada** (simulação de `FinTM2` por circuitos de tamanho polinomial); `NP ⊄ P/poly ⇒ P ≠ NP` sem pontes | ✅ | `PemPpoly.pemPpoly`, `p_ne_np_de_naoPpoly` |
| F4.4 | Hierarquia de tempo; barreiras (Baker–Gill–Solovay, Razborov–Rudich) | ⬜ | — |
| F4.5 | Fronteira linear `α > 3,1` para uma linguagem de NP | ⬜ | `AtaquePvsNP.FronteiraLinear` |

## Frente 5 — Yang–Mills

**Aposta.** O lado da rede é tratável (positividade por reflexão, gap em acoplamento forte);
o limite contínuo em 4D exige controle não perturbativo que ninguém tem. 3D como laboratório.

| Marco | Enunciado | Estado | Alvo Lean |
|---|---|---|---|
| F5.1 | Medida de Wilson invariante; positividade por reflexão abstrata | ✅ | `BaseWilsonMedida`, `BasePositividadeReflexao` |
| F5.2 | `FormaRefletida ⇒` positividade; estável por soma de ações | ✅ | `AtaqueYM.rp_de_forma`, `forma_soma` |
| F5.3 | `FormaRefletida` para a ação de Wilson numa rede refletida | ⬜ | `AtaqueYM.FormaRefletida` |
| F5.4 | Gap em acoplamento forte (expansão em cluster) | ⬜ | — |

## Frentes 6 e 7 — Beal e Hodge

**Beal.** Método modular assinatura por assinatura (o maquinário de FLT); meta intermediária:
"abc efetiva ⇒ Beal fora de um conjunto finito", mais busca certificada de contraexemplos. O
kernel já cobre FLT para primos regulares e famílias `(6k, 6l, 2m)` e `d ∣ mdc`, `d ≤ 17`.

**Hodge.** Faltam na Mathlib a cohomologia de variedades e a comparação de de Rham; a frente
fica na infraestrutura (`BaseHodgeLinear`, `HodgeToro`, `HodgeFiltracao`).

---

## Ordem

1. **BSD**: F1.4 (fórmula refinada para `y² = x³ − x`) → F1.5 (outras curvas CM de condutor pequeno).
2. **Navier–Stokes**: F2.4 → F2.5 (aposta), F2.6 em paralelo.
3. **Riemann**: F3.4 → F3.5.
4. **P vs NP**: F4.4 → F4.5.
5. **Yang–Mills**: F5.3 → F5.4.

O resultado esperado são formalizações publicáveis e algumas contribuições de pesquisa reais; a
única aposta com chance não desprezível de resolver um problema do Clay nos próximos anos é a
explosão em Navier–Stokes por prova assistida por computador.
