# BEAL — fronteira de pesquisa (estado em 21/10/2026)

Equação: aˣ + bʸ = cᶻ, com a, b, c ≥ 1 e x, y, z ≥ 3. Beal afirma que, nesse caso, mdc(a, b, c) > 1. Forma equivalente: não há solução com a, b, c dois a dois coprimos.

**O que o ATK tem (dossier, sem compilação independente).**
- Enunciado `ATK.Conditional.Beal.BealConjecture` fiel. Pontes como hipóteses: B2 = FLT e B8 = Darmon–Merel (DM), esta na **forma fraca, com A, B > 0** (`DarmonMerelReducao.DMSq/DMCube`).
- P1: FLT(n) para 3 ≤ n ≤ 22 (FLT(11/13/17/19) por certificados de PID); caso I de FLT para p < 300 (Germain–Legendre); x⁴ − y⁴ ≠ z²; A⁶ + B⁶ ≠ C².
- Famílias de Beal com d ∣ mdc(x, y, z), d ∈ {3, 4, 5, 7, 11, 13, 17, 19}, mais os padrões (4,4,2), (4,2,4), (2,4,4) e (6,6,2).
- Reduções: incondicional `beal_iff_residual_regular`; condicional `beal_teorema_completo` (B2 ∧ B8 → (Beal ⟺ `ExclusaoResidualFinal`)).
- Coberturas de 11,43% (incondicional) e 16,79% (sob B2 + B8) aparecem só em comentários. Nada toca o resíduo mdc(x, y, z) ≤ 2 (O2).

## 1. Estado da arte

**1.1 Teoremas estruturais**
- Darmon–Granville (1995): para cada assinatura fixa com 1/p + 1/q + 1/r < 1, só finitas soluções primitivas. Prova via Faltings, **inefetiva**: sem algoritmo nem cota [S1]. Fermat–Catalan (finitude com expoentes variando) é consequência de abc [S1, S10].
- Soluções primitivas conhecidas com 1/p + 1/q + 1/r < 1: exatamente 10, **todas com um expoente 2**: 1+2³=3², 2⁵+7²=3⁴, 7³+13²=2⁹, 2⁷+17³=71², 3⁵+11⁴=122², 17⁷+76271³=21063928², 1414³+2213459²=65⁷, 9262³+15312283²=113⁷, 43⁸+96222³=30042907², 33⁸+1549034²=15613³ [S1].
- Catalan/Mihăilescu (2002): 3² − 2³ = 1 é a única solução de xᵖ − yᵠ = 1, logo Beal vale se a = 1 ou b = 1 [S8, S13]. Não formalizado; há só exposições, como Klazar (dez/2025, incompleta) [S12].

**1.2 Assinaturas resolvidas que importam para Beal** (survey Ratcliffe–Grechuk, arXiv 2412.11933, v2 de 14/04/2025, Expo. Math., Tabela 1.1 [S1])
- **Famílias infinitas:** (n,n,n), FLT; (n,n,2) para n ≥ 4 e (n,n,3) para n ≥ 3 (Darmon–Merel, Poonen; (3,4,4) em Cohen, Prop. 14.6.6); (2,4,n) para n ≥ 4 (Ellenberg; Bennett–Ellenberg–Ng; Bruin para n = 5); (2,6,n), (3,6,n) e (3,3,2n).
- **(3,3,n):** todo n ≤ 10⁹ [S1]; para primos p, densidade ≈ 0,844 (Chen–Siksek 2009 mais Freitas 2016: p ≡ 2 mod 3, p ≥ 17) [S18, S19]. Caso geral aberto.
- **(2,3,n):** n ∈ {7, 8, 9, 10, 12, 15}, e n = 11 sob GRH [S1, S8]. Caso geral aberto; critério local novo para X_E⁻(p) em Freitas–Mocanu–Sánchez-Rodríguez (dez/2025) [S20].
- **Casos isolados:** (3,4,5) (Siksek–Stoll); (5,5,7), (5,5,19) e (7,7,5) (Dahmen–Siksek); sob GRH também (5,5,11), (5,5,13) e (7,7,11) [S15].
- **Programa de Darmon, (r,r,n):**
  - x¹¹ + y¹¹ = zⁿ sem solução se 2 ∣ a+b ou 11 ∣ a+b (BCDF I); (5,5,p) completo depende do caso Cartan da conjectura de "big image" [S7];
  - x⁷ + y⁷ = zⁿ só parcial; x⁷ + y⁷ = 3zⁿ resolvido (BCDF II) [S7b];
  - x¹³ + y¹³ = z⁵ só trivial; também z⁷ sob GRH, e qualquer n se 13 ∣ c (Best–Dahmen–Freitas, out/2025) [S17].
