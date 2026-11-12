# Auditoria de enunciados Lean

`Auditor.lean` examina cada teorema de um conjunto de módulos e classifica o **enunciado** (a prova pode ser
`sorry`, como nos benchmarks). Cada classe certificada vem de um termo de prova que passou no kernel.

| Classe | O que significa | Como se decide |
|---|---|---|
| `hipoteses_contraditorias=<tática>` | das hipóteses sai `False`: o enunciado é vazio | `contradiction`, `simp_all`, `omega`, `linarith`, `norm_num at *` fecham `∀ xs, False`; o termo vai ao kernel |
| `conclusao_vazia` | a conclusão desdobra para `True` ou `∃ _, True` | `whnf` + `isDefEq` |
| `falso=<tática>` | a negação do enunciado fechado foi provada | `norm_num`, `simp` em `¬ P`; o termo vai ao kernel |
| `axioma_extra=<nomes>` | depende de axioma fora de `propext`, `Classical.choice`, `Quot.sound` (e `sorryAx`, esperado em benchmark) | `collectAxioms` |
| `trivial=<tática>` | o enunciado inteiro fecha com uma tática padrão (informativo: comparar com o enunciado informal) | `rfl`, `norm_num`, `simp`, `omega`, `linarith`, `positivity`; o termo vai ao kernel |
| `divisao_por_zero_nao_excluida` | denominador em ℝ, ℚ ou ℂ cujo `≠ 0` não sai das hipóteses | tenta `positivity`, `norm_num`, `linarith`, `simp_all` na condição |
| `funcao_totalizada=<nome>` | `Real.sqrt` sem `0 ≤ x` ou `Real.log` sem `0 < x` deriváveis das hipóteses | idem |
| `divisao_inteira`, `subtracao_em_N` | truncamento em ℕ e ℤ | presença no enunciado elaborado |

Os quatro últimos são **riscos de codificação**, não defeitos: o enunciado pode estar certo, mas depende de uma
convenção total do Lean (`x / 0 = 0`, `√(−1) = 0`, `3 − 5 = 0` em ℕ). É a mesma separação do artigo
*Faults in Our Formal Benchmarking* (EleutherAI e Cambridge, ICML 2026), que achou divisão por zero, subtração
em ℕ e divisão inteira como os riscos mais frequentes em miniF2F, ProofNet e outros.

## Uso

```
# no projeto do benchmark, com o Auditor.lean copiado e `lean_lib Auditor` no lakefile
lake build Auditor
lake build <alvo do benchmark>
python3 auditar_benchmark.py --nome <nome> --raiz <pasta dos módulos> --lean "lake env lean" --saida resultados/
```

O auditor roda em lotes; se um lote derruba o processo, os módulos dele rodam um a um. Cada tentativa de tática
tem teto de heartbeats e é desfeita depois. O `plausible` (contraexemplo por amostragem) não entra: ele executa o
enunciado e pode derrubar o processo.

O workflow `.github/workflows/auditoria-benchmarks.yml` roda tudo sobre miniF2F (test e valid) e ProofNet, cada
um com o seu Lean e a sua Mathlib, em commits fixados.

## Limites

- **Detecção parcial.** As táticas acham só contradições e negações que elas mesmas conseguem provar. Um enunciado
  falso que precisa de uma testemunha esperta passa sem marca.
- **Riscos podem ser alarme falso.** Um risco marcado pode estar protegido por um argumento que as táticas não
  fazem (por exemplo, `log z ≠ 0` a partir de `1 < z`).
- **Fidelidade fora do alcance.** O auditor não compara com o enunciado informal. Para isso, a classe `trivial`
  aponta os candidatos a revisão humana.
