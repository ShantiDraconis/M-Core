# Frações e caudas: o que os sete problemas compartilham (rodada 103, 04/11/2026)

Kernel: `atk-kernel/ATK/FracoesChi.lean`, `FracoesBernoulli.lean`, `FracoesEscala.lean`, `FracoesSAT.lean`, `FracoesGama.lean`, `FracoesGamaZeros.lean` (namespaces `ATK.Fracoes.*`).
Numérico: `codigo/caudas.py`, `dados/caudas.json`, `testes/test_caudas.py` (6 testes).
Classe: **ferramenta / consequência / reformulação**. Nada aqui é "novo" no sentido do titular (sem issue
"Proposta R1xx"). Nenhum problema do milênio nem Beal muda de estado: todos continuam `OPEN_MATH`.

## 1. O princípio: cada problema é uma cauda com um expoente

Em cada problema há uma quantidade cujo **resto** (a cauda) decai ou cresce com um expoente. O que se sabe
provar é um valor do expoente. O que se conjectura é outro. A fração não resolve nada sozinha. Ela mostra
**onde** está a distância entre o provado e o conjecturado.

| Problema | Cauda | Expoente / taxa | Provado | Conjectura | No kernel do ATK |
| --- | --- | --- | --- | --- | --- |
| RH | `ψ(x) − x` (erro dos primos) | `Θ = sup Re ρ = c` | `½ ≤ c ≤ 1` | `c = ½` | `PontesRH.rh_iff_c`, `QuasiRH.semZeros_iff_psi` |
| RH (zeros) | resto da fração contínua de `γ` | intervalo racional após `k` passos | 7, 5 e 2 quocientes dos três primeiros zeros | — | `Gama.gama*_fc`, `GamaZeros.tres_zeros_fc` |
| BSD | `∏_{p ≤ x} N_p/p` | `(log x)^r` | 11a1: `L(E,1)/Ω = 1/5` (numérico) | `r` = posto | — (numérico) |
| Beal | nº de soluções primitivas com `C^z ≤ X` | `X^χ`, `χ = 1/x + 1/y + 1/z − 1` | `χ > 0`: infinitas; `(3,3,3)`: nenhuma; `χ < 0`: finitas (Darmon–Granville) | nenhuma para `x, y, z ≥ 3` | `Chi.*` |
| NS | espectro de Fourier `|û_k|` | `e^{−δk}` (analítico) vs `k^{−a}` (singular) | 2D: sempre regular; 3D: tempo curto | `δ(t) > 0` sempre em 3D | `Escala.*` (a lacuna `½`) |
| YM | correlação conexa `⟨O(t)O(0)⟩` | `e^{−mt}`, `m` = gap de massa | rede 2D (exato); 4D só numérico | `m > 0` no contínuo 4D | `Escala.ym_energia_4d` |
| P vs NP | tempo de 3-SAT | `cⁿ` | `c ≤ 4/3` (Schöning), `7/8` ótimo para MAX-3SAT se P≠NP (Håstad) | sem algoritmo polinomial | `SAT.*` |
| Hodge | — (não há cauda natural) | ℚ contra ℤ: denominador `N` com `N·α` algébrico | falha em ℤ (Atiyah–Hirzebruch) | vale em ℚ | `Chi.euler_de_chi`, `Bernoulli.doze_compartilhado` |

## 2. Leis certificadas (teoremas no kernel)

### 2.1 `χ(p, q, r) = 1/p + 1/q + 1/r − 1` — Beal, geometria, grupos, Hurwitz, Euler (`FracoesChi.lean`)

* `chi_pos_iff`, `chi_zero_iff`: a tricotomia. Esférico: `(2,2,n)`, `(2,3,3)`, `(2,3,4)`, `(2,3,5)`.
  Euclidiano: `(2,3,6)`, `(2,4,4)`, `(3,3,3)`. Hiperbólico: o resto.
* `chi_neg_le`, `chi_eq_iff`: **a lacuna `1/42`**. Se `χ < 0`, então `χ ≤ −1/42`, com igualdade só em
  `(2,3,7)`. Daí `hurwitz`: `(2g − 2)/|χ| ≤ 84(g − 1)`. E `hurwitz_klein`: `84·2 = 168 = |GL₃(𝔽₂)|`.
