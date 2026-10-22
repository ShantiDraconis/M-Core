# Rodada 5 — ATK–Closed Math completo, toro e redução terminal de HR

Kernel: `ATK/ClosedMathCEZ.lean`, `ATK/ClosedMathCompleto.lean`, `ATK/ClosedMathToro.lean`,
`ATK/RHTerminal.lean`, `ATK/Cert/Intervalo.lean`, `ATK/Cert/Transc.lean` (Lean 4.34.1 + Mathlib,
axiomas só `propext`, `Classical.choice`, `Quot.sound`). Espelhos em Coq, Isabelle/HOL, SMT-LIB 2,
TPTP e Python em `formatos/` e `pesquisa/rodada5/` (workflow `closed-math-multiprovador`).

**Nada aqui prova ou refuta a Hipótese de Riemann.** O último teorema mostra exatamente o contrário:
a desigualdade "global" pedida é equivalente a HR.

## 1. O que foi provado (escopo modelo — `UGModelo`, provado)

| Bloco | Resultado no kernel |
| --- | --- |
| Semântica | `classificacao` (C/E/N_C/N_E exaustivos), `exclusivos` (6 pares), "ambos" só para famílias |
| Verificador | `checar_correto` (todo veredito traz prova), `checar_nunca_zero` (invólucro nunca prova igualdade), `nao_zero_certificavel` (não zero é semidecidível), `zero_sempre_indeterminado`, `indeterminado_nao_e_estado`; `checarIC` racional, decidido pelo kernel |
| Operadores | grupo de Klein `{I, J, R, S}`, `T` involução e isometria que não comuta com `R`, `T R T (w) = w̄ + i` |
| Modelo `G_{d,γ}` | P1–P5: zeros `½ ± d ± iγ`, crítico, externo, trajetória "ambos", não zeros `2 ∈ N_E` e `½ ∈ N_C` com `G(½) = (d² + γ²)²` |
| Cruzamento | expansão quártica, velocidades ±1, aceleração 0, separação `2|λ|` **não diferenciável** no encontro, **conservação**: `card roots = 4` para todo `λ`, multiplicidade 2 no encontro e 1 fora |
| Geometrias | corda esférica `4|s−w|²/((1+|s|²)(1+|w|²))`, cilindro injetivo em `0 < Re < 1` e periódico fora, `d_C = 2|sin 2πδ|` com derivada `4π`, cone que **perde** a ordenada (`cone_nao_decide_zero`), cone elevado injetivo |
| Taxonomia | ordem por derivadas, `(z−2)^m` de ordem `m`, zeros `±a, ±ib`, `sin πz = 0 ⟺ z ∈ ℤ` (infinitos), zero de ordem 2 no infinito de `1/z²`, `(x²−1)/(x−1) → 2` (direto e por L'Hôpital, com `0/0 = 0` como convenção ≠ limite), derivada logarítmica, **princípio do argumento** para `(z−a)^m g` e para multiconjuntos, exemplo `(1/2πi)∮ f'/f = 5 − 2 = 3`, truncamentos decimais de 1/3 nunca são zeros, teorema da identidade, multiplicidade infinita ⇒ `f ≡ 0` |
| Modelo `H_{d,γ}` | `q_{½} q_{½+d} q_{½−d} / Γ(1 + s/2)`: inteira, zeros triviais `−2, −4, …`, conjunto completo de zeros, `H_{¼,1}(½) = 289/(256 Γ(5/4))`, **ordem 3** no encontro (`d = 0`) e 1 fora, `(1/2πi)∮ H'/H = 6` nos dois regimes, a reflexão não preserva os triviais |
| Pontes | transporte `G(φ s) = u(s) F(s)` (e falha sem `u ≠ 0`), B17 (fator analítico não nulo preserva a ordem), singularidade removível, `ξ(1 − s) = ξ(s)`, **B20**: `ξ = 0 ⟺ ζ = 0` na faixa |

## 2. Toro

`𝕋(s) = ((R + r cos 2πσ) cos(2πt/T), (R + r cos 2πσ) sin(2πt/T), r sin 2πσ)`, `R > r > 0`.

* Superfície exata; dupla periodicidade (perde `Re mod 1` e `Im mod T`); toro elevado `(𝕋(s), Im s)` injetivo na faixa.
* `R` = espelho `z ↦ −z`; `J` = espelho `y ↦ −y`; `S = 1 − s` = rotação de π em torno de `x`, com exatamente os
  pontos fixos `σ ∈ ½ℤ, t ∈ (T/2)ℤ` (quatro por célula: o quociente é a "fronha" de 4 pontos cônicos).
* A linha crítica é o **equador interno** (raio `R − r`) e, na faixa, `z = 0 ⟺ Re s = ½`. Logo
  **`rh_iff_equador`: HR ⟺ todo zero não trivial cai no equador interno** (reformulação exata, não prova).
* Curvatura (Brioschi, a partir de `E = r², F = 0, G = (R + r cos θ)²` derivados da imersão):
  `K = cos θ / (r(R + r cos θ))`. Na linha crítica `K = −1/(r(R − r))`, **o mínimo global**; a região `K < 0` é
  exatamente a faixa central `¼ < σ < ¾`. Área `4π²Rr`; curvatura total `0` (Gauss–Bonnet, χ = 0).
* Par simétrico: distância `2r|sin 2πδ|`. **Reencontro artificial**: em `λ = ½` os ramos `0 + iγ` e `1 + iγ`
  coincidem no toro, mas seguem zeros distintos e simples no plano.
* Fluxo de cruzamento `Φ_λ(s) = s + λ`: grupo a um parâmetro; os zeros de `G_λ` são órbitas dos críticos;
  no toro atravessa o equador **transversalmente** (velocidade vertical `−2πr`); conjugado por `T` vira vertical.

Constantes (R = 3, r = 1, T = 28; `closed_math.json`): raio do equador interno 2; `K(π) = −0,5`;
`K(0) = 0,25`; área 118,4352528131 = 4π²·3; Gauss–Bonnet numérico −2·10⁻¹⁵; distância do par
½ ± 0,1 + 14i: 1,1755705046 (= 2 sin(0,2π)); corda esférica do mesmo par 0,0020277809 (ângulo 0,0020277812).

## 3. Tempos verbais

`Afirmacao` carrega enunciado, tempo e a testemunha que o tempo **exige** (o tipo obriga):
*perfeito* (foi provado ⇒ prova), *negado* (foi refutado ⇒ prova da negação), *condicional* (seria, se `H` ⇒ `H → P`),
*futuro* (aberto ⇒ nada), *presente* (observado numericamente ⇒ nada). `futuro_vazio`: `P` e `¬P` cabem no futuro.
Catálogo: classificação (perfeito), "simetria força a linha" (negado), HR ⟺ ZE = ∅ (perfeito), zeros no equador
interno (condicional a HR), HR (futuro).

## 4. Redução terminal (`ATK/RHTerminal.lean`)

* `T25`: HR ⟺ ζ ≠ 0 em `S₊ = {½ < Re < 1}` (e o mesmo para ξ).
* `cobertura`: `S₊ = ⋃_{n≥5} K_n`; `K_n` compacto e não vazio.
* `rh_iff_minimos`: HR ⟺ para todo `n ≥ 5`, `|ζ|` tem mínimo positivo em `K_n`.
* `rh_iff_delta`: com `η(s) = (1 − 2^{1−s}) ζ(s)` e `δ_n = min_{K_n} |η|` (mínimo atingido, `delta_atingido`),
  **HR ⟺ ∀ n ≥ 5, δ_n > 0**; `eta_zero_iff`: em `K_n`, `η = 0 ⟺ ζ = 0` (o fator `1 − 2^{1−s}` não se anula para `Re s < 1`).
* `criterio_aproximacao` (T28) e `T31_iff`: HR ⟺ existe aproximante com `E_n < L_n` em cada `K_n`.
* **Aproximante explícito, independente de HR**: `EM_uniforme`: `|ζ − EM_{N,M}| ≤ E(n,N,M)` em todo `K_n`, com
  `E(n,N,M) = (√(1+n²)+M)^M/M! · C_M · N^{½−M}/(M − ½)` e `Eb_tende_zero`.
* **`rh_iff_criterioEM`: HR ⟺ ∀ n ≥ 5, ∃ N M L, L ≤ |EM_{N,M}| em K_n e E(n,N,M) < L.**

Instâncias com `n` fixo (tempo *presente*, grade numérica, `N = 40`, `M = 10`):

| n | E(n,40,10) (cota provada) | min \|EM\| em K_n (grade) |
| --- | --- | --- |
| 5 | 2,9·10⁻¹⁰ | 0,574 |
| 10 | 5,0·10⁻⁹ | 0,550 |
| 15 | 4,6·10⁻⁸ | 0,0526 |
| 20 | 2,8·10⁻⁷ | 0,0394 |
| 30 | 5,0·10⁻⁶ | 0,0261 |

A queda em `n = 15` é o primeiro zero (14,1347…): `K_15` chega a `t = 15` e passa a `1/n` dele.
Cada linha é uma conta finita; transformá-la em certificado do kernel exige avaliação intervalar de ζ em
retângulos (fase 3). O quantificador `∀ n` é a própria HR: **não há aqui prova da desigualdade universal**.

## 5. Formatos

| Formato | Verificador | Conteúdo |
| --- | --- | --- |
| Lean 4 + Mathlib | kernel (`lake build`, `#print axioms`) | tudo acima |
| Coq (Rocq) | `coqc` + `coqchk` (CI) | semântica, operadores, modelo G, P1–P5, quártica, esfera, cilindro, cone, toro, curvatura, pontes, T28, tempos |
| Isabelle/HOL | `isabelle build` (CI) | idem, com complexos nativos |
| SMT-LIB 2 | z3 / cvc5 (CI) | 12 obrigações negadas, espera-se `unsat` |
| TPTP | E prover (CI) | classificação, redução terminal (forma lógica), tempos |
| Python | `pytest` (+ SymPy) | aritmética exata em ℚ[i], contornos, toro, critério |

Este ambiente não tem Coq nem Isabelle (rede bloqueada para instalá-los): esses verificadores rodam no
GitHub Actions e só contam como verificados quando o job do CI passa.
