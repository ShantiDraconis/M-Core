# Brief — rodar os testes baratos do programa de pesquisa

Você vai IMPLEMENTAR e RODAR testes numéricos/computacionais especificados nos mapas de fronteira em
`/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/<TOPIC>_frontier.md`
(seção de testes). Leia o arquivo do seu tópico primeiro; os testes que você deve rodar estão listados na sua tarefa.

## Ambiente (importante)
- Máquina Linux com 2 núcleos, compartilhada com uma compilação do Lean que roda em segundo plano. **Rode tudo com
  `nice -n 10`** e mantenha cada teste ≤ 15 minutos de relógio (use `timeout 900`). Se um teste não couber, reduza os
  parâmetros (N menor, menos casos) e diga exatamente o que reduziu.
- **Não há acesso ao PyPI.** Não há numpy/scipy/pari. Disponíveis: Python 3.13 com a biblioteca padrão, e bibliotecas
  puras em Python via
  `export PYTHONPATH=/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/pylibs/mpmath:/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/pylibs/sympy:/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/pylibs/networkx`
  (mpmath, sympy, networkx). Solver SAT: `/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/pylibs/cadical/build/cadical` (formato DIMACS). gcc/g++/make existem: para laços pesados, escreva C e compile com `-O2`.
- Não use o Lean nem rode `lake` (a CPU está ocupada pela compilação). Não clone repositórios grandes. Não modifique nada
  em `audit/repos/` nem em `/home/claude/*`.
- Código em `/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/code/<TOPIC>_<teste>.*`.

## Rigor
- Antes de rodar, valide o código num caso de controle cujo resultado é conhecido (o mapa costuma indicar um: OEIS,
  tabela publicada, valor teórico). Se o controle falhar, conserte antes de seguir.
- Separe o que o teste **mostra** do que ele **sugere**. Números finitos não provam enunciados assintóticos.
- Se o resultado contradiz a literatura, a primeira hipótese é erro seu: confira de novo antes de reportar.

## Saída
Para cada teste, `/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/<TOPIC>_<teste>.md`
(em português, ≤ 60 linhas): hipótese testada, método (com o controle e se passou), parâmetros efetivos, resultados (tabela),
interpretação honesta, limites, e o que testar a seguir. Depois responda em ≤ 20 linhas: um resultado por teste, em uma
ou duas frases, deixando claro o que foi controle e o que é novo.
