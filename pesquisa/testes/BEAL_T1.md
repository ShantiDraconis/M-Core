# BEAL T1: mapa de cobertura (kernel × pontes × literatura) em {3..200}³

**Hipótese.** S4 − S2 ≥ 25 p.p.: a maior parte do "83,21% aberto" do kernel já estaria resolvida na literatura arbitrada,
e (2,3,13), (2,5,7) e (3,5,11) dominariam o ranking.

**Método.**
- (x,y,z) fica coberto por A^p + B^q = C^r sobre ℤ se algum arranjo de (+aˣ, +bʸ, −cᶻ), ou de todos com sinal trocado,
  nos slots (+A^p, +B^q, −C^r) cumpre: expoente do slot divide o do termo; sinal diferente só em slot de expoente ímpar.
  Os padrões (dx,dy,dz) são gerados em Python e marcados num cubo de 198³ bytes em C.
- Conservadora: entradas "*" da Tab. 1.1 (Ratcliffe–Grechuk, 2412.11933v2) só na ordem enunciada, as demais a menos de
  permutação. Permissiva: todas a menos de permutação.
- Levantamento (as 10 soluções conhecidas e 1+2³=3²): toda identidade tem um termo que só é potência com expoente ≤ 2,
  então **nenhuma levanta** a Beal e a regra fica só divisibilidade mais paridade de sinal.

**Controles (todos passaram).**
- S0 e S2 recalculados num laço Python independente, direto das definições Lean (`ExclusaoResidualRegular`, `ResidualFinal`):
  **887.152 (11,43%)** e **1.303.296 (16,79%)**, com 0 divergências célula a célula contra os padrões.
- S2 em mdc ≤ 2: 800.982 (11,03%), igual ao `obligations.json`. |E| = 7.762.392 e |mdc ≤ 2| = 7.260.078.
- Três candidatas recontadas por enumeração direta, idênticas ao C: (2,3,13) 36.566, (2,5,7) 41.592, (3,5,11) 32.316.

**Resultados (cumulativos; conservadora, entre parênteses a permissiva).**

| cenário | % de E | % de mdc≤2 |
|---|---|---|
| S0 kernel (`beal_iff_residual_regular`) | 11,43 | 5,32 |
| S1 + FLT (B2) | 11,45 | 5,32 |
| S2 + DM fraca do kernel (B8) | 16,79 | 11,03 |
| S3 + DM sobre ℤ (todas as permutações e sinais) | 27,17 | 22,13 |
| S4 + literatura arbitrada (Tab. 1.1 sem GRH; (2,3,15)) | **66,00** (66,92) | 63,64 (64,63) |
| S5 + GRH: (2,3,11), (5,5,11), (5,5,13), (7,7,11), (13,13,7) | 66,87 (67,75) | 64,57 (65,52) |
| S6 + sem arbitragem: (3,5,7) Chocian, (13,13,5) BDF | 67,21 (68,09) | 64,94 (65,88) |
| S7 + SFC (p,p,q) de Mihăilescu (não verificada) | 71,17 (72,04) | 69,17 (70,10) |
| S7 + ABC_{7/4} (s ≤ 4/7) | 99,995: restam 380 triplos ordenados (70 classes) | |

- **Ranking bruto sobre S4** (triplos descobertos que cada assinatura cobriria):
  (2,5,11) 47.602; (2,3,11) 45.614 [já resolvida sob GRH]; (2,5,7) 41.592; (2,5,13) 38.634; (2,3,13) 36.566; (3,5,11) 32.316;
  (2,7,11) 31.328; (2,5,17) 28.798; (2,3,17) 26.832; (3,5,13) 25.944; (2,7,13) 25.150; (3,5,7) 24.720; (3,4,11) 20.774.
- **Bruto sobre S6** (com GRH e Chocian): (2,5,7) 30.824 ≈ (2,5,11) 30.502 > (2,5,13) 27.794 > (2,3,13) 26.244. **Guloso sobre S4** (ganho marginal): (2,5,11), (2,3,11), (2,5,7), (2,3,13), (2,5,13), depois (2,3,p) para p = 29, 31, 37, 23, 17, 19.
  As 25 escolhas juntas cobrem só **15,9%** dos 2.639.559 triplos descobertos.
- **Descobertos em S4 com s > 0,61353** (um contraexemplo ali não seria recorde abc): 62 triplos ordenados em 11 classes,
  (3,4,p) para p ∈ {11,13,17,19,23,29,31}, (3,4,22), (3,4,26), (3,5,7) e (3,5,11).

**Interpretação.**
- **Hipótese confirmada com folga:** S4 − S2 = +49,2 p.p. Só com teoremas arbitrados, o "aberto" do kernel cai de 83,21% para 34,0% de E.
- O maior salto isolado é reescrever B8 sobre ℤ (S2→S3: +10,4 p.p.); a forma fraca perde permutações e sinais, como previa Q2(i).
- Ranking: (2,5,7), (2,3,13) e (3,5,11) estão no top 6 mas não dominam. (2,5,11) e (2,5,13) valem tanto ou mais; (2,5,11) só
  lidera porque (5,5,11) é GRH. A cauda é longa: nenhuma assinatura passa de 1,8% do descoberto, o que reforça B4.
- **Discrepância:** no resíduo S7+ABC_{7/4}, 69 das 70 classes se reduzem a Q = {(3,4,p), (3,5,p) com 7 ≤ p ≤ 23} de
  Laishram–Shorey. A exceção é **(4,5,7)** (s = 0,593 > 4/7), que depende de (2,5,7) ou (4,5,7), abertas.
  Ou o resumo de Q no mapa está incompleto, ou L–S usam um argumento fora desta lista. É preciso conferir no artigo.

**Limites.**
- A Tab. 1.1 veio de uma extração resumida do HTML, não de cópia literal. Incluí (2,3,15) (Siksek–Stoll) apesar de um artefato.
  A leitura de (2j,2k,17)* como "j,k primos ≠ 5" pode estar errada.
- Fora do mapa: IUT-Zhou (a lista das 2446 não estava disponível) e resultados parciais (BCDF (11,11,n) com 2∣a+b, (7,7,n)).
  A caixa {3..200}³ é arbitrária: números finitos descrevem a caixa, não Beal.
**Próximos passos.** (i) `Covered` (arranjo + não-levantamento) no Lean, com S0/S2 conferidos por `decide` numa caixa pequena.
(ii) Ler L–S para resolver (4,5,7). (iii) Lista de Zhou para S7-IUT. (iv) Alvos: (2,5,7), (2,5,11), (2,3,13), (2,5,13), (3,5,11).

Código: `tests/code/BEAL_T1_{patterns.py,mark.c,analyze.py,candcheck.py}`; saída: `tests/work/BEAL_T1_analyze.out`. Tempo ≈ 1 min (C) + 3 min (Python).
