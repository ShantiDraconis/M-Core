# Status calculado do ATK

Gerado por `scripts/status_calculado.py` em 2026-10-22T10:47:48+00:00. Nada aqui é digitado.

* Teoremas `ATK.*` no ambiente: 6963; certificados (só axiomas padrão): 6963; proibidos: 0; axiomas declarados sob `ATK`: 0.
* Produtores materiais (portão existe e certificado): 0 de 7.

| Linha | Produtor | Equivalência certificada | Arquivo-portão existe | Produtor material |
| --- | --- | --- | --- | --- |
| RH | `Filter.Tendsto ATK.Conditional.Riemann.DN Filter.atTop (nhds 0)` | True | False | False |
| Beal | `ATK.BealCompleto.ExclusaoResidualFinal` | True | False | False |
| NS | `ATK.Conditional.NavierStokes.EnstrophyAPrioriBound M.ns` | None | False | False |
| PNP | `ATK.Conditional.PvsNP.SATNotInP M.cx M.sat` | None | False | False |
| Hodge | `ATK.Conditional.Hodge.MiddleCodimension M.hodge` | None | False | False |
| BSD | `ATK.Conditional.BSD.RankOpen M.bsd ∧ ATK.Conditional.BSD.RefinedOpen M.bsd` | None | False | False |
| YM | `ATK.Conditional.YangMills.ConstructiveYM4D M.ym` | None | False | False |

| Obrigação | Declarado | Calculado | Teorema |
| --- | --- | --- | --- |
| B1 | PROVADA_NO_KERNEL | PROVADA_NO_KERNEL | `ATK.ObligationsClosed.B1` |
| B2 | PARCIAL_NO_MODELO_DO_LANE | SEM_PROVA_NO_KERNEL | `—` |
| B3 | PROVADA_NO_KERNEL | PROVADA_NO_KERNEL | `ATK.ObligationsClosed.B3` |
| B4 | PROVADA_NO_KERNEL | PROVADA_NO_KERNEL | `ATK.ObligationsClosed.B4` |
| B5 | PUBLICADA_NAO_FORMALIZADA | SEM_PROVA_NO_KERNEL | `—` |
| B6 | PUBLICADA_NAO_FORMALIZADA | SEM_PROVA_NO_KERNEL | `—` |
| B7 | PUBLICADA_NAO_FORMALIZADA | SEM_PROVA_NO_KERNEL | `—` |
| B8 | PUBLICADA_NAO_FORMALIZADA | SEM_PROVA_NO_KERNEL | `—` |
| O1 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O1m | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O2 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O3 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O4 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O5 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O6 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O7 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| O8 | OPEN_MATH | SEM_PROVA_NO_KERNEL | `—` |
| L1 | CLOSED | PROVADA_NO_KERNEL | `ATK.LigacaoNS.clayA_iff` |
| L2 | CLOSED | PROVADA_NO_KERNEL | `ATK.ModeloPNP.fielL2` |
| L3 | NAO_EXISTE_NA_MATHLIB | SEM_PROVA_NO_KERNEL | `—` |
| L4 | PARTE_DO_POSTO_NO_KERNEL | SEM_PROVA_NO_KERNEL | `—` |
| L5 | NAO_EXISTE_NA_MATHLIB | SEM_PROVA_NO_KERNEL | `—` |
