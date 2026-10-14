# As definições de `I` do acervo contra o `I` do ATK (14/10/2026)

`ATK/IPortadores.lean` (30 teoremas). Referência: `RI = Option ℝ`, `I = none` absorvente
(`ATK.Indeterminacy`, modelo ABS). Fonte dos portadores: `ShantiDraconis/The-Algebra-of-Ideterminate-I`,
com os blobs citados no catálogo `catalog/ilaws/A_algebra_of_I.md` §1 (conferidos), mais o IMath
(`ATK/IMathPonte.lean`).

"INCOMPATÍVEL" significa sempre: **não existe** `f : X → RI` que fixe os números (reais ou
naturais) e preserve as operações indicadas — qualquer que seja o valor de `f(I)`.

| Portador | Veredito | Teoremas |
|---|---|---|
| **ABS** (`ModelElement`, sobre ℚ) | EQUIVALENTE ao `RI` restrito a ℚ: mergulho que preserva `+`, `·`, `÷` | `ABS.emb_injective`, `emb_add`, `emb_mul`, `emb_div` |
| **IMath** (`Phi3`) | QUOCIENTE: `RI = Phi3 ℝ / (∞ ~ I)`. A soma passa ao quociente em todos os casos; a divisão só entre finitos | `IMathPonte.pi_absorbingAdd`, `pi_idiv`; `imath_divisao_nao_preservada` (`1 ÷ ∞ = 0` em `Phi3`, `1 ⊘ I = I` em `RI`) |
| **NexusField** (N1–N15) | COMPATÍVEL: `RI` é um NexusField, e todo NexusField tem `inv 0 = I` e `0·I = I`, a lei do `RI` | `Nexus.modeloRI`, `inv_zero_eq_I`, `zero_mul_I` |
| **CARD** (`ℕ ∪ {I}`) | MERGULHO para `⊕` e `⊗`; INCOMPATÍVEL para `⊖` (`n ⊖ n = I`, mas `n − n = 0`) | `CARD.emb_add`, `emb_mul`, `emb_injective`, `sub_incompativel` |
| **KIJ** (`ℝ ∪ {I, J}`) | INCOMPATÍVEL: `0 ⊗ I = 0` com `I` absorvente na soma | `KIJ.zero_mul_I`, `incompativel` |
| **IEA** (singularidades) | INCOMPATÍVEL (mesmo motivo). O axioma **A3 é falso** no próprio modelo, para todo `λ` e nas duas leituras de `x ⊕ y ⊕ z` | `IEA.incompativel`, `A3_falso` |
| **AEI** ("`I = 1/0`") | INCOMPATÍVEL: `0·I = 1`. A multiplicação **não é associativa**: `(0·I)·I = I`, `0·(I·I) = 1` | `AEI.incompativel`, `nao_associativa` |
| **ZDIV** | INCOMPATÍVEL: `1 ⊕ (−1) = I`. `⊕` **não é associativa**: `(1⊕1)⊕(−1) = 1`, `1⊕(1⊕(−1)) = I`. O axioma **`j_property : J = 1 ⊘ I` é falso** (`1 ⊘ I = I` pela própria definição) | `ZDIV.incompativel`, `nao_associativa`, `j_property_falso` |
| **FLEX** (`a + bI`, `Ω(I) = I`) | INCOMPATÍVEL com `RI` (`(−1)·I + I = 0`: `I` tem oposto). EQUIVALENTE ao anel `ℝ × ℝ` por `a + bI ↦ (a, a + b)` | `FLEX.incompativel`, `iso_add`, `iso_mul`, `iso_bijective`, `I_idempotente` |
| **PAX** (P1–P15) | INCONSISTENTE: P2, P4, P5, P10 e P12 já provam `False` | `PAX_inconsistente` |

## Leitura

Os portadores formam dois blocos sem ponte entre si:

* **`0·I = I`** (ABS, IMath, NexusField, CARD): compatíveis com o `RI` do ATK. Um NexusField
  qualquer é forçado a essa lei pelos próprios axiomas N1, N2 e N15.
* **`0·I ≠ I`** (KIJ e IEA com `0·I = 0`, AEI com `0·I = 1`, FLEX como anel): não há aplicação
  que preserve as operações. AEI e ZDIV ainda perdem a associatividade, e FLEX é só o anel `ℝ × ℝ`
  com outro nome.

PAX não tem modelo nenhum.

## Fidelidade

CARD, ABS, NexusField, ZDIV e as operações de FLEX são transcritos da fonte. Em KIJ, IEA e AEI a
fonte **não compila como está**: usa padrões literais `real 0` sobre `ℝ` e nomes de `def` (`I`,
`J`) como padrões. O arquivo usa a semântica pretendida, escrita nos comentários da fonte e no
catálogo (`0 ⊗ I = 0`, `0·I = 1`), com `if a = 0` no lugar do padrão literal.

## Limites

Nada aqui toca uma obrigação O1–O8. `UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`. Os
portadores menores do catálogo (ExtendedOperations, multiestado, rodas, ultrapotência, lógica
`{T, F, I}`) não foram comparados.
