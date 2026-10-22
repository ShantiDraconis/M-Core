# P vs NP — fronteira de pesquisa para o programa ATK (2026-10-21)

**Ponto de partida (auditoria).** P0 = 0; O4 (`SAT ∉ P`) = OPEN_MATH. Ativos P1 (kernel, Lean 4.34.1, Mathlib d13f23b): Cook–Levin sobre `Turing.FinTM2` (`CookLevinNP.cookLevin`, B4), `sat_em_NP`, `lacuna_pnp_iff : SAT ∉ P ↔ P ≠ NP`, `Shannon.shannon`/`familia_fora_de_Ppoly`, `CircuitoExplicito.cota_linear` (n ≤ 2s+1); só em ramos laterais: `pemPpoly` (P ⊆ P/poly) e `pneNP_iff_fc_incondicional` (≡ formal-conjectures).
Observações técnicas desta leitura (verificadas no fonte):
- `ATK.Shannon.Circuito` = base {∧,∨,¬}, fan-in 2, **¬ conta como porta**; a referência a um fio ainda não calculado lê `false` (`getD … false`), logo constantes são grátis. Qualquer codificação SAT ou teste deve reproduzir essa semântica.
- `shannon` é vazio para n ≤ 5 (⌊2ⁿ/(8n)⌋ = 0) e fica a um fator ≈ 8 do valor assintótico 2ⁿ/n. A cota de Lupanov (superior) não existe no corpus.
- `cota_linear` é mais fraca até que a cota trivial de conectividade. Se f depende das n entradas, o cone da saída tem ≥ n+s′−1 arestas efetivas e ≤ 2s′, logo **s ≥ n−1**, justa para OUₙ. Para XORₙ, ≥ 3(n−1) é certo (Schnorr) e o valor esperado é 4(n−1) (Q1): um fator 6 a 8 acima do kernel.
- A fronteira **explícita** neste mesmo modelo é 5n−o(n). Toda porta ∧/∨ ATK é uma porta U2 e as ¬ somem em U2, logo C_U2 ≤ C_ATK, e o resultado de Iwama–Lachish–Morizumi–Raz se transfere.

## 1. Estado da arte (out/2026)
- **Circuitos gerais, base B2.** 3n−o(n) (Blum 1984); (3+1/86)n−o(n) para dispersores afins (Find–Golovnev–Hirsch–Kulikov, FOCS 2016). A revisão de 2022 dá 3.11n condicionada a dispersores quadráticos explícitos, que não se sabe construir. O recorde é **3.1n−o(n)** para dispersores afins (Li–Yang, ECCC TR21-023 de fev/2021, STOC 2022). O resumo diz que nenhuma função explícita exige 10n. Uma lista curada verificada em 2026-08-10 não acha melhoria.
- **Base U2/De Morgan (¬ grátis).** 5n−o(n) para funções "strongly two-dependent" (Iwama–Morizumi, MFCS 2002; Iwama–Lachish–Morizumi–Raz). Schnorr: XORₙ exige 3(n−1).
- **Eliminação de portas, avanços de 2025–26.**
  - *Limite:* com substituições limitadas por passo, a eliminação não passa de cn para alguma constante c (Golovnev–Hirsch–Knop–Kulikov, MFCS 2016).
  - *Carmosino–Dang–Jackman (arXiv 2602.17942, 20/02/2026):* a simplificação de circuitos é um sistema de reescrita **convergente** para De Morgan e {∧,⊕,¬}, e não existe sistema convergente análogo para U2/B2. Eles tornam Schnorr **construtivo**: um algoritmo que acha o input onde um circuito com menos de 3(n−1) portas erra XORₙ. Citam a verificação em Lean 4 como próximo passo natural.
