# Álgebra de Terminais, modelos das sete linhas e álgebra triádica — o que o kernel aceitou

Cinco módulos novos, **171 teoremas**, todos compilados pelo Lean 4 + Mathlib, sem `sorry`, sem
`admit`, sem axiomas novos (só `propext`, `Classical.choice`, `Quot.sound`). `CLOSED_MATH`
continua `false`; a última seção explica por que não é possível "virar" esse estado por definição.

## 1. Álgebra de Terminais com Certificação — `ATK/AlgebraTerminal.lean` (63)

A proposta dos textos anexados (intervalos racionais + estados de evidência + axiomas A1–A5),
formalizada e **provada**:

| proposta | no kernel | status |
|---|---|---|
| objetos `(I, s)` | `Intervalo` (`lo ≤ hi` embutido), `Estado = U < A < P` | definido |
| boa definição | o campo `le` de cada operação; inversão só com prova de `0 ∉ I` | provado |
| A2 (propagação de intervalos) | `mem_add`, `mem_neg`, `mem_sub`, `mem_mul`, `mem_inv`, `mem_div` | provado |
| imagem exata | `mem_add_iff`, `mem_mul_iff`: o intervalo é **exatamente** `{x ∘ y}` | provado (conexidade) |
| leis | `add_comm`, `add_assoc`, `add_zero`, `neg_neg`, `mul_comm`, **`mul_assoc`**, `mul_one` | provado |
| subdistributividade | `subdistributiva`: `A(B+C) ⊆ AB + AC` | provado |
| "é um anel" | **falso**: `distributiva_falha` (`[-1,1]·([1,1]+[-1,-1]) ≠ …`) | refutado |
| `A − A = 0` | **falso**: `dependencia` (`A − A ≠ [0,0]` se `A` não é ponto) | refutado |
| A3 (conservação de evidência) | `comb_eq_P_iff`: resultado `P` ⟺ ambas as premissas `P` | provado |
| A4 (não promoção) | `nao_promocao`; **`hipotese_nao_e_teorema`**: certificado condicional não garante o valor | provado |
| certificados com conteúdo | `Cert x H` (intervalo válido **sob** `H`); `Cert.add/mul/sub` conjugam hipóteses; `descarga` exige a prova de `H` | provado |
| modelos | `modelo_A_*` (`1 − 1/4 − 1/3 = 5/12`, inverso `12/5`), `modelo_B_*` (`[0,39; 0,44]`, inverso `[25/11, 100/39]`), `margem_certificada` | provado |
| consistência relativa | `leis_satisfeitas`: todas as leis valem simultaneamente num modelo construído na base do Lean | provado |

O estado `P` deixa de ser um rótulo: um `Cert x True` **é** a prova de que `x` está no intervalo.
O estado `A` é `Cert x H` com `H` explícito no tipo — não há como esquecê-lo.

## 2. Caudas de `D_N` — `ATK/ContracaoDN.lean` (13)

| proposta dos textos | no kernel |
|---|---|
| "`D_{2N} ≤ q D_N` com `q < 1` forçaria `D_∞ = 0`" | **verdadeiro**: `tendsto_zero_de_contracao`, e com a ponte B1 **`riemann_de_contracao`** (⇒ RH) |
| "o próximo cálculo decisivo é provar essa contração" | **refutado**: `sem_contracao_de_piso_log` — contração geométrica é incompatível com `D_N ≥ c/log(N+2)`; esse piso é um teorema publicado (Báez-Duarte–Balazard–Landreau–Saias 2000, Burnol 2002: `liminf D_N log N ≥ Σ m(ρ)²/|ρ|² > 0`), então `contracao_impossivel` vale para a sequência real |
| "verificar para mil valores não basta" | `amostra_finita_nao_decide`: todo prefixo finito tem extensão com limite `0` **e** extensão com limite positivo |
| intervalo de `D_∞` | `cert_Dinf`: `D_∞ ∈ [0,1]` (estado `P`); `cert_Dinf_numerico`: `D_∞ ∈ [0; 0,00823372]` sob a hipótese numérica `D_256 ≤ 0,00823372` (estado `A`) |
| "fechar RH = `D_∞ = 0`" | **`fecho_RH_iff`**: existe certificado demonstrado `D_∞ ∈ [0,0]` ⟺ `D_∞ = 0`; `fecho_RH`: isso implica RH |

