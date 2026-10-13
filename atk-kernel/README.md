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
6. `closure/closure_gate.py` decide **OPEN_MATH** no nível meta (ver `closure/README.md`): um problema
   só fecha com uma declaração de tipo exatamente igual ao enunciado oficial ou à sua negação,
   aceita pelo kernel com axiomas padrão. Controles provam que o portão recusa `axiom`, `sorry`,
   tipo errado, a resolução clássica vazia e a disjunção de Navier–Stokes.

**Job `numerics`**
Reproduz o resíduo real D_N de Nyman–Beurling/Báez-Duarte para N ≤ 300, em 40 e 60 dígitos.
O arquivo `numerics/dn_N1500_prec45.csv` traz a tabela até N = 1500.

## Teoremas (110 certificados; tabela abaixo = núcleo original)

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

| `Exact` | enunciados oficiais: RH (Mathlib), NS (A)–(D) de Fefferman, Beal, P/NP com `TM2` | sanidade das definições |
| `Horizon` | não há primo final; Ostrowski; fórmula do produto; fator Γ_ℝ de ζ | o "primo no infinito" é o lugar arquimediano |
| `Closure` | fechamento = decisão; (A) ∨ (C) de NS é teorema (reescala); falsificadores de RH/NS/Beal/P≠NP; contraexemplo de RH só em 0 < Re s < 1; leis AGOT de extração/transporte e seus contraexemplos | nenhuma conjectura decidida |

Nenhum destes lemas prova uma conjectura do milênio: `OPEN_MATH = true` (portão: 0/7 fechados; BSD, YM e Hodge nem são enunciáveis na Mathlib v4.34.1).
