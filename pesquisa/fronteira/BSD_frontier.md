# BSD (Birch–Swinnerton-Dyer): fronteira de pesquisa para o programa ATK (2026-10-21)

**Ponto de partida (dossiê `BSD_summary.md`).** Nenhum P0. Os P1 genuínos são estes. Na main: E32 `y²=x³−x` com E(ℚ)={O,(0,0),(±1,0)}, bijeção congruente; o Clay reduzido a `∃ continuação inteira de WeierstrassCurve.LSeries com ord₁ = posto`; Ω, #tors, Néron–Tate, regulador, c_p (p∤2) para E32; Mordell–Weil para 2-torção completa; posto ≥ 2 para `y²=x(x+30)(x+2)`; posto ≥ 1 para `y²=x³−36x`. Só nos ramos (`atk/rh-rho-independent`, `atk/bsd-fc-sem-hipoteses-20261015`): **BSD-posto incondicional para E32** e o critério `AtaqueBSD.L1_ne_zero` (sinal +1, |aₙ|≤n, e^{−2π/√N}<½ ⇒ L(E,1)≠0, ou seja N<82); a ponte modular de E32 por fatoração da teta de Hecke de ℚ(i) em produto de tetas de Jacobi 1D (`PonteModularCurva32`); e **Mordell–Weil para toda E/ℚ** (`MordellWeilGeral`, `SelmerFinito`). O7 (fórmula refinada) e O6 (posto ∀E) estão intocadas.

## 1. Estado da arte (outubro de 2026)

