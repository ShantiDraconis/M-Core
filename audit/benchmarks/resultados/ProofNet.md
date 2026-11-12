# Auditoria: ProofNet

Fonte: https://github.com/rahul3613/ProofNet-lean4 @ 6deae98b38954dadf732746d023e8be65c56f246 (leanprover/lean4:v4.20.0)

- módulos: 11; compilam: 11; teoremas auditados: 360
- com defeito certificado no kernel: 1

| Classe | Teoremas |
|---|---|
| divisao_inteira | 4 |
| divisao_por_zero_nao_excluida | 18 |
| falso_por_contraexemplo | 1 |
| funcao_totalizada | 8 |
| subtracao_em_N | 17 |
| trivial | 4 |

## Defeitos certificados

| Teorema | Arquivo:linha | Achados |
|---|---|---|
| `exercise_4_4_9` | `Auditados/Herstein.lean:173` | falso_por_contraexemplo=2; divisao_inteira; subtracao_em_N |

## Para revisão (trivial por uma tática; riscos de codificação)

| Teorema | Arquivo:linha | Achados |
|---|---|---|
| `exercise_1_3` | `Auditados/Axler.lean:10` | trivial=norm_num |
| `exercise_1_4` | `Auditados/Axler.lean:14` | trivial=norm_num |
| `exercise_5_13` | `Auditados/Axler.lean:85` | subtracao_em_N |
| `exercise_6_3` | `Auditados/Axler.lean:109` | divisao_por_zero_nao_excluida |
| `exercise_1_1_20` | `Auditados/DummitFoote.lean:40` | trivial=norm_num |
| `exercise_2_1_5` | `Auditados/DummitFoote.lean:88` | subtracao_em_N |
| `exercise_2_1_13` | `Auditados/DummitFoote.lean:93` | divisao_por_zero_nao_excluida |
| `exercise_9_4_2d` | `Auditados/DummitFoote.lean:396` | subtracao_em_N |
| `exercise_2_2_6c` | `Auditados/Herstein.lean:35` | subtracao_em_N |
| `exercise_2_4_36` | `Auditados/Herstein.lean:50` | subtracao_em_N |
| `exercise_2_11_22` | `Auditados/Herstein.lean:136` | subtracao_em_N |
| `exercise_4_2_9` | `Auditados/Herstein.lean:161` | divisao_por_zero_nao_excluida; divisao_inteira |
| `exercise_5_4_3` | `Auditados/Herstein.lean:221` | divisao_por_zero_nao_excluida |
| `exercise_1_27` | `Auditados/IrelandRosen.lean:7` | subtracao_em_N |
| `exercise_2_21` | `Auditados/IrelandRosen.lean:23` | divisao_inteira; funcao_totalizada=Real.log |
| `exercise_2_27a` | `Auditados/IrelandRosen.lean:29` | divisao_por_zero_nao_excluida |
| `exercise_3_10` | `Auditados/IrelandRosen.lean:42` | subtracao_em_N |
| `exercise_3_14` | `Auditados/IrelandRosen.lean:46` | subtracao_em_N |
| `exercise_4_5` | `Auditados/IrelandRosen.lean:57` | divisao_inteira; subtracao_em_N |
| `exercise_4_8` | `Auditados/IrelandRosen.lean:66` | subtracao_em_N |
| `exercise_4_11` | `Auditados/IrelandRosen.lean:70` | subtracao_em_N |
| `exercise_2_32a` | `Auditados/Pugh.lean:23` | trivial=norm_num |
| `exercise_3_4` | `Auditados/Pugh.lean:58` | funcao_totalizada=Real.sqrt |
| `exercise_3_63a` | `Auditados/Pugh.lean:62` | divisao_por_zero_nao_excluida; funcao_totalizada=Real.log |
| `exercise_3_63b` | `Auditados/Pugh.lean:67` | divisao_por_zero_nao_excluida; funcao_totalizada=Real.log |
| `exercise_2018_b4` | `Auditados/Putnam.lean:20` | subtracao_em_N |
| `exercise_2010_a4` | `Auditados/Putnam.lean:39` | subtracao_em_N |
| `exercise_2001_a5` | `Auditados/Putnam.lean:43` | subtracao_em_N |
| `exercise_1998_b6` | `Auditados/Putnam.lean:62` | funcao_totalizada=Real.sqrt |
| `exercise_3_2a` | `Auditados/Rudin.lean:141` | funcao_totalizada=Real.sqrt |
| `exercise_3_7` | `Auditados/Rudin.lean:165` | divisao_por_zero_nao_excluida; funcao_totalizada=Real.sqrt |
| `exercise_3_13` | `Auditados/Rudin.lean:179` | subtracao_em_N |
| `exercise_5_2` | `Auditados/Rudin.lean:320` | divisao_por_zero_nao_excluida |
| `exercise_5_4` | `Auditados/Rudin.lean:333` | divisao_por_zero_nao_excluida |
| `exercise_5_6` | `Auditados/Rudin.lean:346` | divisao_por_zero_nao_excluida |
| `exercise_5_7` | `Auditados/Rudin.lean:355` | divisao_por_zero_nao_excluida |
| `exercise_1_19b` | `Auditados/Shakarchi.lean:26` | divisao_por_zero_nao_excluida |
| `exercise_1_19c` | `Auditados/Shakarchi.lean:31` | divisao_por_zero_nao_excluida |
| `exercise_2_2` | `Auditados/Shakarchi.lean:43` | divisao_por_zero_nao_excluida |
| `exercise_3_3` | `Auditados/Shakarchi.lean:61` | divisao_por_zero_nao_excluida |
| `exercise_3_4` | `Auditados/Shakarchi.lean:66` | divisao_por_zero_nao_excluida |
| `exercise_3_9` | `Auditados/Shakarchi.lean:71` | funcao_totalizada=Real.log |
| `exercise_3_22` | `Auditados/Shakarchi.lean:79` | divisao_por_zero_nao_excluida |
