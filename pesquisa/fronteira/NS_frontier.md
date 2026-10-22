# NS — fronteira de pesquisa para a linha Clay (A) (ℝ³, f ≡ 0, dados de Schwartz) — 2026-10-21

**Resumo.** O ATK tem um ativo real: B3 (critério de Leray da enstrofia), existência local e unicidade no modelo fiel `modeloNS`, ~10k linhas Fourier, só no branch `atk/ns-b3-fourier-20261014`. O3 (`EnstrophyAPrioriBound modeloNS`) **não é uma redução**: dado B3 e uma unicidade na classe de Clay, O3 ⇔ (A). Em set/2026 surgiu uma explosão **forçada** com certificado Lean: OpenAI, alternativas (C)/(D). Ela ainda não tem revisão independente. Se for correta, mata toda rota para (A) que seja estável sob forçamento suave, inclusive forçamento criticamente pequeno (§2, B4). As apostas realistas são (b) de alto rendimento sobre a biblioteca Fourier existente (Lei–Lin crítico; critério de Serrin–Wiener) e (a) perguntas novas sobre "remover a força".

## 1. Estado da arte (outubro de 2026)

### 1.1 Teoria clássica e consolidada
- **Critérios.** Escauriaza–Seregin–Šverák (Russ. Math. Surveys 58:2, 2003): soluções em L^∞_t L³_x são suaves (via backward uniqueness). Seregin (2012, clássico): na explosão, ‖u(t)‖_{L³} → ∞. Tao (arXiv 1908.04958, 2019): versão quantitativa do ESS (cotas triplo-exponenciais) e taxa ‖u(t)‖_{L³} ≳ (log log log 1/(T*−t))^c ao longo de uma sequência de tempos.
- **Exclusões de cenários Tipo I.** Nečas–Růžička–Šverák (1996) e Tsai (1998), ambos clássicos: não há explosão autossimilar de Leray. Koch–Nadirashvili–Seregin–Šverák (Acta Math. 203, 2009): soluções axissimétricas com |u| ≤ C/r, ou Tipo I com cauda C/r, são limitadas. Logo uma explosão axissimétrica só pode ser **Tipo II** ("slow blow-up").
- **Dados pequenos críticos.** Kato e Koch–Tataru (clássicos). Lei–Lin (CPAM 64, 2011): ‖u₀‖_{χ⁻¹} = ∫|û₀(ξ)|/|ξ| dξ < ν dá solução global; o enunciado usa outra normalização de 𝓕. Em T³, Ambrose–Lopes Filho–Nussenzveig Lopes (PAMS 152, 2024).
- **Barreira de Tao.** Tao (JAMS 29, 2016; arXiv 1402.0290) construiu uma explosão para uma NS "média" que preserva a identidade de energia. Logo nenhuma prova de (A) pode usar só energia + estimativas harmônicas do termo não linear.
- **Não unicidade.** Buckmaster–Vicol (Ann. Math. 189, 2019): soluções fracas de energia finita não são únicas. Albritton–Brué–Colombo (Ann. Math. 196, 2022): não unicidade de Leray–Hopf **com força**, via um vórtice autossimilar instável. Cheskidov–Dai–Palasek (arXiv 2511.09556, nov/2025): em T^d, d ≥ 2, e para qualquer dado suave, existe solução suave fora de um instante T* com explosão Tipo I **instantânea**. A injeção de energia vem de número de onda infinito, do lado t ↓ T*. Isso dá não unicidade de soluções suaves, mas não contradiz (A)/(B).
- **Euler e evidência numérica.** Chen–Hou (arXiv 2210.07191, 2022; Parte II em MMS 23, 2025, com integração numérica rigorosa assistida por computador) provam explosão de Euler 3D axissimétrico **com fronteira**, dados suaves. Hou (FoCM 2022) dá evidência numérica, não prova, de comportamento potencialmente singular para NS axissimétrico com dados suaves. Wang, Lai, Gómez-Serrano, Buckmaster et al. (arXiv 2509.14185, set/2025) encontram soluções autossimilares **instáveis** com precisão próxima da dupla e conjecturam que, sem fronteira, as singularidades de Euler/NS são instáveis (codimensão finita).
- **Modelos de cascata (2026).** Palasek (arXiv 2605.13827): explosão num modelo de Obukhov viscoso com escalas superexponenciais e força suave **que se anula perto de T\***; janela α ∈ (2, 5/2] "candidata" para NS 3D. Cheskidov–Dai–Palasek (arXiv 2609.26790): o modelo misto DN–O com N_k = 2^k e **sem força** explode para α perto de 5/2 (prova adiada). O crescimento é apenas levemente Tipo II, com a norma crítica ~ (T−t)^{−0.020} em α = 2.4906. Os autores dizem que o mecanismo "lembra parcialmente" o da OpenAI, mas que lá "a força tem papel proeminente". Looi (Princeton, 2/abr/2026, só palestra): o Obukhov viscoso puro é globalmente regular para dados críticos ou mais regulares.