- **Menor assinatura de Beal em aberto, segundo o survey: (3,5,7).** Para Fermat–Catalan: (2,5,7) [S1].

**1.3 Buscas computacionais e prêmio**
- Sikora: nenhuma solução além das 10. Lendo os expoentes perdidos na extração, o limite das potências é 2⁸⁰ se o menor expoente é 3, 2¹⁰⁰ se é 4, 2¹¹³ se é ≥ 5 [S10]. O preprint 2410.21552 não pôde ser aberto.
- Busca até bases e expoentes ≤ 1000 (danvk, c. 2006–07) [S9].
- Prêmio Beal: US$ 1.000.000, guardado pela AMS, não concedido; exige publicação com arbitragem [S25].

**1.4 abc e IUT**
- Recorde de qualidade: Reyssat (1987), 2 + 3¹⁰·109 = 23⁵, q ≈ 1,62991; exatamente 236 triplas com q ≥ 1,4 até 20 dígitos [S24].
- Laishram–Shorey: abc explícito de Baker ⇒ c < rad(abc)^{7/4}, e Beal vale **fora de Q = {(3,4,p) para p primo, (3,5,p) para 7 ≤ p ≤ 23}** (a menos de permutação); em Q, max ≤ e^{1758,3} [S11].
- Zhou (arXiv 2503.14510 e 2510.05448, 06/10/2025) afirma, *via IUT*, que restam só **2446 assinaturas de Beal** (ex.: (3,5,n) com 7 ≤ n ≤ 3677; (3,4,n) com 11 ≤ n ≤ 109) [S5]. Depende do Cor. 3.12 de IUT III, que o relatório LANA (Kato, Commelin, Kedlaya, Hoshi, Topaz; 16/07/2026) *não* valida: o "wall" de San Diego "had not yet been crossed", sem juízo final [S6].

**1.5 Novidades 2025–2026 e status de verificação**
- **FLT completo em Lean (Anthropic, 04/09/2026)** [S2, S3, S4]:
  - repo anthropics/fermats-last-theorem; Lean 4.33.1, Mathlib v4.33.0; 60.475 módulos; só axiomas padrão; verificado por comparator ("okay") e nanoda (1.052.234 declarações); Buzzard revisou;
  - reutilizável: `WeierstrassCurve.modularity_of_semistableModel`, modularidade **só para modelos semiestáveis** (casamento de a_ℓ); Ribet só para a representação de Frey (`FreyPackage.level_lowering_to_two`); Mazur só para curvas de Frey;
  - build: ~67 GB de disco, até 36 GB de RAM por módulo.
- **KummerCriterion (Brasca, Reservoir, 01/09/2026, Lean 4.34.0-rc2)** [S14]: critério de Kummer (regular ⟺ p ∤ numeradores de B₂, …, B_{p−3}); `fermatLastTheoremFor_le100_of_ne_irregular` (FLT(n) para 2 < n ≤ 100, n ∉ {37, 59, 67, 74}); infinitude dos irregulares.
- **(3,5,7) declarado resolvido (Chocian, arXiv 2609.26996, 22/09/2026)** [S16]: descida de Dahmen–Siksek (7 corpos sépticos), Chabauty e Mordell–Weil sieve sobre Q(√−7), level lowering de Hilbert sobre Q(√5). Magma V2.29-10, PARI, Sage; assistido por IA (Codex/ChatGPT; Claude como "auditor"); sem Lean e **sem arbitragem**.
- **"Strong Fermat–Catalan" (Mihăilescu, arXiv 2509.18275, v1 de 22/09/2025, sem arbitragem)** [S22]:
  - afirma que (xᵖ + yᵖ)/(x + y) = pᵉ z^q (e ∈ {0, 1}) não tem solução coprima para primos ímpares distintos p > 3 e q; daí xᵖ + yᵖ = z^q sem solução. Companheiro: Bartolomé–Mihăilescu 2108.08572 v4, "under review" [S21];
  - **alerta:** com y = −1 isso implica Nagell–Ljunggren (xᵖ − 1)/(x − 1) = z^q para n = p primo, problema que Bennett–Levin chamam de "beyond current technology" mesmo com n = q [S23].
