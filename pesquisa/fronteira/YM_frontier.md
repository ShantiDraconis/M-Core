# YM (existência e lacuna de massa): fronteira de pesquisa, 2026-10-21

**Diagnóstico.** O corpus não tem nenhum resultado sobre teoria de calibre. Os 7 itens P1 são Ising 1D (matriz 2×2).
`YMNucleo` é sombra do enunciado do Clay: tem testemunha candidata, o `:φ²:` do campo livre massivo, já registrada em `StatusFinal`.
O fato externo que mais pesa: **já existe em Lean 4 uma prova sem sorry e sem axiomas de projeto** de lacuna para TGR U(n)
(clustering exponencial) em acoplamento forte: `mrdouglasny/lgt`, maio/2026. O ATK está atrás do estado da arte *formal*. A rota honesta é portar, auditar e estender esse código, e não reinventá-lo.

## 1. Estado da arte (out/2026)
**Contínuo 4D.**
- Enunciado do Clay (Jaffe–Witten): para todo G compacto simples, uma YM quântica não trivial em ℝ⁴, com axiomas ≥ Wightman/OS e Δ>0 [Wiki/Clay].
- Nenhuma teoria de calibre 4D foi construída. Summers (2016): "resultados definitivos só em d<4".
- Balaban (1983–89): estabilidade UV da TGR em volume finito, d=3,4. Não dá volume infinito, nem OS no contínuo, nem gap (exposição de Dimock, arXiv 1108.1335).
- Magnen–Rivasseau–Sénéor (mp_arc 92-38): funções de Schwinger de SU(2) 4D com cutoff IR fixo, setor topológico trivial, dois calibres.
- Faria da Veiga–O'Carroll (2205.07376): cotas de estabilidade termodinâmica+UV de Z para U(N), d≤4. É nível de energia livre, não de correlações.

**2D: resolvido.**
- Dang–Nohra (2602.08591, fev/2026): a medida de YM em superfícies compactas é limite universal de Wilson/Villain/Manton.
- Chevyrev–Shen (2302.12160 v3, abr/2026): medida 2D invariante e única para a dinâmica de Langevin. Dahlqvist (2603.11374): N→∞ em gênero ≥2.
- Com c.c. livre as plaquetas são i.i.d. Daí sai uma lei de área exata para todo β. Não há graus propagantes, então o "gap" é trivial.

**3D.**
- CCHS (2201.03487): soluções locais de YMH estocástico e renormalização covariante. Chevyrev–Shen (ARMA 250:11, 2026) provam a unicidade dessa renormalização.
  Os dois trabalhos dizem que **continua aberta** a construção da medida de YM 3D, mesmo em T³.
- Cao–Chatterjee: espaço de estados 3D (CMP 405, 2024). Chatterjee (2602.00436, jan/2026): prova curta de confinamento logarítmico para TGR 3D com U(1) central (inclui U(N)):
  |⟨W⟩| ≤ n·exp{−c(1+nβ)⁻¹·T·log(R+1)}. Göpfert–Mack (Villain) já provaram que U(1) 3D confina para todo β.

**Rede, acoplamento forte.**
- Osterwalder–Seiler 1978: positividade de reflexão (RP), lei de área e gap para β ≲ c(d)/N.
- Shen–Zhu–Zhu (2204.12737): Langevin + Bakry–Émery dão LSI, medida de volume infinito única e gap.
  Vale para SU(N) com |β|<1/(16(d−1)) (escala βN) e para SO(N) com (N−2)/(32N(d−1)).
- Nissim (2510.22788, out/2025): o mesmo para U(N), via ambiente aleatório U(1)×SU(N). Bakry–Émery falha ali porque Ricci não é uniforme.
- Cao–Nissim–Sheffield (2505.16585, v3 set/2025): lei de área U(N) para β≤β₀(d) **uniforme em N** (laços mestres, fusão truncada); ver também 2509.04688 (PAMS).
- Chatterjee (2006.16229, CMP 2021): simetria de centro não quebrada implica confinamento. Decaimento exponencial sob c.c. arbitrárias mais centro não trivial implica que ela não quebra.

