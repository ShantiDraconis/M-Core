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
`σ = 1/4`; **fechada na rodada 28**, §4ah), o teorema de Hardy (infinitos zeros na reta; **fechado na rodada 50**, §4bd) e a infinitude dos zeros não triviais por Hadamard com zeros
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
`BUILD_PENDING` — **fechado na rodada 28** (§4ah: `m₄ ≥ 1/20`; o novo primeiro ponto aberto é `m₅ > 0`). O
universal `∀ n ≥ 4` é HR.

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

## 4aa. O encontro: matrizes, composições, colisões e o certificado exato (rodada 21)

`ATK/ZeroClasses/Encontro.lean` (48 teoremas, total 6805, só axiomas padrão). Responde a "cruze os dados e ache
exatamente onde esses zeros se encontram no mundo hipotético". O mundo hipotético entra **só como hipótese**
(`HFora`); nada aqui supõe RH nem `¬RH`.

**Matriz, soma, diferença, produto: quatro escritas do mesmo número** (`det_matA`, `matA_mul`, `det_zeta`,
`xi_espelho`, `xi_bilateral`, `det_B`, `soma_diferenca`, `cruzamento`, `criterio_SD`). `A(w) = [[Re w, −Im w],
[Im w, Re w]]` tem `det A = |w|²` e **é** a multiplicação (`A(wv) = A(w)A(v)`). Com `s₋ = 1 − s̄₊`, `ξ(s₋) = conj ξ(s₊)`
(exato, qualquer altura), e

  `(|S|² + |D|²)/4 = det A(ξ(s₊)) = ξ(s₊)·ξ(s₋) = |ξ(s₊)|²`,  `S = ξ(s₊) + ξ(s₋)`, `D = ξ(s₊) − ξ(s₋)`;

na faixa, `S = D = 0 ⟺ ζ(s₊) = 0`. Não são quatro evidências: é o mesmo escalar. E **a simetria não obriga zero**
(`simetria_nao_obriga`: `a = 3 + 4i`, `36 + 64 = 100`, `a ≠ 0`).

**Zero coletivo ≠ zero individual** (`zero_coletivo`, `zero_coletivo_zeta`, `dois_pontos`,
`coletivo_sem_individual`, `composicao_funcional`). `(ζ3 − ζ4)ζ2 + (ζ4 − ζ2)ζ3 + (ζ2 − ζ3)ζ4 = 0` com o peso
`ζ4 − ζ2 = π⁴/90 − π²/6 ≠ 0` e nenhum `ζ(k)` nulo; `exp` nunca se anula e ainda admite cancelamento exato; a equação
funcional é uma composição **identicamente** nula. Também: `ζ(−½) ≠ 0` (`zeta_menos_meio`), `ζ(qₙ) ≠ 0` para
`qₙ = −1/(2n+1) + i·10¹⁰⁰` (`q_nao_zero`, `semiplano_esquerdo`) e `ζ(−2·10¹⁰⁰⁰) = 0` (`zero_trivial_gigante`:
zero **trivial**, não refuta nada).

**Colisão: possível em família, impossível para `ζ` fixa** (`Fcol_zero_iff`, `colisao_dupla`, `logderiv_Fcol`,
`logderiv_limite`, `colisao_atk`, `sem_colisao`, `atk_finitos`). `F_δ(s) = (s − c)² − δ²` tem zeros `c ± δ` que
colidem num zero duplo; `F′/F = 1/(s − ρ₊) + 1/(s − ρ₋) → 2/(s − c)`. Para `ζ`: **se `sₙ → c` com `sₙ ≠ c`, então
`ζ(sₙ) ≠ 0` para `n` grande** — vale em todo `c`, inclusive no polo. Em cada altura `t`, a sequência ATK
`½ + 1/(2n+1) + it` só toca zeros para **finitos** `n`.

**Estabilização** (`estabilizacao`, `estabilizacao_primeiro_zero`): `|f(ρ+u)|²/u² → |f′(ρ)|²` em qualquer zero;
no primeiro zero certificado, `|ζ(ρ₁+u)|²/u² → |ζ′(ρ₁)|² > 0`, `|ξ(ρ₁+u)|²/u² → |ξ′(ρ₁)|²` e
`|ξ(ρ₁ − u)| = |ξ(ρ₁ + u)|`. É a assinatura de um zero **simples na linha**, não de uma colisão.
(`ξ′(ρ₁) ≠ 0` segue de `ζ′(ρ₁) ≠ 0` e `½ρ₁(ρ₁ − 1)Γℝ(ρ₁) ≠ 0`; fechado na rodada 24, §4ad.)

**Onde exatamente: o certificado** (`certificado_existencia`, `certificado_exclusao`, `DiscoFora`,
`certificado_refuta`, `certificado_robusto`, `fora_simples_iff_certificado`). Se `‖1 − f′/c‖ ≤ ½` no disco
`B(z₀, r)` e `‖f(z₀)/c‖ ≤ r/2`, há **exatamente um** zero no disco, e ele é simples; se `‖f′‖ ≤ M` e `M·r < |f(z₀)|`,
não há nenhum. Para `ζ`:

  **existe zero simples fora da linha ⟺ existe um disco inteiramente fora da linha com o certificado de contração.**

E todo zero simples fora da linha é certificado por **qualquer** dado de precisão finita suficiente (centro a menos
de `r/4`, inclinação a menos de `|ζ′(ρ)|/8`, todo `r < r₀`). Ou seja: se o mundo hipotético for o real, **uma conta
finita o verifica**; o que nenhuma conta finita faz é provar que ele é falso — isso é RH.

**O encontro no mundo hipotético** (`PrimeiroFora`, `primeiro_fora`, `altura_unica`, `encontro_hipotetico`). Sob
`HFora` existe um **primeiro** zero fora da linha `ρ* = β + iγ*` (menor altura positiva), e `γ*` é **único**. Com
Platt–Trudgian e Bellotti–Trudgian–Yang como hipóteses nomeadas: `γ* > 3 000 175 332 800`,
`1/(R log γ*) < β < 1 − 1/(R log γ*)`, o quarteto `ρ*, 1 − ρ̄*, ρ̄*, 1 − ρ*` são zeros, abaixo de `γ*` não há
zero fora da linha, e o par `ρ*, 1 − ρ̄*` tem ponto médio **`½ + iγ*`**, na linha. **Esse é o ponto exato de encontro.**
O valor de `γ*` não é determinado por dado algum: só `γ* > H`; uma cota superior seria uma refutação de RH.

**O candidato gigante** (`delta_gigante`, `rhoGig`, `candidato_gigante`). `ρ = ½ + 1/(2·10¹⁰⁰⁰ + 1) + i·10¹⁰⁰`
está na reta ATK `n = 10¹⁰⁰⁰ − 1`, fora da linha, acima de `H` e **dentro** da janela de 2026 — nada conhecido o
exclui, nada conhecido o confirma. Seu estado é `ζ(ρ) = 0 ⟺ det A(ξ(ρ)) = 0 ⟺ S = D = 0`: **não calculado** (a soma
de Riemann–Siegel nessa altura tem `≈ 3,99·10⁴⁹` termos; `T·δ < 5·10⁻⁹⁰¹`).

| Afirmação | Estado |
| --- | --- |
| `det A = \|ζ\|²`, `(\|S\|²+\|D\|²)/4 = ξ(s₊)ξ(s₋) = \|ξ(s₊)\|²`, `S = D = 0 ⟺ ζ = 0` | CERTIFIED (kernel) |
| zero coletivo / dois pontos / composição funcional — sem zero individual | CERTIFIED |
| colisão em família (`F_δ`), polo de resíduo 2 | CERTIFIED |
| `ζ` sem colisão; sequência ATK com finitos zeros por altura | CERTIFIED |
| estabilização no 1º zero (`ζ`, com limite > 0; `ξ`, limite e paridade) | CERTIFIED |
| `ξ′(ρ₁) ≠ 0` | CERTIFIED na rodada 24 (`xi_deriv_primeiro_zero`, §4ad) |
| zero simples fora da linha ⟺ certificado num disco fora da linha | CERTIFIED |
| primeiro zero fora da linha (sob `HFora`), altura única, encontro em `½ + iγ*` | CERTIFIED (condicional a `HFora`) |
| `γ* > 3·10¹²`, `β` na janela | CERTIFIED condicional às hipóteses nomeadas da literatura |
| existência de zero fora da linha | OPEN_MATH (equivale a `¬RH`) |
| valor de `ζ` no candidato gigante | não calculado |

Numérico (`codigo/encontro.py`, `dados/encontro.json`, `testes/test_encontro.py`, 9 testes): os 15 módulos
`|ζ(σ + iγₖ)|` e o peso `w = 1,2737523955 + 0,0629566840i` conferem; `ζ(−½) = −0,2078862250 = −ζ(3/2)/(4π)`;
`|ξ′(ρ₁)|² = 1,9119121·10⁻⁶` com convergência quadrática de `D(u)/u²`; a identidade `(|S|²+|D|²)/4 = |ξ|²` em pontos
de teste; **varredura** de `|ζ|` em `0,05 ≤ σ ≤ 0,45` e `0,55 ≤ σ ≤ 0,95`, `10 ≤ t ≤ 100`: mínimo `0,0391` em
`(0,55; 14,14)` (ao lado do 1º zero), 180/180 blocos com margem de exclusão positiva **heurística** (`M` amostrado,
não cota rigorosa); certificados de contração numéricos nos zeros 2–5 (todos na linha).

## 4ab. Onde o real encontra o imaginário: componentes, mínimos, caudas e o infinito (rodada 22)

`ATK/ZeroClasses/Componentes.lean` (28 teoremas, total 6833, só axiomas padrão). Com `ζ(σ + it) = u + iv`, o kernel
separa **componentes iguais**, **troca de componentes** e **anulação simultânea**, e acrescenta o teorema que
decide o "quase zero".

**Curvas e rotação** (`diagonais`, `cruzam_so_no_zero`, `curvas_C`, `igual_nao_e_zero`, `rotacao`). As curvas
`C₊ = {u = v}` e `C₋ = {u = −v}` cruzam-se **exatamente** nos zeros de `ζ`; `u = v` sozinho não é zero (`1 + i`). A
troca `(u, v) ↦ (−v, u)` é `J = A(i)`, com `J² = −1`, `J⁴ = 1`, `|iz| = |z|`: girar não cria zero.

**Cauchy–Riemann e o ângulo reto** (`cauchy_riemann`, `cruzamento_perpendicular`). Em `s ≠ 1`:
`∂σu = Re ζ′`, `∂σv = Im ζ′`, `∂tu = −Im ζ′`, `∂tv = Re ζ′` (logo `uσ = vt`, `ut = −vσ`). Os gradientes de `u` e `v` —
e os de `u − v` e `u + v` — são **ortogonais** e de mesma norma `|ζ′|`: num zero simples, as curvas cruzam-se em
ângulo reto.

**Não existe "quase zero" que seja mínimo** (`nao_localmente_constante`, `minimo_local_e_zero`,
`sem_maximo_local`, `minimo_na_fronteira`). Pelo princípio do módulo mínimo, **todo mínimo local de `|ζ|` fora do
polo é um zero exato**; `|ζ|` não tem máximo local; e num compacto sem zeros o mínimo de `|ζ|` fica **na fronteira**.
Isso explica a varredura da rodada 21: o mínimo fora da linha (`0,0391`) estava em `σ = 0,55`, a borda da região — o
que o teorema obriga numa região sem zeros. Para procurar zeros, os mínimos locais são **os** candidatos, e um
mínimo positivo no interior é impossível.

**A cauda de influência** (`residuo_logderiv`, `residuo_primeiro_zero`, `residuo_triviais`). Num zero de ordem
`m` de `f` analítica, `(s − ρ)·f′(s)/f(s) → m`: a parcela `m/(s − ρ)` é a influência do zero sobre a vizinhança. No
primeiro zero certificado e em todos os triviais, `m = 1`. A influência não cria zeros.

**Caudas de zeros** (`sem_curva_de_zeros`, `sem_curva_unitInterval`, `cauda_iff`, `triviais_ilimitados`).
Nenhuma curva contínua não constante (em qualquer espaço pré-conexo, em particular `[0, 1]`) é feita de zeros de
`ζ`. **Infinitos zeros fora da linha ⟺ alturas ilimitadas**: uma "cauda" de zeros externos é compatível com o
isolamento (os triviais `−2n` são uma sequência ilimitada de zeros), mas não está demonstrada.

**Simetria não obriga zeros fora** (`Fch_refl`, `Fch_conj`, `Fch_zero_iff`, `Fch_na_linha`, `simetria_sem_fora`).
`cosh(s − ½)` tem `F(1 − s) = F(s)` e `F(s̄) = conj F(s)`, zeros em alturas ilimitadas, e **todos** na linha.

**Depois do infinito** (`arquimediano`, `altura_infinita`, `deslocamento_infinitesimal`, `ordinal_sucessor`).
Nos reais não há deslocamento infinitesimal: todo `δ > 0` supera algum `1/(2n+1)`. Nos hiper-reais, `ω` excede todo
real e `½ < ½ + ε < ½ + r` para todo real `r > 0`. Nos ordinais, `1 + ω = ω < ω + 1`. Nenhum desses objetos é um
argumento de `ζ`; a transferência para `*ζ` não está no kernel, e ela não mudaria a pergunta clássica.

**Li e contagem.** O critério de Li já está no kernel (`ATK/LiCriterio.lean`: `RH ⟺ |1 − 1/ρ| = 1` para todo `ρ`).
Riemann–von Mangoldt não está; numericamente, o termo principal em `T = 10¹⁰⁰` é **`≈ 3,62·10¹⁰¹`** (não `10¹⁰²`).

| Afirmação | Estado |
| --- | --- |
| `C₊ ∩ C₋` = zeros; rotação `J`; Cauchy–Riemann; gradientes ortogonais | CERTIFIED |
| todo mínimo local de `\|ζ\|` é zero; sem máximo local; mínimo na fronteira de compacto sem zeros | CERTIFIED |
| resíduo `(s − ρ)f′/f → m`; `m = 1` no 1º zero e nos triviais | CERTIFIED |
| sem curva de zeros; zeros externos infinitos ⟺ alturas ilimitadas | CERTIFIED |
| modelo `cosh(s − ½)`: simetrias de `ξ`, todos os zeros na linha | CERTIFIED |
| arquimediano, `ω`, `½ + ε`, `1 + ω = ω < ω + 1` | CERTIFIED |
| Riemann–von Mangoldt `N(T)` | não formalizado (BUILD_PENDING) |
| interseção `C₊ ∩ C₋` fora da linha | OPEN_MATH (equivale a `¬RH`) |

Numérico (`codigo/componentes.py`, `dados/componentes.json`, `testes/test_componentes.py`, 7 testes): Cauchy–Riemann
no 1º zero a `10⁻⁹`; na malha `0,05 ≤ σ ≤ 0,95`, `10 ≤ t ≤ 100`, **29 mínimos locais, todos sobre os 29 zeros da linha**
(conferidos por Newton); em `0,55 ≤ σ ≤ 0,95`, **nenhum** mínimo interior e o mínimo global na borda `σ = 0,55`;
`(s − ρ₁)ζ′/ζ − 1 = O(d)`; `N(10³) ≈ 649`, `N(3·10¹²) ≈ 1,2363·10¹³` (a contagem de Platt–Trudgian), espaçamento
médio `≈ 0,0275` em `10¹⁰⁰`; zeros do modelo `cosh` na linha.

## 4ac. Forçar um zero: o quarteto construído, o certificado de módulo mínimo, caudas e zeros booleanos (rodada 23)

`ATK/ZeroClasses/Forcar.lean` (32 teoremas, total 6865, só axiomas padrão). O que se pode **forçar**, e onde.

**O quarteto construído** (`Pq_eq_Q`, `Pq_zero_iff`, `Pq_refl`, `Pq_conj`, `quarteto_fora`, `quarteto_gigante`).
`P(s) = ((s − ½)² − δ² + T²)² + 4T²δ²` é exatamente o `Q δ T` da rodada 19. Seus zeros são **exatamente**
`½ ± δ ± iT`, ele tem as duas simetrias de `ξ`, e com `δ = 1/(2·10¹⁰⁰⁰+1)`, `T = 10¹⁰⁰` os quatro zeros estão fora
da linha. Zeros forçados, mas de `P`, não de `ζ`.

**Somar não força** (`Xi_lambda_refl`, `Xi_lambda_conj`, `somar_nao_forca`). `Ξ_λ = ξ + λP` mantém as simetrias
(`λ` real), mas em cada zero `ρ` de `P`, `Ξ_λ(ρ) = ξ(ρ)`: `Ξ_λ(ρ) = 0 ⟺ ζ(ρ) = 0`.

**O certificado de módulo mínimo** (`cota_fronteira`, `certificado_modulo_minimo`, `certificado_E1`,
`certificado_E1_refuta`). A Mathlib não tem Rouché; o kernel usa o princípio do módulo máximo aplicado a `1/f`. Se
`‖f′(z) − f′(c)‖ ≤ L` no disco fechado e

  `2|f(c)| + L·r < r|f′(c)|`,

então `f` tem um zero no disco aberto. Com `‖f″‖ ≤ M₂`: `2|f(c)| + M₂r² < r|f′(c)|`. A forma afiada
`|f(c)| + M₂r²/2 < r|f′(c)|`, com unicidade, precisa de Rouché e fica BUILD_PENDING; a unicidade já vem do
certificado de contração (§4aa). Para `ζ`, um disco fora da linha que passa o teste **refuta RH**. Exemplos
provados: `f(z) = z − (4/5 + 10i)` e `f(z) = (z − c) + ¼(z − c)² + 1/20` em `B(¾ + 10i, ⅛)` têm zero com `Re > ½`;
`g(z) = 1 + (z − c)` não passa e não tem zero.

**Cauda por certificados e o mundo `H_ext`** (`cauda_por_certificados`, `Hext`, `hext_iff`, `hext_refuta`,
`hext_quartetos`, `teoria_conjunta`). Infinitos certificados em discos disjuntos fora da linha ⟹ infinitos zeros
externos. `H_ext` (zeros externos em alturas arbitrariamente grandes) ⟺ o conjunto externo é infinito; `H_ext ⟹ ¬RH`,
com quartetos acima de toda altura. Uma hipótese independente `Q` (por exemplo `SAT ∉ P`) só se **compõe**:
`H_ext → Q → ¬RH ∧ Q`; nenhuma implica a outra.

**Zeros booleanos e aritméticos** (`viol_eq_prod`, `R_zero_iff`, `sat_iff_zero`, `lacuna`, `lacuna_min`,
`exemplo_sat`, `exemplo_unsat`, `div_iff_zero`, `exemplo_84`). `R_φ(x) = Σ_C q_C(x)`, `q_C = ∏_{ℓ∈C}(1 − ℓ(x))`:
`φ ∈ SAT ⟺ ∃x, R_φ(x) = 0`, e **`R_φ(x) < 1 ⟹ R_φ(x) = 0`** — a lacuna discreta que a `ζ` não tem. `b ∣ a ⟺ ∃k,
a − bk = 0`; `84 − 7·12 = 0` e `7 ∤ 85`.

**Zero assintótico ≠ zero** (`limite_sem_zero`, `quase_polinomial`). `1/(n+1) → 0` sem nunca ser `0`;
`(log x)²/x → 0`, mas `x^{log x}` supera `C·xᵏ` para todo `k` e `C`.

| Afirmação | Estado |
| --- | --- |
| quarteto `½ ± δ ± iT` de `P`, simetrias, gigante fora da linha | CERTIFIED (para `P`) |
| `Ξ_λ(ρ) = ξ(ρ)` nos zeros de `P` | CERTIFIED |
| certificado de módulo mínimo e forma `E1` (constantes `2` e `M₂r²`) | CERTIFIED |
| forma afiada de `E1` via Rouché | CERTIFIED na rodada 25 (`E1_afiado`, §4ae) |
| exemplos linear e quadrático; contraexemplo | CERTIFIED |
| cauda por certificados; `H_ext ⟺` externos infinitos; `H_ext ⟹ ¬RH` | CERTIFIED |
| SAT ⟺ zero booleano; lacuna; divisibilidade; zero assintótico | CERTIFIED |
| `ζ` passa o certificado em algum disco fora da linha | OPEN_MATH (equivale a `¬RH` para zeros simples) |
| `P ≠ NP` | OPEN_MATH (só entra como hipótese `Q`) |

Numérico (`codigo/forcar.py`, `dados/forcar.json`, `testes/test_forcar.py`, 6 testes): `P = Q` e os quatro zeros;
`Ξ_λ(ρ) = ξ(ρ)` para `λ = 1, 10, 10⁶`; os três exemplos; **discos em torno dos zeros 1–5 da linha passam** o
certificado (`L` amostrado) e **os 164 discos fora da linha** em `0,6 ≤ σ ≤ 0,9`, `10 ≤ t ≤ 50` **falham todos**; 200
fórmulas 3-SAT aleatórias (`n = 6`) com a lacuna `R = 0` ou `R ≥ 1`.

## 4ad. As pontes B1–B23 no kernel: SAT, determinantes, espectro, ordem de anulação, função geradora, e P vs NP no modelo genuíno (rodada 24)

`ATK/ZeroClasses/Pontes.lean` (44 teoremas, total 6909, só axiomas padrão). As pontes enviadas passam a ser
teoremas, e a parte de P vs NP fica ligada ao modelo genuíno que o kernel já tinha: `classeP`, `classeNP` sobre
`Turing.FinTM2` (Mathlib), `P_sub_NP`, `SAT ∈ NP` e o teorema de Cook–Levin (`ATK.CookLevinNP.red_SAT`).

**Contagem genérica** (`Nz`, `Zpol`, `ordem_Zpol`, `det_diag_zero_iff`, `nucleo_iff`, `posto_mais_nucleo`,
`det_regularizado`, `lacuna_espectral`, `Fger_zero`, `Fger_aprox`, `recupera_contagem`). Para `r : ι → ℕ` num tipo
finito:

* `ord_{t=0} ∏ᵢ(t + rᵢ²) = #{i | rᵢ = 0}` e `det(diag(r²) + tI) = ∏ᵢ(rᵢ² + t)`;
* `det diag(r) = 0 ⟺ ∃ rᵢ = 0 ⟺ diag(r) tem núcleo não trivial`; posto + `N` = `|ι|`;
* lacuna espectral: ou algum `rᵢ² = 0`, ou todos `≥ 1`;
* `F(z) = Σ z^{rᵢ}`: `F(0) = N`, `0 ≤ F(z) − N ≤ |ι|·z`; com `|ι|·z ≤ ¼`, **todo `v` a menos de `¼` de `F(z)`
  arredonda para `N`** (T2 / ATK-CLOSED-3).

**SAT em `Fin n`** (`B1_divisibilidade`, `S_um_iff`, `sat_iff_raiz_real`, `cadeia_sat`, `contagem_unificada`,
`exemplo_um`, `exemplo_zero`). `B > m ⟹ (R = 0 ⟺ B ∣ R)` (B1); `∏(1 − q_C) = 1 ⟺ R = 0` (B10); **SAT ⟺ o polinômio
real `Q_φ = R_φ² + Σ(xᵢ(1 − xᵢ))²` tem raiz real** (B2); e a cadeia

  `SAT ⟺ N > 0 ⟺ det D = 0 ⟺ núcleo ≠ 0 ⟺ ord₀ Z > 0 ⟺ F(0) > 0`,  `#SAT = ord₀ Z = F(0)`

(ATK-CLOSED-1/2). `(x∨y)∧(¬x∨y)∧(x∨¬y)` tem `N = 1` (`Z = t(1+t)³`); `x ∧ ¬x` tem `N = 0` (`Z = (1+t)²`).

**A ordem de anulação no modelo genuíno** (`RK_zero_iff`, `var_lt`, `satisfativel_iff_fin`,
`satisfativel_iff_ordem`, `ZERO_ORDER`, `zero_order_eq_sat`). Para as fórmulas `CNF` do kernel (índices em `ℕ`),
`ZERO_ORDER = {cod ψ | ord_{t=0} Z_ψ(t) > 0}` **é** a linguagem `SAT`.

**As relações entre P e NP** (`p_le_np`, `p_ge_np_iff`, `p_gt_np_falso`, `p_lt_np_iff`, `dicotomia`,
`p_eq_np_iff_sat`, `p_ne_np_iff_sat`, `p_eq_np_iff_zero_order`, `p_ne_np_iff_zero_order`, `aproximacao_nao_basta`,
`aproximacao_com_retorno`, `troca_quantificadores`). A lista `P = NP`, `P ≥ NP`, `P > NP`, `P < NP`, `P ≤ NP`,
`P ≈ NP`, `P ≠ NP` fica decidida **até onde é decidível**:

| Relação | Estado no kernel |
| --- | --- |
| `P ≤ NP` | teorema (`p_le_np`) |
| `P > NP` | falso (`p_gt_np_falso`) |
| `P ≥ NP` | `⟺ P = NP` (`p_ge_np_iff`) |
| `P < NP` | `⟺ P ≠ NP` (`p_lt_np_iff`) |
| `P = NP` ou `P < NP` | exatamente um (`dicotomia`) — **qual dos dois é OPEN_MATH** |
| `P = NP` | `⟺ SAT ∈ P ⟺ ZERO_ORDER ∈ P` (Cook–Levin) |
| `P ≈ NP` (classe `R` com `P ⊆ R ⊇ NP`) | não dá igualdade (`aproximacao_nao_basta`); só com `R ⊆ P` |
| `∀k ∃A_k` em `n^{k+1}` | não é `∃A ∃c`: `n^{n+1}` supera todo `C·n^c` (`troca_quantificadores`) |

A correção do material enviado vale: a aproximação de `F(2^{−(n+2)})` com erro `< ¼` equivale a **contar** (`#SAT`),
o que é mais forte do que decidir SAT; a negação disso não dá `P ≠ NP`.

**Pendência fechada** (`xi_deriv_simples`, `xi_deriv_primeiro_zero`): em todo zero simples não trivial,
`ξ′(ρ) = ½ρ(ρ−1)Γℝ(ρ)ζ′(ρ) ≠ 0`; em particular `ξ′(ρ₁) ≠ 0`.

