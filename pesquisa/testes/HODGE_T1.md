# HODGE T1: censo de caracteres de Hodge em X_m^4, 3 ≤ m ≤ 100

**Hipótese testada (H1, do frontier).** Para m par em [22,64], R_m ≠ ∅ só se 3 | m. R_m = órbitas sob (ℤ/m)^× de caracteres de Hodge que não são decomponíveis nem quase-decomponíveis, isto é, as que violam (P_m^4).

**Método.** Código em `tests/code/HODGE_T1.c`, `HODGE_T1_check.py`, `HODGE_T1_check2.py` e `HODGE_T1_classify.py`; saídas brutas em `tests/work/`.
- *Enumeração.* Multiconjuntos 1 ≤ a_0 ≤ … ≤ a_5 ≤ m−1 com Σa = 3m, testando Σ⟨t a_i⟩ = 3m para todo t ∈ (ℤ/m)^×; dim Hdg²_prim = Σ 6!/∏mult!.
- *Definições (da Silva, arXiv 2101.04739, conferidas no PDF).* **dec**: existe um par {b, −b} ⊂ a. **qdec**: a + {β,−β} = c + d com c, d ∈ M_m e c, d ≠ a; módulo dec, equivale a uma partição 3+3 com tripla T de soma s ≢ 0 e (T, −s) ∈ M_m(2). (P_m^4) ⇔ R_m = ∅, e pelo Thm 2.5 de da Silva (atribuído a Shioda) (P_m^4) ⇒ HC(X_m^4).
- *Anotações extras, fora de (P_m^4).* **tsplit**: duas triplas de soma 0 (vem de X^1×X^1 + Lefschetz (1,1); critério (1) de Jumagulov). **aoki5** = {x + j·m/5} ∪ {−5x}; **prog4** contém {x + j·m/4}; **mult5/mult4** contêm x·H, H ≤ (ℤ/m)^× de ordem 5/4.

**Controles (todos passaram).**
- *dim Hdg²_prim.* m = 3, 4, 5, 6 dão 20, 141, 400, 1751 = postos de AMV (1711.02628, Tab. 1: 21, 142, 401) menos h², e h^{2,2} = 1752 da sêxtica. Os "pareáveis" em m = 6 somam 1001 = posto linear 1002 da AMV menos 1.
- *Força bruta.* Em m ≤ 9 (todas as 6-uplas ordenadas, definição literal sem a redução 3+3) e em m ∈ {25, 32, 33, 36} (recenseamento Python independente), (orb, indec, qdec, R) idênticos ao C. Os 77 representantes residuais reverificados um a um.
- *Literatura.* R_m = ∅ para todo m ≤ 20 (Shioda, Thm 2.7) e m = 21, 27 (da Silva, Thm 3.5). R_33 ≠ ∅ (Prop. 3.6): **exatamente 1 órbita**, (1,4,16,22,25,31) = {4^k} ∪ {2m/3}. Tabela φ(m) de da Silva consistente em 20..43 (φ = 1 ⇒ 0 indecomponíveis; φ ≥ 3 ⇒ há indecomponíveis em y = 3).
- **Controle do frontier que falhou, por erro do frontier e não do código.** "mdc(m,6) = 1 ⇒ R_m = ∅ (Prop. 3.1)" é falso para R_m: m = 25, 35, 55, 65, 85, 95 têm 1 órbita cada, sempre aoki5. O Thm 3.3 de da Silva usa linhas de Aoki/Shioda, não (P_m^4): HC vale ali, mas (P_m^4) falha.

**Parâmetros efetivos.** Todo m de 3 a 100 (pedido: até 64), cerca de 13 s de CPU; sem redução.

