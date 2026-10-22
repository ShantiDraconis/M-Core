# Mapa das folhas: o que a árvore de redução não captura

Proposta do autor (cinco pontos), com o que foi **conferido no kernel ou na Mathlib v4.34.1** nesta
sessão e as **correções** que a conferência exigiu.

## 1. Folhas compartilhadas

| Folha | Serve a | Observação |
|---|---|---|
| finitude de `#Ш` (Kolyvagin para uma classe de curvas) | O6 e O7 | um esforço, dois avanços |
| FLT completo (ponte B2, externa) | O2 (`exponent_gcd_le_two`) e qualquer redução a Fermat | |
| análise real (regiões de zeros; desigualdades de Sobolev) | O1 e O3 | sobreposição real é menor do que parece: O1 usa análise complexa de `ζ`, O3 análise funcional |

## 2. Interface: o enunciado da literatura é o que o kernel precisa?

Uma linha por folha marcada "fechável" (o modo de falha do B3/`lerayHopf`).

| Folha | Literatura | Campo do kernel | Mesmo enunciado? |
|---|---|---|---|
| O1, necessidade | Báez-Duarte 2003: `d_N → 0` sob RH, com `χ = 𝟙_(0,1]`, `ρ_k(t) = {1/(kt)}`, `L²((0,∞), dt)` | `ATK.Conditional.Riemann.DN` com exatamente essas escolhas; `NecessidadeRH` (`FechamentoO1`) | **sim** (normalização confere; por fonte, de memória) |
| O3, ponte | BKM (`∫‖ω‖_∞ dt = ∞` na explosão) e Prodi–Serrin–Ladyzhenskaya (`u ∈ L^p_t L^q_x`, `2/p + 3/q ≤ 1` ⇒ suave) | `EnstrophyBlowupCriterion`: na explosão, a **enstrofia** fica ilimitada (Leray 1934) | **não**: é um terceiro critério. "O3 = BKM + PSL fechável" é nome parecido, não interface. **Fechável com interface**: provar `EnstrophyBlowupCriterion` a partir de BKM ou de PSL é trabalho próprio |
| O7, instância | `L(E,1)/Ω = #Ш · ∏c_p / #E(ℚ)_tors²` | `FormulaRefinada`; para `y² = x³ − x`: `… / 16` | **sim**: `16 = 4²` (torsão `ℤ/2 × ℤ/2`), e `periodo` integra sobre `{g > 0}` inteiro (as duas componentes de `E(ℝ)`), que é o `Ω` de BSD |
| O8, sombra | Wightman (Streater–Wightman cap. 3) | `structure Wightman` (`L5Base`) | **sim**, 11/12 campos 1:1, e o 12º (domínio de `φ`) provado inofensivo no kernel (`F1_O8.md` §6) |

## 3. Promoção: o que fechar uma folha compra

* Uma instância verificada (O7 numérico) **não** muda `status(O7)`: o alvo é `RefinedOpen`, para
  toda curva. Isso é progresso sem mudança de estado; o registro precisaria de um campo separado
  (`instancias_fechadas`), não criado.
* Se `YMNucleo` for provado no kernel, o item O8 passa a `T`. **Decisão pendente do autor**: ou
  `CLOSED_MATH` passa a contar a sombra (e então `CLOSED_MATH = true` não significaria "Clay
  resolvido"), ou O8 é trocado por um enunciado fiel antes. `StatusFinal.shadowO8 = true` já
  registra que o O8 contado não é o Clay.

## 4. Gatilhos de re-auditoria (I.3), um por obrigação

| O | Evento externo | Efeito |
|---|---|---|
| O1 | região livre de zeros `Re s > 1 − ε` com `ε > 0` **fixo** ("quase-RH") | não fecha O1, mas é um intermediário real: hoje só existem regiões que encolhem (`1 − c/log t`). *Correção*: a proposta original dizia que não havia intermediário |
| O2 | prova de ABC | implica Beal **a menos de finitos contraexemplos**, não Beal inteiro. *Correção*: a proposta dizia "Beal segue" |
| O4 | cota inferior superpolinomial de circuitos para SAT | `NP ⊄ P/poly` ⇒ P ≠ NP; as barreiras (relativização, provas naturais, algebrização) são contra técnicas, não contra o resultado |
| O6 | conjectura principal de Iwasawa para posto ≥ 2 | reduz a outro aberto; não colapsa |
| O7 | finitude de `Ш` em geral | colapsa a parte de finitude; a fórmula continua |
| O8 | construção de Yang–Mills contínuo 4D | fecha o Clay, não muda `YMNucleo` (que, por fonte, já tem testemunha) |

## 5. Mathlib: o que existe e o que falta (conferido em v4.34.1)

Correções ao mapa proposto:

* **Sobolev fracionário existe**: `Mathlib/Analysis/FunctionalSpaces/BesselPotentialSpace.lean`
  (espaços de potencial de Bessel `H^{s,p}`) e `Mathlib/Analysis/Distribution/Sobolev`. O que
  falta para O3 é a teoria de EDP por cima (BKM, PSL), não os espaços.
* O não-anulamento em `Re s = 1` se chama `riemannZeta_ne_zero_of_one_le_re`
  (`NumberTheory/LSeries/Nonvanishing.lean`); `zeta_ne_zero_of_re_eq_one` não existe.
* `LinearPMap` está em `Mathlib/LinearAlgebra/LinearPMap.lean`, com o adjunto em
  `Mathlib/Analysis/InnerProductSpace/LinearPMap.lean`.
* `WeierstrassCurve` tem `LFunction` em `Mathlib/AlgebraicGeometry/EllipticCurve/LFunction.lean`.

## Frase de encerramento (proposta do autor)

"Para sete dos oito, a árvore de redução termina num problema Millennium. O kernel torna a folha
explícita e verificável; não a move. O trabalho futuro é (a) fechar as folhas fecháveis, (b)
registrar as interfaces, e (c) esperar a matemática, que é o que nenhum destes oito depende do
kernel para acontecer."

Ajuste pela seção 2: O3 é fechável **com interface** (o critério do kernel é o de enstrofia, não
BKM nem PSL).