### 1.2 A onda de setembro de 2026: explosões forçadas com certificado Lean

**Córdoba–Martínez-Zoroa–Zheng (arXiv 2407.06776, 2024).** NS hipodissipativa, força em L¹_t C^{1,ε} ∩ L^∞_t L².

**Alpöge–Buckmaster (7–8/set).** Preprints e `tristanbuckmaster/fluid_lean` (commit d0124689, Lean 4.32.2, Mathlib 81a5d257). Provam explosão com força C^∞, de suporte compacto e com todas as derivadas limitadas até T, para:
- Boussinesq 2D, em duas variantes;
- Euler 3D;
- IPM em T², com Coiculescu (arXiv 2609.16470).

Segundo o README, há certificados de aritmética intervalar decididos pelo kernel, desafio Comparator e nenhum sorry fora de `Challenge.lean`; eu não reexecutei. A extensão para NS não foi publicada; Buckmaster diz que a verificação Lean está incompleta.

**OpenAI (8/set; repo `openai/NavierStokesAndEuler`, commit f9e8bc5b, 10/set).**
- **Enunciado.** O Thm 1.1 do PDF vale para todo ν > 0. Há u com u(·,0) = 0 e f ∈ C_c^∞(ℝ³×(0,∞)). Para t < 1, supp u(t) ∪ supp p(t) ⊂ K compacto e sup_{t<1} ‖u(t)‖₂ < ∞. A explosão é limsup_{t↑1} ‖u(t)‖_∞ = ∞. O resultado dá (C) e, pelo Cor. 10.6, (D).
- **Mecanismo.** No primeiro termo é axissimétrico e autossimilar, com ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h}, u_θ, u_z ≍ τ^{−1/2−h}, u_r = O(τ^{−1/2}), 0 < h < 1/100 e τ = 1 − t. Somam-se pulsos não axissimétricos "semeados por uma força exponencialmente pequena" e amplificados pelo cisalhamento de fundo. A força é o resíduo, e esse resíduo é **plano** (anula-se a toda ordem) no ponto singular.
- **Lean.** Toolchain v4.34.0-rc2. O diretório NavierStokes/ tem 708 arquivos e 412 645 linhas; Euler/ tem 211 578 linhas. O enunciado do Comparator foi copiado de formal-conjectures@8bf45ed, com os 3 axiomas padrão. Meu grep textual não achou `axiom`, `sorry` nem `native_decide` em NavierStokes/; não houve replay de kernel. O arquivo `R3FiniteEnergyComparison` prova a unicidade contra um competidor só de energia finita e pressão arbitrária.
- **Euler sem força.** Mesmo repo: Euler 3D **sem força**, dado C_c^∞ em ℝ³, ‖∇u‖ e ∫‖ω‖_∞ explodem.
- **Status em set/2026.** Nenhuma revisão por pares nem replay independente do Comparator foi relatado (remio, The Neuron). O Clay "não aceitou" e fará uma avaliação "deliberadamente sem pressa" (Bridson). A OpenAI não pedirá o prêmio. Fefferman (Quanta): "thrilled that the problem was solved". Há disputa de crédito com Buckmaster.
- **Observação ATK.** `atk-ns` fixa 8937a8f (8/set). Esse commit existe no GitHub, mas difere do main atual em 188 arquivos (+25k linhas); os arquivos do ComparatorChallenges são idênticos.

