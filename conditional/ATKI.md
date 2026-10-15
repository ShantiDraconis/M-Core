# ATK-I no kernel (14/10/2026)

Formalização das partes demonstráveis dos textos ATK-I: estados, certificados, fechamento por
defeito, números relacionais e os sete cálculos concretos. `ATK/ATKI.lean` (50 teoremas) e
`ATK/ATKIExemplos.lean` (18).

## O que entrou

| Peça | Conteúdo | Teoremas |
|---|---|---|
| Classe de três estados | `Nada < I < Todo`; inversão involutiva que fixa só `I`; `⊕ = máx`, `⊗ = mín`; De Morgan, idempotência, comutatividade, associatividade, distributividade; é a K3 do kernel | `Estado.inv_inv`, `inv_fixo_iff`, `de_morgan_*`, `distrib`, `paraK3_*` |
| Defeito | `Δ(d) = Nada ⟺ d = 0`; com defeitos não negativos, `máx qⱼ = 0 ⟺ todos os qⱼ = 0` | `detecta_nada_iff`, `defeito_global_zero_iff` |
| Certificados | `Cert P` = provado / refutado / aberto. `Todo` só com prova, `Nada` só com refutação, `aberto` nunca é `Todo`; a conjunção tem o estado `⊗`; sete `Todo` dão os sete enunciados | `Cert.sound_todo`, `sound_nada`, `aberto_nao_todo`, `estado_and`, `universal` |
| Fechamento por defeito majorado | `T ↔ d = 0`, `0 ≤ d ≤ εₙ`, `εₙ → 0` ⟹ `T`; transferência; composição de pontes | `fechamento_por_defeito`, `transferencia`, `ponte_composta` |
| Números relacionais `(a R b)` | seis relações; `J(a R b) = (−a R* −b)`, troca de lados, escala `Sₖ`, translação `Tₐ`; `J² = id`, `SₖSₗ = Sₖₗ`, `TₐT_b = T_{a+b}`; `J` e `Sₖ` como `Equiv`; ação de `ℝ` por translações (`AddAction`); `J`, troca, translação e escala positiva preservam a verdade | `RelNum.neg_neg`, `scale_scale`, `transl_transl`, `negEquiv`, `scaleEquiv`, `holds_*` |
| Retorno ≠ verdade | `(0 > 1)` é falso e volta a si mesmo por `J²` | `retorno_nao_implica_verdade` |
| Ciclo do texto | `(3 > 0) → (6 > 0) → (−6 < 0) → (−3 < 0) → (3 > 0)`, com a verdade preservada em cada passo | `ciclo_quatro`, `ciclo_preserva_verdade` |
| Compatibilidade | `interpretar ∘ J = interpretar`, `interpretar ∘ Sₖ = interpretar` (`k > 0`) | `compat_neg`, `compat_scale` |
| Defeitos de aproximação | `D N = inf_c Σ wₖ (1 − Σ cₘ gₘ(k))²` é ≥ 0, decrescente e converge; `D∞ = 0 ⟺ ∀ ε > 0, ∃ N, D N < ε`; instância na família do texto (`ρₘ(k) = (k mod m)/m`, pesos `1/(k(k+1))`) | `defeito_antitone`, `defeito_converge`, `defeito_limite_zero_iff`, `texto_converge` |

## Os sete cálculos (`ATK/ATKIExemplos.lean`)

| Classe | Cálculo verificado |
|---|---|
| P vs NP | `(x ∨ y) ∧ (¬x ∨ y)` é satisfatível; `(x ∨ y) ∧ (¬x ∨ z)` tem 4 de 8 atribuições |
| Navier–Stokes | `u = (A e^{−νt} sin y, 0, 0)`, `p = 0`: `∂ₜu₁ = ν ∂²_y u₁`, e o termo não linear e a divergência são nulos |
| Yang–Mills | `[σ₁, σ₂] = 2i σ₃`; `diag(0, 2, 5)` tem autovetores `eᵢ` e gap `2` |
| BSD | `y² = x³ − x`: `Δ = 64`, `c₄³ = 1728·Δ` (`j = 1728`), 2-torção total, posto 0 |
| Hodge | no modelo algébrico `ℚ[h]/(h³)`: `h³ = 0`, `⟨a h, b h⟩ = a b`, `⟨3h, 2h⟩ = 6` |
| Beal | `3³ + 6³ = 3⁵`, `mdc(3, 6, 3) = 3`, valorações 3-ádicas `3, 3, 5` |
| RH | o `D N` da família do texto decresce e converge (seção anterior) |

