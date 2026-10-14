# As lacunas dos 7 problemas — fronteira certificada, lemas de caminho e o que falta

Para cada problema: **(1)** a fronteira que o kernel do Lean já certifica, **(2)** os lemas novos
que empurram essa fronteira (todos sem `sorry`, sem axiomas novos, auditados pelo CI), **(3)** a
lacuna exata que sobra. Nenhum destes lemas fecha um problema: `CLOSED_MATH` continua `false`, e
continuará até que a lacuna listada em (3) seja provada.

Princípio: uma **equivalência** (como `riemann_iff_fim`) tem a mesma dificuldade do problema; o que
abre caminho é um teorema **intermediário** — mais forte que o conhecido, mais fraco que a
conjectura — ou uma redução que encolhe o caso que falta.

## Riemann

1. Fronteira: `Re s ≥ 1` sem zeros (Mathlib); `Re s ≤ 0` só zeros triviais
   (`ZetaSimetria.zero_trivial_de_re_nao_pos`); `ζ(σ) < 0` em `(0,1)`; ponte B1 provada
   (`BaezDuarteBridge.baezDuarteCriterion`); `D_N` só nos estados `zero`/`finito`.
2. Novo — `ATK/ZetaRetangulo.lean` (16):
   * `Hr_le`: `∫_1^∞ {t} t^{-σ-1} dt ≤ 1/(2σ)` (meia-média de `{t}` em cada intervalo unitário);
   * `zeta_ne_zero_disco`: **`ζ(s) ≠ 0` se `|s − 1| < 2·Re s`** — uma região sem zeros que entra na
     faixa e cruza a reta crítica;
   * `zeta_ne_zero_baixo`, `riemannAte_raiz`: **nenhum zero na faixa com `|Im s| < √3/2`: RH vale
     até essa altura**; `riemann_iff_ate`: RH ⟺ RH até toda altura.
   Novo — `ATK/ZetaRegiao.lean` (10), **o fim fechado entra na faixa em toda altura**:
   * `tres_quatro_um`: a desigualdade `|ζ(1+x)³ ζ(1+x+it)⁴ ζ(1+x+2it)| ≥ 1` (Mathlib);
   * `norm_zeta_le_de_zero`: perto de um zero `β + it`, `|ζ(σ+it)| ≤ (σ−β)(9+4|t|)`;
   * `regiao_sem_zeros`: para `|t| ≥ 1/2`, todo zero tem `Re s < 1 − c(t)`,
     `c(t) = 1/(256·(9+4|t|)⁴·(3+3|t|))`;
   * **`faixa_estreitada`: todo zero não trivial tem `c(t) < Re s < 1 − c(t)`** — início e fim
     fechados avançam juntos, em toda altura.
3. Lacuna: a largura ganha decai como `|t|⁻⁵`. Próximos lemas conhecidos e formalizáveis: região de
   de la Vallée Poussin `σ > 1 − c/log(|t|+2)` (exige cotas `|ζ| ≪ log|t|` por somas parciais),
   Hardy (infinitos zeros na reta), limite inferior de Burnol para `D_N`. Qualquer extremo uniforme
   `a < 1` (quase-RH) já seria inédito; `a = 1/2` é RH (O1).

## Beal

1. Fronteira: Beal ⟺ excluir soluções dois a dois coprimas com `3 ∤ g`, `4 ∤ g`, `g = mdc(x,y,z)`
   (`BealResidual.beal_iff_residual_pairwise`, via FLT(3), FLT(4) da Mathlib).
2. Novo — `ATK/BealFLT.lean` (10):
   * `divisor_fermat`: todo `g ≥ 3` tem divisor `4` ou primo ímpar;
   * `beal_mdc_ge_tres`: com o `FermatLastTheorem` da Mathlib, **nenhuma solução com `g ≥ 3`**;
   * `beal_iff_mdc_pequeno_pairwise`: **com FLT, Beal ⟺ nenhuma solução dois a dois coprima com
     `g ∈ {1, 2}`**; `beal_mdc_primo_de_flt`: cada primo `p` com `FLT(p)` provado exclui `p ∣ g`
     já hoje.
   Em paralelo, na mesma conta (`BealFourFourTwo`, `FermatRightTriangle`, `BealFermatDescent`):
   descida de Fermat `x⁴ − y⁴ ≠ z²` e exclusão **incondicional** das assinaturas `(4k, 4l, 2m)`,
   `(4k, 2l, 4m)`, `(2k, 4l, 4m)` — casos com `g = 2` como `(4, 4, 6)`; cobertura ≈ 4,8 % dos
   triplos com `g ≤ 2` e expoentes de 3 a 200.
