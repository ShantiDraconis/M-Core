# AUDIT NOTE — NS-SCALING-FALSE (12/10/2026)

**Escopo:** rota interna do ATK para Navier–Stokes (cotas absolutas subcríticas). **ATK interno ≠ problema do
milênio:** os enunciados (A)–(D) do Clay em `ATK/Exact.lean` não foram tocados e seguem OPEN_MATH.

## Veredito

| Item | Enunciado | Status | Onde |
|---|---|---|---|
| 19 | ∃ C, ∀ u, S ≤ θνz + C·y² | **FALSE** | `ATK.Correcao_20261012.ns_19_false` |
| 20, 21 | c_B* + c_T* finitos com S = B + T | **FALSE** (soma = +∞) | `ns_20_21_false`, `ns_20_21_no_split` |
| 52 | orçamento bulk + tail (+ resto quadrático) | **FAILED_DEPENDENCY** (19–21) | `ns_52_failed` |

## Prova

Leis de escala (ℝ³), **medidas** no campo semente com expoentes exatos até 10⁻⁶
(`m-core-openai-ns-audit/atk-kernel/ns_data/scaling_counterexample.py`, 128³):

| Operação | y | z | S |
|---|---|---|---|
| amplitude u ↦ a·u | a² | a² | a³ |
| dilatação u ↦ λ·u(λ·) | λ | λ³ | λ³ |

- **Lema A (amplitude):** S/(νz) = a·S₀/(νz₀) → ∞. Logo nenhuma divisão S = B + T tem c_B* + c_T* finito.
- **Lema B (dilatação):** depois de escolher a com S₁ − θνz₁ > 0, (S − θνz)/y² = λ·(S₁ − θνz₁)/y₁² → ∞.
  Logo nenhum C serve.
- **Rigidez (`only_cubic_survives`):** uma cota S ≤ θνz + C·yᵖ para todos os estados obriga p = 3 — o expoente
  da cota clássica S ≤ (ν/2)z + C ν⁻³ y³, que só dá existência por tempo curto.

Campo semente (v = rot ψ, ψ gaussiana × polinômio, σ = 0.5): y = 43.4111, z = 1258.88, S = 0.111925,
estável em 64³, 96³ e 128³.

## Correções à proposta de fix recebida

1. Na dilatação, y_λ = λ·y₀ (logo y_λ² = λ²·y₀², não λ·y₀²) e a razão (S − θνz)/y² cresce **∝ λ**, não ∝ λ².
2. A amplitude sozinha **não** faz (S − θνz)/y² divergir: com S ~ a³ e y² ~ a⁴ a razão vai a 0. O máximo é em
   a* = 2θνz₀/S₀ = 20245.5, com razão 1.467·10⁻⁹. Os valores "≈ 1.18 em a = 20000" e "≈ 59.4 em a = 10⁶" estão
   errados: os corretos são 1.467·10⁻⁹ e 5.88·10⁻¹¹. A divergência vem da dilatação (λ > C/1.467·10⁻⁹).
3. A cota intermediária |S| ≤ c·y^(3/2)·z^(1/2) é falsa (vetor de escala (4, 3) ≠ (3, 3)). A desigualdade
   correta (Gagliardo–Nirenberg) é |S| ≤ c·y^(3/4)·z^(3/4) ≤ (ν/2)z + C ν⁻³ y³.

## Como não cair de novo

`scripts/scaling_check.py` roda no CI antes do Lean, sobre `scripts/proposed_bounds.json`: toda cota
S ≤ Σ cᵢ y^αᵢ z^βᵢ só é admissível se (3, 3) estiver no fecho convexo dos vetores (2αᵢ + 2βᵢ, αᵢ + 3βᵢ).
Condição necessária: quem falha é falso; quem passa ainda precisa de prova. Hoje: itens 19 e 20/21 e a
proposta y^(3/2)z^(1/2) REJEITADOS; cota clássica y³ e Gagliardo–Nirenberg ADMISSÍVEIS.

## Estado após o fix

Abertos de verdade (8 enunciados): RH; taxa uniforme D_N log N; Yang–Mills com gap; BSD (posto); BSD (fórmula);
Hodge; Beal; P ≠ NP. Navier–Stokes: o problema do Clay segue aberto; a rota por cotas absolutas foi encerrada.
