# Indeterminações como pontos de 3 estados — formalização verificada pelo kernel

Arquivo Lean: [`atk-kernel/ATK/Indeterminacy.lean`](../atk-kernel/ATK/Indeterminacy.lean) ·
**50 teoremas, todos certificados** (Lean 4.34.1 + Mathlib v4.34.1; axiomas só
`propext`, `Classical.choice`, `Quot.sound`; nenhum `sorry`, nenhum `axiom`).

Esta é a proposta do autor — *cada indeterminação é um ponto com 3 estados; as interações entre
pontos são pontos com 3 estados ou mais; o estado é resolvido e medido por L'Hôpital, e a medida é
uma constante* — escrita como matemática que o kernel aceita. Os textos de outras IAs anexados à
conversa descreviam esses resultados mas não conseguiram compilar (sem Lean no ambiente delas).
Aqui todos foram compilados e auditados.

## 1. O ponto de 3 estados

Um **ponto** é o germe orientado `a·tᵐ` quando `t → 0⁺`, com `a ≠ 0` e ordem `m ∈ ℤ`.
O estado é decidido pela ordem:

| ordem `m` | estado | comportamento (teorema) |
|---|---|---|
| `m > 0` | `zero` | `a·tᵐ → 0` (`estado_zero_tendsto`) |
| `m = 0` | `finito` | constante `a` |
| `m < 0` | `infinito` | `a·tᵐ → +∞` para `a > 0` (`estado_infinito_tendsto`) |

**Interações** (`mul`, `div`, `inv`) fecham: produto, quociente e inverso de pontos são pontos, e o
germe respeita as operações (`germe_mul`, `germe_div`, `germe_inv`, `mul_inv_eq_um`). O estado do
quociente é decidido pela ordem relativa `m − n` (`estado_div_zero_iff`, `estado_div_finito_iff`,
`estado_div_infinito_iff`); inverter troca `zero ↔ infinito` e fixa `finito` (`estado_inv_*`).

## 2. A medida é uma constante

- **Estado finito**: se as ordens coincidem, `p/q → a/b` (`medida_finita`). A indeterminação
  `0/0` desse par **é medida pela constante `a/b`**.
- **L'Hôpital**: `f(0) = g(0) = 0`, `f'(0) = a`, `g'(0) = b ≠ 0` ⇒ `f/g → a/b` (`lhopital_mede`).
  Exemplo verificado: `(eᵗ − 1)/t → 1` (`exp_sub_one_div_mede`).
- **`0⁰` mede a multiplicidade**: para `t ∈ (0,1)`,
  `(tᵐ)^(c/(−log t)) = e^(−mc)` **exatamente** (`zero_pow_zero_mede`), logo o limite é a constante
  `e^(−mc)` (`zero_pow_zero_tendsto`). A forma `0⁰` devolve a ordem `m` como número.

## 3. Por que a ordem é indispensável

- `0/0` tem os **3 estados**: existem pontos de estado `zero` cujo quociente cai em `zero`,
  `finito` ou `infinito` (`zero_div_zero_tres_estados`); o mesmo para `∞/∞`
  (`inf_div_inf_tres_estados`).
- **Todo real é a medida de algum `0/0`** (`zero_div_zero_qualquer_valor`).
- Só o limite perde a ordem: `t` e `t²` têm o mesmo estado, mas o quociente os distingue
  (`limite_perde_ordem`).

Ou seja: a constante que mede uma indeterminação vem dos **dados do ponto** (coeficiente e ordem),
não do símbolo `0/0`.

## 4. A constante `I = 0 ⊘ 0`

Em `RI = Option ℝ` (com `I = none`) a divisão é total e `0 ⊘ 0 = I` (`zero_divI_zero`); a inclusão
de ℝ é injetiva e preserva soma e produto (`ι_injective`, `ι_add`, `ι_mul`); `I` é absorvente
(`mulI_I`, `addI_I`).

Duas propriedades que o kernel também prova e que limitam o que `I` pode fazer:

- **Sem cancelamento**: `I·D = I·0` para todo `D` (`sem_cancelamento`) — nenhuma regra com `I`
  deduz `D = 0`.
- **Não é anel**: `0·I = I ≠ 0` (`nao_anel`).

## 5. Lógica de 4 estados e certificado

- Belnap–Dunn: `T, F, B, N`; negação troca componentes, `nao B = B`; acúmulo de evidência é
  comutativo, associativo e idempotente; **sem explosão** — `P` e `¬P` designados não tornam um `Q`
  arbitrário designado (`nao_explode`).
- `ClosedMath P := Certificado P` e **`ClosedMath P ↔ P`** (`closedMath_iff`); fechado e refutado ao
  mesmo tempo é impossível (`closed_e_refutado_impossivel`); a flag `!false` vale `true` e mesmo
  assim `False` não está fechado (`flag_nao_e_prova`).

## 6. O que isso faz com os 7 problemas

O kernel prova, no mesmo arquivo, os limites da construção:

- **`RH_I_iff`**: a Hipótese de Riemann reescrita na extensão com `I` *é* a Hipótese de Riemann.
  A constante não move nenhum zero.
- **`monotona_nao_basta`**: uma sequência decrescente e positiva (`1/2 + 1/(2(N+1))`) não tende a 0 e
  não tem majorante `K/log(N+2)`. Decrescer não fecha a rota de Báez-Duarte.
- `log_majorante_tendsto` e `um_gerador_otimo` são os passos certificados da rota de Riemann: o
  majorante força `D_N → 0`, e o coeficiente ótimo de um gerador é `b/a`. A cota uniforme para a
  família concreta (obrigação **O1**) continua sendo o que falta.

Por isso este módulo entra no kernel como **infraestrutura certificada** e **não muda o portão**:
`CLOSED_MATH` é calculado por `ATK.ClosedMathGate.closed_math`, que exige um termo sem hipóteses
de cada obrigação O1–O8. A teoria dos 3 estados descreve e mede indeterminações com rigor; ela não
contém, por si, nenhuma informação sobre onde estão os zeros de ζ, sobre MDC de soluções de Beal ou
sobre regularidade de Navier–Stokes — e o kernel mostrou isso formalmente para o caso de Riemann.

## Próximo passo que de fato aproximaria um fechamento

Usar a medida por ordem onde ela tem conteúdo: na rota de Riemann, `D_N` é um ponto do tipo
`K/log N`. Provar que o germe de `D_N` (família concreta `ρ_k(t) = {1/(k t)}`) tem estado `zero`
com ordem logarítmica **é** a obrigação O1. A linguagem dos 3 estados é adequada para enunciá-la;
a desigualdade em si ainda precisa ser provada.
