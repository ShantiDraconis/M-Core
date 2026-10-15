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

## Primeiro tijolo da função L de y² = x³ − x (`ATK/BSDPontosE32.lean`, 7 teoremas)

Na curva y² = x³ − x (condutor 32), o kernel já mostrou que B6 e O6 se reduzem a `L(E,1) ≠ 0` e
que O7 se reduz a um valor exato de `L(E,1)` (`ATK.BSDRefinada.pontes_E32_iff`,
`formula_E32_iff`). Chegar lá exige construir a função L dessa curva, que a Mathlib não continua
analiticamente. Primeiro passo, publicado e agora certificado:

* `card_afim`: para todo primo `p ≡ 3 (mod 4)`, `#{(x, y) ∈ 𝔽_p² : y² = x³ − x} = p`;
* `card_projetivo`, `traco_zero`: `#E(𝔽_p) = p + 1` e `a_p = 0` (primos supersingulares);
* a prova: `#{y : y² = a} = χ(a) + 1` e `Σ_x χ(x³ − x) = 0`, porque `x ↦ −x` troca o sinal e
  `χ(−1) = −1` quando `p ≡ 3 (mod 4)`.

Próximos tijolos, todos publicados: `a_p` para `p ≡ 1 (mod 4)` (somas de Jacobsthal,
`p = a² + b²`); ligar `a_p` ao fator de Euler `WeierstrassCurve.localEulerFactor` da Mathlib;
a série L como função L de Hecke de ℚ(i) e sua continuação; o valor de `L(E,1)`. Nada disso toca
O6 em geral nem O7 em geral, que seguem abertos.

## O fator de Euler na função L da Mathlib (`ATK/BSDEulerE32.lean`, 10 teoremas)

`polinomioLocal_E32`: para todo primo `v ∤ 2` com `q = #κ_v ≡ 3 (mod 4)`, o fator local que a
**própria Mathlib** usa em `WeierstrassCurve.LFunction` para `y² = x³ − x` é

> `localPolynomial = 1 + q T²`, isto é, `a_v = 0`.

Para chegar lá foram fechados três passos que abriram no caminho:

* `card_pontos`: sobre **todo** corpo finito `F` com `|F| ≡ 3 (mod 4)`, `#W(F) = |F| + 1` (não só
  `ℤ/p`);
* `card_pontos_mudanca`: a contagem não muda por mudança de variáveis (`equacao_mudanca`, bijeção
  `(x, y) ↦ (u²x + r, u³y + u²sx + t)`);
* `reducao_minimal`: a redução do modelo minimal que a Mathlib escolhe é `C̄ • W̄`; o `u` da mudança
  é unidade de `R` porque `u` e `u⁻¹` são raízes de `X¹² − w` e `X¹² − w⁻¹`.

Próximo: os primos `≡ 1 (mod 4)` (`a_p = 2a`, `p = a² + b²`) e o fator em 2.

Estado: BSD_CLAY aberto (B6 publicada não formalizada, O6 aberto), BSD_REFINED aberto (O7).
`UNIVERSAL_GREEN = false`, `FINAL_ROOT = null`, `CLOSED_MATH = false`.
