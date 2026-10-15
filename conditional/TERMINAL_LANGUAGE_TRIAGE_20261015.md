# ATK — Triagem de linguagem terminal (15-10-2026)

**Escopo:** somente os 21 registros de `FORMAL_LANGUAGE_REVIEW_SEED.csv`. Não é varredura de todas as refs. Nenhum kernel foi executado nesta triagem.

## Contagem sem duplicação

- 21 registros de declarações.
- 20 unidades `(repositório, branch, caminho)`: duas declarações compartilham o mesmo arquivo Yang–Mills.
- 19 unidades `(repositório, caminho)`: o arquivo de Riemann aparece em duas branches.
- 8 repositórios distintos.
- **9 unidades de alto risco** `(repo, branch, path)`: Riemann (2), Horizon Prime (All, BSD, Hodge, PvsNP, RH, YM: 6), Universal Emergent Logic UETheta (1) = **9**. Todas exigem verificar fidelidade/axiomas antes de qualquer selo terminal.
- Mais 1 unidade Universal Emergent Logic MasterTheorem requer auditoria de hipóteses transitivas.
- Os demais registros são **REVIEW**, não erros confirmados: alguns são contraexemplos ou firewalls deliberados.

## Classificação preliminar por tipo

| Categoria | Unidades repo/branch/path | Motivo |
|---|---:|---|
| AXIOM_DEPENDENT_OR_LOCAL_TARGET | 8 | Riemann (2) e Horizon Prime (6): dependências axiomáticas ou alvos locais |
| VACUOUS_TARGET | 1 | Universal Emergent Logic UETheta: `RiemannHypothesis := True` |
| ASSUMPTION_DEPENDENT | 1 | Universal Emergent Logic MasterTheorem: classe e axiomas importados |
| SCOPE_REVIEW | 10 | M-Core (3), PvsNP (4), Hodge (1), Yang–Mills (1), snapshot PvsNP (1) |

Total: 20 unidades. **Os 10 primeiros são prioridades para mudança da apresentação de certificação, não prova de que o arquivo fonte esteja incorreto.** Em particular, provas de modelos degenerados são úteis quando rotuladas como testes negativos.

## Mudanças prioritárias

1. Nos 9 arquivos `AXIOM_DEPENDENT_OR_LOCAL_TARGET` e `VACUOUS_TARGET`, retirar alegações de certificado incondicional e explicitar os axiomas/definições locais; preservar o conteúdo histórico.
2. No `MasterTheorem`, explicitar `[UniversalThetaFramework]` e a dependência transitiva dos axiomas.
3. Nos 10 arquivos `SCOPE_REVIEW`, verificar se os títulos e relatórios externos extrapolam o enunciado realmente provado. Não renomear contraexemplos corretos.
4. Para cada alvo terminal, exigir `#print axioms`, definição fiel, kernel executado, e correspondência com o enunciado original.

## Limites

O número de arquivos que **de fato exigem edição** continua desconhecido. Esta triagem detecta **10 unidades prioritárias para correção/explicitação de certificação**, não 10 alterações confirmadas. O inventário histórico de 250 repositórios e 4094 branches não foi reexecutado.
