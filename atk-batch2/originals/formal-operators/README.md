# ATK — Pipeline de fechamento verificável (fail-closed)

Este pacote fornece estrutura de código, prova auxiliar, gates de fechamento, manifesto, build Lake, CI, auditoria de fontes e certificado externo gerado pelo script. **Não fornece habitantes das sete conjecturas abertas.**

## Executar

Instalar Lean 4.21.0 via elan, depois:

```sh
lake build
python3 tools/audit.py
```

O script retorna erro se o kernel não estiver disponível, se o build falhar ou se detectar `sorry`, `admit`, `axiom` ou `unsafe` no código auditado. Escreve `certificates/EXTERNAL_AUDIT.json` mesmo se o build falhar.

## Regras de certificação

1. Importar e fixar SHA das definições concretas originais de cada repo.
2. Demonstrar o habitante da obrigação universal, não um exemplo isolado.
3. Demonstrar a ponte até o enunciado oficial, sem circularidade.
4. Compilar e inspecionar dependências e `#print axioms` de cada teorema final.
5. Alterar `terminal_manifest.json` para VERIFIED **somente** depois da evidência correspondente. O manifesto sozinho não constitui auditoria independente; o script é uma primeira barreira, não um verificador de verdade semântica.
6. Gerar certificado vinculado aos SHA dos arquivos compilados e ao run CI.

`TerminalGate` e `SevenGates` são combinadores lógicos. Não são certificados de problemas do milênio.
