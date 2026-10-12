# ATK — Matemática concreta e fronteira terminal

Este pacote contém candidatos a formalizações de resultados auxiliares não circulares. Não contém demonstrações universais das sete conjecturas. Os arquivos Lean NÃO foram compilados neste ambiente e podem requerer correções de elaboração. Nenhum certificado terminal é emitido.

## Regra de prova

Para cada conjectura, vincular definições originais a um tipo matemático concreto, provar invariantes sem pressupor a conclusão, e demonstrar uma ponte independente para o enunciado original. `sorry`, `admit`, declarações novas de `axiom` e `unsafe` são proibidos. A auditoria também deve detectar uso circular de hipóteses, axiomas importados e enunciados alterados.

## Resultados auxiliares propostos

- Aritmética: impossibilidade de descida estrita global de medida natural em domínio habitado; divisor primo comum de duas bases divide a terceira base de uma igualdade de potências.
- Semântica: interpretador booleano definido recursivamente, lei de conjunção, dupla negação e relação entre verificação de conjunção e verificações componentes.
- Análise: antitonicidade de ínfimos de custo sob inclusão de conjuntos de aproximação.

## Verificações pendentes

1. Instalar Lean 4 + Mathlib compatíveis; `lake exe cache get && lake build`.
2. Corrigir erros de elaboração sem introduzir hipóteses circulares.
3. Substituir o tipo genérico dos exemplos pelas estruturas matemáticas concretas dos repositórios.
4. Demonstrar os sete teoremas terminais (ainda abertos).
5. Executar `#print axioms` e auditar dependências transitivas.
6. Registrar commit, SHA-256, run ID e logs de compilação reais.

Estado: SOURCE_LOCAL | KERNEL_NOT_RUN | TERMINAL_CERTIFIED=0/7 | OPEN_MATH=true | CLOSED_MATH=false.