* `ordem_*`: `2/χ` é a ordem do grupo esférico: diedral `2n`, `A₄` = 12, `S₄` = 24, `A₅` = 60.
* `euler_de_chi`, `platonicos`: com `E = 1/χ(2,p,q)`, `V = 2/(qχ)`, `F = 2/(pχ)`, vale `V − E + F = 2`. Os
  cinco sólidos platônicos saem daí. A característica de Euler da esfera é `2χ/χ`.
* Beal: `beal_chi_nonpos`, `beal_chi_zero_iff`, `beal_chi_gap` (`χ ≤ −1/12` fora de `(3,3,3)`).
  `beal_333` (FLT3, Mathlib). `esferico_222_infinito` (infinitas primitivas em `χ = ½`).
  `beal_por_chi`: com a ponte de Darmon–Granville, finitas em toda a região de Beal.

### 2.2 Bernoulli — RH, Hodge, formas modulares, `E₈` (`FracoesBernoulli.lean`)

* `zeta_neg_*`: `ζ(0) = −1/2`, `ζ(−1) = −1/12`, `ζ(−3) = 1/120`, `ζ(−5) = −1/252`, `ζ(−7) = 1/240` e
  `ζ(−9) = −1/132`. Usam `B₆ = 1/42`, `B₈ = −1/30` e `B₁₀ = 5/66`.
* `doze_compartilhado`: o coeficiente de `X²` em `X/(e^X − 1)` é `1/12 = −ζ(−1)`. A mesma série dá a
  classe de Todd de Hirzebruch–Riemann–Roch, de onde vem o `/12` de Noether `χ(𝒪_S) = (K² + e)/12`.
  `noether_exemplos` avalia a fórmula (só a aritmética).
* `duzentos_e_quarenta`: `2/ζ(−3) = 1/ζ(−7) = 240`.
* `staudt_clausen`, `bernoulli_chi`: `B₄ = −χ(2,3,5)`, `B₆ = −χ(2,3,7)`, `B₈ = −χ(2,3,5)`,
  `B₁₀ = −χ(2,3,11)` (ver §4).

### 2.3 Escala — NS e YM (`FracoesEscala.lean`)

* `escala`: `∫‖k^a f(kx)‖^q dx = k^{aq − d} ∫‖f‖^q`. A fração crítica é `q = d/a` (`critico_iff`).
* NS: `ns_L3_critico` (L³ é invariante em `d = 3`) e `ns_energia_3d` (a energia ganha `k^{−1}`:
  supercrítica). `ns_energia_2d` (crítica em `d = 2`, onde a regularidade é teorema). `serrin_invariante`
  (`2/p + 3/q = 1`). `lacunas`: NS 3D tem lacuna `½`, NS 2D e YM 4D têm `0`.
* YM: `ym_energia_4d` (`∫|k²F(k·)|² = ∫|F|²`). O gap de massa é quântico e não sai daqui.

### 2.4 P vs NP (`FracoesSAT.lean`)

* `clausula_sete_oitavos`, `clausula_falha`: 7 das 8 atribuições satisfazem uma 3-cláusula.
* `schoening`, `schoening_k`: `Σ_j C(n,j) 2⁻ⁿ (k−1)⁻ʲ = (k/(2(k−1)))ⁿ`. `base`: `2(k−1)/k` vale `1` em
  `k = 2` e `4/3` em `k = 3`.

### 2.5 Partes imaginárias em fração (`FracoesGama.lean`, `FracoesGamaZeros.lean`)

* `gama1_fc`: `γ₁ = [14; 7, 2, 2, 1, 2, 1, …]`. A cauda `x₇` fica em
  `[36 140 203/21 453 481, 38 960 203/17 593 481]`, e `|γ₁ − 2728/193| < 1/193²`.
* `gama2_fc`: `[21; 45, 2, 1, 2, …]`. `gama3_fc`: `[25; 92, …]`.
* `GamaZeros.tres_zeros_fc`: incondicional (zeros de `ζ` certificados no kernel).
* `gigante1_fc`, `gigante2_fc`: o par em altura `3·10¹²` tem 16 e 17 quocientes a partir de
  `3 000 180 519 279`, com bolas de raio `~3·10⁻¹⁸` (hipóteses da Arb). O convergente final tem numerador de
  21 dígitos e denominador de 8.

