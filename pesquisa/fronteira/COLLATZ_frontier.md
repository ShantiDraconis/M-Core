# COLLATZ (3n+1) — fronteira de pesquisa (estado em 2026-10-21)

**Resumo.** A conjectura está aberta. O corpus do ATK não tem nada provado.
- O enunciado fiel está em `sorry` (collatz_reverse-tree `lean/Collatz/Basic.lean:97`).
- As "verificações até N" são `axiom`s com N abstrato.
- Há um lema Isabelle falso (`by eval`, 21 elementos) e um único `collatz_5` por `reflexivity` em Coq.

O fato novo de 2026 são resultados de densidade assistidos por IA e formalizados em Lean, ainda **não arbitrados**:
- Mazur (09/2026) prova densidade inferior positiva dos n que chegam a 1 em ≤ 10,46·ln n passos.
- Também prova densidade inferior positiva dos predecessores de qualquer a com 3∤a, o que implica a Conjectura A de Applegate–Lagarias (El Jaouhari, Lean).
- Isso superaria o expoente x^0,84 de Krasikov–Lagarias (2003).

Em paralelo, uma "refutação" de Collatz feita por IA em 07/2026 só passou no kernel porque explorava o bug de soundness #14576 (corrigido no Lean 4.32.2).

## 1. Estado da arte (com fontes abertas)
- **Terras 1976 / Everett 1977.** Quase todo n tem tempo de parada finito, e as classes de densidade existem.
  - Thm C (Terras): o tempo de parada ≤ k é determinado por n mod 2^k (vetor de paridade), a menos de um conjunto finito por classe.
  - Thm D: a taxa de convergência a 1 é exponencial (entropia).
  - OEIS A076227 conta os resíduos sobreviventes mod 2^k: 1,1,1,2,3,4,8,13,19,38,64,128,226,…; a(16)=2114, a(20)=27328.
- **Korec 1994** (Math. Slovaca 44): para todo c > log₄3 ≈ 0,7925, {y : alguma iterada < y^c} tem densidade natural 1.
- **Tao 2019** (arXiv 1909.03562; Forum Math. Pi 2022): Col_min(N) < f(N) para quase todo N **em densidade logarítmica**, para qualquer f → ∞.
  - Variável de Syracuse: Syrac(ℤ/3ⁿ) = Σ_{k=1}^{n} 3^{k−1}·2^{−(a₁+…+a_k)} mod 3ⁿ, com aᵢ ~ Geom(2) i.i.d.
  - Prop 1.17: sup_{3∤ξ} |E e^{−2πiξ·Syrac/3ⁿ}| ≪_A n^{−A}.
  - Tao observa que a cota "poderia talvez" chegar a O(e^{−cn}), mas não persegue isso.
  - O erro exp(O(n^{1/2})) é "a principal razão" para usar densidade logarítmica.
  - Rmk 1.4: cotar Col_min por uma constante para quase todo N é "quase tão difícil" quanto Collatz.
- **Krasikov–Lagarias 2003** (math/0205002, Acta Arith. 109): π₁(x) ≥ x^{0,84} (prova assistida por computador).
  Tao (blog, 01/2020): se c_n := min_{3∤b} P(Syrac(ℤ/3ⁿ)=b) = 3^{−n+o(n)}, então π₁(x) ≫ x^{1−o(1)}.
  Pelo Lema 2 de Tao (c_{n₁+n₂−1} ≥ c_{n₁}c_{n₂}), e_n := −log₃c_{n+1} é subaditiva.
  Normalizando c_n = 3^{−κn+o(n)}, vale κ ≥ 1 trivialmente (c_n ≤ (3/2)3^{−n}); a conjectura é κ = 1.
  O espelho do blog imprime a desigualdade trivial com o sentido trocado, mas os valores c₁=1/3 e c₂=2/63 conferem com o meu cálculo exato.