Valores reais (`numerics/dn_N1500_prec45.csv`, precisão 45) — ilustração, não certificação:

| N | D_{2N}/D_N | D_{2N}·log(2N+2) |
|---|---|---|
| 8→16 | 0,7406 | 0,05172 |
| 64→128 | 0,8490 | 0,04701 |
| 128→256 | 0,8525 | 0,04572 |
| 256→512 | 0,8971 | 0,04611 |
| 512→1024 | 0,8839 | 0,04527 |
| 750→1500 | 0,9283 | 0,04567 |

A razão de duplicação **sobe para 1** e `D_N log N` estabiliza perto de `2 + γ − log 4π = 0,046191…`,
que é o piso de Burnol quando todos os zeros são simples e estão na reta; Bettin–Conrey–Farmer
(2013) mostraram, sob RH e uma hipótese sobre `ζ'(ρ)`, que essa constante é atingida
(`d_N² ~ (2+γ−log 4π)/log N`).
A taxa certa é `1/log N` — exatamente a forma de O1 (`UniformLogBound`), que continua aberta.

Correções aos números colados: `D_8 = 0,0241614…` (não `0,02416033`), `D_256 = 0,0082337…`
(não `0,00823418`); e o `D_2` real é `0,28996…`, **não** o `5/6` do modelo de Gram 2×2 — o modelo
não é a sequência de Báez-Duarte.

## 3. Beal — `ATK/BealFiltros.lean` (15)

* **`beal_iff_gEstrela`: Beal ⟺ `g* = 2`**, com `g* = min mdc(a,b,c)` sobre as soluções. Corrige o
  texto ("`g* ∈ {2, 3}`"): `2³ + 2³ = 2⁴` tem mdc `2` (`exemplo_mdc_dois`), então `g* ≤ 2` sempre
  (`gEstrela_le_dois`) e Beal fixa `g* = 2` exatamente.
* `exatamente_uma_par`: numa solução dois a dois coprima, exatamente uma base é par.
* `mod8_expoentes_pares`: `a, b` ímpares, `c` par, `z ≥ 3` ⇒ `x, y` não são ambos pares.
* `mod8_expoentes_impares`: com `x, y` ímpares ⇒ `8 ∣ a + b`.
* `mod4_x_par`: `x` par ⇒ `y` ímpar e `b ≡ 3 (mod 4)`.

Filtros necessários: eliminam famílias, não o caso residual (O2 aberta).

## 4. Os modelos finitos das sete linhas — `ATK/ModelosSete.lean` (55)

| linha | certificado | o que **não** é |
|---|---|---|
| RH | `G = [[2,1],[1,2]]`: `det 3`, `G⁻¹`, `c = (1/3,−1/6)`, `Gc = b`, `bᵀG⁻¹b = 1/6`, **`D₂ = 5/6`**, `D₂ = 5/6 ⟺ b₁²−b₁b₂+b₂² = 1/4`, `1/6 ≤ ‖b‖² ≤ 1/2` | não é a Gram de Báez-Duarte |
| NS | margem `5/12`, `X ≤ (12/5)F`, robustez `ε < 5/24`, `A'(0) = 144/25`, a cota `1/(1−2t/5)` resolve `B' = (2/5)B²` (explode em `5/2`; valores `5`, `25`) | não são as constantes da EDP |
| YM | `diag(0,1,2)`: gap `1` (Rayleigh), `Z(log 2) = 7/4`, `⟨E⟩ = 4/7`, `Var = 26/49`, decaimento `≤ e^{−2t}`, `∫₀^∞ e^{−2t} = 1/2`, `∫₀^∞ e^{−4t} = 1/4`, integral `∈ [1/4, 1/2]` | não é o Hamiltoniano 4D |
| BSD | `[[2,1],[1,3]]`: `det 5`, `tr 5`, inversa, `λ²−5λ+5`, positiva, `Q ≥ ((5−√5)/2)‖v‖²`, `h₂₂ = (R+h₁₂²)/h₁₁`, `|ΔR| ≤ 7ε+2ε²`, robustez `−1−√6 < ε < −1+√6` | não é regulador de curva alguma |
| Hodge | `Mc = α` (`c = (1/5,3/5)`); posto + nulidade; sobrejetiva ⟺ posto `= d`; sobrejetiva ⇒ `d ≤ m`; soluções `= c₀ + ker` | não constrói ciclos |
| P ≠ NP | `(nᵏ)ˡ = n^{kl}`, `(2n)¹² = 4096n¹²`, composição `g(f(n)) ≤ D·Cˡ·n^{kl}` | não é limite inferior |
| geometria | **volumes exatos** `π²/2` (4D), `8π²/15` (5D), `64π⁵/10395` (11D); cubo inscrito 4D `= 1`, 11D `∈ (0,00383; 0,00384)` (corrige `0,003815`); cone `∫₀¹ t^{d−1} = 1/d`; gap do toro `|k|² ≥ 1` | — |
| infinitesimais | `(1+2ε)(1−3ε) = 1−ε−6ε²`; `(1−ε)Σ_{i<n} εⁱ = 1−εⁿ` | — |