## 3. Pontes nomeadas (publicadas, não formalizadas)

| Ponte | Onde | O que daria |
| --- | --- | --- |
| Darmon–Granville (1995) | `Chi.PonteDarmonGranville` | finitude das primitivas para `χ < 0` |
| de Bruijn–Newman, Rodgers–Tao | `PontesRH` (rodada 102) | `RH ⟺ Λ = 0` |
| Håstad (2001) | texto | `7/8 + ε` é NP-difícil |
| Harder (1971) | texto | `χ(SL₂ℤ) = ζ(−1) = −1/12` |
| teta de `E₈` = `E₄` | texto | as 240 raízes são o `240 = 2/ζ(−3)` |
| Poonen–Schaefer–Stoll (2007) | texto | as soluções primitivas de `(2,3,7)` são exatamente as 5 encontradas |

## 4. Coincidências registradas (mesma fração, nenhum mapa)

* **`7/8`**: aparece em `N(T) = (T/2π) log(T/2πe) + 7/8 + S(T)`, onde vem da fase `−π/8` de `Γ`. Aparece
  também em MAX-3SAT, onde vem de `1 − 2⁻³`. Não há teorema que ligue as duas.
* **`B_{2k} = −χ(primos)`**: vale porque, para `2k ≤ 10`, os primos com `(p − 1) | 2k` são três (ou dois)
  e o inteiro de von Staudt–Clausen é `1`. Para `(2,3,∞)` há mapa (Harder). Para `(2,3,5)`, `(2,3,7)` e
  `(2,3,11)` não se conhece nenhum. Em `2k = 12` a identidade já não tem a forma de `χ`: cinco primos e
  `B₁₂ = −691/2730`.
* **`1/42`**: é `B₆` e é `|χ(2,3,7)|`. Pela identidade acima, é o mesmo fenômeno aritmético. Não há
  ligação conhecida entre a cota de Hurwitz e `ζ(−5)`.

Regra adotada: **igualdade de frações não é conexão**. Conexão exige um teorema que leve um objeto no outro
(uma série geradora comum, um grupo, um funtor). Sem isso, a coincidência só é registrada.

## 5. Números gigantes e gigantemente pequenos

| Objeto | Gigante | Pequeno |
| --- | --- | --- |
| zero em `T ≈ 3·10¹²` | parte inteira com 13 dígitos; convergente com 21 dígitos | raio `2,85·10⁻¹⁸`; cauda após 16 passos |
| `∏_{p ≤ 10⁴} N_p/p` (BSD) | numerador com ~3 900 dígitos | — |
| Beal `(2,3,7)` | `15 312 283² + 9 262³ = 113⁷` | `|χ| = 1/42` |
| calibre `Z₂` (YM, rede 2D) | — | `⟨W⟩ = (1/2)^{área}`: `1/16` em área 4 |
| Hurwitz | `84(g − 1)` automorfismos | `1/42` |

## 6. Onde cada problema aparece no cotidiano, e o que a engenharia faz

A engenharia **contorna** os problemas abertos com modelos, cotas e computação. Não os resolve.

