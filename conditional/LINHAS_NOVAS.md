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
