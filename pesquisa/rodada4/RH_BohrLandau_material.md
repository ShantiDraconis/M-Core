# RH — Bohr–Landau: o lado material da prova (22/10/2026)

O kernel prova **incondicionalmente** `ATK.BLProva.bohrLandau : TeoremaBohrLandau`, isto é, para todo δ > 0 existe C
com N(1/2 + δ, T) ≤ C·T para T ≥ 2, só com os axiomas padrão. O teorema não dá C. Este relatório mede numericamente
as duas peças analíticas da prova e a constante que sai dela. Os números são **ilustração**: ponto flutuante, sem
certificação intervalar.

Código: `codigo/bohr_landau_material.py` (numpy; ζ por Euler–Maclaurin de ordem 16). Dados: `dados/bohr_landau_material.json`.

## Controles

| Grandeza | Valor obtido | Referência |
| --- | --- | --- |
| ζ(2) − π²/6 | 4,4·10⁻¹⁶ | 0 |
| \|ζ(1/2 + 14,134725141734693 i)\| | 2,1·10⁻¹⁵ | 0 (1º zero) |
| ζ(1/2 + 10i) | 1,544895 − 0,115336 i | 1,5448952 − 0,1153365 i |

## 1. Média quadrática (peça `BLMediaZeta.media_zeta`)

(1/Y)·∫_{1/2}^{Y} |ζ(σ + it)|² dt:

| σ | ζ(2σ) | Y = 50 | Y = 100 | Y = 200 | Y = 400 | dois termos clássicos, Y = 400 |
| --- | --- | --- | --- | --- | --- | --- |
| 0,55 | 10,584 | 2,148 | 2,670 | 3,230 | 3,681 | 3,668 |
| 0,60 | 5,592 | 2,014 | 2,437 | 2,870 | 3,188 | 3,175 |
| 0,625 | 4,595 | 1,954 | 2,336 | 2,716 | 2,985 | — |
| 0,75 | 2,612 | 1,710 | 1,942 | 2,148 | 2,265 | 2,246 |
| 1,0 | 1,645 | 1,409 | 1,504 | 1,574 | 1,601 | — |
| 1,5 | 1,202 | 1,149 | 1,178 | 1,193 | 1,197 | — |
| 4,0 | 1,004 | 0,992 | 0,999 | 1,002 | 1,003 | — |

* A razão fica limitada, como o kernel prova. Ela sobe devagar até ζ(2σ), e mais devagar quanto mais perto de 1/2.
* A última coluna é ζ(2σ) + (2π)^{2σ−1} ζ(2−2σ)/((2−2σ)·Y^{2σ−1}), o termo principal mais o secundário da fórmula
  clássica de valor médio. Ela bate com o número medido até ~1%. Como ζ(2−2σ) < 0 para 1/2 < σ < 1, o termo
  secundário é negativo, e por isso a convergência é lenta.
* Constante efetiva para σ₀ = 1/2 + δ/2 = 0,625 (δ = 1/4), medida até Y = 400: M ≈ 3,00. É o supremo de I(Y)/Y
  em 1 ≤ Y ≤ 400, e ele cresce até ζ(1,25) ≈ 4,6. A constante que a prova formal produz é muito maior, porque usa
  `sq_three`, `media_D` e a cota da cauda.

## 2. Contagem por Jensen (peça `BLProva.jensen_y`)

Com δ = 1/4: R = 1,375, r = 1,3125, λ = log(R/r) = 0,04652, L₀ = −log(2 − π²/6) = 1,03545. A cota de zeros com
Re > 3/4 numa janela |Im − y| ≤ 1/8 é (média(|ζ|², 2+iy, R) + L₀)/λ:

| y | 2 | 5 | 10 | 14,13 | 20 | 50 | 100 | 200 | 400 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| média(\|ζ\|²) | 0,98 | 0,75 | 1,49 | 0,62 | 1,14 | 0,75 | 1,62 | 4,08 | 1,91 |
| cota por janela | 43 | 39 | 54 | 36 | 47 | 38 | 57 | 110 | 63 |

O número verdadeiro é 0 em todas as janelas: todos os zeros com altura até 3·10¹² estão na linha (Platt–Trudgian 2021).
A janela inteira, mesmo na linha, contém em média ~0,17 zero perto de y = 400. Jensen é grosseiro e só precisa ser
**uniforme**.

## 3. A constante da prova e o que ela diz

Com M ≈ 3,00 a prova dá C = (5M/2 + L₀)/(λδ) ≈ 734 para δ = 1/4. A contagem total de zeros N(T) ~ (T/2π) log(T/2πe)
só passa de 734·T a partir de T ≈ 10²⁰⁰⁵. Portanto:

* **O teorema é qualitativo.** "Quase todos os zeros estão a menos de δ de 1/2" é uma afirmação assintótica. Com
  estas constantes, ela só tem conteúdo numérico para alturas astronomicamente grandes.
* Isto **não** é uma fraqueza da formalização. É a natureza do argumento de Bohr–Landau. Versões quantitativas
  (Selberg, Ingham, Guth–Maynard) precisam de ferramentas bem mais finas e não estão no kernel.
* O que o kernel agora tem de incondicional: N(1/2 + δ, T) = O(T) (`bohrLandau`), o mesmo à esquerda
  (`bohrLandau_esquerda`), a soma dos dois lados (`fora_da_faixa`), e "zeros distintos vão para o infinito"
  (`zeros_escapam`). O que segue condicional: a densidade (`Densidade`) depende só de B10, o crescimento N(T)/T → ∞
  (`densidade_de_crescimento`). E RH segue aberta.