- **Fórmulas De Morgan.** n^{3−o(1)} (Håstad 1998) e Ω(n³/(log²n·loglog n)) (Tal 2014). Nenhuma cota supercúbica explícita até ago/2026 (fonte secundária). KRW continua aberta; há cúbicas para AC⁰ (Filmus–Meir–Tal).
- **ACC⁰.** Williams 2011: NEXP ⊄ ACC⁰. Murray–Williams (STOC 2018): NQP ⊄ ACC∘THR de tamanho n^{logᵏn}, via o "easy witness lemma" para NP/NQP. Chen (2019): NQP é difícil em média para ACC⁰.
- **Construções explícitas e range avoidance.**
  - Chen–Hirahara–Ren (TR23-144, set/2023; STOC 2024): S₂E/₁, Σ₂E e ZPE^NP/₁ exigem 2ⁿ/n (i.o.), via Avoid ∈ FZPP^NP/₁ i.o.
  - Z. Li (TR23-156, out/2023; STOC 2024): **S₂E ⊄ SIZE[2ⁿ/n] para todo n**, sem conselho, porque Avoid ∈ FS₂P de valor único.
  - Os dois resultados **relativizam**. Aberto: Avoid ∈ FP^NP, que implicaria E^NP com circuitos de ~2ⁿ/(2n).
  - Huang–Li–Zhong (TR25-049, abr–nov/2025): AC⁰-Avoid[n,n^{1+ε}] ∈ FP^NP ⟺ E^NP ⊄ AC⁰ de tamanho 2^{o(n)}.
- **Magnificação.** Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam (ITCS 2020; JACM 2022) mostram, por exemplo, que MCSP[2^{√n}] ∉ GapAND-Formula[N^{2.01}] ⇒ NQP ⊄ NC¹. Propõem também a **barreira de localidade** (Seção 2).
- **Metacomplexidade.**
  - MCSP parcial é NP-difícil por reduções aleatorizadas (Hirahara, FOCS 2022; supera a barreira relativizante de Ko).
  - MCSP com oráculo aleatório é NP-difícil (Ilango, 2023, palestra no IAS em fev/2024).
  - MCSP total segue aberto. Carmosino–Dang–Jackman (arXiv 2511.16903, nov/2025) mostram que a "XOR-Simple Extension" está em P, então XOR não substitui OR para estender a ETH-dureza de Ilango ao MCSP total.
- **Complexidade de provas.**
  - Res(⊕) regular: o PHP binário exige 2^{Ω(n^{1/3}/log n)} (Efremenko–Garlík–Itsykson, STOC 2024).
  - Trade-off supercrítico tamanho×profundidade (Itsykson–Knop, ECCC TR25-116, jul/2025).
  - Tseitin "lifted" até profundidade N^{2−ε} (Bhattacharya–Chattopadhyay, STOC 2026; fonte secundária).
  - **Res(⊕) dag geral: sem cota superpolinomial** (status de ago/2026).
- **Algébrico e GCT.**
  - Limaye–Srinivasan–Tavenas (2021): primeiras cotas superpolinomiais para circuitos algébricos de profundidade constante (IMM, característica 0).
  - GCT: obstruções de ocorrência não bastam (Bürgisser–Ikenmeyer–Panova 2016). Fonte não reaberta: arXiv bloqueado nesta sessão.
- **Tempo vs. espaço.** TIME[t] ⊆ SPACE[√(t log t)] (Williams, arXiv 2502.17779, STOC 2025). Corolário: há problemas em espaço linear que exigem n^{2−ε} de tempo em MT multifita.
- **IA, 2025–26.**
  - AlphaEvolve (Nagda–Raghavan–Thakurta, arXiv 2509.18057, set–nov/2025) produziu gadgets que dão NP-dureza de aproximar MAX-4-CUT (0.987), MAX-3-CUT (0.9649) e TSP métrico (111/110). Os verificadores foram acelerados até ~10⁴×. Nada sobre P vs NP.
  - Fortnow (blog, 10/06/2026): nenhum progresso de IA em P vs NP, e ceticismo explícito sobre rotas via Lean. O pacote Reservoir `Mintpath/p_ne_np` (jul/2026) alega "0 sorries, **2 axioms**": é o padrão A_AXIOM do corpus, sem aceitação.
  - A alegação da OpenAI sobre NS (08/09/2026) não toca P vs NP (fonte secundária).