| Problema | Onde aparece | O que a engenharia faz | Fração envolvida |
| --- | --- | --- | --- |
| RH | geração de chaves RSA/TLS (achar primos grandes); teste de Miller | testes probabilísticos (Miller–Rabin). Sob GRH, testar bases `a < 2 ln² n` torna o teste determinístico (Bach) | densidade `1/log x`; erro `x^{½}` sob RH |
| BSD | criptografia de curvas elípticas (ECDSA no Bitcoin/secp256k1, TLS, Signal) | contagem de pontos (Schoof) para escolher curvas com `#E(𝔽_p)` primo | `#E(𝔽_p) = p + 1 − a_p`, `|a_p| ≤ 2√p` |
| Beal / χ | pisos (2,4,4), favo de mel e grafeno (2,3,6), treliças (3,3,3), bola de futebol e cúpulas geodésicas (2,3,5), cápsides de vírus (`A₅`, 60) | ladrilhamento e projeto estrutural pela classificação de `χ`; restrição cristalográfica (só simetrias de ordem 2, 3, 4, 6 periódicas; quasicristais de Shechtman para 5) | `χ = 1/p + 1/q + 1/r − 1`; `V − E + F = 2` |
| NS | previsão do tempo, aerodinâmica, oleodutos, sangue | CFD com modelos de turbulência (RANS `k-ε`, LES/Smagorinsky) que **cortam** a cauda de Fourier | `k^{−5/3}` (Kolmogorov, fenomenológico) |
| YM | por que a força nuclear tem alcance curto (~1,4 fm); massa dos prótons | QCD na rede em supercomputadores mede massas e o gap numericamente | cauda de Yukawa `e^{−mr}/r`; `β₀ = 11N/3 − 2n_f/3` |
| P vs NP | escalas de tripulação, rotas de entrega, verificação de chips, Sudoku generalizado | resolvedores SAT/MIP com heurísticas; aproximações (`7/8` em MAX-3SAT é o ótimo se P≠NP) | `7/8`, `(4/3)ⁿ` |
| Hodge | malhas 3D (CAD, impressão 3D: `V − E + F = 2 − 2g` como verificação), análise topológica de dados | invariantes topológicos (Betti, Euler) em validação de malhas e homologia persistente | `χ(𝒪_S) = (K² + e)/12` |
| Casimir (`ζ(−3)`) | aderência em MEMS (microdispositivos) | projeto de folgas contra o colapso por Casimir | `π²ħc/(240 a⁴)`, `240 = 2/ζ(−3)` |

## 7. Numérico (`codigo/caudas.py`)

* **Zeros**: os quocientes e as caudas coincidem com `FracoesGama.lean`. `|γ − p/q|·q²` vale 0,38, 0,14, 0,10,
  0,10 e 0,20 (todos `< 1`).
* **BSD**: `a_p` conferem com o LMFDB. 11a1: `L(E,1)/Ω = 0,2000000000000000` (erro `3·10⁻¹⁷`), contra
  `|Ш|·c₁₁/|T|² = 1·5/25`. Expoente local de `∏ N_p/p` entre `10³` e `10⁴`: `0,29` (posto 0), `1,71`
  (posto 1), `2,31` (posto 2). A convergência para `r` é lenta (termo `√2·e^{rγ}`, Goldfeld), mas a
  ordem é a do posto.
* **Beal**: `(2,2,2)` tem 10, 32, 100 e 316 primitivas até `10³`, …, `10⁶`, expoente `0,4997` (`χ = ½`).
  `(2,2,3)` tem expoente `0,36` (`χ = 1/3`). `(3,3,3)`: nenhuma até `10⁶`. `(2,3,7)`: até `10¹⁵`, exatamente
  as 5 soluções do teorema de Poonen–Schaefer–Stoll (`1⁷ + 2³ = 3²`, `2⁷ + 17³ = 71²`,
  `17⁷ + 76 271³ = 21 063 928²`, `1414³ + 2 213 459² = 65⁷`, `9262³ + 15 312 283² = 113⁷`).
* **NS (Burgers, Cole–Hopf, `t = 1`)**: largura da cauda exponencial `δ = 0,77; 0,46; 0,27` para
  `ν = 0,2; 0,1; 0,05`. `δ ∝ ν^{0,74}` encolhe: no limite invíscido vira o choque, com coeficientes exatamente
  `1/k`.
* **YM (calibre `Z₂`, rede `2×2`, enumeração de `2¹²` configurações)**: `⟨W⟩ = 1/2, 1/4, 1/16` para
  áreas 1, 2 e 4. É a lei de área com tensão `log 2`.
* **P vs NP**: a média exata de cláusulas satisfeitas é `7/8` (`n = 10`, `m = 40`). Schöning em `n = 12`
  teve sucesso `0,60` por tentativa, contra a cota `(3/4)¹² = 0,032` de pior caso.
* **Euler/Descartes**: `V − E + F = 2` e defeito angular total `4π` nos cinco sólidos.

