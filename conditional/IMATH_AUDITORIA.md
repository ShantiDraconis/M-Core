# I-Mathematics — auditoria independente (14/10/2026)

Fonte: `ShantiDraconis/meta-mathematics-indeterminate-I`, commit `919fc81` (núcleo congelado em
`b8b1da78`), `src/IMath/**`: 10 arquivos Lean, 514 linhas, toolchain original Lean/Mathlib `v4.12.0`.

## Resultado do kernel

* Os 10 arquivos foram copiados para `atk-kernel/ATK/IMath/**` **sem mudança de conteúdo**; só os
  `import IMath.…` viraram `import ATK.IMath.…` (conferido por `diff`).
* Compilam em Lean `4.34.1` + Mathlib `v4.34.1`, o toolchain do kernel.
* Fontes: 0 `sorry`, 0 `axiom` declarado.
* Os **15 certificados** passam pelo auditor do kernel (`ATK/IMathPonte.lean`, apelidos `C01`–`C15`):
  cada um depende só de `propext`, `Classical.choice`, `Quot.sound`. O arquivo original imprime
  `#print axioms` de 8 dos 15 ("representativos"); aqui são os 15.

O núcleo IMath é uma **extensão conservadora**: tipos indutivos e estruturas, nenhum axioma. Isso o
separa dos sistemas de axiomas do `I` refutados em `ATK.IAlgebra` (PAX/`K_I`, P1).

## C01–C15 comparados com o ATK e com a Mathlib

| Cert. | Enunciado | No ATK | Na Mathlib | Veredito |
|---|---|---|---|---|
| C01 | `state I = indeterminate` | — (`RI` não tem estados) | — | novo na forma, definicional |
| C02 | `I ≠ ∞` | — (`RI` não tem `∞`) | — | novo na forma, construtores distintos |
| C03 | `I ≠ finito z` | `ATK.Indeterminacy.I_ne_ι` | `Option.some_ne_none` | análogo |
| C04 | `ℝ ↪ Phi3 ℂ` injetiva | `ATK.Indeterminacy.ι_injective` | `Complex.ofReal_injective` | análogo |
| C05 | `ℂ ↪ Phi3 ℂ` injetiva | `ATK.Indeterminacy.ι_injective` | injetividade de construtor | análogo |
| C06 | `0 ÷ 0 = I` | `ATK.Indeterminacy.zero_divI_zero` | — | análogo |
| C07 | `∞ ÷ ∞` guarda a expressão de origem | — | — | novo na forma, definicional |
| C08 | colapso idempotente | — | — | novo na forma, trivial |
| C09 | soma absorvente sem cancelamento à direita | `ATK.Indeterminacy.addI_I`, `sem_cancelamento` | — | análogo |
| C10 | refinamento transitivo | `ATK.IndeterminacyStates.refina_trans` (outra ordem) | `Set.Subset.trans` | **é o lema da Mathlib** |
| C11 | os germes `x/x` e `x²/x` são distintos | — | — | trivial |
| C12 | `x/x → 1` | `ATK.Indeterminacy.zero_div_zero_qualquer_valor` | limites elementares | subsumido |
| C13 | `x²/x → 0` | `ATK.Indeterminacy.zero_div_zero_qualquer_valor` | limites elementares | subsumido |
| C14 | a mesma forma `0/0` tem resoluções diferentes | `ATK.IFormas.div00_eq` (conjunto de valores de `0/0` = `[−∞, +∞]`) | — | subsumido |
| C15 | pontos determinados ↪ `IPoint` injetiva | — | injetividade ponto a ponto | trivial |

**Mathlib:** nenhum dos 15 é candidato a PR. `Refinement/Realization.lean` define
`refines A B := A ⊆ B`, e as três provas (`refl`, `trans`, `antisymm`) **são**
`Set.Subset.rfl`, `Set.Subset.trans`, `Set.Subset.antisymm`. Os limites de C12–C14 são casos
particulares do que a Mathlib já tem com `Tendsto`.

**ATK:** C12–C14 são casos particulares de resultados mais fortes já certificados
(`zero_div_zero_qualquer_valor`: todo real é limite de algum `0/0`; `div00_eq`). C03–C06 e C09
têm análogos em `ATK.Indeterminacy`, sobre outro portador.

## Duas definições de `I`, compatíveis (`ATK/IMathPonte.lean`, 9 teoremas)

| | IMath (`Phi3 α`) | ATK (`RI = Option ℝ`) |
|---|---|---|
| estados | finito, `∞`, indeterminado (guarda a expressão) | finito, `I` |
| `0/0` | `I` | `I` |
| `a/0`, `a ≠ 0` | `∞` | `I` |
| soma com `I` | `absorbingAdd` (experimental, não é a soma global) | `addI`, `I` absorvente |

A projeção `proj : Phi3 ℝ → RI` (finito ↦ finito; `∞` e indeterminados ↦ `I`):

* `pi_absorbingAdd`: `proj (x ⊕ y) = addI (proj x) (proj y)` para **todos** `x, y`;
* `pi_idiv`: `proj (a ÷ b) = divI a b` para todos os finitos, inclusive `0/0` e `a/0`;
* `pi_collapse`, `pi_surjective`, `pi_eq_I_iff` (`proj` identifica exatamente `∞` e os
  indeterminados);
* `modelos_diferem_em_um_sobre_zero`: em `Phi3`, `1/0 = ∞ ≠ I`; em `RI`, `1 ⊘ 0 = I`.

Logo `RI` é o quociente de `Phi3 ℝ` que identifica `∞` com `I`. As duas definições não se
contradizem: a do IMath guarda mais informação.

## O que isto não faz

Nenhum teorema aqui toca uma obrigação O1–O8. `UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`.
A varredura das outras definições de `I` (catálogo `catalog/ilaws/`) continua como estava: só a do
IMath foi comparada e ligada ao ATK.
