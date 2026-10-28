# Ponte B4 (Cook–Levin) — metade "SAT ∈ NP" no kernel (14/10/2026)

`CookLevin M SAT = SAT ∈ M.NP ∧ ∀ L ∈ M.NP, M.Red L SAT`. Sobre o modelo genuíno `modeloPNP`
(ligação L2, `CLOSED`), a primeira metade está provada:

**`ATK.SatNPMaquina.sat_em_NP : SAT ∈ classeNP`**, com só os 3 axiomas padrão (127 declarações em
`ATK/SatNPSemantica.lean` e `ATK/SatNPMaquina.lean`).

## Como

* **Certificado** (`cert`): um segmento `valor · índice · 10` por ocorrência de literal, com o
  índice escrito do bit mais significativo ao menos significativo; `|c| ≤ |x|` (`cert_length`).
  A valoração lida é `τ_c(i)` = valor do primeiro segmento com o índice de `i`.
* **Verificador** (`verif`): `|x|` par e `evalStart` sobre os símbolos de `x`, consultando o
  certificado em cada literal. `verif_par_sound` (o que é aceito é `codCNF φ` com `φ` satisfeita
  por `τ_c`) e `verif_codCNF` (sobre fórmulas codificadas, `verif` é a avaliação de `φ` sob `τ_c`).
* **`sat_iff_verif`**: `x ∈ SAT ⟺ ∃ c, |c| ≤ |x| ∧ verif ⟨x, c⟩ = true`.
* **A máquina** (`verifTM`): `FinTM2` com 7 pilhas e 19 rótulos.
  * Fase 0: decodifica `⟨x, c⟩` em símbolos.
  * Fase 1: avalia a fórmula. Cada literal faz uma consulta que varre o certificado, compara
    índices símbolo a símbolo e restaura as pilhas.
  * Cada passo foi verificado (`run_rx` … `run_fase1`, `run_total`). Tempo: `2 (n + 2)³`
    (`verifComputavel`).

## A outra metade: `∀ L ∈ NP, L ≤p SAT`

Dada uma linguagem com verificador `V : TM2ComputableInPolyTime cod encodeBool χ` e polinômio `q`:

| Marco | Módulo | O que está provado |
|---|---|---|
| CL1 | `CookLevinJanela` | um passo só lê/escreve as `profMax M` células do topo (`step_janela`) |
| CL2–CL3 | `CookLevinTableau` | tableau CNF (exatamente-um por grandeza; passo como tabela finita de casos; parada absorvente); `tableau_correto` |
| CL3b | `CookLevinRestricao` | alfabetos restritos ao que a máquina empilha (finito); `run_restr` |
| CL3c | `CookLevinInicio` | linha 0 com certificado livre de comprimento `≤ m` |
| CL3d | `CookLevinVerificador` | **`verificador_tableau`**: `formulaW V m w` satisfatível ⟺ `∃ c, |c| ≤ m ∧ χ (par w c) = true` |
| CL4a | `CookLevinReducao` | `fCL V q w := codCNF (fórmula de w)`; **`fCL_correta`**: `w ∈ L ⟺ fCL V q w ∈ SAT`; **`cookLevin_de_computavel`** |

`cookLevin_de_computavel` diz: se cada `fCL V q` é computável por uma `FinTM2` em tempo polinomial,
então `CookLevin modeloPNP SAT`.

## A máquina da redução (CL4b) e o fecho (CL5)

| Marco | Módulo | O que está provado |
|---|---|---|
| CL4b-1/2 | `Gerador` | linguagem de laços com contadores unários (`out`, `inc`, `dec`, `clr`, `seq`, `loop`, `forIn`) e o montador para `TM2`; **`asm_ok`**: o código montado faz o que a semântica diz, em `≤ cost` passos |
| CL4b-3 | `GeradorTM` | **`computavel`**: todo programa de custo `≤ B(|w|)` (polinômio) é `TM2ComputableInPolyTime` |
| CL4b-4a | `GeradorForm` | moldes de fórmula (cláusulas, laços sobre contadores e sobre os bits da entrada); `comp_ok` (escreve exatamente a fórmula), `comp_cost` (custo polinomial) |
| CL4b-4b | `GeradorArit` | aritmética unária: `evalP` calcula `q(x)` (`horn_coefs`) com custo polinomial |
| CL4b-4c | `CookLevinMolde` | o molde da fórmula de Cook–Levin (linhas, parada, casos em três zonas, linha inicial pelos bits de `w`, aceitação); `sem_formulaT`, `wf_formulaT` |
| CL4b-4d | `CookLevinPrograma` | `aritP`: `|w|`, `q(|w|)`, `T`, `S`, `S − c` nos contadores; semântica e custo |
| CL5 | `CookLevinFinal` | **`progCL_out`** (a saída é `fCL V q w`), **`fCL_computavel`**, **`cookLevin : CookLevin modeloPNP SAT`** |

`ATK.ObligationsClosed.B4 : ATK.Conditional.PvsNP.CookLevin ATK.ModeloPNP.modeloPNP
ATK.ModeloPNP.SAT` — só `propext`, `Classical.choice`, `Quot.sound`; sem `sorry`, sem `axiom`.
O enunciado da obrigação B4 em `obligations.json` passa a ser o predicado aplicado ao modelo
genuíno (ligação L2): antes era o predicado paramétrico, sem modelo, que não é uma proposição.

## Estado

Ponte B4 **provada no kernel**: contador de pontes 2/8 (B1, B4). P ≠ NP continua dependendo da
obrigação aberta O4 (`SATNotInP`). `UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
