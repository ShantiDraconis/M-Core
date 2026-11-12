# Auditoria: miniF2F-test

Fonte: https://github.com/yangky11/miniF2F-lean4 @ 5746b7d6c47855ce1294bed87329618ff7f1bc31 (leanprover/lean4:v4.24.0)

- módulos: 244; compilam: 244; teoremas auditados: 244
- com defeito certificado no kernel: 2

| Classe | Teoremas |
|---|---|
| divisao_inteira | 7 |
| divisao_por_zero_nao_excluida | 18 |
| falso | 1 |
| funcao_totalizada | 7 |
| hipoteses_contraditorias | 1 |
| subtracao_em_N | 18 |
| trivial | 57 |

## Defeitos certificados

| Teorema | Arquivo:linha | Achados |
|---|---|---|
| `mathd_algebra_208` | `MiniF2F/Test/mathd_algebra_208.lean:7` | falso=norm_num; divisao_inteira |
| `mathd_algebra_275` | `MiniF2F/Test/mathd_algebra_275.lean:7` | hipoteses_contraditorias=simp_all; divisao_inteira |

## Para revisão (trivial por uma tática; riscos de codificação)

| Teorema | Arquivo:linha | Achados |
|---|---|---|
| `aime_1983_p1` | `MiniF2F/Test/aime_1983_p1.lean:7` | divisao_por_zero_nao_excluida; funcao_totalizada=Real.log |
| `aime_1983_p3` | `MiniF2F/Test/aime_1983_p3.lean:7` | funcao_totalizada=Real.sqrt |
| `aime_1989_p8` | `MiniF2F/Test/aime_1989_p8.lean:7` | trivial=linarith |
| `aime_1991_p9` | `MiniF2F/Test/aime_1991_p9.lean:7` | divisao_por_zero_nao_excluida |
| `algebra_cubrtrp1oncubrtreq3_rcubp1onrcubeq5778` | `MiniF2F/Test/algebra_cubrtrp1oncubrtreq3_rcubp1onrcubeq5778.lean:7` | divisao_por_zero_nao_excluida |
| `algebra_ineq_nto1onlt2m1on` | `MiniF2F/Test/algebra_ineq_nto1onlt2m1on.lean:7` | divisao_por_zero_nao_excluida |
| `algebra_sum1onsqrt2to1onsqrt10000lt198` | `MiniF2F/Test/algebra_sum1onsqrt2to1onsqrt10000lt198.lean:7` | divisao_por_zero_nao_excluida; funcao_totalizada=Real.sqrt |
| `amc12_2000_p6` | `MiniF2F/Test/amc12_2000_p6.lean:7` | subtracao_em_N |
| `amc12_2001_p5` | `MiniF2F/Test/amc12_2001_p5.lean:7` | divisao_inteira |
| `amc12a_2013_p4` | `MiniF2F/Test/amc12a_2013_p4.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2019_p12` | `MiniF2F/Test/amc12a_2019_p12.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2020_p7` | `MiniF2F/Test/amc12a_2020_p7.lean:7` | subtracao_em_N |
| `amc12a_2021_p25` | `MiniF2F/Test/amc12a_2021_p25.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2021_p3` | `MiniF2F/Test/amc12a_2021_p3.lean:7` | trivial=omega; divisao_inteira |
| `amc12a_2021_p8` | `MiniF2F/Test/amc12a_2021_p8.lean:7` | subtracao_em_N |
| `amc12a_2021_p9` | `MiniF2F/Test/amc12a_2021_p9.lean:7` | trivial=rfl; subtracao_em_N |
| `amc12b_2002_p2` | `MiniF2F/Test/amc12b_2002_p2.lean:7` | trivial=linarith |
| `amc12b_2020_p2` | `MiniF2F/Test/amc12b_2020_p2.lean:7` | trivial=norm_num |
| `amc12b_2020_p21` | `MiniF2F/Test/amc12b_2020_p21.lean:7` | funcao_totalizada=Real.sqrt |
| `amc12b_2021_p18` | `MiniF2F/Test/amc12b_2021_p18.lean:7` | divisao_por_zero_nao_excluida |
| `amc12b_2021_p3` | `MiniF2F/Test/amc12b_2021_p3.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1968_p5_1` | `MiniF2F/Test/imo_1968_p5_1.lean:7` | funcao_totalizada=Real.sqrt |
| `imo_1969_p2` | `MiniF2F/Test/imo_1969_p2.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1981_p6` | `MiniF2F/Test/imo_1981_p6.lean:7` | subtracao_em_N |
| `imo_1985_p6` | `MiniF2F/Test/imo_1985_p6.lean:7` | divisao_por_zero_nao_excluida |
| `imo_2001_p6` | `MiniF2F/Test/imo_2001_p6.lean:7` | subtracao_em_N |
| `induction_nfactltnexpnm1ngt3` | `MiniF2F/Test/induction_nfactltnexpnm1ngt3.lean:7` | subtracao_em_N |
| `induction_pord1p1on2powklt5on2` | `MiniF2F/Test/induction_pord1p1on2powklt5on2.lean:7` | divisao_por_zero_nao_excluida |
| `induction_pprime_pdvdapowpma` | `MiniF2F/Test/induction_pprime_pdvdapowpma.lean:7` | subtracao_em_N |
| `induction_prod1p1onk3le3m1onn` | `MiniF2F/Test/induction_prod1p1onk3le3m1onn.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_107` | `MiniF2F/Test/mathd_algebra_107.lean:7` | trivial=linarith |
| `mathd_algebra_125` | `MiniF2F/Test/mathd_algebra_125.lean:7` | trivial=omega |
| `mathd_algebra_139` | `MiniF2F/Test/mathd_algebra_139.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_142` | `MiniF2F/Test/mathd_algebra_142.lean:7` | trivial=linarith |
| `mathd_algebra_160` | `MiniF2F/Test/mathd_algebra_160.lean:7` | trivial=linarith |
| `mathd_algebra_17` | `MiniF2F/Test/mathd_algebra_17.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_170` | `MiniF2F/Test/mathd_algebra_170.lean:7` | divisao_inteira |
| `mathd_algebra_176` | `MiniF2F/Test/mathd_algebra_176.lean:7` | trivial=linarith |
| `mathd_algebra_24` | `MiniF2F/Test/mathd_algebra_24.lean:7` | trivial=linarith |
| `mathd_algebra_270` | `MiniF2F/Test/mathd_algebra_270.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_289` | `MiniF2F/Test/mathd_algebra_289.lean:7` | subtracao_em_N |
| `mathd_algebra_296` | `MiniF2F/Test/mathd_algebra_296.lean:7` | trivial=rfl |
| `mathd_algebra_304` | `MiniF2F/Test/mathd_algebra_304.lean:7` | trivial=rfl |
| `mathd_algebra_314` | `MiniF2F/Test/mathd_algebra_314.lean:7` | trivial=norm_num; divisao_inteira |
| `mathd_algebra_329` | `MiniF2F/Test/mathd_algebra_329.lean:7` | trivial=linarith |
| `mathd_algebra_332` | `MiniF2F/Test/mathd_algebra_332.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_354` | `MiniF2F/Test/mathd_algebra_354.lean:7` | trivial=linarith |
| `mathd_algebra_359` | `MiniF2F/Test/mathd_algebra_359.lean:7` | trivial=linarith |
| `mathd_algebra_362` | `MiniF2F/Test/mathd_algebra_362.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_388` | `MiniF2F/Test/mathd_algebra_388.lean:7` | trivial=linarith |
| `mathd_algebra_392` | `MiniF2F/Test/mathd_algebra_392.lean:7` | divisao_inteira; subtracao_em_N |
| `mathd_algebra_398` | `MiniF2F/Test/mathd_algebra_398.lean:7` | trivial=linarith |
| `mathd_algebra_400` | `MiniF2F/Test/mathd_algebra_400.lean:7` | trivial=linarith |
| `mathd_algebra_412` | `MiniF2F/Test/mathd_algebra_412.lean:7` | trivial=linarith |
| `mathd_algebra_427` | `MiniF2F/Test/mathd_algebra_427.lean:7` | trivial=linarith |
| `mathd_algebra_432` | `MiniF2F/Test/mathd_algebra_432.lean:7` | trivial=linarith |
| `mathd_algebra_440` | `MiniF2F/Test/mathd_algebra_440.lean:7` | trivial=linarith |
| `mathd_algebra_80` | `MiniF2F/Test/mathd_algebra_80.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_numbertheory_1124` | `MiniF2F/Test/mathd_numbertheory_1124.lean:7` | trivial=omega |
| `mathd_numbertheory_12` | `MiniF2F/Test/mathd_numbertheory_12.lean:7` | trivial=rfl |
| `mathd_numbertheory_127` | `MiniF2F/Test/mathd_numbertheory_127.lean:7` | trivial=rfl |
| `mathd_numbertheory_175` | `MiniF2F/Test/mathd_numbertheory_175.lean:7` | trivial=omega |
| `mathd_numbertheory_185` | `MiniF2F/Test/mathd_numbertheory_185.lean:7` | trivial=omega |
| `mathd_numbertheory_207` | `MiniF2F/Test/mathd_numbertheory_207.lean:7` | trivial=rfl |
| `mathd_numbertheory_212` | `MiniF2F/Test/mathd_numbertheory_212.lean:7` | trivial=rfl |
| `mathd_numbertheory_229` | `MiniF2F/Test/mathd_numbertheory_229.lean:7` | trivial=rfl |
| `mathd_numbertheory_235` | `MiniF2F/Test/mathd_numbertheory_235.lean:7` | trivial=rfl |
| `mathd_numbertheory_237` | `MiniF2F/Test/mathd_numbertheory_237.lean:7` | trivial=rfl |
| `mathd_numbertheory_239` | `MiniF2F/Test/mathd_numbertheory_239.lean:7` | trivial=rfl |
| `mathd_numbertheory_247` | `MiniF2F/Test/mathd_numbertheory_247.lean:7` | trivial=omega |
| `mathd_numbertheory_254` | `MiniF2F/Test/mathd_numbertheory_254.lean:7` | trivial=rfl |
| `mathd_numbertheory_293` | `MiniF2F/Test/mathd_numbertheory_293.lean:7` | trivial=omega |
| `mathd_numbertheory_299` | `MiniF2F/Test/mathd_numbertheory_299.lean:7` | trivial=rfl |
| `mathd_numbertheory_3` | `MiniF2F/Test/mathd_numbertheory_3.lean:7` | trivial=rfl |
| `mathd_numbertheory_320` | `MiniF2F/Test/mathd_numbertheory_320.lean:7` | trivial=omega; subtracao_em_N |
| `mathd_numbertheory_328` | `MiniF2F/Test/mathd_numbertheory_328.lean:7` | trivial=omega |
| `mathd_numbertheory_34` | `MiniF2F/Test/mathd_numbertheory_34.lean:7` | trivial=omega |
| `mathd_numbertheory_342` | `MiniF2F/Test/mathd_numbertheory_342.lean:7` | trivial=rfl |
| `mathd_numbertheory_343` | `MiniF2F/Test/mathd_numbertheory_343.lean:7` | trivial=rfl |
| `mathd_numbertheory_345` | `MiniF2F/Test/mathd_numbertheory_345.lean:7` | trivial=rfl |
| `mathd_numbertheory_430` | `MiniF2F/Test/mathd_numbertheory_430.lean:7` | subtracao_em_N |
| `mathd_numbertheory_447` | `MiniF2F/Test/mathd_numbertheory_447.lean:7` | trivial=rfl |
| `mathd_numbertheory_517` | `MiniF2F/Test/mathd_numbertheory_517.lean:7` | trivial=rfl |
| `mathd_numbertheory_521` | `MiniF2F/Test/mathd_numbertheory_521.lean:7` | subtracao_em_N |
| `mathd_numbertheory_551` | `MiniF2F/Test/mathd_numbertheory_551.lean:7` | trivial=rfl |
| `mathd_numbertheory_559` | `MiniF2F/Test/mathd_numbertheory_559.lean:7` | trivial=omega |
| `mathd_numbertheory_582` | `MiniF2F/Test/mathd_numbertheory_582.lean:7` | trivial=omega |
| `mathd_numbertheory_618` | `MiniF2F/Test/mathd_numbertheory_618.lean:7` | subtracao_em_N |
| `mathd_numbertheory_66` | `MiniF2F/Test/mathd_numbertheory_66.lean:7` | trivial=rfl |
| `mathd_numbertheory_728` | `MiniF2F/Test/mathd_numbertheory_728.lean:7` | trivial=rfl; subtracao_em_N |
| `mathd_numbertheory_764` | `MiniF2F/Test/mathd_numbertheory_764.lean:7` | subtracao_em_N |
| `mathd_numbertheory_765` | `MiniF2F/Test/mathd_numbertheory_765.lean:7` | trivial=omega |
| `mathd_numbertheory_769` | `MiniF2F/Test/mathd_numbertheory_769.lean:7` | trivial=rfl |
| `mathd_numbertheory_85` | `MiniF2F/Test/mathd_numbertheory_85.lean:7` | trivial=rfl |
| `mathd_numbertheory_99` | `MiniF2F/Test/mathd_numbertheory_99.lean:7` | trivial=omega |
| `numbertheory_2pownm1prime_nprime` | `MiniF2F/Test/numbertheory_2pownm1prime_nprime.lean:7` | subtracao_em_N |
| `numbertheory_3pow2pownm1mod2pownp3eq2pownp2` | `MiniF2F/Test/numbertheory_3pow2pownm1mod2pownp3eq2pownp2.lean:7` | subtracao_em_N |
