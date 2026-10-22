# O sistema paramétrico e a zeta trocada: provados e certificados (22/10/2026)

**Resultado.** Tudo o que o texto encaminhado (22/10, 13:41) afirma como teorema está agora provado no kernel, sem
hipóteses: 47 teoremas, axiomas padrão. Os teoremas estão em `atk-kernel/ATK/ModeloParametrico.lean` (34) e
`atk-kernel/ATK/ZetaTroca.lean` (13).

Todas as tabelas numéricas do texto conferem:
* modelo: 18 de 18 valores, em aritmética racional exata;
* zeta trocada: diferenças ≤ 5·10⁻¹², todas dentro do envelope certificado pela cota provada;
* zeros 100, 1000 e 10000: confirmados.

Código: `codigo/certifica_texto.py`. Dados: `dados/certifica_texto.json`.

## O que o texto chamava de "PROVEN" ou "PROVEN sob A7", agora no kernel

| Afirmação do texto | Teorema |
| --- | --- |
| T(T(z)) = z, \|T(z)\| = \|z\|, det = −1 | `troca_troca`, `norm_troca`, `det_troca`, `troca_matriz` |
| k_N = c + 1/(2N) + 1/(2(N+1)²) é o centro das duas aproximações | `k_eq_centro` |
| k_N > c, k_{N+1} < k_N, k_N → c, N(k_N − c) → 1/2 | `k_gt`, `k_anti`, `k_tendsto`, `k_taxa` |
| k′ < 0, k″ > 0, primitiva ct + ½ log t − 1/(2(t+1)) | `hasDerivAt_kt`, `hasDerivAt_kt'`, `kt'_neg`, `kt''_pos`, `kt_strictAntiOn`, `hasDerivAt_P` |
| ∫_{N₀}^{N} E = ½ log(N/N₀) + 1/(2(N₀+1)) − 1/(2(N+1)), e diverge | `integral_desvio`, `integral_desvio_diverge` |
| lei geral c + A/N^p + B/(N+1)^q → c; acima e decrescente se A, B > 0; o sinal depende da lei | `kg_tendsto`, `kg_acima`, `kg_decresce`, `sinal_depende_da_lei` |
| \|centro − c\| ≤ τ; desvios opostos podem se cancelar | `centro_aprox`, `cancelamento` |
| Approx ⇏ Exact; (∀N, v_N ≠ c) é compatível com v_N → c | `approx_nao_implica_exato`, `offset_compativel` |
| a constante terminal c não é determinada pelas derivadas nem pelos incrementos | `incrementos_iguais`, `k_desloca`, `terminal_indeterminado`; com uma medição exata: `c_de_medicao` |
| \|ζ(w) − 1\| ≤ 2^{−σ} + 2^{1−σ}/(σ−1); ζ → 1 uniformemente | `norm_zeta_sub_one_le`, `norm_zeta_sub_one_le_tres`, `zeta_tende_um` |
| os zeros trocados não são zeros; F = ζ∘T transporta os zeros | `troca_nao_zero`, `F_preserva` |
| até a escala de 10¹² | `zeta_trilhao`: \|ζ − 1\| ≤ 3·2^{−10¹²} |
| 0 ≤ D_∞ ≤ D_N | `dInf_le_DN`, `dInf_le_de_cota` (com `ATK.DInfinito.dInf_nonneg`) |

**Dois teoremas a mais, que respondem diretamente à proposta "1/2 sempre aproximado, nunca exato":**

* **`exato_de_toda_tolerancia`**: um número **fixo** que aproxima c em toda tolerância τ > 0 é igual a c. Só
  uma **sequência** pode ser aproximada sem nunca ser exata. A abscissa de um zero é um número fixo. Portanto
  "aproximado em toda precisão" vira "exato".
* **`limite_unico`**: uma sequência sempre deslocada tem um único limite. Se ε_N → 0, o limite é c, não "perto
  de c".