- **Formalização.**
  - `formalcs/circuit-complexity` (Wesonga, arXiv 2609.24188, 22/09/2026; Lean **4.33.1**) contém o lema de troca de Håstad, PARITY ∉ AC⁰ com cota exp(Ω(n^{1/(d−1)})) e Razborov–Smolensky (ACC[p] ≠ MOD_r). O README diz "complete", mas o status de `sorry`/axiomas não é declarado.
  - Isabelle e Coq já têm Cook–Levin e uma cota monótona para CLIQUE (citado em Carmosino–Dang–Jackman 2026).

## 2. Barreiras e o que elas excluem nas rotas do corpus
- **Relativização (Baker–Gill–Solovay 1975).** Existe A com P^A = NP^A, e então NP^A ⊆ P^A/poly. Logo nenhuma prova relativizante (simulação, diagonalização, contagem) dá P ≠ NP ou NP ⊄ P/poly. Isso exclui:
  - as "pontes universais" do tipo Kleene (`KleeneUniversalBridge`);
  - qualquer argumento que use `TM2ComputableInPolyTime` só como caixa-preta;
  - reforçar `familia_fora_de_Ppoly` até NP com as mesmas armas. Chen–Hirahara–Ren e Li, que relativizam, param em S₂E.
- **Provas naturais (Razborov–Rudich 1997).** Uma propriedade construtiva (poly(2ⁿ) na tabela-verdade) e larga não é útil contra P/poly se existirem PRFs. Isso atinge as rotas κ_PNP, "curvatura" e "entropia espectral" (UEL, Universe-0-0), que hoje nem têm definição (`κ_PNP := sorry`). Qualquer instanciação computável e larga é natural. O teste T3 audita isso empiricamente.
- **Algebrização (Aaronson–Wigderson 2008).** Rotas de aritmetização ou de extensão de baixo grau (como as variantes "Hilbert/adélicas") não bastam.
- **Localidade (Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam 2022).** Técnicas que continuam válidas com portas-oráculo de fan-in pequeno (restrições aleatórias, eliminação) não atravessam os limiares de magnificação. Atacar O4 "magnificando" com essas técnicas está bloqueado.
- **Limites da eliminação de portas (Golovnev–Hirsch–Knop–Kulikov 2016).** `cota_linear`, Q1 e Q4 nunca passam de cn. São rotas para a fronteira linear, não para O4.
- **Fidelidade de modelo.** `pnp_depende_do_modelo` mostra que resultados sobre `ComplexityModel` paramétrico são vazios. O UEL tem P = todas as linguagens. Só `modeloPNP` (FinTM2) conta, e o mesmo vale para qualquer novo modelo de circuitos, que precisa de um teorema de ponte com `Circuito`.

## 3. Questões atacáveis, por valor × tratabilidade ((a) matemática nova; (b) formalização ausente da Mathlib)
**Q1 (b, alta×alta) — A fronteira linear no próprio modelo ATK.**
- *Alvos, em ordem:*
  - `cota_conexa : (∀ i, Depende f i) → C.computa = f → n - 1 ≤ s`;
  - `xor_cota : C.computa = xorN n → 3*(n-1) ≤ s` (Schnorr), depois `4*(n-1) ≤ s` (¬ contado). O valor 4(n−1) é o esperado pela caracterização clássica dos ótimos como árvores de n−1 blocos (¬)XOR₂, que Carmosino–Dang–Jackman 2025 estendem ao caso de ¬ grátis; a atribuição a Red'kin 1973 não foi reconferida;
  - por fim, 5n−o(n) para funções strongly-two-dependent explícitas (construção de Lachish–Raz).
