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