### 1.3 O que (C) forçado diz, e não diz, sobre (A)
1. **Lógica.** (C) não implica ¬(A), e o portão `NSRefutacao` do ATK não fecha com ele. Se o Clay aceitar (C), o *prêmio* fica resolvido e (A) continua aberto como matemática.
2. **Auditoria de escala.** Contas minhas, sobre as assintóticas acima:
   - ‖u‖_{L³} ~ τ^{−4h/3} → ∞, compatível com ESS/Seregin/Tao;
   - enstrofia ~ τ^{−1/2−3h}, acima da taxa de Leray τ^{−1/2} e integrável;
   - ∫‖u‖²_∞ e ∫‖ω‖_∞ divergem;
   - todas as integrais de Serrin divergem com margem ∝ h;
   - a dissipação escalada de CKN no raio √τ é ~ τ^{−3h};
   - é Tipo II (‖u‖_∞√τ ~ τ^{−h}), coerente com KNSS;
   - Re_loc = Uℓ_r/ν ~ τ^{−h} → ∞, ou seja, o núcleo é dominado por inércia e "tipo Euler".

   É uma explosão **marginalmente supercrítica**, como o modelo DN–O (expoente 0.020).
3. **Onde está a lacuna para ¬(A).** Existe uma solução aproximada **não forçada** com resíduo plano no ponto singular, mas O(1) longe dele e nas fases iniciais (é a força que cria o fluxo a partir do repouso). Refutar (A) seria "exactificar", isto é, trocar cada semente forçada por sementes nos dados (Q6). A experiência de Wang et al. sugere codimensão finita por estágio, mas aqui há infinitos estágios.
4. **Para provar (A).** Avaliação minha: as ferramentas de rigidez da equação exata — Liouville (KNSS), unicidade retrógrada e Carleman (ESS/Tao) — não são refutadas pelo contraexemplo forçado, porque dependem da equação exata. Ferramentas de "desigualdade funcional + energia" morrem (B2–B4).

## 2. Barreiras e no-go (e rotas do ATK que já excluem)
- **B1 Supercriticalidade.** Os controles coercivos conhecidos são supercríticos: a energia escala como λ^{−1}, e ∫∫|∇u|² também. A teoria global só existe em normas críticas pequenas (L³, Ḣ^{1/2}, BMO⁻¹, χ⁻¹). O3 pede exatamente cruzar esse vão. A rota G5 do ATK (S ≤ θνz + Cy²) já morreu por escala (`ns_19_false`).
- **B2 Tao 2016.** Desigualdades diferenciais escalares y' ≤ F(y), com constantes que dependem só da energia e de estimativas harmônicas, não fecham (A). O próprio `explosao_comparacao` do ATK é uma miniatura disso. **A família NSPequeno/NSExplosao/Riccati está morta** como rota para O3.
- **B3 Explosão forçada.** Condicional à correção da OpenAI. Nenhuma cota a priori da forma enstrofia ≤ Φ(u₀, normas de f) vale para f ∈ C_c^∞. **Toda prova de O3 que funcione também com força é falsa.**
- **B4 Robustez crítica.** Corolário meu de 1.2 + escala (u_λ = λu(λx, λ²t), λ = τ₀^{−1/2}), com u₀ = u(t₀) e τ₀ = 1 − t₀ → 0. Para todo ε > 0 há:
  - dado C_c^∞ com energia ≤ Cτ₀^{1/2} < ε;
  - força com ‖f‖_{L¹_t L³_x} ≤ Cτ₀ < ε e ‖f‖_{L¹_t L^∞_x} ≤ Cτ₀^{1/2} < ε;
  - explosão no tempo 1.

  Só ‖u₀‖_{L³} ~ τ₀^{−4h/3} é grande, como exige o resultado de Kato com dado e força pequenos. Logo (A), se verdadeiro, não é estável sob forçamento criticamente pequeno.
- **B5 Não unicidade** (BV, ABC, CDP 2025). Rotas via compacidade de soluções fracas + unicidade não dão regularidade. O ATK já trabalha na classe suave, o que está certo.
- **B6 Explosão tem de ser Tipo II.** Vem de NRS/Tsai/KNSS e de "L³ → ∞". Uma prova de (A) precisa excluir Tipo II marginal (h → 0), justamente o regime da construção OpenAI e do DN–O.
- **B7 Evidência contrária.** Numérica de Hou; Euler sem força da OpenAI (se correto); explosão sem força no modelo DN–O. Não há evidência séria a favor de (A) além da ausência de contraexemplo.

