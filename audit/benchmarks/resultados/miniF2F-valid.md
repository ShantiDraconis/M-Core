# Auditoria: miniF2F-valid

Fonte: https://github.com/yangky11/miniF2F-lean4 @ 5746b7d6c47855ce1294bed87329618ff7f1bc31 (leanprover/lean4:v4.24.0)

- módulos: 244; compilam: 244; teoremas auditados: 244
- com defeito certificado no kernel: 0

| Classe | Teoremas |
|---|---|
| divisao_inteira | 3 |
| divisao_por_zero_nao_excluida | 22 |
| funcao_totalizada | 8 |
| subtracao_em_N | 21 |
| trivial | 49 |

## Defeitos certificados

| Teorema | Arquivo:linha | Achados |
|---|---|---|

## Para revisão (trivial por uma tática; riscos de codificação)

| Teorema | Arquivo:linha | Achados |
|---|---|---|
| `aimeII_2001_p3` | `MiniF2F/Valid/aimeII_2001_p3.lean:7` | subtracao_em_N |
| `aimeII_2020_p6` | `MiniF2F/Valid/aimeII_2020_p6.lean:7` | divisao_por_zero_nao_excluida; subtracao_em_N |
| `aime_1983_p9` | `MiniF2F/Valid/aime_1983_p9.lean:7` | divisao_por_zero_nao_excluida |
| `aime_1987_p8` | `MiniF2F/Valid/aime_1987_p8.lean:7` | divisao_por_zero_nao_excluida |
| `aime_1997_p11` | `MiniF2F/Valid/aime_1997_p11.lean:7` | divisao_por_zero_nao_excluida |
| `amc12_2001_p9` | `MiniF2F/Valid/amc12_2001_p9.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2003_p1` | `MiniF2F/Valid/amc12a_2003_p1.lean:7` | subtracao_em_N |
| `amc12a_2003_p24` | `MiniF2F/Valid/amc12a_2003_p24.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2003_p25` | `MiniF2F/Valid/amc12a_2003_p25.lean:7` | funcao_totalizada=Real.sqrt |
| `amc12a_2008_p2` | `MiniF2F/Valid/amc12a_2008_p2.lean:7` | trivial=linarith |
| `amc12a_2008_p4` | `MiniF2F/Valid/amc12a_2008_p4.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2009_p2` | `MiniF2F/Valid/amc12a_2009_p2.lean:7` | trivial=norm_num |
| `amc12a_2009_p25` | `MiniF2F/Valid/amc12a_2009_p25.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2016_p3` | `MiniF2F/Valid/amc12a_2016_p3.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2017_p7` | `MiniF2F/Valid/amc12a_2017_p7.lean:7` | subtracao_em_N |
| `amc12a_2019_p21` | `MiniF2F/Valid/amc12a_2019_p21.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2019_p9` | `MiniF2F/Valid/amc12a_2019_p9.lean:7` | divisao_por_zero_nao_excluida |
| `amc12a_2020_p13` | `MiniF2F/Valid/amc12a_2020_p13.lean:7` | divisao_inteira |
| `amc12b_2002_p11` | `MiniF2F/Valid/amc12b_2002_p11.lean:7` | subtracao_em_N |
| `amc12b_2002_p3` | `MiniF2F/Valid/amc12b_2002_p3.lean:7` | subtracao_em_N |
| `imo_1964_p1_1` | `MiniF2F/Valid/imo_1964_p1_1.lean:7` | subtracao_em_N |
| `imo_1965_p1` | `MiniF2F/Valid/imo_1965_p1.lean:7` | funcao_totalizada=Real.sqrt |
| `imo_1966_p4` | `MiniF2F/Valid/imo_1966_p4.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1966_p5` | `MiniF2F/Valid/imo_1966_p5.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1967_p3` | `MiniF2F/Valid/imo_1967_p3.lean:7` | subtracao_em_N |
| `imo_1978_p5` | `MiniF2F/Valid/imo_1978_p5.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1979_p1` | `MiniF2F/Valid/imo_1979_p1.lean:7` | divisao_por_zero_nao_excluida |
| `imo_1987_p6` | `MiniF2F/Valid/imo_1987_p6.lean:7` | subtracao_em_N |
| `induction_divisibility_9div10tonm1` | `MiniF2F/Valid/induction_divisibility_9div10tonm1.lean:7` | subtracao_em_N |
| `induction_seq_mul2pnp1` | `MiniF2F/Valid/induction_seq_mul2pnp1.lean:7` | subtracao_em_N |
| `induction_sum2kp1npqsqm1` | `MiniF2F/Valid/induction_sum2kp1npqsqm1.lean:7` | subtracao_em_N |
| `induction_sum_1oktkp1` | `MiniF2F/Valid/induction_sum_1oktkp1.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_10` | `MiniF2F/Valid/mathd_algebra_10.lean:7` | trivial=norm_num |
| `mathd_algebra_104` | `MiniF2F/Valid/mathd_algebra_104.lean:7` | trivial=linarith |
| `mathd_algebra_109` | `MiniF2F/Valid/mathd_algebra_109.lean:7` | trivial=linarith |
| `mathd_algebra_11` | `MiniF2F/Valid/mathd_algebra_11.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_119` | `MiniF2F/Valid/mathd_algebra_119.lean:7` | trivial=linarith |
| `mathd_algebra_123` | `MiniF2F/Valid/mathd_algebra_123.lean:7` | trivial=omega; subtracao_em_N |
| `mathd_algebra_13` | `MiniF2F/Valid/mathd_algebra_13.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_131` | `MiniF2F/Valid/mathd_algebra_131.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_144` | `MiniF2F/Valid/mathd_algebra_144.lean:7` | trivial=omega |
| `mathd_algebra_181` | `MiniF2F/Valid/mathd_algebra_181.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_190` | `MiniF2F/Valid/mathd_algebra_190.lean:7` | trivial=norm_num |
| `mathd_algebra_224` | `MiniF2F/Valid/mathd_algebra_224.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_267` | `MiniF2F/Valid/mathd_algebra_267.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_282` | `MiniF2F/Valid/mathd_algebra_282.lean:7` | divisao_inteira |
| `mathd_algebra_35` | `MiniF2F/Valid/mathd_algebra_35.lean:7` | divisao_por_zero_nao_excluida |
| `mathd_algebra_433` | `MiniF2F/Valid/mathd_algebra_433.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_455` | `MiniF2F/Valid/mathd_algebra_455.lean:7` | trivial=linarith |
| `mathd_algebra_462` | `MiniF2F/Valid/mathd_algebra_462.lean:7` | trivial=norm_num |
| `mathd_algebra_480` | `MiniF2F/Valid/mathd_algebra_480.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_493` | `MiniF2F/Valid/mathd_algebra_493.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_51` | `MiniF2F/Valid/mathd_algebra_51.lean:7` | trivial=linarith |
| `mathd_algebra_536` | `MiniF2F/Valid/mathd_algebra_536.lean:7` | trivial=norm_num |
| `mathd_algebra_547` | `MiniF2F/Valid/mathd_algebra_547.lean:7` | funcao_totalizada=Real.sqrt |
| `mathd_algebra_568` | `MiniF2F/Valid/mathd_algebra_568.lean:7` | trivial=linarith |
| `mathd_algebra_69` | `MiniF2F/Valid/mathd_algebra_69.lean:7` | subtracao_em_N |
| `mathd_algebra_96` | `MiniF2F/Valid/mathd_algebra_96.lean:7` | trivial=linarith |
| `mathd_numbertheory_101` | `MiniF2F/Valid/mathd_numbertheory_101.lean:7` | trivial=rfl |
| `mathd_numbertheory_102` | `MiniF2F/Valid/mathd_numbertheory_102.lean:7` | trivial=rfl |
| `mathd_numbertheory_109` | `MiniF2F/Valid/mathd_numbertheory_109.lean:7` | subtracao_em_N |
| `mathd_numbertheory_110` | `MiniF2F/Valid/mathd_numbertheory_110.lean:7` | trivial=omega; subtracao_em_N |
| `mathd_numbertheory_132` | `MiniF2F/Valid/mathd_numbertheory_132.lean:7` | trivial=rfl |
| `mathd_numbertheory_136` | `MiniF2F/Valid/mathd_numbertheory_136.lean:7` | trivial=omega |
| `mathd_numbertheory_149` | `MiniF2F/Valid/mathd_numbertheory_149.lean:7` | trivial=rfl |
| `mathd_numbertheory_155` | `MiniF2F/Valid/mathd_numbertheory_155.lean:7` | trivial=rfl |
| `mathd_numbertheory_169` | `MiniF2F/Valid/mathd_numbertheory_169.lean:7` | trivial=rfl |
| `mathd_numbertheory_188` | `MiniF2F/Valid/mathd_numbertheory_188.lean:7` | trivial=rfl |
| `mathd_numbertheory_198` | `MiniF2F/Valid/mathd_numbertheory_198.lean:7` | trivial=omega |
| `mathd_numbertheory_200` | `MiniF2F/Valid/mathd_numbertheory_200.lean:7` | trivial=rfl |
| `mathd_numbertheory_202` | `MiniF2F/Valid/mathd_numbertheory_202.lean:7` | trivial=rfl |
| `mathd_numbertheory_211` | `MiniF2F/Valid/mathd_numbertheory_211.lean:7` | trivial=rfl |
| `mathd_numbertheory_236` | `MiniF2F/Valid/mathd_numbertheory_236.lean:7` | trivial=omega |
| `mathd_numbertheory_24` | `MiniF2F/Valid/mathd_numbertheory_24.lean:7` | trivial=rfl |
| `mathd_numbertheory_252` | `MiniF2F/Valid/mathd_numbertheory_252.lean:7` | trivial=rfl |
| `mathd_numbertheory_257` | `MiniF2F/Valid/mathd_numbertheory_257.lean:7` | subtracao_em_N |
| `mathd_numbertheory_269` | `MiniF2F/Valid/mathd_numbertheory_269.lean:7` | trivial=rfl |
| `mathd_numbertheory_284` | `MiniF2F/Valid/mathd_numbertheory_284.lean:7` | trivial=omega |
| `mathd_numbertheory_30` | `MiniF2F/Valid/mathd_numbertheory_30.lean:7` | trivial=rfl |
| `mathd_numbertheory_301` | `MiniF2F/Valid/mathd_numbertheory_301.lean:7` | trivial=omega |
| `mathd_numbertheory_33` | `MiniF2F/Valid/mathd_numbertheory_33.lean:7` | trivial=omega |
| `mathd_numbertheory_335` | `MiniF2F/Valid/mathd_numbertheory_335.lean:7` | trivial=omega |
| `mathd_numbertheory_37` | `MiniF2F/Valid/mathd_numbertheory_37.lean:7` | trivial=rfl |
| `mathd_numbertheory_370` | `MiniF2F/Valid/mathd_numbertheory_370.lean:7` | trivial=omega |
| `mathd_numbertheory_403` | `MiniF2F/Valid/mathd_numbertheory_403.lean:7` | trivial=rfl |
| `mathd_numbertheory_405` | `MiniF2F/Valid/mathd_numbertheory_405.lean:7` | subtracao_em_N |
| `mathd_numbertheory_45` | `MiniF2F/Valid/mathd_numbertheory_45.lean:7` | trivial=rfl |
| `mathd_numbertheory_458` | `MiniF2F/Valid/mathd_numbertheory_458.lean:7` | trivial=omega |
| `mathd_numbertheory_466` | `MiniF2F/Valid/mathd_numbertheory_466.lean:7` | trivial=rfl |
| `mathd_numbertheory_530` | `MiniF2F/Valid/mathd_numbertheory_530.lean:7` | divisao_inteira |
| `mathd_numbertheory_543` | `MiniF2F/Valid/mathd_numbertheory_543.lean:7` | subtracao_em_N |
| `mathd_numbertheory_640` | `MiniF2F/Valid/mathd_numbertheory_640.lean:7` | trivial=rfl |
| `mathd_numbertheory_739` | `MiniF2F/Valid/mathd_numbertheory_739.lean:7` | trivial=rfl |
| `mathd_numbertheory_81` | `MiniF2F/Valid/mathd_numbertheory_81.lean:7` | trivial=rfl |
| `mathd_numbertheory_84` | `MiniF2F/Valid/mathd_numbertheory_84.lean:7` | trivial=norm_num |
| `mathd_numbertheory_92` | `MiniF2F/Valid/mathd_numbertheory_92.lean:7` | trivial=omega |
| `mathd_numbertheory_961` | `MiniF2F/Valid/mathd_numbertheory_961.lean:7` | trivial=rfl |
| `numbertheory_aneqprodakp4_anmsqrtanp1eq2` | `MiniF2F/Valid/numbertheory_aneqprodakp4_anmsqrtanp1eq2.lean:7` | funcao_totalizada=Real.sqrt |
| `numbertheory_nckeqnm1ckpnm1ckm1` | `MiniF2F/Valid/numbertheory_nckeqnm1ckpnm1ckm1.lean:7` | subtracao_em_N |
| `numbertheory_sumkmulnckeqnmul2pownm1` | `MiniF2F/Valid/numbertheory_sumkmulnckeqnmul2pownm1.lean:7` | subtracao_em_N |
