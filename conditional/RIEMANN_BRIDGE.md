# Ponte B1 provada no kernel: `D_N → 0 ⇒ Hipótese de Riemann`

Arquivos: `atk-kernel/ATK/ZetaStrip.lean` (14 teoremas), `atk-kernel/ATK/MellinRho.lean` (10),
`atk-kernel/ATK/BaezDuarteBridge.lean` (22), `atk-kernel/ATK/ObligationsClosed.lean` (1).
Todos dependem só de `propext`, `Classical.choice`, `Quot.sound`; nenhum `sorry`, `admit` ou `axiom`.

## O que foi provado

```lean
theorem ATK.BaezDuarteBridge.baezDuarteCriterion : ATK.Conditional.Riemann.BaezDuarteCriterion
-- BaezDuarteCriterion := Tendsto DN atTop (𝓝 0) → RiemannHypothesis
```

`RiemannHypothesis` é o enunciado **da Mathlib** (todo zero não trivial de `riemannZeta`, `s ≠ 1`,
tem `Re s = 1/2`). `DN N = inf_c ∫_{(0,∞)} (χ − Σ_{k≤N} c_k {1/(k t)})² dt` é a família concreta de
Báez-Duarte. Até este commit, essa implicação era a hipótese **B1** ("publicada, não formalizada")
do condicional de Riemann. Agora é um teorema, e o auditor a marca `CLOSED` por cálculo
(`proof_theorem` certificado com enunciado literal igual à obrigação).

## Como a prova funciona

1. **ζ na faixa crítica** (`ZetaStrip`). `H(s) = ∫_1^∞ {t} t^{-s-1} dt` é a transformada de Mellin
   de `{t}·𝟙_{t>1}`, holomorfa em `Re s > 0`. Para `Re s > 1`, a somação de Abel da Mathlib
   (`LSeries_eq_mul_integral'`) e `{t} = t − ⌊t⌋` dão `H(s) = 1/(s−1) − ζ(s)/s`. Pelo princípio da
   identidade no semiplano (contra `(1 − ζ₀(s))/s`, com `ζ = 1/(s−1) + ζ₀` inteira), a fórmula vale
   em todo `Re s > 0`, `s ≠ 1`.
2. **Mellin dos geradores** (`MellinRho`). `∫_0^∞ {u} u^{-s-1} du = 1/(1−s) + H(s) = −ζ(s)/s` em
   `0 < Re s < 1`; por mudança de variável, `∫_0^∞ {1/(k t)} t^{s−1} dt = −k^{−s} ζ(s)/s`.
3. **Contradição** (`BaezDuarteBridge`). Se `ζ(s) = 0` com `1/2 < σ < 1`, todo resíduo
   `f = χ − Σ c_k ρ_{k+1}` tem `∫_0^∞ f(t) t^{s−1} dt = 1/s`. Mas
   `|∫ f t^{s−1}| ≤ (λ‖f‖² + 1/(λ(2σ−1)))/2 + ‖f‖/(1−σ)` (em `(0,1]` por `2ab ≤ λa² + b²/λ`; em
   `(1,∞)` o resíduo é `−S/t` e `S² ≤ ‖f‖²`). Com `D_N → 0` o lado direito fica menor que `1/|s|`.
4. **Faixa → RH**: `ζ ≠ 0` em `Re s ≥ 1` (Mathlib) e a equação funcional
   `ζ(1−s) = 2(2π)^{−s} Γ(s) cos(πs/2) ζ(s)` (Mathlib) cobrem `Re s < 1/2`, separando os zeros
   triviais.

## O que isso muda — e o que não muda

- A rota de Riemann agora depende **só** da obrigação **O1**: `D_N → 0`, equivalentemente
  `inf_N D_N = 0` (`riemann_of_iInf_zero`), equivalentemente "`D_N` não está no estado `finito`"
  (`riemann_of_not_finito`, com `RiemannStates`).
- `riemann_of_uniformLogBound : UniformLogBound → RiemannHypothesis` não tem mais ponte.
- O1 continua **aberta**: é equivalente à própria Hipótese de Riemann (a direção recíproca, mais
  difícil, de Báez-Duarte não foi formalizada e não é necessária para esta implicação).
- `CLOSED_MATH` continua `false`: o portão exige as sete provas incondicionais.
