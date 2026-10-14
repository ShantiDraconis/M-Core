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
então `CookLevin modeloPNP SAT`. Essa hipótese é hipótese de teorema, não axioma.

## O que falta para B4 inteira (CL4b)

Só a máquina: `Nonempty (TM2ComputableInPolyTime cod cod (fCL V q))`. A fórmula é escrita por laços
com contadores unários (por isso as variáveis são `0^i 1 0^t 1 0^p 1`): calcular `m = q(n)`,
`T` e `S` em unário (Horner), percorrer instantes, casos finitos e células, e copiar os bits de `w`
na linha 0. Plano: uma linguagem pequena de laços com contadores, compilada para `TM2` com
correção e custo provados uma vez, e `fCL` escrita como programa dessa linguagem.

Até lá B4 fica em `PARCIAL_NO_KERNEL` e o contador de pontes continua em 1/8.
`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