- **Posto analítico ≤ 1 (Gross–Zagier 1986 + Kolyvagin 1988–90 + modularidade BCDT 2001).** Para toda E/ℚ, r_an ∈ {0,1} implica r = r_an. Coates–Wiles (1976/77) já davam isso para CM com L(E,1)≠0 [Clay]. Ш é finito nesses casos; BSZ apresentam "BSD-posto e Ш finito" como consequência de r ≤ 1 [BSZ].
- **Recíprocas (p-converse).** Skinner (Annals 2020): E semiestável com redução multiplicativa adequada em primos ímpares, posto 1 e #Ш<∞ ⇒ r_an = 1 [Sk]. Burungale–Skinner–Tian–Wan (arXiv 2409.01350, set/2024): conjectura principal supersingular de Kobayashi para E semiestável; parte p de BSD em r_an ≤ 1; **primeiras famílias infinitas de curvas não-CM com BSD completo** [BSTW]. Burungale–Tian (2506.03465, v2 out/2025): para E CM, corank Sel_{p^∞} = 0 ⇒ r_an = 0 [BT25]. Yan–Zhu (2412.20078): conjectura principal não-CM ordinária sob a hipótese de Heegner. Retira a hipótese de primo ruim de Skinner–Urban [SU14] e dá a p-converse em r ≤ 1 [YZ].
- **Estatística.** Bhargava–Shankar: média de Sel₅ é 6 e posto médio ≤ 0,885 [Baker]. Bhargava–Skinner–Zhang (2014): **≥ 66,48%** das E/ℚ (por altura) satisfazem BSD-posto e têm Ш finito; ≥16,50% têm r=r_an=0 e ≥20,68% têm r=r_an=1 [BSZ]. Heurística de Park–Poonen–Voight–Wood (JEMS 2019): só finitas E com posto > 21 [PPVW].
- **Verificação numérica do BSD completo.** Creutz–Miller (2012): fórmula BSD completa provada para **toda E/ℚ com N < 5000 e r_an ≤ 1**, fechando 11 pares (classe, ℓ ∈ {5,7}) por segunda descida [CM].
- **Posto ≥ 2: muro.** "Não há algoritmo incondicional conhecido para o posto". Sob BSD, r_an só é determinável exatamente para ordem ≤ 3 (Buhler–Gross–Zagier 1985 para posto 3); acima disso só há cotas condicionais a GRH [Bob]. Não encontrei prova de Ш finito para nenhuma E/ℚ de posto ≥ 2. Banwait (arXiv 2609.08431, set/2026, **assistido por Claude, com formalização Lean parcial**) prova só Ш[p^∞]=0 **primo a primo**. As hipóteses: E CM de posto 2 e sinal +1, p split ≥ 5, e a condição de unidade sobre c̃₂(p), o 2º coeficiente de Taylor do L_p de Mazur–Tate–Teitelbaum. Há também um critério equivalente com o regulador p-ádico. A questão "horizontal" (Ш[p]=0 para todo p grande) fica explicitamente aberta [Ban]. Sobre corpos de funções, Ш finito em r>1 só vale para classes especiais de superfícies [HYZ].
- **Recordes de posto.** Posto ≥ 29: Elkies–Klagsbrun (2024). Posto ≥ 30 e ≥ 31: Alpöge–Howell (2026), segundo nota da tabela "foi Claude, com L. Alpöge e A. Howell"; não verificado independentemente [Mag]. Posto ≥ 32: Elkies–Klagsbrun–Li (2026). Maior posto conhecido *exatamente* e incondicionalmente: 22 (S. Li, set/2026) [Duj]. Todos são **cotas inferiores algébricas**, nada analítico.
- **Números congruentes.** Tunnell: n congruente ⇒ 2Aₙ = Bₙ, incondicional (via Coates–Wiles); a recíproca exige BSD [Clay]. Genocchi/Razar: p ≡ 3 (8) não é congruente. Heegner: p ≡ 5,7 (8) é congruente. Monsky: n com dois primos ímpares [Dal]. Tian (2014) e Tian–Yuan–Zhang dão critérios por períodos e pontos de gênero; com ord ≤ 1, BSD dá #Ш(Eₙ) = L̂(n)² [TYZ]. Smith + Burungale–Tian: densidade 1 de n ≡ 1,2,3 (8) não congruentes, e Goldfeld de paridade par vale para essa família [BT21]. Para n ≡ 5,6,7 (8): ">50%" [BT21]; Kriz (2020, não publicado): "100%" [Dal]. Zhao e Li–Tian dão BSD para famílias com Selmer φ trivial [Rho].
- **IA e fenômenos.** Murmurações foram descobertas por aprendizado de máquina (He–Lee–Oliver–Pozdnyakov 2022). Prova no aspecto peso sob GRH: Bober–Booker–Lee–Lowry-Duda, ANT 20:2 (2026) [BBLL]. Para curvas ordenadas por altura (arXiv 2504.12295): conjectura com densidade explícita e teorema só para uma variante [SS].
- **FLT em Lean (Anthropic, 04/09/2026).** 13 M linhas, Lean 4.33.1, Mathlib v4.33.0. Só usa os 3 axiomas padrão, foi checada por comparator e nanoda, e Buzzard revisou [AnFLT, FLTgh]. Inclui **`WeierstrassCurve.modularity_of_semistableModel`**: todo modelo semiestável é `IsModular`, isto é, os a_ℓ coincidem nos primos bons com os de uma autoforma de peso 2 em algum Γ₀(N). O próprio texto diz "nada sobre curvas não semiestáveis, parametrizações modulares ou funções L" [PP].
- **Mathlib d13f23b (24/09/2026), lida localmente.**
  - Já tem: curvas de Weierstrass e lei de grupo (afim, jacobiana, projetiva), polinômios de divisão, redução e modelos minimais (Wang 2025), `WeierstrassCurve.LFunction` (Browning 2026), altura ingênua com paralelogramo aproximado e o `GroupTheory/Descent` (Stoll 2026), L de formas modulares como `WeakFEPair` f ↔ f|S para Γ aritmético (Loeffler 2025; entire para formas cuspidais), η com η(−1/z)=√(z/i)η(z) (`Discriminant.lean`), anéis de Hecke abstratos (Birkbeck 2026, só definições), Jacobi/Hurwitz e Poisson em ℝ [LS].
  - **Não tem:** cota de Hasse, operadores T_n em S_k(Γ₀(N)), newforms, Atkin–Lehner/Fricke, CM e endomorfismos, módulo de Tate, Selmer/H¹ de Galois de E, Mordell–Weil, altura de Néron–Tate, caracteres de Hecke (Grössencharaktere).

