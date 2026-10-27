#!/usr/bin/env python3
"""Companheiro numérico da rodada 77: a fórmula explícita para `x` real não inteiro
(ATK/ZeroClasses/ExplicitaReal.lean).

Só biblioteca padrão (zeros de `canonico.py`, `ψ` de `explicita_limite.py`). **Nada aqui é certificado.**

* `abs_log_ge_x`: `min_n |log(x/n)| · (2x + 2)/d ≥ 1` para `x = 10,3; 30,7; 100,05`, `d = dist(x, ℤ)`;
* `formula_explicita_T_x`: `Σ_{|γ|≤T} x^ρ/ρ` contra `x − ψ(x) − log 2π − ½ log(1 − x^{−2})` para `x = 10,3` e
  `x = 30,7`, `T = 100, 300, 600` (os 341 zeros de `0 < γ ≤ 600`).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import explicita_limite as el  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None):
    logs = []
    for x in (10.3, 30.7, 100.05):
        d = min(x - math.floor(x), math.ceil(x) - x)
        m = min(abs(math.log(x / n)) for n in range(1, int(10 * x)))
        logs.append({"x": x, "d": d, "min_log_vezes_constante": m * (2 * x + 2) / d})
    g = ca.zeros(T=600.0)
    form = []
    for x in (10.3, 30.7):
        alvo = x - el.psi_cheb(int(math.floor(x))) - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
        erros = []
        for T in (100, 300, 600):
            soma = sum(2 * (x ** complex(0.5, t) / complex(0.5, t)).real for t in g if t <= T)
            erros.append({"T": T, "erro": soma - alvo})
        form.append({"x": x, "alvo": alvo, "erros": erros})
    out = {"abs_log": logs, "formula": form,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaReal.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_real.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
