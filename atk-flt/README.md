# atk-flt

Subprojeto separado do `atk-kernel`: usa o [`flt-regular`](https://github.com/leanprover-community/flt-regular)
(Último Teorema de Fermat para primos regulares, formalização completa) para provar casos de Beal.

- Lean `v4.35.0`, Mathlib `089be84` (a mesma fixada pelo `flt-regular` em `b8a5f23`).
- Separado porque o `atk-kernel` está na Mathlib `v4.34.1` e não pode depender do `flt-regular`.
- CI: `.github/workflows/atk-flt.yml` compila, roda `#print axioms` e exige só
  `propext`, `Classical.choice`, `Quot.sound` (`scripts/check_axioms.py`).

Arquivo: `AtkFlt/BealRegular.lean`. Nada aqui toca a obrigação O2 (`mdc(x, y, z) ≤ 2`).
