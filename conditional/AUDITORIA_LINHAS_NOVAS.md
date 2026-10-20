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

## Extensão: `LinhasNovasII`, `LinhasNovasIII` e `DInfinito`

Gerada pelo próprio kernel (`#check @<nome>` e `#print axioms <nome>` em `lake env lean --json`),
Lean 4.34.1, Mathlib `v4.34.1`. **53 declarações, 0 com `sorryAx`**, todas com no máximo
`propext`, `Classical.choice` e `Quot.sound`. Todas entram em `scripts/expected_theorems.txt`;
o `check_axioms.py` do CI rejeita qualquer uma que passe a depender de `sorryAx` ou de axioma fora
do padrão (é esse o portão contra regressão silenciosa).

| Nome qualificado | Tipo | Axiomas |
|---|---|---|
| `ATK.LinhasNovas.Meio.half_fixed_point` | `∀ {α : Type u_1} [inst : Field α] [CharZero α] (a x : α), a - x = x ↔ x = a / 2` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Meio.half_normalized` | `∀ {α : Type u_1} [inst : CommRing α] (a c x : α), a - x - c = a - 2 * c - (x - c)` | propext |
| `ATK.LinhasNovas.Meio.half_center_invariant` | `∀ {α : Type u_1} [inst : CommRing α] (a c x : α), a - x = x ↔ a - 2 * c - (x - c) = x - c` | propext |
| `ATK.LinhasNovas.Truncamento.trunc_monotone` | `∀ {α : Type u_1} (L : Set (List α)), Monotone (ATK.LinhasNovas.Truncamento.trunc L)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Truncamento.trunc_iUnion` | `∀ {α : Type u_1} (L : Set (List α)), ⋃ k, ATK.LinhasNovas.Truncamento.trunc L k = L` | propext, Quot.sound |
| `ATK.LinhasNovas.Truncamento.trunc_injective` | `∀ {α : Type u_1} (L L' : Set (List α)), (∀ (k : ℕ), ATK.LinhasNovas.Truncamento.trunc L k = ATK.LinhasNovas.Truncamento.trunc L' k) ↔ L = L'` | propext, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.inv_some` | `∀ {x : ℝ}, x ≠ 0 → ATK.LinhasNovas.inv (some x) = some x⁻¹` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.inv_fixed` | `∀ (x : ATK.LinhasNovas.RetaProj), ATK.LinhasNovas.inv x = x ↔ x = some 1 ∨ x = some (-1)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.neg_fixed` | `∀ (x : ATK.LinhasNovas.RetaProj), ATK.LinhasNovas.neg x = x ↔ x = some 0 ∨ x = ATK.LinhasNovas.infinito` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.neg_involutive` | `Function.Involutive ATK.LinhasNovas.neg` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.inv_involutive` | `Function.Involutive ATK.LinhasNovas.inv` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.RetaProjetiva.neg_inv_involutive` | `Function.Involutive (ATK.LinhasNovas.neg ∘ ATK.LinhasNovas.inv)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.colapso_inf` | `ATK.LinhasNovas.Colapso.colapso ATK.LinhasNovas.infinito = 0` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.colapso_some` | `∀ (x : ℝ), ATK.LinhasNovas.Colapso.colapso (some x) = x` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.colapso_fiber` | `∀ (x y : ATK.LinhasNovas.RetaProj), ATK.LinhasNovas.Colapso.colapso x = ATK.LinhasNovas.Colapso.colapso y ↔ x = y ∨ x = ATK.LinhasNovas.infinito ∧ y = some 0 ∨ x = some 0 ∧ y = ATK.LinhasNovas.infinito` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.colapso_inv` | `∀ (x : ATK.LinhasNovas.RetaProj), ATK.LinhasNovas.Colapso.colapso (ATK.LinhasNovas.inv x) = (ATK.LinhasNovas.Colapso.colapso x)⁻¹` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.inv_real_fixed` | `∀ (x : ℝ), x⁻¹ = x ↔ x = 1 ∨ x = -1 ∨ x = 0` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Colapso.inv_real_bijective` | `Function.Bijective fun x => x⁻¹` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Cauda.conjunto_countable` | `ATK.LinhasNovas.Cauda.conjunto.Countable` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Cauda.conjunto_dense` | `Dense ATK.LinhasNovas.Cauda.conjunto` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Cauda.nao_corpo` | `3 ∈ ATK.LinhasNovas.Cauda.subanel ∧ 1 / 3 ∉ ATK.LinhasNovas.Cauda.subanel` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.InvolucaoComFixos.centro_fixos` | `∀ {α : Type u_1} [inst : Field α] [CharZero α] (a : α), (ATK.LinhasNovas.InvolucaoComFixos.centro a).fixos = {a / 2}` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.InvolucaoComFixos.invProj_fixos` | `ATK.LinhasNovas.InvolucaoComFixos.invProj.fixos = {some 1, some (-1)}` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.InvolucaoComFixos.negProj_fixos` | `ATK.LinhasNovas.InvolucaoComFixos.negProj.fixos = {some 0, ATK.LinhasNovas.infinito}` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Truncamento.trunc_tabela` | `∀ (L : Set (List Bool)) (k : ℕ), ∃ S, ↑S = ATK.LinhasNovas.Truncamento.trunc L k` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Extras.no_fixpoint_of_cancelative` | `∀ {M : Type u_1} [inst : AddLeftCancelMonoid M] {a : M}, a ≠ 0 → ∀ (x : M), x + a ≠ x` | nenhum |
| `ATK.LinhasNovas.Extras.enat_nao_cancelativo` | `¬∀ (a b c : ℕ∞), a + b = a + c → b = c` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Extras.rat_sem_maior_negativo` | `¬∃ r < 0, ∀ x < 0, x ≤ r` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Extras.caudaFinita_iff` | `∀ (x : ℝ), ATK.LinhasNovas.CaudaFinita x ↔ ∃ n k, x * 10 ^ n = ↑k` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Extras.centro_afim` | `∀ {M : Type u_1} [inst : AddCommGroup M] [inst_1 : Module ℚ M] (a x : M), a - x = x ↔ x = (1 / 2) • a` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.InvolucaoComFixos.ofAffineCenter_fixos` | `∀ {M : Type u_1} [inst : AddCommGroup M] [inst_1 : Module ℚ M] (a : M), (ATK.LinhasNovas.InvolucaoComFixos.ofAffineCenter a).fixos = {(1 / 2) • a}` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.dInf_nonneg` | `0 ≤ ATK.DInfinito.dInf` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.dInf_le_one` | `ATK.DInfinito.dInf ≤ 1` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.tendsto_dInf` | `Filter.Tendsto ATK.Conditional.Riemann.DN Filter.atTop (nhds ATK.DInfinito.dInf)` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.dInf_eq_zero_iff` | `Filter.Tendsto ATK.Conditional.Riemann.DN Filter.atTop (nhds 0) ↔ ATK.DInfinito.dInf = 0` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.piso_no_limite` | `∀ {ρ : ℂ}, riemannZeta ρ = 0 → 1 / 2 < ρ.re → ρ.re < 1 → ATK.ForaDaLinha.m ρ ^ 2 ≤ ATK.DInfinito.dInf` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.dInf_pos_of_zeroFora` | `∀ (ρ : ATK.ForaDaLinha.ZeroFora), 0 < ATK.DInfinito.dInf` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.rh_of_dInf_eq_zero` | `ATK.DInfinito.dInf = 0 → RiemannHypothesis` | propext, Classical.choice, Quot.sound |
| `ATK.DInfinito.rh_iff_dInf_eq_zero` | `ATK.FechamentoO1.NecessidadeRH → (RiemannHypothesis ↔ ATK.DInfinito.dInf = 0)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Cauda.conjunto_not_closed` | `¬IsClosed ATK.LinhasNovas.Cauda.conjunto` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Cauda.um_terco_no_fecho` | `1 / 3 ∈ closure ATK.LinhasNovas.Cauda.conjunto ∧ 1 / 3 ∉ ATK.LinhasNovas.Cauda.conjunto` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Truncamento.trunc_eq_self_iff` | `∀ {α : Type u_1} [Finite α] (L : Set (List α)), (∃ k, ATK.LinhasNovas.Truncamento.trunc L k = L) ↔ L.Finite` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Ordem.nat_sem_topo` | `¬BddAbove Set.univ` | propext, Quot.sound |
| `ATK.LinhasNovas.Ordem.enat_com_topo` | `BddAbove Set.univ` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Ordem.maior_abaixo_iff_predOrder` | `∀ {α : Type u_1} [inst : LinearOrder α], (∀ (a : α), ¬IsMin a → ∃ r < a, ∀ x < a, x ≤ r) ↔ Nonempty (PredOrder α)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Ordem.int_pred` | `Nonempty (PredOrder ℤ)` | propext |
| `ATK.LinhasNovas.Ordem.real_sem_pred` | `¬Nonempty (PredOrder ℝ)` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Involucao.quebrada_involutive` | `Function.Involutive ATK.LinhasNovas.Involucao.quebrada` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Involucao.quebrada_strictAnti` | `StrictAnti ATK.LinhasNovas.Involucao.quebrada` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Involucao.strictAnti_involutive_nao_afim` | `∃ f, StrictAnti f ∧ Function.Involutive f ∧ ∀ (a : ℝ), f ≠ fun x => a - x` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.Involucao.quebrada_fixo` | `∀ (x : ℝ), ATK.LinhasNovas.Involucao.quebrada x = x ↔ x = 0` | propext, Classical.choice, Quot.sound |
| `ATK.LinhasNovas.InvolucaoComFixos.Hom.mapsTo_fixos` | `∀ {α : Type u_1} {β : Type u_2} {A : ATK.LinhasNovas.InvolucaoComFixos α} {B : ATK.LinhasNovas.InvolucaoComFixos β} (f : A.Hom B), Set.MapsTo f.toFun A.fixos B.fixos` | propext |
| `ATK.LinhasNovas.InvolucaoComFixos.colapso_nao_injetivo` | `¬Function.Injective ATK.LinhasNovas.InvolucaoComFixos.colapsoHom.toFun` | propext, Classical.choice, Quot.sound |

### Ressalvas desta extensão

1. **Involução decrescente**: a proposta "toda involução estritamente decrescente de `ℝ` é
   `x ↦ a − x`" é **falsa**; o kernel certifica o contraexemplo `quebrada`
   (`strictAnti_involutive_nao_afim`). Os `centro_*` continuam valendo para as reflexões
   específicas dos enunciados, não para toda simetria.
2. **`DInfinito`**: `rh_iff_dInf_eq_zero` toma `NecessidadeRH` como **hipótese** (sem habitante).
   `dInf_pos_of_zeroFora` é incondicional: um zero fora da linha força `D_∞ > 0`. Nada prova RH.
3. **Truncamento**: `trunc_eq_self_iff` diz que o truncamento estabiliza exatamente nas
   linguagens finitas; não separa P de NP.
4. **Reta projetiva**: `RetaProj = Option ℝ` não carrega a topologia de `ℝP¹`; homeomorfismos de
   `inv`/`neg` exigiriam trocar para `OnePoint ℝ` (não feito).

### Leitura da distribuição de axiomas do congelamento (3350)

`propext` 3226, `Quot.sound` 3105, `Classical.choice` 2868; **119 sem nenhum axioma**. "Sem
axioma" só quer dizer que a prova não usa `propext`, `Classical.choice` nem `Quot.sound`. Numa
amostra inspecionada, essas 119 são lemas pequenos: `rfl`, `cases … <;> rfl`, desdobramento de
definição, passos estruturais curtos (ex.: `ATK.SATemNP.Run.mono`, `ATK.SATemNP.dec_some`,
`ATK.ATKI.Rel.flip_flip`). **A contagem não indica força**; não deve ser lida como resultado.