- *Por que importa:* troca a cota (n−1)/2 do kernel pela fronteira real do modelo e cria a biblioteca de eliminação de que Q4 precisa. Casa com o próximo passo que Carmosino–Dang–Jackman 2026 propõem (Lean 4).
- *Progresso:* (1a) em dias; (1b) é ~3× o tamanho de `CircuitoExplicito`; (1c) leva meses. Um bônus "construtivo" é o refutador de Carmosino–Dang–Jackman como função Lean computável.

**Q2 (b, média-alta×alta) — Primeiras cotas superpolinomiais do corpus.**
- *Alvos:*
  - portar `formalcs/circuit-complexity` de 4.33.1 para 4.34.1 e auditar com `#print axioms`;
  - ligar o modelo AC⁰ deles a `Circuito` (profundidade e fan-in ilimitado);
  - deixar como *enunciado-alvo* (não teorema) NQP ⊄ ACC⁰ (Murray–Williams) no modelo FinTM2.
- *Ressalvas:* o rótulo "complete" não foi verificado e o projeto é de set/2026, ainda sem revisão. *Progresso:* PARITY ∉ AC⁰ compilando no `atk-kernel` só com axiomas padrão.

**Q3 (b, média-alta×média) — Do Shannon não construtivo a classes uniformes (a "lacuna" do docstring de Shannon.lean).**
- *Alvos:*
  - (3a) Shannon–Lupanov: L_ATK(n) ∼ 2ⁿ/n, com cota inferior (1−ε)2ⁿ/n e superior via Lupanov;
  - (3b) ∀k ∃L ∉ SIZE[nᵏ] decidida por uma FinTM2 em tempo 2^{n^{O(k)}}, com busca lexicográfica programada na linguagem de laços já verificada (`Compilador`);
  - (3c) Kannan: ∀k, Σ₂P ⊄ SIZE[nᵏ], via Karp–Lipton e autorredutibilidade de SAT.
- *Por que importa:* é o máximo demonstrável hoje na direção "família explícita fora de P/poly". A fronteira real é S₂E (Li 2024), a uma distância exponencial de NP. (3b) relativiza, portanto não ajuda O4.

**Q4 (a, média×média-baixa) — Eliminação de portas assistida por computador.**
- *Enunciado:* exibir f ∈ P com C_B2(f) ≥ (3.1+δ)n − o(n), ou C_U2(f) ≥ (5+δ)n − o(n).
- *Plano:*
  - formular a análise de casos de Li–Yang como uma busca (SAT ou LP) sobre os pesos da medida-potencial e as árvores de casos;
  - verificar cada caso no kernel.
- *Alternativa nova e publicável:* uma constante-limite c₀ *explícita* para uma família bem definida de estratégias. Golovnev–Hirsch–Knop–Kulikov só provam que essa constante existe.

**Q5 (a, alta×média-baixa) — Rota de Ilango para o MCSP total.**
- *Questão:* encontrar uma família explícita f cuja f-Simple-Extension *total* seja NP-difícil (ou ETH-difícil), o passo que falta para estender a dureza do MCSP parcial ao total.
- *O que já está excluído:* OR (fórmulas read-once) e XOR (Carmosino–Dang–Jackman, nov/2025). O algoritmo FPT deles exige ótimos lineares, poucos, enumeráveis e com fan-out limitado.
- *Candidatos:* MAJₙ, MOD3ₙ e THR. O teste T2 mede se eles violam essas condições.

**Q6 (a, muito alta×baixa) — Range avoidance em FP^NP.**
- *Questão:* Avoid ∈ FP^NP? Isso implicaria E^NP ⊄ SIZE[~2ⁿ/(2n)].
- *Versão próxima do formal:* AC⁰-Avoid[n, n^{1+ε}] ∈ FP^NP, equivalente por Huang–Li–Zhong 2025 a E^NP ⊄ AC⁰ de tamanho 2^{o(n)}. Ela se liga diretamente a Q2.

