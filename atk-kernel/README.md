# atk-kernel

Pasta independente do restante do repositório (lakefile e Mathlib próprios).

Verificação no kernel do Lean 4 (Mathlib `v4.34.1`) dos lemas auxiliares do programa ATK,
com auditoria automática de axiomas no GitHub Actions.

## O que roda a cada push

**Job `kernel`**
1. Instala o Lean e baixa a Mathlib já compilada.
2. Roda `lake build`.
3. Compila cada arquivo `ATK/*.lean` separadamente e executa os `#print axioms` do final de cada um.
4. `scripts/check_axioms.py` marca cada teorema como **CERTIFIED** só se:
   * o arquivo compilou sem erro, e
   * os axiomas usados estão entre `propext`, `Classical.choice` e `Quot.sound`, e
   * a fonte não contém `sorry`, `admit` ou `axiom`.

   Um teorema com erro entra no ambiente com `sorryAx` e é reprovado automaticamente.
5. A tabela aparece no resumo da execução, e os logs ficam no artefato `atk-kernel-report`.

**Job `numerics`**
Reproduz o resíduo real D_N de Nyman–Beurling/Báez-Duarte para N ≤ 300, em 40 e 60 dígitos.
O arquivo `numerics/dn_N1500_prec45.csv` traz a tabela até N = 1500.

## Teoremas (47 = 19 lemas auxiliares + 14 condicionais + 14 de regimes)

| Arquivo | Conteúdo | Observação |
|---|---|---|
| `NavierStokes` | absorção; δ > 0; comparação de Riccati; cota y(t) ≤ y₀/(1−2Cy₀t) | estimativa local, não regularidade global |
| `Riemann` | majorante ⇒ D_N → 0; passo de Schur; identidade e cota da Gram | o majorante uniforme implica RH e continua aberto |
| `YangMills` | Cauchy–Schwarz ponderado; inclinação da massa efetiva ≤ 0 | não constrói a teoria 4D nem o gap |
| `BSD` | det 2×2; regulador > 0; recuperação de #Ш **assumindo** a fórmula | não prova BSD |
| `Hodge` | realização linear única com matriz invertível | pressupõe que os ciclos existem |
| `Beal` | gcd(x,y,z) ≤ 2 **dado** Fermat (hipótese `hFLT`) | Fermat ainda não está todo formalizado na Mathlib |
| `PvsNP` | P⊆P/poly ∧ NP⊄P/poly ⇒ P≠NP; SAT∈NP ∧ SAT∉P ⇒ P≠NP | só a forma lógica, sem máquinas de Turing |
| `Geometry` | ∫R dV = 12π²a na S³ redonda | identidade algébrica |

### Condicionais (`ATK/Conditional/`)

Molde: PONTE (literatura, não formalizada) → HIPÓTESE ABERTA → ENUNCIADO. Ambas entram como
argumentos explícitos; detalhes em `scripts/conditionals.json`.

| Arquivo | Teorema principal | Enunciado |
|---|---|---|
| `Conditional/Riemann` | `riemann_conditional` (+ `DN_nonneg`, `DN_tendsto_zero`) | `RiemannHypothesis` da Mathlib |
| `Conditional/Beal` | `beal_conditional` (+ `beal_iff_gcdLowerBound`, `exponent_gcd_le_two`, `one_lt_gcd_iff`) | enunciado elementar completo |
| `Conditional/NavierStokes` | `ns_conditional` | relativo a `NSModel` |
| `Conditional/PvsNP` | `pvsnp_conditional` (+ `pneNP_iff_sat_not_in_P`) | relativo a `ComplexityModel` |
| `Conditional/Hodge` | `hodge_conditional` | relativo a `HodgeModel` |
| `Conditional/BSD` | `bsd_conditional` (+ `bsd_rank_conditional`) | relativo a `BSDModel` |
| `Conditional/YangMills` | `ym_conditional` | relativo a `YMModel` |

### Regimes do gateway (`ATK/Regimes.lean`)

Núcleo incondicional `W_strictMono` (W = W₀ + 10⁻⁶·t, independente de Seff — `W_ignores_Seff`),
classificação dos regimes vácuo/suave/crítico/explosão, histerese sem flapping, custo de
tunelamento, gatilhos H1 (RH) e H3 (BSD, forma correta) e ruído. Camada de simulação: não
toca `OPEN_MATH`.

Nenhum destes teoremas prova uma conjectura do milênio: `OPEN_MATH = true`.
