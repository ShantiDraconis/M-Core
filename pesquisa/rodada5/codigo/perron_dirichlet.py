#!/usr/bin/env python3
"""Companheiro numérico da rodada 45: Perron truncada para séries de Dirichlet
(ATK/ZeroClasses/PerronDirichlet.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `perron_LSeries` com `f = μ` (Möbius): `Σ_{n ≤ N} μ(n) n^{−s}` contra
  `(1/2π) ∫_{−T}^{T} x^{c+it} / ((c + it) ζ(s + c + it)) dt`, `x = N + ½`, e a cota `x^c (4x + 2) ζ(σ + c)/(πT)`;
* `abs_log_ge`: `min_n |log(x/n)| · (4x + 2) ≥ 1` para `x = N + ½`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def mobius(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    if m > 1:
        r = -r
    return r


def integral(s, c, x, T, h=0.01):
    n = int(2 * T / h)
    if n % 2:
        n += 1
    h = 2 * T / n

    def g(t):
        z = complex(c, t)
        return cmath.exp(z * math.log(x)) / (z * zc.zeta(s + z))

    tot = g(-T) + g(T)
    for k in range(1, n):
        tot += (4 if k % 2 else 2) * g(-T + k * h)
    return tot * h / 3 / (2 * math.pi)


def main(saida=None):
    linhas = []
    s = complex(0.8, 5.0)
    c = 0.5
    zs = zc.zeta(complex(s.real + c, 0)).real
    for N in (10, 30):
        x = N + 0.5
        soma = sum(mobius(n) * n ** (-s) for n in range(1, N + 1))
        for T in (20.0, 50.0):
            I = integral(s, c, x, T)
            erro = abs(soma - I)
            cota = x ** c * (4 * x + 2) * zs / (math.pi * T)
            linhas.append({"N": N, "T": T, "erro": erro, "cota": cota})
    pior_log = min(min(abs(math.log((N + 0.5) / n)) * (4 * (N + 0.5) + 2) for n in range(1, 4 * N + 10))
                   for N in range(0, 60))
    res = {"s": [s.real, s.imag], "c": c, "perron_mu": linhas, "min_log_vezes_4x2": pior_log}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "perron_dirichlet.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