**Sobre o sistema trocado ζ(a+ib) = 0 = ζ(b+ia), proposto como próximo teste:** `sistema_trocado` prova que
toda solução tem 0 < a < 1 e 0 < b < 1. Então as duas são zeros não triviais de altura menor que 1.
`sistema_trocado_sem_solucao` conclui que, sem zeros de altura |γ| < 1, não há solução. O primeiro zero tem
γ = 14,13, por verificação rigorosa da literatura. Isso ainda não está na Mathlib, por isso entra como hipótese
explícita.

## Tabelas do texto, conferidas

**Modelo (racional exato, arredondado às casas impressas): 18/18.**
* Regra consecutiva: v_N e k_N para N = 10, 100, 10³, 10⁴, 10⁶, 10⁹. A fórmula fechada
  k_N − 1/2 = (2N+1)/(2N(N+1)) também confere.
* A7: j_N para N = 10, 100, 10³, 10⁶, 10¹².
* A expansão até N⁻⁴ confere; o resto vale −2/N⁵.

**ζ nos zeros trocados T(ρ) = γ + i/2.** A "cota" é o envelope provado: |ζ(Tρ) − 1| ≤ 2^{−σ} + 2^{1−σ}/(σ−1),
avaliado em aritmética racional com σ = ⌊γ⌋.

| n | γ | \|ζ(Tρ)\| calculado | texto | cota certificada de \|ζ − 1\| |
| --- | --- | --- | --- | --- |
| 1 | 14,134725 | 1,00005244444 | 1,00005244444 | 10^−4,15 |
| 2 | 21,022040 | 1,00000044177 | 1,00000044177 | 10^−6,28 |
| 3 | 25,010858 | 1,00000002782 | 1,00000002782 | 10^−7,49 |
| 4 | 30,424876 | 1,00000000065 | 1,00000000065 | 10^−9,00 |
| 5 | 32,935062 | 1,00000000011 | 1,00000000011 | 10^−9,61 |
| 100 | 236,524230 | 1 (\|ζ−1\| = 2·10⁻⁷²) | ≈ 1 | 10^−71,0 |
| 1000 | 1419,422481 | 1 | ≈ 1 | 10^−427 |
| 10000 | 9877,782654 | 1 | ≈ 1 | 10^−2973 |

Os γ dos zeros 100, 1000 e 10000 citados no texto foram conferidos de três formas:
* resíduo |ζ(1/2+iγ)| ≤ 3·10⁻¹¹;
* troca de sinal de Z(t) em γ ± 10⁻⁶, logo há um zero exatamente na reta nesse intervalo;
* θ(γ)/π + 1 = 99,81, 999,42 e 9999,68, contra n − 1/2. Isso é compatível com o índice (|S(T)| < 1), mas não
  prova o índice.

**D_N.** D_256 = 0,008233716277261 confere com a rodada 2 (24 dígitos). O certificado intervalar da rodada 3
dá D_256 ≤ 0,00823372, com folga de 3,7·10⁻⁹. D_8000 = 0,0050691202 confere com a rodada 3 (double). Com
`dInf_le_de_cota`: 0 ≤ D_∞ ≤ 0,00823372 é certificado. D_∞ ≤ 0,0050691202 depende do valor numérico de D_8000,
que não tem certificado intervalar.

## A lei A7 contra a lei real de truncamento

A7 (ε₁ = 1/N, ε₂ = 1/(N+1)²) foi escolhida. Ela dá k_N − c > 0 e decrescente para todo N (`k_gt`, `k_anti`).

A lei real, os zeros do truncamento ζ_N da rodada 4c, é outra. ε_N troca de sinal 45, 67 e 78 vezes perto
de ρ₁, ρ₂ e ρ₃: 148/104, 142/109 e 131/120 valores positivos/negativos. Ela se aproxima de 1/2 pelos dois
lados, como permite `sinal_depende_da_lei`. A constante terminal da lei real não é livre: o limite é um zero
exato de ζ (`limite_de_zeros_truncados`), e para esses três zeros ele está na reta, por troca de sinal de Z.