3. Lacuna: o resto do caso `g ∈ {1, 2}` (onde nenhum caso de Fermat ajuda) — p.ex. `(3, 4, 5)`.
   A formalização completa de Fermat (projeto de Buzzard, em andamento) tornaria a redução a
   `g ∈ {1, 2}` incondicional.

## P vs NP

1. Fronteira: no modelo do lane, `NP ⊄ P/poly ⇒ P ≠ NP` (`PvsNP.p_ne_np_of_np_not_subset_ppoly`).
2. Novo — `ATK/Shannon.lean` (9): circuitos booleanos como programas lineares;
   * `card_circuito`: `(3(n+s)²)^s` circuitos de tamanho `s`;
   * `shannon`: **para `n ≥ 4` existe função de `n` bits sem circuito com `≤ 2^n/(8n)` portas**;
   * `familia_fora_de_Ppoly`: **existe família fora de `P/poly`** (para todo `k`, eventualmente sem
     circuito de tamanho `n^k`).
3. Lacuna: exibir **uma** família em NP fora de `P/poly` (O4). A contagem garante que quase todas
   as funções estão fora, mas não aponta nenhuma; as barreiras conhecidas (relativização, provas
   naturais, algebrização) excluem os métodos óbvios. Antes disso falta o modelo de complexidade
   completo na Mathlib (L2).

## Navier–Stokes

1. Fronteira: comparação de Riccati local (`NavierStokes.riccati_upper_bound`).
2. Novo — `ATK/NSPequeno.lean` (3): dada a desigualdade de enstrofia `y' ≤ −a y + b y³`,
   * `barreira_exponencial`: se `y(0) < M` e `b M² < a`, então `y(t) ≤ M e^{−κt}`;
   * `enstrofia_limitada`: **sem explosão (estado `+∞` excluído) para dados pequenos**;
   * `enstrofia_estado_zero`: decaimento ao estado `zero`.
3. Lacuna: derivar a desigualdade da equação exige o modelo (L1, ausente da Mathlib); e a cota para
   **todo** dado (O3) é remover `b M² < a` — para dados grandes só vale a cota local, que pode
   explodir.

## Yang–Mills

1. Fronteira: desigualdades auxiliares do lane (`YangMills.weighted_cauchy_schwarz`, …).
2. Novo — `ATK/YMToy.lean` (16): modelo de rede exatamente solúvel (cadeia de transferência `ℤ₂`,
   redução da teoria de calibre `ℤ₂` 2D):
   * `W_formula`, `correl_eq`, `razao_eq_tanh`: correlação `= tanh(β)ⁿ`;
   * `massa_pos`, `correl_exp`: **gap de massa `m(β) = log(coth β) > 0` e decaimento `e^{−m n}`**;
   * `massa_tende_zero`: **o gap fecha no acoplamento fraco (`β → ∞`)** — a lacuna em miniatura.
3. Lacuna: teoria quântica de campos 4D contínua (L5) e gap positivo no limite contínuo (O8). Passos
   conhecidos formalizáveis: gap em acoplamento forte para grupos gerais na rede
   (Osterwalder–Seiler), positividade por reflexão.

## BSD e Hodge

* BSD — em paralelo, na mesma conta (`CongruentCurve`, via `FermatRightTriangle`): para
  `E : y² = x³ − x` como `WeierstrassCurve ℚ` da Mathlib, **`E(ℚ)` tem exatamente 4 pontos**
  (posto 0, 2-torção completa) — o primeiro cálculo de Mordell–Weil de uma curva concreta no kernel.
  A conjectura em geral precisa de L-funções de curvas elípticas e de Mordell–Weil (L4), ausentes da
  Mathlib; O6/O7 seguem abertas.
* Hodge: precisa de teoria de Hodge e ciclos algébricos (L3), ausentes da Mathlib. Primeiro alvo
  quando houver base: teorema de Lefschetz (1,1) (Hodge em codimensão 1).

## Contagem

Novos nesta etapa: 64 teoremas (`ZetaRetangulo` 16, `ZetaRegiao` 10, `BealFLT` 10, `Shannon` 9,
`NSPequeno` 3, `YMToy` 16). Total esperado no CI (com os módulos paralelos de Beal/Fermat/curva
congruente): 547.
