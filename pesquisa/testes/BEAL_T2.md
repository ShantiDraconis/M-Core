# BEAL T2: busca de contraexemplos para a "Strong Fermat–Catalan" (Mihăilescu, arXiv 2509.18275)

**Hipótese testada.** F_p(x,y) = (xᵖ + yᵖ)/(x + y) = pᵉ z^q, com e = v_p(F) ∈ {0,1}, z ≥ 2, x e y coprimos e q primo
ímpar ≠ p, não tem solução. Testado para p ∈ {5, 7}. Qualquer acerto refuta o Teorema 1 como enunciado.

**Método (C, `__int128` exato).**
- F é calculado pela soma Σ x^{p−1−i}(−y)^i. Divide-se por p enquanto der; registro à parte se v_p ≥ 2.
- Para todo primo q ≤ 127 com 2^q ≤ G: estimo z por exp(log G / q) (double se G < 2¹⁰⁰, senão long double) e ajusto em
  inteiros até z = ⌊G^{1/q}⌋ exato; acerto se z^q = G. Todos os q são testados, então G = w⁶ conta para q = 2 e q = 3.
- q = 2 e q = p são registrados à parte. Não são contraexemplos.

**Controles.**
- *Autoteste*: 142 potências sintéticas z^q (z até 4·10¹⁸, os dois caminhos de ponto flutuante) são achadas, e G+1 não é.
  O autoteste **pegou um erro real**: a estimativa em long double errava em mais de 1 para z ~ 10¹⁸. Troquei a conferência z±1 pelo ajuste inteiro exato.
- *p = 3, onde a afirmação tem de falhar* (x²−xy+y² é norma de Eisenstein). Caixa N = 400: 37 acertos com q = 3 e 6 com q = 5, incluindo e = 1.
  Exemplos verificáveis à mão: F₃(18,−1) = 343 = 7³; F₃(87,−62) = 16807 = 7⁵; F₃(20,−17) = 1029 = 3·7³. **Passou.**
- *Controle positivo q = 2*: F₅(3,−1) = 121 = 11² (Nagell–Ljunggren) aparece, e também F₅(11,8) = 10201 = 101²
  (11⁵+8⁵ = 19·101², conferível à mão). **Passou.**
- *Segunda implementação* (inteiros de Python, `iroot`) na caixa N = 150 para p = 3, 5, 7: contagens idênticas por q
  (p = 3: 98/17/3 para q = 2/3/5) e listas idênticas para q ≥ 3. **Passou.**

**Parâmetros efetivos** (2 núcleos compartilhados, load 5–9, `nice -n 10`):

| busca | domínio | pares testados | tempo |
|---|---|---|---|
| caixa p = 5 | 2 ≤ x ≤ 8000, −x < y < x, y ≠ 0, mdc = 1 | 38.911.562 | 142 s |
| caixa p = 7 | 2 ≤ x ≤ 5000 (idem) | 15.200.914 | 77 s |
| fatias p = 5 | y = −1 e y = 1−x, x ≤ 10⁷ | 19.999.998 | 195 s |
| fatias p = 7 | y = −1 e y = 1−x, x ≤ 10⁶ | 1.999.998 | 39 s |

A caixa é maior que a do mapa (3000 e 2000). A tarefa limitou a busca a p ∈ {5,7}, então p = 11, 13 e as fatias com p ≤ 23 ficaram de fora.

**Resultados.**

| | q ímpar ≠ p (contraexemplo) | q = p | q = 2 | v_p(F) ≥ 2 |
|---|---|---|---|---|
| p = 5, caixa | **0** | 0 | 4: (3,−1)→11², (11,8)→101², (123,35)→13361², (808,−627)→1169341² | 0 |
| p = 7, caixa | **0** | 0 | 0 | 0 |
| p = 5, fatias | **0** | 0 | 1: (3,−1), só Ljunggren | 0 |
| p = 7, fatias | **0** | 0 | 0 | 0 |

Os quatro acertos com q = 2 foram reconferidos em Python com inteiros exatos.

**Interpretação.**
- *O teste mostra:* não há contraexemplo da SFC com p ∈ {5,7} em max(|x|,|y|) ≤ 8000 e 5000 respectivamente, nem nas fatias
  y = −1 e y = 1−x até 10⁷ e 10⁶. Também confirma v_p(F) ≤ 1 e Nagell–Ljunggren (x⁵−1)/(x−1) = □ só com x = 3 nesse alcance.
- *O teste sugere:* heuristicamente, o número esperado de acertos é Σ_x x·(x^{p−1})^{1/q−1}. A soma converge para q ≥ 3 (p = 5),
  então um eventual contraexemplo tenderia a ser pequeno, e isso dá algum peso à busca. Para p = 5, q = 2 ela diverge como log N,
  coerente com os 4 acertos em x ≈ 3, 11, 123, 808: pontos de uma quártica de gênero 1, provavelmente de posto ≥ 1.
- Zero acertos é **evidência fraca** e não verifica a prova. O alerta do mapa continua: y = −1 implicaria Nagell–Ljunggren com n primo,
  que Bennett–Levin chamam de "beyond current technology". O ponto a auditar é o passo de Stickelberger, não a numérica.

**Limites.** p ≥ 11 não testado; caixa finita; q ≤ 127; não procurei soluções com |x| = |y| nem x + y = 0, que são triviais.

**Próximos passos.**
- (i) Mesma busca para p = 11, 13 (x ≤ 1000 e 800) e fatias até p = 23 com aritmética de 256 bits.
- (ii) Ler o passo β(t)^q = (y+ζx)^t/p^{ek} e localizar onde ele usa p > 3, já que p = 3 tem infinitas soluções, como mostra o controle.
- (iii) Estender os pontos de F₅ = z² (curva de gênero 1) como controle de posto.

Código: `tests/code/BEAL_T2_sfc.c`, `tests/code/BEAL_T2_check.py`; saídas: `tests/work/T2_*.out`, `tests/work/BEAL_T2_p3_ctrl.out`.