| Afirmação | Estado |
| --- | --- |
| B1, B2, B10–B19, T2, ATK-CLOSED-1/2/3 | CERTIFIED |
| `ZERO_ORDER = SAT` no modelo genuíno | CERTIFIED |
| `P ≤ NP`, `¬(P > NP)`, `P ≥ NP ⟺ P = NP`, `P < NP ⟺ P ≠ NP`, dicotomia | CERTIFIED |
| `P = NP ⟺ SAT ∈ P ⟺ ZERO_ORDER ∈ P` | CERTIFIED (Cook–Levin no kernel) |
| `ξ′(ρ₁) ≠ 0` | CERTIFIED |
| qual de `P = NP` / `P < NP` vale | OPEN_MATH |
| princípio do argumento, Rouché | CERTIFIED na rodada 25 (§4ae) |
| Riemann–von Mangoldt | BUILD_PENDING (ausente da Mathlib) |

Numérico (`codigo/pontes.py`, `dados/pontes.json`, `testes/test_pontes.py`, 4 testes): 300 fórmulas aleatórias
(`n ≤ 7`) — `ord₀ Z = N`, `det = 0 ⟺ SAT`, posto + `N` = `2ⁿ`, T2 e B1 em **todas**; `Z = t(1+t)³` e `(1+t)²` nos
exemplos. Tudo por enumeração de `2ⁿ` atribuições: as pontes mudam a linguagem, não o custo.

## 4ae. O que faltava na Mathlib: princípio do argumento, Rouché e `E1` afiado (rodada 25)

`ATK/ArgPrincipio.lean` (12 teoremas) e `ATK/ZeroClasses/Rouche.lean` (9 teoremas): total 6930, só axiomas padrão.
A Mathlib tinha a integral de Cauchy em círculos, `∮ (z − w)⁻¹ = 2πi` e a extração de zeros de funções meromorfas
(`MeromorphicOn.extract_zeros_poles`), mas **não** o princípio do argumento nem Rouché. Agora o kernel tem os dois.

**Princípio do argumento** (`principio_argumento`). Se `f` é analítica numa vizinhança de `B̄(c, R)` e não se anula
no círculo, então

  `∮_{|z−c|=R} f′(z)/f(z) dz = 2πi · Σ_{u ∈ B(c,R), f(u)=0} ord_u f`.

A prova engrossa o disco (`engrossa`), mostra que a ordem é finita (`ordem_finita`), fatora `f = ∏(z − u)^{d u}·g`
com `g` sem zeros (Mathlib), transforma a igualdade codiscreta em igualdade numa vizinhança de cada ponto do
círculo (`codiscreta_vizinhanca`), e soma: `∮ (z − u)⁻¹ = 2πi` dentro, `0` fora (`integral_inv_fora`), e
`∮ g′/g = 0` (`integral_logDeriv_sem_zeros`).

**Rouché** (`rouche`). Se `|g − f| < |f|` no círculo, `f` e `g` têm o mesmo número de zeros (com multiplicidade)
no disco. A prova é a simétrica: `g/f` cai em `Re > 0` no círculo, onde `log` é analítico, logo
`∮ (g′/g − f′/f) = ∮ (log(g/f))′ = 0`.

**`E1` afiado** (`taylor2`, `deriv_ne_zero_of_ordem_um`, `E1_afiado`). Com Taylor de ordem 2
(`|f(z) − f(c) − f′(c)(z − c)| ≤ (M/2)|z − c|²` se `|f″| ≤ M`) e Rouché contra `L(z) = f′(c)(z − c)`:

  `|f(c)| + M r²/2 < r|f′(c)|`  ⟹  `f` tem **exatamente um** zero em `B(c, r)`, e ele é **simples**.

É a forma enviada (ATK-E1), agora com unicidade; ela substitui o certificado mais fraco de §4ac
(`2|f(c)| + M r² < r|f′(c)|`, só existência).

**Para `ζ`** (`contagem_zeta`, `rouche_zeta`, `E1_zeta_fora`, `E1_zeta_linha`, `cauda_E1`):

* `∮ ζ′/ζ = 2πi·#zeros` em todo disco fechado sem o polo e sem zeros no círculo;
* qualquer aproximante `F` com `|ζ − F| < |F|` no círculo tem o mesmo número de zeros que `ζ`;
* um disco **fora da linha** que passa `E1` afiado contém exatamente um zero de `ζ`, simples e fora da linha —
  **refuta RH**;
* um disco **centrado na linha** (raio `< ½`) que passa `E1` afiado contém exatamente um zero, e ele está **na
  linha** (a torção o fixa);
* infinitos discos disjuntos fora da linha passando `E1` ⟹ infinitos zeros externos.

O exemplo quadrático enviado (`1/20 + (½)(⅛)²/2 = 69/1280 < 160/1280`) tem **exatamente um** zero em `B(¾ + 10i, ⅛)`,
com `Re > ½` (`exemplo_quadratico_unico`).

| Afirmação | Estado |
| --- | --- |
| princípio do argumento em círculos | CERTIFIED |
| Rouché | CERTIFIED |
| Taylor de ordem 2 com `M/2` | CERTIFIED |
| `E1` afiado: exatamente um zero, simples | CERTIFIED |
| `E1` para `ζ`: fora da linha ⟹ `¬RH`; na linha ⟹ zero na linha | CERTIFIED |
| `ζ` passar `E1` num disco fora da linha | OPEN_MATH (equivale a `¬RH` para zeros simples) |
| princípio do argumento em retângulos, Riemann–von Mangoldt | BUILD_PENDING |

Numérico (`codigo/argumento.py`, `dados/argumento.json`, `testes/test_argumento.py`, 3 testes):
`(1/2πi)∮ ζ′/ζ` por trapézios dá `1,00000` em torno do 1º zero, `0,00000` em discos fora da linha e `2,99999` no
disco `|z − (½ + 20i)| = 7` (zeros 14,13; 21,02; 25,01); Rouché com `F = ζ′(ρ₁)(z − ρ₁)` no raio `0,05`
(`|ζ − F|/|F| ≤ 0,021`); `E1` afiado perto do 1º zero (`0,0009 < 0,0040`, `M` amostrado).

## 4af. O finito exato, a aritmética terminal e a faixa tolerante (rodada 26)

`ATK/ZeroClasses/Finito.lean` (30 teoremas, total 6960; quatro não usam axioma nenhum, os demais só os padrão).

**SAT finito exato** (`Fpol_eval_zero`, `ordem_Fpol`, `codificacao_inteira`, `Zp_cotas`, `Zp_log_cotas`, `Zp_limite`,
`exemplo_A`, `exemplo_B`, `exemplo_C`, `exemplos_pela_codificacao`). Para `r : ι → ℕ` num tipo finito:

* `F(z) = Σ z^{rᵢ}`: `F(0) = N` e **`ord_{z=0} F = min rᵢ`** — o mínimo de cláusulas violadas. São duas ordens de
  anulação diferentes: `ord₀ det(L + tI) = #SAT` (§4ad) e `ord₀ F = min R`;
* **codificação inteira** (ATK-FINITE-1): se `rᵢ ≤ m` e `B > |ι|`, então `⌊(Σᵢ B^{m − rᵢ})/B^m⌋ = N`. Com `B = 2^{n+1}`,
  `#SAT` é o dígito principal de um inteiro, sem limite nem aproximação;
* **função de partição**: `Z(τ) = Σ e^{−τ rᵢ}` satisfaz `e^{−τμ} ≤ Z ≤ |ι|e^{−τμ}`,
  `μ − log|ι|/τ ≤ −log Z(τ)/τ ≤ μ` e `−log Z(τ)/τ → μ = min R`;
* os três casos enviados, por `decide`: `M_A = 704 = (1300)₈`, `M_B = 8 = (020)₄`, `M_C = 81 = (121)₈`;
  `det(L + I) = 8, 4, 20`; `#SAT = 1, 0, 1` — e o teorema geral recupera os três.

**Aritmética terminal** (`satAdd_assoc`, `satAdd_comm`, `terminal_absorve`, `cancelamento_falha`,
`colapso_congruencia`, `zero_um_trivial`, `Ev_nao_aditivo`, `boxplus_tabela`, `boxplus_nao_assoc`, `divisao_terminal`,
`arredonda_um_iff`, `E01_unifica`, `E01_soma_mal_definida`):

* a soma saturada `min(Z, a + b)` é **associativa e comutativa**, `Z ⊕ 1 = Z`, `Z − Z = 0`, e **perde o cancelamento**
  (`Z ⊕ 1 = (Z−1) ⊕ 1`);
* uma congruência aditiva com `0 ∼ 1` identifica **todos** os naturais; num semianel, `0 = 1` força o trivial;
* o avaliador `E(1) = 0` não é aditivo (`E(1+1) = 2`, `E(E1 + E1) = 0`) e `a ⊞ b = E(min(Z, a + b))` **não é
  associativa**: `(0⊞1)⊞1 = 0`, `0⊞(1⊞1) = 2` (a tabela enviada, `Z = 7`, confere);
* `Z/Z = 1 ≠ 0` num corpo: o "`≡ 0`" é a leitura `E(1) = 0`, não a divisão;
* `round x = 1 ⟺ ½ ≤ x < 3/2`; o estado "01" em `[0, 3/2)` dá `E(0) = E(1) = E(1,49999)`, mas a soma **não** é bem
  definida nas classes: `E(0 + 1) = 01 ≠ 2 = E(1 + 1)`.

**A faixa tolerante** (`Tol`, `exemplos_tolerancia`, `torcao_tol`, `fora_em_tol`, `tol_refuta`, `rh_iff_tolerancias`,
`tol_verificada`, `exemplos_nao_zeros`). `T_ε = {0 < Re s < 1, |Re s − ½| ≤ ε}` contém `9/20 + 10i` e `11/20 + 10i`
(fora da linha), é invariante pela torção com a mesma distância à linha, e todo zero fora da linha está em alguma
`T_ε`. Um zero de `ζ` em `T_ε` fora da linha refuta RH; RH ⟺ todo zero está a menos de `ε` da linha para todo `ε > 0`.
Com `VerificadoAte H` (Platt–Trudgian) nenhum ponto de `T_ε` fora da linha com `|t| ≤ H` é zero; em particular os dois
pontos enviados não são zeros. **A tolerância não impõe zeros.**

| Afirmação | Estado |
| --- | --- |
| `ord₀ F = min R`, codificação inteira, função de partição, casos A/B/C | CERTIFIED |
| soma saturada; colapso de `0 ∼ 1`; `⊞` não associativa; estado "01" mal definido na soma | CERTIFIED |
| faixa tolerante; zero nela fora da linha ⟹ `¬RH`; RH ⟺ todas as faixas | CERTIFIED |
| `9/20 + 10i`, `11/20 + 10i` não são zeros | CERTIFIED condicional a `VerificadoAte` |
| calcular `M_φ` (ou seu dígito principal) sem enumerar `2ⁿ` atribuições | OPEN_MATH (é `#SAT`) |

Numérico (`codigo/finito.py`, `dados/finito.json`, `testes/test_finito.py`, 3 testes): os três casos com aritmética
inteira exata; 300 fórmulas aleatórias com `⌊M/B^m⌋ = #SAT`, `ord₀ F = min R` e as cotas da função de partição em
**todas**; associatividade da soma saturada em `0..8`; `⊞` e o estado "01".

## 4ag. A fronteira entre estados, antes do colapso (rodada 27)

`ATK/ZeroClasses/Fronteira.lean` (72 teoremas, total 7032, só os axiomas padrão). Formaliza a aritmética de
estados com fronteira enviada: quantização, produtor multivalorado, adjacência, competição `Δ_ab`, a ponte com RH,
intervalos e uma semântica de três valores.

**Quantização** (`Q`, `cel`, `Q_eq_round`, `Q_eq_iff`, `celulas_particao`, `celulas_disjuntas`, `celulas_exemplos`,
`Q_int`, `Q_add_int`, `Q_monotone`, `Q_proximo`, `Q_nao_aditivo`, `Q_soma_cotas`, `Q_soma_cotas_atingidas`).
`Q(x) = ⌊x + ½⌋` é o `round` de Mathlib; `Q x = k ⟺ x ∈ C_k = [k − ½, k + ½)`; as células particionam `ℝ`; `Q` é
monótona, comuta com translações inteiras e escolhe um inteiro mais próximo. **O colapso não é aditivo**:
`Q(x + y) − Q x − Q y ∈ {−1, 0, 1}`, e os dois extremos ocorrem (`Q(½ + ½) = 2Q(½) − 1`, `Q(⅖ + ⅖) = 2Q(⅖) + 1`).

**Produtor multivalorado** (`P`, `Q_mem_P`, `P_interior`, `P_fronteira`, `P_exemplos`, `P_sub`, `P_dois_iff`,
`P_eq_argmin`, `colapso_fronteira`). `P(x) = {k ∈ ℤ | |x − k| ≤ ½}`:

* `P(x) = {k}` no interior, `P(k + ½) = {k, k + 1}`; em particular **`P(½) = {0, 1}`, `P(3/2) = {1, 2}`**;
* `P(x) ⊆ {Q x − 1, Q x}`, contém `Q x`, e tem dois elementos **exatamente** nas fronteiras `k + ½`;
* `P(x)` é exatamente o conjunto dos inteiros mais próximos de `x`;
* o colapso desempata para cima: `Q(k + ½) = k + 1`, embora `k ∈ P(k + ½)`.

**Adjacência** (`Adj`, `adj_iff`, `adj_exemplos`, `adj_nao_transitiva`, `adj_symm`, `adj_irrefl`, `colapso_fecho`,
`fecho_tudo`). Compartilhar uma fronteira ⟺ `|a − b| = 1`. `0 ∼ 1` e `1 ∼ 2`, mas **não** `0 ∼ 2`: a adjacência
não é transitiva. Toda equivalência que a contém identifica **todos** os inteiros; o fecho de equivalência
(`Relation.EqvGen`) é a relação total.

**Competição** (`Dif`, `Dif_fatora`, `Dif_zero_iff`, `Dif_equidistante`, `Dif_neg_iff`, `Dif_lado`, `Dif01`,
`Dif01_zero_iff`, `Dif12_zero_iff`, `meio_equidistante`, `Dif_reflexao`, `Dif01_antissim`, `reflexao_fixa`,
`fronteira_iff`, `fronteira_iff_Dif`). `Δ_ab(x) = (x − a)² − (x − b)² = (b − a)(2x − a − b)`; para `a ≠ b`,
`Δ_ab = 0 ⟺ x = (a + b)/2 ⟺ |x − a| = |x − b|`, e `Δ_ab < 0 ⟺ x está mais perto de a`. `Δ₀₁ = 2x − 1` zera só em
`½`, `Δ₁₂` só em `3/2`. A reflexão `x ↦ a + b − x` troca o sinal; `x ↦ 1 − x` fixa só `½`. **A fronteira de `P`
entre `k` e `k + 1` é exatamente o zero de `Δ_{k,k+1}`.**

**Ponte com RH** (`Dif01_re`, `ponte_iff_RH`, `zero_iff_re_im`, `nao_rh_iff_produtor`, `dl`, `dl_zero_iff`,
`classifica`, `regiao_decimo`, `distancias_exemplos`, `reflexo_zero`, `simetria_permite_pares`,
`tolerancia_independente`):

* **ATK-RH-BRIDGE ⟺ RH** (`ponte_iff_RH`): a ponte é a própria hipótese, não um lema disponível;
* **o "produtor que falta"** — `σ + it` com `0 < |σ − ½| ≤ ε < ½` e `Re ζ = Im ζ = 0` — **existe ⟺ RH é falsa**;
* `d(s) = |Re s − ½|`; classificação exata em central / tolerante fora da linha / fora da tolerância;
  `T_{1/10} = {⅖ ≤ Re s ≤ ⅗}`; `d(9/20 + 10i) = d(11/20 + 10i) = 1/20`;
* a reflexão `β + iγ ↦ (1 − β) + iγ` leva zeros a zeros, preserva `d` e troca o sinal de `Δ₀₁`;
* a simetria sozinha admite pares fora da linha (`{9/20, 11/20}`), e a tolerância é independente da função: há
  função sem zeros em `T_ε` e função com zero em `T_ε` fora da linha.

**Intervalos** (`Intervalo`, `pts`, `soma`, `neg`, `sub`, `pt`, `larg`, `larg_nonneg`, `soma_correta`, `pts_soma`,
`soma_assoc`, `soma_comm`, `soma_zero`, `pt_soma`, `larg_soma`, `sub_auto`, `zero_mem_sub_auto`,
`sub_auto_eq_zero_iff`, `sem_inverso`, `estados`, `estados_iff`, `estados_pt`, `estados_tolerancia`,
`estados_unidade`). A soma de intervalos é **exata** (igual à soma de Minkowski), associativa, comutativa, com
neutro; as larguras somam. `I − I = [−w, w]` contém `0` e **só é `{0}` para estado fixo** — "`Z − Z = 0`" vale
exatamente quando a tolerância é zero; com tolerância positiva **não há inverso aditivo**. Os estados de
`[lo, hi]` são os `k` com `lo ≤ k + ½` e `k − ½ ≤ hi`: `[⅖, ⅗]` e `[0, 1]` têm os estados `{0, 1}` (o estado "01");
`[0, 3/2]` já toca o estado `2`.

**Semântica de três valores** (`Valor`, `aval`, `aval_ne_falso_iff`, `aval_fronteira_iff`, `aval_meio`,
`aval_colapso`). "`x` está no estado `k`" é verdadeiro (`|x − k| < ½`), fronteira (`= ½`) ou falso; não-falso ⟺
`k ∈ P(x)`; fronteira ⟺ `x = k ± ½`; em `½`, os estados `0` e `1` valem *fronteira* e `2` vale falso; o colapso
respeita a verdade.

| Afirmação | Estado |
| --- | --- |
| `Q`, células, não aditividade do colapso com erro em `{−1, 0, 1}` | CERTIFIED |
| `P(½) = {0, 1}`, `P(3/2) = {1, 2}`, `P = argmin`, dois estados ⟺ fronteira | CERTIFIED |
| adjacência ⟺ `\|a − b\| = 1`, não transitiva; fecho transitivo colapsa tudo | CERTIFIED |
| `Δ_ab = (b − a)(2x − a − b)`, zero ⟺ ponto médio; fronteira de `P` = zero de `Δ` | CERTIFIED |
| simetria `Δ₀₁(1 − x) = −Δ₀₁(x)`; reflexão dos zeros preserva `d` | CERTIFIED |
| ATK-RH-BRIDGE ⟺ RH; produtor fora da linha ⟺ `¬RH` | CERTIFIED (equivalências) |
| intervalos: soma exata, sem inverso; estados de `[lo, hi]`; semântica de três valores | CERTIFIED |
| todo zero não trivial está na fronteira `Δ₀₁ = 0` | OPEN_MATH (é RH) |
| existe zero com `0 < \|σ − ½\| ≤ ε` | OPEN_MATH (é `¬RH`) |

Numérico (`codigo/fronteira.py`, `dados/fronteira.json`, `testes/test_fronteira.py`, 3 testes), em aritmética
exata: 4001 racionais em `[−5, 5]` com `P = argmin`, `|P| ≤ 2`, `|P| = 2` só nas fronteiras; 160 801 pares com
`Q(x + y) − Q x − Q y ∈ {−1, 0, 1}` (21 000 / 120 801 / 19 000); adjacência e fecho em `{−6..6}` (uma classe);
1997 triplas para `Δ`; 300 pares de intervalos (Minkowski, larguras, `I − I`, estados por força bruta). Em ponto
flutuante: `|ζ(9/20 + 10i)| ≈ 1,567`, `|ζ(11/20 + 10i)| ≈ 1,531`; a reflexão do primeiro zero é zero.

## 4ah. Empurrar a fronteira: `m₄ > 0` provado e a competição `Re(ξ′/ξ)` (rodada 28)

Quatro arquivos, **60 teoremas** (total 7092), só os axiomas padrão; as verificações numéricas são feitas pelo
próprio kernel (`decide +kernel`, sem `native_decide`).

A partir desta rodada, cada resultado é classificado em quatro classes: **reformulação** (P ⟺ RH), **consequência**
(RH ⟹ P), **parcial** (P provada sem RH, mais fraca que RH) e **alavanca** (P provada sem RH e P ⟹ RH). Só a
última cruza a linha.

**1. O primeiro ponto aberto do `FinalAudit`, fechado** (`ZeroClasses/QuartoAval.lean`, `QuartoGeral.lean`,
`Quarto.lean`). `K₄ = {¼ + it : ¼ ≤ t ≤ 4}` e `m₄ = inf_{K₄} |ζ|`:

* **avaliação certificada de `ζ(¼ + it)`** (`mem_zetaI4`): Euler–Maclaurin `EM_{6,8}` com resto explícito,
  `n^{¼}` por intervalos racionais (`lo⁴ ≤ n ≤ hi⁴`, `mem_qrt`), `e^{iθ}` e `log n` pelos certificados de §4f;
* **cota grosseira geral** (`cota_geral`, `cotaQ_spec`): para `Re w > 0`, `‖w‖ ≤ R`, `‖w − 1‖ ≥ d`,
  `‖ζ(w)‖ ≤ N + N/d + ½ + Σ_{j=2}^{M} |B_j|/j!·(R)_{j−1}N^{1−j} + (R)_M/M!·C_M·N^{1−M}/(M − 1)`, com valor
  racional calculado pelo kernel;
* **Cauchy** (`deriv_cota`): `‖ζ′‖ ≤ B/r` no segmento; **peça** (`peca`, `peca_cert`): malha de passo `h` com
  `‖ζ(c)‖ ≥ (B/r)h + δ` nos centros ⟹ `‖ζ‖ ≥ δ`; **cobertura** (`cobre`, `cobre_seg`, `centros_seg`);
* **as quatro peças** (`peca1`–`peca4`): `[¼, 1]`, `[1, 2]`, `[2, 3]`, `[3, 4]`, `r = 6/25`, `B = 6,11; 4,91;
  4,35; 4,76`, **95 centros**, cada um um retângulo certificado de `ζ(¼ + it)`;
* **`cota_K4`: `|ζ(s)| ≥ 1/20` em todo `K₄`**; **`m4_cota`: `m₄ ≥ 1/20`**; `m4_pos`; `K4_sem_zeros`;
  `m4_menor_um` (`m₄ < 1`, pelo retângulo em `¼ + 2i`);
* `espelho_sem_zeros`: pela torção, também `ζ(¾ + it) ≠ 0` para `¼ ≤ t ≤ 4`;
* `novo_primeiro_ponto`: o primeiro ponto aberto passa a ser **`m₅ > 0`** (`K₅ = [⅕, 3/10] × [⅕, 5]`, uma região
  bidimensional), com `m₅ > 0 ⟺ ζ` sem zeros em `K₅` e `RH ⟹ m₅ > 0`. **Na rodada 29 (§4ai) `m₅, …, m₁₃ > 0` ficam
  provados de uma vez e o primeiro ponto aberto passa a ser `m₁₄ > 0`.**

**2. A competição analítica** (`ZeroClasses/Lagarias.lean`). `L(s) = Re(ξ′(s)/ξ(s))` é a versão analítica de `Δ₀₁`
(§4ag):

* `Lg_antissim`: `L(1 − s̄) = −L(s)` (a mesma lei de `Δ₀₁(1 − x) = −Δ₀₁(x)`, `Lg_e_Dif_antissim`); `Lg_linha`:
  `L(½ + it) = 0`;
* `deriv_log_norm`: **`∂_σ log|ξ(σ + it)| = L(σ + it)`** onde `ξ ≠ 0`;
* `sinal_negativo`: num zero de `ξ` com `Re ρ > ½`, `L < 0` logo à esquerda (o resíduo `m/(s − ρ)` domina);
* **`positividade_implica_RH`** (meia-ponte de Lagarias): `L ≥ 0` em `Re s > ½` (fora dos zeros) ⟹ RH;
  **`monotonia_implica_RH`** (Sondow–Dumitrescu): `|ξ(σ + it)|` estritamente crescente em `σ > ½` ⟹ RH;
* `positividade_iff_RH_de`, `monotonia_iff_RH_de`: com as recíprocas nomeadas (Lagarias 1999, Sondow–Dumitrescu
  2010; dependem do produto de Hadamard de `ξ`, ausente da Mathlib: BUILD_PENDING), as duas condições são
  **equivalentes** a RH; `nao_RH_forca_negativo`: `¬RH` ⟹ existe `s` com `Re s > ½` e `L(s) < 0`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `ζ ≠ 0` em `K₄` e no espelho `σ = ¾`, `¼ ≤ t ≤ 4`; `1/20 ≤ m₄ < 1` | CERTIFIED | parcial |
| avaliação certificada de `ζ(¼ + it)`; cota grosseira geral; certificado de peça | CERTIFIED | ferramenta |
| `L(1 − s̄) = −L(s)`, `L = 0` na linha, `L = ∂_σ log\|ξ\|` | CERTIFIED | incondicional |
| `L ≥ 0` em `Re s > ½` ⟹ RH; monotonia de `\|ξ\|` ⟹ RH | CERTIFIED | reformulação (meia) |
| RH ⟹ `L > 0` em `Re s > ½` (Lagarias), RH ⟹ monotonia | BUILD_PENDING (Hadamard) | consequência |
| `m₅ > 0` | OPEN (finito, verificável; próximo ponto) | parcial |
| `L ≥ 0` sem RH | OPEN_MATH | seria alavanca |

Numérico (`codigo/quarto.py`, `dados/quarto.json`, `testes/test_quarto.py`, 3 testes): `m₄ ≈ 0,46114` em
`t ≈ 2,175`, espelho `min |ζ(¾ + it)| ≈ 0,585`; nas quatro peças, a cota racional domina o máximo amostrado de `|ζ|`
na região, `B/r` domina `|ζ′|` no segmento, e a folga entre `|ζ|` nos centros e o limiar é `≥ 0,027`; `L(½ + it) ≈ 0`
(`< 10⁻⁸`), antissimetria `< 10⁻⁸`, `L > 0` em todos os 2400 pontos de `½ < σ ≤ 2`, `0,5 ≤ t ≤ 40`; num modelo
com zero artificial em `0,7 + 30i`, `L(ρ − h) ≈ −1/h`.

## 4ai. Nenhum zero de `ζ` até a altura 13: `VerificadoAte 13` vira teorema (rodada 29)

Seis arquivos, **128 teoremas** (total 7220), só os axiomas padrão; 930 avaliações certificadas de `ζ`, todas
verificadas pelo kernel (`decide +kernel`, sem `native_decide`).

**Ferramentas** (`ZeroClasses/FaixaAval.lean`, `FaixaGeral.lean`):

* **`ζ(σ + it)` certificada para `σ` racional qualquer** (`mem_zetaIG`): `m^{−σ}` por certificado de raiz
  (`lo^q m^p ≤ 1 ≤ hi^q m^p`, `σ = p/q`), com o candidato calculado pelo kernel por bissecção inteira (`iroot`);
  resto de Euler–Maclaurin com `N^{1−σ−M} = N · N^{−σ} · N^{−M}`;
