# O1 (Riemann): estrutura completa do fechamento

Arquivo: `atk-kernel/ATK/FechamentoO1.lean`, com 13 teoremas, todos com os axiomas padrão.
O1 continua `N = ⟨false, false⟩`.

## 1. Provado agora (incondicional)

| Teorema | Conteúdo |
|---|---|
| `zeros_finitos_compacto` | zeros de ζ num compacto sem o ponto 1 são finitos (ζ analítica e não nula em ℂ∖{1}, conexo ⇒ zeros isolados) |
| `abs_im_ge` | todo zero não trivial tem `|Im ρ| ≥ 1/2` |
| `zerosAte_finito`, `zerosSim_finito` | zeros com `0 < Im ρ ≤ T` e com `|Im ρ| ≤ T` são finitos |
| `N` (definição) | contagem de zeros com multiplicidade (`analyticOrderNatAt`), **bem definida** |
| `N_mono`, `N_baixo` | `N` é monótona e vale 0 para `T < 1/2` |
| `xi`, `xi_zero` | `ξ(s) = s(s−1)/2 · Λ₀(s) + 1/2` (inteira), `ξ(0) = 1/2` |

## 2. O que falta na Mathlib: enunciados com tipo exato, sem prova

| Nome | Enunciado | Literatura |
|---|---|---|
| `RiemannVonMangoldt` | `N(T) = (T/2π) log(T/2π) − T/2π + O(log T)` | von Mangoldt 1905 |
| `HadamardXi` | `ξ(s) = e^{A+Bs} ∏ (1 − s/ρ) e^{s/ρ}` (produtos simétricos, com multiplicidade) | Hadamard 1893 |
| `LittlewoodSobRH` | sob RH, `1/ζ(σ+it) = O(|t|^ε)` em `σ ≥ 1/2 + δ` | Littlewood 1912 |

## 3. Estrutura do fechamento

```
NecessidadeRH = RiemannVonMangoldt ∧ HadamardXi ∧ LittlewoodSobRH ∧ (dedução → EntradasNecessidade)
        │
        ├─► rh_iff_DN        : RH ⟺ D_N → 0      (a volta é B1, já provada)
        └─► entradas_iff_rh  : EntradasNecessidade ⟺ RH

RotaO1  (produtores que fechariam O1)
  ├─ semZeroFora : IsEmpty ZeroFora            ─┐
  ├─ baezDuarte  : D_N → 0   (via B1 provada)  ─┼─► fecha_O1 : RiemannHypothesis
  └─ entradas    : EntradasNecessidade          ─┘
rotaO1_iff_rh : RotaO1 ⟺ RH   (toda rota tem a força exata de RH)
```

**Leitura**:
- Preencher `NecessidadeRH` (formalizar os três teoremas e a dedução) fecha a **necessidade** (o iff de RH), que é a parte (a). Não fecha RH.
- Fechar O1 exige um **produtor**: `IsEmpty ZeroFora`, `D_N → 0` ou as entradas sem hipótese. O kernel prova que cada um desses produtores é equivalente a RH (`rotaO1_iff_rh`), então não existe produtor mais fraco. Os produtores dos outros seis estão em `ATK/Termos.lean` e `ATK/ClosedMathReal.lean` (`Lacunas`).

## 4. Zeros fora da linha (`atk-kernel/ATK/ZerosFora.lean`, 18 teoremas)

* **Órbitas**: as simetrias `s ↦ 1 − s` e `s ↦ s̄` formam o grupo de Klein. A órbita tem
  **1, 2 ou 4** pontos (`orbita_card`), **nunca 3 nem 5** (`orbita_nao_tres_nem_cinco`). Um zero
  fora da linha tem órbita de exatamente 4 (`card_fora`); um zero na linha, de 2 (`card_na_linha`).
* **Contagem**: só finitos zeros fora da linha abaixo de cada altura (`foraAte_finito`).
  Infinitos zeros fora da linha ⟺ há zero fora da linha acima de **qualquer** altura
  (`infinitos_iff`). Não há "zero no infinito" em `ℂ`; na leitura hiper-real, um zero de altura
  infinita corresponde exatamente a infinitos zeros comuns fora da linha.
* **Esconderijo no truncamento**: um zero `ρ` fora da linha garante `D_N ≥ m(ρ)²` (`piso_DN`), mas
  `m(ρ)² ≤ (2 Re ρ − 1)/‖ρ‖²` e `m(ρ)² ≤ 1/(4‖ρ‖²)` (`piso_esconde`). O piso garantido tende a 0
  com a altura (`piso_some`). Um zero na altura `10¹²` garante no máximo `≈ 2,5·10⁻²⁵`: é
  invisível a truncamentos calculáveis, mas é positivo.