**Rede, acoplamento fraco.**
- Adhikari–Cao (Ann. Probab. 53, 2025), G finito, d=4:
  |Cov(f₁,f₂)| ≤ 4(4096|G|²)^{|B₁|+|B₂|}‖f₁‖‖f₂‖e^{−(β/2)Δ_G(L−1)} para β ≥ (114+4log|G|)/Δ_G, uniforme no volume.
  Para ℤ₂ isso dá β≥58.4. É gap sem confinamento. ℤ₂ 4D: Chatterjee (1811.09770) obtém ⟨W_γ⟩ ≈ exp(−2ℓe^{−12β}), lei de perímetro.
- U(1) 4D: fase de Coulomb sem gap (Fröhlich–Spencer 1981). Ito–Seiler usam essa transição como teste negativo.
- **SU(N) 4D com β intermediário ou grande: nada rigoroso.**

**Formal (Lean).**
- Douglas–Hoback–Mei–Nissim (2603.15770, mar/2026): o campo livre 4D satisfaz os axiomas de Glimm–Jaffe, feito com assistentes de IA.
- `pphi2`: P(φ)₂, OS0–OS4 em curso, 26 axiomas de projeto (2026-10-08). Não faz a reconstrução OS.
- **`lgt`** (Douglas–Rajasekaran, PR #2 de 2026-05-04, commit b8793cc). Teoremas `ym_mass_gap_exponential_decay` e `ym_mass_gap_rate_exists`.
  Hipóteses: U(n) Wilson em (ℤ/N)^d, d≥2, N≥3, β<1/(32n(d−1)), ação βΣ(n−ReTrU_p).
  Conclusão: |⟨ReTrU_p;ReTrU_q⟩| ≤ 32n²/(1−α)·α^{(dist−1)/2}, com α=8(d−1)(1−e^{−4nβ}).
  Usa só propext/choice/Quot.sound. Roda em Lean v4.30; o README diz que falha em v4.33–v4.36-rc1. O repositório tem AGENTS.md e CLAUDE.md.
- O que li no fonte de `lgt`:
  - `HasHaarProbability` só exige medida de probabilidade, sem invariância. O teorema é um fato genérico de alta temperatura e não usa a estrutura de calibre.
  - O `∃ m` vem depois de N. A uniformidade em volume vale de fato (m=−½log α), mas não está enunciada.
  - "Gap" significa clustering de ReTrU_p, não lacuna espectral de T.
  - Não há lei de área, RP nem reconstrução. `MassGap2D` está parcial e a ponte RG tem `sorry`.

**Alegações 2025–26 (nenhuma aceita).**
- Nye (Int. J. Topology, fev/2025): circular segundo análise crítica, porque assume a lei de área.
- Jacobsen (2506.00284, physics.gen-ph). Faizal–Shabir (2606.19362, hep-lat, jun/2026): polímeros + RG + compacidade, "definitivo", sem revisão.
- Preprints no Zenodo (out/2026). No Kalshi, "YM próximo Clay antes de 2045" subiu cerca de 20 pontos em 17/10/2026 sem matemática nova.
  O mesmo artigo atribui a "Cao e Chatterjee" um gap no regime de 't Hooft em fins de 2025. **Não confirmei**; o que encontrei é Nissim 2510.22788 (só acoplamento forte).
- Faria da Veiga–O'Carroll (2509.03513 v2, jan/2026): conjugação de carga e Elitzur rigorosos. O gap **não** é provado.

## 2. Barreiras e no-go
1. **Invisibilidade perturbativa.** Δ ∝ a⁻¹exp(−1/(2b₀g²)), com b₀=11N/(48π²). Isso não é analítico em g=0, então toda ordem finita dá zero.
2. **Raio finito dos métodos convergentes** (Dobrushin, polímeros/Kotecký–Preiss, Bakry–Émery, laços mestres). Todos exigem β<β₀(d,N) fixo.
   O contínuo exige β(a)→∞, com 1/g²≈(11N/24π²)log(1/aΛ). Nenhum desses métodos chega ao contínuo; a rugosidade limita as expansões fortes.
   O `lgt` certifica SU(2) em d=4 só até β=1/192.
3. **Contraexemplos abelianos.** U(1) 4D tem fóton sem massa; ℤ_N 4D tem fase desconfinada.
   Todo argumento "para todo β" precisa usar a não comutatividade. Essa é a objeção de Ito–Seiler a Tomboulis (2007).
4. **Gap ≠ confinamento.** G finito tem gap em acoplamento fraco (Adhikari–Cao) com lei de perímetro (Chatterjee).
   O ℤ₂ 2+1D desconfinado é uma ordem topológica com gap. Lei de área ⇒ gap não é teorema.
   Por isso `wilson_area_law` (que é renomeação de Ising) não ajuda nem O8 nem B7.
5. **Elitzur e Gribov.** Observáveis não invariantes têm média nula, e não existe fixação global de calibre contínua.
   O gap tem de ser enunciado no setor invariante. Rotas via A_μ fixado globalmente ficam excluídas.
6. **Trivialidade 4D.** φ⁴₄ e Ising 4D crítico dão limites gaussianos (Aizenman–Duminil-Copin, Annals 194, 2021).
   Não trivialidade em 4D só pode vir de liberdade assintótica. Nenhuma QFT 4D com matriz S não trivial foi construída.
7. **Barreira definicional (O8).** `NaoTrivial := ¬Gaussiana` aceita o `:φ²:` livre, que tem lacuna 2m. Provar `YMNucleo` seria matemática dos anos 1960, não YM.
8. **Volume finito é vazio.** Para G finito, T é positiva entrada a entrada no setor invariante. Por Perron–Frobenius, gap>0 para todo L e todo β.
   O conteúdo real é a **uniformidade em L**.
   Rotas do corpus que ficam excluídas: `YMModel` paramétrico, Ising 1D, `wilsonLoop := correl` e `massa_tende_zero` (sem calibre).

## 3. Questões atacáveis, por valor × tratabilidade ([F] formalização de matemática conhecida, [N] matemática nova)
**Q1 [F] Portar, auditar e endurecer `lgt` dentro do ATK.**
- Alvo: ∃ m>0, C, ∀N≥3, ∀p,q: |⟨ReTrU_p;ReTrU_q⟩_{N,β}| ≤ C·e^{−m·dist}.
- Para G⊂U(n) com Haar invariante; mais a versão `Fintype` (somas finitas) e SU(n) via `HasGaugeTrace`. Constante exata para ℤ₂: β<½artanh(1/(3(d−1))), ou seja 0.0841 (d=3) e 0.0558 (d=4). O `lgt` dá 0.0156 e 0.0104 (fator 5.4).
- Por que importa: é o primeiro resultado de calibre genuíno no kernel. Progresso = compilar em 4.34.1 e provar o corolário uniforme.

**Q2 [F] RP e matriz de transferência (B7 na rede).** Toro (ℤ/N)^d com N par:
- (a) Wilson é RP em relação a planos por sítios e por elos.
- (b) T é autoadjunto, com 0≤T≤λ₀, em L²(G^{elos espaciais})^{inv}.
- (c) Clustering com taxa m ⇒ spec(T)∖{λ₀} ⊂ [0, λ₀e^{−m}], uniforme em N, com vácuo único (Osterwalder–Seiler).
- Isso converte o `lgt` numa **lacuna espectral de Hamiltoniano**, o análogo exato de `GapMassa`. Fazer primeiro G finito (matrizes), depois G compacto (operador de Hilbert–Schmidt).

**Q3 [F + N leve] Mapa certificado de gap para ℤ₂ via dualidade.**
- Ferramentas: dualidade de Wegner em 4D (autodual, tanh β*=e^{−2β}) e Kramers–Wannier em 3D (TGR ↔ Ising).
- Com acoplamentos locais inomogêneos: ⟨σ_p;σ_q⟩_β = (sinh 2β)^{−2}⟨σ*;σ*⟩_{β*} para p≠q.
  Caixa com c.c. livre corresponde ao dual com c.c. fixa; no toro aparecem setores torcidos.
- Combinado com Dobrushin exato, dá gap uniforme em L:
  - d=4: β<0.0558 ou β>1.4436. Adhikari–Cao só cobrem β≥58.4 para ℤ₂.
  - d=3: β<0.0841 ou β>0.8814 (Dobrushin de Ising 3D com β̃<¼ln2). A transição está em 0.7614.
  - O 3D completo para β≠0.7614 deve sair de DGR 2019 + ABF/DT, mas é pesado e falta verificar a transferência das correlações de energia.
- Provavelmente é folclore como fato, mas é novo como teorema formal com constantes. Aberto: fechar a janela [0.0558, 1.4436] (ver Q6).

**Q4 [F] TGR 2D exata.** G finito (depois compacto), caixa com c.c. livre, laço simples C de área A:
- ⟨χ_ρ(W_C)⟩ = d_ρ·ĉ_ρ^A, com ĉ_ρ=c_ρ/(d_ρc₀) e c_ρ=|G|⁻¹Σ_g χ_ρ(g)e^{βReχ_F(g)}.
- Para ℤ₂ dá tanh(β)^A; no toro L×L, (t^A+t^{L²−A})/(1+t^{L²}). Tratabilidade alta: a Mathlib tem caracteres de grupos finitos e a fixação por árvore geradora é combinatória.
- Isso dá à docstring de `YMToy` o conteúdo que ela anuncia e substitui `wilson_area_law`.

**Q5 [F] Lei de área em acoplamento forte, d≥3.**
- Para ℤ₂/G finito: ⟨W_C⟩ = Σ_{∂S=C}t^{|S|} / Σ_{∂S=0}t^{|S|}.
- As componentes conexas por arestas que não tocam C são fechadas e se fatoram. Daí ⟨W_C⟩ ≤ K^{|C|}(c_d t)^{A_min(C)} para t<1/c_d.
- É só contagem de animais de plaquetas. A versão uniforme em N é a de Cao–Nissim–Sheffield, mais difícil. O `lgt` não tem lei de área.

**Q6 [N] Ir além de Dobrushin para ℤ₂ 4D ou para 2T=SL(2,3)⊂SU(2).**
- Criar um critério de volume finito (tipo Dobrushin–Shlosman, por blocos) **compatível com a invariância de calibre**:
  fixação axial dentro do bloco, ou variáveis de plaqueta com a restrição de Bianchi.
- Verificá-lo exatamente por computador em blocos pequenos para β∈[0.06, 0.4].
- Progresso = qualquer β>0.0558 certificado em ℤ₂ 4D. Não encontrei isso na literatura.

**Q7 [N/F] Tornar O8 fiel.**
- Trocar `NaoTrivial` por não trivialidade de espalhamento (Haag–Ruelle), ou fixar
  `Corresponde` := limite OS de medidas de Wilson com β(a) dado pela liberdade assintótica e ⟨trF²·trF²⟩ não gaussiano.
- Provar no kernel que `:φ²:` satisfaz `YMNucleo` (via OSforGFF + reconstrução). Isso transforma "sombra" em teorema.

**Q8 [N] Medida de YM 3D em T³** (medida invariante da dinâmica de CCHS). É o maior valor realista no contínuo, e segue aberto (Chevyrev–Shen 2026). Tratabilidade baixa.

## 4. O que precisa ser criado
- Complexo celular de (ℤ/N)^d e de caixas com bordo: elos orientados, plaquetas, ∂, e H¹/H² com coeficientes em ℤ₂. Portar de `LGT/Lattice/CellComplex`.
- Campos em G^{elos}, grupo de calibre G^{sítios}, holonomia "laço" (lasso), σ-álgebra invariante e **teorema de Elitzur** como lema.
- Medida de Wilson com Haar invariante (a `haarMeasure` da Mathlib serve) e versão `Fintype` decidível.
  **Peter–Weyl e caracteres de grupos compactos** não existem na Mathlib d13f23b (só `RepresentationTheory/Character`, para grupos finitos).
- RP abstrata (⟨θF,F⟩≥0), operador de transferência, **Perron–Frobenius/Krein–Rutman** (ausentes) e espectro de operadores compactos positivos.
- Teorema abstrato de **Kotecký–Preiss**, reutilizável em Ising, φ⁴ e TGR. Dobrushin vem de `markov-semigroups`.
- Dualidade KW/Wegner com acoplamentos inomogêneos, como identidade finita de Fourier em ℤ₂^{células}.
- Lado contínuo: OS para observáveis invariantes (laços de Wilson suavizados, trF² suavizado).
  Falta o **teorema de reconstrução OS** em todos os projetos Lean que conheço, e falta o espalhamento de Haag–Ruelle.
- Métrica de progresso: a "fração certificada" β_cert/β_c, com taxa m(β) e tensão de corda σ(β) explícitas.

## 5. Testes baratos (só especificados, não executados)
**T1. Limiar exato de Dobrushin de um elo contra `lgt`** (numpy, <5 min).
- Grupos: ℤ₂, ℤ₃, ℤ₄ como fases (n=1); S₃ na irrep real de dim. 2; Q₈ e 2T como quatérnions (n=2); SU(2). d∈{3,4}. Ação βΣ(n−ReTr). Lei condicional de um elo: μ_h(x) ∝ exp(βΣ_{j≤k}ReTr(x h_j)), com k=2(d−1) grampos.
- c(β) = max TV(μ_h, μ_{h'}) com h, h' diferindo em um grampo. Sem perda de generalidade h₁=1.
  Enumerar multiconjuntos dos outros k−1 grampos: para 2T em d=4 são C(28,5)=98 280, vezes 24.
- SU(2): μ é von Mises–Fisher em S³ com vetor 2β(r+a), |a|=1 e |r|≤k−1.
  A TV é uma integral no disco unitário, porque a projeção de S³ uniforme num 2-plano é uniforme no disco. Otimizar com grade + Nelder–Mead.
- α=6(d−1)c(β); β_D por bisseção. Teste de unidade: ℤ₂ tem de reproduzir ½artanh(1/(3(d−1))).
- Hipóteses: β_D/β_lgt ∈ [3,10] para todo G, e β_D(2T)≈β_D(SU(2)). É informativo se o sup em SU(2) ocorrer com |r|>0.

**T2. Lei de área 2D exata: caixa contra toro** (<3 min).
- G∈{ℤ₂,ℤ₃,S₃,Q₈}, β∈{0.1, 0.5, 1, 2}. Caixa 2×2 com c.c. livre (12 elos). ℤ₂ e ℤ₃ por enumeração (4 096 e 531 441 configurações). S₃ e Q₈ por contração tensorial exata, sem fixar calibre.
- Calcular ⟨χ_ρ(W_C)⟩ para C=∂(1×1), ∂(1×2), ∂(2×2) e para todas as irreps ρ. Comparar com d_ρĉ_ρ^A, tolerância 1e−12.
- Toros 2×2 (ℤ₂, ℤ₃) e 3×3 (ℤ₂): comparar com (t^A+t^{L²−A})/(1+t^{L²}).
- Esperado: igualdade na caixa e desvio exato no toro. Isso fixa a hipótese topológica do enunciado Lean de Q4.

**T3. Diagonalização exata da matriz de transferência ℤ₂ 2+1D** (scipy, ≤15 min).
- Toro L×L com L∈{2,3,4}. Base invariante: plaquetas (com ∏=1) × holonomias (W_x,W_y), dimensão 2^{L²+1} (131 072 para L=4).
- T = D^{1/2}KD^{1/2}, com D=exp(βΣ_pσ_p) e K=∏_ℓ(e^β+e^{−β}X_ℓ) (calibre temporal).
  X_ℓ inverte as 2 plaquetas vizinhas de ℓ e a holonomia de referência que contém ℓ.
- `eigsh` com 6 autovalores via LinearOperator; β de 0.02 a 1.2.
- Separar os autovetores pelo fluxo de 't Hooft (inverter W_x ou W_y comuta com T). Medir m_L(β)=log(λ₀/λ₁) no fluxo 0 e o desdobramento entre fluxos.
- (H1) m_L não depende de L (L=3 contra 4, diferença <1e−3) para β≤0.5.
- (H2) m_L é muito maior que a taxa de Dobrushin: em β=0.01, a taxa do `lgt` é 0.23, a exata 1.06 e a previsão de tubo −4log tanh β dá 18.4.
- (H3) Para β>0.76 o desdobramento entre fluxos vai a zero como e^{−cL}, mas o gap no fluxo 0 continua aberto. É gap sem confinamento, com vácuo não único em volume finito.
- Uso: define como enunciar `GapMassa`/vácuo único e se vale formalizar polímeros para obter a taxa correta.

**T4. Viabilidade do port de `lgt` para Lean 4.34.1/Mathlib d13f23b** (caixa de tempo de 20 min).
- Projeto lake de rascunho com a Mathlib já construída e `lgt@b8793cc`, `markov-semigroups@acf6491`, `gaussian-field@dc2b3b8`, mais as dependências transitivas do manifest.
- Compilar o fecho de imports de `LGT/MassGap/StrongCoupling.lean` arquivo a arquivo com `lake env lean`.
  Registrar quantos arquivos passam, o primeiro erro de cada um e o tempo.
- Se compilar: `#print axioms ym_mass_gap_rate_exists` e o corolário `∃ m>0, ∀ N>2, …`. Decisão: até 30 erros, vendorizar em `ATK/External/LGT` (Apache-2.0, com atribuição). Acima disso, depender de um fork fixado.

## Fontes (abertas nesta sessão)
- Clay/enunciado: https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_existence_and_mass_gap · https://arxiv.org/pdf/1203.3991 (Summers) · https://arxiv.org/abs/1803.01950v1
- Balaban/contínuo: https://www.arxiv.org/pdf/1108.1335 · https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=92-38 · https://arxiv.org/pdf/2205.07376 · https://arxiv.org/html/2509.03513
- 2D/3D: https://arxiv.org/html/2602.08591v1 · https://arxiv.org/html/2302.12160v3 · https://arxiv.org/html/2603.11374v2 · https://iris.sissa.it/retrieve/5552fa0c-b271-4617-8790-97e2c2ac3c0c/Chevyrev_Shen_26_YMH_3D_C.pdf · https://arxiv.org/abs/2602.00436v1
- Rede forte: https://arxiv.org/abs/2204.12737 · https://arxiv.org/abs/2510.22788 · https://www.arxiv.org/pdf/2505.16585 · https://arxiv.org/abs/2006.16229v5 · https://www.mit.edu/~skycao/research.html
- Rede fraca/abeliano: https://www.arxiv.org/abs/2202.10375 · https://arxiv.org/pdf/2202.10375 · https://arxiv.org/abs/1811.09770 · https://www.arxiv.org/pdf/1811.09770 · https://arxiv.org/pdf/0711.4930 · https://archives.ihes.fr/document/P_81_40.pdf (só metadados)
- Ising/φ⁴: https://arxiv.org/pdf/1808.00439 · https://annals.math.princeton.edu/2021/194-1/p03 · https://www.arxiv.org/abs/1810.01700
- Lean: https://arxiv.org/abs/2603.15770 · https://reservoir.lean-lang.org/@mrdouglasny/LGT · https://github.com/mrdouglasny/lgt (fonte lido via git clone, b8793cc) · https://reservoir.lean-lang.org/@mrdouglasny/pphi2/_payload.json · https://www.alphaxiv.org/overview/2607.06379
- Alegações: https://tech-insider.org/yang-mills-solved-next-before-2045-kalshi-odds/ · https://omarora.in/blog/is-mass-gap-problem-solved/ · https://arxiv.org/abs/2506.00284 · https://arxiv.org/pdf/2606.19362
- Bloqueados por permissão, não lidos: claymath.org/wp-content/uploads/2022/06/yangmills.pdf, arXiv 2509.04688, arXiv 2201.03487 (abs). Göpfert–Mack: o link no projecteuclid veio vazio.