**Resultados, m par em [22,64]** (#órb = órbitas de Hodge; R = órbitas residuais, com sua dimensão; R' = R sem tsplit):

| m | dim Hdg²_prim | #órb | R (dim) | R' | estrutura de R' |
|---|---|---|---|---|---|
| 22, 24, 26, 28, 30, 34, 38, 46, 58 | — | — | **0** | 0 | — |
| 32 | 727201 | 196 | 1 (2880) | 1 | prog4 |
| 36 | 1923971 | 574 | 9 (69120) | 8 | 8 outro |
| 40 | 2016681 | 496 | 1 (2880) | 1 | aoki5 |
| 42 | 5661851 | 1030 | 1 (4320) | 1 | outro |
| 44 | 1843141 | 342 | 1 (7200) | 1 | prog4 |
| 48 | 3911651 | 959 | 12 (72000) | 12 | 3 prog4, 1 mult4, 8 outro |
| 50 | 2639041 | 397 | 4 (34560) | 4 | 2 aoki5, 2 outro |
| 52 | 2925981 | 444 | 1 (8640) | 1 | prog4 |
| 54 | 4314491 | 719 | 20 (259200) | 18 | 18 outro |
| 56 | 3902701 | 651 | 7 (51840) | 7 | 2 prog4, 5 outro |
| 60 | 16107791 | 2794 | 9 (70560) | 8 | 1 mult4, 7 outro |
| 62 | 4795621 | 445 | 1 (4320) | 1 | mult5: {33^k} ∪ {31} |
| 64 | 5150721 | 615 | 2 (8640) | 2 | prog4 |

- *Ímpares ≤ 64 com R ≠ ∅.* 25, 35, 55 (aoki5); 33 (mult5); 39 (2 órbitas, ambas tsplit: R' = ∅); 45 (aoki5 + mult4). São ∅: 21, 27, 51, 57, 63.
- *Extensão 65..100.* R_m = ∅ para m par ∈ {74, 82, 86, 94, 98} e ímpares 69, 77, 81, 87, 91, 93. Maiores R': m = 66 (23), 72 (27), 78 (38), 84 (25), 90 (24), 96 (34). Lista completa em `tests/work/HODGE_T1_*.txt`.

**Interpretação honesta.**
- **H1 é refutada como enunciada:** R_m ≠ ∅ com m par e 3 ∤ m em m = 32, 40, 44, 50, 52, 56, 62, 64.
- *Versão refinada sugerida.* Fora de 3 | m, quase todo resíduo tem estrutura de progressão (aoki5/prog4) ou de coset multiplicativo (mult5/mult4); exceções: m = 50 (2 órbitas), 56 (5), além de 70 e 100. O "outro" denso aparece com 3 | m: 36, 42, 48, 54, 60, 66, …, 96.
- *O que o teste mostra.* (P_m^4) vale, por cálculo finito exato, para m par ∈ {22, 24, 26, 28, 30, 34, 38, 46, 58, 74, 82, 86, 94, 98}; pelo Thm 2.5, HC(X_m^4) nesses m. São **candidatos a casos novos**: não chequei se Aoki (1987) já cobre m = 2p, 28, 24 ou 30.
- *Padrão aritmético.* 2p com R = ∅, mas 62 = 2·31 com R ≠ ∅ (ord_31(2) = 5): o obstáculo parece ser elementos de ordem 5 em (ℤ/m)^×.
- *Só sugestão.* Que prog4/aoki5/mult* sejam "standard" no sentido de Aoki, logo algébricos; não implementei o cálculo de Aoki.

**Limites.**
- Só (P_m^4) + tsplit. Não implementei os ciclos padrão de Aoki, os critérios "two-pair"/"level-lifted" de Jumagulov nem Favero–Kelly.
- O censo de Jumagulov (78 299 representantes, 89 níveis ímpares) não é comparável: o texto acessível não dá contagens por m, e nossa soma de órbitas em ímpares 21..99 já é 10 351.
- O teorema de Shioda/da Silva foi usado como caixa-preta (insumo de fonte).

**Próximos testes.**
1. Implementar os elementos padrão de Aoki e reclassificar R'; em m ∈ {32, 44, 52, 64}, se prog4 for padrão, H1 vale "módulo Aoki".
2. Certificar em Lean (T3) a lista de m com R_m = ∅.
3. Atacar m = 50 e 56 (primeiros resíduos sem estrutura com 3 ∤ m); levar as órbitas de m = 36 e 54 ao 032 e a Favero–Kelly.