## 2. Barreiras (no-go) e rotas do ATK que elas eliminam

1. **Barreira da anulação.** A numérica certifica L^{(k)}(E,1) ≠ 0, mas nunca = 0.
   - Zeros exatos só vêm de três fontes: (i) paridade do sinal ε; (ii) racionalidade de L(E,1)/Ω com denominador limitado (símbolos modulares, Manin–Drinfeld); (iii) Gross–Zagier para L′ (ponto de Heegner de torção).
   - Por isso r_an só é conhecido exatamente até 3 [Bob].
   - *Elimina:* qualquer prova de r_an = r para as curvas-recorde, e r_an = 2 para `y²=x(x+30)(x+2)` sem símbolos modulares.
   - Observação útil: a não anulação é **semidecidível** pelo método do ATK. Com K termos explícitos e cauda geométrica, todo E com L(E,1)≠0 tem certificado finito, desde que a ponte modular esteja provada.
2. **Barreira de sistemas de Euler.** Kolyvagin precisa de uma classe-base não torção (ponto de Heegner), o que só acontece em r_an ≤ 1 [Clay]. Em r ≥ 2 o ponto de Heegner é de torção e o método não limita Ш.
   - *Elimina:* O7 (∀E: Ш finito + fórmula) por qualquer rota conhecida.
   - Mais forte: **o BSD completo de uma única curva** exige um sistema de Euler. Mesmo para E32 a descida só controla Ш[2^∞]; Ш[p] para todo p ímpar requer Rubin (unidades elípticas) ou Kolyvagin.
3. **Densidade ≠ universalidade.** BS/BSZ/Smith dão proporções; um conjunto de densidade 0 de contraexemplos fica intacto [BSZ, BT21].
   - *Elimina:* "ponte" de médias para ∀E, como os axiomas `uniform_nonvanishing` e `regulator_bounds_families` em `FinalTheorems/`.
4. **Não efetividade do posto.** Não há algoritmo conhecido [Bob]. "Calcular o posto de toda E" em Lean pressupõe Ш finito.
5. **Barreira de definição formal.** O posto analítico do ATK exige continuação inteira, portanto modularidade.
   - A FLT cobre **só semiestáveis**, e só a_ℓ bons. Toda curva CM tem redução aditiva em algum primo, logo **não é semiestável**: a rota FLT e a rota Hecke/CM são complementares, não redundantes.
   - *Elimina:* "BSDRank ∀E" sem newforms, Atkin–Lehner e o nível igual ao condutor (Carayol).
6. **Modelos paramétricos.** `BSDModel` com `analyticRank := rank` satisfaz BSDFull trivialmente. Só o `modeloCompleto` (L4) conta. Os `axiom kolyvagin` (∀E, posto 0) etc. são falsos ou vácuos.

## 3. Questões atacáveis, em ordem de valor × tratabilidade

**Q1 (b, formalização) — BSD-posto para todas as curvas CM de posto 0 com N ≤ X, sem Coates–Wiles.**
- *Enunciado:* para cada E de uma lista explícita, o `L4Base.BSDConjecture E` da main: as 13 classes de j CM e suas torções quadráticas com N ≤ 1000 e ε = +1 (p.ex. 27a, 36a `y²=x³+1`, 64a `y²=x³−4x`, 49a, 121b).
- *Por quê:* transforma o caso único E32 num **método**.
- *Ideia nova a formalizar:* para K de número de classes 1 (d ∈ {−3,−4,−7,−8,−11,−19,−43,−67,−163}), escreva 4N(α) = u² + |d|b². A teta de Hecke Σ ψ(α)q^{Nα}, com ψ(α)=χ(α mod 𝔣)·α, vira **soma finita de produtos de tetas 1D com característica** módulo M (M ∈ ℤ ∩ 𝔣, vezes 2). A FE então se reduz à FE 1D da Mathlib mais uma identidade de Fourier finita em (ℤ/M)², checável por `decide` em ZMod/AddChar. É o truque de `PonteModularCurva32` generalizado.
- *Também:* `L1_ne_zero` com K termos (certificado) e 2-descida explícita para o posto 0.
- *Progresso:* 2ª curva (36a ou 64a) no kernel; depois um teorema-esquema paramétrico em (d, 𝔣, χ).

