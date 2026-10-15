# atk-fermat

Subprojeto que compila **do código-fonte** a prova completa do Último Teorema de Fermat em Lean
(`anthropics/fermats-last-theorem`, commit `6e837e7`, Lean 4.33.1, Mathlib `v4.33.0`) e prova
com ela, no ATK:

- `ATK.Fermat.fermat : FermatLastTheorem` (enunciado da Mathlib);
- `ATK.Fermat.beal_de_mdc_ge_tres_incondicional`: Beal vale para todo triplo com `mdc(x,y,z) ≥ 3`;
- `ATK.Fermat.beal_iff_residual_incondicional`: Beal ⟺ o resíduo `mdc(x,y,z) ≤ 2` (obrigação O2).

As reduções são as de `atk-kernel/ATK/BealFermat.lean` (lá com FLT como hipótese explícita),
copiadas porque o atk-kernel está em outra Mathlib.

**Custo.** O projeto da Anthropic tem 60 474 módulos. Segundo o README dele, o build leva
5 h 32 min com 96 jobs, com pico de 153 GB de memória, até 36 GB num único módulo e ~300 GB de
disco. O CI hospedado do GitHub não comporta isso. O workflow `atk-fermat.yml` é manual e roda
num runner auto-hospedado com o rótulo `atk-grande`.

Nada aqui prova Beal: o resíduo `mdc ∈ {1, 2}` continua aberto.
