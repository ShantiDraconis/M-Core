# atk-kernel

Pasta independente do restante do repositório (lakefile e Mathlib próprios).

Verificação no kernel do Lean 4 (Mathlib `v4.34.1`) dos lemas auxiliares do programa ATK,
com auditoria automática de axiomas no GitHub Actions.

## STATUS (12/10/2026)

- Kernel: **85/85** teoremas certificados (axiomas só `propext`, `Classical.choice`, `Quot.sound`) e teste de escala
  **5/5** (`scripts/scaling_check.py`, roda no CI antes do Lean).
- **Navier–Stokes, rota interna do ATK:** a cota S ≤ θνz + C·y² (rota G5) foi provada FALSA com contraexemplo
  (`ATK/Correcao_20261012.lean`, `AUDIT_NOTE_NS_SCALING_20261012.md`): itens 19–21 FALSE, 52 FAILED_DEPENDENCY.
  Rota G5 arquivada.
- **O problema do milênio de Navier–Stokes, (A)–(D) do Clay, permanece ABERTO** (`ATK/Exact.lean`, intocado).
- Os 72 parâmetros estão todos registrados (`parametros_72_preenchidos_20261012.csv`): 34 com valor, 11 resolvidos,
  4 falsos e 23 abertos. Os 23 abertos são 8 enunciados mínimos — RH; taxa uniforme D_N·log N; Yang–Mills com gap;
  BSD (posto); BSD (fórmula refinada e Ш finito); Hodge em codimensão ≥ 2; Beal; SAT superpolinomial (P ≠ NP).
  Corpus de cálculo esgotado: o que falta nesses 8 são provas, não valores. Nenhuma conjectura do milênio foi provada.

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

## Teoremas da primeira versão (26; total atual: 85)

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

Nenhum destes lemas prova uma conjectura do milênio: `OPEN_MATH = true`.