## A ponte de Bagchi (`ATK/ATKIBagchi.lean`, 20 teoremas)

`rh_of_texto : (⨅ N, Defeito wTexto gTexto N) = 0 → RiemannHypothesis`, com a `RiemannHypothesis`
da Mathlib e sem hipóteses. A prova é a isometria de Bagchi:

1. `{t/q} = {⌊t⌋/q} + {t}/q`, logo `ρ_q(x) − ρ_1(x)/q = {⌊1/x⌋/q}` (`rho_sub`), com
   `ρ_k(x) = {1/(kx)}` a família de Báez-Duarte;
2. para cada vetor `c` do texto, `c' = (−Σ c_m/(m+2), c)` dá um resíduo de Báez-Duarte nulo em
   `(1, ∞)` e constante `1 − Σ c_m γ_{m+2}(n)` em `(1/(n+1), 1/n]` (`res_on_faixa`);
3. logo as duas distâncias coincidem (`residualSq_coefBD`) e `D^{BD}_{N+1} ≤ D^{texto}_N`
   (`DN_succ_le`);
4. `D∞ = 0` ⟹ `D^{BD}_N → 0` ⟹ RH pela ponte B1 já provada (`baezDuarteCriterion`).

Também: `rh_of_texto_eps` (forma `∀ ε > 0, ∃ N, D_N < ε`) e `texto_pos_of_not_rh` (se RH é
falsa, o `D∞` do texto é estritamente positivo). Isto liga o `D∞` do ATK-I à RH, mas não prova
`D∞ = 0`: esse é o passo aberto, equivalente à própria RH.

## Pares relacionais, proximidade e normalização (`ATK/ATKINormal.lean`, 33 teoremas)

* `Par` é o objeto `(a = b)`; `vale ↔ a = b ↔ defeito |a − b| = 0`; escala e potência
  componente a componente.
* Ordem de proximidade `R ⪰ S ↔ defeito R ≤ defeito S`: pré-ordem total, não antissimétrica
  (`(0 = 1)` e `(1 = 0)`), com as relações que valem no topo.
* **`(0 = 1)·3 ⪰ (2 = 1)³`**: `(0 = 3) ⪰ (8 = 1)`, defeitos `3 ≤ 7` (`exemplo_proximidade`). Pela
  diferença (`−3 ≥ 1`), componente a componente e com infinitésimo hiper-real (`−3ε ≥ (2 − ε)³`)
  a desigualdade é falsa: o resultado depende da ordem escolhida.
* Normalização `T_t(a = b) = ((1 − t)a + tb = b)`: `T₀ = id`, `T_s ∘ T_t = T_{s+t−st}`,
  `T₁ ∘ T₁ = T₁`, `defeito(T_t R) = |1 − t|·defeito R`, estabilidade nas relações que valem,
  monotonia da ordem; `D_x(R) = defeito R/(1 + x) → 0`; o desvio de `T_{x/(1+x)}(0 = 1)` vai a 0.
* **Normalizar não é provar**: `T₁(0 = 1) = (1 = 1)` vale e `(0 = 1)` não; para `t ≠ 1`, `T_t` não
  muda a verdade; `T₁(D∞ = 0) = (0 = 0)` qualquer que seja `D∞`. Já `(D∞ = 0)` **valer** implica
  RH (`vale_D_infinito_RH`, pela ponte de Bagchi).

## Álgebra relacional completa (`ATK/ATKIAlgebra.lean`, 28 teoremas)

* Operações componente a componente nos pares `(a = b)` e as leis de anel comutativo (comutatividade,
  associatividade, distributividade, zero, um, oposto); a diagonal das relações verdadeiras é
  fechada por soma, produto e escala.