- Bug de soundness do kernel Lean #14576 (tipos indutivos aninhados), reportado e corrigido em 4.32.2 em 28/07/2026 [S26]. O ATK roda em 4.34.1, posterior ao fix; ainda assim, checar com nanoda ou lean4checker atualizados.

## 2. Barreiras (e rotas do ATK que elas eliminam)

- **B1. Não há obstrução local.** (1, m, 1) satisfaz 1 + mʸ ≡ 1ᶻ (mod m) com bases coprimas, então nenhuma congruência ou argumento p-ádico fecha uma assinatura. ⇒ `BealFiltros` (mod 4/8) e a partição de paridade T59 só podem podar; a única classe fechável por congruência, "c par, x e y pares" (mod 4), já é conhecida [S8].
- **B2. O método modular precisa de um primo ℓ comum aos três expoentes.** Fora disso, o nível de Serre da curva de Frey–Hellegouarch depende de rad(c) (ou de a, b): não há lista finita de newforms, como o próprio `FreyBealResidual` admite.
  - ⇒ a rota "Ribet no resíduo" morre. Com mdc ≤ 2 restam só descida + Chabauty (assinatura por assinatura) e o programa de Darmon (variedades abelianas de Frey), que exige modularidade sobre corpos totalmente reais, big image (caso Cartan aberto) e eliminação de newforms de Hilbert [S7, S27].
- **B3. Soluções triviais obstruem a eliminação.** (1, −1, 0) e (1, 0, 1) produzem newforms no nível de Serre que não podem ser eliminadas; por isso os resultados (r,r,n) só valem com 2 ∣ a+b, r ∣ a+b ou coeficiente 3 [S7, S17].
- **B4. Inefetividade e falta de uniformidade.** Darmon–Granville não dá cotas; há infinitas assinaturas, cada uma com sua prova, e nenhum método é uniforme em p, q, r com mdc ≤ 2, salvo abc (IUT contestada) e a SFC (não verificada). ⇒ percentuais de cobertura de caixas de expoentes **não medem progresso** rumo a Beal.
- **B5. Barreira tipo caso I (Germain–Legendre).** Para q ≡ 1 mod mmc(x, y, z) com expoentes coprimos, H_x, H_y, H_z ⊂ F_q* são grandes e o número de soluções unitárias de u + v = w é ~ |H_x||H_y||H_z|/(q−1) ≫ 1 (Weil/Jacobi, erro ≤ d₁d₂d₃√q).
  - ⇒ não há "primo de Germain" que force q ∣ abc, salvo obstruções triviais (q−1 dividindo dois expoentes). A maquinaria `GermainLegendre` (FLT caso I, p < 300) não se transporta para O2. Ver T3.
- **B6. Infraestrutura Lean ausente.** Falta modularidade não semiestável (BCDT, necessária para DM e (3,3,p)), Ribet geral, formas de Hilbert, Chabauty–Coleman e Mordell–Weil sieve (para Bruin, Poonen–Schaefer–Stoll, Siksek–Stoll, (3,5,7)) e Stickelberger (para Catalan e SFC). B8 continua ponte mesmo depois de importar o FLT da Anthropic.
- **B7. abc-qualidade.** Num contraexemplo, rad(abc) ≤ abc < cᶻ·ˢ com s = 1/x + 1/y + 1/z, logo q(a^x, b^y, c^z) > 1/s.
  - Se s < 0,6135, o contraexemplo seria **recorde abc** (q > 1,62991). Isso vale fora de {(3,3,·), (3,4,≤33), (3,5,≤12), (3,6,≤8), (3,7,7), (4,4,≤8), (4,5,≤6)} a menos de permutação.
  - Nada disso prova Beal: só explica onde contraexemplos seriam "baratos".