**Q7 (a, média×baixa) — Res(⊕) dag com cota superpolinomial; τ(f,s) em resolução.**
- *Questão principal:* uma cota inferior superpolinomial para Res(⊕) dag geral, rumo a AC⁰[2]-Frege. Segue aberta; Itsykson–Sokolov (APAL 2020) só têm cotas tree-like.
- *Lado ATK:* medir quanto crescem as provas de resolução de τ(f,s) = "f não tem circuito de s portas" (dados de T1/T4). Formalizar Res e Res(⊕) com correção em Lean.

## 4. O que precisa ser criado
1. **Biblioteca de circuitos sobre `Circuito`:** cone, fan-out, restrição `C ↾ (xᵢ:=b)` com lema de tamanho, normalização (constantes, portas duplicadas, ¬¬); conversões ATK ↔ U2 ↔ B2 com fatores explícitos (C_B2 ≤ C_U2 ≤ C_ATK); ponte para o modelo de profundidade e fan-in ilimitado do formalcs.
2. **Arcabouço de eliminação de portas:** medidas-potencial µ = s + Σ pesos; o lema genérico "toda substituição elimina ≥ k portas" ⇒ µ ≥ ck; dispersores afins com construção explícita (pesado), Lachish–Raz.
3. **Ponte uniforme/não uniforme:**
   - fundir `pemPpoly` ao ramo principal;
   - `FinTM2` com oráculo; Σₖ por certificados alternados;
   - Karp–Lipton e busca→decisão de SAT;
   - hierarquia de tempo para FinTM2, necessária para Kannan em EXP e para o método de Williams;
   - Baker–Gill–Solovay como teorema: ∃B, P^B ≠ NP^B. É um "certificado de barreira" contra rotas relativizantes.
4. **Probabilidade e análise:** restrições aleatórias (PMF sobre {0,1,*}ⁿ), redução de fórmulas (shrinkage); Fourier no cubo booleano (verificar o que a Mathlib d13f23b já oferece); jogos de Karchmer–Wigderson e complexidade de comunicação (ausente).
5. **Metacomplexidade:** MCSP e MCSP parcial como linguagens em `modeloPNP` (codificação de tabelas-verdade); Kt/Kᵗ (verificar se a Mathlib já tem algo); `NaturalProperty` (construtiva, larga, útil) e Razborov–Rudich condicional a PRFs.
6. **Provas:** sintaxe e correção de Res/Res(⊕) e Cook–Reckhow; **ponte LRAT → kernel sem `Lean.ofReduceBool`**; codificação verificada `sat(φ(f,s)) ↔ TemCircuito f s`. Com ela, dados SAT de n pequeno viram teoremas P1.

## 5. Testes baratos (≤ 20 min, 2 CPUs; especificação, não executados)
**T1 — Complexidade exata no modelo ATK (SAT).**
- *Codificação* `pip install python-sat` (CaDiCaL 1.5.3), fiel a `ATK.Shannon.Circuito`:
  - fios 0..n−1 são entradas; a porta k é o fio n+k, com op one-hot ∈ {e, ou, nao};
  - seletores one-hot a_k, b_k ∈ [0, n+s); um fio j ≥ n+k lê `false`;
  - valores v[k][x] para os 2ⁿ inputs x; a saída é o último fio (com s = 0, é x_{n−1}).