**Q2 (b) — BSD-posto para uma curva de posto 1: E₆ `y²=x³−36x` (N=576, ε=−1, CM por ℤ[i]).** Não encontrei instância formal publicada com r ≥ 1.
- *Enunciado:* `BSDConjecture E₆`, isto é, ∃F inteira = L(E₆,s) em Re s>3/2 com ord₁F = 1 = posto.
- *Passos:* (i) FE da teta de ψ₆ = ψ₃₂·(χ₆∘N), via Q1, com ε=−1. Então `Λ₀_um` dá Λ(1) = (1+ε)∫ = 0, um **zero exato sem numérica**. (ii) L′(E,1) = 2Σ aₙE₁(2πn/√N)/n ≠ 0, com certificado de K termos e E₁(t) ≤ e^{−t}/t. (iii) posto ≥ 1 já está provado (`posto_R6`, P=(−3,9)). (iv) posto ≤ 1: mostrar #im φ ≤ 8 em `MordellWeilDois.phi` por obstruções locais em 2, 3 e ∞.
- *Progresso:* qualquer um de (i), (ii), (iv) isolado no kernel.

**Q3 (a, matemática nova) — Desigualdade 2-ádica de Selmer para os valores de Tunnell.**
- *Enunciado:* para n livre de quadrados ≡ 1,2,3 (8) com t(n) := 2Aₙ−Bₙ (ou 2Cₙ−Dₙ para n par) ≠ 0, vale v₂(Ш_an(n)) ≥ s₂(n) − 2. Aqui Ш_an(n) := t(n)²/(κ·4^{ω(n)}), com κ calibrado; s₂(n) = dim Sel₂(Eₙ), que é dado pela matriz de Monsky.
- *Contexto:* é consequência de BSD + Cassels–Tate. É uma afirmação **puramente combinatória** (formas ternárias × símbolos de Legendre).
- *Conhecido:* casos de famílias (Zhao; Li–Tian; Rhoades Thm 1.3–1.4 [Rho]; TYZ [TYZ]). Em geral não encontrei prova.
- *Progresso:* prova para ω(n) ≤ 2, ou contraexemplo numérico (T2), que refutaria BSD ou a calibração.

**Q4 (b + a) — Família infinita: ∀p ≡ 3 (8), BSD-posto para E_p: y²=x³−p²x (N=32p²).**
- Lado algébrico: posto 0 por 2-descida paramétrica (Genocchi), ao alcance de `MordellWeilDois`.
- Lado analítico: L(E_p,1) ≠ 0 é conhecido (Zhao/Li–Tian [Rho]).
- *Pergunta (a):* existe prova elementar dessa não anulação via a representação teta-produto de Q1? Por exemplo, uma congruência 2-ádica da soma finita, no espírito de `serie_re_pos`.
- *Valor:* seria a primeira família infinita de instâncias do Clay em Lean.

**Q5 (b, grande) — Ponte FLT → função L para curvas semiestáveis.**
- *Enunciado:* `IsModular W ∧ IsSemistableModel W ⇒ ∃F inteira, F = W.LSeries em Re s>3/2`.
- *Falta:* operadores T_n em Γ₀(N) com multiplicatividade; teoria de newforms (Atkin–Lehner–Li); o operador W_N e a FE autodual (a Mathlib só dá f ↔ f|S); nível = condutor e coeficientes nos primos ruins (Carayol, como hipótese explícita no início). O passo analítico isolado já é tratável: "newform f com f|W_N = −εf e coeficientes = aₙ(E) ⇒ `PonteModular E (2π/√N) ε`".
- *Primeiro passo barato:* clonar `anthropics/fermats-last-theorem` e extrair a definição exata de `IsModular` (nível? autoforma para quais T_ℓ?).
- *Valor:* torna a hipótese `Modularidade` da main um teorema para semiestáveis, por exemplo 11a, 37a e 389a.