## 3. Questões atacáveis (ordem: valor × tratabilidade)

**Q1 [(b) formalização/engenharia; V alto, T alto] — Descarregar B2 no kernel.**
- Enunciado: `theorem flt : FermatLastTheorem` com axiomas ⊆ {propext, Classical.choice, Quot.sound}, numa lane que compile `BealCompleto`. Daí, sem pontes: Beal ⟺ resíduo com mdc(x,y,z) ≤ 2 ∧ ¬(4,4,2)-famílias ∧ ¬(6,6,2).
- Caminho: lane fixada em Lean 4.33.1 / Mathlib v4.33.0 importando o repositório da Anthropic e portando de volta os ~10 arquivos de Beal (Mathlib elementar); build em máquina ≥ 64 GB; verificação com nanoda.
- Interino barato: KummerCriterion (FLT para n ≤ 100 exceto 37, 59, 67, 74) substitui os certificados de Minkowski, e a cota ≈ 9,3·10⁶ estimada pelo ATK para p = 23 desaparece.
- Progresso: CI com `#print axioms` verde e checagem independente. Ganho em O2: zero; ganho de honestidade: B2 sai da lista de pontes.

**Q2 [(b), com pouca (a); V alto, T alto] — "Resíduo de literatura" exato e corrigido.**
- (i) Reescrever B8 na forma publicada, sobre ℤ (A, B, C ∈ ℤ primitivos, ABC ≠ 0); a forma fraca com A, B > 0 perde permutações. Ex.: `ResidualFinal 4 5 5` e `ResidualFinal 3 5 5` são verdadeiros no ATK, mas c⁵ + (−b)⁵ = (a²)² e c⁵ + (−b)⁵ = a³ são casos de DM.
- (ii) Pontes explícitas, cada uma com sua lista de soluções conhecidas e um lema de levantamento decidível: (3,3,n) para n ≤ 10⁷ ou 10⁹; (2,4,n); (2,6,n); (3,6,n); (2,3,n) para n ∈ {7,…,10,12,15}; (3,4,5); (3,4,4); Dahmen–Siksek.
  - Também estão hoje no `ResidualFinal` e já resolvidos: (3,3,4), (3,4,4), (4,4,5) (via (2,4,5)) e (3,4,7) (via (2,3,7), pois 2213459 e 15312283 não são quadrados).
- (iii) Provar `beal_iff_residual_literatura`.
- Valor: troca o "83,21% aberto" pelo conjunto realmente aberto e pelas assinaturas primitivas mínimas. Medir com T1.

**Q3 [(a) verificação de alegação; V altíssimo se verdadeira, T médio, P(correta) baixa] — Strong Fermat–Catalan.**
- Se o Teorema 1 de 2509.18275 vale, todo triplo com dois expoentes compartilhando um primo p ≥ 5 e o terceiro com fator primo ímpar q ≠ p fica fora de Beal; isso cobre quase toda a fatia (p,p,q) do resíduo.
- Ações: (a) falsificação numérica, T2; (b) checar o passo do ideal de Stickelberger (β(t)^q = (y + ζx)^t / p^{ek}) contra p = 3, onde a equação tem infinitas soluções (normas de Eisenstein) e o argumento *precisa* falhar; (c) checar a consistência com BCDF, que precisa de big image para (5,5,p).
- Progresso: um contraexemplo, um passo falso identificado, ou uma prova sobrevivente que aponte um alvo de Lean (Stickelberger).

**Q4 [(a), com (b) para certificados; V médio, T médio] — (3,5,7) e as próximas assinaturas primitivas mínimas.**
- Reproduzir Chocian sem Magma (PARI/Sage) e certificar no kernel os grupos de classes e unidades dos 7 corpos sépticos, com a técnica de `FermatDezenove` (558 certificados de geradores de ideais) levada ao grau 7.
- Depois atacar, por descida + Chabauty, as próximas assinaturas abertas que T1 indicar (esperado: (3,5,11), (3,5,13), (3,7,11), (4,5,7) ← (2,5,7)).
- Progresso: cada assinatura excluída com certificados reproduzíveis.

