# Publicação incremental do espelho `atk-math-core-public`

A junção MVEI (`tools/publicar_espelhos.py`, fora deste repositório) regrava `mvei/SOURCE.json`,
`mvei/SOURCES.sha256` e `mvei/README.md` do espelho a partir do commit verificado `390e378` e apaga os registros
dos arquivos do `atk-kernel/` adicionados depois dele (os arquivos `.lean` continuam no espelho). Aconteceu em
05/11, 09/11 e 11/11.

**Depois de cada junção MVEI**, rode:

    python3 scripts/espelho/publicar_incremental.py <clone do M-Core> <commit> <clone do espelho> scripts/espelho/ci_espelho.json
    cd <clone do espelho> && sha256sum -c mvei/SOURCES.sha256

O script copia só `atk-kernel/` (as ferramentas de `audit/` e os casos plantados ficam privados), refaz
`SOURCES.sha256`, acrescenta ao `AFTER_VERIFIED_COMMIT.csv` os teoremas dos arquivos novos (com os axiomas de
`atk-kernel/audits/axioms.txt`; sai com erro se algum não for padrão ou estiver `VER CI` sem valor do CI) e
restaura a seção "Added after the verified commit".

`ci_espelho.json`: runs do CI do kernel (mais novo primeiro), texto da conferência local, linhas da tabela
(`n = 0` é preenchido pela contagem) e `so_ci` (prefixos conferidos só pelo CI). A cada rodada nova, acrescente o
run e a linha da tabela.
