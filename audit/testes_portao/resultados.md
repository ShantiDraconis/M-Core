# Teste do portão (Lean (version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release))

| Caso | Defeito | G: grep do ci.yml | T: busca sem comentários | L: aviso de sorry no log | M: portão do M-Core | V: vazios do MVEI | K: referência (kernel) |
|---|---|---|---|---|---|---|---|
| C01 limpo | — | ok | ok | ok | ok | ok | ok |
| C02 sorry tático | sorry | pegou | pegou | pegou | pegou | **deixou passar** | pegou |
| C03 sorryAx escrito direto | sorry | **deixou passar** | **deixou passar** | pegou | pegou | **deixou passar** | pegou |
| C04 axioma com atributo na linha | axioma | **deixou passar** | **deixou passar** | **deixou passar** | pegou | **deixou passar** | pegou |
| C05 axioma privado | axioma | **deixou passar** | **deixou passar** | **deixou passar** | pegou | **deixou passar** | pegou |
| C06 native_decide | confia no compilador | **deixou passar** | **deixou passar** | **deixou passar** | pegou | **deixou passar** | pegou |
| C07 limpo; 'sorry' em comentário e docstring | — | **alarme falso** | ok | ok | ok | ok | ok |
| C08 limpo; 'sorry' dentro de uma string | — | **alarme falso** | ok | ok | **alarme falso** | ok | ok |
| C09 enunciado `True` | vazio | **deixou passar** | **deixou passar** | **deixou passar** | **deixou passar** | pegou | pegou |
| C10 vazio escondido numa definição | vazio | **deixou passar** | **deixou passar** | **deixou passar** | **deixou passar** | **deixou passar** | pegou |
| C11 hipótese contraditória | vazio | **deixou passar** | **deixou passar** | **deixou passar** | **deixou passar** | **deixou passar** | pegou |
| C12 limpo; condicional honesto | — | ok | ok | ok | ok | ok | ok |
| **Total** | | 1/8 pegos, 2 falsos | 1/8 pegos, 0 falsos | 2/8 pegos, 0 falsos | 5/8 pegos, 1 falsos | 1/8 pegos, 0 falsos | 8/8 pegos, 0 falsos |