- *Execuções:* "fiel" e, em paralelo, "com quebra de simetria" (toda porta não-saída usada; a_k ≤ b_k; ordem canônica de portas independentes; sem constantes). As duas devem dar o mesmo s mínimo.
- *Funções:* OUₙ (n ≤ 6), XORₙ (n ≤ 4), MAJ₃, MAJ₅, THR²ₙ e MOD3ʳₙ (n ≤ 5) e TRI₄ (triângulo em K₄, 6 bits).
- *Procedimento:* s cresce a partir de n−1, com timeout de 300 s por chamada e registro de [lo, hi].
- *Calibração:* a mesma rotina na base B2 tem de reproduzir MOD3ʳ₄ = 7, 7, 6 (Kulikov–Pechenev–Slezkin). Como desafio extra, tentar SAT para tamanho ≤ 11 em MOD3¹₆ e MOD3²₆ na base B2, casos abertos segundo eles (Knuth: MOD3⁰₆ = 12).
- *Hipóteses:* C_ATK(XORₙ) = 4(n−1); C_ATK(OUₙ) = n−1; medir C_ATK/C_B2 e a folga sobre `cota_linear`.
- *Saída informativa:* qualquer XOR com menos de 4(n−1) refuta a caracterização citada. Os valores exatos de C_ATK (¬ contado, constantes livres) não estão tabelados na literatura que lemos.

**T2 — Estrutura dos circuitos ótimos (condições do algoritmo FPT de Carmosino–Dang–Jackman, Q5).**
- *Entrada:* f com s* exato vindo de T1 (n ≤ 4, e n = 5 se s* ≤ 10).
- *Método:* enumerar todas as soluções SAT de tamanho s* com cláusulas de bloqueio (teto de 10⁴), canonizar como DAG rotulado (isomorfismo via networkx) e deduplicar.
- *Medidas:* N_opt(f) e, sobre os ótimos, o fan-out máximo e mínimo; se todo ótimo é árvore de blocos.
- *Hipótese:* XOR satisfaz as condições (sanidade); MAJ e MOD3 têm N_opt crescendo rápido com n e fan-out crescente.
- *Leitura:* se a hipótese valer, eles seguem candidatos a Simple Extension difícil. Se não, a barreira de Carmosino–Dang–Jackman se estende a eles. Tempo de ≤ 10 min.

**T3 — Auditoria "natural proofs" de medidas candidatas.**
- *Tamanhos:* n ∈ {10, 12, 14, 16}.
- *Amostras:*
  - R: 200 tabelas uniformes;
  - C_s: 200 funções de circuitos ATK aleatórios, para s ∈ {n, 2n, 4n, n^{1.5}, n², 2n²}, com dois geradores: entradas uniformes entre fios anteriores, ou janela dos últimos 2n fios (que mistura melhor). Registrar a fração de funções constantes ou degeneradas;
  - E: CLIQUE₃ em v = 5 (n = 10) e v = 6 (n = 15), 3-COL em v = 5, MAJₙ, MOD3ₙ, IPₙ.
- *Medidas μ, todas em poly(2ⁿ) e vetorizadas em numpy:*
  - entropia de Fourier e influência total (Walsh–Hadamard);
  - ‖f̂‖₁; grau sobre GF(2) (Möbius); sensibilidade máxima;
  - posto real e posto sobre GF(2) da matriz 2^{⌊n/2⌋}×2^{⌈n/2⌉};
  - número de subfunções nas últimas n/2 variáveis (estilo Nechiporuk).
- *Quantidade medida:* s*_μ(n) = o menor s com KS(μ(C_s), μ(R)) < 0.1, além da posição de μ(E). *Hipótese:* s*_μ(n) = O(n²) para toda μ testada, ou seja, circuitos quadráticos aleatórios já parecem aleatórios. Uma μ com s*_μ que explode é o achado a investigar.
- *Uso:* serve de régua para qualquer futura definição de κ_PNP. Tempo de ~10 min.

**T4 — Certificados SAT dentro do kernel.**
- *Entrada:* CNFs UNSAT de T1 (XOR₃ com s = 7, MAJ₃ com s*−1, XOR₄ com s = 11 se resolvido). DRUP vem do CaDiCaL do pysat (`with_proof=True`) e LRAT vem do drat-trim (`-L`, compilado do GitHub).
- *Verificação em Lean 4.34.1:*
  - (A) com o verificador LRAT de `Std.Tactic.BVDecide` no core (confirmar o nome exato), via `Lean.ofReduceBool`;
  - (B) só no kernel: CNF e prova como termos, com `checker cnf prova = true` por `decide`/`rfl` e `maxHeartbeats 0`.
