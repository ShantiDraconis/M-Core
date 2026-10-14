# Fichas: provado, refutado, lacuna — e os zeros fora da linha

Cada conjectura tem três partes, agora separadas no kernel: o que está **provado**, o que é
**refutado** (um reforço natural da conjectura que é falso) e a **lacuna** — a parte de "erro",
com `Conjectura ⟺ Lacuna` provado quando possível. Ao lado de cada família (o que se quer provar)
está a contra-família (as testemunhas que a refutariam), formalizada como **anti-produto**.
Nada aqui fecha uma conjectura: `CLOSED_MATH` continua `false`.

## Os zeros fora da linha — `ATK/ForaDaLinha.lean` (11 teoremas)

O teorema que supõe que existem zeros fora da linha crítica e diz o que eles teriam de satisfazer:

* `riemann_iff_vazio`, `nao_riemann_iff`: **RH ⟺ não há zero fora da linha**; `¬RH ⟺ existe um`;
* `evita`: um zero fora da linha **evita** a reta crítica, o eixo real, a faixa `|Im ρ| < √3/2` e as
  bordas `Re ρ ≤ c(t)` e `Re ρ ≥ 1 − c(t)`;
* `quarteto_fora`: vem com `1 − ρ`, `ρ̄`, `1 − ρ̄` — **quatro zeros fora da linha distintos**
  (parâmetros de tensão e de torção);
* `piso_DN` (**condensação**): um zero `ρ` com `1/2 < Re ρ < 1` força, para todo `N`,
  `D_N ≥ m(ρ)²`, com `m(ρ) = 1/(|ρ|·(1/√(2σ−1) + 1/(1−σ)))` e `σ = Re ρ`;
* `finito_de_zero_fora`, `finito_de_nao_riemann` (**materialização**): logo `¬RH ⇒ D_N` fica no
  estado `finito`, com limite `≥ m(ρ)² > 0`.

Família (produto `D_N → 0 ⇒ RH`, já provado) e contra-família (zeros fora da linha) são as duas
metades da mesma lacuna O1.

## As fichas — `ATK/Fichas.lean` (24)

| conjectura | provado | refutado (teorema `¬`) | lacuna |
|---|---|---|---|
| Riemann (`fichaRiemann`) | `c(t) < Re s < 1 − c(t)` e `|Im s| ≥ √3/2` para todo zero não trivial | "todo zero de ζ tem parte real 1/2" (`ζ(−2) = 0`) | não há zero fora da linha (`⟺ RH`) |
| Beal (`fichaBeal`) | sem solução quando `3 ∣ g` ou `4 ∣ g` | "sem solução alguma com expoentes > 2" (`2³ + 2³ = 2⁴`) | excluir as soluções dois a dois coprimas com `3 ∤ g`, `4 ∤ g` (`⟺ Beal`) |
| Yang–Mills, rede (`fichaYM`) | `m(β) > 0` para todo `β > 0` | "existe gap uniforme em `β`" | limite contínuo 4D (O8) |
| P vs NP, circuitos (`fichaPNP`) | função de `n` bits sem circuito `≤ 2ⁿ/(8n)` | "toda família tem circuitos polinomiais" | uma família de NP fora de P/poly (O4) |
| BSD (`fichaBSD`) | todo ponto racional de `y² = x³ − x` tem `y = 0` | "o mesmo vale para `y² = x³ − n²x`, todo `n`" (`n = 6`: `(−3, 9)`) | BSD geral (O6) |
| Navier–Stokes (`fichaNS`) | dado pequeno (`bM² < a`) ⇒ enstrofia limitada | "a desigualdade limita também dados grandes" | estrutura extra da equação (O3) |

Anti-produtos completos (`AntiProduto`): `antiRiemann` (zeros fora da linha) e `antiBeal`
(contraexemplos primitivos), com `AntiProduto.iff_vazio`: conjectura ⟺ não há testemunha.
`metateorema_falso`: a "lei" `Nonempty H ⟺ IsEmpty W`, proposta como regra geral, é falsa.

## Parâmetros

