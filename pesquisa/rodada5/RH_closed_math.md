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
| 963449d2 | `G₁₁ = log 2π − γ − 1` | falso (esquece `∫₁^∞ t⁻² = 1`) | `GramDois.G11_ne_texto1` |
| 1fb0a5dd | `G₁₁ = log 2` | falso (`G₁₁ − log 2 = log π − γ > 0`) | `GramDois.G11_ne_log2` |
| 9654e97e | `b_k = (1 − γ + log k − H_{k−1})/k` | falso: dá `b₄ < 0`, mas `b_k > 0` | `GramDois.b4_texto_errado` |
| 9e0c6efb | coeficiente `(p/i + q/j)` na integral por pedaços | falso: `i=1, j=2, [2,3]` daria `< 0` | `GramDois.contraexemplo_pedaco` |
| 56e0dfa6 | `B = d∫₀¹ Re F′` | falso: é `Im F′` (`F = z²`) | `XiAnalitica.contraexemplo_Re`, `B_integral` |
| 8af24fb4 / bef58a09 | `λ ≠ 0` ⇒ quatro zeros simples; `λ = 0` ⇒ dois duplos | falta `γ ≠ 0`: zero duplo / quádruplo | `GeometriaExtra.cruzamento_*` |
| f1754ca5 / 0e761a7c | Jensen montado com `aₙ` | normalização errada: `Θ = 1+2x+2x²` passa e tem zeros não reais | `GeometriaExtra.jensen_a_hiperbolico`, `jensen_gamma_detecta` |
| 0e761a7c | `TP∞(γ)` caracteriza zeros reais negativos | falso: `(1+x)³` tem `D₃,₁(γ) = −3` | `Jensen.tp_a_nao_passa_gamma` |
| 425e4bc1 | "HR ⇏ O1" | mal posto: provar `¬(HR → Q)` provaria HR | `GeometriaExtra.nao_implica_prova_rh` |
| 99d52102 | ajuste `D_N ≈ a + C/log N` com os dois valores | intercepto negativo, incompatível com `D_N ≥ 0` | `BarreiraModelos.sem_modelo_nao_negativo` |
| e1644f4c / f1754ca5 | `Ξ(t) = ∫Φ(u)cos(tu)du` | fator 2 (é `2∫₀^∞`; `2∫Φ = ξ(½)`) | só numérico (`jensen.py`) |
| 48cacf85 | `HR ⟺ ∀T > 2, M₊(T) > 0` | mal posto para `2 < T < 4` (região vazia) | registrado; a versão `K_n, n ≥ 5` está formalizada |
| 7a43314b | `0,831908` (`1/ζ(3)`) | é `0,8319073726…` | só numérico |

## 4l. O que continua pendente (não formalizado aqui)

Ganho de Schur exato e Tikhonov; `D_∞` como resíduo ortogonal em `L²`; o núcleo `ψ` fora da linha; o princípio do
argumento em círculos; a identidade de Green (a) no retângulo; `N(14) = 0` (cobertura certificada, pesada); a constante
`0,831908`; e, claro, HR (`D_∞ = 0`, `∀n δ_n > 0`, `Re ξ′/ξ > 0` em `Re s > ½`) — todas as formas equivalentes continuam
abertas.

## 5. Formatos

| Formato | Verificador | Conteúdo |
| --- | --- | --- |
| Lean 4 + Mathlib | kernel (`lake build`, `#print axioms`) | tudo acima |
| Coq (Rocq) | `coqc` + `coqchk` (CI) | semântica, operadores, modelo G, P1–P5, quártica, esfera, cilindro, cone, toro, curvatura, pontes, T28, tempos; discriminante cúbico, Turán 2 e 3, Toeplitz, momentos; K₆, Jensen `γ`, rotação, ajuste, integral por pedaços |
| Isabelle/HOL | `isabelle build` (CI) | idem, com complexos nativos (inclui a seção Jensen/Turán) |
| SMT-LIB 2 | z3 / cvc5 (CI) | 23 obrigações negadas (13–16: Jensen/Turán/Toeplitz; 17–23: K₆, Jensen `γ`/`a`, ajuste, barreira, rotação, integral por pedaços), espera-se `unsat` |
| TPTP | E prover (CI) | classificação, redução terminal (forma lógica), tempos |
| Python | `pytest` (+ SymPy) | aritmética exata em ℚ[i], contornos, toro, critério; coeficientes de `Θ`, Turán, Toeplitz, Sturm, primeiro zero |

Este ambiente não tem Coq nem Isabelle (rede bloqueada para instalá-los): esses verificadores rodam no
GitHub Actions e só contam como verificados quando o job do CI passa.
