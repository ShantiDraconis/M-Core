# YM T1 — Limiar exato de Dobrushin de um elo vs. `lgt`

**Hipótese testada (YM_frontier §5 T1).** Para a ação de Wilson β Σ_p (n − ReTr U_p), o limiar exato β_D do critério de
Dobrushin de um elo fica 3 a 10 vezes acima da hipótese β < 1/(32n(d−1)) do `lgt`. Além disso, β_D(2T) ≈ β_D(SU(2)), e
é informativo se o sup em SU(2) ocorrer com |r| > 0.

**Método.** A lei condicional de um elo é μ_M(x) ∝ exp(β ReTr(xM)), com M = Σ_j h_j a soma dos k = 2(d−1) grampos.
O coeficiente é c(β) = sup TV(μ_h, μ_h′) sobre pares h, h′ que diferem num grampo. Cada elo tem 6(d−1) vizinhos, e cada
vizinho compartilha exatamente uma plaqueta com ele, logo α = 6(d−1)c(β); β_D sai por bisseção em α = 1 (tolerância 1e−10).
- *Redução.* Sem perda de generalidade h₁ = 1 (troca x → xg) e h₁′ é representante de classe de conjugação.
- *Grupos finitos.* ℤ₂, ℤ₃, ℤ₄ como fases; S₃ na irrep real de dimensão 2; Q₈ e 2T (extra) como quatérnions em SU(2).
  Enumeração exata de todas as somas distintas de k−1 grampos: 4 a 3 721 perfis. Monotonia de c(β) conferida numa grade.
- *SU(2).* μ é von Mises–Fisher em S³ com vetor 2β(r+a). Escrevendo a = p+q e a′ = p−q (p ⊥ q), a região viável é
  m₁² + (m₂ − √(1−|q|²))² ≤ (k−1)². A TV vira uma integral sobre o meio-disco {y₁ > t₀}, porque a fronteira {f_u = f_v} é
  uma reta. A integral 1D é feita por Gauss–Legendre (48 nós); o sup, por grade (5×25×13) mais busca local.
- *Controles.*
  1. ℤ₂: deduzi c = tanh(2β)/2, porque S = Σ_{j≥2} h_j é ímpar. O máximo fica em S = ±1, logo α = 3(d−1)tanh 2β e
     β_D = ½ artanh(1/(3(d−1))). O código reproduz isso: **passou**, com 12 dígitos (0.0841180592 e 0.0557858878).
  2. TV de SU(2) por fórmula contra grade 2D (600²) e Monte Carlo em S³ (10⁵): concordância de 3·10⁻⁴ relativo e 1,8σ.
  3. Normalização exata (=1) e inclinação c(β)/β → 8/(3π) = 0.848826: **passou**.
  4. O sup de SU(2) cai em r = 0 e a′ = −a. Daí sai a forma fechada nova c = L₁(2β)/I₁(2β), com L₁ a função de Struve
     modificada. Pelo mpmath, ela dá 0.0983964711 e 0.0655153856, iguais à otimização numérica até 1e−8.
     Busca aleatória com 2·10⁴ pontos não achou nada maior.

**Resultados** (β_lgt = 1/(32n(d−1)), a hipótese do teorema; a forma via α_lgt = 8(d−1)(1−e^{−4nβ}) < 1 dá 3% a mais)

| G | n | β_D (d=3) | β_D/β_lgt | β_D (d=4) | β_D/β_lgt |
|---|---|---|---|---|---|
| ℤ₂ | 1 | 0.0841180592 | 5.38 | 0.0557858878 | 5.36 |
| ℤ₃ | 1 | 0.1447298837 | 9.26 | 0.0960505965 | 9.22 |
| ℤ₄ | 1 | 0.1442668283 | 9.23 | 0.0953571386 | 9.15 |
| S₃ | 2 | 0.1097316909 | 14.05 | 0.0721680454 | 13.86 |
| Q₈ | 2 | 0.1096010570 | 14.03 | 0.0710830393 | 13.65 |
| 2T (extra) | 2 | 0.0972220500 | 12.44 | 0.0647338416 | 12.43 |
| SU(2) | 2 | 0.0983964711 | 12.59 | 0.0655153856 | 12.58 |

- Taxas para ℤ₂, d = 3, β = 0.01: −½ log α vale 1.060 com o α exato e 0.233 com o do `lgt`. Reproduz os números da fronteira.
- Maximizadores nos grupos finitos (β = 0.05): configurações "polarizadas", com |R| > 0 (todos os outros grampos iguais) e
  g = −1 nos grupos de quatérnions.

**Interpretação.**
- *O que o teste mostra.*
  - A cota do `lgt` é conservadora por um fator de 5.4 (ℤ₂) até 14 (S₃, Q₈).
  - A faixa [3, 10] da hipótese **vale para ℤ_N e falha para os grupos com n = 2** (12.4 a 14.0). Parte do fator vem do 1/n
    no `lgt`, enquanto o β_D por unidade de ReTr não cai como 1/n.
  - β_D(2T) fica 1.2% abaixo de β_D(SU(2)) nas duas dimensões, de acordo com a hipótese.
  - O sup em SU(2) ocorre com **|r| = 0**: grampo invertido e os outros somando zero. Isso foi achado numericamente e é
    coerente com a forma fechada; por esse critério da fronteira, o resultado não é "informativo".
- *O que ele sugere.* Um port do `lgt` com a constante exata ganharia ~5× em ℤ₂ e ~12× em SU(2). Mesmo assim continua
  em β < 0.1: a barreira 2 (raio finito) não muda de natureza.
- *Limites.* β_D vale só para o critério de Dobrushin de **um elo** (sem blocos, sem fixar calibre). Para SU(2), o sup é
  numérico (grade e busca local, sem prova de otimalidade global), apoiado pela forma fechada e pela busca aleatória.

**A seguir.**
1. Provar que o sup em SU(2) está em r = 0 (monotonia em |m|), o que torna L₁/I₁ um lema formalizável.
2. Dobrushin–Shlosman em blocos 2×2×… com fixação axial (Q6) para ℤ₂, acima de 0.0558 em d = 4.
3. Repetir para SU(3) (integral de Weyl em 2D).

Código: `research/tests/code/YM_T1.py` (saída em `research/tests/work/YM_T1.json`). Tempo: 53 s.