## 3. Perguntas atacáveis (ordenadas por valor × tratabilidade)
Normalização ATK: v = û = ∫e^{−2πix·ξ}u, c = 4π²ν, L1(f) = ∫|f|, χ^s(f) = ∫|ξ|^s|f|.

**Q1 (b) — Lei–Lin crítico no modelo genuíno.** [valor alto × tratabilidade alta]
- *Enunciado:* ∀ν > 0, ∀u₀ ∈ 𝓢(ℝ³,ℝ³) com div u₀ = 0 e χ^{−1}(û₀) < c/(2π) = 2πν ⇒ ∃U P, `SolucaoGlobal ν u₀ U P`.
- *Derivação na normalização ATK:* d/dt χ^{−1} ≤ −cχ^{1} + 2π(L1)² ≤ −(c − 2πχ^{−1})χ^{1}, usando L1² ≤ χ^{−1}χ^{1}. É preciso conferir a constante contra a normalização de Lei–Lin.
- *Por quê:* é a primeira instância **não trivial** de `ClayStatementA` num aberto invariante por escala. Esse aberto contém dados de energia e enstrofia arbitrariamente grandes. Substitui o vácuo de NSPequeno.
- *O que já se sabe:* a matemática (2011), e o ATK já tem `nl`, `Bq`, `kernel_bound`, pesos e a solução maximal com B3.
- *Progresso:* um teorema com os 3 axiomas, passando por Q2 (∫L1² ≤ χ^{−1}(0)·∫χ^{1} < ∞).
- *Risco técnico:* |v(ξ,t)| não é diferenciável em v = 0. Use a forma de Duhamel ou √(|v|² + ε²).

**Q2 (b) — Critério de Serrin–Wiener e taxa de Leray.** [médio × muito alto]
- *Enunciado:* se `¬GlobalSmooth`, então ∫₀^{T*} L1(v(t))² dt = ∞.
- *Prova:* em `enstrofia_deriv_le`, tome μ = c/(2πL1). Isso dá Q1' ≤ (2/ν)·L1²·Q1; por Gronwall com coeficiente variável e depois `cota_continua` + `explosao_peso4`, sai o critério.
- *Segunda parte:* com um Picard em L¹_ξ, que usa o mesmo `kernel_bound`, a taxa L1(v(t)) ≥ c₀√ν (T*−t)^{−1/2}.
- *Por quê:* é o primeiro critério **crítico** do ATK (L²_t de 𝓕L¹ é invariante por escala), fortalece B3 e é pré-requisito de Q1.
- *Progresso:* um arquivo `NSSerrin.lean` com menos de 400 linhas (teste T3).

**Q3 (a) — Barreira de forçamento crítico pequeno (B4) como teorema.** [médio-alto × alto]
- *Enunciado:* para todo ε há (u₀, f) C_c^∞ com ‖u₀‖₂ + ‖f‖_{L¹_t(L³∩L^∞)} < ε e explosão em t = 1.
- *Corolário:* não existe Φ com enstrofia ≤ Φ(‖u₀‖₂, ‖f‖_{L¹(L³∩L^∞)}).
- *A medir:* inf ‖u₀‖_{L³}/ν nessa família, contra a constante ε₀ de Kato.
- *O que já se sabe:* nada publicado nas fontes vistas; é um corolário de escala da OpenAI.
- *Progresso:* uma nota de 2 páginas e um enunciado Lean condicional a `navier_stokes_breakdown_R3`.

**Q4 (a) — Constante ótima de Lei–Lin.** [baixo-médio × alto]
- *Enunciado:* κ* = inf_u χ^{−1}(u)·χ^{1}(u)/N(u), com N a parte não linear de d/dt χ^{−1}. Lei–Lin dá κ* ≥ 1. É verdade que **κ\* > 1**?
- *Heurística:* em uma tríade, |q·û_p| ≤ |q||û_p| e û_p ⊥ p. A igualdade L1² = χ^{−1}χ^{1} exige uma casca única, onde as tríades são equiláteras e o fator vale ≤ √3/2. Isso sugere κ* ≥ 2/√3 em configurações de uma casca.
- *Por quê:* qualquer κ* > 1 provado amplia Q1 para χ^{−1} < κ*·2πν. É matemática nova, pequena e formalizável em seguida. Não vi isso nas fontes. Teste T2.