- **Mazur, "Explicit Positive-Density Collatz Convergence in Logarithmic Time"** (v2.1, 06/09/2026; ProofAtlas, GPT/Codex).
  - Enunciado: existem c, X₀ explícitos tais que, para todo X ≥ X₀, #{1 ≤ n < X : τ(n) ≤ (523/50)·ln n} ≥ cX.
  - Lean: Lean 4.30.0-rc2, Mathlib 5450b53e, axiomas {propext, Classical.choice, Quot.sound}. O README do pacote M1 diz que **não** rodou leanchecker independente.
  - Pacote M2: `predecessors_positive_lower_density` (todo a > 0 com 3∤a tem predecessores de densidade inferior positiva).
    Também `nonconvergence_positive_lower_density_of_counterexample` e `universal_reaches_one_of_arbitrarily_dense_convergence`.
  - Na biblioteca vendorizada (lida via git) está **formalizada a Prop 1.17 de Tao com A = 6409**, com constante astronômica:
    `explicitRenewal_numericalPrimitiveDecay : syracPMFPrimitivePolynomialDecayAt 6409 C`, onde C = (32·6409·C′)^6409.
  - Kontorovich (X, via Digg): "I think it's right", com o mapeamento da matemática ainda em andamento.
  - Ressalvas no próprio texto: constantes inutilizáveis numericamente; não é densidade 1.
- **El Jaouhari, `neljaouh/ConjectureA`** (26–29/09/2026): prova em Lean a Conjectura A de Applegate–Lagarias sobre ℤ e o expoente de crescimento = 1 (Kontorovich–Lagarias).
  Vendoriza M1/M2 sem modificações, roda `leanchecker --fresh` com exit 0 (em v4.30.0-rc2) e porta para 3x−1.
- **Shaik** (21/09/2026, academia.edu): para todo c > 3/log(4/3) ≈ 10,428, densidade inferior positiva de {τ(x) ≤ c·log x}.
  O limiar 3/log(4/3) coincide com a taxa heurística média (≈ 3 passos ordinários por passo de Syracuse, fator médio 3/4). A formalização em Lean é parcial.
- **Programa de Wirsching** (arXiv 2608.27617, 31/08/2026): as Conjecturas 1 e 3 (forma restrita) foram provadas e a 2 segue aberta. Não há melhoria incondicional.
- **Verificação computacional.** Barina (J. Supercomput. 81:810, aceito 21/04/2025): todo n ≤ 2^71 converge, concluído em 15/01/2025, com checksum por unidade de trabalho e sem dupla checagem independente descrita.
  O artigo afirma que um ciclo não trivial tem comprimento ≥ 355.504.839.929 (citando Hercher).
- **Ciclos.** Simons–de Weger: m ≥ 76. Hercher (JIS 26, art. 23.3.5, 2023): não há m-ciclos com m ≤ 91, usando X₀ = 695·2^60.
  Corolário 29 de Hercher: X₀ ≥ 3·2^69 ⇒ K > 1,375·10^11 ímpares. Com 2^71 > 3·2^69 esse corolário já vale, consistente com 2,585·K ≈ 3,555·10^11 passos.
- **Indecidibilidade.** Conway 1972: funções de Collatz generalizadas simulam máquinas de Minsky. Kurtz–Simon 2007 (TAMC, LNCS 4484): o problema generalizado é Π⁰₂-completo.
- **Reescrita.** Yolcu–Aaronson–Heule (2105.14697): Collatz ⇔ terminação de um sistema de reescrita misto binário-ternário; o solver prova enfraquecimentos não triviais.
  Para o sistema unário, interpretações matriciais naturais não bastam.
- **Enunciados formais públicos.** `google-deepmind/formal-conjectures` define `CollatzConjecture.collatzStep`, que é o mapa usado por Mazur.

