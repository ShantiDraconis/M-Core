# Roteiro até o limite: o que falta, em ordem

Status certificado (`atk-kernel/ATK/StatusFinal.lean`, calculado pelo kernel):
**`OPEN_MATH = true`, `CLOSED_MATH = false`** (`open_math_true`, `closed_math_false`). O registro
não pode mentir: evidência positiva exige prova, negativa exige refutação, e o estado `B` é
impossível (`nenhum_item_em_B`). Se `CLOSED_MATH` der `true`, todas as proposições valem
(`closedMath_correto`).

## Inventário certificado

| Camada | Itens | Estado |
|---|---|---|
| Pontes/resultados provados | B1 Báez-Duarte (suficiência), B4 Cook–Levin, SAT ∈ NP, FLT 3 ≤ n ≤ 22, N(T) bem definido, Littlewood ε > 1/2 | **T** (com o termo de prova) |
| Lacunas da Mathlib | Riemann–von Mangoldt, Hadamard para ξ, Littlewood sob RH, Modularidade, Mordell–Weil | N |
| Pontes publicadas não formalizadas | B2 FLT completo, B3 Leray, B5 Lefschetz, B6 GZK, B7 Osterwalder–Schrader | N |
| Obrigações (os problemas) | O1 … O8 | N (O1, O2, O4 ⟺ a conjectura real, `obrigacoes_sao_conjecturas`) |

## O que precisa, por nível

### Nível A: formalização de matemática publicada (avança o kernel, não fecha nada)

| # | Peça | Destrava | Tamanho |
|---|---|---|---|
| A1 | Riemann–von Mangoldt (com `N(T)` já definido em `FechamentoO1`) | parte de `NecessidadeRH` | grande (argumento de ξ, Stirling) |
| A2 | Hadamard para funções inteiras de ordem 1, aplicado a ξ | `HadamardXi`, `J(ε) → 0` | grande (teoria de produtos canônicos) |
| A3 | Littlewood sob RH (cotas de 1/ζ) | `EntradaLittlewood` para ε ≤ 1/2 | grande |
| A4 | Dedução clássica A1+A2+A3 ⇒ `EntradasNecessidade` | **iff de RH** (`rh_iff_DN`) | média |
| A5 | Critério de Leray (B3) sobre `modeloNS` | NS: só falta O3 | grande (teoria local de NS) |
| A6 | Mordell–Weil, Modularidade, GZK | BSD: só faltam O6, O7 | muito grande (projetos FLT/BSD em andamento) |
| A7 | Analitificação, decomposição de Hodge, classe de ciclo | Hodge real sem parâmetro | muito grande (Kähler, cohomologia) |
| A8 | Lefschetz (1,1) (B5) | Hodge: casos conhecidos | grande, depende de A7 |
| A9 | Reconstrução de Osterwalder–Schrader em ℝ⁴ (B7) | YM: só falta O8 | grande |
| A10 | FLT completo (B2) | Beal: só falta O2 | projeto Imperial (em andamento) |

### Nível B: escolhas de definição (não são matemática nova, mas mudam o enunciado)

* **YM**: fixar um critério formal de "corresponde a Yang–Mills" (limite de rede com ação de Wilson,
  OPE com liberdade assintótica, …). Hoje é parâmetro (`Corr`).

### Nível C: os produtores O1–O8 (os próprios problemas)

São abertos. O kernel prova que, para O1, O2 e O4, não existe produtor mais fraco que a conjectura
(`rotaO1_iff_rh`, `obrigacoes_sao_conjecturas`). Nenhum trabalho dos níveis A e B fecha o nível C.

## Até onde dá para ir com certificação

* Com **A1–A4**: RH ⟺ `D_N → 0` certificado. O1 continua N.
* Com **A5–A10**: cada problema fica reduzido **só** à sua obrigação O, no enunciado real e sem
  parâmetro (menos YM, que depende de B).
* O limite certificável é **`CLOSED_MATH = false` com todas as pontes em T e todas as obrigações em
  N**. Passar disso é resolver os problemas.