**Q5 (b) — Modelo forçado no ATK + importação do (C).** [médio × médio]
- `NSModelF`, com decaimento (5) do Clay e iff de fidelidade com `NavierStokesExistenceAndSmoothnessRn`.
- B3 forçado: Duhamel com f na biblioteca Fourier.
- `¬EnstrophyAPrioriBound_F`, condicional ao (C) importado no commit f9e8bc5b.
- Comparação só de energia na classe de Clay, portada de `R3FiniteEnergyComparison`. Isso também fecha a direção (A) ⇒ O3, hoje dependente de `NSUnico`, que exige enstrofia finita.

**Q6 (a) — Singularidade local sem força.** [muito alto × baixo-médio]
- *Enunciado:* existe f ∈ C_c^∞ com **f ≡ 0** num cilindro parabólico Q_r(x*, T*) tal que a solução forçada explode em (x*, T*)?
- *O que já se sabe:* hoje f é só plana nesse ponto, e não há resultado nas fontes.
- *Por quê:* isola (A). Se a resposta for sim, a teoria local (CKN, ESS local, KNSS locais) não fecha (A), e uma prova teria de usar o decaimento em ∞ / Schwartz.
- *Progresso:* empurrar o resíduo para fora de Q_r com correções do "heat exterior" ou de tipo Bogovskii. Alternativa: uma obstrução local de Liouville.

**Q7 (a) — Remoção da força (exactificação), com a subpergunta do orçamento de sementes.** [máximo × baixo]
- *Enunciado:* para u_app da OpenAI, existem t₀ < 1 e w₀ ∈ C_c^∞ pequeno tais que a solução **não forçada** a partir de u_app(t₀) + w₀ explode? Isso equivale a refutar (A) por essa via.
- *Subpergunta quantitativa:* uma semente co-móvel no colapso sofre amortecimento viscoso exp(−∫νk(t)²dt) ≈ (τ_j/τ₀)^{Cν}, uma perda **polinomial**, porque k(t) ~ 1/ℓ_r(t) ~ τ^{−1/2}. Se a amplitude exigida no estágio j for só exp(−C·j), as sementes podem ser pré-carregadas no dado, e o problema se reduz a estabilidade de codimensão finita por estágio.
- *Progresso:* um "livro-razão de sementes" com os parâmetros σ_j, q^{2nh} do artigo (seções 5–9), ou uma contra-heurística.