**Q6 (b) — r_an = 2 formal para uma curva.**
- *Candidata:* E₃₄ `y²=x³−34²x`. Pela literatura clássica, 34 é o menor congruente ≡ 1,2,3 (8), com posto 2 e ε=+1; confirmar em T4.
- *Precisa de:* L(E₃₄,1)=0 exato, via a fórmula de Tunnell–Waldspurger (L ∝ (2C−D)², e 2C₃₄ = D₃₄ é contagem finita) ou via Manin–Drinfeld; L″(1)≠0 por certificado; posto = 2 por pontos + descida.
- *Valor:* primeiro "Clay com r=2" formal. A tratabilidade é baixa porque Tunnell/Waldspurger e os símbolos modulares não existem na Mathlib.

**Q7 (a, aberta de verdade) — Ш[p^∞] = 0 para um conjunto de primos de densidade positiva numa curva CM de posto 2.** É a versão "horizontal" de Banwait [Ban].
- *Enunciado:* para E = y²=x³−Dx de posto 2 e ε=+1, mostrar que v_𝔭(B(𝔭)) = 2 para uma proporção positiva de p split, onde B é a combinação explícita de três valores L de Hecke de peso 2p−1 em Banwait.
- *Valor:* altíssimo; seria o primeiro controle de Ш em posto ≥ 2 para infinitos p.
- *Tratabilidade:* baixa. T3 mede a heurística.

## 4. O que precisa ser criado

1. **`HeckeTheta`:** Grössencharaktere de K imaginário quadrático de tipo ∞ igual a 1, dados por (𝔣, χ). A teta é separada em cosets mod M; a FE vem de `jacobiTheta₂` e dos núcleos de Hurwitz par/ímpar mais `ZMod`/`AddChar`/`GaussSum`; o sinal W(ψ) é uma soma de Gauss finita. Generaliza `PonteModularCurva32`.
2. **Deuring por família:** a_p = ψ(𝔭)+ψ̄(𝔭) para y²=x³−n²x e y²=x³+k via `JacobiSum` (a Mathlib não tem CM/End(E)). O ATK já fez E32 com contagens de Gauss.
3. **Cota de Hasse** |a_p| ≤ 2√p na Mathlib, que fornece o `CotaCoef` (P2) genérico; e Hasse–Deligne |aₙ| ≤ d(n)√n.
4. **Numérica certificada:** cotas racionais de exp/E₁, somas parciais de K ≤ 10³ termos por `norm_num`/`decide`, e a fórmula de Mellin para Λ′(1) com ε=−1.
5. **Certificados de descida:** Sel₂ exato para uma curva dada (matriz de Monsky como `def` decidível) e "#im φ ≤ 2^{r+2} ⇒ posto ≤ r" sobre `MordellWeilDois`/`SelmerFinito`. Upstream de `MordellWeilGeral` para a Mathlib (ela ainda não tem Mordell–Weil).
6. **Ponte modular geral:** T_n em S_k(Γ₀(N)) (as bases são os anéis de Hecke de Birkbeck), newforms, W_N, FE autodual; port de `modularity_of_semistableModel` de 4.33.1 para 4.34.1.
7. **Zeros exatos em ε=+1:** símbolos modulares com Manin–Drinfeld, ou a fórmula de Tunnell–Waldspurger para Eₙ.
8. **Longo prazo:** pontos de Heegner, Gross–Zagier, sistemas de Euler (Kolyvagin; Rubin para CM). São indispensáveis para Ш, inclusive o Ш(E32)=0 que O7 exige em `formula_E32_iff`.

## 5. Testes baratos (não executados; cada um ≤ 20 min em 2 núcleos)

