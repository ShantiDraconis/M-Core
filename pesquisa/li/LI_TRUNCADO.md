# Critério de Li: truncagens, o sinal e a obstrução de Davenport–Heilbronn (rodada 108)

Kernel: `atk-kernel/ATK/LiTruncado.lean` (27 teoremas, só Mathlib) e `atk-kernel/ATK/LiTruncadoPonte.lean` (2).
Numérico: `codigo/li_tabela.py`, `dados/lambda_ate_10000.tsv`, `testes/test_li.py`.
Classificação: **reformulação/consequência**. RH continua `OPEN_MATH`.

## 1. De onde veio

Um texto propôs fechar RH com um "Lema 2": provar `λₙ ≥ 0` para todo `n` reescrevendo `λₙ` "só com `π` e `Γ`" e
usando a convexidade de `log Γ`. Três correções:

- **`λₙ ≥ 0 ∀n` já é equivalente a RH.** É o critério de Li, que está no kernel desde a rodada 68
  (`ATK.ZeroClasses.LiCompleto.rh_iff_li`). O núcleo zero a zero é da rodada 15 (`ATK.Li`), e
  `λ₁ = 1 + γ/2 − ½ log 4π` é da rodada 69 (`LiUm`). Um artigo com o "Lema 2" como conjectura deixa a própria RH
  como hipótese.
- **Os números do texto (0,015; 0,063; 0,14) não são `λ₁, λ₂, λ₃`.** São somas sobre os 20 primeiros zeros:
  aqui deram 0,016; 0,0638; 0,1434, contra `λ₁ = 0,0230957…`, `λ₂ = 0,0923457…`, `λ₃ = 0,2076389…`. Para zeros
  na reta, cada parcela é `1 − cos(nθ) ≥ 0` (Lei 1), então essa soma é positiva por construção.
- **A convexidade de `log Γ` não decide o sinal.** A Lei 5 mostra isso no começo da sequência; a Lei 6 mostra o
  motivo geral (Davenport–Heilbronn).

## 2. As leis no kernel

| Lei | Teoremas | Enunciado |
| --- | --- | --- |
| 1 | `norm_w_sq_sub_one`, `w_fora_iff`, `w_le_one_iff`, `re_um_sub_pow_nonneg`, `liS_nao_negativo` | `|w(ρ)|² − 1 = (1 − 2 Re ρ)/|ρ|²`, com `w(ρ) = 1 − 1/ρ`. Se `Re ρ ≥ ½`, cada parcela tem `Re(1 − wⁿ) ≥ 0`. |
| 2 | `dirichlet_simultaneo`, `re_pow_eq`, `re_soma_pot_ilimitada`, `liS_ilimitado` | Numa família finita qualquer, basta **um** ponto com `Re ρ < ½` para `λₙ(S)` ficar abaixo de qualquer `−M`, para `n` arbitrariamente grande. Nenhuma quantidade finita de zeros na reta compensa um zero fora. |
| 3 | `liS_criterio` | Critério de Li finito: `(∀n, λₙ(S) ≥ 0) ⟺ ∀ρ ∈ S, Re ρ ≥ ½`. |
| 4 | `finito`, `zerosAte`, `liT`, `existe_zero_esquerda`, `liT_nao_negativo`, `liT_mono`, `liT_ilimitado`, **`rh_iff_liT`** | **RH ⟺ toda truncagem `λₙ^{(T)} ≥ 0`**. `λₙ^{(T)}` soma sobre os zeros não triviais com `‖ρ‖ ≤ T`, que são finitos (`IsCompact.inter_riemannZetaZeros_finite` do Mathlib). Sob RH, `λₙ^{(T)}` cresce com `T`. Se RH falhar, toda truncagem acima da altura do zero fora desce a `−∞`. |
| 4′ | `Ponte.liT_le_lam` | Sob RH, `λₙ^{(T)} ≤ λₙ`, onde `λₙ` é o `lam` completo da rodada 68 (com multiplicidades). |
| 5 | `principal_negativo` | O termo principal `(n/2)(log n − 1 + γ − log 2π)`, a parte que vem de `π` e `Γ`, é **negativo para 1 ≤ n ≤ 6** (o kernel usa `γ < 2/3`; numericamente vale até `n = 9`). Mesmo assim `λₙ > 0` ali. O sinal no começo vem da parte dos primos. |
| 6 | `dh_taxa`, `dh_obstrucao` | Zero de Davenport–Heilbronn, certificado por Newton intervalar no Arb e usado aqui como hipótese: `β + iγ = 0,80851718245663738555 + 85,699348485377592172i`. O refletido `σ = 1 − β + iγ` tem `|w(σ)|² − 1 ∈ (84014; 84015)·10⁻⁹`, então a parcela dele cresce como `e^{4,2006·10⁻⁵ n}`. Toda soma de Li finita que contém `σ` é ilimitada para baixo. |