## 4. O que precisa ser criado
- **Higiene.** Fazer o merge do branch B3-Fourier no kernel novo (PR #55 não tem NSCriterio) e marcar B3 como provada em `obligations.json`. Aposentar `NSReducao.b3_de_classicos`. Fixar a OpenAI no commit f9e8bc5b.
- **Biblioteca χ^s.** Momentos de Fourier χ^s para s ∈ [−1, 2], com |ξ|^{−1} localmente integrável em ℝ³. Lemas: interpolação L1² ≤ χ^{−1}χ^{1}, Young L¹ * L¹ e um Picard em 𝓕L¹ (taxa de Q2).
- **Gronwall com coeficiente variável.** y' ≤ a(t)y com a ∈ L¹ ⇒ y ≤ y(0)e^{∫a}. A Mathlib tem `gronwallBound` para K constante; se faltar, levar para a Mathlib.
- **Simetrias de `SolucaoLocal`/`SolucaoGlobal`.** Escala (u_λ, p_λ), translação e rotação, com teoremas de invariância. Base para B4, para taxas e para qualquer enunciado crítico.
- **NS forçado.** `NSModelF`, Duhamel com f, fidelidade vs Comparator e comparação só de energia (Q5).
- **Longo prazo, (b) pesado.** Normas Lᵖ das fatias e Sobolev/GNS em ℝ³ (a Mathlib tem GNS para C¹ compacto). Riesz/Calderón–Zygmund para a pressão, que não está na Mathlib. Soluções suaves locais com desigualdade local de energia. Isso é pré-requisito de CKN e ESS.
- **Numérica certificada no kernel.** Aritmética intervalar com certificados racionais, como em `euler-blowup/Num` de Alpöge–Buckmaster. Infraestrutura para estabilidade assistida por computador no estilo Chen–Hou.

## 5. Testes baratos (especificação; não executados)
**T1 — Auditoria de escala da explosão OpenAI e janela de expoentes.** Python/sympy, menos de 2 min.
- *Entrada:* ℓ_r = τ^a, ℓ_z = τ^b, U_θ = U_z = τ^{−c}, U_r = τ^{−d} com d = c + b − a (incompressibilidade U_r/ℓ_r ≍ U_z/ℓ_z), ν = 1. Ponto OpenAI: (a, b, c) = (1/2, 1/2 − h, 1/2 + h), com h simbólico em (0, 1/100).
- *Cálcular os expoentes de τ de:* energia do núcleo, ‖u‖_∞, ‖u‖_{L³}, enstrofia e ∫enstrofia, ‖ω‖_∞ e ∫‖ω‖_∞, ∫‖u‖_{L^q}^p para 2/p + 3/q = 1, q ∈ {4, 6, 9, ∞}, a quantidade CKN r^{−1}∫∫_{Q_r}|∇u|² em r = √τ, Re_loc e a razão de aspecto.
- *Verificar com `solve_univariate_inequality`:* energia limitada, Leray (‖u‖_∞ ≳ τ^{−1/2}), L³ → ∞, BKM, Serrin, CKN ≥ ε e Tipo II.
- *Calcular também:* os expoentes de B4 após a escala λ = τ₀^{−1/2}, para ‖u₀‖₂², ‖f‖_{L¹L³}, ‖f‖_{L¹L^∞} e ‖f‖_{L¹Ẇ^{k,p}} com k ≤ 3, p ∈ {3, ∞}.
- *Varredura:* grade (a, b, c) ∈ [0.3, 1]³ com passo 0.005, mesmas condições, mais balanço ∂_t ≲ inércia (c ≥ 1 − a) e viscosidade ≲ inércia (c ≥ a).
- *Hipótese:* toda janela viável tem Re_loc → ∞ e a margem Tipo II pode ir a 0.
- *Informativo:* qualquer condição violada no ponto OpenAI falsifica a assintótica anunciada ou revela um desvio de enunciado.

**T2 — κ\* de Lei–Lin em T³ (Q4).** numpy/scipy, ≤ 15 min.
- *Campos:* û_k ∈ ℂ³, k ∈ ℤ³∖0, |k_i| ≤ M com M ∈ {2, 3}, k·û_k = 0, û_{−k} = conj(û_k).
- *Fórmulas:* A_s = Σ|k|^s|û_k| e G_k = −iP_k Σ_{p+q=k}(k·û_p)û_q, por convolução direta ou FFT com padding. Depois N = Σ_{û_k≠0}|k|^{−1}Re⟨û_k/|û_k|, G_k⟩ + Σ_{û_k=0, k∈S+S}|k|^{−1}|G_k|; a segunda soma é a derivada à direita nos modos nulos e não pode ser omitida.
- *Otimização:* minimizar ρ = A_{−1}A_1/N sobre N > 0. ρ é invariante por u ↦ su e por k ↦ mk.
- *Busca:* L-BFGS-B com gradiente numérico e 20–50 reinícios; também famílias analíticas de tríades e quartetos (≤ 36 parâmetros), Nelder–Mead.
- *Saída:* o menor ρ por M e a estrutura do minimizador (número de cascas, ângulos das tríades).
- *Leitura:* ρ_min ≥ 1.1, estável em M, apoia κ* > 1 e motiva a prova. ρ_min → 1 indica Lei–Lin ótimo para este argumento.

**T3 — Viabilidade Lean de Q2 no branch `atk/ns-b3-fourier-20261014`.** ≤ 20 min.
- *Compilar:* só o fecho de imports de `ATK.NSContinua` (NSFourierBase, NSPicard, NSRegular, NSEnergia, NSContinua, cerca de 3.5k linhas).
- *Arquivo `NSSerrin.lean`, passo 1:* enunciar com `sorry` o teorema abaixo e checar a elaboração.
  `serrin_Q1 (h : SolF c T v) : ∀ t ∈ Icc 0 T, Q 1 (v·t) ≤ Q 1 (v·0) * exp ((2/ν) * ∫ s in 0..t, L1 (v·s)^2)`
- *Passo 2:* provar, a partir de `enstrofia_deriv_le` com μ = c/(2π·L1), separando o caso L1 = 0, mais `hasDerivWithinAt_Q` e um fator integrante.
- *Registrar:* lemas faltantes (continuidade de t ↦ L1, Gronwall variável) e o tempo de build.
- *Hipótese:* a biblioteca atual basta para um critério crítico em menos de 400 linhas.

**T4 — Modelo DN–O sem força: janela de α e expoente Tipo II.** numpy, ≤ 20 min.
- *Equação (12) de CDP 2026:* X_k' = −νN_k²X_k + η(N_{k−1}^αX_{k−1}² − N_k^αX_kX_{k+1}) − N_k^αX_{k+1}² + N_{k−1}^αX_{k−1}X_k, com X₀ = X_{K+1} = 0.
- *Parâmetros:* ν = 1, N_k = 2^k, η ∈ {10⁻⁵, 10⁻³, 10⁻²}, K ∈ {30, 40, 50}. Dados em k ≤ 3 com amplitude A ∈ {10, 10², 10³}.
- *Integrador:* ETD-RK4 (dissipação exata) com dt = 0.1/max_k N_k^α|X_k|; verificar a identidade de energia.
- *Varredura:* α ∈ {2.05, 2.10, …, 2.60}.
- *Medidas:*
  - tempo T_K em que Φ = sup_k N_k^{α−2}|X_k| atinge 10⁶; T_K → T∞ < ∞ quando K cresce é o sinal de explosão;
  - expoente β com Φ ~ (T−t)^{−β}; a sanidade é β ≈ 0.020 em α = 2.4906.
- *Hipóteses:* (i) explosão só numa vizinhança estreita de 5/2 (o ε do Thm 1.10) ou em todo (2, 5/2]; (ii) β(α) → 0 em algum α_c, o análogo do h → 0 da OpenAI.
- *Por quê:* é um laboratório barato de "explosão sem força" com identidade de energia e escala de NS, justamente a classe que a barreira de Tao não exclui.

## Fontes (URLs abertas nesta pesquisa)
- https://openai.com/index/navier-stokes-solution/ · https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
- https://github.com/openai/NavierStokesAndEuler (clonado: f9e8bc5b; 8937a8f obtido por fetch) · https://github.com/tristanbuckmaster/fluid_lean (clonado: d0124689)
- https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/ · https://unite.ai/openai-says-internal-ai-system-resolved-the-navier-stokes-problem
- https://quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908 · https://www.implicator.ai/clay-institute-navier-stokes-openai-proof-claim.md
- https://www.remio.ai/de/post/openai-navier-stokes-proof-adds-lean-4-but-verification-is-not-finished · https://theneuron.ai/news/inside-openais-navierstokes-claim-the-proof-the-ai-effort-and-the-credit-fight/
- https://zeli.app/story/49607944 · https://officechai.com/ai/terrance-tao-calls-buckmaster-alpoges-fluid-dynamics-proofs-a-remarkable-achievement-says-could-help-solve-navier-stokes/ (paráfrases de Tao, de segunda mão)
- https://arxiv.org/abs/2407.06776v1 · https://arxiv.org/pdf/2609.16470 · https://arxiv.org/abs/2511.09556 · https://arxiv.org/pdf/2609.26790 · https://arxiv.org/pdf/2605.13827
- https://arxiv.org/pdf/2209.10203 · https://arxiv.org/pdf/2609.21312 · https://www.math.princeton.edu/node/19357
- https://mathnet.ru/eng/rm609 · https://arxiv.org/abs/1402.0290v1 · https://arxiv.org/pdf/1908.04958
- https://arxiv.org/abs/2210.07191v2 · https://authors.library.caltech.edu/records/n8p3w-pkt03 · https://authors.library.caltech.edu/records/13ysw-25660 · https://arxiv.org/abs/2509.14185
- https://annals.math.princeton.edu/2019/189-1/p03 · https://annals.math.princeton.edu/2022/196-1/p03
- https://pdf.arxiv.org/pdf/0709.3599 · https://experts.umn.edu/en/publications/liouville-theorems-for-the-navier-stokes-equations-and-applicatio/
- https://arxiv.org/pdf/1312.2136 (Lei–Lin citado) · https://doi.org/10.1090/proc/16615
- Bloqueados, não lidos: post de Tao (terrytao.wordpress.com/2026/09/07/…) e o PDF oficial do Clay (claymath.org/…/navierstokes.pdf). O texto de (C)/(D) foi lido na cópia do formal-conjectures dentro do repo da OpenAI.
- Clássicos citados sem URL: Leray 1934, CKN 1982, NRS 1996, Tsai 1998, Kato 1984, Koch–Tataru 2001, Seregin 2012.