* **retângulos** (`ret`, `convex_ret`, `reg_ret`, `deriv_cota_ret`, `cobre_ret`, `centrosR_ret`, `chkR_spec`,
  `peca_ret`, `ret_split_re`, `ret_split_im`): região de Cauchy `[s0 − r, s1 + r] × [a − r, b + r]`, cota grosseira
  `cotaQ` (§4ah), `‖ζ′‖ ≤ B/r`, malha `nσ × nt` com raio `h ≥ √(hσ² + ht²)`.

**As peças** (`FaixaPecas1`–`3`): `[½, 1] × [43/50, 13]` dividido em **50 retângulos** por bissecção adaptativa
(`codigo/faixa_plano.py` escolhe a divisão e a malha; `codigo/faixa_lean.py` escreve o Lean), `r = 2/5`,
`δ = 1/50`, 930 centros.

**Resultados** (`ZeroClasses/Faixa.lean`):

* `faixa_ate_13`: **`|ζ(s)| ≥ 1/50` em `½ ≤ Re s ≤ 1`, `43/50 ≤ Im s ≤ 13`**;
* **`faixa_sem_zeros`: `ζ(s) ≠ 0` para `0 < Re s < 1` e `|Im s| ≤ 13`**. A metade `Re s < ½` vem da torção
  `s ↦ 1 − s̄`, `Im s < 0` da conjugação e `Im² < ¾` de `zeta_ne_zero_baixo`;
* **`verificado_13`: `VerificadoAte 13`** — a hipótese nomeada (Platt–Trudgian) é teorema até a altura 13;
* `zeros_acima_13`: todo zero não trivial tem `|Im ρ| > 13`; `primeiro_zero_entre`: com `ρ₁` (§4f), o zero de
  menor altura positiva está em `13 < γ₁ ≤ 14,1347…`;
* `m_pos_ate_13`: **`m_n > 0` para todo `4 ≤ n ≤ 13`**; `novo_primeiro_ponto_14`: o primeiro ponto aberto passa a
  ser `m₁₄ > 0`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `ζ ≠ 0` na faixa crítica com `\|Im s\| ≤ 13`; `VerificadoAte 13` | CERTIFIED | parcial |
| `m₄, …, m₁₃ > 0`; `13 < γ₁ ≤ 14,1347…` | CERTIFIED | parcial |
| avaliação de `ζ` com `σ` racional; certificado de retângulo | CERTIFIED | ferramenta |
| `VerificadoAte H` para `13 < H ≤ 3·10¹²` | hipótese nomeada (Platt–Trudgian) | — |
| `m₁₄ > 0` (o novo primeiro ponto; finito, exige refinar a malha perto de `½ + 14i`) | OPEN | parcial |
| `∀ n ≥ 4, m_n > 0` | OPEN_MATH (é RH) | — |

Numérico (`codigo/faixa.py`, `dados/faixa.json`, `dados/faixa_plano.json`, `testes/test_faixa.py`, 2 testes):
as 50 cotas racionais, malhas, raios e limiares conferidos em frações exatas; a área dos retângulos é exatamente a
de `[½, 1] × [43/50, 13]` (`607/100`); folga mínima `|ζ(c)| − v ≥ 0,012`; `min |ζ| ≈ 0,526` na metade direita e
`≈ 0,389` na esquerda; o primeiro zero `½ + 14,134725141734693i`.

## 4aj. A fórmula de Jensen da Mathlib aplicada a `ξ`: `N(T) = O(T log T)` (rodada 30)

Um arquivo, **17 teoremas** (total 7237), só os axiomas padrão. A Mathlib já tinha a **fórmula de Jensen**
(`AnalyticOnNhd.sum_divisor_le`: zeros em `‖s − c‖ ≤ r` com multiplicidade `≤ log(M/‖f c‖)/log(R/r)` quando
`‖f‖ ≤ M` em `‖s − c‖ = R`); faltava aplicá-la a `ξ`. `ZeroClasses/Jensen.lean`:

* **cotas de crescimento**: `cota_zeta` (`‖(s − 1)ζ(s)‖ ≤ 1 + ‖s − 1‖(½ + 3‖s‖)` em `Re s ≥ ½`, Euler–Maclaurin de
  ordem 1); `cota_Gammaℝ` (`‖Γℝ(s)‖ ≤ Γ(Re s/2)`); `Gamma_le_um`, `Gamma_le` (`Γ(x) ≤ 4 + n!` em `¼ ≤ x ≤ n + 1`:
  convexidade em `[1, 2]`, `Γ(x) = Γ(x+1)/x` abaixo de 1, monotonia acima de 2);
* **cota de `ξ` na bola** (`Bx`, `Bx_ge`, `norm_le_de`, `cota_xi_direita`, `cota_xi`): `‖ξ(s)‖ ≤ Bx R n` em
  `‖s − ½‖ ≤ R` se `R + ½ ≤ 2(n + 1)`; o lado `Re s < ½` pela equação funcional `ξ(1 − s) = ξ(s)`;
* **Jensen para `ξ`** (`xi_metade_ne_zero`, `jensen_xi`): `ξ(½) ≠ 0` e
  `Σ div ξ (‖s − ½‖ ≤ T + 1) ≤ log(Bx(2T + 2, ⌈T⌉ + 1)/‖ξ(½)‖)/log 2`;
* **as ordens coincidem** (`ordem_zeta_eq_xi`, `ordemNat_zeta_eq_xi`): para `Re ρ > 0`, `ρ ≠ 1`,
  `ord_ρ ζ = ord_ρ ξ` (perto de `ρ`, `ζ = ξ · g` com `g = 2Γℝ⁻¹/(s(s − 1))` analítica e `g(ρ) ≠ 0`);
* **a contagem** (`zerosAte_sub_bola`, `N_le_divisor`, `N_cota`): a `N(T)` de `ATK.FechamentoO1` (zeros com
  `0 < Im ρ ≤ T`, com multiplicidade) satisfaz **`N(T) ≤ log(Bx(2T + 2, ⌈T⌉ + 1)/‖ξ(½)‖)/log 2`**;
* **`N_O_TlogT`: `∃ C, ∀ T ≥ 2, N(T) ≤ C · T · log T`** (com `log_Bx_le`:
  `log Bx ≤ 13 log T + 4 T log T`; `C = ((13 + |log ξ(½)|/log 2)/2 + 4)/log 2 ≈ 15,9`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `N(T) ≤ log(Bx/‖ξ(½)‖)/log 2`; `N(T) = O(T log T)` | CERTIFIED | parcial |
| `ord_ρ ζ = ord_ρ ξ` na faixa; `‖ξ‖ ≤ Bx` na bola; Jensen para `ξ` | CERTIFIED | ferramenta |
| `N(T) = (T/2π) log(T/2π) − T/2π + O(log T)` (`RiemannVonMangoldt`) | BUILD_PENDING | — |
| `N(T + 1) − N(T) = O(log T)` (Jensen local; exige a simetria das ordens `ρ ↦ 1 − ρ̄`) | BUILD_PENDING | ferramenta |
| `Σ_ρ m_ρ/\|ρ\|^{1+ε} < ∞` e o produto de Hadamard de `ξ` | BUILD_PENDING | alavanca (Lagarias, §4ah) |
| RH | OPEN_MATH | — |

`N_O_TlogT` é a metade superior (fraca) de Riemann–von Mangoldt, com a ordem de grandeza certa: é a entrada que o
produto de Hadamard de `ξ` precisa (expoente de convergência dos zeros `≤ 1`). Não diz nada sobre **onde** estão os
zeros.

Numérico (`codigo/contagem.py`, `dados/contagem.json`, `testes/test_contagem.py`, 2 testes): `ξ(½) = 0,4971207781…`;
`cota_zeta` em 1331 pontos (razão máxima `0,43`); `Γ ≤ 4 + n!` em `[¼, n + 1]` para `n ≤ 12`; `max |ξ|` na
circunferência de raio `R` muito abaixo de `Bx`; a cota de Jensen fica acima do termo principal de Riemann–von
Mangoldt e de `N(100) = 29`, `N(1000) = 649`, e abaixo de `C·T·log T`; a razão cota/`T log T` tende a `1/log 2 ≈ 1,44`,
cerca de 9 vezes `1/(2π)`.

## 4ak. Jensen local, `Σ_ρ 1/|ρ|² < ∞` e o produto canônico: `HadamardXi` vira uma identidade (rodada 31)

Dois arquivos, **31 teoremas** (total 7268), só os axiomas padrão.

**Jensen local** (`ZeroClasses/JensenLocal.lean`, 23 teoremas). A fórmula de Jensen da Mathlib, agora para `ζ` em bolas
de raio fixo centradas em `2 + iy`, onde `|ζ(2 + iy)| ≥ 2 − π²/6` (`BLProva.zeta_dois_lb`):

* `cota_zeta_circ`: `|ζ(s)| ≤ 15|y| + 62` em `‖s − (2 + iy)‖ ≤ 19/10`, `|y| ≥ 4` (Euler–Maclaurin de ordem 1);
* `jensen_local`: os zeros em `‖s − (2 + iy)‖ ≤ 8/5`, com multiplicidade, são `≤ Lc |y|`, onde
  `Lc t = log((15t + 62)/(2 − π²/6))/log(19/16)`;
* `ordem_xi_reflexao`, `ordemNat_zeta_reflexao`: **`ord_{1−ρ} ζ = ord_ρ ζ`** na faixa (via `ξ(1 − s) = ξ(s)` e
  `analyticOrderAt_comp_of_deriv_ne_zero`);
* `caixa_le`: para qualquer conjunto finito de pontos da faixa com `|Im ρ − y| ≤ ½`, `Σ m_ρ ≤ 2 Lc |y|`. A metade
  `Re ρ ≥ ½` fica na bola de `2 + iy`; a outra é refletida para a bola de `2 − iy`;
* **`N_succ_le`: `N(T + 1) − N(T) ≤ 2 Lc(T + ½)`** e **`N_local_O_log`: `N(T + 1) − N(T) = O(log T)`**;
* **`soma_ordem_inv_quadrado`: `Σ_ρ m_ρ/|ρ|² < ∞`** e `soma_inv_quadrado`: `Σ_ρ 1/|ρ|² < ∞`, somando sobre **todos** os
  zeros da faixa. A prova soma por blocos `⌈|Im ρ|⌉ = n`, usa `|Im ρ| > 13` da rodada 29 e compara com `n^{−3/2}`.

**O produto canônico** (`ZeroClasses/Canonico.lean`, 8 teoremas):

* `E1 z = (1 − z)e^z`, `E1_sub_one_le`: `‖E1 z − 1‖ ≤ 3‖z‖²` para `‖z‖ ≤ 1`;
* `ZM`: os zeros com multiplicidade (`Σ ρ : Z, Fin m_ρ`); `summable_ZM`;
* **`canonico_converge`: `∏_{(ρ, j)} (1 − s/ρ)e^{s/ρ}` converge incondicionalmente para todo `s`**; `Pcan s` é o valor;
* `produtos_simetricos`: os produtos parciais simétricos de `HadamardXi` (`|Im ρ| ≤ T`, com multiplicidade)
  convergem para `Pcan s`;
* **`hadamardXi_iff`: `HadamardXi ⟺ ∃ A B, ∀ s, ξ(s) = e^{A + Bs} · Pcan(s)`**.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `N(T + 1) − N(T) = O(log T)`; `ord_{1−ρ} ζ = ord_ρ ζ` | CERTIFIED | ferramenta |
| `Σ_ρ m_ρ/\|ρ\|² < ∞`, `Σ_ρ 1/\|ρ\|² < ∞` | CERTIFIED | parcial (convergência de Hadamard) |
| o produto canônico converge; `HadamardXi ⟺ ξ = e^{A+Bs}·P` | CERTIFIED | ferramenta (redução) |
| `ξ = e^{A + Bs}·P` (a identidade de Hadamard: `ξ/P` inteira, sem zeros, de ordem `≤ 1`) | BUILD_PENDING | alavanca (Lagarias, §4ah) |
| `RiemannVonMangoldt` | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Das três peças ausentes da Mathlib em `NecessidadeRH` (§4aj), `HadamardXi` deixa de ser um enunciado sobre limites e
vira uma identidade entre duas funções definidas. Isso ainda não prova RH nem a necessidade.

Numérico (`codigo/canonico.py`, `dados/canonico.json`, `testes/test_canonico.py`, 2 testes): 138 zeros `0 < γ ≤ 300`
por trocas de sinal da função `Z` de Riemann–Siegel, com contagem a menos de 1 de Riemann–von Mangoldt em
`T = 50, …, 300`. `N(T + 1) − N(T)` fica no máximo em 2% da cota `2 Lc(T + ½)`. `Σ_{|γ| ≤ 300} 1/|ρ|²`, mais a cauda
estimada, dá `0,0461912` contra `2 + γ − log 4π = 0,0461914`. Com `A = −log 2` e `B = −γ/2 − 1 + ½ log 4π`, a
identidade `ξ(s) ≈ e^{A+Bs}·P_{300}(s)` vale em `s = 2` e `s = ½ + 2i` com erro relativo de cerca de 1%, dentro da
cauda `|s|²·Σ_{|γ|>300} 1/|ρ|²`.

## 4al. O produto canônico é inteiro, com exatamente os zeros de `ξ` (rodada 32)

Um arquivo, **30 teoremas** (total 7298), só os axiomas padrão. `ZeroClasses/CanonicoInteira.lean`:

* **`soma_ordem_inv_pot`: `Σ_ρ m_ρ/|ρ|^p < ∞` para todo `p > 1`** (`gp`, `gp_le`, `summable_gp`, `summable_ZM_pot`).
  É o argumento de blocos da §4ak com `n^{−(p+1)/2}` no lugar de `n^{−3/2}`;
* o fator: `E1_eq_zero_iff` (`E1 z = 0 ⟺ z = 1`) e **`norm_E1_le`: `‖E1 z‖ ≤ e^{3‖z‖^{3/2}}`** para todo `z`;
* **produtos gerais** `∏'_i E1(z/r_i)`, com `r_i ≠ 0` e `Σ 1/|r_i|² < ∞`:
  * convergem uniformemente em bolas (`prodE_tendstoUniformlyOn`, via `Summable.hasProdUniformlyOn_one_add` da Mathlib);
  * são **inteiros** (`prodE_differentiable`, limite localmente uniforme de funções holomorfas);
  * **não se anulam** fora dos `r_i` (`prodE_ne_zero`, via `cexp_tsum_eq_tprod`);
  * satisfazem **`‖∏'‖ ≤ exp(3‖z‖^{3/2} Σ 1/|r_i|^{3/2})`** (`prodE_norm_le`);
* para `P = Pcan`:
  * `Pcan_differentiable` e `Pcan_norm_le` (`log|P(s)| ≤ 3S|s|^{3/2}`);
  * `Pcan_ne_zero` fora de `Z`;
  * `Pcan_fator`: `P = E1(s/ρ₀)^{m₀} · P_resto`, com `P_resto(ρ₀) ≠ 0`;
  * **`ordem_Pcan`: `ord_ρ P = m_ρ`**;
* **`xi_eq_zero_iff_Z`: os zeros de `ξ` são exatamente os zeros de `ζ` na faixa**; **`ordem_Pcan_eq_xi`:
  `ord_z P = ord_z ξ` para todo `z ∈ ℂ`**.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `P` inteira, `ord_z P = ord_z ξ` em todo `z`, `log\|P\| = O(\|s\|^{3/2})` | CERTIFIED | ferramenta |
| `Σ_ρ m_ρ/\|ρ\|^p < ∞` (`p > 1`); zeros de `ξ` = `Z` | CERTIFIED | ferramenta |
| `ξ = e^{A+Bs}·P` (`ξ/P` inteira, sem zeros, de ordem `≤ 1` ⟹ `e^{A+Bs}`) | BUILD_PENDING (rodada seguinte) | alavanca |
| RH | OPEN_MATH | — |

Do lado de `P` está tudo pronto: `ξ/P` é inteira e sem zeros, e `log|P| = O(|s|^{3/2})`. Falta o argumento de ordem:
Poisson para `Re log(ξ/P)`, Borel–Carathéodory, e as estimativas de Cauchy para `(log(ξ/P))″ = 0`.

Numérico (`codigo/inteira.py`, `dados/inteira.json`, `testes/test_inteira.py`, 2 testes):
`max log‖E1‖/(3‖z‖^{3/2}) = 0,25` em `|z| ≤ 6`; `S_{3/2} ≈ 0,50`, sendo `0,28` da soma até 300 e `0,22` da cauda;
`log|P_{300}|` em `|s| = 40` vale `20,6`, contra a cota `376`. Com os zeros refinados pela secante em `Ξ`,
`|P_{300}(ρ₁ + h)|/h` estabiliza (zero simples), e `ξ/P_{300}` perto de `ρ₁` é liso e igual a `e^{A+Bρ₁}` vezes a
cauda `exp(−ρ₁²/2 · Σ_{|γ|>300} 1/ρ²)`, a menos de `10⁻⁴`.

## 4am. O teorema de Hadamard para `ξ` (rodada 33)

Um arquivo, **23 teoremas** (total 7321), só os axiomas padrão. **`hadamardXi : HadamardXi`**: existem `A, B` com
`ξ(s) = lim_{T→∞} e^{A+Bs} ∏_{|Im ρ| ≤ T} ((1 − s/ρ)e^{s/ρ})^{m_ρ}`, sem hipóteses. A Mathlib não tem a fatoração
de Hadamard; a prova junta as rodadas 30–32 com seis ferramentas que a Mathlib tem (`ZeroClasses/Hadamard.lean`):

1. **o quociente** (`existe_quociente`): funções inteiras com a mesma ordem em todo ponto diferem por um fator
   inteiro sem zeros. Com `ordem_Pcan_eq_xi` (§4al), `ξ = P · F`;
2. **o logaritmo** (`existe_log`): `F = e^g` com `g` inteira. É a primitiva de `F′/F`, pelo teorema de Morera da
   Mathlib (`Differentiable.isExactOn_univ`);
3. **a média** (`media_mono_fora`, `posLog_Pcan_le`, `posLog_xi_le`, `media_posLog_exp_le`): em `|z| = R ≥ 2`,
   `média log⁺|e^g| ≤ média log⁺|ξ| + média log⁺|P| − média log|P| ≤ (34 + 3S) R^{3/2}`. Três ingredientes:
   * `log⁺(ab) ≤ log⁺a + log⁺b` fora dos zeros de `P` no círculo, que são finitos;
   * a fórmula de Jensen da Mathlib dá `média log|P| ≥ log|P(0)| = 0`;
   * as cotas `‖ξ‖ ≤ Bx` (§4aj) e `log|P| ≤ 3S|s|^{3/2}` (§4al);
4. **Poisson** (`nucleo_cotas`, `re_g_le`): `Re g(w) ≤ 3 · média log⁺|e^g|` em `|w| ≤ R/2`, pela fórmula de Poisson da
   Mathlib com o núcleo `≤ (R + |w|)/(R − |w|) ≤ 3`;
5. **Borel–Carathéodory** (`norm_g_le`, da Mathlib): `|g| ≤ 2(3K R^{3/2} + 1) + 3|g(0)|` em `|z| ≤ R/4`;
6. **Cauchy duas vezes** (`norm_g2_le`, `g2_zero`, `g_afim`): `|g″(z₀)| ≤ 1024·B(R)/R² → 0`, logo `g″ ≡ 0` e
   `g(z) = g(0) + g′(0)z`;
7. **conclusão** (`xi_hadamard`, `hadamardXi`): `ξ = e^{A+Bs}·P`, e pela redução `hadamardXi_iff` (§4ak) segue
   `HadamardXi`. `necessidade_iff`: `NecessidadeRH` passa a depender só de Riemann–von Mangoldt, de Littlewood sob RH e
   da dedução clássica.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `HadamardXi`: `ξ = e^{A+Bs} ∏ ((1 − s/ρ)e^{s/ρ})^{m_ρ}` | CERTIFIED | ferramenta/alavanca |
| `NecessidadeRH ⟺ RvM ∧ Littlewood ∧ dedução` | CERTIFIED | redução |
| a recíproca de Lagarias (RH ⟹ `Re ξ′/ξ ≥ 0` em `Re s > ½`) via `ξ′/ξ = B + Σ (1/(s − ρ) + 1/ρ)` | BUILD_PENDING | redução |
| `RiemannVonMangoldt`, `LittlewoodSobRH` | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Das três peças ausentes da Mathlib em `NecessidadeRH`, Hadamard é a primeira fechada. Isso não toca a posição dos
zeros.

Numérico (`codigo/hadamard_xi.py`, `dados/hadamard_xi.json`, `testes/test_hadamard_xi.py`, 2 testes):
* as constantes:
  * `A = log ξ(0) = −log 2`;
  * `B = ξ′(0)/ξ(0) = −0,0230957090` por diferença finita, igual a `−γ/2 − 1 + ½ log 4π` a `10⁻¹¹`;
  * `−Σ Re(1/ρ)` até 300, mais a cauda, dá `−0,0230989`;
* a identidade `ξ = e^{A+Bs}·P_{300}·cauda`, com `cauda(s) ≈ exp(−s²/2 · Σ_{|γ|>300} 1/ρ²)`, vale com erro
  relativo `≤ 3·10⁻⁴` em `s = 2, ½+2i, 3+5i, −1+3i, ½+10i`;
* `g″ ≈ 6·10⁻⁶`, o ruído da diferença finita.

## 4an. As recíprocas de Lagarias e de Sondow–Dumitrescu, sem hipóteses (rodada 34)

Um arquivo, **14 teoremas** (total 7335), só os axiomas padrão. A rodada 28 deixou `RecLagarias` e `RecMonotonia`
como hipóteses nomeadas, porque dependiam do produto de Hadamard. Com `hadamardXi` (§4am) as duas viram teoremas
(`ZeroClasses/LagariasHadamard.lean`):

* `Pcan_localmente`: o produto canônico converge localmente uniformemente em `ℂ`;
* `logDeriv_E1`, `summable_logDeriv`, **`logDeriv_xi_eq`: `ξ′/ξ(s) = B + Σ_{(ρ,j)} (1/(s − ρ) + 1/ρ)`** onde
  `ξ(s) ≠ 0`, via `logDeriv_tprod_eq_tsum` da Mathlib; `Lg_eq` dá a parte real;
* **`Lg_sob_RH`: sob RH, `L(s) = Σ_{(ρ,j)} (σ − ½)/|s − ρ|²`**. A constante `Re B + Σ Re 1/ρ` sai de `L(½) = 0`
  (`Lg_linha`, §4ah), e `termo_sob_RH` faz a conta termo a termo;
* **`rec_lagarias : RecLagarias`**; `Lg_pos`: sob RH, `L > 0` em `Re s > ½`, porque há um zero de verdade
  (`existe_zero_altura`);
* **`rec_monotonia : RecMonotonia`**: sob RH, `σ ↦ |ξ(σ + it)|` é estritamente crescente em `σ > ½`
  (`∂_σ log|ξ| = L > 0`, `deriv_log_norm`);
* **`positividade_iff_RH`: `(Re ξ′/ξ ≥ 0 em Re s > ½, fora dos zeros) ⟺ RH`** e **`monotonia_iff_RH`:
  `(|ξ(σ + it)| estritamente crescente em σ > ½ para todo t) ⟺ RH`**, sem hipóteses.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `ξ′/ξ = B + Σ (1/(s − ρ) + 1/ρ)`; sob RH, `L = Σ (σ − ½)/\|s − ρ\|²` | CERTIFIED | ferramenta |
| `positividade_iff_RH`, `monotonia_iff_RH` (Lagarias 1999, Sondow–Dumitrescu 2010) | CERTIFIED | reformulação |
| `∀ s, Re s > ½ → ξ(s) ≠ 0 → Re ξ′/ξ(s) ≥ 0` (sem RH) | OPEN_MATH (é RH) | alavanca |
| RH | OPEN_MATH | — |

As duas condições têm agora exatamente a força de RH, e isso está certificado. Provar qualquer uma delas sem RH
seria provar RH.

Numérico (`codigo/lagarias_rec.py`, `dados/lagarias_rec.json`, `testes/test_lagarias_rec.py`, 2 testes):
* em `s = 2, 0,8+5i, 0,6+14i, 1,5+30i`, `ξ′/ξ` por diferença finita bate com `B + Σ_{|γ| ≤ 300}` mais a cauda
  `≈ s·Σ_{|γ|>300} 1/γ²` (erro `≤ 2,5·10⁻⁴`), e `L` bate com `Σ (σ − ½)/|s − ρ|²` mais a cauda (erro `≤ 4·10⁻⁵`);
* `L(½) ≈ 10⁻¹⁰`;
* `|ξ(σ + it)|` é estritamente crescente em `½ < σ ≤ 3` para `t = 0,3, 5, 14,13, 20, 50`.

## 4ao. O expoente de convergência dos zeros é exatamente 1; há infinitos zeros (rodada 35)

Um arquivo, **12 teoremas** (total 7347), só os axiomas padrão (`ZeroClasses/Expoente.lean`):

* `norm_E1_le_lin`: `‖(1 − z)e^z‖ ≤ e^{2‖z‖}`; `prodE_norm_le_lin`: se `Σ 1/|r_i| < ∞`, então
  `‖∏' E1(z/r_i)‖ ≤ e^{2‖z‖ Σ 1/|r_i|}`;
* `zeta_lb_re_ge_dois`: `|ζ(s)| ≥ 2 − π²/6` em `Re s ≥ 2`; **`xi_lb_par`: `|ξ(2n + 2)| ≥ (2 − π²/6)·n!/π^{n+1}`**
  (`Γ(n + 1) = n!`);
* **`nao_somavel_ZM`: `Σ_{(ρ,j)} 1/|ρ| = ∞`**. Se a série convergisse, o teorema de Hadamard (§4am) daria
  `|ξ(s)| ≤ e^{a + K|s|}`, e `n! ≤ C·Dⁿ` contradiz `Dⁿ/n! → 0`. `soma_ordem_inv_diverge` é a mesma coisa sobre `Z`;
* **`expoente_exato`: `Σ_ρ m_ρ/|ρ|^p < ∞ ⟺ p > 1`**, junto com §4al;
* **`zeros_infinitos`**: `Z` é infinito. `conj_mem_Z` dá a simetria `ρ ↦ ρ̄`, e daí `zeros_infinitos_acima`: há
  infinitos zeros com `Im ρ > 0`. Com `ordem_pos`, **`N_tende_infinito`: `N(T) → ∞`**.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| expoente de convergência dos zeros `= 1`; `Σ 1/\|ρ\| = ∞` | CERTIFIED | consequência |
| infinitos zeros não triviais; `N(T) → ∞` | CERTIFIED | consequência |
| `N(T)/T → ∞` (`CrescimentoN`, B10) | BUILD_PENDING (pede as constantes de RvM) | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/expoente.py`, `dados/expoente.json`, `testes/test_expoente.py`, 2 testes): `Σ_{|γ| ≤ T} 1/|ρ|`
segue `(log(T/2π))²/(2π)` (2,35 contra 2,38 em `T = 300`) e diverge, enquanto `Σ 1/|ρ|^{1,2}` cresce cada vez mais
devagar. `|ξ(2n + 2)|` fica acima de `(2 − π²/6)·n!/π^{n+1}` para `n ≤ 40`, e `log ξ(s)/s` cresce sem parar.

## 4ap. O lema de Landau: a derivada logarítmica perto do centro de um disco (rodada 36)

Um arquivo, **5 teoremas** (total 7352), só os axiomas padrão (`ZeroClasses/Landau.lean`). A Mathlib não tem o lema;
ele é a ferramenta local que substitui a fórmula de Hadamard nas regiões livres de zeros (§4aq).

* `quociente_local`: se `ord Q ≤ ord f` num aberto `U`, então `f = Q·G` com `G` analítica em `U`, e `G ≠ 0` onde as
  ordens coincidem (`Q` sem ordem infinita);
* `ordem_monomio`, `ordem_poli`: a ordem de `∏_{u ∈ S} (z − u)^{m_u}` em `w` é `m_w` (ou `0` fora de `S`);
  `logDeriv_poli`: sua derivada logarítmica é `Σ m_u/(z − u)`;
* **`landau`**: se `f` é analítica em `‖z − z₀‖ ≤ R`, `f(z₀) ≠ 0` e `‖f‖ ≤ M‖f(z₀)‖` no disco (`M ≥ 1`), existe o
  conjunto finito `S` dos zeros em `‖z − z₀‖ ≤ R/4`, e

  `‖f′/f(z₀) − Σ_{ρ ∈ S} m_ρ/(z₀ − ρ)‖ ≤ 16(log M + 1)/R`.

  A prova junta quatro ferramentas da Mathlib: o quociente `G = f/Q` pelos zeros de `S`; o módulo máximo para `G`
  em `‖z − z₀‖ ≤ R/2` (`|Q| ≥ (R/4)ⁿ` no círculo e `|Q(z₀)| ≤ (R/4)ⁿ`, logo `|G| ≤ M|G(z₀)|`); o logaritmo
  `G = G(z₀)e^h` no disco `R/4`, com `Re h ≤ log M`; e Borel–Carathéodory mais Cauchy no círculo `R/8`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| lema de Landau (forma no centro) | CERTIFIED | ferramenta |
| RH | OPEN_MATH | — |

Numérico (`codigo/landau.py`, `dados/landau.json`, `testes/test_landau.py`, 2 testes): a cota vale nos três casos
testados. Num polinômio com um zero duplo e um simples no disco pequeno, o resto é exatamente o termo do zero de fora
(`1/3` contra a cota `119,5`). Para `ζ` em `0,55 + 14,13i` com `R = 1`, `S = {ρ₁}` e o erro é `0,41` contra `70,2`;
em `1,1 + γ₁i` com `R = ½`, `S` é vazio e o erro é `1,30` contra `45,8`.

## 4aq. A região livre de zeros de de la Vallée Poussin (rodada 37)

Um arquivo, **19 teoremas** (total 7371), só os axiomas padrão (`ZeroClasses/RegiaoLivre.lean`). A Mathlib tem só a
não anulação em `Re s ≥ 1`; aqui está a primeira região livre de zeros à esquerda dessa reta.

* **cotas perto de `Re s = 1`**: `cota_zeta_faixa`: `|ζ(s)| ≤ 3|Im s| + 12` em `½ ≤ Re s ≤ 3`, `|Im s| ≥ 1` (pela cota
  de Euler–Maclaurin de §4aj); `cota_zeta_real`: `|ζ(σ)| ≤ 8/(σ − 1)` em `1 < σ ≤ 2`;
* **a cota inferior**: `prod341` é o produto `|ζ(σ)³ζ(σ + it)⁴ζ(σ + 2it)| ≥ 1` da Mathlib, lido para `ζ`, e daí
  `zeta_lb`: `|ζ(σ + it)|⁴ ≥ (σ − 1)³/(512(6|t| + 12))`;
* **Landau para `ζ`** (§4ap, `zeta_local`) no disco `‖z − (σ + it)‖ ≤ ½`. Os termos `Re m_ρ/(s − ρ)` são `≥ 0`
  (`re_termo_nonneg`, `re_lt_um`), logo `re_logDeriv_local`: `−Re ζ′/ζ(σ + it) ≤ 32(2 log|t| + log(1/(σ − 1)) + 7)`.
  Com um zero `ρ = β + iγ` a `1/8` do centro, `re_logDeriv_local_zero` desconta `1/(σ − β)`;
* **o polo** (`polo`): `−Re ζ′/ζ(σ) ≤ 1/(σ − 1) + C` em `1 < σ ≤ 2`. Aqui `G(s) = 2ξ(s)/(sΓℝ(s)) = (s − 1)ζ(s)`
  (`Gp_eq`), `G ≠ 0` em `[1, 2]` e `ζ′/ζ = G′/G − 1/(s − 1)`; `C` sai por compacidade;
* **a desigualdade 3-4-1** (`tres_quatro_um`): `3 Re(−ζ′/ζ)(σ) + 4 Re(−ζ′/ζ)(σ + it) + Re(−ζ′/ζ)(σ + 2it) ≥ 0`,
  termo a termo na série `Σ Λ(n)n^{−s}` (`termo341`: `3 + 4 cos θ + cos 2θ = 2(1 + cos θ)²`);
* **a montagem**. Em `regiao_livre_grande`, `σ = 1 + 1/(962 log|γ|)`, e `4/(σ − β) ≤ (2886 + 481) log|γ|` dá
  `1 − β ≥ 1/(6734 log|γ|)` para `|γ| ≥ T₀`. Em **`regiao_livre`, existe `c > 0` com `β ≤ 1 − c/log|γ|` para todo
  zero não trivial com `|γ| ≥ 2`**: os zeros com `|γ| < T₀` são finitos (`IsCompact.inter_riemannZetaZeros_finite`).
  Na forma de não anulação, `zeta_ne_zero_regiao` dá `ζ(s) ≠ 0` em `Re s > 1 − c/log|Im s|`, `|Im s| ≥ 2`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| região livre de zeros `β ≤ 1 − c/log\|γ\|` (`\|γ\| ≥ 2`) | CERTIFIED | parcial |
| desigualdade 3-4-1 para `−ζ′/ζ`; cota local `O(log\|t\|)` | CERTIFIED | ferramenta |
| RH | OPEN_MATH | — |

A região encosta em `Re s = 1` quando `|γ| → ∞` e não chega perto de `Re s = ½`. RH continua OPEN_MATH.

Numérico (`codigo/regiao_livre.py`, `dados/regiao_livre.json`, `testes/test_regiao_livre.py`, 3 testes). Na grade
testada, `|ζ(s)|/(3|t| + 12)` não passa de `0,084`, `(σ − 1)|ζ(σ)|` de `1,65` (a cota é `8`), e o produto 3-4-1 fica
acima de `4,9`. A combinação 3-4-1 de `−ζ′/ζ` fica acima de `5,1`. `−ζ′/ζ(σ) − 1/(σ − 1)` vai a `−γ_E` (`−0,576` em
`σ = 1,001`). A cota local usa no máximo `0,1 %` de si mesma. A aritmética confere: `2886 + 481 = 3367 = 7·481` e
`c = δ/7 = 1/6734`.

## 4ar. Littlewood sob RH: `1/ζ(σ + it) = O(|t|^ε)`; `NecessidadeRH` reduz-se a Riemann–von Mangoldt (rodada 38)

Um arquivo, **13 teoremas** (total 7384), só os axiomas padrão (`ZeroClasses/LittlewoodRH.lean`). **`LittlewoodSobRH`,
uma das três peças de `NecessidadeRH` que estavam BUILD_PENDING, agora é teorema.**

* `tres_circulos`: **os três círculos de Hadamard**, que a Mathlib não tem, saem do teorema das três retas da
  Mathlib aplicado a `w ↦ g(c + e^w)` na faixa `log r₁ ≤ Re w ≤ log r₃`;
* `log_bola`: `F ≠ 0` holomorfa num disco é `F(c)·e^H` com `H(c) = 0`. Mais `zeta_ne_zero_RH` (sob RH, `ζ ≠ 0` em
  `Re s > ½`), `cota_zeta_re` (`|ζ| ≤ K` em `Re s ≥ 5/4`) e `young_rpow` (`B x^a ≤ εx + C` para `a < 1`);
* `nucleo` usa o disco em torno de `c = 3 + it` (`|t| ≥ 3`). No disco grande, `Re H = log|ζ/ζ(c)| ≤ log(36|t|)`, e
  Borel–Carathéodory dá `|H| ≤ 20 log(36|t|)/δ` no círculo `5/2 − δ/2`. Em `Re s > 5/4`, `|H| ≤ M₁` no círculo
  `3/2`. Os três círculos dão `|H(σ + it)| ≤ M₁ (20 log(36|t|)/δ)^a` com
  `a = log((5/2 − δ)/(3/2))/log((5/2 − δ/2)/(3/2)) < 1`;
* `cota_grande`, `cota_compacta` (`1 ≤ |t| ≤ 3`, por compacidade), **`cota_sob_RH`: sob RH,
  `‖ζ(σ + it)^{±1}‖ ≤ C|t|^ε` em `σ ≥ ½ + δ`, `|t| ≥ 1`**. Daí **`littlewoodSobRH : ATK.FechamentoO1.LittlewoodSobRH`**
  e `lindelof_fora_sob_RH` (Lindelöf fora da reta, sob RH);
* **`necessidade_iff_rvm`**: `NecessidadeRH ⟺ RiemannVonMangoldt ∧ (a dedução)`, porque `HadamardXi` (§4am) e
  `LittlewoodSobRH` já são teoremas.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `LittlewoodSobRH` (RH ⟹ `1/ζ = O(\|t\|^ε)` em `σ ≥ ½ + δ`) | CERTIFIED | consequência |
| RH ⟹ `ζ = O(\|t\|^ε)` em `σ ≥ ½ + δ` | CERTIFIED | consequência |
| três círculos de Hadamard | CERTIFIED | ferramenta |
| `NecessidadeRH ⟺ RiemannVonMangoldt ∧ dedução` | CERTIFIED | alavanca |
| `RiemannVonMangoldt`; a dedução de Báez-Duarte | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

O teorema é condicional: ele usa RH como hipótese, não a prova.

Numérico (`codigo/littlewood_rh.py`, `dados/littlewood_rh.json`, `testes/test_littlewood_rh.py`, 2 testes; RH não é
usada). `log M(r)` de `e^{z²} + z³` é convexa em `log r`. O expoente vale `a(½) = 0,71`, `a(0,1) = 0,96` e
`a(0,01) = 0,996`. `|log ζ(σ + it) − log ζ(3 + it)|` fica entre `0,34` e `2,05`, contra `log(36|t|) ≥ 6,2`. Nas
janelas `t ∈ [T, 2T]` até `T = 640`, `max|ζ|^{±1}` não passa de `13` em `σ = 0,6`, e de `5,6` e `3,3` em `σ = 0,75`
e `σ = 1`.

## 4as. Stirling complexo: um logaritmo holomorfo de `Γ` (rodada 39)

Um arquivo, **23 teoremas** (total 7407), só os axiomas padrão (`ZeroClasses/StirlingComplexo.lean`). A Mathlib tem
Stirling para `n!` e a sequência de Gauss `GammaSeq z n → Γ(z)`, mas não tem um logaritmo de `Γ` complexa nem a
sua assintótica.

* `ell z = (z − ½) log z − z + ½ log 2π − Σ_k e_k(z)`, com o termo de Euler–Maclaurin explícito
  `e_k(z) = 1 − (z + k + ½)(log(z + k + 1) − log(z + k))`. A identidade `soma_log`
  (`Σ_{k ≤ n} log(z + k) = [F]₀ⁿ + (log z + log(z + n))/2 + Σ_{k<n} e_k`) é exata e não usa integrais;
* `norm_ek_le`: `|e_k(z)| ≤ 2/|z + k|²`, pelo resto de Taylor de `log(1 + x)` da Mathlib. Daí
  `tsum_norm_ek_le`: `Σ_k |e_k(z)| ≤ 8/|Im z|` para `|Im z| ≥ 2`;
* `tendsto_lgs`: `log GammaSeq(z, n) → ell z`, com Stirling para `n!`; logo **`exp_ell`: `exp(ell z) = Γ(z)`**
  em `Re z > 0`;
* **`ell_diff`: `ell` é holomorfa** em `Re z > 0`, com **`hasDerivAt_ell`: `ell′ = ψ`** (a digama da Mathlib) e
  `ell_real` (real no eixo real);
* **`stirling`: `‖ell z − ((z − ½) log z − z + ½ log 2π)‖ ≤ 8/|Im z|`** em `Re z > 0`, `|Im z| ≥ 2`;
* **`im_ell_quarto`: `|Im ell(¼ + iτ) − (τ log τ − τ − π/8)| ≤ 9/τ`** para `τ ≥ 2`. É o termo principal
  `(T/2π) log(T/2π) − T/2π` de Riemann–von Mangoldt.

A docstring de `ZeroClasses/Hadamard.lean` passa a citar `media_posLog_exp_le`; antes citava um nome inexistente
(revisão dos PRs #105 e #108). Nenhum teorema muda.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| logaritmo holomorfo de `Γ` em `Re z > 0`, `ell′ = ψ` | CERTIFIED | ferramenta |
| Stirling complexo com erro `8/\|Im z\|` | CERTIFIED | ferramenta |
| `RiemannVonMangoldt` | BUILD_PENDING (faltam o princípio do argumento em retângulos e `S(T) = O(log T)`) | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/stirling_complexo.py`, `dados/stirling_complexo.json`, `testes/test_stirling_complexo.py`,
2 testes). `exp(ell z)` reproduz o `Γ` de Lanczos a `3·10⁻¹²` em seis pontos, e `ell′` reproduz `ψ` a `3·10⁻⁷`.
O máximo de `|e_k|·|z + k|²` é `0,0833 = 1/12` (a cota é `2`). `τ·(Im ell(¼ + iτ) − (τ log τ − τ − π/8))` tende a
`1/96`, bem abaixo da cota `9`.

