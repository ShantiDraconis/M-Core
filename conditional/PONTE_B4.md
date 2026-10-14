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

## O que falta para B4 inteira

`∀ L ∈ NP, L ≤p SAT`. Dada uma linguagem com verificador `FinTM2` de tempo `p(n)`, é preciso:

1. a fórmula CNF que descreve a execução (tableau) de uma `FinTM2` arbitrária: várias pilhas,
   alfabetos finitos quaisquer e instruções em árvore (`TM2.Stmt`);
2. a correção: a fórmula é satisfatível ⟺ existe certificado que a máquina aceita;
3. a própria redução como `FinTM2` de tempo polinomial (a função `x ↦ codCNF φ_x`).

É um projeto maior que esta metade. Até ele, B4 fica em `PARCIAL_NO_KERNEL` e o contador de pontes
continua em 1/8. `UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