**T1 — Censo CM: módulo de separação e tamanho do certificado (cypari2 ≥ 2.15, numpy).**
- *Curvas:* para cada j CM, E₀ = `ellminimalmodel(ellinit(ellfromj(j)))` (para j=0 e 1728, usar y²=x³+1 e y²=x³−x), mais as torções `elltwist(E₀,D)` com D discriminante fundamental e |D| ≤ 200. Manter N ≤ 5000 e deduplicar por (N, primeiros 100 aₙ).
- *Dados por curva:* ε=`ellrootno`, r=`ellanalyticrank`, aₙ=`ellan(E,20000)`.
- *(i) Certificado:* c=2π/√N.
  - ε=+1, r=0: S_K = Σ_{n≤K} aₙe^{−cn}/n. Cauda T¹_K = e^{−c(K+1)}/(1−e^{−c}), usando |aₙ| ≤ n como hoje no ATK; cauda T²_K = Σ_{n>K} d(n)n^{−1/2}e^{−cn}. Kᵢ = min{K : |S_K| > Tᵢ_K}.
  - ε=−1, r=1: o mesmo com aₙE₁(cn)/n e E₁(t) ≤ e^{−t}/t.
- *(ii) Caractere:* identificar ψ_E com `gcharinit`/`gcharidentify` em `bnfinit(x²−d)` e checar `lfunan` igual por 5000 coeficientes. Registrar 𝔣, M = 2·(𝔣∩ℤ) e o número de classes (u,b) mod M com Φ≠0. *Fallback:* ajuste linear exato (sympy) de Φ:(ℤ/M)² → ℂ aos aₙ, n ≤ 3000.
- *Hipóteses:* K₂ ≤ 0,5·√N·log N; M = O(√N). *Informativo:* tabela de custo Lean por curva. Outliers de K/(√N log N) indicam L(E,1) anormalmente pequeno (Ш grande) dentro de famílias de torção, e indicam se a separação é sempre "pequena".
- *Tempo:* ~5–10 min.

**T2 — Tunnell × Monsky até X = 10⁶ (numpy, sieve; PARI só para calibrar).**
- *Contagens:* Aₙ, Bₙ, Cₙ, Dₙ por convolução esparsa (y²+2x² via `np.add.at`, depois 177 deslocamentos de 32z² etc.); t(n) como em Q3.
- *Selmer:* s₂(n) pela matriz de Monsky (apêndice de Heath-Brown, Invent. 1994), validada contra `ellrank(Eₙ)` para n ≤ 2000.
- *Calibração:* Ш_an(n) = L(Eₙ,1)#tors²/(Ω∏c_p) para 200 valores n ≤ 3000 (`lfun`, `ellglobalred`, `E.omega`); ajustar κ por classe mod 8 e paridade.
- *Hipóteses:* (H1) Ш_an(n) é quadrado inteiro, v₂(Ш_an) ≥ s₂−2 e tem a paridade certa; t(n)=0 ⇒ s₂(n) ≥ 4. (H2) A distribuição de v₂(Ш_an)/2 condicionada em s₂ e ω(n) converge para a de Smith/Swinnerton-Dyer–Kane.
- *Medições:* distância TV em X = 10⁴, 10⁵, 10⁶ (a taxa de convergência não está documentada até onde sei) e a fração de zeros t(n)=0 (Smith: → 0).
- *Informativo:* qualquer violação de H1 (após checar com PARI) refuta a calibração ou BSD 2-ádico; H1 sem exceção sustenta Q3.
- *Tempo:* < 8 min.