**Q5 [(a) nova barreira + (b); V médio, T alto] — Teorema "sem caso I no resíduo".**
- Enunciado: para mdc(x,y,z) ≤ 2 e todo primo q > C·(d₁d₂d₃)², com d_i = mdc(expoente_i, q−1), existem u, v, w ∈ F_q* com uˣ + vʸ = wᶻ; abaixo da cota, lista explícita de exceções vinda de T3.
- Prova: soma de caracteres. A Mathlib tem `jacobiSum` e `jacobiSum_mul_jacobiSum_inv`; falta a contagem de soluções de equações diagonais.
- Valor: certifica formalmente que nenhum argumento de Germain/Legendre fecha O2, podando uma rota do próprio ATK.

**Q6 [(b); V baixo-médio, T muito alto] — Pontes abc no kernel.**
- (i) `ABC_κ → Beal` para s ≤ 1/κ, elementar (`UniqueFactorizationMonoid.radical` já existe); (ii) o lema do recorde (q > 1/s).
- (iii) **Beal polinomial já está na Mathlib** (`Polynomial.flt_catalan`, via Mason–Stothers `Polynomial.abc`, verificado no Mathlib local do ATK); embrulhar como `BealPolinomial` custa uma linha e é o análogo de corpo de funções da rota abc.
- (iv) Enunciar Laishram–Shorey (Baker ⇒ resíduo ⊆ Q ∪ altura ≤ e^{1758}) como ponte condicional.

**Q7 [(a); V alto, T baixo] — A família (3,4,p), o "núcleo duro" sob abc.**
- a³ + b⁴ = c^p é (2,3,p) com o quadrado sendo uma quarta potência; conhecido só para p ∈ {5, 7}, mais 11 sob GRH.
- Pergunta: a estrutura extra (x = b², isto é, a assinatura (4,3,p)) permite um argumento de Q-curvas tipo Ellenberg, ou o critério local de [S20], para uma densidade positiva de p?
- Progresso: qualquer densidade positiva de p. Problema irmão: (3,3,p) para p ≡ 1 mod 3 (densidade ~0,156 aberta).

## 4. O que precisa ser criado

1. `ATK/GenFermat/Signature.lean`: assinaturas com sinal; lema de arranjo (uma solução de Beal com expoentes (X,Y,Z) dá uma solução primitiva de (p,q,r) quando p∣X, q∣Y, r∣Z, e um termo muda de lado só se o expoente do seu slot for ímpar); lema decidível de levantamento das 10 soluções conhecidas.
2. `ATK/GenFermat/Bridges.lean`: registro de teoremas publicados *na forma inteira original*, com metadados (referência; status arbitrado / GRH / sem arbitragem / IUT / abc). Substitui B8 fraca.
3. `Covered : ℕ → ℕ → ℕ → Bool` com teorema de correção (Covered ∧ pontes ⇒ sem solução coprima) e contagens verificadas pelo kernel em caixas pequenas; a contagem em 3..200 fica em Python, com dupla implementação.
4. Contagem de soluções de equações diagonais sobre F_q via `jacobiSum`, para Q5.
5. Infraestrutura pesada, de longo prazo: Stickelberger (Catalan/SFC); Chabauty–Coleman com certificados e Mordell–Weil sieve; grupos de classes/unidades em grau ≤ 7 (generalizando os certificados de Minkowski); importação de `modularity_of_semistableModel`, que *não* basta para DM (é preciso BCDT + Ribet geral).
6. Higiene: percentuais de cobertura saídos de código (T1), não de comentários; rodar nanoda nos kernels após o bug #14576.

## 5. Testes baratos (não executados; ≤ 20 min, 2 núcleos)