## 2. Barreiras (e o que já excluem nas rotas do corpus)
1. **Indecidibilidade do caso generalizado** (Conway, Kurtz–Simon). Um argumento que use só a estrutura "afim por classes mod m" provaria demais.
   A prova precisa usar aritmética específica de (3, 2), como 2 ser raiz primitiva mod 3ⁿ e a independência de log 3/log 2.
2. **Barreira de densidade agora nítida** (M2, condicional à correção de Mazur). Se existe contraexemplo, os inícios não convergentes têm densidade inferior positiva.
   Logo "densidade superior 1 dos convergentes" ⇔ Collatz. Nenhum resultado de "quase todo n chega a 1" em densidade natural é mais fraco que a conjectura completa.
   Em particular, densidade 1 de {τ(n) ≤ c·ln n} para algum c já implica Collatz. Isso concorda com a Rmk 1.4 de Tao.
3. **Densidade logarítmica vs. natural**: o erro exp(O(n^{1/2})) de Tao. O upgrade exigiria mistura fina do mapa afim aleatório inteiro (Rmk 1.16).
4. **Teste de sanidade 3x−1.** O mapa 3x−1 tem ciclos não triviais (ex.: 5→14→7→20→10→5), e a máquina de densidade de Mazur porta para ele (El Jaouhari).
   Portanto qualquer "prova de ausência de ciclos" que não use algo que falha para 3x−1 está errada.
5. **Ciclos.** Métodos tipo Baker/LLL e Hercher excluem m-ciclos para m finito. As cotas de comprimento crescem com a verificação X₀ e não excluem todos os ciclos.
   Órbitas divergentes: não há técnica.
6. **Confiança no kernel.** O CollatzLean (R. Kumar, 25/07/2026) passou no kernel e no Nanoda antigo explorando o bug #14576. Foi corrigido no Lean 4.32.2 (28/07/2026).
   M1/M2/ConjectureA foram compilados em v4.30.0-rc2, **antes da correção**, e devem ser re-verificados.
7. **Rotas do corpus.**
   - Axiomatizar "verificado até N" não tem conteúdo.
   - `drift_negative`/`expected_decay` são enunciados estatísticos e não podem valer pontualmente.
   - `exact_ratio_impossible` (2^a ≠ 3^b) é trivial e insuficiente.
   - `no_cycles_below` só é provável para N explícito, via computação.
   - As "mother theorems" de árvore reversa são reformulações e não dão progresso.

## 3. Questões atacáveis (ordenadas por valor × tratabilidade)
**Q1 [F/verificação] — Auditoria independente de Mazur M1/M2 + ConjectureA.**
- Enunciado: em Lean ≥ 4.32.2, com Comparator, um enunciado-alvo escrito só com Mathlib e `leanchecker`/Nanoda atuais, verificar `predecessors_positive_lower_density` e `positive_density`.
- Em paralelo, conferir à mão os passos novos: mistura ternária finita (2.3), contagem de histórias inversas ponderadas e o lema de valuação.
- Importância: decide se K–L x^0,84 foi superado e se a Conjectura A vale. No ATK seria o primeiro resultado genuíno de Collatz.
- Progresso: relatório reprodutível com o kernel corrigido e a lista de discrepâncias de enunciado.
- Sinal a conferir: na leitura do PDF v2.1, a §8 usa b = 280 e diz que o argumento de tempo continua válido "em b = 280 ≥ 5125", enquanto a §7 fixa b₀ = 5125. Provavelmente é erro tipográfico, mas precisa ser checado contra o Lean.

**Q2 [N] — Decaimento exponencial explícito de Fourier da medida de Syracuse.**
- Enunciado: existem ρ < 1 e C explícitos com sup_{3∤ξ} |φ_n(ξ)| ≤ C·ρⁿ para todo n.
- Recursão exata: φ_n(ξ) = Σ_{a≥1} 2^{−a}·e(−ξ2^{−a}/3ⁿ)·φ_{n−1}(ξ2^{−a} mod 3^{n−1}).
  Equivalentemente, é o decaimento de Fourier da medida autossimilar Syrac(ℤ₃) em caracteres de ordem 3ⁿ, um análogo 3-ádico das convoluções de Bernoulli.