## 4at. O princípio do argumento em retângulos (rodada 40)

Um arquivo, **17 teoremas** (total 7424), só os axiomas padrão (`ZeroClasses/ArgRetangulo.lean`). A Mathlib tem o
teorema de Cauchy em retângulos (`integral_boundary_rect_eq_zero_of_differentiableOn`) e o divisor de funções
meromorfas, mas não tem a contagem de zeros por `∮ f′/f` num retângulo.

* `bordo g z w` é a integral de `g` no bordo do retângulo `Ret z w = [z.re, w.re] × [z.im, w.im]`, percorrido no
  sentido positivo, como soma de quatro integrais de intervalo. `Bordo z w` é o conjunto dos quatro lados;
* `bordo_congr`, `bordo_add`, `bordo_sum`, `bordo_const_mul`: `bordo` é linear e só depende de `g` no bordo;
  `bordo_cauchy`: `bordo g = 0` se `g` é holomorfa no retângulo fechado;
* **`bordo_inv`: `bordo (s ↦ 1/(s − u)) = 2πi`** para `u` no interior, por primitivas explícitas `log(s − u)` com os
  saltos `log(−x) = log x ∓ πi` (`log_neg_im_pos/neg`);
* **`principio_argumento`**: se `f` é analítica num aberto que contém o retângulo, tem ordem finita em cada ponto
  dele e não se anula no bordo, os zeros no retângulo formam um `Finset S` e
  **`bordo (f′/f) = 2πi Σ_{u ∈ S} ord_u f`**. A finitude vem do divisor da Mathlib num compacto. A prova fatora
  `f = Π (s − u)^{ord_u} · G`, com `G` sem zeros no retângulo (o quociente local da rodada 36), e aplica
  `bordo_cauchy` a `G′/G` e `bordo_inv` aos fatores.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| princípio do argumento em retângulos (com multiplicidade) | CERTIFIED | ferramenta |
| `RiemannVonMangoldt` | BUILD_PENDING (falta `S(T) = O(log T)`) | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/arg_retangulo.py`, `dados/arg_retangulo.json`, `testes/test_arg_retangulo.py`, 2 testes).
Simpson nos quatro lados dá `(1/2πi)∮ ds/(s − u) = 1` dentro (erro `10⁻⁹`) e `0` fora (`10⁻¹⁵`). Para um
polinômio com um zero duplo, um simples e um fora do retângulo, `(1/2πi)∮ f′/f = 3,0000000000`. Para `ζ` em
`[0,1; 0,9] × [10, 30]`, o resultado é `3,0000000000`: os zeros `14,13`, `21,02` e `25,01`.

## 4au. `S(T) = O(log T)`: a variação do argumento de `ζ` num segmento horizontal (rodada 41)

Um arquivo, **17 teoremas** (total 7441), só os axiomas padrão (`ZeroClasses/VariacaoArg.lean`). É o argumento
clássico de Backlund: a variação de `arg ζ` em `[½, 2] + iT` é no máximo `π` vezes (um mais) o número de zeros de
`Re ζ(σ + iT)`, e esses zeros se contam por Jensen.

* `cota_zeta_quarto`: `‖ζ(s)‖ ≤ ½ + 1/‖s − 1‖ + 6‖s‖` em `Re s ≥ ¼` (Euler–Maclaurin de ordem 1, `EM11`, `Cb1`);
  `re_zeta_dois`: `Re ζ(s) ≥ 2 − π²/6 > 0` em `Re s ≥ 2`;
* `variacao_simples`: se `Re ζ(σ + iT)` não se anula em `(a, b)`, então `|Im ∫_a^b ζ′/ζ(σ + iT) dσ| ≤ π` (há um
  logaritmo contínuo de `ζ` no semiplano `±Re > 0`);
* `variacao`: com no máximo `k` zeros de `Re ζ(σ + iT)` em `(a, b)`, a variação é `≤ (k + 1)π` (indução forte,
  cortando no zero);
* `gT(s) = (ζ(s + iT) + ζ(s − iT))/2` é analítica (`gT_analitica`), real no eixo real com `gT(σ) = Re ζ(σ + iT)`
  (`gT_real`), e `cota_gT`: `‖gT‖ ≤ 6T + 38` no disco `‖s − 2‖ ≤ 7/4`;
* `conta_zeros_re`: os zeros de `Re ζ(σ + iT)` em `(½, 2)` são no máximo `log((6T + 38)/(2 − π²/6))/log(7/6)`
  (Jensen da Mathlib, `AnalyticOnNhd.sum_divisor_le`, no disco de raio `7/4` em torno de `2`);
* **`variacao_log`: existe `C` com `|Im ∫_{1/2}^{2} ζ′/ζ(σ + iT) dσ| ≤ C log T`** para `T ≥ 4` sem zero de `ζ` no
  segmento.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `S(T) = O(log T)` (variação horizontal de `arg ζ`) | CERTIFIED | ferramenta |
| `RiemannVonMangoldt` | BUILD_PENDING (falta montar o contorno de `ξ`) | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/variacao_arg.py`, `dados/variacao_arg.json`, `testes/test_variacao_arg.py`, 2 testes).
Para `T` entre 20 e 300, `|V(T)|/log T ≤ 0,41`. O número `k` de trocas de sinal de `Re ζ` em `[½, 2]` é 0 ou 1,
contra a cota de Jensen de 40 a 55. A razão `|ζ(s)|/(½ + 1/|s − 1| + 6|s|)` fica abaixo de `0,11` na grade.

## 4av. Riemann–von Mangoldt (rodada 42)

Um arquivo, **31 teoremas** (total 7472), só os axiomas padrão (`ZeroClasses/RiemannVonMangoldt.lean`).
**`riemannVonMangoldt : ATK.FechamentoO1.RiemannVonMangoldt`**: existe `C` tal que, para todo `T ≥ 2`,

  `|N(T) − ((T/2π) log(T/2π) − T/2π)| ≤ C log T`,

com `N(T)` o número de zeros não triviais de `ζ` com `0 < Im ρ ≤ T`, **contados com multiplicidade** (a definição
`FechamentoO1.N`). A Mathlib não tem a fórmula. A prova junta as rodadas 39–41:

1. **contorno** (`bordo_eq_N`): o princípio do argumento da rodada 40 para `ξ` no retângulo `[−1, 2] × [1, T]` dá
   `∮ ξ′/ξ = 2πi N(T)`. Em `Im s = 1` não há zeros (a faixa sem zeros `|Im s| ≤ 13`), nos lados `Re s = −1` e
   `Re s = 2` também não, e no topo exige-se que `T` não seja ordenada de zero (`NaoOrdenada T`);
2. **dobra** (`lado_horizontal`, `lado_esquerdo`, `identidade`): as simetrias `ξ′/ξ(1 − s) = −ξ′/ξ(s)` e
   `ξ′/ξ(s̄) = conj ξ′/ξ(s)` levam o contorno à metade direita: `πN(T) = Im K₁ − Im K_T + Re R_T`;
3. **primitivas** (`hasDerivAt_E`, `hasDerivAt_Λ`, `lado_direito`, `topo`): com
   `E(s) = log s + log(s − 1) − (s/2) log π + log Γ(s/2)` (o `ell` da rodada 39) e `Λ = E + log ζ` em `Re s ≥ 2`
   (onde `Re ζ > 0`), **`formula_N`**: `πN(T) = Im E(½ + iT) + arg ζ(2 + iT) − Im ∫_{1/2}^{2} ζ′/ζ(σ + iT) dσ + C₁`;
4. **estimativas**: `im_E_meio` (`|Im E(½ + iT) − ((T/2) log(T/2π) − T/2 + 7π/8)| ≤ 18/T`, de `im_ell_quarto` e
   `arg_meio`), `|arg ζ(2 + iT)| ≤ π/2` e `variacao_log` (rodada 41) dão **`rvm_nao_ordenada`**;
5. **todas as alturas**: as ordenadas são finitas em cada faixa (`existe_nao_ordenada`); para `T > 13`, toma-se
   `T₁ ∈ (T − 1, T)` e `T₂ ∈ (T, T + 1)` não ordenadas, a monotonia de `N` e `m_lip`
   (`0 ≤ m(x) − m(y) ≤ log x` para `2π ≤ y ≤ x ≤ y + 1`); para `T ≤ 13`, `N(T) = 0` e `|m(T)| ≤ 20`.

Daí **`necessidade_iff_deducao`**: `NecessidadeRH` equivale à dedução de Báez-Duarte com `RiemannVonMangoldt`,
`HadamardXi` e `LittlewoodSobRH` como hipóteses, e as três agora são teoremas (rodadas 33, 38 e 42).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `RiemannVonMangoldt` (com multiplicidade) | CERTIFIED | alavanca |
| `formula_N` (fórmula exata de `πN(T)` nas alturas não ordenadas) | CERTIFIED | ferramenta |
| `CrescimentoN` (zeros *distintos*, B10) | BUILD_PENDING (não segue de RvM sem cota de multiplicidade melhor que `O(log T)`) | — |
| a dedução de Báez-Duarte (`EntradasNecessidade`) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/rvm.py`, `dados/rvm.json`, `testes/test_rvm.py`, 2 testes). Nas oito alturas de `20,5` a
`299,7`, `formula_N` reproduz `N(T)` (de 1 a 137) a `6·10⁻¹³`, com `C₁ ≈ −1,4·10⁻¹²`, isto é, `C₁ = 0`
numericamente. `|N(T) − m(T)|/log T ≤ 0,24`. `T·(Im E(½ + iT) − termo principal) ≈ 0,021`, contra a cota `18`. A
média de `N(T) − m(T) − 7/8` nas oito alturas é `−0,27`.

## 4aw. `J(ε) → 0` sob RH: uma segunda prova (rodada 43)

Um arquivo, **19 teoremas** (total 7491), só os axiomas padrão (`ZeroClasses/JSobRH.lean`). A rodada 42 deixou a
estrutura nomeada `FechamentoO1.NecessidadeRH` equivalente à dedução `RH ⇒ EntradasNecessidade`, e
`EntradasNecessidade` tem duas partes: a entrada de Littlewood (mollificador de corte abrupto) e `J(ε) → 0`.

**Já estava certificado** (2026-10-15, `ATK/NecessidadeRH.lean`): `tendsto_J_RH`, o mesmo enunciado, por
Phragmén–Lindelöf para `ζ(s)/ζ(s + ε)` (`ATK.RazaoZeta`), e **`rh_iff_DN : RH ⟺ D_N → 0`**, com o mollificador
suavizado `μ(n)(1 − n/N)₊ n^{−ε}` e Perron suavizada (`ATK.PerronSuave`). O critério de Báez-Duarte completo não está
pendente. Esta rodada dá uma **segunda prova, independente**, de

**`tendsto_J`: sob RH, `J(ε) = ∫ |1 − ζ(½ + iτ)/ζ(½ + ε + iτ)|²/|½ + iτ|² dτ → 0` quando `ε → 0⁺`,**

trocando Phragmén–Lindelöf pela monotonia de Sondow–Dumitrescu e por Stirling:

1. **monotonia em `σ = ½`** (`xi_meio_le`): sob RH, `|ξ(½ + iτ)| ≤ |ξ(½ + ε + iτ)|`, pela recíproca de
   Sondow–Dumitrescu (`rec_monotonia`, §4an) e continuidade;
2. **o fator `Γ`** (`norm_log_add_sub_le`, `razao_Gamma_alto`, `razao_Gamma_baixo`, `razao_Gamma`, `razao_Gammaℝ`):
   `|Γℝ(½ + ε + iτ)| ≤ K (1 + |τ|)^{1/4} |Γℝ(½ + iτ)|` para `0 ≤ ε ≤ ½`, por Stirling complexo (§4as) em `|τ| ≥ 4`
   (com constante `e^{17/2}`) e compacidade em `|τ| ≤ 4`;
3. **a razão** (`razao_zeta`): de `ξ = s(s − 1)/2 · Γℝ · ζ`, sob RH,
   `|ζ(½ + iτ)| ≤ K (1 + |τ|)^{1/4} |ζ(½ + ε + iτ)|`, uniformemente em `0 < ε < ½`;
4. **convergência dominada** (`cota_erro`, `integrable_dom`, `ae_zeta_ne_zero`, `tendsto_erro`): o integrando é
   `≤ 16(1 + K²)(1 + |τ|)^{−3/2}`, integrável. Fora dos zeros de `ζ` na linha crítica ele tende a `0`, e esses
   zeros são enumeráveis (finitos em cada janela, `zerosSim_finito`).

Daí **`necessidade_iff_entrada`**: `FechamentoO1.NecessidadeRH ⟺ (RH ⇒ ∀ᶠ ε → 0⁺, EntradaLittlewood ε)`. Para a
estrutura nomeada falta só a convergência dominada das somas parciais de corte abrupto
`Σ_{n ≤ N} μ(n) n^{−½−ε−iτ}` (o teorema de Littlewood de 1912), isto é, a fórmula de Perron truncada e a cota de
Littlewood para `1/ζ` (§4ar) num deslocamento de contorno.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `J(ε) → 0` sob RH (segunda prova; a primeira é `ATK.NecessidadeRH.tendsto_J_RH`) | CERTIFIED | ferramenta |
| razão `ζ(½ + iτ)/ζ(½ + ε + iτ) = O(\|τ\|^{1/4})` sob RH, uniforme em `ε` | CERTIFIED | ferramenta |
| `RH ⟺ D_N → 0` (`ATK.NecessidadeRH.rh_iff_DN`, 2026-10-15) | CERTIFIED (anterior) | reformulação |
| `EntradaLittlewood ε` sob RH, `ε` pequeno (corte abrupto) | BUILD_PENDING (Perron truncada) | — |
| a estrutura nomeada `FechamentoO1.NecessidadeRH` | BUILD_PENDING (só a entrada acima) | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/jsobrh.py`, `dados/jsobrh.json`, `testes/test_jsobrh.py`, 2 testes). `J(ε)` truncada em
`|τ| ≤ 120` vale `2,27; 0,72; 0,21; 0,058; 0,011; 0,0031` para `ε = 0,4; 0,2; 0,1; 0,05; 0,02; 0,01`, caindo como
`≈ ε²`. A razão `|Γ(¼ + h + iy)|/(|Γ(¼ + iy)|(1 + |y|)^{1/4})` fica `≤ 1` na grade (a prova usa `e^{17/2}`). A
razão `|ζ(½ + iτ)|/(|ζ(½ + ε + iτ)|(1 + |τ|)^{1/4})` fica `≤ 0,87` para `τ ≤ 200`. A monotonia
`|ξ(½ + iτ)| ≤ |ξ(½ + ε + iτ)|` vale nos 903 pontos da grade.