* Defeito: simetria, `d(R ⊕ S) ≤ d(R) + d(S)`, `d(R ⊗ S) ≤ |c|·d(R) + |b|·d(S)` e a fatoração
  exata `d(Rⁿ) = d(R)·|Σ aⁱ bⁿ⁻¹⁻ⁱ|` (`|2 − 1|·7 = 7`). A potência pode apagar o defeito:
  `(−1 = 1)` é falsa e `(−1 = 1)² = (1 = 1)`.
* O quociente por "mesmo defeito" não preserva a soma: `(1 = 0) ∼ (0 = 1)`, mas as somas com
  `(1 = 0)` têm defeitos 2 e 0.
* Três estados por tolerância (verdade / aproximada / longe); `(0 = 1)` com `τ = 1/4` está longe.
* `(ε = 0)` nos hiper-reais: defeito positivo e menor que todo real positivo. Defeito
  infinitesimal não é defeito zero.
* Fechamento simultâneo: `Σ wᵢ dᵢ/(1 + dᵢ) = 0 ⟺ os sete dᵢ = 0` e `Σ wᵢ (aᵢ − bᵢ)² = 0 ⟺ ∀ i, aᵢ = bᵢ`.

## Aplicações às sete conjecturas (`ATK/ATKIAplicacoes.lean`, 25 teoremas)

| Problema | O que foi provado | O que continua aberto |
|---|---|---|
| RH | `Σ_N (D_N − D_{N+1}) = D_0 − D∞`, `D_0 = Σ 1/((k+1)(k+2)) = 1`; `Σ_N (D_N − D_{N+1}) = 1 ⟹ RH` (Bagchi) | provar que a soma dos ganhos é 1 |
| Yang–Mills | coercividade `⟪ψ, Hψ⟫ ≥ δ‖ψ‖²` em `Ω^⊥` ⟹ autovalores em `Ω^⊥` são `≥ δ`; gaps `1/(n+1) > 0` somem no limite | construir `H` em 4D e a coercividade |
| Navier–Stokes | absorção com `c < 1` ⟹ `Y' ≤ 2CY` ⟹ `Y(t) ≤ Y(0) e^{2Ct}` (Grönwall); `δ = 5/12` | a absorção para NS 3D sem supor regularidade |
| BSD | defeito de posto `< 1` ⟹ postos iguais; cotas `[2, 2]` fecham; `det !![2,1;1,3] = 5`, `h₂₂ = 3` | as cotas para toda curva |
| Hodge | `2z₁ + 3z₂ = α`; transição `D(t) = 10(1 − t)`; lei de contração `f(q(t)) − α = (1 − t)(f(q₀) − α)`, que pressupõe a solução exata | os ciclos algébricos |
| P vs NP | `∀N ∃m, m > N` vale e `∃m ∀N, m > N` não; `2ⁿ` atribuições; aproximação finita trivial; erro `1/(n+1) → 0` sem zerar | excluir todo algoritmo polinomial |

Também os números do navio do texto (`Re = 1,6·10⁹`, `q = 32800 Pa`), só como aritmética.

## O que isto não é

* Nenhum teorema aqui prova uma conjectura nem toca uma obrigação O1–O8.
* A família discreta do texto (`ρₘ(n) = {n/m}`, pesos `1/(n(n+1))`) é exatamente a do teorema 1 de
  Bagchi (2006, arXiv:math/0607733): **RH ⟺ a sequência constante 1 está no fecho do span de
  `{n/m}` nesse espaço ⟺ `D∞ = 0`**. Logo `D∞ = 0` não é um enunciado novo: é RH. A direção
  `D∞ = 0 ⟹ RH` está **provada no kernel** (`ATK/ATKIBagchi.lean`, abaixo); a recíproca não está
  formalizada, e `D∞ = 0` continua **aberto**. O valor `D₁ = 1 − ln 2` do texto não foi formalizado.
* O modelo de Hodge é só a álgebra `ℚ[h]/(h³)`; a Mathlib não tem `H*(ℂP², ℚ)`.
* O gap de `diag(0, 2, 5)` não é o gap de Yang–Mills.
* `Cert` torna explícito o que os textos dizem: classificar como `I` ou `Todo` não prova nada; só
  o construtor `provado`, que exige uma prova de `P`, chega a `Todo`.

`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
