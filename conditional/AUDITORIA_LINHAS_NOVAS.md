# Auditoria das declarações de `ATK/LinhasNovas.lean`

Commit compilado: `7fdcc61` (Lean 4.34.1, Mathlib `v4.34.1`, compilação local com `lake env lean`).
Comandos: `#check @<nome>` e `#print axioms <nome>` com o nome completamente qualificado.
Resultado: **21 entradas (20 declarações e o construtor `NaturalFinal.mk`), 0 com `sorryAx`**; todas usam no máximo
`propext`, `Classical.choice` e `Quot.sound`.

| Nome qualificado | Tipo | Axiomas |
|---|---|---|
| `ATK.LinhasNovas.NaturalFinal.mk` | `(N : ℕ) → N + 1 = N → NaturalFinal` | nenhum |
| `ATK.LinhasNovas.natural_final_vazio` | `IsEmpty NaturalFinal` | propext, Quot.sound |
| `ATK.LinhasNovas.sem_ultimo_natural` | `¬∃ N, ∀ (n : ℕ), n ≤ N` | propext, Quot.sound |
| `ATK.LinhasNovas.enat_final` | `⊤ + 1 = ⊤ ∧ ∀ (n : ℕ), ↑n < ⊤` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.enat_sem_cancelamento` | `⊤ + 1 = ⊤ + 0 ∧ 1 ≠ 0` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.sem_maior_negativo` | `¬∃ r < 0, ∀ x < 0, x ≤ r` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.int_maior_negativo` | `-1 < 0 ∧ ∀ x < 0, x ≤ -1` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.um_terco_cauda_infinita` | `¬CaudaFinita (1 / 3)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.raiz_dois_cauda_infinita` | `¬CaudaFinita √2` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.inv_inf` | `inv infinito = some 0` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.inv_zero` | `inv (some 0) = infinito` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.neg_inf` | `neg infinito = infinito` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.inv_inv` | `∀ (x : RetaProj), inv (inv x) = x` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.inv_neg` | `∀ (x : RetaProj), inv (neg x) = neg (inv x)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.centro_reflexao` | `∀ (a x : ℝ), a - x = x ↔ x = a / 2` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.centro_rh` | `∀ (σ : ℝ), 1 - σ = σ ↔ σ = 1 / 2` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.centro_bsd` | `∀ (s : ℝ), 2 - s = s ↔ s = 1` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.centro_bsd_normalizado` | `∀ (s : ℝ), 2 - s - 1 / 2 = 1 - (s - 1 / 2)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.centro_hodge_normalizado` | `∀ {n p q : ℝ}, n ≠ 0 → p + q = n → q / n = 1 - p / n ∧ (p = q ↔ p / n = 1 / 2)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.aproximacao_trivial` | `∀ (L : Set (List Bool)) (w : List Bool), ∀ᶠ (k : ℕ) in Filter.atTop, w ∈ truncamento L k ↔ w ∈ L` | propext, Quot.sound |
| `ATK.LinhasNovas.truncamento_finito` | `∀ (L : Set (List Bool)) (k : ℕ), (truncamento L k).Finite` | propext, Classical.choice, Quot.sound |

## Ressalvas matemáticas (auditoria ATK-O1)

1. **Reta projetiva**: `inv`, `neg` e `infinito` são definidos em `RetaProj = Option ℝ`, não na
   divisão de `ℝ` (onde a Mathlib convenciona `0⁻¹ = 0`).
2. **Centro de BSD**: a simetria original `s ↦ 2 − s` tem centro **1** (`centro_bsd`). Só na
   coordenada `t = s − ½` a mesma simetria fica `t ↦ 1 − t`, de centro ½
   (`centro_bsd_normalizado`). O centro não muda; muda a coordenada.
3. **Truncamentos**: `aproximacao_trivial` vale para toda linguagem. Não fornece algoritmo
   polinomial uniforme nem limite inferior, e não decide P vs NP.

Nenhuma dessas declarações é produtora de O1–O8; OPEN_MATH inalterado.

CI: runs 318, 324 e 326 `success`; 327–329 em andamento no momento desta auditoria.