**T1 — Mapa de cobertura literatura × kernel (Python/numpy, ~2–5 min).**
- *Entrada:* E = {3..200}³ ordenado, para aˣ + bʸ = cᶻ (7.762.392 triplos; subdomínio mdc ≤ 2: 7.260.078).
- *Lista L:* cada entrada é uma equação A^p + B^q = C^r sobre ℤ, com faixa de parâmetros, soluções primitivas conhecidas (Tabela 1.2 de [S1]) e status. Fontes: Tabela 1.1 sem asterisco de [S1], mais [S15, S17, S16, S22, S5, S11].
- *Regra de cobertura:*
  - atribuir (+aˣ, +bʸ, −cᶻ) aos slots (+A^p, +B^q, −C^r), com inversão global de sinal permitida; o expoente de cada slot divide o do termo; termo com sinal diferente do slot exige expoente de slot ímpar;
  - nenhuma solução conhecida pode levantar: testar com `sympy.integer_nthroot` se |A| = a^{X/p} etc., com bases positivas, coprimas e expoentes ≥ 3;
  - duas variantes de arranjo: conservadora (só arranjos enunciados) e permissiva (todas as permutações).
- *Cenários cumulativos:* S0 = kernel (`ExclusaoResidualRegular`, deve dar **887.152 = 11,43%**); S1 = + FLT; S2 = + DM fraca (`ResidualFinal`, deve dar **16,79%**); S3 = DM inteira; S4 = literatura arbitrada; S5 = + GRH; S6 = + alegações sem arbitragem ((3,5,7); SFC (p,p,q)); S7 = + IUT-Zhou (excluir tudo fora da lista de exceções do Teorema A de [S5]); S8 = ABC_{7/4} (s ≤ 4/7) e Q de Laishram–Shorey.
- *Saídas:* % de E e do subdomínio mdc ≤ 2 por cenário; ranking das 25 assinaturas candidatas (p ≤ q ≤ r ≤ 50, p ≥ 2) pelo número de triplos descobertos em S4 que cobririam; lista dos triplos descobertos com s > 0,6135.
- *Hipótese:* S4 − S2 ≥ 25 p.p. Se valer, a maior parte do "83%" do ATK já está resolvida na literatura; o ranking diz qual assinatura atacar (Q4) e se (2,3,13), (2,5,7) e (3,5,11) dominam.
- *Validação:* reproduzir S0 e S2 exatamente; caso contrário, o código está errado.

**T2 — Falsificação da Strong Fermat–Catalan (Python + gmpy2, ~5–10 min).** Seja F_p(x, y) = (xᵖ + yᵖ)/(x + y).
- *Caixa:* p ∈ {5, 7, 11, 13}; pares coprimos com 2 ≤ x ≤ N_p, −x < y < x, y ≠ 0, N = 3000/2000/1000/800 (≈ 9·10⁶ pares).
- *Teste por par:* e = v_p(F) (0 ou 1; registrar se ≥ 2); verificar se F/pᵉ é q-ésima potência perfeita (`gmpy2.is_power`, depois `iroot` sobre os primos q ≤ log₂F), com z ≥ 2.
- *Fatias de 1 variável até x ≤ 10⁶, p ≤ 23:* y = −1 (Nagell–Ljunggren) e y = 1 − x (xᵖ − (x−1)ᵖ).
- *Registrar à parte:* q = 2 (controle positivo: F₅(3,−1) = 121 = 11² deve aparecer) e q = p.
- *Hipótese:* nenhuma solução com q ímpar ≠ p. Qualquer acerto refuta o Teorema 1 de 2509.18275 como enunciado e poupa Q3 (b, c); zero acertos é evidência fraca, mas obrigatória antes de investir em leitura.

**T3 — Censo de obstruções tipo Germain no resíduo (Python, ~5–15 min).**
- *Caixa:* todos (X,Y,Z) ∈ [3,60]³ com mdc ≤ 2 (~1,8·10⁵) e todos os primos q ≤ 2·10⁴.
- *Teste:* com dᵢ = mdc(expoente, q−1) e H_d = (F_q*)^d, decidir se existem u ∈ H_{d_X}, v ∈ H_{d_Y} com u + v ∈ H_{d_Z} \ {0}; memoizar por (q, d_X, d_Y, d_Z) e amostrar ao acaso primeiro. Obstrução ⇒ toda solução coprima tem q ∣ abc (vira lema `decide`).
- *Classificação:* triviais = q−1 divide dois dos expoentes (ex.: 6 ∣ Y, Z ⇒ 7 ∣ abc); as demais são não-triviais.
- *Saídas:* fração de triplos com obstrução não-trivial; maior q obstrutor em função de d_X·d_Y·d_Z, comparado com a cota de Weil (d₁d₂d₃)².
- *Hipótese (B5/Q5):* não existe obstrução não-trivial para mdc ≤ 2. Refutada, dá lemas novos de divisibilidade verificáveis pelo kernel; confirmada, fixa a lista de exceções de Q5.