- Importância: troca A = 6409 e as constantes astronômicas por constantes utilizáveis, e é o insumo natural para as versões em densidade natural (Rmk 1.16).
  Para dar a escala: Shaik relata log₂log₂log₂C < 176 para a sua constante, e a de Mazur é ainda maior.
- Conhecido: n^{−A} (Tao) e A = 6409 formal (Mazur).
- Progresso: evidência numérica de ρ (T1) seguida de prova assistida por computador. Por exemplo, contração uniforme do operador de r passos sobre ℚ₃/ℤ₃ verificada para todos os ξ mod 3^{n₀}, mais um argumento de cauda.

**Q3 [F] — Terras + Everett + Korec em Lean/Mathlib.** Resultados genuínos e clássicos, ausentes da Mathlib.
- Thm C de Terras: afinidade T^j(2^k m + r) = 3^{o_j(r)}·2^{k−j}·m + T^j(r).
- Densidade 1 de σ(n) < ∞, com taxa exponencial via cota de entropia binomial.
- Korec: c > log₄3.
- A biblioteca de Mazur tem `Erdos1135/Terras` com apenas definições e API de densidade.
- Progresso: teoremas sem `sorry` no ATK, mais o enunciado de densidade com `HasPositiveLowerDensity` no estilo de Mazur.

**Q4 [N/computação] — m-ciclos com X₀ = 2^71.** Refazer a análise de Hercher (Lemas 16–29) com o X₀ de Barina para obter m ≥ M* > 92.
Formalizar a versão condicional `VerifiedUpTo X₀ → ∀ ciclo, K ≥ K*(X₀)`, que usa frações contínuas; Mathlib.NumberTheory.DiophantineApproximation tem Legendre (verificar a API) e precisa de cotas racionais certificadas para log₂3.

**Q5 [N] — Densidade inferior com constante não-astronômica**, por exemplo c ≥ 10^{−3} para {τ(n) ≤ 11·ln n}.
Depende de Q2. A barreira 2 mostra que o alvo "densidade 1" é equivalente a Collatz, então o horizonte realista é constante explícita e limiar 3/log(4/3) com densidade inferior.

**Q6 [N, baixo peso] — κ = 1 para os mínimos de Syrac** (conjectura de Tao de 2020). Q6 perdeu a motivação de π₁(x), se Mazur estiver certo, mas continua sendo uma questão de equidistribuição. T1 mede isso.

**Q7 [F] — Indecidibilidade de Conway / Kurtz–Simon em Lean**, via FRACTRAN ou máquinas de Minsky sobre `Nat.Partrec`. Formaliza a barreira 1.

Status incerto: Mazur cita um resultado próprio anterior de "almost bounded" em densidade natural (C_ND ≈ 436). Não o verifiquei; checar antes de atacar a versão em densidade natural de Tao.

## 4. O que precisa ser criado
- **Uma faixa `ATK/Collatz/` alinhada a `CollatzConjecture.collatzStep`**, para ser compatível com Comparator/Mazur. Conteúdo:
  - mapa acelerado T, vetores de paridade, σ (parada) e τ (parada total);
  - densidades inferior, superior e logarítmica com API (`HasPositiveLowerDensity`);
  - `syracPMF` (reutilizável de Mazur);
  - equação de ciclo n(2^{K+L} − 3^K) = Σ 3^{K−1−i}·2^{s_i}.
