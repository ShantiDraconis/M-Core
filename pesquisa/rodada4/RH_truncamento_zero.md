# RH — Truncamento inexato, limite exato; o sistema (k, d, y) (22/10/2026)

**Resultado.** O modelo ρ_N = A_N/B_N com ε_N ≠ 0 e ε_N → 0 agora tem uma regra concreta: ρ_N é o zero do
truncamento de Euler–Maclaurin do kernel, ζ_N(s) = Σ_{m≤N} m^{−s} + N^{1−s}/(s−1).

* Nos três primeiros zeros, ε_N nunca é zero (0 de cerca de 250 valores de N). O sinal troca 45, 67 e 78 vezes
  entre N = 2 e N = 10⁵, e |ε_N| ≤ N^{−1/2}/(2|ζ′(ρ)|).
* O limite é um zero **exato** de ζ. Isso está provado no kernel: `limite_de_zeros_truncados`.
* O sistema com três incógnitas (k, d, y) não tem solução **se e só se** RH vale (`rh_iff_sem_solucao`).

Kernel: `atk-kernel/ATK/TruncamentoZero.lean` (9 teoremas, axiomas padrão). Código: `codigo/truncamento_zero.py`.
Dados: `dados/truncamento_zero.json`. Figura: `dados/truncamento_zero.png`.

## No kernel

| Teorema | Enunciado |
| --- | --- |
| `eixo_unico` | se os zeros são simétricos em torno de Re s = κ e existe algum zero, então κ = 1/2 |
| `aproximantes_sobem` | zeros exatos com Re ρ_N ≠ 1/2 e Re ρ_N → 1/2 têm ‖ρ_N‖ → ∞ |
| `aproximante_refuta` | um único zero exato com ε ≠ 0 refuta RH |
| `norm_cauda_le` | \|I_N(s)\| ≤ N^{−σ}/σ |
| `residuo_trunc` | \|ζ(s) − ζ_N(s)\| ≤ \|s\|·N^{−σ}/σ |
| `limite_de_zeros_truncados` | ζ_N(ρ_N) = 0 e ρ_N → ρ (Re ρ > 0, ρ ≠ 1) ⇒ ζ(ρ) = 0 |
| `rh_iff_sem_solucao` | RH ⟺ não existem k, d ≠ 0, y com ζ(k ± d + iy) = 0 e 0 < k ± d < 1 |
| `solucao_eixo_deslocado` | uma solução com k ≠ 1/2 exige um terceiro zero distinto na altura y |

Sobre o argumento "igualar 2k − s̄ = 1 − s̄ em todo ponto": ele supõe o que quer provar, que a reflexão em k é a
própria reflexão funcional. `eixo_unico` supõe só que o conjunto dos zeros é invariante pela reflexão em κ.
Composta com s ↦ 1 − s̄, essa reflexão vira a translação s ↦ s + (1 − 2κ). Repetida, a translação tira qualquer
zero da faixa 0 < Re < 1, a menos que κ = 1/2.

## Numérico: os zeros truncados perto de ρ₁, ρ₂, ρ₃

A previsão de primeira ordem é ζ_N(s) ≈ ζ(s) + N^{−s}/2. Daí vem ρ_N − ρ ≈ −N^{−ρ}/(2ζ′(ρ)), com módulo
N^{−1/2}/(2|ζ′(ρ)|) e fase −γ log N.

| γ do zero exato | N | ε_N | previsto | \|ρ_N − ρ\| | previsto | \|ζ(ρ_N)\| | cota do kernel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 14,1347 | 100 | +4,37·10⁻² | +4,73·10⁻² | 5,23·10⁻² | 6,30·10⁻² | 4,09·10⁻² | 2,13 |
| 14,1347 | 10⁴ | +5,48·10⁻⁴ | +2,05·10⁻⁴ | 6,28·10⁻³ | 6,30·10⁻³ | 4,98·10⁻³ | 0,281 |
| 14,1347 | 10⁵ | −1,80·10⁻³ | −1,78·10⁻³ | 2,03·10⁻³ | 1,99·10⁻³ | 1,61·10⁻³ | 0,092 |
| 21,0220 | 10⁵ | +1,36·10⁻³ | +1,38·10⁻³ | 1,37·10⁻³ | 1,39·10⁻³ | 1,56·10⁻³ | 0,131 |
| 25,0109 | 10⁵ | −8,49·10⁻⁴ | −8,48·10⁻⁴ | 1,16·10⁻³ | 1,15·10⁻³ | 1,60·10⁻³ | 0,160 |

* ε_N oscila em torno de 0 e se aproxima pelos dois lados. Não há viés para um lado de 1/2.
* \|ζ(ρ_N)\| é pequeno, mas não é zero: o ponto truncado não é zero de ζ. Seu resíduo é ≈ |ζ′(ρ)|·|ρ_N − ρ|.
* A cota provada |s|·N^{−σ}/σ é folgada, 20 a 100 vezes o resíduo real. Ela basta para o limite exato.
* Para N < ~20, a primeira ordem falha. Os desvios lá passam do envelope, porque o truncamento ainda é grosseiro.

## O sistema (k, d, y) nos dados

Uma solução exige dois zeros distintos na mesma altura. Até γ = 300, as 138 alturas são todas diferentes; a menor
separação é 0,608, perto de γ = 295. Portanto o sistema não tem solução com |y| ≤ 300, numericamente, sem
certificado. Rigorosamente, Platt–Trudgian (2021) põem todos os zeros até 3·10¹² na reta, e lá o sistema também
não tem solução.
