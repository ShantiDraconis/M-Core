# Fechamento de OPEN_MATH — critério, portão e falsificadores

## O critério

`OPEN_MATH` é um **estado de conhecimento**, não uma proposição. Escrito como `Prop`
(`OpenMath := ¬ ClosedMath`), ele afirma que alguma conjectura é **falsa** — o kernel prova isso em
`ATK.Closure.openMath_prop_iff`. Por isso o fechamento é decidido no nível meta:

> `OPEN_MATH = false` ⇔ para cada um dos 7 problemas existe uma declaração nomeada que o kernel
> aceita com tipo **exatamente** igual ao enunciado oficial ou à sua negação, com axiomas
> ⊆ {propext, Classical.choice, Quot.sound}.

Fechar é **decidir** (prova ou refutação). O que **não** fecha, e o portão recusa:

| Tentativa | Por que é vazia | Teorema |
|---|---|---|
| `Nonempty (Resolution P)` | vale para todo `P` (terceiro excluído) | `resolution_nonempty` |
| `NavierStokes := A ∨ B ∨ C ∨ D` | `(A) ∨ (C)` é **teorema** (reescala `a·u(a t, x)`) | `clayA_or_clayC`, `navierStokes_disjunction` |
| `ExactCertificate` com NS | o campo NS é vazio; reduz-se a RH ∧ Beal ∧ P≠NP | `exactCertificate_iff` |
| `axiom`, `sorry` | não são prova | controles do portão |

BSD, Yang–Mills e Hodge não são enunciáveis na Mathlib v4.34.1, então hoje `OPEN_MATH = true`
**necessariamente**.

## O que tornaria cada fechamento falso

| Problema | Caso que torna o fechamento falso | Kernel |
|---|---|---|
| RH | zero não trivial de ζ com Re s ≠ 1/2; ele está necessariamente em 0 < Re s < 1 | `rh_false_iff`, `rh_counterexample_in_open_strip` |
| NS (A) | ν > 0 e dado suave, div 0, decaimento rápido, sem solução suave de energia limitada; então (C) vale | `clayA_false_iff`, `clayA_or_clayC` |
| Beal | Aˣ+Bʸ=Cᶻ, x,y,z>2, gcd = 1 (certificado finito) | `beal_false_iff`, `beal_refuted_by_witness` |
| P≠NP | P = NP | `pnp_false_iff` |
| BSD | curva E/ℚ com posto ≠ ord_{s=1} L(E,s) ou coeficiente líder ≠ fórmula | não enunciável |
| YM | G compacto simples sem teoria 4D ou sem lacuna espectral | não enunciável |
| Hodge | classe de Hodge racional que não é combinação de ciclos algébricos | não enunciável |

As leis AGOT de extração e de transporte são teoremas (`extraction_law`, `transport_law`) e ficam
**falsas** sem compacidade (`Ioc_not_compact`), sem semicontinuidade (`jumpDefect_not_lsc`) ou com
constante não uniforme (`transport_fails_nonuniform`).

## O portão

`closure_gate.py` (passo do CI depois do `lake build`) lê `registry.json`, compila
`theorem _ : <alvo exato> := @decl` para cada entrada, audita `#print axioms` e roda controles:
aceita uma decisão verdadeira de brinquedo; recusa tipo errado, `axiom`, `sorry`, a resolução
clássica vazia e a disjunção de NS. Saída: `reports/closure_gate.md` e `.json`.

Para propor um fechamento: compile o teorema em `ATK/` e acrescente
`{"problem": "...", "claim": "...", "decl": "..."}` ao registro. O portão faz o resto.