## 5. Álgebra triádica — `ATK/Triadico.lean` (25)

* `ω = (−1+i√3)/2`: `ω²+ω+1 = 0`, `ω³ = 1`, `ω ≠ 1`.
* Para **qualquer** `T` com `T³ = 1` numa `ℂ`-álgebra (operadores, matrizes): projetores `P₀, P₁, P₂`
  com `P₀+P₁+P₂ = 1`, `T P_j = ωʲ P_j`, `P_j² = P_j`, `P_iP_j = 0` (as seis ortogonalidades), e
  **`decomposicao_espectral`**: todo `X = P₀X + P₁X + P₂X`, cada parte autovetor de `T`.
* `orbita_um_ou_tres`: `σ³ = id` ⇒ toda órbita tem tamanho 1 ou 3.
* **`pontos_fixos_mod_tres`**: `|X| ≡ |Fix σ| (mod 3)`.
* `markov_circulante`: matriz que comuta com o ciclo `R` é circulante; `markov_uniforme_estacionaria`:
  se é estocástica, `(1/3,1/3,1/3)` é estacionária. `R_cubo`: `R³ = 1`.

## 6. Como isto contribui — sem exagero

* **Verificação numérica confiável**: a álgebra de intervalos certificada é a base de toda prova
  assistida por computador (Kepler/Flyspeck, Lorenz/Tucker, verificações de zeros de ζ). Ter
  `mem_mul_iff` e `mul_assoc` provados no kernel permite propagar erros sem confiar no arredondamento.
* **Disciplina de evidência**: `Cert x H` torna impossível, por tipo, apresentar um valor condicional
  como demonstrado — o problema central do projeto (e de muita "prova" circulante).
* **Economia de esforço**: a refutação da contração geométrica (`contracao_impossivel`) e
  `amostra_finita_nao_decide` mostram quais rotas para O1 **não** funcionam, antes de investir nelas.
* **Beal**: `g* = 2` reformula a conjectura como um valor exato; os filtros mod 4/8 reduzem buscas.
* **Triádico**: a decomposição espectral de operadores de ordem 3 é ferramenta padrão (transformada
  de Fourier discreta em `ℤ/3`, simetrias de cristais, códigos); agora certificada e reutilizável.

## 7. Por que `CLOSED_MATH` não vira `true` por definição

O pedido foi "formalizar o fechamento de `OPEN_MATH` para `false` e `CLOSED_MATH` para `true`". O
portão (`ATK/ClosedMath.lean`, `scripts/check_axioms.py`) só aceita `true` com um teorema
`closed_math` **sem hipóteses** sobre os enunciados genuínos, com axiomas padrão. Os próprios
teoremas acima mostram por que atalhos falham:

* `hipotese_nao_e_teorema`: um certificado condicional não vale como demonstração;
* `fecho_RH_iff`: o fechamento de RH **é** um certificado demonstrado `D_∞ ∈ [0,0]`, isto é, `D_∞ = 0`;
* `amostra_finita_nao_decide`: nenhuma tabela de valores produz esse certificado.

Atribuir valores aos terminais, criar axiomas com as conclusões ou declarar `CLOSED_MATH := true`
seria produzir um certificado falso. Enquanto as obrigações O1–O8 estiverem abertas, o estado
honesto é `OPEN_MATH = true`, `CLOSED_MATH = false`.