- **Formato de certificado "verificado até 2^k"** (crivo de resíduos de Terras com checagem por classe) checável por kernel, para substituir os axiomas `collatz_verified_to`.
- **Conjugação 2-ádica Φ : ℤ₂ → ℤ₂ (Lagarias/Bernstein) e medida de Haar em ℤ₂ via `PadicInt`.** É a infraestrutura para enunciados ergódicos.
- **Workspace de re-verificação** (Lean ≥ 4.32.2, Comparator, Nanoda atualizado) para artefatos externos de IA. Serve também a Poincaré.
- **Remover:** o lema Isabelle falso, os axiomas de verificação e as "mother theorems" com `sorry` apresentadas como progresso.

## 5. Testes baratos (≤ 20 min, 2 núcleos). Especificados, não executados.
**T1 — Lei exata de Syrac(ℤ/3ⁿ): decaimento de Fourier M_n e mínimos c_n (Python + numpy/scipy, ~5–10 min).**
- Algoritmo:
  - 2 é raiz primitiva mod 3ⁿ, então indexe as unidades por ℓ ∈ ℤ/L_n, L_n = 2·3^{n−1}, u = 2^ℓ. A tabela de dlog sai de potências em blocos.
  - Recursão Syrac_n = 2^{−a}(1 + 3·Syrac′_{n−1}). Defina Q_n(ℓ) = P_{n−1}(dlog_{n−1}(y)) se ℓ é par e y := (2^ℓ−1)/3 mod 3^{n−1} é unidade; caso contrário Q_n(ℓ) = 0. Para n=1, Q₁ = δ₀.
  - Então P_n(ℓ) = ½Q_n(ℓ+1) + ½P_n(ℓ+1), cíclico. Calcule com `scipy.signal.lfilter([0.5],[1,-0.5])` sobre a sequência invertida, em 2 voltas; a contração ½ torna o erro ≤ 2^{−L}.
  - Valide contra o cálculo exato em `Fraction` para n ≤ 6: c₁ = 1/3, c₂ = 2/63, c₃ = 1598/262143.
- Saídas para n = 1..16:
  - c_n, ρ_n := c_n·(2/3)·3ⁿ (= 1 sse uniforme) e e_n/n = −log₃(c_{n+1})/n. Por subaditividade, cada valor é cota **superior** rigorosa de κ; use `python-flint` (arb) nos 3 maiores n.
  - Para n ≤ 15, M_n := max_{3∤ξ} |FFT(P_n)(ξ)| com FFT de comprimento 3ⁿ (14,3 M pontos), o ξ* que atinge o máximo e a oscilação de Tao O(m,n) para m = n−1, n−2.
- Hipóteses:
  - H1 (Tao, rmk): log M_n é linear em n. Ajuste −αn + β contra −A·log n + β em n = 6..15 e compare os resíduos.
  - H2 (Tao 2020): ρ_n é limitado inferiormente (κ = 1), contra decaimento geométrico (κ > 1).
- Informativo: um α estável quantifica o alvo de Q2. Uma cota κ ≤ 1+ε pequena, ou ρ_n → 0, é informação nova; não encontrei esses números publicados.

**T2 — Crivo de Terras certificado pelo kernel Lean (Lean 4.34.1 + Mathlib local, ≤ 20 min).**
- Definições: `T n := if n % 2 = 0 then n/2 else (3n+1)/2`; `odds j r` = número de ímpares entre r, …, T^[j−1] r; `survives k r := ∀ j ∈ [1,k], 2^j ≤ 3^(odds j r)` (Bool); `S k := #{r < 2^k | survives k r}`.
- Provar `S k = a(k)` com `decide`/`rfl` para k = 8, 12, 16, e 20 se o tempo der. Os valores esperados são 19, 226, 2114 e 27328.
  Conferi em Python que S(k) = A076227(k) para k ≤ 12, sem deslocamento de índice.
- Provar por indução o lema afim geral de Terras (válido para j ≤ k).
- Registrar o tempo de kernel por k (`#time` / `lake env lean --profile`).
- Hipótese: o kernel com GMP sustenta ~10⁵–10⁶ passos-resíduo/s.
- Informativo: o throughput define até que 2^k um "verificado até N" pode ser **teorema** em vez de axioma. Também pega bugs de definição como o do lema Isabelle falso.