## 4ax. A fórmula de Perron truncada: o núcleo (rodada 44)

Um arquivo, **10 teoremas** (total 7501), só os axiomas padrão (`ZeroClasses/Perron.lean`). A Mathlib não tem a fórmula
de Perron. O núcleo é

  `perron(L, c, T) = (1/2π) ∫_{−T}^{T} e^{(c+it)L}/(c + it) dt = (1/2πi) ∫_{c−iT}^{c+iT} y^z/z dz`, `y = e^L`.

* **`perron_pos`**: para `L > 0` (`y > 1`), `‖perron(L, c, T) − 1‖ ≤ e^{cL}/(πTL)`;
* **`perron_neg`**: para `L < 0` (`y < 1`), `‖perron(L, c, T)‖ ≤ e^{cL}/(πT|L|)`;
* **`perron_degrau`**: as duas juntas, `‖perron(L, c, T) − 1_{L>0}‖ ≤ e^{cL}/(πT|L|)` para `L ≠ 0`.

A prova desloca o segmento vertical com os retângulos da rodada 40. Para `y > 1`, até `Re z = −U`: o resíduo em
`z = 0` sai de `e^{zL}/z = dslope(e^{·L}, 0) + 1/z`, com `bordo_cauchy` para a parte inteira e `bordo_inv` para `1/z`.
Para `y < 1`, até `Re z = U`, sem polos. Os dois lados horizontais custam `≤ e^{cL}/(|L|T)` cada (`horiz`), o vertical
deslocado `≤ 2T/U` (`vert`), e `limite` faz `U → ∞`. `alg_esq` e `alg_dir` são a álgebra das quatro integrais.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Perron truncada para o degrau, com erro `e^{cL}/(πT\|L\|)` | CERTIFIED | ferramenta |
| Perron truncada para séries de Dirichlet | BUILD_PENDING (próxima rodada) | — |
| `EntradaLittlewood` sob RH (corte abrupto); a estrutura nomeada `FechamentoO1.NecessidadeRH` | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/perron.py`, `dados/perron.json`, `testes/test_perron.py`, 2 testes). Simpson em 36 pontos
`L ∈ {±2, ±0,5, ±0,1}`, `c ∈ {0,3; 1}`, `T ∈ {5, 20, 60}`. O maior erro/cota é `0,91`, de modo que a cota é quase
justa. Em `L = 0`, fora da cota, o núcleo tende a `½` (`0,437; 0,484; 0,495`).

## 4ay. Perron truncada para séries de Dirichlet (rodada 45)

Um arquivo, **11 teoremas** (total 7512), só os axiomas padrão (`ZeroClasses/PerronDirichlet.lean`). Para coeficientes
`|f(n)| ≤ 1`, `x = N + ½`, `c > 0`, `σ + c > 1` (`σ = Re s`) e `T > 0`, **`perron_LSeries`**:

  `|Σ_{n ≤ N} f(n) n^{−s} − (1/2π) ∫_{−T}^{T} F(s + c + it) x^{c+it}/(c + it) dt| ≤ x^c (4x + 2) ζ(σ + c)/(πT)`,

com `F = LSeries f` e `ζ(σ + c)` escrita como `Σ_n n^{−σ−c}`.

* `termo`: `f(n) n^{−s} e^{z log(x/n)} = f(n) n^{−(s+z)} x^z`;
* **`soma_perron`**: `Σ_n f(n) n^{−s} perron(log(x/n), c, T) = (1/2π) ∫ F(s + c + it) x^{c+it}/(c + it) dt`, trocando
  soma e integral por convergência dominada (`|f(n) n^{−s−z} x^z/z| ≤ n^{−σ−c} x^c/c`);
* `abs_log_ge`: `|log(x/n)| ≥ 1/(4x + 2)` para `n ≥ 1`, porque `x` é meio-inteiro;
* o degrau da rodada 44 em cada `n`, somado com pesos `n^{−σ}(x/n)^c`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Perron truncada para séries de Dirichlet com coeficientes limitados | CERTIFIED | ferramenta |
| deslocamento para `Re = ½ + ε/2` com `1/ζ` sob RH; `EntradaLittlewood` | BUILD_PENDING (próxima rodada) | — |
| a estrutura nomeada `FechamentoO1.NecessidadeRH` (corte abrupto; `RH ⟺ D_N → 0` já é `ATK.NecessidadeRH.rh_iff_DN`) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/perron_dirichlet.py`, `dados/perron_dirichlet.json`, `testes/test_perron_dirichlet.py`, 2 testes).
Com `f = μ`, `s = 0,8 + 5i`, `c = ½`: o erro é `0,041` e `0,016` (`N = 10`, `T = 20` e `50`) e `0,029` e `0,0051`
(`N = 30`), muito abaixo da cota (`3,6` a `43`). `min_n |log(x/n)|·(4x + 2) = 2,0` para `N < 60`.

## 4az. O teorema de Littlewood para `Σ μ(n) n^{−s}` e `NecessidadeRH` (rodada 46)

Um arquivo, **21 teoremas** (total 7533), só os axiomas padrão (`ZeroClasses/LittlewoodMu.lean`).

**`cota_PN`** (Littlewood, 1912, com taxa): sob RH, para `Re w = ½ + ε` com `0 < ε ≤ 1` e `N ≥ 1`,

  `|Σ_{n ≤ N} μ(n) n^{−w} − F(w)| ≤ K (1 + |Im w|)^{ε/16} (N + ½)^{−ε/4}`,

com `F(w) = (w − 1)/ζ₁(w) = 1/ζ(w)` (`ATK.RHLogZeta.F`) e `K` dependendo só de `ε`. Daí **`littlewood`**: sob RH,
`Σ_{n ≤ N} μ(n) n^{−w} → 1/ζ(w)` para `½ < Re w ≤ 3/2`. A Mathlib não tem o teorema.

1. **Perron** (§4ay) com `f = μ`, `c = ½`, `T = x²`, `x = N + ½`: a soma parcial é
   `(1/2π) ∫_{−T}^{T} x^{½+it} F(w + ½ + it)/(½ + it) dt` a menos de `x^{½}(4x + 2)ζ(1 + ε)/(πT)` (`LSeries_mu`);
2. **o resíduo** (`bordo_g`): sob RH, `G(z) = x^z F(w + z)` é holomorfa em `Re(w + z) > ½`, e
   `∮ G(z)/z dz = 2πi F(w)` no retângulo `[−ε/2, ½] × [−T, T]` (`dslope` + `bordo_inv`);
3. **os três lados** (`horiz_g`, `vert_g`), com `|F(s)| ≤ C(1 + |Im s|)^{ε/16}` em `Re s ≥ ½ + ε/2`
   (`ATK.RHLogZeta.norm_F_le`): os horizontais custam `x^{½} C (1 + |Im w|)^η (1 + T)^η/T`; o vertical em
   `Re z = −ε/2` custa `x^{−ε/2} C (1 + |Im w|)^η (1 + 2/ε)(1 + T)^{2η} ∫ (1 + |y|)^{−1−η}`;
4. **as potências** (`rpow_mul_le`, `rpow_div_le`, `um_add_sq_rpow_le`): os três erros são `O(x^{−ε/4})`.

Consequências:

* **`entradaLittlewood`**: sob RH, `ATK.NecessidadeBD.EntradaLittlewood ε` para `0 < ε ≤ ¼` (mollificador de corte
  abrupto `μ(n) n^{−ε}`), com a dominação `16(1 + M²)(1 + |τ|)^{−5/4}` vinda da razão `ζ(s)/ζ(s + ε)` (§4aw) e de
  Lindelöf à direita da reta (`ATK.RHLogZeta.norm_zeta_le_RH`);
* **`entradas`**: sob RH, `EntradasNecessidade`;
* **`necessidadeRH : ATK.FechamentoO1.NecessidadeRH`**: a estrutura nomeada é um teorema;
* **`rh_iff_DN_classico`**: `RH ⟺ D_N → 0` pelo caminho clássico. A primeira prova (`ATK.NecessidadeRH.rh_iff_DN`,
  2026-10-15) usa o mollificador suavizado; as duas são independentes.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Littlewood: sob RH, `Σ_{n≤N} μ(n) n^{−w} → 1/ζ(w)` em `½ < Re w ≤ 3/2`, com taxa `N^{−ε/4}` | CERTIFIED | consequência |
| `EntradaLittlewood ε` sob RH (`0 < ε ≤ ¼`) | CERTIFIED | consequência |
| `ATK.FechamentoO1.NecessidadeRH` | CERTIFIED | fecha a estrutura nomeada |
| `RH ⟺ D_N → 0` (segunda prova, clássica) | CERTIFIED | reformulação |
| `CrescimentoN` (zeros distintos, B10) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

`NecessidadeRH` fecha a **necessidade** do critério (RH ⇒ `D_N → 0`). O critério é uma equivalência e não prova RH.

Numérico (`codigo/littlewood_mu.py`, `dados/littlewood_mu.json`, `testes/test_littlewood_mu.py`, 2 testes). Em
`w = 0,8 + 5i`, `0,7 + 14i` e `0,6 + 3i`, o erro `|Σ_{n≤N} μ(n)n^{−w} − 1/ζ(w)|` cai de `N = 10` a `N = 10⁵`
(`0,15 → 0,0057`, `3,3 → 0,53`, `0,23 → 0,051`). O quociente pela taxa `(N + ½)^{−ε/4}` fica `≤ 3,8`. O erro
espectral com `ε = 0,2`, `N = 2000`, vezes `(1 + |τ|)^{5/4}`, fica `≤ 1,1` em `τ = 0, 5, 20, 50`.

## 4ba. Hardy, parte 1: a teta na cúspide `y = i` (rodada 47)

Um arquivo, **12 teoremas** (total 7545), só os axiomas padrão (`ZeroClasses/HardyCuspide.lean`). O alvo R4 do programa
(`ATK.AtaqueRH.Hardy`: infinitos zeros na reta crítica, Hardy 1914) não está provado, nem na Mathlib. A rota clássica
(Titchmarsh §10.2) usa os momentos `∫ Ξ(t)/(t² + ¼) t^{2n} cosh(αt) dt = (−1)^n (π/2) H^{(2n)}(iα)`, com
`H(u) = 2 cosh(u/2) − e^{u/2} θ(e^{2u})`, e o fato de que a parte com `θ` e **todas** as suas derivadas se anulam quando
`α → π/4⁻`. Esta rodada prova esse fato.

* `th y = θ₂(0, iy) = Σ_{n ∈ ℤ} e^{−πn²y}`; **`th_cusp_eq`**: `θ(i + η) = θ₂(½, iη)`, porque `n(n + 1)` é par;
* **`norm_th_cusp`**: pela equação funcional de Jacobi da Mathlib, para `Re η > 0` e `Re(1/η) ≥ 1`,
  `|θ(i + η)| ≤ K₀ |η|^{−1/2} e^{−(π/4) Re(1/η)}`, `K₀ = Σ_{n∈ℤ} e^{−π(n² − |n|)}` (`norm_theta2_le`);
* `Th u = e^{u/2} θ(e^{2u})`, holomorfa em `|Im u| < π/4` (`re_exp_two_pos`, `th_diff`, `Th_diff`);
* `geometria`: para `α = π/4 − 2r`, `r ≤ 1/250` e `|u − iα| ≤ r`, `η = e^{2u} − i` tem `Re η ≥ 2r/π` e
  `|η| ≤ 12r`, logo `Re(1/η) ≥ 1/(72πr)`;
* **`norm_Th_cusp`**: nesse círculo, `|Θ(u)| ≤ 2K₀ (2r/π)^{−1/2} e^{−1/(288 r)}`;
* **`norm_iteratedDeriv_Th_le`** (estimativa de Cauchy da Mathlib) e **`iteratedDeriv_Th_tendsto`**: para todo
  `k`, `Θ^{(k)}(i(π/4 − 2r)) → 0` quando `r → 0⁺`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| a teta e todas as derivadas de `Θ` se anulam na cúspide | CERTIFIED | ferramenta |
| `Ξ(t)/(t² + ¼) = ∫₀^∞ H(u) cos(tu) du` e o decaimento de `Ξ` | CERTIFIED na rodada 48 (§4bb) | ferramenta |
| a identidade dos momentos e Hardy (`ATK.AtaqueRH.Hardy`) | CERTIFIED nas rodadas 49–50 (§4bc–§4bd) | ferramenta; consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/hardy_cuspide.py`, `dados/hardy_cuspide.json`, `testes/test_hardy_cuspide.py`, 2 testes).
`K₀ = 3,0037`. Em cinco pontos com `Re(1/η)` entre `1,5` e `15`, `|θ(i + η)|` fica em `≈ 2/3` da cota (a constante
verdadeira é `2`, não `K₀`). `|Θ(i(π/4 − 2r))|` cai de `0,31` (`r = 0,08`) a `3,9·10⁻⁴` (`r = 0,02`), e `|Θ′|` de
`3,8` a `0,09`. Em `r ≤ 1/250` os valores ficam abaixo da precisão da máquina; a cota da prova vai de `50`
(`r = 0,004`) a `0,32` (`r = 0,0005`).

## 4bb. Hardy, parte 2: a representação de Fourier de `Ξ` e o decaimento (rodada 48)

Um arquivo, **22 teoremas** (total 7567), só os axiomas padrão (`ZeroClasses/HardyFourier.lean`). Liga a teta da Mathlib
(rodada 47) à fórmula de Riemann já certificada (`ATK.BaseRiemannTeta.Xi_riemann`) e dá as duas entradas analíticas da
identidade dos momentos de Hardy.

* **`th_ofReal`**: `θ(ix) = 1 + 2ψ(x)`, com `ψ(x) = Σ_{n≥1} e^{−πn²x}` de `ATK.BaseRiemannTeta`; `continuousAt_psi`;
* **`psi_inv`**: a equação funcional real `1 + 2ψ(1/x) = x^{1/2}(1 + 2ψ(x))` (`evenKernel_functional_equation` da
  Mathlib); `psi_le`: `ψ(y) ≤ 2e^{−πy}` para `y ≥ 1` (comparação com a série geométrica);
* `Hr u = e^{−u/2} − 2e^{u/2}ψ(e^{2u})`; **`Hr_eq`**: `Hr = 2 cosh(u/2) − Θ(u)` (o `Θ` da rodada 47); **`Hr_neg`**:
  `Hr` é par; `continuous_Hr`; **`abs_Hr_le`**: `|Hr(u)| ≤ 5e^{−|u|/2}`;
* `integral_exp_cos`: `∫₀^∞ e^{−u/2} cos(tu) du = (1/2)/(t² + 1/4)` (`integral_exp_mul_complex_Ioi`);
  `integral_psi_exp`: a troca `x = e^{2u}` na fórmula de Riemann;
* **`Fx_eq`** (Titchmarsh (2.16.1)): `Ξ(t)/(t² + 1/4) = ∫₀^∞ Hr(u) cos(tu) du`;
* `norm_Gamma_quarto`: `|Γ(1/4 + iτ)| ≤ 8CΓ(1 + 2|τ|)e^{−π|τ|/2}` (Stirling vertical de `ATK.GammaVertical` em
  `Γ(w + 1) = wΓ(w)`); **`abs_Xi_le`**: `|Ξ(t)| ≤ 24CΓ(1 + |t|)⁴e^{−π|t|/4}` (com `|ζ(s)| ≤ ½ + 1/|s − 1| + 6|s|`);
  `abs_Fx_le`, `Fx_neg`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `Ξ(t)/(t² + ¼) = ∫₀^∞ H(u) cos(tu) du`, `H` par, `\|H(u)\| ≤ 5e^{−\|u\|/2}` | CERTIFIED | ferramenta |
| `\|Ξ(t)\| ≤ 24CΓ(1 + \|t\|)⁴e^{−π\|t\|/4}` | CERTIFIED | ferramenta |
| inversão de Fourier, continuação à faixa `\|Im x\| < π/4` e a identidade dos momentos | CERTIFIED na rodada 49 (§4bc) | ferramenta |
| Hardy (`ATK.AtaqueRH.Hardy`) | CERTIFIED na rodada 50 (§4bd) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/hardy_fourier.py`, `dados/hardy_fourier.json`, `testes/test_hardy_fourier.py`, 2 testes).
`Hr(−u) = Hr(u)` até `10⁻¹⁵` em cinco pontos; `|Hr(u)|` fica em `≈ 1/5` da cota. Por Simpson em `[0, 80]`,
`(1/4)∫₀^∞ Hr = 0,49712077818826`, contra `ξ(1/2) = 0,49712077818831`; `(t² + 1/4)∫₀^∞ Hr(u) cos(tu) du` vale
`+7,1·10⁻⁵` em `t₁ − 0,05` e `−6,7·10⁻⁵` em `t₁ + 0,05` (`t₁ = 14,1347…`, o primeiro zero). A cota de decaimento é
folgada: em `t = 30`, `|Ξ| = 1,5·10⁻⁸` contra `0,15`.

Também nesta rodada: `testes/test_rvm.py` perde um `import math` sem uso (apontado pela revisão automática do #117).

## 4bc. Hardy, parte 3: inversão de Fourier, continuação e a identidade dos momentos (rodada 49)

Um arquivo, **27 teoremas** (total 7594), só os axiomas padrão (`ZeroClasses/HardyMomentos.lean`). Sobre a
representação de Fourier e o decaimento da rodada 48 e a cúspide da rodada 47, prova a identidade dos momentos de
Hardy (Titchmarsh §10.2).

* funções pares na reta: `integrable_of_even`, `integral_of_even`, `integral_exp_of_even`
  (`∫ e^{iav}g(v)dv = 2∫₀^∞ g(v)cos(av)dv`);
* `integrableOn_dom`: `|Fx(t)| t^m e^{βt}` é integrável em `(0, ∞)` para `β < π/4` (do decaimento de `Ξ`);
  `integrable_Hr`, `fourier_Hr` (`𝓕Hr(w) = 2Fx(2πw)`);
* **`integral_Fx_cos`** — inversão de Fourier (`Continuous.fourierInv_fourier_eq` da Mathlib):
  `∫₀^∞ Fx(t) cos(xt) dt = (π/2) Hr(x)` para `x` real;
* a faixa `|Im z| < π/4` (`faixa`, aberta e convexa); `Gc n z = ∫₀^∞ Fx(t) t^{2n} cos(zt) dt` e
  `Sc n z = ∫₀^∞ Fx(t) t^{2n+1} sin(zt) dt`, com `hasDerivAt_Gc` (`Gc′ = −Sc`) e `hasDerivAt_Sc` (`Sc′ = Gc_{n+1}`)
  por derivação sob a integral (`hasDerivAt_trig`);
* **`Gc_zero_eq`**: `Gc 0 = (π/2)(2cosh(z/2) − Θ(z))` na faixa — princípio da identidade da Mathlib a partir da
  igualdade na reta real;
* **`Gc_eq`**: `Gc n z = (−1)^n (π/2)(2·4^{−n}cosh(z/2) − Θ^{(2n)}(z))` na faixa (indução);
* **`momento`**: para `|α| < π/4`,
  `∫₀^∞ Fx(t) t^{2n} cosh(αt) dt = (−1)^n (π/2)(2·4^{−n} cos(α/2) − Re Θ^{(2n)}(iα))`;
* **`momento_tendsto`**: quando `α = π/4 − 2r → π/4⁻`, o momento tende a `(−1)^n π 4^{−n} cos(π/8)`
  (`iteratedDeriv_Th_tendsto`, rodada 47).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| inversão de Fourier `∫₀^∞ Fx(t)cos(xt)dt = (π/2)Hr(x)` | CERTIFIED | ferramenta |
| a identidade dos momentos e o seu limite na cúspide | CERTIFIED | ferramenta |
| Hardy (`ATK.AtaqueRH.Hardy`) | CERTIFIED na rodada 50 (§4bd) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/hardy_momentos.py`, `dados/hardy_momentos.json`, `testes/test_hardy_momentos.py`, 2 testes), com
`Ξ` calculada por Lanczos e Euler–Maclaurin (`encontro.py`), independente da fórmula da rodada 48. Por Simpson em
`[0, 60]`, `∫₀^∞ Fx(t)cos(xt)dt` e `(π/2)Hr(x)` coincidem até `10⁻¹⁵` em `x = 0; 0,5; 1; 2`. Os momentos com
`n = 0, 1` e `α = 0,2; 0,3; 0,4` coincidem com a fórmula até `2·10⁻⁸` em termos relativos (o resto é o corte em
`t = 60`). O lado direito para `n = 1` oscila antes de assentar (`17,8; −11,2; −96,3; −1,54; −0,727; −0,7264` em
`α = 0,5; 0,65; 0,72; 0,76; 0,775; 0,78`), contra o limite `−π cos(π/8)/4 = −0,7256`.

## 4bd. O teorema de Hardy: infinitos zeros de `ζ` na reta crítica (rodada 50)

Um arquivo, **6 teoremas** (total 7600), só os axiomas padrão (`ZeroClasses/HardyTeorema.lean`). Fecha o alvo R4 do
programa: **`ATK.ZeroClasses.Hardy.hardy : ATK.AtaqueRH.Hardy`**, isto é, o conjunto
`{t > 0 : ζ(1/2 + it) = 0}` é infinito (Hardy, 1914). O teorema não está na Mathlib fixada no `lake-manifest.json` (busca no código-fonte). O argumento é
o de Titchmarsh §10.2, sobre a identidade dos momentos da rodada 49:

* `existe_Xi_ne_zero`: `Ξ` não se anula identicamente em nenhuma semirreta (princípio da identidade para `ξ`,
  inteira, com `ξ(0) = 1/2`);
* `sinal_constante`: sem trocas de sinal depois de `T`, `Ξ` tem sinal constante `σ = ±1` em `[T, ∞)`;
* **`sem_sinal_constante`**: isso é impossível. Toma-se `t₀ ≥ 2T` com `Ξ(t₀) ≠ 0` e um intervalo `[t₀, t₀ + δ]` onde
  `σFx ≥ c > 0`; para `0 < α < π/4`,
  `σ∫₀^∞ Fx(t) t^{2n} cosh(αt) dt ≥ t₀^{2n} cδ − T^{2n} A`, `A = ∫_{(0,T]} |Fx| cosh(πt/4)`.
  Quando `α → π/4⁻`, o lado esquerdo tende a `σ(−1)^n π 4^{−n} cos(π/8)` (`momento_tendsto`), negativo para `n` da
  paridade certa; e `t₀^{2n} cδ − T^{2n}A ≥ T^{2n}(4^n cδ − A) > 0` para `n` grande;
* **`trocasInfinitas`**: `ATK.AtaqueRH.TrocasInfinitas`; **`hardy`** (por `hardy_of_trocas`, rodada antiga);
  **`existe_zero_acima`**: para todo `T` há `t > T` com `ζ(1/2 + it) = 0`.

O projeto Hardy ocupou as rodadas 47–50 (§4ba–§4bd, `HardyCuspide`, `HardyFourier`, `HardyMomentos`,
`HardyTeorema`, 67 teoremas).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Hardy (1914): infinitos zeros de `ζ` na reta crítica (`ATK.AtaqueRH.Hardy`) | CERTIFIED | consequência (teorema clássico, incondicional) |
| zeros na reta com altura arbitrariamente grande | CERTIFIED | consequência |
| uma proporção positiva dos zeros na reta (Selberg, Levinson); `N₀(T) ≫ T` (Hardy–Littlewood) | BUILD_PENDING | — |
| todos os zeros na reta (RH) | OPEN_MATH | — |

Hardy **não** é RH nem a aproxima no sentido quantitativo: dá infinitos zeros na reta, sem dizer nada sobre os zeros
fora dela. Numérico (`codigo/hardy_teorema.py`, `dados/hardy_teorema.json`, `testes/test_hardy_teorema.py`,
2 testes): numa malha de passo `0,01`, `Ξ` troca de sinal **10** vezes em `(0, 50]` e **29** em `(0, 100]`, o valor de
`N(100)` (o termo principal de Riemann–von Mangoldt dá `29,002`); as dez primeiras trocas ficam a menos de `0,005` de
`γ₁, …, γ₁₀`.

## 4be. O critério de Littlewood: `RH ⟺ M(x) = O(x^{1/2 + ε})` (rodada 51)

Um arquivo, **12 teoremas** (total 7612), só os axiomas padrão (`ZeroClasses/MertensRH.lean`). Com
`M(N) = Σ_{n ≤ N} μ(n)` (a função de Mertens) e `MertensFraco := ∀ ε > 0, ∃ C, ∀ N, |M(N)| ≤ C(N + 1)^{1/2 + ε}`:

* **`rh_iff_mertens : RiemannHypothesis ↔ MertensFraco`** (Littlewood 1912; Titchmarsh §14.25);
* `abel`: somação por partes finita;
* **`mertens_of_RH`** (⇒): sob RH, `Σ_{n ≤ N} μ(n)n^{−w}` converge em `w = ½ + ε` (o teorema de Littlewood da
  rodada 46, §4az), logo é limitada por `B`; por partes, `|M(N)| ≤ 2B N^{1/2 + ε}`;
* **`RH_of_mertens`** (⇐): `norm_cpow_sub_le` (`|a^{−z} − (a + 1)^{−z}| ≤ |z| a^{−Re z − 1}`, valor médio),
  `G(z) = Σ_{n ≥ 0} M(n + 1)((n + 1)^{−z} − (n + 2)^{−z})` normalmente convergente em compactos de `Re z > θ`
  (`summable_gM`) e holomorfa lá (`differentiableAt_G`, Weierstrass da Mathlib); em `Re z > 1`,
  `G = Σ μ(n)n^{−z} = 1/ζ` (`G_eq_LSeries`); pelo princípio da identidade, `ζ₁(z)G(z) = z − 1` em `Re z > θ`, e `ζ`
  não se anula lá.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `RH ⟺ M(x) = O(x^{1/2 + ε})` para todo `ε > 0` | CERTIFIED | reformulação |
| `M(x) = O(x^{1/2 + ε})` | OPEN_MATH (é RH) | — |
| a conjectura de Mertens `\|M(x)\| < √x` | falsa (Odlyzko–te Riele, 1985); não formalizada | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/mertens_rh.py`, `dados/mertens_rh.json`, `testes/test_mertens_rh.py`, 2 testes). Por crivo até
`2·10⁵`: `M(10⁴) = −23`, `M(10⁵) = −48`; o máximo de `|M(N)|/√N` cai de `0,47` (`10³ < N ≤ 10⁴`) para `0,38`
(`10⁵ < N ≤ 2·10⁵`) — dado finito, sem valor de prova. A série por partes dá `G(2) = 0,60792710` contra
`6/π² = 0,60792710`, e a identidade de `abel` confere em `s = 0,75`, `N = 10⁴`.

