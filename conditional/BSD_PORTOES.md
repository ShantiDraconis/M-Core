# BSD em dois portões: BSD_CLAY e BSD_REFINED (15/10/2026)

O enunciado oficial do Clay para BSD é a parte do posto; a fórmula do coeficiente líder é a forma
refinada. A linha BSD do projeto **continua exigindo as duas**:

> **BSD_FULL = BSD_CLAY ∧ BSD_REFINED** (`ATK.BSDPortoes.full_iff`)

A separação não enfraquece o alvo. Ela só torna cada parte um portão auditável por si.

| Portão | Enunciado no modelo | Peças | Arquivo do portão |
|---|---|---|---|
| BSD_CLAY | `BSDRank modeloGenuino` (`ord_{s=1} L(E,s) = posto E(ℚ)` para toda E/ℚ) | ligação L4, ponte B6 (Gross–Zagier–Kolyvagin), produtor O6 | `ATK/Terminal/BSDClay.lean` (modelo `BSDClay.lean.tpl`) |
| BSD_REFINED | `RefinedOpen modeloGenuino` (Ш finito e `L^{(r)}(E,1)/r! = Ω·Reg·∏c_p·#Ш/#tors²`) | ligação L4, produtor O7 | `ATK/Terminal/BSDRefinada.lean` (modelo `BSDRefinada.lean.tpl`) |
| BSD_FULL (a linha) | `BSDFull modeloGenuino` | nenhuma própria: compõe os dois | `ATK/Terminal/BSD.lean` (modelo `BSD.lean.tpl`) |

## O que o kernel certifica (`ATK/BSDPortoes.lean`, 9 teoremas)

* `full_iff`, `full_clay`, `full_refinada`, `full_de_partes`: BSD_FULL é exatamente a conjunção.
* `clay_iff`: BSD_CLAY = ponte B6 ∧ produtor O6. `refinada_iff`: BSD_REFINED = produtor O7.
* `clay_fiel`: com modularidade e Mordell–Weil (teoremas publicados, como hipóteses explícitas),
  BSD_CLAY no modelo do posto (L4) é **exatamente** `ClayBSD`, o enunciado do Clay sobre a Mathlib.
* `clay_nao_implica_full`, `refinada_nao_implica_clay`: em modelos-teste, cada parte vale sem a
  outra. As duas são independentes; tirar a fórmula refinada do alvo o enfraqueceria de fato.

## Na contagem

* `terminal_gates.json`: a linha BSD ganhou `subgates` (BSD_CLAY, BSD_REFINED) e `full_rule`;
  `universal_green.py` calcula e relata os subportões (`SUBGATES_GREEN`), sem mudar a regra da linha.
* `instalar_portao.py BSDClay` / `BSDRefinada` instala um subportão com as mesmas exigências.
* As peças B6, O6 e O7 mudaram de modelo (`BSDClay`, `BSDRefinada`) no catálogo `termos.json`; o
  número de termos que faltam não muda.

Estado: BSD_CLAY aberto (B6 publicada não formalizada, O6 aberto), BSD_REFINED aberto (O7).
`UNIVERSAL_GREEN = false`, `FINAL_ROOT = null`, `CLOSED_MATH = false`.