**Por que a Lei 6 é a obstrução.** `f` (Davenport–Heilbronn) tem a mesma equação funcional, o mesmo
`Γ((s+1)/2)` e a mesma potência de `π` que `L(s, χ mod 5)`. O critério de Bombieri–Lagarias vale para qualquer
multiconjunto simétrico de zeros (a Lei 3 é o caso finito). Logo `λₙ(f) < 0` para algum `n`. Qualquer argumento
de positividade que use só `π`, `Γ`, convexidade e a equação funcional valeria também para `f`, e por isso é falso.
A prova teria de usar o produto de Euler, que `f` não tem.

## 3. Numérico

**`λₙ` sem zeros.** Rodei `keiper_li` (FLINT/Arb 3.3.1, exemplo de F. Johansson) com `n ≤ 10 000`,
`prec = 10 600`. O tempo foi de 95 s e o pico de memória 450 MB. Ele expande `log ξ` em `s = 1` e nunca usa
zeros. As bolas certificam **`λₙ > 0` para 1 ≤ n ≤ 10 000** (`dados/lambda_ate_10000.tsv`, coluna
`cota_inferior`). Raio relativo máximo: `3·10⁻¹⁴³`.

| n | λₙ | termo principal (n/2)(log n − 1 + γ − log 2π) |
| ---: | ---: | ---: |
| 1 | 0,0230957090 | −1,1303 |
| 2 | 0,0923457352 | −1,5675 |
| 4 | 0,3687904795 | −1,7487 |
| 9 | 1,8509160484 | −0,2855 |
| 10 | 2,2793393632 | 0,2096 |
| 100 | 118,6037753768 | 117,2254 |
| 1 000 | 2 326,0531616865 | 2 323,5469 |
| 10 000 | 34 736,5797322416 | 34 748,3949 |

Este cálculo **não é um recorde**. Johansson (2015) foi a `n = 10⁵`, citado por Voros (2017). O
`RH_frontier.md` dizia "n ≈ 2550–4000"; está corrigido. Ir além de `10⁵` aqui não cabe na memória: cada vetor da
série tem `n` números de `≈ n` bits.

**Truncagens com zeros na reta** (nossos 10 001 zeros certificados):

| n | só os 20 primeiros zeros | só os 10 001 primeiros | λₙ |
| ---: | ---: | ---: | ---: |
| 1 | 0,0160 | 0,0230 | 0,0230957 |
| 2 | 0,0638 | 0,0918 | 0,0923457 |
| 3 | 0,1434 | 0,2064 | 0,2076389 |

As truncagens crescem com `T` e ficam abaixo de `λₙ` (Leis 4 e 4′). Isso vale **por supor** os zeros na reta;
não é evidência de RH.

**Davenport–Heilbronn: onde `λₙ(f)` fica negativo (estimativa, não calculada).** O par fora da reta contribui
`2 − 2e^{4,2006·10⁻⁵ n} cos(nφ)`, com `φ ≈ 1/85,7` (período ≈ 538 em `n`). A parte regular é
`≈ (n/2)(log 5n − 1 + γ − log 2π)`. As duas se cruzam em **`n ≈ 3,3–3,4·10⁵`**, supondo que o par de altura 85,7
domina; os outros pares fora da reta são mais altos e crescem mais devagar. Calcular `λₙ(f)` até aí exigiria cerca
de `3·10⁵` bits por coeficiente e uma série desse comprimento, o que não cabe nesta máquina. Voros (2017, §4.4)
estudou o mesmo `f₊` na versão discretizada do critério e estimou o limiar de detecção em `≈ 3·10¹⁴`.

## 4. O que continua aberto

- A RH, isto é, `λₙ ≥ 0` para todo `n`.
- A fórmula aritmética de Bombieri–Lagarias (`λₙ = S_∞(n) − S_f(n) + …`, com `S_f` sobre os primos) não está no
  kernel. Ela localizaria formalmente o sinal na parte dos primos.
- Ligar `lam` (soma sobre zeros) às derivadas de `log ξ` em `s = 1` (a definição de Keiper). Isso tornaria a
  tabela certificada acima um teorema do kernel. O produto de Hadamard (`hadamardXi`) já está lá.

## Referências

- X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65 (1997).
- E. Bombieri, J. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory 77 (1999).
- J. B. Keiper, *Power series expansions of Riemann's ξ function*, Math. Comp. 58 (1992).
- F. Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its derivatives*,
  Numer. Algorithms 69 (2015).
- A. Voros, *Discretized Keiper/Li approach to the Riemann Hypothesis*, arXiv:1703.02844 (2017), §4.4.
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series I, II*, J. London Math. Soc. 11 (1936).
