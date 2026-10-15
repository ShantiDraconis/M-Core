# Classes de ℚ(ζₚ) e o último teorema de Fermat

Pedido do titular (15/10/2026): calcular todas as classes, os comportamentos e as enumerações, e
formalizar o teorema. Este documento separa o que foi **calculado** (fora do kernel) do que está
**formalizado** (no kernel), e diz por que o teorema inteiro não sai por esse caminho.

## 1. Cálculo (numérico, fora do kernel)

Script: `atk-kernel/numerics/classes_ciclotomicas.py`. Dados: `atk-kernel/numerics/hmenos_p300.csv`
e `atk-kernel/numerics/irregulares_p10000.csv`.

**Número de classes relativo h⁻(ℚ(ζₚ)), exato, para os 61 primos 3 ≤ p ≤ 293.** A fórmula é
h⁻ = 2p·∏_{χ ímpar}(−½B_{1,χ}). O produto é calculado como o determinante inteiro da
multiplicação por Σ rⱼxʲ em ℤ[x]/(x^{(p−1)/2} + 1).

| p | 3–19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 | 53 | 59 | 61 | 67 | 71 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| h⁻ | 1 | 3 | 8 | 9 | 37 | 11² | 211 | 5·139 | 4889 | 3·59·233 | 41·1861 | 67·12739 | 7²·79241 |

p é regular ⟺ p ∤ h⁻: pelo teorema de Kummer, p | h⁺ ⟹ p | h⁻. Assim 23, 29 e 31 são regulares,
e 37, 59 e 67 são os primeiros irregulares. O crescimento acompanha a previsão de Kummer,
h⁻ ≈ 2p·(p/4π²)^{(p−1)/4}: a razão observada fica entre 0,8 e 1,3 para p = 101, 199, 293. Essa
forma exata é conjectural; log h⁻ ∼ (p/4)·log p é teorema. Com p = 293, h⁻ já tem 67 algarismos.

**Pares irregulares (p, k) com p | B_k, para os 1227 primos 5 ≤ p ≤ 10 000.** O cálculo usa a
congruência de Voronoi, com uma raiz primitiva como multiplicador.

* 497 primos irregulares (**40,51 %**), contra 1 − e^{−1/2} ≈ 39,35 % na heurística de Siegel.
* Índice de irregularidade, observado contra Poisson(½):

  | índice | observado | Poisson(½) |
  |---|---|---|
  | 0 | 59,5 % | 60,7 % |
  | 1 | 30,9 % | 30,3 % |
  | 2 | 8,3 % | 7,6 % |
  | 3 | 1,3 % | 1,3 % |

  Os primeiros primos de índice 3 são 491, 617 e 647; nenhum p < 10 000 tem índice 4.
* Conferência cruzada: para os 60 primos 5 ≤ p ≤ 293, "p | h⁻" e "existe par irregular" coincidem
  sempre (para p = 3 não há k a testar). É o critério de Kummer conferido numericamente.

Nada disto é certificado pelo kernel. O critério de Kummer e a fórmula analítica de h⁻ (fatoração de
ζ_K em funções L de Dirichlet, valores B_{1,χ}, índice de unidades) não estão na Mathlib. A Mathlib
tem só o resíduo de ζ_K em s = 1 (`NumberField.dedekindZeta_residue`).

## 2. Formalização (kernel)

`ATK/FermatExpoentes.lean` (7 teoremas, axiomas padrão) enumera os expoentes:

* `flt_de_fator`: FLT(n) vale sempre que 4 ∣ n ou n tem um fator primo ímpar ≤ 19.
* `flt_de_fator_regular`: FLT(n) vale sempre que n tem um fator primo ímpar regular.
* `flt_iff_residuo`: `FermatLastTheorem ⟺` FLT(n) para todo n do `Residuo`. O `Residuo` são os n ≥ 3
  com 4 ∤ n e todos os fatores primos ímpares ≥ 23. Ele contém 25,61 % dos n ≤ 10 000.
* `flt_iff_residuo_irregular`: `FermatLastTheorem ⟺` FLT(n) para todo n cujos fatores primos
  ímpares são todos irregulares. Esse é o resíduo exato do método de Kummer. Pelos dados numéricos,
  contém 7,90 % dos n ≤ 10 000.

Com `ATK/FermatRegular.lean`, isto é tudo o que o kernel prova sobre FLT: FLT para todo primo
regular, FLT(3, 4, 5, 7, 11, 13, 17, 19), FLT(n) para 3 ≤ n ≤ 22, e B2 ⟺ primos irregulares p ≥ 23.

## 3. Por que o teorema inteiro não sai calculando classes

1. **Primos irregulares.** O método de Kummer só prova FLT(p) para p regular, e há infinitos primos
   irregulares (Jensen, 1915); 40 % dos primos até 10 000 o são. Nenhum cálculo de classes cobre
   esses expoentes. Os critérios de Kummer–Vandiver tratam irregulares caso a caso, sempre um número
   finito.
2. **Regularidade de 23, 29, 31 no kernel.** O método de 11–19 (todo ideal de norma até a cota de
   Minkowski é principal, com certificado) não se aplica, porque esses anéis não são principais
   (h = 3, 8, 9). Seria preciso mostrar que o grupo de classes tem ordem prima a p, com uma relação
   certificada para cada primo abaixo da cota. As cotas são:

   | p | cota de Minkowski | primos ≡ 1 (mód p) abaixo dela |
   |---|---|---|
   | 23 | ≈ 9,32·10⁶ | 28 371 |
   | 29 | ≈ 1,50·10¹⁰ | — |
   | 31 | ≈ 2,03·10¹¹ | — |

   Só o caso 23 já pediria horas de kernel, além do que o CI suporta. O atalho algébrico
   (Stickelberger e Herbrand, ou a fórmula analítica de h⁻) não está na Mathlib.
3. **O teorema completo** exige Wiles–Taylor (modularidade). Essa formalização é um projeto de vários
   anos (ImperialCollegeLondon/FLT). B2 continua `PARCIAL`; `CLOSED_MATH` continua falso.
