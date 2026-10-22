# RH T1 (reduzido) — expoente ponderado κ(σ) para ζ: mollificador de Möbius suave vs. ótimo

**Hipótese.** Em N ∈ [100, 800], a inclinação log-log de E_N(σ) é −(2σ−1) ± 0,1, onde E_N(σ) usa o mollificador c_k = −μ(k)g(k/N). Pergunta adicional: D_N/E_N → 0?
**Atenção:** E_N é uma **cota superior** de D_N(σ), porque é uma escolha particular de c. Não é o ínfimo. O ínfimo D_N foi calculado à parte, exatamente, por Gram.

## Método
- E_N(σ) = (1/π)∫₀ᵀ |1 − ζ(s)M_N(s)|²/|s|² dτ + cauda de valor médio (1/πT)(ζ(2σ)Σa_j a_k lcm(j,k)^{−2σ} − 1), com T = 16000 ≥ 20N.
- D_N(σ) = min_{c∈ℝᴺ} do mesmo funcional, com Gram + cauda e Cholesky em long double. Sai para todo N = 1..240 de uma vez, com T_G = 8000 ≥ 20·240.
- ζ por Euler–Maclaurin: M = ⌈τ/2⌉+50 termos e 12 correções de Bernoulli (o spec pedia 6, que dariam só ~1e−7). n^{−iτ} por rotação, com recálculo exato a cada 64 passos.
- Quadratura: trapézio. O integrando é par em τ, então o trapézio é espectral em 0; o Simpson do spec não é. Passo h = 0,025 em [0,50] (polo de ζ a distância 1−σ) e 0,05 em [50, T].
- σ ∈ {0,6; 0,7; 0,8; 0,9}. Mollificador em 41 valores de N log-espaçados (25·2^{j/8}). Ótimo em todo N ≤ 240.
- Código: `tests/code/RH_T2_bd.c` (modo R; ζ é a variante 0), `RH_T2_checks.py`, `RH_T2_analyze.py`. Dados em `tests/work/rh/`. Cerca de 50 s por σ.

## Controles (todos passaram)
1. ζ contra `mpmath.zeta`, 221 pontos por σ com τ até 16000: erro relativo máximo 2,4e−11 (σ = 0,7) e 6,5e−12 (σ = 0,9). Alvo: < 1e−9.
2. Plancherel, lado t independente: Gram ⟨ρ_j,ρ_k⟩ = ∫{x/j}{x/k}x^{−2σ−1}dx, integrado exatamente por partes em mpmath.
   - D_1..D_5 batem com o lado Mellin até 3e−8 em σ = 0,9.
   - Em σ = 0,7 a diferença é 1,5e−6, explicada pelo termo T^{2−2σ} da cauda de valor médio.
3. Solver: o D_N do Cholesky coincide com a reavaliação direta (soma de termos ≥ 0 no c*, independente do solver) até ~1e−10 relativo.
4. Convergência: com passo h/2, Δ ≤ 1,3e−6 relativo. Trocando T_G 8000 → 12000, Δ ≤ 4,6e−5.

## Resultados
Inclinações por mínimos quadrados na grade densa em N; o ± é o erro-padrão da regressão.

| σ | previsto −(2σ−1) | E: inclinação [100,800] | E_800 | D (ótimo): inclinação [60,240] | D_240 | D_200/E_200 | inclinação de D/E em [60,240] |
|---|---|---|---|---|---|---|---|
| 0,6 | −0,20 | −0,211 ± 0,027 | 6,84e−3 | −0,357 ± 0,004 | 3,18e−3 | 0,29 | −0,25 ± 0,04 |
| 0,7 | −0,40 | −0,416 ± 0,031 | 1,66e−3 | −0,508 ± 0,007 | 1,15e−3 | 0,33 | −0,22 ± 0,05 |
| 0,8 | −0,60 | −0,621 ± 0,038 | 4,13e−4 | −0,679 ± 0,010 | 3,95e−4 | 0,35 | −0,20 ± 0,07 |
| 0,9 | −0,80 | −0,827 ± 0,056 | 1,07e−4 | −0,861 ± 0,013 | 1,31e−4 | 0,31 | −0,19 ± 0,12 |

- O erro é dominado pela oscilação quase periódica em log N (período 2π/γ₁ ≈ 0,44).
- Com só N ∈ {25, 50, …, 800} (fator 2) a inclinação sai aliasada: σ = 0,9 daria −1,04. Por isso usei a grade densa.
- Inclinações locais do ótimo em janelas [N, 2N]: oscilam entre −0,53 e −1,09 em σ = 0,9.

## Interpretação
- **Mostra (controle clássico):** o mollificador recupera −(2σ−1) dentro de ~0,03 nos quatro σ.
  - Isso é o deslocamento de contorno, com os zeros relevantes na reta crítica.
  - Ao contrário de σ = 1/2, onde a taxa é 1/log N, a taxa de potência já é visível com N ~ 10².
- **Mostra:** o ótimo D_N é cerca de 3× menor que E_N em N = 200 e, até N = 240, decai mais rápido.
  - O excesso de inclinação é de 0,06 a 0,16 e cresce perto de σ = 1/2.
- **Sugere, sem provar:** D_N/E_N → 0 polinomialmente na faixa medida, isto é, o Möbius suave não é ótimo.
  - Isso não se distingue de um regime pré-assintótico. O ótimo pode estar cancelando os resíduos dos primeiros zeros, que dominam por causa do peso 1/|s|².
  - Não contradiz Q2(iii), que é assintótica. Mas N ≤ 240 não basta para ler κ a partir do ótimo para ζ.
- A previsão do mapa de "inclinação rasa em σ = 0,6" não se confirmou: o mollificador dá −0,21 e o ótimo dá −0,36.

## Limites
- Valores finitos (N ≤ 800 no mollificador, N ≤ 240 no ótimo) não determinam κ.
- A cauda de valor médio tem viés de ~1e−6 em σ = 0,7.
- Solver em long double, não em mpmath dps 40. A reavaliação direta faz o papel de certificado do valor.
- O ótimo não foi calculado em N = 400 e 800 (redução em relação ao spec).

## Próximo
- Calcular o ótimo até N ~ 1000: Gram 1000², T ≥ 20000, cerca de 15× o custo atual, viável em C.
- Inclinação de D/E em janela deslizante: se o excesso diminuir, é pré-assintótico; se estabilizar, κ_ótimo > 2σ−1 para ζ, o que tensionaria Q2(iii).