**T3 — Anomalias do regulador p-ádico em posto 2 (PARI).**
- *Curvas:* ~15 curvas de posto analítico 2 achadas por busca (aᵢ ∈ [−5,5], `ellanalyticrank`=2, N<5000, p.ex. 389a1 = [0,1,1,−2,0]), mais `y²=x(x+30)(x+2)`, E₃₄ e y²=x³+17.
- *Medida:* geradores por `ellrank`/`ellsaturation`. Para cada p bom e ordinário com 5 ≤ p ≤ 1000: R_p = `ellpadicregulator(E,p,6,gens)` e a(p) = [v_p(R_p) > valor modal]. Para N < 1000 e p ≤ 100: `ellpadicbsd(E,p,6)` → #Ш_p previsto, testando se é unidade p-ádica.
- *Hipótese:* P(a(p)=1) ≈ 1/p, independente, logo ~1,5 anomalias esperadas por curva em [5,1000]. Teste de Poisson no agregado.
- *Informativo:* excesso ou falta de anomalias põe a heurística em xeque. Um p com p | #Ш_p previsto é um candidato a Ш[p]≠0 em posto 2, raríssimo. Nas curvas CM, os primos split não anômalos são onde o critério (2) de Banwait (Q7) pode valer.
- *Tempo:* ~10 min.

**T4 — Convenções do ATK e calibração de Q2/Q6 (mpmath + PARI, < 2 min).**
- (a) E32: calcular Ω_ATK = ∫_{g>0} 2/√g com g = 4x³−4x (mpmath, 30 dígitos), c₂ (`ellglobalred`) e L(E,1) (`lfun`). Testar se L(E,1) = Ω_ATK·c₂/16, o que corresponde a #Ш=1. **Um fator 2 de discrepância indica erro de convenção em `FormulaRefinada`/`formula_E32_iff`.**
- (b) E₆ e E₃₄: N, ε, r_an, L′(1) ou L″(1)/2, Sel₂ (`ellrank`), geradores, regulador, e K mínimo do certificado como em T1.
- (c) C₃₄ e D₃₄ (Tunnell, n par) diretamente. Decide a viabilidade de Q2 e Q6.

## Fontes (abertas nesta pesquisa)
- [Clay] https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf
- [BSZ] https://arxiv.org/abs/1407.1826 · [Baker] https://mattbaker.blog/2014/03/10/the-bsd-conjecture-is-true-for-most-elliptic-curves/
- [Sk] https://annals.math.princeton.edu/2020/191-2/p01 · [BSTW] https://arxiv.org/abs/2409.01350 · [BT25] https://arxiv.org/abs/2506.03465v2
- [YZ] https://arxiv.org/pdf/2412.20078 (inclui a comparação com [SU14] Skinner–Urban)
- [CM] https://ar5iv.arxiv.org/html/1105.4018 · [Bob] https://antsmath.org/ANTSX/bober/paper.pdf
- [Ban] https://arxiv.org/abs/2609.08431 · [HYZ] https://ar5iv.labs.arxiv.org/html/2207.11904
- [Duj] https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html · [Mag] https://magica.com/news/claude-assisted-elliptic-curve-rank-record · [PPVW] https://ems.press/journals/jems/articles/16228
- [BT21] https://arxiv.org/pdf/2104.06732 · [TYZ] https://arxiv.org/abs/1411.4728 · [Dal] https://arxiv.org/pdf/2201.11071 · [Rho] https://arxiv.org/pdf/0706.4344
- [BBLL] https://msp.org/ant/2026/20-2/ant-v20-n2-p03-s.pdf · [SS] https://web3.arxiv.org/abs/2504.12295
- [AnFLT] https://www.anthropic.com/news/formalizing-fermats-last-theorem · [FLTgh] https://github.com/anthropics/fermats-last-theorem · [PP] https://github.com/anthropics/fermats-last-theorem/blob/main/PROOF-PATH.md
- [LS] https://arxiv.org/pdf/2503.00959v3 (Loeffler–Stoll), além da Mathlib local d13f23b (`EllipticCurve/LFunction.lean`, `Reduction.lean`, `Height/EllipticCurve.lean`, `GroupTheory/Descent.lean`, `ModularForms/LFunction.lean`, `Discriminant.lean`, `HeckeRing/Defs.lean`)
- Programa Rational Points 2025 (palestra de Angdinata sobre curvas elípticas em Lean): https://www.mathe2.uni-bayreuth.de/stoll/workshop2025/program-with-abstracts.pdf