## 8. Rodada 104: o par recorde em frações e `7/8` para toda fórmula (kernel)

### 8.1 O par 12 363 187 982 787/788 (`ATK/FracoesParRecorde.lean`, 16 teoremas)

Hipóteses: as bolas da Arb de `par_mais_fragil_continuacao8` (clay-riemann-proof), `|γ₁ − c₁| ≤ 265·10⁻²⁰`,
`|γ₂ − c₂| ≤ 379·10⁻²⁰`. Parte inteira comum `E = 3 000 183 404 278`. Consequências exatas:

| teorema | enunciado |
| --- | --- |
| `cauda1_fc` | `γ₁ − E = [0; 1, 3, 7, 1, 2, 7, 2, 1, 1, 4, 17, 10, 2, 1, 3, 1, x₁₇]`, `x₁₇ ∈ [430 714 988 867/51 406 891 183, 434 252 755 933/46 907 084 017]` |
| `cauda2_fc` | `γ₂ − E = [0; 1, 3, 7, 3, 40, 4, 1, 1, 2, 3, 1, 3, 1, 2, 3, 4, 2, x₁₈]`, `x₁₈ ∈ [487 467 507 456/308 072 325 131, 541 748 748 544/186 879 730 869]` |
| `separam_no_quarto` | as duas caudas coincidem até `[0; 1, 3, 7]` e diferem no 4º quociente (1 contra 3) |
| `simples1`, `simples2` | `314 849 491/415 434 260` e `296 762 215/391 380 514` estão nas bolas; nenhuma fração de denominador menor está (vizinhos de Farey, `farey_min`) |
| `delta_bolas` | `Δγ ∈ 3 643 183 291 679/10¹⁶ ± 644·10⁻²⁰` |
| `delta_fc` | `Δγ = [0; 2744, 1, 5, 1, 3, 2, 1, 6, 1, 10, 6, x₁₂]` com a cauda num intervalo racional |
| `simples_delta` | `97 021/266 308 314` é a fração mais simples no erro de `Δγ` |
| `lambda_bolas` | `−Δγ²/2` entre dois racionais exatos (`≈ −6,6364·10⁻⁸`) |
| `log_altura` | `26 < log(T/2π) < 28` para `3·10¹² ≤ T ≤ 3,001·10¹²` (de `3,14 < π < 3,15`, `2,7182818283 < e < 2,7182818286`) |
| `s_novo`, `s_anterior`, `recorde` | `3/2000 < s_novo < 1/600 < 1/400 < s_anterior`: o par novo é mais apertado que o 12 363 167 808 945/946 |

### 8.2 `7/8` para toda fórmula 3-CNF (`ATK/FracoesSATMedia.lean`, 8 teoremas)

`card_padrao_oito` (cada padrão de 3 bits em variáveis distintas tem `2ⁿ/8` atribuições, pela inversão de bits),
`card_satisfaz` (`7·2ⁿ/8` satisfazem a cláusula), **`media_sete_oitavos`** (`8·Σ_v #sat(v) = 7m·2ⁿ`) e
**`existe_sete_oitavos`** (Johnson: alguma atribuição satisfaz `≥ 7m/8`). Håstad: garantir `7/8 + ε` é NP-difícil
(ponte). P vs NP continua `OPEN_MATH`.

### 8.3 B7 no tempo (`ATK/OS*.lean`, 52 teoremas, portados da branch `atk/rh-rho-independent`)

Reconstrução de Osterwalder–Schrader na forma temporal: medida euclidiana estacionária e positiva por reflexão ⇒
espaço de Hilbert físico, matriz de transferência `P(t) = e^{−tH}` autoadjunta e positiva, decaimento
exponencial das correlações conexas ⇒ lacuna `‖P(t)w‖ ≤ e^{−mt}‖w‖` (`lacuna_OS`, `lacuna_processo`), simetrias
⇒ isometrias que comutam com `e^{−tH}`, e o exemplo em `ℂ²` com a cota atingida. É a cauda `e^{−mt}` de YM da
§1 como teorema abstrato. Falta a medida de Yang–Mills em `S′(ℝ⁴)` (O8). B7 continua `PUBLICADA_NAO_FORMALIZADA`.