## 4bf. `ζ′/ζ = O(log² t)` na região livre de zeros (rodada 52)

Um arquivo, **5 teoremas** (total 7617), só os axiomas padrão (`ZeroClasses/LogDerivZeta.lean`). Primeira peça do
teorema dos números primos com o erro de de la Vallée Poussin, `ψ(x) = x + O(x e^{−c√log x})` — o TNP não está na
Mathlib fixada.

* **`landau_fora`**: o lema de Landau da rodada 36 **fora do centro e com contagem**. Se `f` é analítica em
  `‖z − z₀‖ ≤ R`, `f(z₀) ≠ 0` e `‖f‖ ≤ M‖f(z₀)‖`, os zeros `S` em `‖z − z₀‖ ≤ R/4` satisfazem `(Σ m_ρ) log 2 ≤ log M`
  (módulo máximo de `f/Q` no círculo `3R/4`) e, para `‖z − z₀‖ ≤ R/16` com `f(z) ≠ 0`,
  `‖f′/f(z) − Σ_{ρ∈S} m_ρ/(z − ρ)‖ ≤ 32(log M + 1)/R` (Borel–Carathéodory no disco `R/8`, Cauchy no círculo
  `R/16` em volta de `z`);
* `zeta_disco`, **`zeta_local_fora`**: a aplicação a `ζ` com centro `σ + it`, `1 < σ ≤ 2`, `|t| ≥ 2`;
* `norm_logDeriv_le`: `|ζ′/ζ(σ + it)| ≤ −ζ′/ζ(σ)` em `σ > 1` (série de von Mangoldt da Mathlib);
* **`logDeriv_zeta_le`**: existem `c > 0`, `T₁ ≥ 2` e `C ≥ 0` com `ζ(σ + it) ≠ 0` e `|ζ′/ζ(σ + it)| ≤ C log²|t|` para
  `|t| ≥ T₁` e `1 − c/log|t| ≤ σ ≤ 2`. Centro `σ₀ = 1 + 1/log|t|`; os zeros a distância `≤ 1/8` têm
  `β ≤ 1 − c₀/(2 log|t|)` pela região livre (§4aq), logo cada termo de Landau é `≤ 4 log|t|/c₀`, e há `O(log|t|)` deles.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Landau fora do centro, com contagem de zeros | CERTIFIED | ferramenta |
| `\|ζ′/ζ(σ + it)\| ≤ C log²\|t\|` em `σ ≥ 1 − c/log\|t\|` | CERTIFIED | ferramenta |
| Perron suavizado para `Λ` e o deslocamento até a região livre | CERTIFIED na rodada 53 (§4bg) | ferramenta |
| RH | OPEN_MATH | — |

Numérico (`codigo/logderiv_zeta.py`, `dados/logderiv_zeta.json`, `testes/test_logderiv_zeta.py`, 2 testes). Com `ζ`
por Euler–Maclaurin e `ζ′` por diferença central: `|ζ′/ζ(σ + it)|/log²t` fica abaixo de `0,036` para
`t = 10, 100, 1000` e `σ` entre `1 − 0,05/log t` e `2`; `|ζ′/ζ(σ + it)| ≤ −ζ′/ζ(σ)` em `σ = 1,1; 1,5; 2`, com
`−ζ′/ζ(2) = 0,5699610`.

## 4bg. A soma de Chebyshev suavizada com o erro de de la Vallée Poussin (rodada 53)

Um arquivo, **18 teoremas** (total 7635), só os axiomas padrão (`ZeroClasses/ChebyshevSuave.lean`). Segunda peça do
TNP com erro:

  `|Σ_{n ≤ x} Λ(n)(1 − n/x) − x/2| ≤ K x log x · e^{−a√log x}`   para `x ≥ x₀`   (**`chebyshev_suave`**).

* **Perron suavizado em `Re s = c`** (`perron_kk_c`, inversão de Mellin da Mathlib para `k(u) = (1 − u)₊` com
  `K(s) = 1/(s(s + 1))`), e daí **`Ssm_eq_integral`**: `Σ_{n ≤ x} Λ(n)(1 − n/x) = (1/2π)∫ x^{c+iy}L(Λ, c + iy)K(c + iy) dy`
  para `c > 1` (troca soma–integral como em `ATK.PerronSuave.AN_eq_integral`);
* `logDeriv_eq_Gp`: `ζ′/ζ = G′/G − 1/(s − 1)` com `G(s) = (s − 1)ζ(s)`; `zeros_compacto`; **`regiao_contorno`**:
  `ζ ≠ 0` e `|ζ′/ζ(s) + 1/(s − 1)| ≤ C log²T` em `1 − c₁/log T ≤ Re s ≤ 2`, `|Im s| ≤ T` (rodada 52 mais compacidade);
* **`bordo_fx`**: no retângulo `[1 − c₁/log T, c] × [−T, T]`, `∮ x^s(−ζ′/ζ)(s)K(s) ds = πi x` (resíduo `x·K(1) = x/2`,
  pela técnica `dslope` da rodada 46 e o princípio do argumento da rodada 40);
* `cauda` (`‖∫_ℝ f − ∫_{−T}^{T} f‖ ≤ 2B/T` se `|f(y)| ≤ B/(1 + y²)`, via `arctan`), `norm_KK_um`, `norm_logDeriv_c`,
  `continuous_logDeriv_c` e **`erro_explicito`**: o erro em função de `x`, `c`, `T`;
* **`chebyshev_suave`**: `c = 1 + 1/log x` e `T = e^{√log x}` (então `x^c = e·x` e `x^{1 − c₁/log T} = x e^{−c₁√log x}`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `Σ_{n ≤ x} Λ(n)(1 − n/x) = x/2 + O(x log x · e^{−a√log x})` | CERTIFIED | ferramenta |
| `ψ(x) = x + O(x e^{−b√log x})` (tirar a suavização) | CERTIFIED na rodada 54 (§4bh) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/chebyshev_suave.py`, `dados/chebyshev_suave.json`, `testes/test_chebyshev_suave.py`, 2 testes).
Por crivo até `10⁶`, `|Ssm(x) − x/2|/x` vale `2,1·10⁻³`, `1,7·10⁻⁴`, `3,2·10⁻⁶` e `6,1·10⁻⁶` em
`x = 10³, 10⁴, 10⁵, 10⁶` — a oscilação é a dos zeros, e a constante `a` da prova não é explícita.

## 4bh. O teorema dos números primos com o erro de de la Vallée Poussin (rodada 54)

Um arquivo, **11 teoremas** (total 7646), só os axiomas padrão (`ZeroClasses/TNP.lean`). Com `ψ`, `θ` e `π` da
Mathlib (`Chebyshev.psi`, `Chebyshev.theta`, `Nat.primeCounting`):

* **`psi_tnp`**: existem `b > 0` e `K` com `|ψ(x) − x| ≤ K x e^{−b√log x}` para `x` grande;
* **`tendsto_psi_div`**: `ψ(x)/x → 1`; **`tendsto_theta_div`**: `θ(x)/x → 1` (com `ψ − θ = O(√x)` da Mathlib);
* **`tendsto_primeCounting`**: **`π(x) log x / x → 1`** — o teorema dos números primos (Hadamard, de la Vallée Poussin,
  1896). Pela fórmula de Abel da Mathlib `π(x) = θ(x)/log x + ∫₂^x θ(t)/(t log²t) dt`, com a integral `O(√x + x/log²x)`
  (`integral_inv_log_sq_le`).

A prova tira a suavização da rodada 53: `ψ₁(y) = y·Ssm(y) = Σ_{n ≤ y} Λ(n)(y − n)` (`mul_Ssm_eq`), e a monotonia de
`ψ` dá **`incremento`**: `hψ(y) ≤ ψ₁(y + h) − ψ₁(y) ≤ hψ(y + h)`. Com `ψ₁(y) = y²/2 + O(y²η²)` uniformemente em
`[x/2, 2x]`, `η = √(2K log x)·e^{−(a/4)√log x}`, e `h = ηx`, vem `x − 2,5ηx ≤ ψ(x) ≤ x + 5,5ηx`; por fim
`t e^{−(a/4)t} ≤ (8/a) e^{−(a/8)t}` (`le_exp_mul`).

O TNP não está na Mathlib fixada. Já tinha sido formalizado em Isabelle (AFP) e em Lean fora da Mathlib (projeto
PrimeNumberTheoremAnd, de onde vêm `ψ` e `θ` da Mathlib). Aqui as constantes não são explícitas.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `ψ(x) = x + O(x e^{−b√log x})`; `ψ(x)/x → 1`; `θ(x)/x → 1` | CERTIFIED | consequência (incondicional) |
| `π(x) ~ x/log x` | CERTIFIED | consequência (incondicional) |
| constantes explícitas; `π(x) = Li(x) + O(x e^{−b√log x})` | BUILD_PENDING | — |
| `ψ(x) = x + O(x^{1/2+ε})` (equivale a RH) | OPEN_MATH | — |

Numérico (`codigo/tnp.py`, `dados/tnp.json`, `testes/test_tnp.py`, 2 testes). Por crivo até `10⁶`:
`|ψ(x) − x|/x` vale `3,3·10⁻³`, `1,3·10⁻³`, `5,2·10⁻⁴`, `4,1·10⁻⁴` em `x = 10³, …, 10⁶`; `θ(10⁶)/10⁶ = 0,99848`;
`π(10⁶) = 78498` e `π(x) log x/x` cai de `1,161` (`10³`) para `1,084` (`10⁶`), a convergência lenta esperada
(`π(x) = x/log x + x/log²x + …`). O `incremento` confere em três pontos.

## 4bi. `ψ(x) = x + O(x^θ)` ou `M(x) = O(x^θ)` ⟹ `ζ ≠ 0` em `Re s > θ` (rodada 55)

Um arquivo, **13 teoremas** (total 7659), só os axiomas padrão (`ZeroClasses/VonKoch.lean`). A metade
"aritmética ⟹ analítica" dos critérios de von Koch e de Littlewood, **com o expoente `θ` livre** (`0 ≤ θ < 1`):

* **`zeroFree_of_psi`**: se `|ψ(N) − N| ≤ C(N + 1)^θ` para todo `N`, então `ζ(s) ≠ 0` em `Re s > θ`;
* **`RH_of_psi`**: `ψ(x) = x + O(x^{1/2 + ε})` para todo `ε > 0` ⟹ RH (von Koch 1901, direção ⇐);
* **`zeroFree_of_mertens`**: o mesmo com `|M(N)| ≤ C(N + 1)^θ` — generaliza `RH_of_mertens` (§4be);
* `mertens_of_vonKoch`: a hipótese de von Koch implica a de Littlewood (passando por RH e `mertens_of_RH`).

A prova para `ψ`:

* `gA`, `GA`, `summable_gA`, **`differentiableAt_GA`**, **`GA_eq_LSeries`**: a série por partes da rodada 51 para
  qualquer sequência `A(N) = O((N + 1)^θ)` — holomorfa em `Re s > θ` e igual a `Σ c(n)n^{−s}` em `Re s > 1` quando
  `A(n + 1) = Σ_{k ≤ n} c(k + 1)`;
* `E(N) = ψ(N) − N`, `cL(n) = Λ(n) − 1`, `E_succ`, **`LSeries_cL`**: `Σ (Λ(n) − 1)n^{−s} = −ζ′/ζ(s) − ζ(s)` em `Re s > 1`;
* com `ζ₁(s) = (s − 1)ζ(s)` inteira, `(s − 1)ζ₁′ = ζ₁·(1 − ζ₁ − (s − 1)G)` vale em `Re s > 1` e, pelo princípio da
  identidade, em `Re s > θ` — uma equação diferencial linear que **não tem polo** em nenhum zero;
* **`zero_de_edo`**: se `q f′ = f P` perto de `ρ`, com `f` analítica, `P`, `q` contínuas, `q(ρ) ≠ 0` e `f(ρ) = 0`,
  então `f ≡ 0` perto de `ρ` (se `f = (s − ρ)^{m+1}g` com `g(ρ) ≠ 0`, dividir por `(s − ρ)^m` dá `q(ρ)(m + 1)g(ρ) = 0`).
  Aplicado a `ζ₁` com `q = s − 1`, um zero `ρ` em `θ < Re ρ < 1` faria `ζ₁ ≡ 0`, contra `ζ₁(2) = ζ(2) ≠ 0`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `\|ψ(N) − N\| ≤ C(N + 1)^θ` ⟹ `ζ ≠ 0` em `Re s > θ` | CERTIFIED | reformulação |
| `\|M(N)\| ≤ C(N + 1)^θ` ⟹ `ζ ≠ 0` em `Re s > θ` | CERTIFIED | reformulação |
| `ψ(x) = x + O(x^{1/2 + ε})` ⟹ RH | CERTIFIED | reformulação |
| RH ⟹ `ψ(x) = x + O(x^{1/2 + ε})` | CERTIFIED na rodada 56 (§4bj) | reformulação |
| `ψ(x) = x + O(x^{1/2 + ε})`; `ψ(x) = x + O(x^θ)` para algum `θ < 1` | OPEN_MATH | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/von_koch.py`, `dados/von_koch.json`, `testes/test_von_koch.py`, 2 testes). Com `ψ` por crivo até
`10⁶`, a série por partes dá `G(2) = −1,0749730737` contra `−ζ′/ζ(2) − ζ(2) = −1,0749730737` (diferença `3·10⁻¹¹`;
`1,5·10⁻⁸` em `s = 1,5`), e a identidade de `ζ₁` confere com resíduo `≤ 10⁻⁸` em `s = 1,5; 2; 3`. Nos dados,
`max |ψ(N) − N|/√N ≈ 0,7–0,78` por década até `10⁶`, e `|ψ(N) − N|/(√N log²N)` fica abaixo de `0,029`, dentro da cota
de Schoenfeld sob RH (`1/(8π) ≈ 0,0398`) — dado finito, sem valor de prova.

## 4bj. O critério de von Koch: `RH ⟺ ψ(x) = x + O(x^{1/2 + ε})` (rodada 56)

Um arquivo, **22 teoremas** (total 7681), só os axiomas padrão (`ZeroClasses/VonKochRH.lean`). Com a rodada 55:

* **`rh_iff_psi : RiemannHypothesis ↔ VonKochFraco`** (von Koch 1901; `VonKochFraco := ∀ ε > 0, ∃ C, ∀ N,
  |ψ(N) − N| ≤ C(N + 1)^{1/2 + ε}`);
* **`psi_of_RH`** (⇒), e **`vonKoch_iff_mertens`**: as hipóteses de von Koch e de Littlewood são equivalentes.

A prova de `psi_of_RH` segue `mertens_of_RH` (§4be) com `Λ − 1` no lugar de `μ`:

* **Littlewood geral** (`bordo_g`, `desloca`, `horiz_g`, `vert_g`, **`cota_gen`**): a estimativa da rodada 46 (§4az)
  para quaisquer coeficientes `|f(n)| ≤ 1` cuja série `L` se estende a uma `Φ` holomorfa em `Re u > ½`, com
  `|Φ(u)| ≤ C(1 + |Im u|)^{ε/16}` em `Re u ≥ ½ + ε/2`: `|Σ_{n ≤ N} f(n)n^{−w} − Φ(w)| ≤ K(1 + |Im w|)^{ε/16}(N + ½)^{−ε/4}`
  em `Re w = ½ + ε`;
* **`H = −ζ′/ζ − ζ`** (`Hf := −ζ₁′/ζ₁ − ζ₀`, `Hf_eq`, `differentiableAt_Hf`): holomorfa em `Re s > ½` sob RH (o polo
  em `s = 1` cancela); **`norm_H_le`**: `|H(s)| ≤ C(1 + |Im s|)^η` em `Re s ≥ ½ + δ`, por Cauchy no círculo de raio
  `δ/2` aplicado ao ramo de `log ζ` da rodada 45 (`ATK.RHLogZeta.norm_L_le`), mais `|ζ| ≤ e^{|log ζ|}`, Young,
  `|ζ′/ζ| ≤ A` em `Re s ≥ 2` (`norm_logDeriv_le_dois`) e compacidade;
* **normalização** (`norm_cL_le`, `fco`, `norm_fco_le`, `term_fco`, `LSeries_fco`): `|Λ(n) − 1| ≤ (1/δ + 1)n^δ`, e
  `f(n) = (Λ(n) − 1)/((1/δ + 1)n^δ)` tem série `H(u + δ)/(1/δ + 1)`;
* **`somas_limitadas`**: sob RH, `Σ_{n ≤ N} (Λ(n) − 1)n^{−σ}` é limitada para `σ = ½ + ε + δ`; **`abel_cota`**,
  **`E_eq_sum`**: por partes, `|ψ(N) − N| ≤ 2B N^σ`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `RH ⟺ ψ(x) = x + O(x^{1/2 + ε})` para todo `ε > 0` | CERTIFIED | reformulação |
| `ψ(x) = x + O(x^{1/2+ε}) ⟺ M(x) = O(x^{1/2+ε})` | CERTIFIED | reformulação |
| Littlewood para coeficientes limitados com continuação de crescimento polinomial lento | CERTIFIED | ferramenta |
| `\|ψ(x) − x\| ≤ √x log²x/(8π)` sob RH (Schoenfeld, constante explícita) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/von_koch_rh.py`, `dados/von_koch_rh.json`, `testes/test_von_koch_rh.py`, 2 testes). Com `ψ` por
crivo até `10⁶`, `S_N(0,8) = Σ_{n ≤ N} (Λ(n) − 1)n^{−0,8}` vai de `−1,298` (`N = 10²`) a `−1,186` (`N = 10⁶`), contra
`H(0,8) = −1,1794` (diferença `0,006`, oscilando); `|H(σ + it)|/(1 + t)^{0,1}` fica abaixo de `1,7` em
`σ = 0,6; 0,75; 1; 1,5` e `t = 10, 100, 1000`; `|Λ(n) − 1| ≤ (1/δ + 1)n^δ` com folga (razão máxima `0,31`);
`max_{N ≤ 10⁶} |ψ(N) − N|/(N + 1)^{1/2 + ε}` vale `0,71`, `0,68`, `0,59` para `ε = 0,05; 0,1; 0,25` — dado finito,
sem valor de prova.

## 4bk. Quasi-RH: `ζ ≠ 0` em `Re s > θ` ⟺ `ψ(x) = x + O(x^{θ+ε})` ⟺ `M(x) = O(x^{θ+ε})` (rodada 57)

Um arquivo, **27 teoremas** (total 7708), só os axiomas padrão (`ZeroClasses/QuasiRH.lean`). Com
`SemZeros θ := ∀ s, θ < Re s → ζ(s) ≠ 0` e `½ ≤ θ < 1`:

* **`semZeros_iff_psi`**: `SemZeros θ ⟺ ∀ ε > 0, |ψ(N) − N| ≤ C(N + 1)^{θ+ε}`;
* **`semZeros_iff_mertens`**: `SemZeros θ ⟺ ∀ ε > 0, |M(N)| ≤ C(N + 1)^{θ+ε}`;
* **`psi_iff_mertens`**: as duas cotas são equivalentes para cada `θ`; `semZeros_meio_iff`: `SemZeros ½ ⟺ RH`.

As direções ⇐ são `zeroFree_of_psi`/`zeroFree_of_mertens` (§4bi). As ⇒ (`psi_of_semZeros`, `mertens_of_semZeros`)
refazem as rodadas 51 e 56 com `θ` no lugar de `½`:

* o ramo de `log ζ` no disco de centro `cθ = 5/2 + θ + it` e raio `5/2` (contido em `Re s > θ`; o disco interno de
  raio `½` fica em `Re s ≥ 5/2`): `bola_props`, `norm_zeta_le_bola`, `existe_log_zeta`, `L_eq_log`, **`norm_L_le`**
  (Borel–Carathéodory e três círculos, como em `ATK.RHLogZeta`, com `SemZeros θ` no lugar de RH);
* **`norm_F_le`** (`|1/ζ| ≤ C(1 + |t|)^η`) e **`norm_H_le`** (`|ζ′/ζ + ζ| ≤ C(1 + |t|)^η`) em `Re s ≥ θ + δ`;
* **o deslocamento** (`escala`, `term_escala`, `LSeries_escala`, **`somas_limitadas_gen`**): `a(n)n^{−(θ − ½ + δ)}`
  tem série holomorfa em `Re u > ½`, e o Littlewood geral da rodada 56 (`cota_gen`) vale sem mudança;
* somação por partes (`abel_cota`, `E_eq_sum`, `M_eq_sum`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `SemZeros θ ⟺ ψ(x) = x + O(x^{θ+ε}) ⟺ M(x) = O(x^{θ+ε})`, `½ ≤ θ < 1` | CERTIFIED | reformulação |
| cotas de `1/ζ` e `ζ′/ζ` com crescimento `\|t\|^η` em `Re s ≥ θ + δ` sob `SemZeros θ` | CERTIFIED | ferramenta |
| `SemZeros θ` para algum `θ < 1` | OPEN_MATH | — |
| importar um semiplano externo (p. ex. θ = 7/8, Q1 de `fronteira/RH_frontier.md`) | BUILD_PENDING (o módulo externo não está no repositório) | — |
| RH (`SemZeros ½`) | OPEN_MATH | — |

Numérico (`codigo/quasi_rh.py`, `dados/quasi_rh.json`, `testes/test_quasi_rh.py`, 2 testes). Por crivo até `10⁶`
(`M(10⁶) = 212`): `max |ψ(N) − N|/(N + 1)^θ` vale `0,78`, `0,68`, `0,59`, `0,54` e `max |M(N)|/(N + 1)^θ` vale
`0,82`, `0,68`, `0,59`, `0,54` para `θ = 0,5; 0,6; 0,75; 0,9`; `Σ_{n ≤ N} μ(n)n^{−0,8}` vai de `−0,148` (`N = 10²`) a
`−0,2221` (`N = 10⁶`), contra `1/ζ(0,8) = −0,2254`. Dado finito, sem valor de prova: não decide `SemZeros θ`.

## 4bl. Teoremas Ω: `ψ(x) − x` e `M(x)` não são `o(√x)` (rodada 58)

Um arquivo, **23 teoremas** (total 7731), só os axiomas padrão (`ZeroClasses/OmegaPsi.lean`). Incondicionais:

* **`psi_nao_o`**: não existem, para todo `ε > 0`, constantes `C_ε` com `|ψ(N) − N| ≤ ε√(N + 1) + C_ε`;
  **`psi_nao_littleO`**: `¬ (ψ(N) − N =o[atTop] √N)` (Schmidt 1903, na forma Ω);
* **`mertens_nao_o`**, **`mertens_nao_littleO`**: o mesmo para `M(N) = Σ_{n ≤ N} μ(n)`;
* `psi_nao_O_rpow`, `mertens_nao_O_rpow`: para `θ < ½`, nem `ψ(x) − x` nem `M(x)` são `O(x^θ)`.

A prova junta o teorema de Hardy (rodada 50, `existe_zero_acima`: um zero `ρ₀ = ½ + iγ₀`) com a série por partes
`G(s) = Σ A(n + 1)((n + 1)^{−s} − (n + 2)^{−s})` da rodada 55:

* **`o_GA`**: se `A(N) = o(√N)`, então `(σ − ½)|G(σ + iγ)| → 0` quando `σ → ½⁺` (`norm_GA_le_o`, com
  `(σ − ½)ζ(σ + ½) → 1`, `tendsto_Z`, do resíduo de `ζ` em `1` da Mathlib);
* `GA_E_eq_Hf`, `GA_M_eq_F`: com `A = ψ − N` (resp. `M`) e `O(√N)`, `G = −ζ′/ζ − ζ` (resp. `1/ζ`) em `Re s > ½`
  (rodada 55 para não haver zeros em `Re s > ½`, depois o princípio da identidade);
* `fatora` (`ζ₁ = (s − ρ₀)^{m+1} g` com `g(ρ₀) ≠ 0`), **`cota_inf_H`** (`(σ − ½)|H(σ + iγ₀)| ≥ ½`, pelo polo de
  resíduo `−(m + 1)` de `−ζ′/ζ`) e **`cota_inf_F`** (`(σ − ½)|1/ζ(σ + iγ₀)| ≥ c > 0`): contradição.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `ψ(x) − x ≠ o(√x)`; `M(x) ≠ o(√x)` | CERTIFIED | consequência (incondicional) |
| `ψ(x) − x ≠ O(x^θ)`, `M(x) ≠ O(x^θ)` para `θ < ½` | CERTIFIED | consequência (incondicional) |
| `ψ(x) − x = Ω±(√x log log log x)` (Littlewood 1914); `M(x) = Ω±(√x)` | BUILD_PENDING | — |
| `limsup \|M(x)\|/√x = ∞` (conhecido: `> 1,06` por Odlyzko–te Riele 1985, `> 1,82` por Hurst 2018; ilimitado sob a independência linear das ordenadas) | OPEN_MATH | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/omega_psi.py`, `dados/omega_psi.json`, `testes/test_omega_psi.py`, 2 testes). No primeiro zero
`γ₁ = 14,1347…`: `(σ − ½)|ζ′/ζ + ζ|(σ + iγ₁)` vale `0,968`, `0,996`, `0,9996`, `0,99996` para `σ − ½ = 10⁻¹, …, 10⁻⁴`
(o resíduo `m = 1`), e `(σ − ½)|1/ζ|` tende a `1/|ζ′(ρ₁)| = 1,2608`. Por crivo até `10⁶`, o máximo por década de
`|ψ(N) − N|/√N` fica entre `0,69` e `0,78`, e o de `|M(N)|/√N` entre `0,44` e `0,83` — dado finito.