**T4 — Sonda Lean: critério de Kummer no kernel ATK (≤ 20 min).**
- Clonar github.com/riccardobrasca/KummerCriterion @972cab3; comparar o Mathlib do `lake-manifest` dele com o do ATK.
- Compilar só `KummerCriterion/BernoulliFast/*` e `FermatLastTheoremUpTo100` contra o Mathlib do ATK, com `LEAN_NUM_THREADS=2` e `timeout 20m`.
- Medir: sucesso; erros de portabilidade; `#print axioms fermatLastTheoremFor_le100_of_ne_irregular`; tempo de kernel do certificado de regularidade por primo (p = 101, 103, …, 199), ajustando tempo ~ p^α.
- *Hipótese:* α ≤ 4 e todos os primos regulares < 500 são certificáveis em minutos. Decide se Q1-interino substitui os certificados de Minkowski (FLT11–19) e leva FLT(n) até 100 ao kernel do ATK.

## Fontes (abertas nesta sessão)
[S1] https://arxiv.org/html/2412.11933v2 · https://arxiv.org/abs/2412.11933v2 · https://arxiv.org/pdf/2412.11933
[S2] https://www.anthropic.com/news/formalizing-fermats-last-theorem · [S3] https://github.com/anthropics/fermats-last-theorem · [S4] https://github.com/anthropics/fermats-last-theorem/blob/main/PROOF-PATH.md
[S5] https://arxiv.org/html/2510.05448v1 · https://arxiv.org/abs/2510.05448v1 · https://arxiv.org/abs/2503.14510
[S6] https://ncatlab.org/nlab/files/LANAProject-Report-July2026.pdf · https://zeli.app/story/48963019
[S7] https://arxiv.org/html/2205.15861v5 · [S7b] https://arxiv.org/html/2308.07062v2 · [S27] https://www.mpim-bonn.mpg.de/print/10637
[S8] https://en.wikipedia.org/wiki/Beal_conjecture · [S9] https://www.danvk.org/wp/beals-conjecture/index.html · [S10] https://en.wikipedia.org/wiki/Fermat%E2%80%93Catalan_conjecture
[S11] https://ar5iv.arxiv.org/html/1112.2461 · [S12] https://arxiv.org/html/2601.14900v1 · [S13] https://www.ams.org/journals/bull/2004-41-01/S0273-0979-03-00993-5
[S14] https://reservoir.lean-lang.org/@riccardobrasca/KummerCriterion · https://github.com/riccardobrasca/KummerCriterion
[S15] https://pdf.arxiv.org/pdf/1309.4030 · [S16] https://arxiv.org/pdf/2609.26996 · [S17] https://arxiv.org/html/2510.12092v1
[S18] https://wrap.warwick.ac.uk/27755/ · [S19] https://arxiv.org/pdf/1601.06361 · [S20] https://arxiv.org/abs/2512.10781v1
[S21] https://arxiv.org/html/2108.08572v4 · https://arxiv.org/abs/2108.08572 · [S22] https://arxiv.org/html/2509.18275v1 · https://arxiv.org/abs/2509.18275
[S23] https://pdf.arxiv.org/pdf/1312.4037 · [S24] https://arxiv.org/pdf/1409.2974 · [S25] https://ams.org/beal-prize · [S26] https://gigazine.net/gsc_news/en/20260803-collatz-lean-kernel-bug
Bloqueadas/não lidas: norvig.com/beal.html, arxiv.org/abs/2410.21552 (Sikora), página lean-eval de Mihăilescu, Wikipedia "Abc conjecture" (erro de servidor).
