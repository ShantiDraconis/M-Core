# ATK — Operadores e semântica material

## Conteúdo demonstrado no código-fonte
- Lógica: habitante explícito, composição de implicações e troca de conjunção.
- Aritmética: não negatividade dos naturais, sucessor estrito, impossibilidade de descida estrita global em zero.
- Álgebra: identidade, comutatividade e associatividade da adição inteira.
- Geometria: pontos de coordenadas inteiras em duas dimensões e composição de translações.
- Semântica: avaliador recursivo de expressões booleanas e equações de avaliação.
- Aplicação terminal: somente de uma premissa já demonstrada e uma ponte independente.

## Fronteira matemática
Esses resultados são incondicionais em seu domínio elementar, mas NÃO estabelecem as sete conjecturas.
`OPEN_MATH=false` pode ser atribuído a uma obrigação auxiliar somente após verificação do kernel e auditoria de dependências. O estado global permanece OPEN.

## Compilar
`lake build ATK` e depois `lake env lean ATK/FormalOperators.lean`.
Inspecionar axiomas com `#print axioms ATK.Formal.terminal_application` e para cada teorema exportado.
