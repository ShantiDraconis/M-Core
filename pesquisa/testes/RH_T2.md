# RH T2 — zero plantado fora da reta: κ(σ) "lê" Θ?

**Hipótese (Q2(iii), conjectura).** Se F tem zeros com Re = β₀ < σ, então D_N^F(σ) ≍ N^{−2(σ−β₀)}: a inclinação vira −2(σ−β₀), em vez de −(2σ−1). Se σ < β₀, D_N^F fica acima de um piso.

## Método
- Pipeline de RH_T1 (`tests/code/RH_T2_bd.c`): ótimo exato por Gram para N = 1..240 (T_G = 8000) e mollificador, que é só **cota superior**, em 41 valores de N em [25, 800] (T = 16000). σ ∈ {0,6; 0,7; 0,8; 0,9}, β₀ ∈ {0,65; 0,75}.
- **(R) desenho do mapa:** F = ζ·R, com R = (s−ρ₀)(s−ρ̄₀)/((s−ρ₁)(s−ρ̄₁)), ρ₁ = ½ + iγ₁, ρ₀ = β₀ + iγ₁.
- **(D) desenho corrigido:** F = ζ(s)(1 − 2^{β₀−s}).
  - Série de Dirichlet com produto de Euler (só o fator em 2 muda), zeros em β₀ + 2πik/log 2, k ∈ ℤ.
  - Mollificador: coeficientes de 1/F, isto é, (μ ∗ 2^{β₀j}[n = 2^j])(k)·g(k/N).
- **Piso de Pick (rigoroso, σ < β₀):** D ≥ (1/2π)w*K⁻¹w, com K o núcleo de H²(Re s > σ), K_ij = 1/(2π(z_i + z̄_j − 2σ)), w_i = B(z_i)/z_i e B = (s−1)/(s−2σ+1) (Blaschke no polo s = 1), nos zeros de F à direita de σ.

## Achado 1 — o desenho (R) é mal posto (argumento rigoroso)
- Na reta σ vale (1+FP)/s = R·Mellin[h − Σc_kρ_k], com h = χ·(1 + 2Re[(A/ρ₀)(t^{−ρ₀} − 1)]) e A = Res_{ρ₀}(1/R).
- Em cada intervalo (1/(n+1), 1/n], todo elemento de span{ρ_k} é α/t + β_n, e h não é dessa forma.
- Logo D_N^F ≥ min|R|²·Σ_n dist²(h, ⟨1/t,1⟩) > 0 **para todo N e todo σ**, haja ou não zero fora da reta: o R racional não é "tipo Dirichlet". Cotas: σ = 0,9: ≥ 5,9e−5 (β₀ = 0,65) e ≥ 6,6e−5 (0,75); σ = 0,8: ≥ 4,2e−5 e 1,5e−5; σ = 0,7, β₀ = 0,65: ≥ 1,2e−5.
- Portanto a inclinação assintótica em (R) é 0 em todos os casos.
- Na prática, (R) dá **falso positivo** em σ = 0,9 (ótimo −0,47 e −0,29, contra −0,50 e −0,30 previstos). Falha em σ = 0,8 (−0,45 e −0,29 contra −0,30 e −0,10) e em σ = 0,7, β₀ = 0,65 (−0,37 contra −0,10): é uma mistura pré-assintótica do decaimento de ζ com o piso.

## Achado 2 — desenho (D)

| σ | β₀ | previsto | E (mollif.) incl. [100,800] | D (ótimo) incl. [60,240] | idem [120,240] | D_240 | D/E (N=200) |
|---|---|---|---|---|---|---|---|
| 0,9 | 0,65 | −0,50 | −0,504 ± 0,025 | −0,517 ± 0,003 | −0,546 | 3,30e−2 | 0,47 |
| 0,9 | 0,75 | −0,30 | −0,302 ± 0,022 | −0,314 ± 0,002 | −0,334 | 6,41e−2 | 0,66 |
| 0,8 | 0,65 | −0,30 | −0,300 ± 0,015 | −0,314 ± 0,002 | −0,333 | 7,89e−2 | 0,75 |
| 0,8 | 0,75 | −0,10 | −0,097 ± 0,010 | −0,139 ± 0,001 | −0,149 | 1,09e−1 | 0,73 |
| 0,7 | 0,65 | −0,10 | −0,097 ± 0,009 | −0,149 ± 0,001 | −0,159 | 1,51e−1 | 0,71 |
| 0,7 | 0,75 | piso | +0,107 (diverge) | −0,057 | | 0,138 ≥ Pick 0,095 | |
| 0,6 | 0,65 | piso | +0,105 | −0,059 | | 0,222 ≥ Pick 0,148 | |
| 0,6 | 0,75 | piso | +0,308 | −0,031 | | 0,158 ≥ Pick 0,126 | |

Linha de base, ζ sem zero plantado: ótimo −0,86 / −0,68 / −0,51 / −0,36 em σ = 0,9 / 0,8 / 0,7 / 0,6. Pisos de Pick com 61 zeros (|k| ≤ 30).

## Controles (todos passaram)
1. **Clássico:** em (D), o mollificador recupera −2(σ−β₀) nos 5 casos com σ > β₀, com erro ≤ 0,01 (deslocamento de contorno, cota superior).
2. **Pisos:** com σ < β₀, D^F estabiliza acima do piso de Pick nos 3 casos de (D). Em (R) também: D_240 = 4,5e−3; 5,9e−3; 2,9e−3, todos ≥ os pisos 1,0e−3; 3,0e−3; 1,0e−3.
3. **Numérica:** ζ contra mpmath, Plancherel, passo h/2 e T_G como em RH_T1.md.

## Interpretação
- **Mostra, em (D) com N ≤ 240:** o ótimo sobre **todos** os polinômios de Dirichlet de comprimento N decai com a mesma inclinação do mollificador, −2(σ−β₀). O excesso é pequeno (0,01–0,05) e D/E ≈ 0,5–0,75 fica quase constante. Neste modelo o ótimo não contorna o zero plantado: κ "lê" Θ, evidência numérica a favor de Q2(iii).
- **Contraste com ζ (RH_T1):** lá o ótimo ganha 0,06–0,16 de inclinação. Aqui o excesso também não é nulo e cresce na janela [120,240]; pode ser correção logarítmica ou deriva de κ_N, e N ≤ 240 não decide.
- **Recomendação:** descartar o T2 do mapa como especificado (F = ζR), que não decide Q2(iii); usar F = ζ·D com D série de Dirichlet.

## Limites
- (D) é modelo de brinquedo: sem equação funcional, e os zeros plantados formam uma reta vertical inteira, com um zero real em β₀. Não é ζ com um zero isolado deslocado.
- N ≤ 240 não prova assintótica; os pisos de Pick são válidos mas não ótimos.

## Próximo
1. (D) até N ~ 1000, para ver se o excesso vai a 0.
2. D com dois primos, 1 − a2^{−s} + b3^{−s}, para ter zeros desalinhados.
3. Tentar provar o piso κ ≤ 2(σ−β₀) para F = ζ·D. Pista: nos primos p > N, o coeficiente de ζP é b_p = c₁, preso a todos esses p, o que obstrui aproximar a parte singular perto de t = 0.
