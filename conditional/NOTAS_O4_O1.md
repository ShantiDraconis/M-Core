# Notas de auditoria F.1 para O4 e O1

Correções do autor, registradas aqui para que sobrevivam ao encontro com o trabalho de outra
sessão (PR #58, `AUDITORIA_F1.md`). Nível: **por fonte** (leitura das definições), não conferido
nesta sessão por compilação.

## O4 (P vs NP)

* `SATNotInP` é **fiel**: `ATK.ModeloPNP.SAT` é o SAT de Cook, não a moldura de Shannon.
* Os resultados de contagem no kernel (Shannon, `n ≤ 2s + 1`) são **contexto**: contam sobre todas
  as funções booleanas e não exibem família em NP.
* Fidelidade do enunciado e força do produtor são **eixos diferentes**: `SATNotInP` = fiel;
  produtores de O4 = contexto; "zero produtores" continua verdadeiro.

## O1 (Riemann)

* `PisoLog` e `UniformLogBound` usam o **mesmo** `DN` e a **mesma** normalização `c / log(N + 2)`.
* Logo `sem_contracao_de_piso_log` refuta exatamente o que diz refutar.
* `route-refuted` para O1 sobe de "plausível" para **"sólido"**: a rota de contração está fechada.