## 4bm. Báez-Duarte ponderado: `D_N(σ) → 0` ⟹ `ζ ≠ 0` em `Re s > σ` (rodada 59)

Um arquivo, **17 teoremas** (total 7748), só os axiomas padrão (`ZeroClasses/BDPonderado.lean`). Para `0 < σ < 1`,
`D_N(σ) = inf_c ∫_0^∞ (χ − Σ_{k ≤ N} c_k ρ_k)² t^{2σ−1} dt` (`DNσ`; `DNσ_meio`: `D_N(½)` é o `D_N` de Báez-Duarte):

* **`semZeros_of_DNσ`**: `inf_N D_N(σ) = 0` ⟹ `ζ ≠ 0` em `Re s > σ`;
* `psi_of_DNσ`, `mertens_of_DNσ` (`½ ≤ σ < 1`): daí `ψ(x) = x + O(x^{σ+ε})` e `M(x) = O(x^{σ+ε})` (rodada 57);
* **`piso_DNσ`**: para `0 < σ < ½`, **`inf_N D_N(σ) > 0`**, incondicionalmente (os zeros de Hardy em `Re s = ½`);
* `rh_of_DN_iInf`: a ponte B1 (`inf_N D_N = 0` ⟹ RH) como o caso `σ = ½`.

A prova é a da ponte B1 (§4, `ATK.BaezDuarteBridge`) com o peso. Num zero `σ < Re s < 1`, `∫ res(t)t^{s−1} = 1/s`;
em `(0, 1]`, `t^{Re s−1}|res| = (|res|t^{σ−½})·t^{Re s−σ−½}` e AM-GM dão `≤ (λW + 1/(2λ(Re s − σ)))/2` (`head_le`);
em `(1, ∞)`, `res = −S/t` e `S² ≤ (2 − 2σ)W` (`tail_sq_le`, `integrable_w`). Logo
`1/|s| ≤ (λW + 1/(2λ(Re s − σ)))/2 + √((2 − 2σ)W)/(1 − Re s)` (`key_ineq`), absurdo com `W` pequeno.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `inf_N D_N(σ) = 0` ⟹ `ζ ≠ 0` em `Re s > σ` (Q2(i) de `fronteira/RH_frontier.md`) | CERTIFIED | reformulação |
| `inf_N D_N(σ) > 0` para `σ < ½` | CERTIFIED | consequência (incondicional) |
| a recíproca com taxa, `Θ ≤ θ < σ` ⟹ `D_N(σ) ≪ N^{−2(σ−θ)+ε}` (Q2(ii)) | BUILD_PENDING | — |
| o piso ponderado `κ(σ) ≤ 2(σ − Θ)` (Q2(iii)) | OPEN_MATH | — |
| RH (`inf_N D_N(½) = 0`) | OPEN_MATH | — |

Numérico (`codigo/bd_ponderado.py`, `dados/bd_ponderado.json`, `testes/test_bd_ponderado.py`, 2 testes). Pela matriz
de Gram em forma fechada (com `x = 1/t`, `{x/j}{x/k}` é quadrático entre múltiplos de `j` e `k`; cauda pela média
`1/4 + mdc(j,k)²/(12jk)`): `D₁(½) = 0,8582120` e `D₂(½) = 0,2899645` (os valores de `gram2.json`), e
`D_8(σ) = 0,0428; 0,0242; 0,0140; 0,0063` para `σ = 0,4; 0,5; 0,6; 0,75`. Os dados finitos não mostram o piso de
`σ = 0,4`: ele é teorema, não observação.

## 4bn. `RH ⟺ π(x) = Li(x) + O(x^{1/2+ε})` (rodada 60)

Um arquivo, **24 teoremas** (total 7772), só os axiomas padrão (`ZeroClasses/PiLi.lean`). Com
`Li(x) = ∫_2^x dt/log t` (`Li`) e `π`, `θ` da Mathlib:

* **`rh_iff_pi`**: **`RH ⟺ ∀ ε > 0, |π(x) − Li(x)| ≤ C_ε x^{1/2+ε}`** para `x ≥ 2` (von Koch 1901, a forma mais
  citada do critério); `rh_iff_theta`: o mesmo para `θ(x) − x`;
* **`semZeros_iff_pi`**, `semZeros_iff_theta` (`½ ≤ θ < 1`): `ζ ≠ 0` em `Re s > θ` ⟺ `π(x) = Li(x) + O(x^{θ+ε})`.

A ponte com as rodadas 56–57 é somação por partes:

* `theta_of_psi`, `psi_of_theta`: com `0 ≤ ψ − θ ≤ 2√x log x` (Mathlib) e `log x ≤ x^δ/δ`, as cotas de `ψ` e de `θ`
  com expoente `b > ½` são equivalentes;
* `Li_partes`: `Li(x) = x/log x − 2/log 2 + ∫_2^x dt/log²t`; com a fórmula de Abel da Mathlib
  `π(x) = θ(x)/log x + ∫_2^x θ(t)/(t log²t) dt`, **`pi_of_theta`**: `θ − x = O(x^b)` ⟹ `π − Li = O(x^b)`;
* `Li_log_partes`: `Li(x) log x = x − 2 + ∫_2^x Li(t)/t dt`; com `θ(x) = π(x) log x − ∫_2^x π(t)/t dt` (Mathlib),
  **`theta_of_pi`**: `π − Li = O(x^b)` ⟹ `θ − x = O(x^{b'})` para todo `b' > b`;
* `erroPsi_of_int`, `int_of_erroPsi`: a forma inteira `|ψ(N) − N| ≤ C(N + 1)^b` das rodadas 55–57 e a forma real.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `RH ⟺ π(x) = Li(x) + O(x^{1/2+ε})`; `RH ⟺ θ(x) = x + O(x^{1/2+ε})` | CERTIFIED | reformulação |
| `ζ ≠ 0` em `Re s > θ` ⟺ `π(x) = Li(x) + O(x^{θ+ε})` (`½ ≤ θ < 1`) | CERTIFIED | reformulação |
| `π(x) = Li(x) + O(x e^{−b√log x})` (TNP com erro, para `π`) | BUILD_PENDING (é `pi_of_theta` com o erro da rodada 54, não montado) | — |
| `\|π(x) − li(x)\| < √x log x/(8π)` sob RH (Schoenfeld) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/pi_li.py`, `dados/pi_li.json`, `testes/test_pi_li.py`, 2 testes). `Li = li − li(2)` pela série de
Ramanujan; as duas integrações por partes conferem por Simpson a `10⁻⁹` (`x = 100`) e `6·10⁻⁵` (`x = 1000`).
Por crivo: `π(10⁶) = 78498`, `Li(10⁶) = 78626,504`, `π − Li = −8,6; −16,1; −36,8; −128,5` em `x = 10³, …, 10⁶`, e
`|π − Li|/(√x log x) ≤ 0,0392 < 1/(8π) = 0,0398` — dado finito, sem valor de prova.

## 4bo. RH ⟹ a hipótese de Lindelöf (rodada 61)

Um arquivo, **9 teoremas** (total 7781), só os axiomas padrão (`ZeroClasses/LindelofRH.lean`).

* **`lindelof_of_RH : RiemannHypothesis → Lindelof`**, com `Lindelof := ∀ ε > 0, ∃ C, ∀ t, |ζ(½ + it)| ≤ C(1 + |t|)^ε`
  — a hipótese de Lindelöf na reta crítica (a rodada 38 tinha `lindelof_fora_sob_RH`, só em `Re s ≥ ½ + δ`).

A prova (Titchmarsh §14.2), com `δ = η = ε/4`:

* na reta `Re s = ½ + δ`: `|ζ| ≤ C(1 + |t|)^η` sob RH (`ATK.RHLogZeta.norm_zeta_le_RH`);
* na reta `Re s = ½ − δ`: a equação funcional com Stirling (`ATK.GammaVertical.norm_zeta_one_sub_le`) dá
  `|ζ(1 − w)| ≤ 2C_Γ|w|^δ|ζ(w)|`, logo `|ζ| ≤ C(1 + |t|)^{δ+η}`;
* `g(s) = ζ(s)(s + 2)^{−(δ+η)}` (`gL`, `norm_gL`, `fator_le`) é limitada nas duas retas, tem crescimento polinomial
  dentro (`norm_gL_faixa`, de `ATK.ZeroClasses.VariacaoArg.cota_zeta_quarto`) e é holomorfa na faixa
  (`differentiableAt_gL`); **Phragmén–Lindelöf** da Mathlib (`PhragmenLindelof.vertical_strip`) dá `|g| ≤ C` na
  faixa, e em `s = ½ + it`, `|ζ| ≤ C|s + 2|^{ε/2} ≤ C′(1 + |t|)^ε` (`lindelof_um`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| RH ⟹ `ζ(½ + it) = O(\|t\|^ε)` (Lindelöf) | CERTIFIED | consequência de RH |
| a hipótese de Lindelöf (sem RH) | OPEN_MATH | — |
| cota de convexidade `ζ(½ + it) = O(\|t\|^{1/4+ε})`; Weyl/Bourgain `O(\|t\|^{13/84+ε})` | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/lindelof.py`, `dados/lindelof.json`, `testes/test_lindelof.py`, 2 testes). `max_{[T,2T]}|ζ(½ + it)|`
vai de `2,34` (`T = 10`) a `10,36` (`T = 640`), com expoente aparente `log M/log T ≈ 0,36–0,39` — dado finito, sem
relação com o expoente assintótico. A razão `|ζ(½ − ¼ + it)|/|ζ(½ + ¼ − it)|` bate com `(t/2π)^{1/4}` a `10⁻⁴` e fica
abaixo da cota grosseira `2C_Γ|w|^{1/4}`.

## 4bp. A abscissa de convergência de `Σ μ(n)n^{−s}` e de `Σ (Λ(n) − 1)n^{−s}` (rodada 62)

Um arquivo, **12 teoremas** (total 7793), só os axiomas padrão (`ZeroClasses/Abscissa.lean`). Para `½ ≤ θ < 1`:

* **`semZeros_iff_mu`**: `ζ ≠ 0` em `Re s > θ` ⟺ `Σ μ(n)n^{−s}` converge em todo `Re s > θ`, e então para `1/ζ(s)`
  (`tendsto_mu`);
* **`semZeros_iff_cL`**: o mesmo para `Σ (Λ(n) − 1)n^{−s}`, com limite `−ζ′/ζ(s) − ζ(s)` (`tendsto_cL`);
* **`rh_iff_mu`**, `rh_iff_cL`: **RH ⟺ `Σ μ(n)n^{−s}` converge em `Re s > ½`** (Littlewood); `mu_tendsto_inv_zeta`:
  sob RH, `Σ μ(n)n^{−s} → 1/ζ(s)` em todo `Re s > ½`, `s ≠ 1`.

Logo a abscissa de convergência das duas séries é `max(½, Θ)` com `Θ = sup Re ρ`. A ida é o Littlewood geral
(`cota_gen`, aqui `tendsto_gen`) com os coeficientes deslocados das rodadas 56–57 (`parametros` escolhe
`ε = min((Re s − θ)/2, 1)` e `d = Re s − ½ − ε`); a volta é convergência num real `σ` ⟹ somas parciais limitadas ⟹
`M(N), ψ(N) − N = O(N^σ)` por partes (`mertens_of_converge`, `psi_of_converge`) ⟹ rodada 55.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| abscissa de `Σ μ(n)n^{−s}` e de `Σ (Λ(n) − 1)n^{−s}` = `max(½, Θ)` | CERTIFIED | reformulação |
| RH ⟺ `Σ μ(n)n^{−s}` converge em `Re s > ½` | CERTIFIED | reformulação |
| convergência em `Re s = ½` (ou em `s = ½`) | OPEN_MATH | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/abscissa.py`, `dados/abscissa.json`, `testes/test_abscissa.py`, 2 testes). Até `N = 10⁶`:
`|Σ μ(n)n^{−s} − 1/ζ(s)|` cai a `0,0065` (`s = 0,75`), `0,012` (`s = 0,75 + 10i`) e `1,3·10⁻⁵` (`s = 1,2 + 3i`), e o
análogo para `Λ − 1` a `0,013`, `0,017`, `2,6·10⁻⁵` — convergência lenta, `≈ N^{−(σ−½)}`; em `s = 0,4` o máximo das
somas parciais cresce (`1,62 → 2,43`).

## 4bq. A soma sobre os zeros e `ζ′/ζ` local (rodada 63)

Um arquivo, **29 teoremas** (total 7822), só os axiomas padrão (`ZeroClasses/SomaZeros.lean`). Primeira peça da
fórmula explícita (Davenport, cap. 15), sobre Hadamard (rodada 33), Jensen local (rodada 31) e Stirling (rodada 39):

* **`soma_wz_O`**: `Σ_ρ m_ρ/(1 + (t − γ)²) = O(log(2 + |t|))` — os zeros agrupados por `⌈|γ − t|⌉ = n`, cada bloco
  contado por duas caixas de Jensen (`bloco_le`), contra a série somável `(1 + log(2 + n))/(1 + n²)`;
* **`norm_digamma_le`**: `|ψ(z)| ≤ log(2 + |Im z|) + 11` em `0 < Re z ≤ 1`, `|Im z| ≥ 3` (Cauchy no resto de
  Stirling `RS`, cuja derivada é `ψ − log + 1/(2z)`, e `ψ(z + 1) = ψ(z) + 1/z`);
* **`logDeriv_xi_sub`**: `ξ′/ξ(s) − ξ′/ξ(s₀) = Σ_ρ (1/(s − ρ) − 1/(s₀ − ρ))`;
* **`zeta_local_O`**: para `0 < σ ≤ 2`, `|t| ≥ 6`, `ζ(s) ≠ 0`: `ζ′/ζ(s) = Σ_{|γ − t| ≤ 1} 1/(s − ρ) + O(log |t|)`, com
  `O(log |t|)` termos (`card_perto_O`) — comparação com `s₀ = 2 + it`;
* **`logDeriv_RH`**: **sob RH**, `|ζ′/ζ(σ + it)| ≤ C log(2 + |t|)/(σ − ½)` em `½ < σ ≤ 2`, `|t| ≥ 6`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `Σ_ρ 1/(1 + (t − γ)²) = O(log t)` e `ζ′/ζ` local | CERTIFIED | ferramenta |
| sob RH, `ζ′/ζ(σ + it) = O(log t/(σ − ½))` | CERTIFIED | ferramenta |
| RH ⟹ `ψ(x) = x + O(√x log³ x)` (Perron + contorno em `Re s = ½ + 1/log x`) | BUILD_PENDING | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/soma_zeros.py`, `dados/soma_zeros.json`, `testes/test_soma_zeros.py`, 2 testes), com os 341 zeros
de `0 < γ ≤ 600`: `S(t)/log t` entre `0,21` e `0,35` para `t = 50…400` (esperado `≈ ½ log(t/2π)/log t`); o resto
`|ζ′/ζ(s) − Σ_{|γ−t|≤1} 1/(s − ρ)|/log t` fica entre `0,03` e `0,31`; `(σ − ½)|ζ′/ζ(σ + 100i)|/log 100` cai de
`0,072` a `0,0003` quando `σ − ½` vai de `0,5` a `0,001`.

## 4br. RH ⟺ `ψ(x) = x + O(√x log³ x)` (rodada 64)

Um arquivo, **20 teoremas** (total 7842), só os axiomas padrão (`ZeroClasses/PsiRH.lean`). A forma quantitativa do
critério de von Koch, por Perron e deslocamento de contorno (sem a fórmula explícita):

* **`psi_RH`**: sob RH, `|ψ(x) − x| ≤ K √x log³ x` para `x ≥ 100`; **`rh_iff_psiLog3`**: RH ⟺ `PsiLog3` (a volta pela
  rodada 55, via `vonKoch_of_psiLog3`, com `log³ N ≤ (3/ε)³ N^ε` e `ψ(N) ≤ N²` para os `N` pequenos);
* **Perron para `Λ`** (`perron_psi`): os coeficientes `f_η(n) = η Λ(n) n^{−η}` têm `|f_η| ≤ 1` (`norm_fL_le`), e a
  fórmula truncada da rodada 45 em `s = −η` dá `ψ(N)` contra `(1/2π) ∫_{−T}^{T} x^{c+it}(−ζ′/ζ)(c + it)/(c + it) dt`,
  com `Σ n^{−σ} ≤ 8/(σ − 1)` (`tsum_um_le`);
* **o resíduo** (`bordo_Fx`): `∮ x^s(−ζ′/ζ)(s)/s ds = 2πi x` no retângulo `[a, c] × [−T, T]` onde
  `G(s) = (s − 1)ζ(s) ≠ 0`;
* **as cotas sob RH** (`logDeriv_RH_unif`): `|ζ′/ζ(σ + iy)| ≤ C log(2 + |y|)/(σ − ½)` em `½ < σ ≤ ¾`, para todo `y`
  (rodada 63 em `|y| ≥ 6`, compacidade em `|y| ≤ 6`); `∫_{−T}^{T} dy/(1 + |y|) = 2 log(1 + T)` (`integral_um_abs`);
* **a escolha** (`psi_RH_meio`) `η = 1/log x`, `c = 1 + 2η`, `a = ½ + η`, `T = x²`, `x = N + ½`: Perron custa
  `48e² log² x/π`, os lados horizontais `O(log² x)`, o vertical `72e C √x log³ x`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| RH ⟺ `ψ(x) = x + O(√x log³ x)` | CERTIFIED | reformulação |
| RH ⟹ `ψ(x) = x + O(√x log² x)` (fórmula explícita, `x^ρ/ρ`) | CERTIFIED (rodada 67) | consequência |
| RH ⟹ `π(x) = Li(x) + O(√x log x)` | CERTIFIED (rodada 67) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/psi_rh.py`, `dados/psi_rh.json`, `testes/test_psi_rh.py`, 2 testes). Até `x = 10⁷`, por década, o
máximo de `|ψ(x) − x|/(√x log³ x)` cai de `0,0080` (`x ≤ 100`) a `0,00024`, e o de `|ψ(x) − x|/(√x log² x/8π)`
(Schoenfeld, sob RH) de `0,92` a `0,083`; `η Λ(n) n^{−η} ≤ 0,35` para `η = 1/log 10⁷`.

## 4bs. RH ⟺ `θ(x) = x + O(√x log³ x)` ⟺ `π(x) = Li(x) + O(√x log² x)` (rodada 65)

Um arquivo, **11 teoremas** (total 7853), só os axiomas padrão (`ZeroClasses/PiLiRH.lean`). Da rodada 64 para `θ` e `π`:

* **`theta_RH`**: sob RH, `|θ(x) − x| ≤ K √x log³ x` em `x ≥ 2` (`ψ − θ ≤ 2√x log x` da Mathlib; `ψ(x) ≤ x²` em
  `[2, 100]`); **`rh_iff_thetaLog3`**;
* **`pi_sub_Li`**: `π(x) − Li(x) = (θ(x) − x)/log x + ∫_2^x (θ(t) − t)/(t log² t) dt + 2/log 2`;
* **`pi_RH`**: sob RH, `|π(x) − Li(x)| ≤ K √x log² x` em `x ≥ 2` (`pi_of_thetaLog3`: o termo de fronteira dá
  `√x log² x`, a integral `∫_2^x log t · t^{−1/2} dt ≤ 2√x log x`); **`rh_iff_piLog2`**;
* as voltas pela rodada 60 com `√x log^k x ≤ (k/ε)^k x^{½+ε}` (`sqrt_log_pow_le`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| RH ⟺ `θ(x) = x + O(√x log³ x)` | CERTIFIED | reformulação |
| RH ⟺ `π(x) = Li(x) + O(√x log² x)` | CERTIFIED | reformulação |
| RH ⟹ `π(x) = Li(x) + O(√x log x)` (fórmula explícita) | CERTIFIED (rodada 67) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/pi_li_rh.py`, `dados/pi_li_rh.json`, `testes/test_pi_li_rh.py`, 2 testes). Até `10⁷`:
`max |θ(x) − x|/(√x log³ x)` por década cai de `0,016` (`10² < x ≤ 10³`) a `0,00065`; `|π(x) − Li(x)|/(√x log² x)` de
`0,019` (`x = 100`) a `0,00041` (`x = 10⁷`, `π − Li = −338,4`); contra a cota de Schoenfeld `√x log x/8π` (válida em
`x ≥ 2657`), `0,44` a `0,17`; a fórmula de partes confere em `x = 10⁴` (`−16,0921`).

## 4bt. As peças da fórmula explícita (rodada 66)

Um arquivo, **15 teoremas** (total 7868), só os axiomas padrão (`ZeroClasses/ExplicitaPecas.lean`). Para deslocar o
contorno de Perron **através** dos zeros (Davenport, cap. 17):

* **`principio_ponderado`**: `∮_{∂R} (f′/f)·φ = 2πi Σ_u m_u φ(u)` para `f`, `φ` analíticas perto do retângulo, sem
  zeros de `f` no bordo (o quociente local da rodada 40 e `φ(s)/(s − u) = dslope φ u (s) + φ(u)/(s − u)`);
* **`bordo_explicita`**: no retângulo `[b, c] × [−T, T]` (`0 < b < 1 < c`) sem zeros de `ζ` no bordo,
  `∮ x^s(−ζ′/ζ)(s)/s ds = 2πi (x − Σ_ρ m_ρ x^ρ/ρ)`, via `G(s) = (s − 1)ζ(s)` (`ordem_Gp`, `Gp_eq_zero_iff`);
* **`soma_ordem_norm`**: `Σ_{|γ| ≤ T} m_ρ/|ρ| ≤ C (1 + log T)²` (blocos `⌊|γ|⌋ = k`, caixas de Jensen,
  `H_n ≤ 1 + log n`);
* **`separa`, `altura_boa`**: em cada `[T₀, T₀ + 1]`, `T₀ ≥ 6`, há `T` com `||γ| − T| ≥ 1/(2(n + 1))` para todo zero
  (`n = O(log T₀)` zeros próximos, casa dos pombos entre `n + 1` candidatos) e, lá, `ζ(σ ± iT) ≠ 0` e
  `|ζ′/ζ(σ ± iT)| ≤ C log²(2 + T)` em `0 < σ ≤ 2` — **incondicional**;
