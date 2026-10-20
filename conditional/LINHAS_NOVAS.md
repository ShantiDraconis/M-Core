# Linhas de pesquisa novas: como o kernel reage

Arquivo: `atk-kernel/ATK/LinhasNovas.lean` (20 teoremas, axiomas padrão). As propostas do autor
foram formalizadas do jeito mais fiel possível, e o kernel decidiu o comportamento de cada uma.

| Linha | No conjunto padrão | Numa extensão | Teoremas |
|---|---|---|---|
| Número natural final sem N+1 | **CONTRADITÓRIA** em ℕ | **CONSISTENTE** em ℕ∞ (`⊤ + 1 = ⊤`), mas perde o cancelamento | `natural_final_vazio`, `sem_ultimo_natural`, `enat_final`, `enat_sem_cancelamento` |
| Maior real negativo | **CONTRADITÓRIA** em ℝ (`r/2` fica entre `r` e `0`) | **CONSISTENTE** em ℤ (é `−1`) | `sem_maior_negativo`, `int_maior_negativo` |
| Fração sem cauda finita | **JÁ EXISTE** em ℝ: `1/3`, `√2` | — | `um_terco_cauda_infinita`, `raiz_dois_cauda_infinita` |
| Ciclo pelo infinito (`+∞ = −∞`, `∞ ↔ 0`) | — | **CONSISTENTE** na reta projetiva `ℝ ∪ {∞}`: `−∞ = ∞`, `1/0 = ∞`, `1/∞ = 0`, inversão involutiva, comuta com a negação | `neg_inf`, `inv_zero`, `inv_inf`, `inv_inv`, `inv_neg` |
| ½ conecta as conjecturas | **NORMALIZÁVEL** para RH (centro ½), BSD (centro 1 → ½ com `t = s − ½`) e Hodge (`p = q` → `p/n = ½`) | não se aplica a P vs NP, Beal, NS e YM: não há involução nos enunciados | `centro_reflexao`, `centro_rh`, `centro_bsd`, `centro_bsd_normalizado`, `centro_hodge_normalizado` |
| P "aproximado" de NP | **VAZIA**: toda linguagem é limite dos seus truncamentos finitos, esteja em P ou não; a aproximação não distingue P de NP | — | `aproximacao_trivial`, `truncamento_finito` |

Fora do formalizável como está: o buraco negro estabilizando o fluido muda a equação e o espaço
(o problema do Clay é em ℝ³ plano, sem gravidade). Nenhuma linha altera OPEN_MATH.

## Extensões (`LinhasNovasII.lean`, `LinhasNovasIII.lean`, `DInfinito.lean`)

| Linha | Veredito afiado | Teoremas |
|---|---|---|
| Fração sem cauda finita | `ℤ[1/10]` é **subanel denso, enumerável e não fechado** de ℝ; não é corpo. `1/3` está no fecho e fora do conjunto | `Cauda.subanel`, `conjunto_dense`, `conjunto_countable`, `conjunto_not_closed`, `um_terco_no_fecho`, `nao_corpo`, `caudaFinita_iff` |
| Natural final / maior negativo | "maior abaixo de cada ponto" ⟺ `PredOrder`: ℤ tem, ℝ não; ℚ também não tem maior negativo; com cancelamento, `x + a = x` força `a = 0` | `maior_abaixo_iff_predOrder`, `int_pred`, `real_sem_pred`, `rat_sem_maior_negativo`, `no_fixpoint_of_cancelative`, `nat_sem_topo`, `enat_com_topo` |
| Ciclo pelo infinito | fixos de `inv` = `{1, −1}`, de `neg` = `{0, ∞}`; `neg ∘ inv` é involução; o colapso `∞ = 0` é **morfismo não injetivo** para a inversão de ℝ (fixos `{−1, 0, 1}`) | `inv_fixed`, `neg_fixed`, `neg_inv_involutive`, `colapso_fiber`, `colapso_inv`, `colapsoHom`, `colapso_nao_injetivo` |
| ½ | o fixo de `x ↦ a − x` é `a/2` em todo corpo de característica 0 e `(1/2)•a` em todo ℚ-módulo; **refutado**: nem toda involução decrescente de ℝ é reflexão | `half_fixed_point`, `centro_afim`, `ofAffineCenter`, `strictAnti_involutive_nao_afim` |
| P aproximado de NP | os truncamentos determinam a linguagem (`trunc_injective`) e estabilizam **exatamente** nas finitas (`trunc_eq_self_iff`); cada truncamento é tabela finita | `trunc_injective`, `trunc_eq_self_iff`, `trunc_tabela` |
| `D_∞` (Báez-Duarte) | `D_∞ = ⨅ D_N ∈ [0, 1]`; `D_N → 0 ⟺ D_∞ = 0`; um zero fora da linha força `D_∞ ≥ m(ρ)² > 0`; `RH ⟺ D_∞ = 0` **sob** `NecessidadeRH` | `dInf_eq_zero_iff`, `piso_no_limite`, `dInf_pos_of_zeroFora`, `rh_iff_dInf_eq_zero` |