**T3 — Auditoria do artefato de Mazur/El Jaouhari (fase A ≤ 10 min, sem build).**
- `git clone --depth 1 neljaouh/ConjectureA` @ afe7f87 (464 `.lean`, 6,2 MB) em diretório isolado; Python `-I`.
- (a) Varredura por `addDecl`, `Environment.add`, `Kernel.`, `unsafe`, `implemented_by`, `@[extern`, `native_decide`, `ofReduceBool`, `skipKernelTC`, `axiom`, `sorry`, `admit`, `run_cmd`, `run_elab`, `elab`.
  `Verification/ConjectureAExact.lean` usa `run_cmd` como auditoria, então essa ocorrência é esperada.
- (b) Comparar textualmente `predecessors`, `Reaches`, `countBelow`/`natCount` e `HasPositiveLowerDensity` com um `Audit.lean` independente:
  `step n := if n%2=0 then n/2 else 3n+1`, `∃k, step^[k] n = a`, e contagem de 0 < n < X.
- Hipótese: não há padrão de injeção no kernel e as definições são fiéis.
- Fase B, fora do orçamento de 20 min: portar para 4.34.1/d13f23b ou instalar v4.30.0-rc2, e então `leanchecker --fresh` + Comparator com `Audit.lean`.

**T4 — Cota elementar de ciclo como validação + certificado (mpmath, < 1 min).**
- Para um ciclo não trivial com K ímpares, todos > X₀, e L divisões: 2^L = Π(3 + 1/xᵢ) ⇒ 0 < L − K·log₂3 < K·log₂(1 + 1/(3X₀)).
- Calcule K_min(X₀) pela fração contínua de log₂3 (convergentes e semiconvergentes, 80 dígitos) para X₀ ∈ {2^60, 695·2^60, 3·2^69, 2^71}.
- Compare com K > 7,2·10^10 (Hercher, X₀ = 695·2^60), K > 1,375·10^11 (Cor. 29) e com o comprimento ≥ 355.504.839.929 de Barina.
- Informativo: separa quanto da cota vem da desigualdade elementar e quanto vem do refinamento de Hercher. Também fornece o (p, q) exato para o teorema condicional em Lean de Q4.

## Fontes (abertas nesta sessão)
- https://arxiv.org/pdf/1909.03562 (Tao) ; https://tagteam.harvard.edu/hub_feeds/3899/feed_items/2604039 (blog de Tao, 2020, espelho)
- https://arxiv.org/abs/math/0205002v1 ; https://www.dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf
- https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node4.html ; https://oeis.org/A076227
- https://www.fit.vut.cz/research/publication/c197809 ; https://www.fit.vut.cz/research/publication-file/c197809/298514/s11227-025-07337-0.pdf
- https://arxiv.org/abs/2201.00406v3 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf
- https://wiki.bbchallenge.org/wiki/Generalized_Collatz_Problem ; https://arxiv.org/abs/2105.14697
- https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf
- https://github.com/neljaouh/ConjectureA (README; código e UPSTREAM/M1, M2 lidos via `git` @ afe7f87)
- https://digg.com/ai/sdeqcy85 (Kontorovich, secundária) ; https://github.com/Charlie-Wang-03/ai4math-radar/pull/40
- https://www.academia.edu/176111183/Positive_density_of_Collatz_convergence_at_every_rate_above_3_log_4_3 ; https://arxiv.org/abs/2608.27617
- https://gigazine.net/gsc_news/en/20260803-collatz-lean-kernel-bug ; https://github.com/google-deepmind/formal-conjectures
- Bloqueados/não usados: arxiv.org/abs/1909.03562 e terrytao.wordpress.com (permissão) ; leodemoura.github.io postmortem #14576 (permissão) ; proofatlas.ai/advances e artefato 0.90 (robots)