* **`logDeriv_quarto_RH`**: sob RH, `|ζ′/ζ(¼ + it)| ≤ C log(2 + |t|)`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| princípio do argumento ponderado; resíduo `x − Σ x^ρ/ρ`; alturas boas | CERTIFIED | ferramenta |
| RH ⟹ `ψ(x) = x + O(√x log² x)` | CERTIFIED (rodada 67) | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/explicita_pecas.py`, `dados/explicita_pecas.json`, `testes/test_explicita_pecas.py`, 2 testes):
`Σ_{|γ|≤T} 1/|ρ|/(1 + log T)²` de `0,028` (`T = 50`) a `0,060` (`T = 600`); o algoritmo de `separa` em
`T₀ = 100…400` acha `T` com separação `0,35–1,26 ≥ δ` e `|ζ′/ζ(σ ± iT)|/log²(2 + T) ≤ 0,11`;
`max_{t ≤ 300} |ζ′/ζ(¼ + it)|/log(2 + t) = 3,01`.

## 4bu. O critério de von Koch na forma clássica: RH ⟺ `ψ(x) = x + O(√x log² x)` ⟺ `π(x) = Li(x) + O(√x log x)` (rodada 67)

Um arquivo, **8 teoremas** (total 7876), só os axiomas padrão (`ZeroClasses/PsiLog2.lean`, namespace
`ATK.ZeroClasses.Koch`). Com as peças da rodada 66, o contorno de Perron atravessa os zeros:

* **`psi_RH_meio`**: sob RH, `|ψ(N) − (N + ½)| ≤ K √(N + ½) log²(N + ½)`. Perron (`perron_psi`, rodada 64) com
  `η = 1/log x`, `c = 1 + 2η` e uma **altura boa** `T ∈ [x², x² + 1]` (`altura_boa`); o resíduo explícito no
  retângulo `[¼, c] × [−T, T]` (`bordo_explicita`) dá `x − Σ_{|γ|<T} m_ρ x^ρ/ρ`; sob RH `|x^ρ| = √x` e
  `Σ m_ρ/|ρ| ≤ C log² x` (`soma_ordem_norm`); os lados horizontais custam `O(log² x)` e o lado `Re s = ¼`,
  `O(x^{1/4} log² x)` (`logDeriv_quarto_RH`);
* **`psi_RH_log2`** (`x ≥ 100`) e **`rh_iff_psiLog2`: RH ⟺ `ψ(x) = x + O(√x log² x)`** (a volta pela rodada 64);
* **`theta_RH_log2`**, **`pi_RH_log`** (fórmula de partes da rodada 65: fronteira `√x log x`, integral
  `∫_2^x t^{−1/2} dt ≤ 2√x`) e **`rh_iff_piLog`: RH ⟺ `π(x) = Li(x) + O(√x log x)`**.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| RH ⟺ `ψ(x) = x + O(√x log² x)` (von Koch 1901) | CERTIFIED | reformulação |
| RH ⟺ `π(x) = Li(x) + O(√x log x)` | CERTIFIED | reformulação |
| constantes explícitas (Schoenfeld: `√x log² x/8π`, `√x log x/8π`) | BUILD_PENDING | consequência |
| RH | OPEN_MATH | — |

Numérico (`codigo/psi_log2.py`, `dados/psi_log2.json`, `testes/test_psi_log2.py`, 2 testes). Até `10⁷`, por década,
`max |ψ(x) − x|/(√x log² x)` cai de `0,032` a `0,0033`; `|π(x) − Li(x)|/(√x log x)` de `0,039` (`x = 10³`) a `0,0066`
(`x = 10⁷`). O resíduo explícito em números: `x − Σ_{0<γ≤600} 2 Re(x^ρ/ρ) − log 2π − ½ log(1 − x^{−2})` reproduz
`ψ(x)` a `0,30` em `x = 100,5` e a `0,19` em `x = 1000,5`.

## 4bv. O critério de Li completo: RH ⟺ `λ_n ≥ 0` para todo `n ≥ 1` (rodada 68)

Um arquivo, **20 teoremas** (total 7896), só os axiomas padrão (`ZeroClasses/LiCompleto.lean`). A rodada 15
(`ATK/LiCriterio.lean`) tinha o núcleo algébrico zero a zero; agora a soma:

* **`lam n = Σ_{(ρ,j)} Re(1 − (1 − 1/ρ)^n)`**, absolutamente convergente (`summable_termo`): pelo **resto binomial**
  `|(1 − u)^n − 1 + nu| ≤ n²|u|²(1 + |u|)^n` (`resto_binom`, indução), `|Re(1 − w^n)| ≤ (n + n²(14/13)^n)/|ρ|²`
  (`abs_termo_le`) e `Σ 1/|ρ|² < ∞` (rodada 31);
* **RH ⟹ `λ_n ≥ 0`** (`lam_nonneg_of_RH`): sob RH `|w| = 1` e `Re(1 − w^n) ≥ 0`;
* **`λ_n ≥ 0` ∀ `n ≥ 1` ⟹ RH** (`RH_of_lam_nonneg`): um zero com `Re ρ < ½` (pela simetria `ρ ↦ 1 − ρ̄`) tem
  `|w| > 1`; os zeros de `|w|` máximo `r` são finitos (`|w|² ≤ 1 + 1/|ρ|²`, `finito_grande`) e os demais têm
  `|w| ≤ r₂ < r`; a **casa dos pombos no toro** (`dirichlet_simultaneo`, `cos_ge_meio`) dá `n` arbitrariamente
  grande com `cos(n arg w) ≥ ½` nos máximos, e a cota
  `λ_n ≤ |A|(1 − r^n/2) + (1 + r₂^n) n² S₂ + n S₁ + 3n² S₂` (`termo_le_cauda`: `Re(1 − w^n) ≤ n Re(1/ρ) + 3n²/|ρ|²`
  quando `|ρ| ≥ n`) fica negativa;
* **`rh_iff_li`**: `RiemannHypothesis ↔ ∀ n ≥ 1, 0 ≤ lam n`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| RH ⟺ `λ_n ≥ 0` para todo `n ≥ 1` (Li 1997, Bombieri–Lagarias 1999) | CERTIFIED | reformulação |
| `λ_1 = 1 + γ/2 − ½ log 4π` (rodada 69, CERTIFIED) e a assintótica `λ_n ~ (n/2) log n` sob RH | BUILD_PENDING (assintótica) | — |
| `λ_n ≥ 0` para todo `n` | OPEN_MATH (= RH) | — |

Numérico (`codigo/li_completo.py`, `dados/li_completo.json`, `testes/test_li_completo.py`, 2 testes): com os 341 zeros
de `0 < γ ≤ 600` e a cauda `n² (log(600/2π) + 1)/(2π·600)`, `λ_1 = 0,023093` (forma fechada `0,0230957`),
`λ_2 = 0,092335` (`0,0923457`), `λ_3 = 0,20762` (`0,2076389`); positivos e crescentes até `n = 30` (`λ_30 ≈ 17,3`,
assintótica `17,1`). Um zero hipotético `ρ = 0,4 + 14,13i` teria `|w| = 1,0005`, e a parcela cai abaixo de `−10` em
`n = 4796`.

## 4bw. `λ₁ = 1 + γ/2 − ½ log 4π` e RH ⟺ `Σ_ρ 1/|ρ|² = 2 + γ − log 4π` (rodada 69)

Um arquivo, **26 teoremas** (total 7922), só os axiomas padrão (`ZeroClasses/LiUm.lean`). Com o produto de Hadamard e
os valores da Mathlib `Λ₀(0) = Λ₀(1) = (γ − log 4π)/2 + 1`:

* **a reflexão nas cópias** (`refl`, `reflEquiv`): `(ρ, j) ↦ (1 − ρ, j)` é uma involução de `ZM` (ordens simétricas,
  rodada 31); daí `Σ_ρ Re 1/(½ − ρ) = 0` (`soma_meio_zero`);
* **`B_eq`**: a constante de Hadamard é `B = ξ′/ξ(0) = −((γ − log 4π)/2 + 1)`;
* **`lam_um`**: `λ₁ = Σ_ρ Re(1/ρ) = 1 + γ/2 − ½ log 4π` (com `L(½) = 0`); `lam_um_pos`, e daí
  **`log 4π < 2 + γ`** (`log_quatro_pi_lt`) — uma desigualdade real deduzida dos zeros;
* **`soma_inv_quad_ge`**: `Σ_ρ 1/|ρ|² ≥ 2 + γ − log 4π`, pois `Σ (1 − 2β)/|ρ|²` vale metade de
  `Σ (1 − 2β)²/(|ρ|²|1 − ρ|²) ≥ 0` (`par_eq`, pareando `ρ` com `1 − ρ`);
* **`rh_iff_soma_inv_quad`**: **RH ⟺ `Σ_ρ 1/|ρ|² = 2 + γ − log 4π`** (com multiplicidade).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `B = −λ₁`, `λ₁ = 1 + γ/2 − ½ log 4π` | CERTIFIED | consequência |
| RH ⟺ `Σ_ρ 1/|ρ|² = 2 + γ − log 4π` | CERTIFIED | reformulação |
| RH | OPEN_MATH | — |

Numérico (`codigo/li_um.py`, `dados/li_um.json`, `testes/test_li_um.py`, 2 testes): `ξ′/ξ(0)` por diferença finita
`= −0,0230957086` (fórmula `−0,0230957090`); `Σ_{0<γ≤600} 2/(¼ + γ²) = 0,043237` mais a cauda `0,002949` dá
`0,046186` contra `2 + γ − log 4π = 0,046191`; um par fora da reta (`β = 0,4`, `γ = 100`) somaria `4,0·10⁻¹⁰` a mais.

## 4bx. A fórmula explícita, primeira metade: os resíduos no retângulo largo (rodada 70)

Um arquivo, **19 teoremas** (total 7941), só os axiomas padrão (`ZeroClasses/ExplicitaResiduos.lean`). Sem hipótese
alguma, no retângulo `[−(2K + ½), c] × [−T, T]` (`c > 1`, `T > 0`, sem zeros de `ζ` nas horizontais):

  **`∮ x^s(−ζ′/ζ)(s)/s ds = 2πi (x − Σ_ρ m_ρ x^ρ/ρ + Σ_{n<K} x^{−2(n+1)}/(2(n+1)) − log 2π)`**   (`bordo_largo`),

`ρ` sobre os zeros não triviais do retângulo com multiplicidade. As peças:

* **o princípio do argumento ponderado com um polo** (`principio_polo`): `∮ (f′/f)(φ + c/(s − p)) =
  2πi (Σ_u m_u (φ(u) + c/(u − p)) + c f′/f(p))` para `φ` analítica e `f(p) ≠ 0`;
* **`ζ₁(s) = (s − 1)ζ(s)`** (`riemannZeta₁` da Mathlib, inteira): `ord_u ζ₁ = ord_u ζ` fora de `1` (`ordem_zeta1`), ordem
  finita em toda parte (`ordem_zeta1_ne_top`), `ζ₁′/ζ₁ = ζ′/ζ + 1/(s − 1)` (`logDeriv_zeta1`) e
  **`ζ₁′/ζ₁(0) = log 2π − 1`** (`logDeriv_zeta1_zero`, de `ζ(0) = −½`, `ζ′(0) = −½ log 2π`);
* **os zeros triviais são simples** (`deriv_trivial`, `ordem_trivial`): pela equação funcional,
  `ζ(s) = h(s) cos(π(1 − s)/2)` perto de `−2(n + 1)` com `h = 2(2π)^{s−1}Γ(1 − s)ζ(1 − s) ≠ 0`, e o cosseno tem zero
  simples (`sen² + cos² = 1`);
* a decomposição `x^s(−ζ′/ζ)/s = −(ζ₁′/ζ₁)(ψ₁ + 1/s) + [dslope x^· 1 − ψ₁] + x/(s − 1) − 1/s`, `ψ₁ = (x^s − 1)/s`
  inteira: o polo de `ζ` em `1` vira o resíduo `x`, o polo de `1/s` em `0` vira `−log 2π`, e cada zero trivial
  `−2(n + 1)` dentro do retângulo dá `x^{−2(n+1)}/(2(n+1))`;
* `horizontais_boas`: as alturas `T ∈ [T₀, T₀ + 1]` da rodada 66 servem de horizontais.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| zeros triviais simples; `ζ₁′/ζ₁(0) = log 2π − 1` | CERTIFIED | ferramenta |
| a identidade de resíduos no retângulo largo (`bordo_largo`) | CERTIFIED | ferramenta |
| o limite `T, K → ∞` (a fórmula explícita `ψ₀(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½ log(1 − x^{−2})`) | CERTIFIED (rodada 71, §4by) | ferramenta |
| RH | OPEN_MATH | — |

Numérico (`codigo/explicita_residuos.py`, `dados/explicita_residuos.json`, `testes/test_explicita_residuos.py`,
2 testes): `ζ₁′/ζ₁(0)` por diferença finita `= 0,8378770668` contra `log 2π − 1 = 0,8378770664`; `ζ′(−2k)`, `k ≤ 5`,
bate com `(−1)^k (2k)! ζ(2k + 1)/(2(2π)^{2k})` (`ζ′(−2) = −0,0304484571`); em `x = 10,3`, a integral de contorno por
Simpson em `[−2,5; 2] × [−20, 20]` dá `8,013047047` contra os resíduos `8,013047044`, e em `[−4,5; 2] × [−20, 20]`
dá `8,013069268` contra `8,013069256`.

## 4by. A fórmula explícita de Riemann–von Mangoldt (rodada 71)

Um arquivo, **25 teoremas** (total 7966), só os axiomas padrão (`ZeroClasses/ExplicitaLimite.lean`). Sem hipótese
alguma, para `x = N + ½` (`N ≥ 1`) e alturas boas `T_k ∈ [k + 6, k + 7]`:

  **`Σ_{|γ| ≤ T_k} m_ρ x^ρ/ρ → x − ψ(N) − log 2π − ½ log(1 − x^{−2})`**   (`formula_explicita`),

`ρ` sobre os zeros não triviais (`ζ(ρ) = 0`, `Re ρ > 0`) com multiplicidade. É a fórmula explícita clássica
`ψ₀(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½ log(1 − x^{−2})` (Davenport cap. 17), com a soma simétrica em alturas boas.
A prova junta a identidade de resíduos da rodada 70 no retângulo `[−(2K + ½), 2] × [−T, T]` (`K = k + 7`) com:

* **Perron** na reta `Re s = 2` (rodada 64): erro `32x²(4x + 2)/(πT)`;
* **as horizontais** `O(log² T/T)` (`hor_le`): `‖ζ′/ζ(σ ± iT)‖ ≤ A(T) − σ` para todo `σ ≤ 2` (`logDeriv_hor`), com
  `A(T) = C log²(2 + T) + O(log T)`; em `σ ≤ 0` pela equação funcional (`logDeriv_esq_le`, de
  `logDeriv_riemannZeta_one_sub` da Mathlib), a digama `‖ψ(s)‖ ≤ log(2 + |Im s|) + 11 + Re s/3` (`digamma_hor`) e
  `‖tan z‖ ≤ 2` em `|Im z| ≥ 1` (`norm_tan_le_dois`); a integral `∫_{−U}^2 x^σ(A − σ) dσ` em forma fechada
  (`integral_exp_lin`);
* **a reta esquerda** `Re s = −(2K + ½)` (`esq_le`): `‖ζ′/ζ‖ ≤ c₀ + B + log(2 + T) + 4K + 8` (`logDeriv_esq_reta`), com
  `‖tan‖ = 1` lá (`norm_tan_le_um`, `sen² = cos²` em `Kπ + 3π/4`) e `‖ψ(n + ½ + iy)‖ ≤ B + log(2 + |y|) + 2n`
  (`digamma_esq`, compacidade em `½ + i[−3, 3]`); o fator `x^{−2K}` mata o resto;
* **os zeros triviais**: `Σ_{n<K} x^{−2(n+1)}/(2(n+1)) → −½ log(1 − x^{−2})` (`triv_soma`);
* o erro total `ε_k → 0` (`eps`, `eps_tendsto`) e a forma com erro altura a altura (`explicita_k`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| a fórmula explícita `Σ_{\|γ\|≤T_k} x^ρ/ρ → x − ψ(N) − log 2π − ½ log(1 − x^{−2})`, sem hipóteses | CERTIFIED | ferramenta |
| a mesma com `T → ∞` sem restringir a alturas boas | CERTIFIED (rodada 72, §4bz) | consequência |
| a mesma com `x` real qualquer (`ψ₀(x)` nos inteiros) | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/explicita_limite.py`, `dados/explicita_limite.json`, `testes/test_explicita_limite.py`, 2 testes):
`‖tan z‖ ≤ 1,313` em `|Im z| ≥ 1`, `‖tan(πs/2)‖ = 1` (a `10⁻¹⁴`) em `Re s = 2K + 3/2`; folga mínima `11,07` em
`digamma_hor` numa grade; a forma logarítmica da equação funcional bate a `2·10⁻¹⁰` (consistência, com `ζ` em `Re < ½`
pela própria equação funcional). Com os 341 zeros de `0 < γ ≤ 600`: em `x = 10,5` o erro cai de `0,128` (`T = 50`) a
`0,027` (`T = 600`); em `x = 30,5`, de `0,79` a `0,12`.

## 4bz. A fórmula explícita com `T → ∞` (rodada 72)

Um arquivo, **7 teoremas** (total 7973), só os axiomas padrão (`ZeroClasses/ExplicitaT.lean`). Para `x = N + ½`
(`N ≥ 1`):

  **`lim_{T → ∞} Σ_{|γ| ≤ T} m_ρ x^ρ/ρ = x − ψ(N) − log 2π − ½ log(1 − x^{−2})`**   (`formula_explicita_T`),

com `T` real qualquer (não só alturas boas), a soma sobre `Zfin T` = zeros não triviais com `|γ| ≤ T` (`zfin_finite`,
`mem_Zfin`). A passagem das alturas boas da rodada 71 para `T` qualquer: em `T, T′ ∈ [k + 6, k + 7]` as somas diferem
pelos zeros com `k + 6 < |γ| ≤ k + 7`, cuja massa é `≤ 4 (a₀ + log(k + 9))/l₀` (`soma_faixa_le`, pelas caixas de
Jensen `caixa_le'`), cada um com `‖x^ρ/ρ‖ ≤ x/(k + 6)` (`norm_termo_le`); logo
`‖Σ_{Zfin T} − Σ_{Zfin T′}‖ ≤ 8 (a₀ + log(k + 9))/l₀ · x/(k + 6) → 0` (`dif_le`).

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `lim_{T→∞} Σ_{\|γ\|≤T} m_ρ x^ρ/ρ = x − ψ(N) − log 2π − ½ log(1 − x^{−2})`, `x = N + ½` | CERTIFIED | consequência |
| `x` real qualquer | BUILD_PENDING | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/explicita_t.py`, `dados/explicita_t.json`, `testes/test_explicita_t.py`, 2 testes): com os 341 zeros
de `0 < γ ≤ 600`, a massa máxima de uma faixa é `4`, contra a cota mínima `155,2` (razão `≤ 0,019`); em `x = 10,5` e
`T = 77,7; 150,2; 333,3; 599,9` os erros são `0,246; −0,105; 0,054; 0,027`.

## 4ca. Báez-Duarte ponderado: a forma espectral e o molificador de Riesz (rodada 73)

Um arquivo, **19 teoremas** (total 7992), só os axiomas padrão (`ZeroClasses/BDEspectral.lean`). Primeira peça da
questão Q2(ii) de `fronteira/RH_frontier.md` (a necessidade com taxa: `Θ ≤ θ < σ ⟹ D_N(σ) ≪ N^{−2(σ−θ)+ε}`).

* **Plancherel de Mellin ponderado** (`plancherel_σ`): `∫_0^∞ |f|² t^{2σ−1} dt = (1/2π) ∫ |𝓜f(σ + iτ)|² dτ`, reduzido
  ao caso `σ = ½` da Mathlib/ATK por `f ↦ t^{σ−½} f`;
* **a forma espectral** (`Wσ_espectral`): `‖χ − Σ c_k ρ_{k+1}‖²_σ = (1/2π) ∫ |1 + ζ(s)Σ c_k (k + 1)^{−s}|²/|s|² dτ`,
  `s = σ + iτ`, `0 < σ < 1`; daí `D_N(σ)` e `inf_N D_N(σ)` ficam abaixo dessa integral para qualquer `c`
  (`DNσ_le`, `iInf_DNσ_le`);
* **o núcleo de Riesz** `w(u) = (1 − u)²₊`: `𝓜w(z) = 2/(z(z + 1)(z + 2))` (`hasMellin_wR`), `‖W(c + iy)‖ ≤
  (8/c)(1 + |y|)^{−2}` (`norm_WR_le`) e a inversão `w(u) = (1/2π) ∫ u^{−(c+iy)} W(c + iy) dy` (`wR_inv`);
* **o molificador** `A_N(s) = Σ_{k<N} μ(k)(1 − k/N)² k^{−s}` e a **representação integral**
  `A_N(s) = (1/2π) ∫ W(c + iy) N^{c+iy} ζ(s + c + iy)^{−1} dy` para `Re s + c > 1` (`LSeries_aN_int`);
* **`DNσ_le_molif`**: `D_N(σ) ≤ (1/2π) ∫ |1 − ζ(s)A_N(s)|²/|s|² dτ`.

O passo seguinte (rodada 74) é deslocar a integral de `A_N` para `Re z = −δ` sob `SemZeros θ`: o resíduo em `z = 0` é
`1/ζ(s)`, e `1 − ζ(s)A_N(s) = O(N^{−δ}|ζ(s)|(1 + |τ|)^η)`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Plancherel ponderado; forma espectral de `D_N(σ)`; molificador de Riesz e sua representação | CERTIFIED | ferramenta |
| Q2(ii): `SemZeros θ ⟹ D_N(σ) ≪ N^{−2(σ−θ)+ε}` para `θ < σ < 1` | CERTIFIED (rodada 75, §4cc) | reformulação |
| Q2(iii): o piso ponderado `κ(σ) ≤ 2(σ − Θ)` | OPEN_MATH | — |
| RH | OPEN_MATH | — |

Numérico (`codigo/bd_espectral.py`, `dados/bd_espectral.json`, `testes/test_bd_espectral.py`, 2 testes):
`𝓜w(0,7 + 3i)` por Simpson bate com `W` a `10⁻¹⁴`; a inversão de Mellin recupera `w(0,3) = 0,49` a `2·10⁻⁸` e
`w(1,7) = 0` a `2·10⁻⁹`; a representação de `A_10(1,5 + 2i)` bate a `3·10⁻⁸`; a cota espectral em `σ = 0,8` cai de
`0,47` (`N = 10`) a `0,047` (`N = 40`) e `0,0039` (`N = 160`).

## 4cb. Báez-Duarte ponderado: o deslocamento do molificador (rodada 74)

Um arquivo, **10 teoremas** (total 8002), só os axiomas padrão (`ZeroClasses/BDDesloc.lean`). Segunda peça da Q2(ii).
Sob `SemZeros θ` (`½ ≤ θ < 1`), para `θ + δ < Re s < 1` e `0 < δ < 1`:

  **`A_N(s) = 1/ζ(s) + (1/2π) ∫ W(−δ + iy) N^{−δ+iy} ζ(s − δ + iy)^{−1} dy`**   (`desloc`),

e daí, na reta `Re s = σ`, **`|A_N(σ + iτ) − 1/ζ(σ + iτ)| ≤ K N^{−δ}(1 + |τ|)^η`** uniforme em `N` e `τ`
(`molif_cota`). A prova:

* `bordo_Gs`: `∮ W(z)N^z F(s + z) dz = 2πi F(s)` em `[−δ, 1] × [−Y, Y]` — `W(z)N^zF(s + z) = H(z)/z` com `H` holomorfa
  (`F = 1/ζ` holomorfa em `Re > θ`, `QuasiRH.differentiableAt_F`), `dslope` + `bordo_inv`;
* `norm_WR_esq`, `norm_WR_hor`: `‖W(−δ + iy)‖ ≤ 8/(δ(1 − δ)) (1 + |y|)^{−2}`, `‖W(x ± iY)‖ ≤ 2/|Y|³`;
* `norm_Gs_le`, `integrable_Gs`: com `|1/ζ| ≤ C(1 + |Im|)^η` (`QuasiRH.norm_F_le`) e
  `(1 + |a + b|)^η ≤ (1 + |a|)^η(1 + |b|)^η` (`um_add_le`), as retas são integráveis;
* `Y → ∞`: as horizontais são `O(Y^{−2})` e as verticais convergem (`intervalIntegral_tendsto_integral`); o lado
  `Re z = 1` é `2π A_N(s)` pela representação da rodada 73.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| `A_N(s) − 1/ζ(s) = (1/2π)∫ W(−δ+iy)N^{−δ+iy}/ζ(s−δ+iy) dy` e `\|A_N − 1/ζ\| ≤ K N^{−δ}(1+\|τ\|)^η`, sob `SemZeros θ` | CERTIFIED | ferramenta |
| Q2(ii): `D_N(σ) ≪ N^{−2δ}` | CERTIFIED (rodada 75, §4cc) | reformulação |
| RH | OPEN_MATH | — |

Numérico (`codigo/bd_desloc.py`, `dados/bd_desloc.json`, `testes/test_bd_desloc.py`, 2 testes): em `s = 0,8 + 3i`,
`δ = 0,2`, `N = 10`, os dois lados de `desloc` batem a `4·10⁻⁸`; `|A_N(s) − 1/ζ(s)|` cai de `0,46` (`N = 10`) a
`0,0077` (`N = 640`), com `|A_N − 1/ζ|·N^{1/4}` decrescendo de `0,82` a `0,039`.

## 4cc. Báez-Duarte ponderado com taxa: a questão Q2(ii) (rodada 75)

Um arquivo, **7 teoremas** (total 8009), só os axiomas padrão (`ZeroClasses/BDTaxa.lean`). Fecha a questão Q2(ii) de
`fronteira/RH_frontier.md`. Para `½ ≤ θ < 1`, sob `SemZeros θ` (`ζ ≠ 0` em `Re s > θ`):

  **`D_N(σ) ≤ K N^{−2δ}`** para todo `0 < δ < σ − θ`, `θ < σ < 1`   (`DNσ_taxa`),

com `D_N(σ) = inf_c ∫_0^∞ (χ − Σ_{k≤N} c_k {1/(kt)})² t^{2σ−1} dt` (rodada 59): `κ(σ) ≥ 2(σ − θ)`. Consequências:

* `DNσ_tendsto`, `iInf_DNσ_eq_zero`: `D_N(σ) → 0` para todo `σ ∈ (θ, 1)`;
* **`semZeros_iff_DNσ`**: `SemZeros θ ⟺ ∀ σ ∈ (θ, 1), inf_N D_N(σ) = 0` (com a suficiência da rodada 59);
* **`rh_iff_DNσ`**: **RH ⟺ `inf_N D_N(σ) = 0` para todo `σ ∈ (½, 1)`**, e sob RH `D_N(σ) ≪ N^{−2δ}` para
  `δ < σ − ½` (`DNσ_taxa_RH`).

A prova junta as rodadas 73–74: `D_N(σ) ≤ (1/2π)∫|1 − ζ(s)A_N(s)|²/|s|²`, `1 − ζA_N = ζ(1/ζ − A_N)`,
`|1/ζ − A_N| ≤ K N^{−δ}(1 + |τ|)^{1/8}` (`molif_cota`) e `|ζ(σ + iτ)| ≤ C(1 + |τ|)^{1/8}` sob `SemZeros θ`
(`norm_zeta_linha`, Borel–Carathéodory da rodada 57 com `exp(Re L)`); com `|s| ≥ σ(1 + |τ|)/2` o integrando fica
`≤ (const) N^{−2δ}(1 + |τ|)^{−3/2}`.

| Afirmação | Estado | Classe |
| --- | --- | --- |
| Q2(ii): `SemZeros θ ⟹ D_N(σ) ≪ N^{−2δ}`, `δ < σ − θ` | CERTIFIED | reformulação |
| `SemZeros θ ⟺ ∀ σ ∈ (θ,1), inf_N D_N(σ) = 0`; RH ⟺ o mesmo com `θ = ½` | CERTIFIED | reformulação |
| a versão incondicional com um semiplano externo (`θ = 7/8` ou `0,8749…`) | BUILD_PENDING (precisa importar o semiplano) | — |
| Q2(iii): o piso ponderado `κ(σ) ≤ 2(σ − Θ)` | OPEN_MATH | — |
| `SemZeros θ` para algum `θ < 1`; RH | OPEN_MATH | — |

Numérico (`codigo/bd_taxa.py`, `dados/bd_taxa.json`, `testes/test_bd_taxa.py`, 2 testes): a cota espectral em
`σ = 0,75` (`|τ| ≤ 1000`) cai de `0,448` (`N = 10`) a `0,0042` (`N = 160`), com expoentes locais `1,53`–`1,76`,
acima do `2(σ − ½) = 0,5` garantido sob RH.

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
