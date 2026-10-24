# Rodada 5 — ATK–Closed Math completo, toro e redução terminal de HR

Kernel: `ATK/ClosedMathCEZ.lean`, `ATK/ClosedMathCompleto.lean`, `ATK/ClosedMathToro.lean`,
`ATK/RHTerminal.lean`, `ATK/Cert/Intervalo.lean`, `ATK/Cert/Transc.lean` (Lean 4.34.1 + Mathlib,
axiomas só `propext`, `Classical.choice`, `Quot.sound`). Espelhos em Coq, Isabelle/HOL, SMT-LIB 2,
TPTP e Python em `formatos/` e `pesquisa/rodada5/` (workflow `closed-math-multiprovador`).

**Nada aqui prova ou refuta a Hipótese de Riemann.** O último teorema mostra exatamente o contrário:
a desigualdade "global" pedida é equivalente a HR.

## 1. O que foi provado (escopo modelo — `UGModelo`, provado)

| Bloco | Resultado no kernel |
| --- | --- |
| Semântica | `classificacao` (C/E/N_C/N_E exaustivos), `exclusivos` (6 pares), "ambos" só para famílias |
| Verificador | `checar_correto` (todo veredito traz prova), `checar_nunca_zero` (invólucro nunca prova igualdade), `nao_zero_certificavel` (não zero é semidecidível), `zero_sempre_indeterminado`, `indeterminado_nao_e_estado`; `checarIC` racional, decidido pelo kernel |
| Operadores | grupo de Klein `{I, J, R, S}`, `T` involução e isometria que não comuta com `R`, `T R T (w) = w̄ + i` |
| Modelo `G_{d,γ}` | P1–P5: zeros `½ ± d ± iγ`, crítico, externo, trajetória "ambos", não zeros `2 ∈ N_E` e `½ ∈ N_C` com `G(½) = (d² + γ²)²` |
| Cruzamento | expansão quártica, velocidades ±1, aceleração 0, separação `2|λ|` **não diferenciável** no encontro, **conservação**: `card roots = 4` para todo `λ`, multiplicidade 2 no encontro e 1 fora |
| Geometrias | corda esférica `4|s−w|²/((1+|s|²)(1+|w|²))`, cilindro injetivo em `0 < Re < 1` e periódico fora, `d_C = 2|sin 2πδ|` com derivada `4π`, cone que **perde** a ordenada (`cone_nao_decide_zero`), cone elevado injetivo |
| Taxonomia | ordem por derivadas, `(z−2)^m` de ordem `m`, zeros `±a, ±ib`, `sin πz = 0 ⟺ z ∈ ℤ` (infinitos), zero de ordem 2 no infinito de `1/z²`, `(x²−1)/(x−1) → 2` (direto e por L'Hôpital, com `0/0 = 0` como convenção ≠ limite), derivada logarítmica, **princípio do argumento** para `(z−a)^m g` e para multiconjuntos, exemplo `(1/2πi)∮ f'/f = 5 − 2 = 3`, truncamentos decimais de 1/3 nunca são zeros, teorema da identidade, multiplicidade infinita ⇒ `f ≡ 0` |
| Modelo `H_{d,γ}` | `q_{½} q_{½+d} q_{½−d} / Γ(1 + s/2)`: inteira, zeros triviais `−2, −4, …`, conjunto completo de zeros, `H_{¼,1}(½) = 289/(256 Γ(5/4))`, **ordem 3** no encontro (`d = 0`) e 1 fora, `(1/2πi)∮ H'/H = 6` nos dois regimes, a reflexão não preserva os triviais |
| Pontes | transporte `G(φ s) = u(s) F(s)` (e falha sem `u ≠ 0`), B17 (fator analítico não nulo preserva a ordem), singularidade removível, `ξ(1 − s) = ξ(s)`, **B20**: `ξ = 0 ⟺ ζ = 0` na faixa |

## 2. Toro

`𝕋(s) = ((R + r cos 2πσ) cos(2πt/T), (R + r cos 2πσ) sin(2πt/T), r sin 2πσ)`, `R > r > 0`.

* Superfície exata; dupla periodicidade (perde `Re mod 1` e `Im mod T`); toro elevado `(𝕋(s), Im s)` injetivo na faixa.
* `R` = espelho `z ↦ −z`; `J` = espelho `y ↦ −y`; `S = 1 − s` = rotação de π em torno de `x`, com exatamente os
  pontos fixos `σ ∈ ½ℤ, t ∈ (T/2)ℤ` (quatro por célula: o quociente é a "fronha" de 4 pontos cônicos).
* A linha crítica é o **equador interno** (raio `R − r`) e, na faixa, `z = 0 ⟺ Re s = ½`. Logo
  **`rh_iff_equador`: HR ⟺ todo zero não trivial cai no equador interno** (reformulação exata, não prova).
* Curvatura (Brioschi, a partir de `E = r², F = 0, G = (R + r cos θ)²` derivados da imersão):
  `K = cos θ / (r(R + r cos θ))`. Na linha crítica `K = −1/(r(R − r))`, **o mínimo global**; a região `K < 0` é
  exatamente a faixa central `¼ < σ < ¾`. Área `4π²Rr`; curvatura total `0` (Gauss–Bonnet, χ = 0).
* Par simétrico: distância `2r|sin 2πδ|`. **Reencontro artificial**: em `λ = ½` os ramos `0 + iγ` e `1 + iγ`
  coincidem no toro, mas seguem zeros distintos e simples no plano.
* Fluxo de cruzamento `Φ_λ(s) = s + λ`: grupo a um parâmetro; os zeros de `G_λ` são órbitas dos críticos;
  no toro atravessa o equador **transversalmente** (velocidade vertical `−2πr`); conjugado por `T` vira vertical.

Constantes (R = 3, r = 1, T = 28; `closed_math.json`): raio do equador interno 2; `K(π) = −0,5`;
`K(0) = 0,25`; área 118,4352528131 = 4π²·3; Gauss–Bonnet numérico −2·10⁻¹⁵; distância do par
½ ± 0,1 + 14i: 1,1755705046 (= 2 sin(0,2π)); corda esférica do mesmo par 0,0020277809 (ângulo 0,0020277812).

## 3. Tempos verbais

`Afirmacao` carrega enunciado, tempo e a testemunha que o tempo **exige** (o tipo obriga):
*perfeito* (foi provado ⇒ prova), *negado* (foi refutado ⇒ prova da negação), *condicional* (seria, se `H` ⇒ `H → P`),
*futuro* (aberto ⇒ nada), *presente* (observado numericamente ⇒ nada). `futuro_vazio`: `P` e `¬P` cabem no futuro.
Catálogo: classificação (perfeito), "simetria força a linha" (negado), HR ⟺ ZE = ∅ (perfeito), zeros no equador
interno (condicional a HR), HR (futuro).

## 4. Redução terminal (`ATK/RHTerminal.lean`)

* `T25`: HR ⟺ ζ ≠ 0 em `S₊ = {½ < Re < 1}` (e o mesmo para ξ).
* `cobertura`: `S₊ = ⋃_{n≥5} K_n`; `K_n` compacto e não vazio.
* `rh_iff_minimos`: HR ⟺ para todo `n ≥ 5`, `|ζ|` tem mínimo positivo em `K_n`.
* `rh_iff_delta`: com `η(s) = (1 − 2^{1−s}) ζ(s)` e `δ_n = min_{K_n} |η|` (mínimo atingido, `delta_atingido`),
  **HR ⟺ ∀ n ≥ 5, δ_n > 0**; `eta_zero_iff`: em `K_n`, `η = 0 ⟺ ζ = 0` (o fator `1 − 2^{1−s}` não se anula para `Re s < 1`).
* `criterio_aproximacao` (T28) e `T31_iff`: HR ⟺ existe aproximante com `E_n < L_n` em cada `K_n`.
* **Aproximante explícito, independente de HR**: `EM_uniforme`: `|ζ − EM_{N,M}| ≤ E(n,N,M)` em todo `K_n`, com
  `E(n,N,M) = (√(1+n²)+M)^M/M! · C_M · N^{½−M}/(M − ½)` e `Eb_tende_zero`.
* **`rh_iff_criterioEM`: HR ⟺ ∀ n ≥ 5, ∃ N M L, L ≤ |EM_{N,M}| em K_n e E(n,N,M) < L.**

Instâncias com `n` fixo (tempo *presente*, grade numérica, `N = 40`, `M = 10`):

| n | E(n,40,10) (cota provada) | min \|EM\| em K_n (grade) |
| --- | --- | --- |
| 5 | 2,9·10⁻¹⁰ | 0,574 |
| 10 | 5,0·10⁻⁹ | 0,550 |
| 15 | 4,6·10⁻⁸ | 0,0526 |
| 20 | 2,8·10⁻⁷ | 0,0394 |
| 30 | 5,0·10⁻⁶ | 0,0261 |

A queda em `n = 15` é o primeiro zero (14,1347…): `K_15` chega a `t = 15` e passa a `1/n` dele.
Cada linha é uma conta finita; transformá-la em certificado do kernel exige avaliação intervalar de ζ em
retângulos (fase 3). O quantificador `∀ n` é a própria HR: **não há aqui prova da desigualdade universal**.

## 4b. Outras superfícies e a ponte espectral (`ATK/ClosedMathGeometrias.lean`)

* Helicoide `(σ cos t, σ sin t, t)` (injetivo em `σ > 0`; a linha crítica é a hélice de raio ½), cilindro
  parabólico `(σ, t, σ²)` e sela `(σ, t, σ² − t²)` (injetivos), hiperboloide `(cosh t cos σ, cosh t sin σ, sinh t)`
  (injetivo na faixa): o transporte `F̃(Φ s) = F(s)` preserva zeros e classes.
* `margem_invariante`: os valores de `|F̃|` em `Φ(K)` são os de `|F|` em `K`; logo a margem `inf |F|` **não muda**
  com a geometria.
* `toro_sem_transporte`: no toro (T = 1) nenhuma `F̃` reproduz `G_{0,1}` — `½ + i` (zero) e `½ + 2i` (não zero)
  têm a mesma imagem; é preciso guardar o rótulo.
* `hilbert_polya` (condicional): se todo zero não trivial for `½ + iμ` com `μ` autovalor de um operador simétrico,
  então HR; `mu_real_iff`: `μ = (ρ − ½)/i` é real ⟺ `Re ρ = ½`. Nenhum operador assim é conhecido.

## 4c. Laplaciano do toro plano (`ATK/EspectroToro.lean`)

`e_{m,n}(x, y) = e^{i(mx+ny)}` é `2π`-periódica e `−Δ e_{m,n} = (m² + n²) e_{m,n}` (derivadas segundas provadas):
um operador com espectro real `≥ 0`. Com `hilbert_polya`, só faltaria a correspondência completa entre zeros e
espectro — que este operador não tem: autovalores inteiros forçariam `Im ρ ∈ ℤ` (`espectro_inteiro_forca`).

## 4d. Hexagrama, `K₆` e energia horizontal (`ATK/Hexagrama.lean`)

Vértices `V_k = R e^{ikπ/3}` com `V_{k+3} = −V_k` (três eixos pelo centro, soma zero); pentagrama `Σ ζ^k = 0`;
`K₆` com 15 arestas, 20 triângulos, 15 quadriláteros e 3 retângulos; adjacência com `A·1 = 5·1` e `A v = −v`
(`Σ v = 0`), laplaciano com autovalores `0` e `6`; energia `E = 6 Σ |z_j − z̄|²`. Para os pontos `±d ± it, ±it`:
**`E = 24d² + 36t²`** (a conta `16d² + 24t²` do texto estava errada) e `E_x = 24d²`. `rh_iff_energia`:
HR ⟺ `24 (Re ρ − ½)² = 0` em todo zero não trivial — reformulação; a energia é sempre `≥ 0` e isso não a anula.

## 4e. Polinômios de Jensen, Turán, Toeplitz e momentos (`ATK/JensenTuran.lean`)

Variável quadrática `x = (s − ½)²`, `Θ(x) = ξ(½ + √x) = Σ aₙ xⁿ`, `γₙ = n!·aₙ`.

* `xiE`: `ξ(s) = s(s−1)/2 · Λ₀(s) + ½`, inteira; **zeros de `ξ` = zeros não triviais de `ζ`** (`xiE_zero_iff`).
* **HR ⟺ `(ρ − ½)²` real e negativo** (`rh_iff_quadrado`) **⟺ todos os zeros de `Θ` são reais negativos**
  (`rh_iff_Theta`) — a forma de Laguerre–Pólya.
* `turan_normalizacao`: `γ_kγ_{k+2} ≤ γ_{k+1}² ⟺ (k+2)a_ka_{k+2} ≤ (k+1)a_{k+1}²`; `jensen_grau2`: `J_{2,k}` só tem
  raízes reais ⟺ Turán; `disc3_jensen`: discriminante de `J₃` = `27[4(γ₁²−γ₀γ₂)(γ₂²−γ₁γ₃) − (γ₁γ₂−γ₀γ₃)²]`, e
  `turan3` (raízes reais ⇒ Turán de ordem 3); `toeplitz2_iff_turan`.
* **Momentos**: `momentos_logconvexos` (Cauchy–Schwarz, toda medida positiva: `M_{n+1}² ≤ MₙM_{n+2}`);
  `turan_iff_momentos`: com `γₙ = C qⁿ n! Mₙ/(2n)!`, **Turán ⟺ `(2n+1)MₙM_{n+2} ≤ (2n+3)M_{n+1}²`** — um
  Cauchy–Schwarz *reverso* com folga `(2n+3)/(2n+1)`; `cs_nao_implica_turan`: a medida `¾δ₀ + ¼δ₂` é log-convexa e
  viola Turán.
* **Correção ao texto**: a positividade total deve ser pedida para **`aₙ`** (Aissen–Schoenberg–Whitney–Edrei), não para
  `γₙ`. `tp_a_nao_passa_gamma`: para `(1+X)³`, `D_{3,1}(a) = 10` mas `D_{3,1}(γ) = −3`. Para `ξ`, numericamente
  `D_{3,1}(γ) < 0` — **TP∞(γ) é falsa**, então essa rota não pode fechar; para `aₙ` todos os menores testados
  (`r ≤ 8`, `k ≤ 24`) são `≥ 0`.

Numérico (`codigo/jensen.py`, só biblioteca padrão, 130 dígitos; `dados/jensen.json`; 11 testes em
`testes/test_jensen.py`): `a₀ = ξ(½) = 0,4971207781883141…`, `a₁ = 0,0114859721…`; troca de sinal de `Ξ` em
`t₁ = 14,13472514173469379045725198357`; Turán vale para `k ≤ 58` (mínimo relativo 0,008); Turán de ordem 3 vale;
sanduíche dos momentos vale para `n ≤ 58`; `J^{d,n}` hiperbólico (Sturm exato) para `d ≤ 8`, `n ≤ 30` — coerente com
Griffin–Ono–Rolen–Zagier (todo `n` para `d ≤ 8`; todo `d` para `n` grande). Nada disso prova HR: HR exige todos os
`d` e todos os `n`.

## 4f. O primeiro zero, certificado no kernel (`ATK/ZeroCertificado.lean`, `ATK/ZeroCritico.lean`)

**`zero_na_linha`**: existe `ρ` com `ζ(ρ) = 0`, `0 < Re ρ < 1`, **`Re ρ = ½`**, `|ρ − (½ + 14,1347251417 i)| ≤ 10⁻⁶`,
e `ρ` é o único zero de `ζ` nesse disco. Incondicional, só axiomas padrão.

1. `mem_zetaI`: `ζ(½ + it)` num retângulo racional — Euler–Maclaurin `N = 30`, `M = 10` (resto ≤ 5,48·10⁻⁹,
   `ATK/EMGeral.lean`), `n^{−s} = n^{−½}e^{−it log n}` com `log n` (série de atanh), `e^{iθ}` (Taylor + redução por
   `2π`), `√n` (certificado), Bernoulli `B₂…B₁₀` provados; tudo calculado por **`decide +kernel`** (`cert_ok`).
2. Retângulos: `ζ(z₀) ∈ [−5,52; 5,53]·10⁻⁹ + i[−5,55; 5,50]·10⁻⁹`;
   `ζ(z₀ + 10⁻⁵ i) ∈ [−1,2525; −1,2414]·10⁻⁶ + i[7,8274; 7,8385]·10⁻⁶`; `c = 0,78330 + 0,12470 i` (`|ζ'(ρ₁)| ≈ 0,793`).
3. `cota_grosseira`: `|ζ| ≤ 240` em `|s − z₀| ≤ 2/5` (`EM_{1,1}`); Cauchy duas vezes: `|ζ''| ≤ 240/0,19² ≈ 6648`.
4. `deriv_menos_c`: `|ζ'(z₀) − c| ≤ F₂δ + (r₀ + r₁)/δ`; `norm_deriv_g`: `|1 − ζ'(z)/c| ≤ ½` no disco (0,0753 ≤ 0,3916);
   `g_maps`: `g(z) = z − ζ(z)/c` leva o disco nele mesmo (1,1·10⁻⁸ ≤ 3,9·10⁻⁷); Banach ⇒ zero e unicidade.
5. `torcao_bola` + `torcao_mem_Z`: `ρ ↦ 1 − ρ̄` preserva o disco e os zeros; o zero é único ⇒ fixo ⇒ `Re ρ = ½`.

`ATK/ZeroCertificadoAplicado.lean` descarrega a hipótese "existe um zero" de `linha_forcada`, `nenhuma_outra_reta`,
`eixo_unico`, `incognita_resolvida` e `centro_exato` (estes dois para `T ≥ 15`). **Um zero na linha não é HR**: HR
fala de todos os zeros; o mesmo método certifica qualquer zero isolado, nunca infinitos.

## 4g. B18: ordem sob mudança de coordenadas (`ATK/OrdemCoordenadas.lean`)

`ordem_coordenadas`: `φ` analítica em `a` com `φ'(a) ≠ 0` ⇒ `ord_a(F ∘ φ) = ord_{φ(a)}(F)`; `ordem_composicao`: em geral
as ordens multiplicam (`ord_{φ(a)}F · ord_a(φ − φ(a))`); `transporte_ordem` (B17 + B18): no transporte
`G(φ(s)) = u(s)F(s)` com `u(a) ≠ 0` e `φ'(a) ≠ 0`, o zero de `G` em `φ(a)` tem a ordem do zero de `F` em `a`.

## 4h. `δ₅ > 0` certificado (`ATK/DeltaCertificado.lean`)

`zeta_K5`: **`|ζ(s)| ≥ 1/10` em todo `K₅ = {7/10 ≤ Re s ≤ 4/5, |Im s| ≤ 5}`**; `eta_K5`: `|η(s)| ≥ (2^{1/5} − 1)/10`;
**`delta_cinco_pos : 0 < delta 5`** e `minimo_K5` (o `m > 0` de `rh_iff_minimos` para `n = 5`). Incondicional.

* Cobertura de `K₅ ∩ {Im ≥ 0}` por 450 discos de raio 3/125 (3 colunas `σ_c = 43/60, 45/60, 47/60` × 150 linhas
  `t_c = (2k+1)/60`); `Im < 0` por `ζ(s̄) = conj ζ(s)` (Mathlib).
* Em cada disco: `ζ = EM_{10,1} + (EM_{10,4} − EM_{10,1}) + (ζ − EM_{10,4})`; `|EM_{10,1}(c)|²` por intervalos racionais
  (`n^{−σ}` por certificados de raiz `lo^{60} n^p ≤ 1 ≤ hi^{60} n^p`, `e^{iθ}`, `log n`); a variação no disco pelo valor médio
  termo a termo (`|d/dw n^{−w}| = log n · n^{−Re w}`, e o termo do polo `10^{−w}(10/(w−1) − ½)`); Bernoulli e resto por
  cotas explícitas. Verificado: `(1/10 + ρL + |corr| + |R|)² ≤ |EM_{10,1}(c)|²` nos 450 discos (18 blocos `decide +kernel`).
* Numericamente `min_{K₅} |ζ| ≈ 0,574` (em `0,7 + 2,67i`); a margem certificada pior é `|A|² − perda² ≈ 0,25`.

Isto é o caso `n = 5` de `rh_iff_delta`. Cada `n` fixo é uma conta finita (para `n ≤ 13`, `min |ζ| ≈ 0,55`; `K₁₄` já
encosta no primeiro zero, `min |ζ| ≈ 0,12`); **o quantificador "para todo `n`" é HR e continua aberto**.

## 4i. Critério de Li, núcleo algébrico (`ATK/LiCriterio.lean`)

`w(ρ) = 1 − 1/ρ` leva a linha crítica no círculo unitário: `|w| = 1 ⟺ Re ρ = ½`, `|w| < 1 ⟺ Re ρ > ½`,
`|w| > 1 ⟺ Re ρ < ½` (`w_unitario_iff`, `w_dentro_iff`, `w_fora_iff`); **HR ⟺ todo zero não trivial tem
`|1 − 1/ρ| = 1`** (`rh_iff_li_unitario`); sob HR cada parcela `1 − w(ρ)ⁿ` tem parte real `≥ 0` (`rh_parcelas`); fora do
círculo `|1 − wⁿ| → ∞` (`parcela_ilimitada`); a simetria `ρ ↦ 1 − ρ̄` vira `w ↦ 1/w̄` (`w_torcao`). A soma
`λₙ = Σ_ρ [1 − w(ρ)ⁿ]` sobre todos os zeros (Keiper–Li) não está no Mathlib.

Numérico (`codigo/li.py`, `dados/li.json`, 3 testes): `λₙ` a partir de `ξ(1+u) = Θ(¼ + u + u²)`;
`λ₁ = 0,02309570896612103381` = `1 + γ/2 − ½ log 4π` (20 dígitos), `λ₂ = 0,0923457352…`, e `λ₁ < … < λ₂₀ = 8,769…`,
todos positivos — coerente com HR, sem prová-la.

## 4j. Pendentes formalizados (rodada 6)

Tudo abaixo compila no kernel com só `propext`, `Classical.choice`, `Quot.sound` (319 teoremas novos; total 6011).

**Simetrias e projetores** (`ATK/Projetores.lean`): `P± = (1 ± S)/2` para `S² = 1` (idempotentes, ortogonais, soma 1,
`SP± = ±P±`, decomposição única); projetores de ordem `m`, `P_j = (1/m)Σ ω^{−jk}S^k` (`Σ P_j = 1`, `SP_j = ω^jP_j`,
`P_jP_l = δ_{jl}P_j`); `⋆` de Hodge em `Λ²ℝ⁴ ≅ ℝ⁶` (`⋆⋆ = 1`, isometria simétrica, `F = F⁺ + F⁻` ortogonal,
`⟨F,⋆F⟩ = |F⁺|² − |F⁻|²`, **Bogomolny** `|⟨F,⋆F⟩| ≤ |F|²` com igualdade ⟺ `F = ±⋆F`); gap 2×2 `Δ = √((a−c)²+4b²)` e
`Δ(H+V) ≥ Δ(H) − Δ(V)`; descida infinita abstrata; somas de pares; limites iterados não comutam; `r^{2−d}` radial.
**BSD** (`ATK/BSDCoefLider.lean`): `ord_a f = r` ⟺ `f^{(k)}(a) = 0` (`k < r`) e `f^{(r)}(a) ≠ 0`; `L` não identicamente
nula ⇒ ordem finita em `s = 1` e **`L^{(r)}(E,1)/r! ≠ 0`**.

**Gram exato** (`ATK/GramExato.lean`, `ATK/GramDois.lean`, `ATK/GamaCotas.lean`):

* `G₁₁ = ∫₀^∞{1/t}² = log 2π − γ` (degraus + Stirling); `D₁ = 1 − (1−γ)²/(log 2π − γ)`; `G_kk = G₁₁/k`;
  `G₁₂ = ∫₀^∞{1/t}{1/(2t)} = ¾(log 2π − γ) − ¼ log 2` (somas de pares em forma fechada + Stirling); `D₂` exato.
* `γ` certificado: `u_n = H_n − log(n+½) − 1/(24(n+1)²)` decresce, `l_n = H_{n+1} − log(n+3/2) − 1/(24(n+1)(n+2))`
  cresce, ambas `→ γ`: **`0,5772156 < γ < 0,5772163`** (a Mathlib só tem `½ < γ < ⅔`); `1,1447295 < log π < 1,1447300`.
* Aritmética intervalar: **`0,85821 < D₁ < 0,85822`**, **`0,2899 < D₂ < 0,2900`**, logo **`D_∞ ≤ D₂ < 0,29`** — a primeira
  cota numérica de `D_∞` provada sem hipótese (a do texto, `0,29670246`, vale); **`0,04619 < C₀ = 2 + γ − log 4π < 0,04620`**.
* Cauda `Σ_{k≥0}(D_{N+k} − D_{N+k+1}) = D_N − D_∞`; ganho uniforme ⟺ `D → 0` (o ganho só estrito não basta:
  `D_N = ½ + 1/(N+1)`); Cauchy–Schwarz para `SemiInner`; **certificado ortogonal**: `h ⊥ ρ_k` ⇒ `⟨χ,h⟩²/‖h‖² ≤ D_N`, e
  um tal `h` com `⟨χ,h⟩ ≠ 0` refutaria HR (nenhum é conhecido); `0 ≤ G_ij ≤ (log 2π − γ)/√(ij) < 2/√(ij)`.
* Reformulações (`ATK/Reformulacoes.lean`): HR ⟺ `bᵀG_N⁻¹b → 1` ⟺ `∀ε ∃N,c: resíduo < ε` ⟺ certificados `≤ 2⁻ʲ`.

**Barreira e modelos** (`ATK/BarreiraModelos.lean`): `∂_βB = B(2/t + 2(β−1)/b − 4β/a)`, `∂_γB = 2γB(1/b − 2/a)`,
`∂_βB(½) = 2/(γ²+¼)`, `B(½+δ)/δ → 2/(γ²+¼)`, `γ²B → 2β − 1`; tabela (`B(0,6; 14,13) ≈ 0,000998` etc., todas `< 0,2967`);
`F(s) = (s−½)ζ(s)`; `ε_N = (ac+bd)/(c²+d²) − ½`; modelo `a + C/log x` (`f′ < 0`, `f″ > 0`, integrais, `f → a`);
**ajuste de dois pontos**: com `D₂₅₆ = 0,0082337162772`, `D₈₀₀₀ = 0,0050691202`, `D₂₅₆ log 256 > D₈₀₀₀ log 8000`, o intercepto é
`a ∈ (−2,92·10⁻⁵, −2,90·10⁻⁵) < 0`: nenhum modelo `a + C/log N` com `a ≥ 0` passa pelos dois pontos.

**`ξ` analítica** (`ATK/XiAnalitica.lean`): `ord ξ = ord ζ` na faixa; **zeros triviais simples** (`ζ′(−2k) ≠ 0`,
ordem 1); `ξ′/ξ = 1/s + 1/(s−1) − ½ log π + ½ψ(s/2) + ζ′/ζ`; `log|ξ|` harmônica fora dos zeros; paridade de
`F(z) = ξ(½+z)` (`F^{(n)}(−z) = (−1)ⁿF^{(n)}(z)`, `F(it) ∈ ℝ`, `F′(it) ∈ iℝ`, `A` par e `B` ímpar em `d`) e integração
horizontal `B = d∫₀¹ Im F′(vd+it)dv`; num zero, `F(it)² ≤ d²∫₀¹(Re F′)²`; **teste do disco de Jensen** (zero em
`B(c,R)` ⟺ média de `log|f|` > `log|f(c)|`) e HR ⟺ igualdade em todo disco da metade direita; **critério de sinal**
(`Re ξ′/ξ > 0` em `Re s > ½` ⇒ HR; só essa direção); energia `H = 24Σm(Re ρ−½)²`; fator Γ em `K_n`.
**Critério de `η`** (`ATK/EtaCriterio.lean`): `η − P_M = −s(H_{2M} − 2^{1−s}H_M)`, `|η − P_M| ≤ 3|s|(2M)^{−σ}/σ`, e
**HR ⟺ ∀n ≥ 5 ∃M: 6√(1+n²)(2M)^{−1/2} < inf_{K_n}|P_M|** (cada `n` é uma conta finita; o `∀n` é HR).
**`|F|²`** (`ATK/LaplacianoModulo.lean`): `∂_σ|F|² = 2Re F′F̄`, `∂_t|F|² = −2Im F′F̄`, `Δ|F|² = 4|F′|²`; cálculo
elementar de 18f9cbdc (`θ′`, `w(−2n)`, `w(½+it)`, `∂d`, `∫_T^∞ = 1/T`).

**Geometria** (`ATK/GeometriaExtra.lean`): K₆ (`x = d(1,−1,−1,1,0,0)`, `y = t(1,1,−1,−1,1,−1)`, somas, normas,
ortogonalidade, `vᵀLv = Σ_{i<j}(vᵢ−vⱼ)²`, autovalores só `0` e `6`, `xᵀLx = 24d²`, `yᵀLy = 36t²`, rotação, área `4|dt|`);
métricas `(E,F,G)` do helicoide, cilindro parabólico, sela e hiperboloide com `EG − F² > 0`; Fourier ortonormal no
toro; energia cinética gaussiana `½∫(ψ′)² = α/4`.

**Zeros 2 e 3** (`ATK/ZeroSegundo.lean`, `ATK/ZeroTerceiro.lean`, `ATK/TresZeros.lean`): mesmo método do primeiro zero
(Euler–Maclaurin intervalar com `N = 40`, `|ζ| ≤ 420` no disco, contração, simetria): **`ρ₂ = ½ + iγ₂`,
`|γ₂ − 21,0220396388| ≤ 10⁻⁶`, e `ρ₃ = ½ + iγ₃`, `|γ₃ − 25,0108575801| ≤ 10⁻⁶`**, cada um o único zero no seu disco;
`γ₁ < γ₂ < γ₃` e os seis zeros `½ ± iγ_k`. Isto não exclui outros zeros com `0 < γ < 26` (seria `N(26) = 3`).

Numérico: `codigo/gram2.py`, `dados/gram2.json`, `testes/test_gram2.py` (10 testes): `γ` cercado, `G₁₂` pela forma
fechada `Pc(K)` (igual à soma direta dos degraus; erro `≈ 0,1458/K`), `D₁ = 0,858212051`, `D₂ = 0,289964574`,
`C₀ = 0,046191418`, intercepto `−2,9122·10⁻⁵`, tabela da barreira, zeros 2 e 3 pela troca de sinal de `Ξ`.

## 4k. Erros dos textos (com contraexemplo ou teorema)

| Texto | Afirmação | Situação | Onde |
| --- | --- | --- | --- |
| 963449d2 | `G₁₁ = log 2π − γ − 1` | falso (esquece `∫₁^∞ t⁻² = 1`); seu `D₁ ≈ 0,31426` é o mínimo do resíduo local | `GramDois.G11_ne_texto1`, `ErrosGram.residuo_split`, `D1texto_minimo_local` |
| 1fb0a5dd | `G₁₁ = log 2` | falso (`G₁₁ − log 2 = log π − γ > 0`); `D₁ ≈ 0,7421` vem dele | `GramDois.G11_ne_log2`, `ErrosGram.D1log2_cotas` |
| 9654e97e | `b_k = (1 − γ + log k − H_{k−1})/k` | falso: é `b_k − H_{k−1}/k`, `< 0` para todo `k ≥ 4` | `GramDois.b4_texto_errado`, `ErrosGram.bTexto_neg` |
| 9e0c6efb | coeficiente `(p/i + q/j)` na integral por pedaços; `G₁₂ ≈ 0,7722083` | falso: `i=1, j=2, [2,3]` daria `< 0`; `G₁₂ > 0,7722084` | `GramDois.contraexemplo_pedaco`, `ErrosGram.G12_cotas` |
| 56e0dfa6 | `B = d∫₀¹ Re F′` | falso: é `Im F′` (`F = z²` e o próprio `ξ`) | `XiAnalitica.B_integral`, `ErrosAnaliticos.texto_Re_falso_para_xi` |
| 8af24fb4 / bef58a09 | `λ ≠ 0` ⇒ quatro zeros simples; `λ = 0` ⇒ dois duplos | falta `γ ≠ 0`: tabela 1 / 2 / 4 | `ErrosAnaliticos.multiplicidade_tabela` |
| f1754ca5 / 0e761a7c | Jensen montado com `aₙ` | normalização errada: Turán(`γ`) ⇒ Turán(`a`), não o contrário | `GeometriaExtra.jensen_a_hiperbolico`, `ErrosAnaliticos.turan_gamma_implica_a`, `jensen_a_falha_gamma_detecta` |
| 0e761a7c | `TP∞(γ)` caracteriza zeros reais negativos | falso: `(1+x)³` tem todos os 2×2 `≥ 0` e `D₃,₁(γ) = −3`; o certo é `TP∞(aₙ)` | `ErrosAnaliticos.tp_binomial`, `ToeplitzTN.tn_de_raizes` (⇐), **`ASWReciproca.asw_iff`** (⟺, qualquer grau) |
| 425e4bc1 | "HR ⇏ O1" | mal posto: provar `¬(HR → Q)` provaria HR; alvo é `D_N → 0` | `GeometriaExtra.nao_implica_prova_rh`, `ErrosAnaliticos.alvo_correto` |
| 99d52102 | ajuste `D_N ≈ a + C/log N` com os dois valores | intercepto negativo; os dados só dizem `D_N log N < C₀` e decrescente | `BarreiraModelos.sem_modelo_nao_negativo`, `ErrosGram.E12_corrigido` |
| e1644f4c / f1754ca5 | `Ξ(t) = ∫Φ(u)cos(tu)du` | fator 2: **`Ξ(t) = 2∫₀^∞Φ(u)cos(tu)du`** | `XiPhi.Xi_eq_dois_int_Phi`, `sem_fator_dois_falso` |
| 48cacf85 | `HR ⟺ ∀T > 2, M₊(T) > 0` | falso para `2 < T < 4` (região vazia, `M₊ = 0`); correto com `T ≥ 4` | `ErrosAnaliticos.texto_M_falso`, `rh_iff_Mplus` |
| 7a43314b | `0,831908` (`1/ζ(3)`); `19,739209` "volume da esfera unitária" | `1/ζ(3) ∈ (0,831907; 0,8319075)`; `2π²` é a área de `S³` | `ErrosConstantes.texto_0831908_errado`, `area_S3` |

## 4l. O que continua pendente (não formalizado aqui)

Ganho de Schur exato e Tikhonov; `D_∞` como resíduo ortogonal em `L²`; o núcleo `ψ` fora da linha; o princípio do
argumento em círculos; a identidade de Green (a) no retângulo; `N(14) = 0` (cobertura certificada, pesada); Edrei na
forma completa (fator `e^{γz}`, funções meromorfas, ordem `≥ 1`); no fluxo de de Bruijn–Newman, os teoremas de de
Bruijn (`1/2 ∈ S`, `S` fechado para cima), Newman (`S` limitado) e Rodgers–Tao (`Λ ≥ 0`), que entram como hipóteses
explícitas (o fechamento de `S` já está provado, §4t), e `e^{−tD²}` na classe de Laguerre–Pólya (o caso polinomial está
no kernel, §4r); Cauchy–Binet e Lindström–Gessel–Viennot (fechamento de TN por produtos, núcleos por caminhos); os
resultados incondicionais de Csordas–Norfolk–Varga (Turán) e Griffin–Ono–Rolen–Zagier; a fórmula explícita e a
positividade de Weil; nas classes de zeros (§4v), a certificação finita de `m₄ > 0` (aritmética intervalar de `ζ` em
`σ = 1/4`), o teorema de Hardy (infinitos zeros na reta) e a infinitude dos zeros não triviais por Hadamard com zeros
complexos, o lema de Csordas (que daria `P(2)` para `Ξ`) e o multiplicador de Laguerre `q^{n²}` (que daria a ida do
fluxo de Toeplitz); a simplicidade dos zeros não triviais e a irracionalidade das suas ordenadas são conjecturas
independentes, `OPEN_MATH`; e, claro, HR (`D_∞ = 0`, `∀n δ_n > 0`, `Re ξ′/ξ > 0` em `Re s > ½`, **PF∞ dos
`aₙ`**) — todas as formas equivalentes continuam abertas. A **equivalência** HR ⟺ PF∞(aₙ) já está no kernel nas duas
direções (§4p–§4q); o que falta é a positividade total dos `aₙ` concretos, que é `OPEN_MATH`.

## 4m. Erros: explicação, correção e teoremas (rodada 7)

Três módulos — `ATK/ErrosGram.lean`, `ATK/ErrosAnaliticos.lean`, `ATK/ErrosConstantes.lean` — com 89 teoremas novos
(total 6100), só `propext`, `Classical.choice`, `Quot.sound`. Para cada erro da tabela §4k: **de onde vem**, **a
correção** e o que o kernel prova (refutação + versão corrigida). Nada disto prova ou refuta HR.

**E1 — `G₁₁ = log 2π − γ − 1` (963449d2).** *Origem*: é exatamente `∫_{(0,1]}{1/t}²dt`; falta a cauda
`∫₁^∞ t⁻²dt = 1` (para `t > 1`, `{1/t} = 1/t`) (`G11_partes`). *Consequência*: o resíduo verdadeiro é
`‖χ − xρ₁‖² = ∫_{(0,1]}(1 − x{1/t})² + x²` (`residuo_split`); o `D₁ = 1 − (1−γ)²/(log 2π − γ − 1) ≈ 0,31426` do texto é o
mínimo só da parte local, atingido em `x ≈ 1,622` (`D1texto_minimo_local`) — não é um `D₁`. *Correção*:
`G₁₁ = log 2π − γ`, `D₁ = 1 − (1−γ)²/(log 2π − γ) ∈ (0,85821; 0,85822)`; o valor do texto fica mais de `0,54` abaixo
(`E1_corrigido`, `D1texto_cotas`, `D1texto_lt_DN1`).

**E2 — `G₁₁ = log 2`, `D₁ ≈ 0,7421` (1fb0a5dd).** *Origem*: o `0,7421` é coerente com o `G₁₁` errado,
`1 − (1−γ)²/log 2 ∈ (0,74212; 0,74213)` (`D1log2_cotas`); não há derivação de `log 2` como `∫{1/t}²`. *Correção*:
`G₁₁ − log 2 = log π − γ > 0`, e esse `D₁` subestima o verdadeiro (`D1log2_lt_DN1`).

**E3 — `b_k = (1 − γ + log k − H_{k−1})/k` (9654e97e).** *Origem*: a fórmula é `b_k − H_{k−1}/k` (`bTexto_eq`).
Escrevendo `b̃_{n+1} = (1 − γ − (H_n − log(n+1)))/(n+1)` (`bTexto_eq_seq`) e usando que `H_n − log(n+1)` cresce para `γ`
(Mathlib), `H₃ − log 4 = 11/6 − 2 log 2 ≈ 0,4470 > 1 − γ ≈ 0,4228` dá **`b̃_k < 0` para todo `k ≥ 4`** (`bTexto_neg`),
contra `b_k > 0` (`bTexto_contradiz`). Os valores listados no texto: `k = 2` (`0,0579657578`) bate com a fórmula;
`k = 3` (`0,0072177332`; a fórmula dá `0,0071322`) e `k = 4` (`−0,0060668825`; a fórmula dá `−0,0060637`) não
(`bTexto_valores`). *Correção*: `b_k = ∫₀¹{1/(kt)}dt = (log k + 1 − γ)/k > 0`.

**E4 — integral por pedaços e `G₁₂` tabelado (9e0c6efb).** *Origem*: `p` e `q` trocados no termo logarítmico; os
coeficientes `q/i + p/j` (certo) e `p/i + q/j` (texto) só coincidem quando `(p − q)(1/i − 1/j) = 0`
(`coef_coincide_iff`), isto é `p = q` ou `i = j` — por isso o erro não aparece na diagonal. Contraexemplo:
`contraexemplo_pedaco` (rodada 6). *Valor tabelado*: `G₁₂ ≈ 0,7722083` está abaixo do intervalo certificado
`(0,7722084; 0,7722094)` (`G12_cotas`; o exato é `0,77220926`); como o integrando é `≥ 0`, toda soma parcial
`Pc(K) + ½` fica por baixo (`truncado_por_baixo`): o valor do texto é compatível com truncar a série (numericamente o
erro é `≈ 0,1458/K`, o que põe o `0,7722083` em `K ≈ 1,5·10⁵`).

**E5 — `B = d∫₀¹ Re F′` (56e0dfa6).** *Origem*: `Re` e `Im` trocados nas equações de Cauchy–Riemann. *Correção*:
`∂_d Im F(d+it) = Im F′(d+it)` e `∂_d Re F = Re F′` (`cauchy_riemann_horizontal`), logo `B = d∫₀¹ Im F′`
(`XiAnalitica.B_integral`). *Refutações*: `F = z²` (`contraexemplo_derivada`: `∂_d Im F = 2`, `Re F′ = 0`); e **para
o próprio `F(z) = ξ(½+z)`**: como `Re F′(it) = 0`, a fórmula do texto daria `∂_d B(0,t) = 0` para todo `t`, logo
`F′(it) = 0` e `Ξ` constante — mas `Ξ(0) > 0` e `Ξ(γ₁) = 0` (`texto_Re_falso_para_xi`).

**E6 — multiplicidades na família de cruzamento (8af24fb4 / bef58a09).** *Origem*: falta a hipótese `γ ≠ 0`.
*Correção* (`multiplicidade_tabela`): o zero `½ + λ + iγ` de `G_λ` tem multiplicidade `1` se `λ ≠ 0` e `γ ≠ 0`, `2` se
exatamente um deles é `0`, `4` se `λ = γ = 0`.

**E7 — Jensen montado com `aₙ` (f1754ca5).** *Origem*: os polinômios de Jensen usam `γₙ = n!aₙ`. *Teoremas*: Turán para
`γ` implica Turán para `a` sempre (`turan_gamma_implica_a`), mas não o contrário (`turan_a_nao_implica_gamma`,
`a = (1,1,1)`, `γ = (1,1,2)`): o teste com `aₙ` é estritamente mais fraco. Para `Θ = 1 + x + x²` (zeros `(−1 ± i√3)/2`,
fora de Laguerre–Pólya), o polinômio montado com `a` (`z² + 2z + 1`) é hiperbólico e o montado com `γ` (`2z² + 2z + 1`)
não (`jensen_a_falha_gamma_detecta`).

**E8 — `TP∞(γ)` (0e761a7c).** *Origem*: Aissen–Schoenberg–Whitney–Edrei é sobre os coeficientes de Taylor `aₙ`. Para
`(1+x)³` (só zeros reais negativos), **todos** os menores 2×2 de `a = (1,3,3,1)` e de `γ = (1,3,6,6)` são `≥ 0`, mas
`D₃,₁(a) = 10` e `D₃,₁(γ) = −3` (`tp_binomial`): Turán para `γ` não dá `TP₃(γ)`. *Correção*: o critério é `TP∞(aₙ)`
(ASWE). Para polinômios as duas direções estão no kernel (`ASWReciproca.asw_iff`, §4o); Edrei (séries infinitas) não.

**E9 — fator 2 em `Ξ(t) = ∫₀^∞Φ(u)cos(tu)du` (e1644f4c / f1754ca5).** *Origem*: o `2` é o jacobiano de `x = e^{2u}`
(`dx = 2e^{2u}du`). *Teoremas*: **`Ξ(t) = ½ − 2(t²+¼)∫₀^∞ψ(e^{2u})e^{u/2}cos(tu)du`** (`Xi_forma_u`, da fórmula de
Riemann já certificada); sem o `2` é falso (`fator_um_falso`: daria `Ξ(γ₁) = ½`); `∫_ℝΦcos = 2∫₀^∞Φcos` para `Φ` par
(`integral_par`); duas integrações por partes (`ibp_cos`, geral) dão, **condicionalmente** à regularidade e ao
decaimento de `g(u) = ψ(e^{2u})e^{u/2}`, `g′`, `g″`, a forma `Ξ(t) = (½ + 2g′(0)) + 2∫₀^∞(g″ − g/4)cos(tu)du`
(`Xi_forma_Phi`). *Não formalizado*: essas hipóteses, a identificação termo a termo `g″ − g/4 = Φ` e `½ + 2g′(0) = 0`
(equação funcional de `θ`). *Numérico*: `2∫₀^∞Φ = 0,497120778188314110 = ξ(½)` e `2∫₀^∞Φ(u)cos(γ₁u)du ≈ 6·10⁻²²`.

**E10 — `HR ⟺ ∀T > 2, M₊(T) > 0` (48cacf85).** *Origem*: a região `½ + 1/T ≤ σ ≤ 1 − 1/T` só é não vazia para `T ≥ 4`.
Para `0 < T < 4` ela é vazia (`R_vazio`), `M₊(T) = inf ∅ = 0` (`Mplus_vazio`), logo "`∀T > 2, M₊(T) > 0`" é **falso**
(`texto_M_falso`) e a equivalência do texto implicaria `¬HR` (`texto_equivalencia_daria_nao_rh`). *Correção*:
**`HR ⟺ ∀T ≥ 4, M₊(T) > 0`** (`rh_iff_Mplus`; `R(T)` compacta e `|ξ|` contínua). A versão com `K_n`, `n ≥ 5`, já estava
formalizada.

**E11 — "O1 ⇒ HR, mas HR ⇏ O1" (425e4bc1).** *Origem*: "HR ⇏ O1" como teorema é inalcançável — provar `¬(HR → Q)`
provaria HR. *Correção* (`alvo_correto`): `O1 ⇒ HR`, `O1 ⇒ D_N → 0` e `HR ⟺ D_N → 0`; o alvo mínimo é `D_N → 0`; se
HR implica O1 é desconhecido.

**E12 — ajuste `D_N ≈ a + C/log N` (99d52102).** *Origem*: dois pontos determinam `a` e `C`; o intercepto sai
`≈ −2,91·10⁻⁵ < 0 ≤ D_∞`. *O que os dados sustentam* (`E12_corrigido`, `produtos_abaixo_C0`, `razoes_C0`):
`D₈₀₀₀ log 8000 ≈ 0,04556 < D₂₅₆ log 256 ≈ 0,04566 < C₀ = 2 + γ − log 4π ≈ 0,04619` (razões `≈ 0,9863` e `≈ 0,9884`);
nem `C/log N` sozinho passa pelos dois pontos (`sem_C_unico`); o intercepto do ajuste não é estimativa de `D_∞`.

**E13 — tabela de constantes (7a43314b).** *`0,831908`*: errado na 6ª casa. `ζ(3) = Σ1/n³` (Mathlib), a soma exata até
`n = 60` (`decide +kernel`) e as caudas telescópicas `1/(2m²) + 1/(2m³)` (minorante) e `1/(2m(m−1))` (majorante) dão
`1,2020568 < ζ(3) < 1,2020570` e **`0,831907 < 1/ζ(3) < 0,8319075 < 0,831908`** (`inv_zeta_tres_cotas`,
`texto_0831908_errado`); o valor é `0,8319073726…` (densidade dos inteiros livres de cubos). *`19,739209`*: o número
está certo (`19,739208 < 2π² < 19,739209`, `dois_pi_quadrado_cotas`), o rótulo não: `2π²` é a **área de `S³ ⊂ ℝ⁴`**
(`d/dr(π²r⁴/2)` em `r = 1`, `area_S3`); o volume da bola unitária é `π²/2` em ℝ⁴ (`vol_bola_unit_quatro`) e `4π/3` em
ℝ³ (`rotulo_errado`). As demais constantes da tabela conferem.

Formatos: SMT-LIB 24–28 (caso base de `b̃_k < 0`, `G₁₂` tabelado, `D_N log N < C₀`, região vazia, `1/ζ(3)`) e as mesmas
cinco obrigações lineares em Coq e Isabelle. Numérico: `codigo/erros.py`, `dados/erros.json`, `testes/test_erros.py`
(8 testes).

## 4n. Fechamento: `Ξ = 2∫₀^∞Φcos` e ASW polinomial (rodada 8)

Os dois itens que ficaram parciais na rodada 7, agora no kernel (`ATK/XiPhi.lean`, `ATK/ToeplitzTN.lean`; 70 teoremas
novos, total 6170, só `propext`, `Classical.choice`, `Quot.sound`).

**`Ξ(t) = 2∫₀^∞ Φ(u)cos(tu)du`, sem hipóteses** (`Xi_eq_dois_int_Phi`), com
`Φ(u) = Σ_{n≥1}(4π²n⁴e^{9u/2} − 6πn²e^{5u/2})e^{−πn²e^{2u}}` — exatamente o `Φ` do texto e1644f4c, com o fator `2`.
Roteiro: `ψ(e^{2u})e^{u/2} = Σ_n h_{c}(u)`, `h_c(u) = exp(u/2 − ce^{2u})`, `c = πn²` (`hasSum_g`); derivadas exatas e
`h_c″ − h_c/4 = (4c²e^{4u} − 6ce^{2u})h_c` (`phiT_texto`); a cota-chave `(ce^{2u})^k h_c(u) ≤ 8e^{−c/2}e^{−u}`
(`u ≥ 0`, `k ≤ 2`, `cota`) dá integrabilidade, limites e somabilidade; integração por partes termo a termo
(`ibp_termo`, de `ErrosAnaliticos.ibp_cos`) e troca soma/integral (`K_tsum`, `Phi_tsum`) dão
`Ξ(t) = (½ + 2Σh_c′(0)) + 2∫₀^∞Φcos` (`Xi_forma_constante`); e **a constante é zero** (`constante_zero`): derivando
`ψ(x) = x^{−1/2}ψ(1/x) + (x^{−1/2} − 1)/2` (`psi_feq`, da equação funcional de `θ` no Mathlib) em `x = 1`, com
`ψ′(1) = −Σc e^{−c}` termo a termo (`hasDerivAt_psi_um`), sai `4Σc e^{−c} = ψ(1) + ½` (`quatro_T`). Sem o `2` a
identidade é falsa (`sem_fator_dois_falso`), e `2∫₀^∞Φ = Ξ(0) = ξ(½)` (`dois_int_Phi_meio`).

**Aissen–Schoenberg–Whitney, direção (⇐), qualquer grau** (`tn_de_raizes`): se as raízes de `p` são todas reais
(`#raízes = grau`) e `≤ 0` e o coeficiente líder é `≥ 0`, a matriz de Toeplitz `T(a)_{ij} = a_{i−j}` dos coeficientes é
**totalmente não negativa** (`Matrix.IsTotallyNonneg` do Mathlib: todos os menores). Prova: multiplicar por `X + r`
troca cada coluna por `r·col_j + col_{j+1}` (`toep_mulLin`); por multilinearidade o menor vira soma, com pesos `≥ 0`, de
menores de `T(a)` com colunas não decrescentes (`det_expand`), cada um `≥ 0` ou com coluna repetida (`tn_mulLin`);
indução no multiconjunto de raízes (`tn_prod`). Em particular **todo menor de Toeplitz `D_{r,m}(aₙ) ≥ 0`**
(`Dmin_nonneg_de_raizes`) e `T(1,3,3,1)` é totalmente não negativa (`tn_binomio_cubo`) — o enunciado correto de E8.

**Direção (⇒) em grau 2** (`tn_grau_dois_iff`): para `a₀, a₂ > 0`, `T(a₀,a₁,a₂)` é totalmente não negativa **⟺
`a₁ ≥ 0` e `a₁² ≥ 4a₀a₂`** ⟺ `a₀ + a₁x + a₂x² = a₂(x + r₁)(x + r₂)` com `rᵢ ≥ 0` (`fatora_iff`). A recíproca usa os
menores tridiagonais `D_{r+2} = a₁D_{r+1} − a₀a₂D_r` (`D_rec`, Laplace duas vezes) e um argumento sem trigonometria
(`cheb_neg`): para `x_{r+2} = 2c x_{r+1} − x_r`, `0 ≤ c < 1`, o invariante `x_{r+1}² − 2cx_{r+1}x_r + x_r² = 1` e a soma
telescópica `2(1−c)Σ_{k≤N}x_k = x₁ − x₀ + x_N − x_{N+1}` são incompatíveis com `x_r ≥ 0` para todo `r`. Para
`Θ = 1 + x + x²`, `D₃ = −1` (`um_x_x2`, `um_x_x2_nao_tn`).

*Não formalizado nesta rodada*: a recíproca em grau `≥ 3` — **fechada na rodada 9** (§4o, sem Pringsheim) — e o
teorema de Edrei para séries infinitas (teoria de Nevanlinna), que continua fora.
Formatos: SMT-LIB 29–30, Coq e Isabelle (constante de `θ`, tridiagonal). Numérico: `codigo/fechamento.py`,
`dados/fechamento.json`, `testes/test_fechamento.py` (4 testes): `4Σce^{−c} − ψ(1) − ½ ≈ 10⁻⁵¹`; menores até 4×4 de
`(1+x)³` e `(x+1)(x+2)(x+3)` todos `≥ 0`; com `a₁ = 1,9` e `1,99` o primeiro `D_r < 0` aparece em `r = 9` e `r = 31`.

## 4o. A recíproca de Aissen–Schoenberg–Whitney, qualquer grau (rodada 9)

`ATK/ASWReciproca.lean`: 33 teoremas novos, total 6203, só `propext`, `Classical.choice`, `Quot.sound`. Com a direção
(⇐) da rodada 8, **ASW para polinômios está completo no kernel**:

**Teorema** (`asw_iff`). Para `p ∈ ℝ[x]` com `p(0) > 0`: `T(coef p)` é totalmente não negativa
(`Matrix.IsTotallyNonneg`, todos os menores) **⟺** `p` tem `deg p` zeros reais contados com multiplicidade, todos `≤ 0`,
e coeficiente líder `≥ 0`; equivalentemente `p = c·∏(x − xᵢ)` com `xᵢ ≤ 0` (`asw_fatora`).

O que faltava no Mathlib e foi formalizado aqui:

1. **Colunas unitárias** (`det_unit_cols`): se a coluna `π_s` de `M` é `e_{ρ_s}`, então
   `det M = (−1)^{Σ(π_s+ρ_s)}·det M[ρᶜ, πᶜ]` (Laplace iterado, reindexação por `succAbove`).
2. **Identidade de Jacobi** para a inversa, forma sem sinal (`jacobi_init`): se `G·X = 1` e `A = DGD`,
   `D = diag((−1)^i)`, então `det X[R, {0..r−1}]·det A = det A[{r..}, Rᶜ]`. Prova: `W` com as colunas de `X` nas
   posições `R` e unitárias fora; `G·W` tem colunas unitárias nas posições `R`; duas vezes o item 1 e paridade.
3. **Seções de Toeplitz** (`sec_mul`: `T_N(φ)T_N(ψ) = T_N(φψ)`) e a **transferência** (`cc_de_tn`): com
   `B = 1/p(−x) = Σb_kx^k`, `G = T_N(p(−x))`, `X = T_N(B)`, tem-se `A = DGD = T_N(p)`, `det A = p(0)^N > 0` e os
   `A[{r..}, Rᶜ]` são menores de `T(p)`; logo **todo menor de `T(b)` com colunas iniciais é `≥ 0`** (`CCTN`).
4. **Uma raiz real, sem Pringsheim**: de `CCTN`, `b_k ≥ 0` e `b_kb_{k+2} ≤ b_{k+1}²` (`cc_log_concave`); um zero de
   `b` propaga-se para a frente (`cc_zero_prop`), e `B` não é polinômio (grau `≥ 1`), então `b_k > 0` para todo `k`
   (`b_pos`); `b_{k+1}/b_k` decresce para `L ≥ 0` (`ratio_tendsto`) e `b_{M+j}/b_M → L^j` (`ratio_pow`). Dividindo a
   recorrência `Σ(−1)^ip_ib_{M+n−i} = 0` por `b_M`: `Σ(−1)^ip_iL^{n−i} = 0`, logo `L > 0` (senão `p_n = 0`) e
   **`p(−1/L) = 0`** (`raiz_real`).
5. **Remoção do fator** (`cc_remove`): `b′ = (1 − Lx)b` também tem `CCTN`. Cada menor de `T(b′)` com colunas iniciais é
   o limite de `det T(b)[R ∪ {M+J+r}, {0..r}]/b_{M+J}` (continuidade do determinante) depois das operações de coluna
   `col_c ← col_c − L·col_{c+1}` (`opCol`, determinante 1): a última linha tende a `(0, …, 0, 1)` porque
   `b_{M+j+1}/b_M − L·b_{M+j}/b_M → L^{j+1} − L·L^j = 0`, e Laplace nela devolve o menor de `T(b′)`.
6. **Indução no grau** (`asw_rec`): `p = (x + 1/L)·q`, `q(0) = L·p(0) > 0`, `q(−x)·(1/L − x)B = 1`, e
   `(1/L − x)B = L⁻¹(1 − Lx)B` tem `CCTN` (`cc_smul`); `raízes(p) = {−1/L} + raízes(q)`.

Com isso E8 fica corrigido por inteiro no caso polinomial: o critério certo é `TP∞(aₙ)`, e ele **caracteriza** zeros
reais `≤ 0` (para `1 + x + x²`, `1/(1 − x + x²) = 1 + x − x³ − x⁴ + …` já tem `b₃ = −1 < 0`).

*Fora do kernel*: o teorema de Edrei (séries infinitas; teoria de Nevanlinna) e a fatoração de Hadamard de `Θ`. Aplicar o
critério à função de HR exigiria os dois e, mesmo assim, só reformularia HR — **nada aqui prova HR**.
Formatos: SMT-LIB 31, Coq e Isabelle (`inv_um_x_x2`). Numérico: `codigo/asw.py`, `dados/asw.json`, `testes/test_asw.py`
(4 testes): para `(x+1)(x+2)(x+3)`, `b = 1/6, 11/36, 85/216, …`, razões decrescentes para `L = 1` (raiz `−1`), menor
mínimo de colunas iniciais (`r ≤ 3`, 10 linhas) `= 1/60466176 > 0`, e `(1 − x)b` é exatamente `coef 1/((2−x)(3−x))`.

## 4p. Edrei para funções inteiras, PF∞ ⇒ HR, Weil e Hilbert–Pólya (rodada 10)

`ATK/EdreiInteira.lean` (30), `ATK/XiTP.lean` (17), `ATK/WeilMecanismo.lean` (5): 52 teoremas novos, total 6255,
só `propext`, `Classical.choice`, `Quot.sound`.

**Edrei (⇒) para funções inteiras, sem Nevanlinna** (`edrei_inteira`): se `F(z) = Σaₙzⁿ` é inteira
(`Σ|aₙ|Rⁿ < ∞` para todo `R`), `a₀ > 0` e `T(a)` é totalmente não negativa, **todo zero complexo de `F` é real e
negativo**. A prova de Edrei (1953) usa teoria de Nevanlinna; aqui ela é trocada por uma descida nos coeficientes
`b` de `B = 1/F(−x)`, estendendo a rodada 9:

1. `cc_de_tn_ser`: TN de `T(a)` ⇒ menores de colunas iniciais de `T(b)` `≥ 0` (Jacobi nas seções finitas).
2. `ev_mul_inv`: onde `Σb_kx^k` converge absolutamente, `F(−x)·B(x) = 1` (produto de Cauchy).
3. Se `F(w) = 0`: `b_k > 0` (`b_pos_ser`: se `b` se anulasse, `B` seria polinômio e `F` não teria zeros),
   `b_{k+1}/b_k ↓ L` com **`L·|w| ≥ 1`** (`raio_ser`: senão a série de `B` convergiria em `−w`) e **`F(−1/L) = 0`**
   (`raiz_ser`: convergência dominada de Tannery, com `b_{M−i}/b_M ≤ L^{−i}`).
4. `F = (1 + Lz)·G` com `G` inteira (`divLin`; `inteira_divLin` usa que a soma parcial de `F(−1/L)` é menos a cauda,
   `ev_divLin`), e `1/G(−x) = (1 − Lx)·B` tem de novo menores de colunas iniciais `≥ 0` (`cc_remove`).
5. Descida (`passo`, `descida`): se `w` não é real negativo, cada passo tira um zero real de módulo `≤ |w|` e baixa
   `b₁` de pelo menos `1/(a₀|w|)`; como `b₁ ≥ 0`, há no máximo `a₀|w|b₁` passos — absurdo.

**(⇐) para produtos de gênero 0** (`tn_genero0`): `αⱼ ≥ 0`, `Σαⱼ < ∞`, `a₀ ≥ 0` ⇒ `T(coef a₀∏(1 + αⱼz))` é TN
(multiplicar por `1 + αz` preserva TN, `tn_mul_one_add`; coeficientes monótonos e limitados por `a₀(Σαⱼ)ⁿ`,
`prodCoef_le`; TN é fechada por limites entrada a entrada, `tn_closed`, `tn_de_limite`).

**PF∞ dos coeficientes de Ξ ⇒ HR** (`XiTP.rh_de_tn`, com o `RiemannHypothesis` do Mathlib). `g(z) = ξ(1/2 + iz)` é
inteira e par; seus coeficientes de Taylor `d_k` são reais (`dXi_im`, pela unicidade de séries de potências,
`coef_zero_of_hasSum_zero`) e os ímpares se anulam (`iteratedDeriv_gXi_odd`). Com `aₙ = (−1)ⁿd_{2n}` (`aXi`),
`B(w) = Σaₙwⁿ` é inteira (`inteira_aXi`), `B(−z²) = g(z)` (`ev_aXi`) e `a₀ = Ξ(0) > 0`. Um zero `z` de `g` dá o zero
`−z²` de `B`, que por Edrei é real negativo; logo `z` é real. Forma explícita: `rh_de_menores` — **se todo menor
`det(a_{i_p − j_q}) ≥ 0`, vale HR**. A hipótese é **`OPEN_MATH`**: é equivalente a HR (a volta, por Hadamard de
gênero 0 e o crescimento de `ξ`, está em §4q). Nada aqui prova HR.

**O mecanismo de Weil** (`ATK.Weil`). Para qualquer forma bilinear simétrica com os números de interseção de `C × C`
(curva de gênero `g` sobre `𝔽_q`: `f₁² = f₂² = 0`, `f₁·f₂ = 1`, `Δ·fᵢ = Γ·f₁ = 1`, `Γ·f₂ = q`, `Δ² = 2 − 2g`,
`Γ² = q(2 − 2g)`, `Δ·Γ = N`) e o índice de Hodge (`x·(f₁ + f₂) = 0 ⇒ x² ≤ 0`), valem Castelnuovo–Severi
`D² ≤ 2(D·f₁)(D·f₂)` (`castelnuovo_severi`) e a **cota de Weil `|N − q − 1| ≤ 2g√q`** (`cota_weil`,
`cota_weil_abs`) — HR para curvas. Sem o índice de Hodge a cota falha: há uma forma simétrica em `ℝ⁴` com exatamente
esses números (`g = 0`, `q = 1`, `N = 5`) e `(N − q − 1)² = 9 > 0` (`hodge_necessario`). Para `Spec ℤ` falta a
"superfície" com forma de interseção; o análogo do índice de Hodge é a positividade de Weil — `OPEN_MATH`.

**Hilbert–Pólya** (`HilbertPolya.rh_de_operador`): se cada zero não trivial `ρ` dá o autovalor `(ρ − 1/2)/i` de um
operador simétrico num espaço com produto interno complexo, vale HR. Sem uma construção natural, a existência do
operador é só uma reformulação; o operador é `OPEN_MATH`.

Numérico (`codigo/edrei.py`, `dados/edrei.json`, `testes/test_edrei.py`, 4 testes): para `B = Σwⁿ/(n!)² = I₀(2√w)`, a
razão dos coeficientes de `1/J₀(2√x)` desce para `4/j₀,₁² = 0,691660276123` (12 dígitos; raiz `−j₀,₁²/4`); os
`aₙ = 2∫₀^∞Φ(u)u²ⁿ/(2n)!du` dão `a₀ = ξ(1/2)` a `2·10⁻¹⁶` (confere `Ξ = 2∫Φcos` da rodada 8), `a₁ = 0,0114859721576`
e Turán `aₙ² ≥ a_{n−1}a_{n+1}` para `n ≤ 8` — verificação finita, que não prova PF∞. Formatos: SMT-LIB 32, Coq e
Isabelle (`descida_tres`).

## 4q. Hadamard de gênero 0 e **HR ⟺ PF∞ dos coeficientes de Ξ** (rodada 11)

`ATK/InteiraAnalitica.lean` (9), `ATK/HadamardGenero0.lean` (35), `ATK/XiCrescimento.lean` (21): 65 teoremas novos,
total 6320, só `propext`, `Classical.choice`, `Quot.sound`. Nenhuma hipótese nova: o produto é **construído** e a sua
**convergência é provada** (não declarada).

**Ferramentas** (`ATK.InteiraAn`): `ev c` é inteira (série `ofScalars` de raio `⊤`, `hasFPowerSeries_ev`), `g⁽ⁿ⁾(0) =
n!cₙ` (`iteratedDeriv_ev`), desigualdade de Cauchy `|cₙ|Rⁿ ≤ max_{|w|=R}|ev c|` (`coef_le`), só finitos zeros num disco
(`zeros_finite`) e existência de um zero de módulo mínimo (`existe_zero_min`).

**Hadamard de gênero 0** (`ATK.Hadamard.hadamard_tn`, `coef_eq_lim`): se `F(z) = Σcₙzⁿ` é inteira, `c₀ > 0`,
`|F(w)| ≤ A·exp(A|w|^σ)` com `σ < 1` e todo zero de `F` é real negativo, então `F = c₀∏(1 + αⱼz)` com `αⱼ ≥ 0`,
`Σαⱼ < ∞` — **coeficiente a coeficiente**: `prodCoef c₀ α k n → cₙ` — e `T(c)` é totalmente não negativa. Com Edrei
(rodada 10): **para ordem `< 1`, `T(c)` TN ⟺ zeros reais negativos** (`tn_iff_zeros`). A prova:

1. Construção (`passo`, `seqH`, `alphaH`): a cada passo tira-se um zero de módulo mínimo `−1/αₖ` com `divLin`, e
   `F = ∏_{j<k}(1 + αⱼz)·Gₖ` (`ev_seqH`, `mk_seqH`); os `αₖ` decrescem (`alphaH_antitone`) e `Gₖ` não tem zeros em
   `|w| < 1/αₖ` (`alphaH_zero_free`).
2. Contagem (`contagem`, `summable_alpha_rpow`): no círculo `|w| = 3/αₖ` cada fator tem `|1 + αⱼw| ≥ 2`, e o módulo
   máximo dá `2^{k+1}c₀ ≤ A·exp(A(3/αₖ)^σ)`; daí `αₖ ≲ k^{−1/σ}` e `Σαⱼ^s < ∞` para todo `s > σ`.
3. `Gₖ → c₀` (`norm_seqH_le`, `coef_seqH_le`, `coef_seqH_tendsto`): `log|Gₖ|` é harmônica no disco sem zeros; pela
   fórmula de Poisson e pelo valor médio (`log_norm_le_poisson`), `log|Gₖ(w)| ≤ log c₀ + (2|w|/(r − |w|))·média|log|Gₖ||`;
   a média é controlada pelo crescimento de `F` e pela fórmula de Jensen para o polinômio `∏(1 + αⱼz)`
   (`avg_log_prod_nonneg`); Borel–Carathéodory e Cauchy dão `|coefₙ(Gₖ) − c₀δₙ₀| → 0`, porque a cauda `Σ_{j≥k}αⱼ^s → 0`
   (`tendsto_E`).
4. TN: `T(prodCoef c₀ α k)` é TN (rodada 10) e TN é fechada por limites entrada a entrada (`tn_closed`).

**Ξ tem ordem `≤ 3/4` em `w`** (`ATK.XiCresc`): a cota forte `|Φ(u)| ≤ 160·e^{u/2 − (3/2)e^{2u}}` (`Phi_cota`, para
`u ≥ 0`) torna `HPhi(z) = 2∫₀^∞Φ(u)cos(zu)du` inteira (holomorfia sob a integral com dominação
`160·e^{Y√Y}e^{−u}`, `hasDerivAt_HPhi`); como `HPhi = Ξ` em `ℝ` (rodada 8), o princípio de identidade dá
**`ξ(1/2 + iz) = 2∫₀^∞Φ(u)cos(zu)du` para todo `z ∈ ℂ`** (`gXi_eq_HPhi`), e daí `|ξ(1/2 + iz)| ≤ 320·e^{|z|√|z|}`
(`norm_gXi_le`, via `u/2 − (3/2)e^{2u} + yu ≤ y√y − u`, `expoente_le`). Com `B(−z²) = ξ(1/2 + iz)`:
`|B(w)| ≤ 320·exp(320·|w|^{3/4})` (`crescimento_B`). Sob HR, todo zero de `B` é real negativo (`zerosNeg_of_rh`; `0`
não é zero porque `Ξ(0) > 0`).

**O teorema** (com o `RiemannHypothesis` do Mathlib):

* `tn_de_rh`: **HR ⇒ `T(aₙ)` totalmente não negativa**;
* `rh_iff_tn`: **HR ⟺ `T(aₙ)` totalmente não negativa** (com `XiTP.rh_de_tn`, rodada 10);
* `rh_iff_menores`: **HR ⟺ todo menor de Toeplitz `det(a_{i_p − j_q})` é `≥ 0`**;
* `rh_iff_genero0`: **HR ⟺ existem `αⱼ ≥ 0`, `Σαⱼ < ∞`, com `B = a₀∏(1 + αⱼw)` coeficiente a coeficiente**.

**Estado.** Isto **não prova HR**: transforma HR, no kernel e sem hipóteses extras, num enunciado sobre uma sequência
real concreta (`aₙ = (−1)ⁿg^{(2n)}(0)/(2n)!` com `g(z) = ξ(1/2 + iz)`, i.e. `aXi`; numericamente
`aₙ = 2∫₀^∞Φ(u)u²ⁿ/(2n)!du`, identidade não formalizada aqui). A positividade total desses `aₙ` é **`OPEN_MATH`** — é HR. Verificações finitas (Turán, menores pequenos) são consistentes e não provam nada sobre todos os menores.

Numérico (`codigo/hadamard.py`, `dados/hadamard.json`, `testes/test_hadamard.py`, 4 testes): para `I₀(2√w) =
∏(1 + 4w/j₀,ₖ²)`, `Σαₖ = 1` e `Σαₖ² = 1/2` a `10⁻¹⁵` (30 zeros por Newton com `J₀` avaliada em 90 dígitos, McMahon até `2·10⁵` e cauda
integral), as funções simétricas elementares dão `1/(n!)²` para `n ≤ 5` a `2·10⁻¹⁴`, e `prodCoef` cresce com o número
de fatores e fica `≤ (Σα)ⁿ`; para `Ξ`, `a₁/a₀ = 0,02310499312` e `Σ1/γₖ² = 0,0231044` (20 zeros conhecidos + cauda de
Riemann–von Mangoldt, sem `S(t)`; a cauda pesa 30 % e confere a `6·10⁻⁷`), `a₂/a₀ = e₂(1/γₖ²)` a `1,3·10⁻⁸` —
consistência com zeros já verificados na linha, não prova. Formatos: SMT-LIB 33, Coq e Isabelle (`prodcoef_dois`).

## 4r. de Bruijn–Newman e Laguerre (rodada 12)

`ATK/DeBruijnNewman.lean` (23), `ATK/LaguerrePolya.lean` (6), `ATK/PolyaCalor.lean` (12): 41 teoremas novos, total
6361, só `propext`, `Classical.choice`, `Quot.sound`.

**A família `H_t`** (`ATK.DBN`), construída sem hipóteses: `H_t(z) = ∫₀^∞e^{tu²}Φ(u)cos(zu)du` é **inteira para todo
`t ∈ ℝ`** (`H_differentiable`; dominação `|e^{tu²}Φ(u)|e^{yu} ≤ 160·e^{|t|+y+(|t|+y)²}e^{−u}`, `peso_cota`, a partir de
`|Φ(u)| ≤ 160e^{u/2−(3/2)e^{2u}}` e `e^{2u} ≥ (2u)⁴/24`), par (`H_neg`), real em `ℝ` (`H_ofReal`), com
**`H₀(z) = ξ(1/2 + iz)/2`** (`H_zero`), e satisfaz a **equação do calor reversa `∂H_t/∂t = −∂²H_t/∂z²`** (`calor`:
derivação sob a integral em `t` e duas vezes em `z`, `hasDerivAt_H_t`, `hasDerivAt_H`, `hasDerivAt_H1`).

**`Λ` e HR.** Com `S = {t | todo zero de H_t é real}` e `Λ = inf S` (`Lambda`): **HR ⟺ `0 ∈ S`** (`rh_iff_zero_mem`,
`rh_iff_H0`), sem hipóteses. As pontes clássicas ficam **condicionais, com as hipóteses à vista**:

* `rh_iff_Lambda_le_zero`: se `S ≠ ∅` (de Bruijn 1950: `1/2 ∈ S`), `S` é limitado inferiormente (Newman 1976), fechado
  (Hurwitz) e fechado para cima (de Bruijn 1950), então **HR ⟺ `Λ ≤ 0`**;
* `rh_iff_Lambda_eq_zero`: somando `Λ ≥ 0` (Rodgers–Tao 2020), **HR ⟺ `Λ = 0`**;
* `Lambda_vazio`, `Lambda_nao_limitado`: com o `sInf` do Mathlib, `S = ∅` ou `S` ilimitado dariam `Λ = 0` — por isso
  as hipóteses `S ≠ ∅` e limitação não são decorativas.

Esses cinco teoremas conhecidos **não estão formalizados aqui** (`BUILD_PENDING`), nem as cotas `Λ ≤ 0,22`
(Polymath15, 2019) e `Λ ≤ 0,2` (Platt–Trudgian, 2021). `Λ ≤ 0` é HR: **`OPEN_MATH`**.

**Laguerre** (`ATK.Laguerre`), o núcleo polinomial do fechamento para cima: para `p ∈ ℝ[X]` com só raízes reais
(`RealRooted`: `#raízes = grau`, `⟺ Splits`) e qualquer `c ∈ ℝ`, **`p + c·p'` tem só raízes reais**
(`realRooted_add_C_mul_derivative`). Prova: Rolle para `e^{x/c}p(x)`, cuja derivada é `e^{x/c}(p + cp')(x)/c`, dá uma
raiz nova entre raízes consecutivas; uma raiz de multiplicidade `m` de `p` tem multiplicidade `≥ m − 1` em `p + cp'`
(`pow_sub_one_dvd_derivative_of_pow_dvd`); isso dá `grau − 1` raízes, e para polinômios reais isso basta
(`realRooted_of_card`: o fator restante teria grau 1). Daí `p − λp''` (`λ ≥ 0`, `1 − λD² = (1 + √λD)(1 − √λD)`,
`realRooted_sub_derivative2`) e **`(1 − λD²)^N p` com raízes reais** (`realRooted_iter`) — com `λ = t/N`, o análogo
discreto de `H_t = e^{−t∂²}H₀`. O sentido oposto não preserva: `X²` tem raízes reais e `(1 + D²)X² = X² + 2` não
(`calor_direto_falha`).

**Pólya–de Bruijn para polinômios** (`ATK.PolyaCalor`), com a passagem ao limite provada: se `p` tem só raízes reais
(coeficiente líder `a`, grau `n`), `|p(z)| ≥ |a|·|Im z|ⁿ` em `ℂ` (`norm_eval_ge`); daí **Hurwitz para polinômios**
(`realRooted_of_tendsto`): um limite coeficiente a coeficiente de polinômios de grau `n` com só raízes reais e
coeficiente `n` do limite `≠ 0` tem só raízes reais (um zero não real `z₀` daria `0 < |a||Im z₀|ⁿ ≤ |f_N(z₀)| → 0`).
Pelo binômio em `Module.End`, `(1 − λD²)^N p = Σ_m C(N,m)(−λ)^m D^{2m}p` (`iter_passoCalor`), e `C(N,m)/N^m → 1/m!`
(`tendsto_choose_div_pow`), logo `(1 − (λ/N)D²)^N p → e^{−λD²}p = Σ_m (−λ)^m/m!·D^{2m}p` coeficiente a coeficiente
(`tendsto_iter_calor`, `calorExato`). Resultado: **`p` com só raízes reais e `λ ≥ 0` ⇒ `e^{−λD²}p` com só raízes
reais** (`realRooted_calorExato`; Pólya 1913) — o caso polinomial do fechamento para cima de de Bruijn. Para `H_t`
falta (`BUILD_PENDING`) Hurwitz para funções inteiras e `e^{−λD²}` na classe de Laguerre–Pólya (aproximar `H_t` por
polinômios com raízes reais, o que em `t = 0` já pressupõe HR).

Numérico (`codigo/dbn.py`, `dados/dbn.json`, `testes/test_dbn.py`): `H₀(0) = ξ(½)/2 = 0,248560389094`
(Simpson), `H₀` troca de sinal entre `14,13` e `14,14`, `∂_tH = −∂²_xH` por diferenças finitas a `10⁻⁵` relativo em
`(t, x) = (0, 5), (0,2; 10), (−0,3; 2)`; Laguerre exato em `ℚ` (Sturm na parte livre de quadrados): `(x+1)(x−½)²(x−3)`
com `p + cp'` (`c = 1/3, −2, 5, −1/7`), `(1 − D²/10)^k p` (`k ≤ 10`) e `e^{−λD²}p` (`λ = 1/1000, 1/3, 1, 5`) com
raízes reais, `e^{D²}X² = X² + 2` e `(x²+1)(x−1)²` sem; 5 testes.
Formatos: SMT-LIB 34, Coq e Isabelle (`laguerre_quadratica`).

## 4s. Grupo 3: produtores de positividade — o que é construção e o que é descoberta (rodada 13)

`ATK/XiMomentos.lean` (20), `ATK/ProdutoresTN.lean` (11), `ATK/JensenPolya.lean` (20): 51 teoremas novos, total 6412, só
`propext`, `Classical.choice`, `Quot.sound`. Separa, no kernel, as camadas formalizáveis (M1–M4, G3.4, G3.7 parcial) do
nó que exige uma descoberta (a positividade total dos `aₙ` concretos).

**M1 — coeficientes como momentos** (`ATK.XiMom`). `Φ(u) > 0` para `u ≥ 0` (`Phi_pos`: cada termo
`(4w² − 6w)e^{u/2−w}`, `w = πn²e^{2u} > 3/2`, é positivo). Com `mₙ = 2∫₀^∞Φ(u)u^{2n}du` (`mom`, integrável e `> 0`):
**`aₙ = mₙ/(2n)!`** (`aXi_eq_mom`) — a série do cosseno trocada com a integral em `HPhi(z) = 2∫Φcos(zu)`
(`hasSum_HPhi`, dominação `|Φ|(|z|u)^{2n}/(2n)! ≤ |Φ|e^{2|z|u}/4ⁿ`) e unicidade dos coeficientes. Daí **`aₙ > 0` para
todo `n`** (`aXi_pos`), sem hipóteses.

**M2 — Hankel e Cauchy–Schwarz.** `Σ_{i,j} cᵢcⱼm_{s+i+j} = 2∫Φu^{2s}(Σcᵢu^{2i})² ≥ 0` (`hankel`), `m_{n+1}² ≤ mₙm_{n+2}`
(`mom_logconvexo`) e, nos `aₙ`, a **cota superior** `a_{n+1}²((2n+2)!)² ≤ aₙ(2n)!·a_{n+2}(2n+4)!` (`aXi_cota_superior`).
A desigualdade de Turán, necessária para PF∞, é uma cota **inferior** — Hankel não a dá.

**M3/M4 — a interface e as ressalvas** (`ATK.ProdTN`):

* `ArithmeticTotalPositiveKernel` (núcleo, identidade com `T(aₙ)`, todos os menores `≥ 0`): **`Nonempty
  ArithmeticTotalPositiveKernel ⟺ RiemannHypothesis`** (`nonempty_iff_rh`). A interface é exatamente HR; uma instância
  incondicional seria uma prova de HR (`OPEN_MATH`).
* `gram_vacuo`: toda matriz é `Aᵢⱼ = ⟨uᵢ, vⱼ⟩` — uma representação `b_{i−j} = ⟨uᵢ, vⱼ⟩` sozinha não carrega
  informação. `psd_nao_tn`: a matriz de Gram `!![1, −1; −1, 2] = BᵀB` não é TN.
* `hankel_nao_toeplitz`: **os momentos de `μ = (3/2)δ₀ + ½δ₁` têm Hankel positiva** (`hankel_momEx`), **mas
  `bₙ = mₙ/(2n)!` tem o menor de Toeplitz `det(b_{i_p−j_q})` (linhas 1, 2, 3; colunas 0, 1, 2) `= −7/2880`**. Ser
  sequência de momentos de uma medida positiva — o que `aₙ` é (M1) — não basta para PF∞.
* Núcleo TN conhecido: **`e^{γz}` é PF∞** (`tn_exp`, `T(γⁿ/n!)` TN para `γ ≥ 0`, limite de `(1 + γz/N)^N` via
  `prodCoef_const` e `C(N,m)/N^m → 1/m!`). Com `∏(1 + αⱼz)` (rodadas 10–11) e `tn_closed`, é a parte suficiente de Edrei
  para funções inteiras — sem afirmar que representa `Ξ`.
* **As pontes de fechamento propostas são HR**: `rh_de_aproximacoes_tn` (matrizes TN que convergem entrada a entrada
  para `T(aₙ)` dão HR) e **`rh_iff_fatores_positivos`: existir um arranjo `c_{N,k} ≥ 0` com
  `a₀·e_n(c_{N,0}, …, c_{N,N−1}) → aₙ` para todo `n` ⟺ HR**. Fechar esse "nó decisivo" é provar HR, não um passo mais
  fácil. (O núcleo de Hankel dos momentos é estritamente totalmente positivo — Andréief + Vandermonde generalizado,
  matemática conhecida, não formalizada aqui; isso também não dá Toeplitz, pelo contraexemplo acima.)

**G3.7 — polinômios de Jensen** (`ATK.JensenPolya`). Com `γ(k) = k!aₖ` e `J^{d,n}(X) = Σ_{j≤d} C(d,j)γ(n+j)X^j`
(`jensen`):

* `realRooted_jensen_of_genero0`: se `B = a₀∏(1 + αⱼw)` coeficiente a coeficiente, todo `J^{d,n}` tem só raízes reais.
  Prova: `Q_K = a₀∏_{i<K}(1 + αᵢD)X^d` tem raízes reais (Laguerre), `Q_K → Σ_k aₖ d^{(k)}X^{d−k}` (Hurwitz para
  polinômios), `J^{d,0}` é o reverso desse limite (`jensen_eq_reverse`, `realRooted_reverse`) e
  `Dⁿ J^{d+n,0} = (d+n)^{(n)}·J^{d,n}` (`iterate_derivative_jensen`).
* **`rh_jensen`: HR ⇒ todo `J^{d,n}` de `Ξ` é hiperbólico** (Pólya 1927, direção ⇒).
* **`turan_de_rh`: HR ⇒ `γ(n)γ(n+2) ≤ γ(n+1)²`**. Com `aXi_cota_superior`, sob HR `a_{n+1}²` fica cercado por cima
  (incondicional) e por baixo.

A volta (todos os `J^{d,n}` hiperbólicos ⇒ HR) está em §4t (Hurwitz); Turán
incondicional (Csordas–Norfolk–Varga 1986) e `J^{d,n}` para `n` grande (Griffin–Ono–Rolen–Zagier 2019) não estão
formalizados.

**O que continua aberto.** M5–M7 (operador espectral, fórmula explícita de Weil e a sua fatoração positiva, a ponte
terminal) e o núcleo `G3_02`/`G3_03` — **uma identidade concreta que represente os `aₙ` por um núcleo cuja positividade
total seja provada sem HR** — são `OPEN_MATH`. Pelos contraexemplos acima, essa identidade não pode vir só de
positividade de momentos, de Hankel ou de uma representação de Gram.

Numérico (`codigo/grupo3.py`, `dados/grupo3.json`, `testes/test_grupo3.py`, 5 testes): `aₙ > 0` para `n < 14`; a razão
de Cauchy–Schwarz sobe de `0,358` para `0,944` (`≤ 1`) e a de Turán desce de `1,0748` para `1,0261` (`≥ 1`); os menores
de Toeplitz contíguos `det(a_{k+i−j})` (`r = 2, …, 8` sob perturbação relativa `10⁻¹²`; `r = 10, 12, 14, 16` sob
`10⁻¹⁴`; o erro de quadratura medido é `2·10⁻¹⁶`) têm sinal positivo estável — nenhum sinal indeterminado nessa
faixa; `J^{d,n}` hiperbólico para `d ≤ 6`, `d + n ≤ 13` (Sturm exato nos coeficientes em ponto flutuante); `−7/2880` confere. Verificação finita: não prova
PF∞. Formatos: SMT-LIB 35, Coq e Isabelle (`turan_raiz`).

## 4t. Hurwitz: o critério de Pólya–Jensen completo e `S` fechado (rodada 14)

`ATK/HurwitzJensen.lean` (11), `ATK/DBNFechado.lean` (9): 20 teoremas novos, total 6432, só `propext`,
`Classical.choice`, `Quot.sound`. Fecha dois nós que estavam `BUILD_PENDING`.

**Hurwitz** (`hurwitz_local`): se `F_n → g` uniformemente num disco fechado, cada `F_n` é holomorfa e sem zeros no disco
e `g ≠ 0` na circunferência, então `g ≠ 0` no centro. Prova sem Rouché: com `δ = min_{|z−z₀|=r}|g|`, para `n` grande
`|F_n| ≥ δ/2` no círculo; o módulo máximo de `1/F_n` dá `|F_n(z₀)| ≥ δ/2`, mas `F_n(z₀) → g(z₀) = 0`.

**A volta de Pólya–Jensen** (`zeros_reais_de_jensen`): se `B(w) = Σaₖwᵏ` é inteira, `a₀ ≠ 0` e todo `J^{d,0}` de
`γ(k) = k!aₖ` tem só raízes reais, **todo zero de `B` é real**. `J^{d,0}(w/d) = Σⱼ (d^{(j)}/dʲ)aⱼwʲ` (`Fj_eq`) converge
uniformemente em discos para `B` (Tannery, `tendstoUniformlyOn_Fj`), não se anula fora do eixo real (`Fj_ne_zero`, pela
cota `|p(z)| ≥ |a||Im z|ⁿ`), e Hurwitz + princípio de identidade concluem. Para `Ξ` (`rh_de_jensen`): um zero `z` de
`ξ(1/2 + iz)` dá `−z²` real, logo `z` real ou imaginário puro, e o segundo caso é impossível porque `ξ > 0` no eixo
real. Com §4s:

* **`rh_iff_jensen`: HR ⟺ todo polinômio de Jensen `J^{d,n}` de `Ξ` tem só raízes reais**;
* **`rh_iff_jensen0`: HR ⟺ todo `J^{d,0}` tem** — o critério de Pólya (1927), nas duas direções, sem hipóteses.

**`S` fechado** (`isClosed_S`): `H_t(0) = ∫₀^∞e^{tu²}Φ(u)du > 0` (`H_ne_zero_at_zero`), `t_n → t ⇒ H_{t_n} → H_t`
uniformemente em discos (convergência dominada, `tendstoUniformlyOn_H`), e Hurwitz no semiplano dá: um zero não real
de `H_t` seria limite de zeros não reais de `H_{t_n}`. Daí `rh_iff_Lambda_le_zero'`: **HR ⟺ `Λ ≤ 0`** condicional só
a de Bruijn (`S ≠ ∅`, fechamento para cima) e Newman (limitação).

**Estado.** São equivalências e pontes: a hiperbolicidade de todos os `J^{d,n}` de `Ξ` e `Λ ≤ 0` continuam
`OPEN_MATH` (são HR).

Numérico (`codigo/hurwitz.py`, `dados/hurwitz.json`, `testes/test_hurwitz.py`, 2 testes): `B(−50) = 2H₀(√50)` a
`10⁻¹⁶` (série dos `aₙ` = integral de `Φ`); `|J^{d,0}(w/d) − B(w)|` em `w = −50` cai como `1/d` (`0,0114` em `d = 10`,
`0,00034` em `d = 320`); `H_t(0) > 0`; o primeiro zero real de `H_t` é `14,2508`, `14,1347`, `14,0190` para
`t = −0,1; 0; 0,1` (varia continuamente). Formatos: SMT-LIB 36, Coq e Isabelle (`hurwitz_circulo`).

## 4u. Dispersão de ordem 2: PF₂ dos coeficientes de `Ξ` sem HR, módulo o lema de Csordas (rodada 15)

`ATK/TuranDispersao.lean` (18 teoremas, total 6450, só `propext`, `Classical.choice`, `Quot.sound`). Responde à
proposta de uma "identidade de dispersão aritmética para os menores de Toeplitz, começando pela ordem 2": a ordem 2
já tem uma — a de Csordas–Norfolk–Varga (1986) — e ela está agora no kernel.

**A identidade** (`turan_disp`, núcleo geral `K` com as hipóteses de `Nucleo`): com `γₖ = ∫₀^∞u^{2k}K(u)du` e
`ψ(u) = −K′(u)/(uK(u))`, integração por partes (`ibp`: `(k+1)∫uᵏK = −∫u^{k+1}K′`) e Fubini com simetrização dão

`(2m+3)γ_{m+1}² − (2m+1)γ_mγ_{m+2} = ½∬ K(t)K(s)(ts)^{2m+2}(t² − s²)(ψ(t) − ψ(s)) ds dt`,

cujo integrando é `≥ 0` se `ψ` é crescente — logo vale a desigualdade de Turán.

**`Φ` é um núcleo** (`nucleo_Phi`): `Φ′ = Σₙ ∂ᵤphiT(cₙ,u)` com `∂ᵤphiT = (−8w³ + 30w² − 15w)e^{u/2−w}`
(`hasDerivAt_phiT`, `hasDerivAt_Phi`), `|Φ′(u)| ≤ 744·(Σe^{−cₙ/2})·e^{−2u}` (`Phid_cota`), e todos os `uᵏΦ`, `uᵏΦ′` são
integráveis com `uᵏΦ → 0`.

**Para `Ξ`, sem HR:**

* `turan_de_csordas`: **se `ψ_Φ` é crescente, `γ(n)γ(n+2) ≤ γ(n+1)²`** para todo `n` (`γ(k) = k!aₖ`) — a mesma
  conclusão de `turan_de_rh` (§4s), com HR trocada por uma propriedade concreta de `Φ`;
* `pf2_de_csordas`: **todo menor `2 × 2` de `T(aₙ)` é `≥ 0`** (PF₂), via `pf2_de_logconcava` (sequência positiva
  log-côncava ⇒ PF₂, `razao_lc`).

**`BUILD_PENDING`**: a monotonia de `ψ_Φ` — equivalente à log-concavidade de `Φ(√x)`, teorema de Csordas (CNV 1986;
Csordas 2015, Thm. 4.2(b)) — não está formalizada; é a única hipótese de `turan_de_csordas` e `pf2_de_csordas`. O nível
seguinte (as "Turán duplas", conjectura de Csordas–Dimitrov) foi provado em 2026 por Planat–Solé (arXiv 2608.19160,
com partes assistidas por computador; não verificado aqui). O programa de Nuttall estende o método a todas as ordens
via sign-regularity dos cumulantes de `Φ` (Karlin) — parcialmente provado, o resto conjectura. **PF_r para `r ≥ 3`
continua `OPEN_MATH`; PF∞ é HR.**

Numérico (`codigo/turan.py`, `dados/turan.json`, `testes/test_turan.py`, 3 testes): `Φ′` termo a termo confere com
diferenças finitas (`10⁻¹⁰`); `ψ_Φ` é crescente numa malha de passo `5·10⁻⁴` em `(0, 2]` (`ψ(0⁺) ≈ 18,73`,
`ψ(1) ≈ 41,79`, `ψ(2) ≈ 169,27`); os dois lados da identidade de dispersão conferem a 10 dígitos para `m = 0, 1, 2`
(quadratura 1D e Simpson 2D). Formatos: SMT-LIB 37, Coq e Isabelle (`simetrizacao_ordem2`).

## 4v. Classes de zeros e truncamento de Toeplitz: as "demais linhas" fechadas (rodada 16)

`ATK/ZeroClasses/{Basic,Symmetry,Multiplicity,Laws,Zeta,Regions,Hipotetico,FinalAudit}.lean` e
`ATK/TruncamentoToeplitz.lean` (222 teoremas, total 6672, só `propext`, `Classical.choice`, `Quot.sound`). Responde
ao prompt ATK-ZERO-CLASSES e ao pedido "ignorar Riemann e fechar em Mathlib as demais linhas": tudo o que é
demonstrável sem HR foi para o kernel; o que é HR está escrito como equivalência, nunca como prova.

**Camada genérica** (`f : ℂ → ℂ` arbitrária, reta `x = c` livre). Partições `Z = Z_{x<c} ⊔ Z_{x=c} ⊔ Z_{x>c}`
(`particao_posicao`, `zero_on_or_off`), `Z = Z_real ⊔ Z*_imag ⊔ Z_misto` (`particao_natureza`, `zero_nature`),
`Z_ℚ ⊔ Z_{ℝ∖ℚ}` para a parte real e para a imaginária; matriz de compatibilidade (imaginário puro ⇒ parte real
racional; para `c ∈ ℚ`, parte real irracional ⇒ fora da reta), **todas as células compatíveis realizadas por uma só
função** (`realiza_celulas`) e compatibilidade ≠ existência (`f ≡ 1`). A classe "localização indeterminada" é
**relativa a um conjunto certificado `K`**, antimonótona e não intrínseca (`indeterminado_nao_intrinseco`).
Simetrias sob hipóteses explícitas (`ConjEquiv`, `ReflZeros`, basta `f(2c − z) = u(z)f(z)` com `u` qualquer); a
órbita `{z, z̄, 2c − z, 2c − z̄}` tem cardinal `1 ⟺ z = c`, `4 ⟺ x ≠ c ∧ y ≠ 0`, `2` nos outros casos, nunca `3`
(`orbita_card_iff`); **a simetria não exclui zeros fora da reta** (`simetria_nao_basta`: `(z − c)⁴ + 4`).
Multiplicidade (`Multiplicity`): todo zero é isolado ou de acumulação (lógica pura); para `f` analítica,
**multiplicidade finita ⟺ isolado**, simples ⟺ ordem 1, simples ou múltiplo; num conexo com `f ≢ 0`, nenhum ponto
acumula zeros. Leis (`Laws`): `Existe F C` (o "ProvenExists" é uma prova dela; um postulado é uma hipótese e é
**inconsistente** quando a classe é refutada — `z² + 1` não tem zero real); leis de conjuntos, união, interseção
(só `⇒`, `existe_inter_nao_reciproca`), lei da simetria `T(Z) ⊆ Z` e `= Z` para `T` involutiva; os operadores
`{id, conj, refl c, tor c}` formam o **grupo de Klein** (`klein`), com a tabela da ação sobre as classes
(`conj_classes`, `refl_classes`, `refl_ratRe`, `tor_classes`).

**`ζ` (`Zeta`)** — matriz das classes, com o estado no kernel:

| Classe | Ocupada? | Teorema |
| --- | --- | --- |
| triviais `−2(n+1)` | **sim** — reais, racionais, **simples** | `trivial_classes`, `linha_trivial` |
| não triviais na reta crítica | **sim** (zero certificado, §4f) | `existe_critico`, `ocupacao` |
| não triviais (prova sem cálculo) | **sim**, por Hadamard: `B ≢` const pois `a₁ > 0` | `existe_nao_trivial`, `sem_zeros_constante` |
| mistos / parte real racional | **sim** (o zero crítico) | `ocupacao` |
| imaginários puros | **não** | `sem_imaginarios_puros` |
| reais na faixa, `Re ≥ 1`, `Re = 0` | **não** | `classificacao_natureza`, `sem_zeros_re_ge_one`, `sem_zeros_re_zero` |
| pontos de acumulação (inclusive `s = 1`) | **não** | `sem_acumulacao_zeta` (resíduo) |
| multiplicidade infinita | **não** | `zeros_isolados` |
| fora da reta crítica | `OPEN_MATH` (¬HR) | `nao_rh_iff_fora` |
| parte real irracional | `OPEN_MATH` (refutaria HR) | `irr_refuta`, `nao_rh_iff_aritm` |
| localização indeterminada (relativa a `Kcert`, regiões certificadas livres de zeros) | = exatamente os não triviais (a classe muda com `K`) | `indeterminados_eq` |

`ζ` é equivariante mas **não** preserva zeros por `s ↦ 1 − s` (`zeta_nao_reflZeros`: `ζ(−2) = 0`, `ζ(3) ≠ 0`); a
camada genérica instancia-se em `ξ` (`xi_conjEquiv`, `xi_reflZeros`, `quarteto_ou_par`).

**O cerco (`Regions`).** `F(σ,t) = |ζ(σ+it)|² ≥ 0`, `F > 0 ⟺ ζ ≠ 0`; `F > 0` incondicional em `t² < 3/4` e em
`σ ≤ c(t)`; **`RH ⟺ F > 0` em `0 < σ < 1/2, t > 0`** (`obrigacao_exata`). `Z_L = ∅ ⟺ Z_R = ∅`, `RH ⟺ Z_L = ∅`,
`RH ⟺ ζ ≠ 0` em `Ω`. Compactos `K_n`: **correção ao texto encaminhado — `K₃ = ∅`** (`1/3 > 1/6`), não vazios para
`n ≥ 4`; compactos, crescentes, `Ω = ⋃_{n≥3} K_n`. Mínimos `m_n`: atingidos, `m_{n+1} ≤ m_n`, `m₃ = 0` (convenção),
**`m_n > 0 ⟺ K_n` sem zeros** e **`RH ⟺ ∀ n ≥ 4, m_n > 0`**; certificados `PositiveCertificate` (o código Lean do
texto, compilado) excluem zeros, ficam abaixo de `m_n`, e **existe certificado ⟺ HR**; certificados de malha com
cota de derivada (`certificado_malha`, `certificado_derivada`). **Novo e incondicional: `m_n → 0`**
(`m_tende_zero`, pelo zero crítico certificado), logo **não existe cota uniforme** (`sem_cota_uniforme`): a camada C
só pode ser positividade ponto a ponto, nunca `m_n ≥ δ > 0`.

**Truncamento de Toeplitz (`TruncamentoToeplitz`).** `P(N+1) ⟺ P(N) ∧ Q(N+1)`, `TN ⟺ ∀N P(N)`, `P(N) ⟺ TN(T_N)`,
`P(0) ⟺ a₀ ≥ 0`, indução, **nível único de primeira falha** (`nivel_unico`, `primeira_falha`); para `Ξ`:
`RH ⟺ ∀N P(N) ⟺ ∀N Q(N+1)`, **`P(1)` incondicional**, **`P(2)` sob Csordas**; logo um zero fora da reta tem nível de
falha `≥ 1` (e `≥ 2` com menor negativo de **ordem `≥ 3`** sob Csordas). O menor do texto
`a₁³ − 2a₀a₁a₂ + a₀²a₃` é o menor contíguo `3×3` (`menor3`); `a₁² − a₀a₂ = (6m₁² − m₀m₂)/24` (`defeito_momentos`).
Fluxo `bₙ(τ) = aₙe^{−τn(n−1)}`: `D₂(b(τ))ₙ = e^{−2τ(n+1)n}(a_{n+1}² − e^{−2τ}aₙa_{n+2})`, crescente em `τ`;
**volta válida** a partir de todo `τ > 0` (também para TN inteira, `volta_valida_tn`), **volta ingênua inválida** a
partir de um `τ` (`a = (1,1,2,1,…)`).

**O universo hipotético (`Hipotetico`).** `OFF_LINE_ZEROS EXIST` entra como **hipótese** `HFora` (`UniversoATK`),
nunca como `axiom`: se HR for verdadeira, o axioma tornaria o sistema inconsistente. `UniversoATK ⟺ ¬HR` e
**refutar o universo é exatamente provar HR** (`refutar_universo_iff`) — a "consistência interna" não é uma
verificação à parte, é a própria questão. Consequências certificadas de `HFora`: quarteto distinto; representantes em
`Ω` e em `1/2 < Re < 1, Im > 0`; os dois ramos aritméticos (cada um refuta HR); `(Im ρ)² ≥ 3/4` e bordas `c(t)`;
finitos abaixo de cada altura; `D_N ≥ μ > 0`; falha de TN com nível único `≥ 1`; Jensen não hiperbólico; `m_n = 0`
para algum `n ≥ 4`; nenhum certificado; `F = 0` em `Ω`. O `painel` mostra que **cada falha é equivalente a
`HFora`**: nenhuma é mais fraca do que HR, e **nenhuma contradição foi derivada** (`ANALYTIC_CONTRADICTION:
NOT_DERIVED` — derivá-la seria provar HR).

**`FinalAudit`**: `fechado` (o incondicional), `reducao` (as equivalências), `primeiro_ponto_aberto`: o primeiro
ponto em que uma prova incondicional não se completa é **`m₄ > 0`**, i.e. `ζ ≠ 0` no segmento
`{1/4 + it : 1/4 ≤ t ≤ 4}` — afirmação **finita**, verdadeira numericamente (`m₄ ≈ 0,461`), cuja certificação no
kernel é mecânica (estender `mem_zetaI` de `σ = 1/2` para `σ = 1/4` e montar a malha com `certificado_derivada`):
`BUILD_PENDING`. O universal `∀ n ≥ 4` é HR.

Numérico (`codigo/zeroclasses.py`, `dados/zeroclasses.json`, `testes/test_zeroclasses.py`, 8 testes): `ζ` por
Euler–Maclaurin (só biblioteca padrão) confere em `ζ(2)`, `ζ(−2)` e no 1º zero; a órbita do 1º zero tem cardinal 2;
`m_n` numa malha global encaixada (passo `0,0125`) decresce de `0,461` (`n = 4`) a `0,415` (`n = 13`) e cai para
`0,125`, `0,061`, `0,051` em `n = 14, 15, 16` (o 1º zero, altura `14,13`); margem heurística de malha positiva para
`n = 4..10`; todos os menores de `T(aₙ)` com índices `≤ N`, `N ≤ 5`, são `> 0` ou estruturalmente nulos (sinal
estável sob perturbação `10⁻¹²`); `menor3/a₁³ ≈ 0,205`. Formatos: SMT-LIB 38–39, Coq e Isabelle (`orbita_quatro`,
`menor3`).

## 4w. O mundo com zeros fora da linha: a linha não cai, e os zeros fora a seguram (rodada 17)

`ATK/ZeroClasses/MundoFora.lean` (15 teoremas, total 6687, só axiomas padrão). Responde à leitura "nesse mundo os
zeros fora da linha são conhecidos; não bastaria um para destruir a linha; o que segura a linha são os zeros fora
dela". O kernel separa as duas coisas que a frase "um zero fora refuta HR" mistura: um zero fora **refuta o
enunciado universal** HR, mas **não destrói a linha**.

* **A linha sobrevive** em qualquer mundo (`linha_sobrevive`, pelo zero certificado §4f) e, sob `HFora`, linha e
  fora **coexistem** (`coexistencia`).
* **A linha é o espelho**: é exatamente o conjunto fixo da torção `s ↦ 1 − s̄`, que leva cada zero fora em outro
  zero fora, distinto (`linha_espelho`); o **ponto médio** de cada par está na linha (`ponto_medio`).
* **Os zeros fora fixam o eixo** (`fora_fixa_eixo`): se o conjunto dos zeros fora é não vazio e simétrico em torno
  de `Re s = κ`, então `κ = 1/2` — só eles já determinam a linha.
* **Equilíbrio exato** (`equilibrio`, `centro_fora`): em toda altura, `Σ_{ρ fora} (β − 1/2) = 0` e a média das
  partes reais dos zeros fora é **exatamente `1/2`**; contagens espelhadas à direita e à esquerda
  (`contagem_espelhada`).
* **Esparsidade** (`esparsidade`, Bohr–Landau, incondicional): a distância `> δ` da linha há no máximo `C·T`
  zeros até a altura `T`; com `N(T)/T → ∞` (B10) eles são uma proporção que tende a zero (`quase_todos_perto`).
* **Dicotomia do mundo** (`dicotomia_mundo`, `rh_acima`, `mundo_finito`): os zeros fora são finitos — e então,
  acima de uma altura, **todos** os zeros estão na linha — ou infinitos, em alturas arbitrariamente grandes.

Sentido exato de "os zeros fora seguram a linha": se existirem, são obrigados a ficar em quartetos espelhados
nela, com centro de massa exatamente nela e densidade nula em relação a ela. A linha em si é fixada pela equação
funcional (é o conjunto fixo da torção) e existiria igual sem eles. Que esse mundo exista é `¬HR` — `OPEN_MATH`.
Na literatura esse mundo é ferramenta clássica: Littlewood (1914) provou `π(x) > li(x)` infinitas vezes tratando
separadamente HR e `¬HR`; sob `¬HR`, com `Θ = sup Re ρ > 1/2`, `ψ(x) − x = Ω±(x^{Θ−ε})` (oscilação de Landau) — a
consequência material de zeros fora sobre os primos (não formalizada: `BUILD_PENDING`).

Teste-modelo (`testes/test_zeroclasses.py::test_mundo_fora_modelo`, não é `ζ`): quartetos hipotéticos têm o
ponto médio na linha e desvios que somam zero.

## 4x. Os dois casos: onde se excluem e onde se complementam (rodada 18)

`ATK/ZeroClasses/Complementar.lean` (29 teoremas, total 6716, só axiomas padrão). Responde a "os dois casos valem,
porque se complementam; a rigidez está na forma da pergunta de Riemann".

* **Para a mesma `ζ`, exatamente um** (`exatamente_um`: `RH ∨ H_fora` e `¬(RH ∧ H_fora)`). Aceitar os dois prova
  qualquer proposição (`explosao`) — é o princípio de não contradição, não uma escolha de formulação.
* **Numa família, os dois coexistem** (`dois_casos_na_familia`, `ambos_realizados`): no modelo
  `F_{d,t}(z) = (w² + t²)((w − d)² + t²)((w + d)² + t²)`, `w = z − 1/2`, com a mesma equação funcional
  `F(1 − z) = F(z)` (`FM_eq_func`) e a mesma conjugação (`FM_conj`) de `ζ`, os zeros são exatamente
  `1/2 ± it`, `1/2 ± d ± it` (`FM_zero_iff`); **todos na reta ⟺ `d = 0`**. Para `d ≠ 0` coexistem zeros centrais
  e um quarteto externo (`FM_externos`) cujo ponto médio é o zero central (`FM_ponto_medio`) — a construção dos
  textos encaminhados (Teoremas 1–4), agora compilada.
* **Um número em vez de sim/não** (`Theta`): `Θ = sup Re ρ ∈ [1/2, 1]`; **RH ⟺ Θ = 1/2**, **H_fora ⟺ Θ > 1/2**
  (`rh_iff_Theta`, `fora_iff_Theta`). A pergunta de Riemann é o extremo de um parâmetro contínuo; `Θ < 1` é
  `OPEN_MATH`. Outras formulações não binárias, na literatura: a constante de de Bruijn–Newman (`RH ⟺ Λ ≤ 0`;
  Rodgers–Tao: `Λ ≥ 0`, i.e. a família `H_t` tem zeros não reais para todo `t < 0`; Polymath: `Λ ≤ 0,2`); a
  proporção de zeros na reta (`> 5/12`, Conrey e sucessores); estimativas de densidade `N(σ, T)`.
* **Funções com os dois casos, na literatura**: a função de Davenport–Heilbronn tem equação funcional do tipo de
  `ζ`, infinitos zeros na reta e infinitos fora dela; o que lhe falta é o **produto de Euler**. Se há rigidez em
  `ζ`, ela vem dos primos, não da forma da pergunta.
* **Triviais** (`triv_passo`, `triv_segunda_diferenca`, `triv_compensados`): `Δ²zₙ = 0` e, em `ξ`, os triviais
  desaparecem (`ζ(−2(n+1)) = 0`, `ξ(−2(n+1)) ≠ 0`).
* **A lei `sin(πs/2)`** (`triv_iff_sin`): `sin(πs/2) = 0 ∧ Re s < 0 ⟺ s = −2(n+1)` — a classe trivial é imposta
  pelo fator `sin` da equação funcional.
* **Necessidade** (`equilibrio_sem_fora`): `Σ(β − 1/2) = 0` vale também só com zeros centrais, logo **não** torna
  os externos necessários. **Teste decisivo** (`teste_decisivo`, `necessidade_iff`): uma propriedade `P` provada
  que seria falsa sem externos prova `H_fora`; e **existe tal `P` ⟺ ¬RH** — demonstrar a necessidade dos externos
  é exatamente refutar RH. No erro dos primos: `ψ(x) − x = O(x^{1/2+ε})` para todo `ε` ⟺ RH (von Koch), e a
  oscilação incondicional de Littlewood `Ω±(x^{1/2} log log log x)` é produzida só pelos zeros centrais — não força
  externos. A lei de acoplamento em que cada zero (trivial, central ou externo) é necessário é a
  fórmula explícita `ψ(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½log(1 − x^{−2})`: `BUILD_PENDING`.

Numérico (`testes/test_zeroclasses.py`, 2 testes novos): a família `F_{d,t}` (simetria, zeros, `d = 0` ⟺ sem
externos, ponto médio) e `Δ²zₙ = 0` com `ζ(zₙ) ≈ 0`.

## 4y. O que a escolha humana constrói, e o que ela não alcança (rodada 19)

`ATK/ZeroClasses/Construcao.lean` (30 teoremas, total 6746, só axiomas padrão). Responde a "a resposta de onde
estão os zeros fora da linha vem dos seres humanos e de como nossas ações possibilitam a existência deles". O
kernel separa os dois sentidos dessa frase.

**O que a escolha constrói** — a escolha é literalmente o parâmetro `t : ℕ → ℝ`. `Z_ATK = ζ·P_N`,
`P_N = ∏_{n<N} Q_{δₙ,tₙ}`, `Q_{δ,t}(s) = ((s−½−δ)² + t²)((s−½+δ)² + t²)`, `δₙ = 1/(2n+3)` (o índice do trivial
`−2(n+1)`):

* **A** (`zeros_ZATK`, `preserva`, `triviais_simples_ATK`): zeros de `Z_ATK` = zeros de `ζ` ∪ zeros de `P_N`; os
  triviais permanecem e continuam **simples** (`Z_ATK′(−2k) = P_N(−2k)ζ′(−2k) ≠ 0`);
* **B** (`externos_ATK`, `lei_transporte_ATK`): cada quarteto `½ ± δₙ ± itₙ` (`tₙ ≠ 0`) é de zeros, **fora da
  linha**, de cardinal 4 — a lei de transporte do texto **vale para `Z_ATK`, por construção**;
* **C** (`simetria_ATK`): `ξ_ATK = ξ·P_N` tem a equação funcional `ξ_ATK(1 − s) = ξ_ATK(s)` e a conjugação.

**O que a escolha não alcança** (`rigidez`, `colar_refuta`, `rh_nao_colar`): pela continuação analítica, uma
função analítica em `ℂ ∖ {1}` que coincide com `ζ` perto de **um** ponto coincide com `ζ` em toda parte. Se `Z_ATK`
coincidisse com `ζ` em qualquer aberto, a própria `ζ` teria os zeros externos (`H_fora`); sob RH, `Z_ATK` difere de
`ζ` perto de todo ponto. Os zeros de `ζ` estão fixados por `Σn^{−s}`; a ação humana os **encontra** (o zero
certificado de §4f foi encontrado por um cálculo desenhado por pessoas), não os cria. A rigidez é a da continuação
analítica, não da formulação de Riemann; e o que `Z_ATK` não preserva é o **produto de Euler** — a ligação com os
primos.

**Os triviais e a fórmula de L'Hôpital do texto** (`deriv_trivial_fechada`, `deriv_trivial_sinal`):
`ζ′(−2k) = (−1)ᵏ(2k)! ζ(2k+1) / (2(2π)^{2k})`, `= (−1)ᵏ·c` com `c > 0`; os únicos zeros reais negativos de `ζ` são
os pares negativos (`zeros_reais_negativos`). Lembrete: os triviais **estão fora da linha** e são certificados; os
externos em aberto são os **não triviais**.

**A lei de transporte para `ζ`** (`lei_transporte_refuta`): uma única instância `ζ(½ + δₙ + iτ) = 0` dá `H_fora`;
`δₙ → 0` e só finitos `n` têm `δₙ > δ` (`delta_tende`, `delta_finitos`), compatível com Bohr–Landau.

Numérico (`testes/test_zeroclasses.py`, 2 testes novos): `ζ′(−2) = −0,0304484571…` e `ζ′(−4)` conferem com a fórmula;
`Z_ATK` com `N = 3` tem os quartetos, a simetria, preserva o 1º zero de `ζ` e não se anula nos triviais.

## 4z. As escalas em que um zero fora da linha ainda pode existir (rodada 20)

`ATK/ZeroClasses/Escalas.lean` (11 teoremas, total 6757, só axiomas padrão). Responde a "a meta é achar
exatamente as escalas onde esse zero poderia existir": é o **complemento das regiões excluídas**. O kernel prova
as exclusões que tem; as da literatura entram como **hipóteses nomeadas**, e o kernel deriva a janela.

**Perto do primeiro zero — a lei da cauda certificada** (`lei_da_cauda`, `primeiro_zero_simples`,
`cauda_nao_zero`). No disco de raio `10⁻⁶` do certificado de §4f, a contração `g(z) = z − ζ(z)/c` dá
`(|c|/2)·|z − ρ₁| ≤ |ζ(z)| ≤ (3|c|/2)·|z − ρ₁|`, `|c| ≈ 0,7932`; o primeiro zero é **simples**; nenhum ponto do disco
fora da linha é zero. É a forma provada da medição `R_n ≈ 0,79316·d_n` da "cauda ATK": a cauda tende a zero sem
zeros exatos — ela se aproxima de um zero **conhecido**, não revela um novo.

**O que o kernel exclui sozinho** (`escalas_kernel`): `(Im ρ)² ≥ 3/4`, `c(γ) < Re ρ < 1 − c(γ)` e o disco do primeiro
zero.

**A janela, com a literatura como hipótese** (`janela`, `janela_2026`):

* `VerificadoAte 3 000 175 332 800` — Platt–Trudgian (2021): todos os zeros até essa altura estão na linha e são
  simples;
* `RegiaoClassica 4,896` — Bellotti–Trudgian–Yang (2026): `ζ ≠ 0` em `σ ≥ 1 − 1/(4,896 log t)`, `t ≥ 3`.

Então **todo zero fora da linha tem `|γ| > 3·10¹²` e `1/(4,896 log|γ|) < Re ρ < 1 − 1/(4,896 log|γ|)`**. A janela
**alarga** com a altura (`janela_alarga`), e **nenhuma reta vertical `σ₀ ∈ (0,1)` fica excluída em todas as alturas**
(`nenhuma_reta_excluida`): por isso não existe "uma escala exata" — existe uma região. As retas ATK
`σₙ = ½ + 1/(2n+3)` estão **todas** dentro dela acima de `3·10¹²` (`retas_atk_acima_de_H`).

| Altura `|γ|` | Janela possível para `Re ρ` | Região que manda | Escala de Selberg `1/log t` |
| --- | --- | --- | --- |
| `3·10¹²` | `(0,00711; 0,99289)` | clássica (`R = 4,896`) | `0,0348` |
| `10²⁰` | `(0,00444; 0,99556)` | clássica | `0,0217` |
| `10¹⁰⁰` | `(0,00111; 0,99889)` | Littlewood (`log log t/(21,233 log t)`) | `0,0043` |
| `e^{10⁶}` | `(7,7·10⁻⁷; 1 − 7,7·10⁻⁷)` | Korobov–Vinogradov (`53,989`) | `10⁻⁶` |

A região de Littlewood passa a clássica em `log t ≈ 76,46` e a de Korobov–Vinogradov só em `log t ≈ 482 036`.
**Quantos** zeros podem estar numa reta: Guth–Maynard (2026) dá `N(σ, T) ≤ T^{30(1−σ)/13 + o(1)}`, útil só para
`σ > 17/30` — e a reta ATK `n = 6` é **exatamente** `σ = 17/30`; nas retas `n ≤ 5` o expoente vai de `0,385`
(`σ = 5/6`) a `0,976`. Bohr–Landau (§4w, no kernel) dá `O(T)` para cada distância fixa. O que **não** está aqui: uma
contagem certificada positiva numa região fora da linha — só ela provaria um zero externo.

Numérico (`codigo/escalas.py`, `dados/escalas.json`, `testes/test_escalas.py`, 6 testes): janelas, cruzamentos das
três regiões, expoentes de Guth–Maynard nas retas ATK e `R/d → 0,79316` dentro dos limites certificados
`[0,3966; 1,1897]`.

## 5. Formatos

| Formato | Verificador | Conteúdo |
| --- | --- | --- |
| Lean 4 + Mathlib | kernel (`lake build`, `#print axioms`) | tudo acima |
| Coq (Rocq) | `coqc` + `coqchk` (CI) | semântica, operadores, modelo G, P1–P5, quártica, esfera, cilindro, cone, toro, curvatura, pontes, T28, tempos; discriminante cúbico, Turán 2 e 3, Toeplitz, momentos; K₆, Jensen `γ`, rotação, ajuste, integral por pedaços; erros corrigidos (`b̃_k`, `G₁₂`, `C₀`, região vazia, `1/ζ(3)`); constante de `θ`, tridiagonal; inversa de `1 − x + x²`; descida de Edrei; coeficientes de um produto de gênero 0; Laguerre no grau 2; Turán a partir de uma raiz real; o passo do círculo de Hurwitz; a simetrização da dispersão de ordem 2; o quarteto de zeros; o menor `3×3` de Toeplitz |
| Isabelle/HOL | `isabelle build` (CI) | idem, com complexos nativos (inclui a seção Jensen/Turán) |
| SMT-LIB 2 | z3 / cvc5 (CI) | 39 obrigações negadas (13–16: Jensen/Turán/Toeplitz; 17–23: K₆, Jensen `γ`/`a`, ajuste, barreira, rotação, integral por pedaços; 24–28: erros corrigidos; 29–30: constante de `θ`, tridiagonal de `1+x+x²`; 31: coeficientes de `1/(1−x+x²)`; 32: descida de Edrei; 33: `prodCoef` de gênero 0; 34: Laguerre no grau 2; 35: Turán a partir de uma raiz; 36: círculo de Hurwitz; 37: simetrização de ordem 2; 38: quarteto de zeros; 39: menor `3×3`), espera-se `unsat` |
| TPTP | E prover (CI) | classificação, redução terminal (forma lógica), tempos |
| Python | `pytest` (+ SymPy) | aritmética exata em ℚ[i], contornos, toro, critério; coeficientes de `Θ`, Turán, Toeplitz, Sturm, primeiro zero |

Este ambiente não tem Coq nem Isabelle (rede bloqueada para instalá-los): esses verificadores rodam no
GitHub Actions e só contam como verificados quando o job do CI passa.
