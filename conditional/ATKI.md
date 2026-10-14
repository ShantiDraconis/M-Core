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

## O que isto não é

* Nenhum teorema aqui prova uma conjectura nem toca uma obrigação O1–O8.
* A família discreta do texto (`ρₘ(k) = (k mod m)/m`, pesos `1/(k(k+1))`) **não** é o `D_N` de
  Báez-Duarte da ponte B1: não há ponte provada entre o seu `D∞` e RH. O valor `D₁ = 1 − ln 2` do
  texto não foi formalizado (a Mathlib não tem a série harmônica alternada como `log 2`).
* O modelo de Hodge é só a álgebra `ℚ[h]/(h³)`; a Mathlib não tem `H*(ℂP², ℚ)`.
* O gap de `diag(0, 2, 5)` não é o gap de Yang–Mills.
* `Cert` torna explícito o que os textos dizem: classificar como `I` ou `Todo` não prova nada; só
  o construtor `provado`, que exige uma prova de `P`, chega a `Todo`.

`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
