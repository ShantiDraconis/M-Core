#!/usr/bin/env python3
"""Companheiro numérico da rodada 44: o núcleo de Perron (ATK/ZeroClasses/Perron.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `perron(L, c, T) = (1/2π) ∫_{−T}^{T} e^{(c+it)L}/(c+it) dt` por Simpson;
* `perron_degrau`: `|perron(L, c, T) − 1_{L>0}|` contra a cota `e^{cL}/(πT|L|)` numa grade de `L`, `c`, `T`;
* a razão erro/cota (sempre `≤ 1` se a cota vale) e o valor em `L = 0`, onde a cota não se aplica
  (`perron(0, c, T) → ½`).
"""
import cmath
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def perron(L, c, T, n=20000):
    h = 2 * T / n

    def f(t):
        z = complex(c, t)
        return cmath.exp(z * L) / z

    s = f(-T) + f(T)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(-T + k * h)
    return s * h / 3 / (2 * math.pi)


def main(saida=None):
    linhas = []
    pior = 0.0
    for L in (-2.0, -0.5, -0.1, 0.1, 0.5, 2.0):
        for c in (0.3, 1.0):
            for T in (5.0, 20.0, 60.0):
                p = perron(L, c, T)
                alvo = 1.0 if L > 0 else 0.0
                erro = abs(p - alvo)
                cota = math.exp(c * L) / (math.pi * T * abs(L))
                pior = max(pior, erro / cota)
                linhas.append({"L": L, "c": c, "T": T, "erro": erro, "cota": cota})
    meio = {str(T): [perron(0.0, 1.0, T).real, perron(0.0, 1.0, T).imag] for T in (5.0, 20.0, 60.0)}
    res = {"grade": linhas, "max_erro_sobre_cota": pior, "L_zero": meio}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "perron.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