- *Medidas:* tempo e memória em função do número de passos LRAT; o maior certificado que (B) aceita em 20 min. *Hipótese:* (B) é viável até ~10⁴ passos. Se for, os valores exatos de T1 viram teoremas P1 com axiomas padrão, uma vez escrita `encode_sound`. Se não for, ficam fora do kernel ou marcados com `ofReduceBool`, que vale o mesmo que `native_decide` na auditoria.

## Fontes (abertas nesta sessão)
- https://eccc.weizmann.ac.il/report/2021/023/ — Li–Yang 3.1n; https://eccc.weizmann.ac.il/report/2015/166/ e https://golovnev.org/papers/rdq.pdf — Find–Golovnev–Hirsch–Kulikov
- https://www.wisdom.weizmann.ac.il/~ranraz/publications/P5nlb.pdf — Iwama–Lachish–Morizumi–Raz, 5n−o(n)
- https://pureportal.spbu.ru/ru/publications/on-the-limits-of-gate-elimination(ed521f27-a1b1-4c8e-a75b-9f2d23693a5f).html
- https://arxiv.org/abs/2602.17942 e https://arxiv.org/pdf/2602.17942 — Carmosino–Dang–Jackman 2026; https://arxiv.org/abs/2511.16903v1 — XOR Simple Extension em P
- https://dspace.mit.edu/handle/1721.1/130542 — Murray–Williams; https://eccc.weizmann.ac.il/report/2019/031 — Chen
- https://eccc.weizmann.ac.il/report/2023/144/ — Chen–Hirahara–Ren; https://eccc.weizmann.ac.il/report/2023/156/download — Z. Li
- https://eccc.weizmann.ac.il/report/2025/049 — Huang–Li–Zhong; https://eccc.weizmann.ac.il/report/2019/168/download e https://dspace.mit.edu/handle/1721.1/146303 — magnificação e localidade
- https://eccc.weizmann.ac.il/report/2022/119/ — Hirahara; https://www.ias.edu/video/expanding-reach-p-not-equal-np-minimum-circuit-size-problem-random-oracle-np-hard — Ilango
- https://eccc.weizmann.ac.il/report/2025/116/download — Itsykson–Knop; https://eccc.weizmann.ac.il/report/2021/081/ — Limaye–Srinivasan–Tavenas; https://www.arxiv.org/abs/2502.17779 — Williams √t
- https://arxiv.org/abs/2509.18057v5 — AlphaEvolve; https://blog.computationalcomplexity.org/2026/06/respect-p-v-np-problem.html — Fortnow
- https://reservoir.lean-lang.org/@Mintpath/p_ne_np; https://www.chatslide.ai/articles/openai-navier-stokes-p-vs-np (secundária)
- https://arxiv.org/abs/2609.24188 e https://github.com/formalcs/circuit-complexity — PARITY/ACC em Lean
- https://arxiv.org/pdf/2102.12579v3 — Kulikov–Pechenev–Slezkin (valores exatos de MOD3; Knuth para B₄ e B₅)
- Secundárias (lista curada, verificada em 2026-08-10): https://lacker.io/complexity/problems/b2-circuit-lower-bound-3-1n.html, …/demorgan-formula-cubic-barrier.html, …/range-avoidance-fpnp-frontier.html, …/res-parities-daglike.html
- https://github.com/google-deepmind/formal-conjectures (raiz aberta; o arquivo de P≠NP não foi localizado)
- Bloqueadas por permissão (não usadas como fonte): arXiv 1604.06431 (GCT), arXiv 2507.23008, ECCC 2024/128, 2025/188, 2026/014, Wikipedia "Natural proof", scottaaronson.com/papers/alg.pdf. As referências clássicas (Baker–Gill–Solovay, Razborov–Rudich, Aaronson–Wigderson, Kannan, Håstad, Tal, Williams 2011) foram citadas de memória bibliográfica.
