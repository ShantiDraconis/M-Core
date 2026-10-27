#!/usr/bin/env python3
"""Companheiro numérico da rodada 78: a fórmula explícita em `x` inteiro, com `ψ₀`
(ATK/ZeroClasses/ExplicitaInteira.lean).

Só biblioteca padrão (zeros de `canonico.py`, `ψ` de `explicita_limite.py`). **Nada aqui é certificado.**

* `integral_um_div`: `∫_{−T}^{T} dt/(c + it) = 2 arctan(T/c)` por quadratura do ponto médio;
* `perron_zero`: `|arctan(T/c)/π − ½| ≤ c/(πT)`;
* `formula_explicita_T_N`: em `x = 10, 11, 30` (`11` primo, `Λ(11) = log 11`), o erro com `ψ₀(N) = ψ(N) − Λ(N)/2`
  contra o erro com `ψ(N)`, usando os 341 zeros de `0 < γ ≤ 600`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import explicita_limite as el  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def mangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return 0.0


def main(saida=None):
    integrais = []
    for c, T in ((2.0, 10.0), (2.0, 100.0), (0.5, 50.0)):
        h = T / 200000
        quad = sum(h * c / (c * c + (-T + (j + 0.5) * h) ** 2) for j in range(int(2 * T / h)))
        integrais.append({"c": c, "T": T, "quadratura": quad, "formula": 2 * math.atan(T / c),
                          "perron_zero": abs(math.atan(T / c) / math.pi - 0.5), "cota": c / (math.pi * T)})
    g = ca.zeros(T=600.0)
    form = []
    for N in (10, 11, 30):
        x = float(N)
        psi = el.psi_cheb(N)
        psi0 = psi - mangoldt(N) / 2
        base = x - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
        soma = sum(2 * (x ** complex(0.5, t) / complex(0.5, t)).real for t in g)
        form.append({"N": N, "Lambda": mangoldt(N), "erro_psi0": soma - (base - psi0),
                     "erro_psi": soma - (base - psi)})
    out = {"integrais": integrais, "formula": form,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaInteira.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_inteira.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