| parâmetro | teorema | conteúdo |
|---|---|---|
| indeterminação | `RiemannStates.estado_DN_dicotomia` | `D_N` só pode estar nos estados `zero` ou `finito` |
| tensão / torção | `ForaDaLinha.quarteto_fora` | órbita de 4 zeros sob `s ↦ 1 − s`, `s ↦ s̄`, `s ↦ 1 − s̄` |
| condensação | `ForaDaLinha.piso_DN` | piso `m(ρ)²` de `D_N` |
| condensação explícita | `ValleePoussin.piso_DN_log` | `D_N ≥ (1/(|ρ|(1/√(2σ−1) + 1/c(t))))²`, `c(t)` logarítmico (`|t| ≥ 4`) |
| materialização | `ForaDaLinha.finito_de_zero_fora` | o zero vira estado `finito` de `D_N` |
| explosão | `Fichas.explosao_dado_grande` | se `b y₀² > a`, solução de `y' = −a y + b y³` explode em `T* = log(b y₀²/(b y₀² − a))/(2a)` |
| criticidade | `Fichas.critico_estacionario` | `b y₀² = a`: solução estacionária (limiar `√(a/b)`) |
| condicionamento | `Fichas.flt_iff_primos_ge_cinco` | FLT ⟺ FLT para os primos `p ≥ 5` (ponte B2 reduzida) |

## Correções aos textos anexados

* **B1 está provada** no kernel (`BaezDuarteBridge.baezDuarteCriterion`: `D_N → 0 ⇒ RH`). O que não
  está formalizado é a recíproca (necessidade de Báez-Duarte) e, claro, `D_N → 0`.
* "Quando entrar de la Vallée Poussin, o `m(ρ)` sobe": `m` é uma função fixa de `ρ`; o que a região
  logarítmica faz é restringir onde `ρ` pode estar (`σ < 1 − c(t)`), o que dá o piso explícito
  `m(ρ) ≥ 1/(|ρ|(1/√(2σ−1) + 1/c(t)))` (`ValleePoussin.m_ge_log`). O piso não é uniforme (vai a `0`
  com `σ → 1/2` e com `|t| → ∞`), então não decide O1. A potência provada é `(log|t|)⁻⁹`, não a
  clássica `1/log|t|`.
* "Provar `D_{2N} ≤ q D_N` (`q < 1`) é o próximo cálculo decisivo": falso para a sequência real —
  contração geométrica contradiz o piso `D_N ≥ c/log N` (`ContracaoDN.sem_contracao_de_piso_log`);
  a numérica dá `D_{2N}/D_N → 1` e `D_N log N ≈ 0,046`.
* "Se Beal for verdadeira, `g* ∈ {2, 3}`": na verdade **Beal ⟺ `g* = 2`** (`BealFiltros.beal_iff_gEstrela`),
  pois `2³ + 2³ = 2⁴` tem mdc 2.
* "A álgebra de intervalos é um anel": falso (`AlgebraTerminal.distributiva_falha`); vale só a
  subdistributividade. O `D₂ = 5/6` do modelo de Gram não é o `D₂` real (`0,28996…`).
* `ZetaRetangulo` não usa numérica nem Riemann–Siegel: é a desigualdade analítica `|s − 1| < 2·Re s`.
* O módulo da curva `y² = x³ − x` calcula `E(ℚ)` (4 pontos); **não** prova BSD para ela (não há
  L-função de curva elíptica na Mathlib).
* "Não há curva de Frey para expoentes mistos" é impreciso: a curva de Frey–Hellegouarch existe e é
  elíptica para qualquer solução (`FreyBeal`, módulo paralelo); o que falta é o rebaixamento de
  nível, que só funciona com um primo comum aos três expoentes.
* `Nonempty H ↔ IsEmpty W` não é uma lei válida (`metateorema_falso`); o correto é
  `Q ↔ IsEmpty W` para anti-produto completo e `H → IsEmpty W` para um produto `H → Q`.
* Itens citados mas **não** formalizáveis hoje: Λ de de Bruijn–Newman (Rodgers–Tao), as barreiras
  de relativização / provas naturais / algebrização (exigem modelo de oráculos), Lefschetz (1,1) e
  Gross–Zagier–Kolyvagin (exigem fundações ausentes da Mathlib).
