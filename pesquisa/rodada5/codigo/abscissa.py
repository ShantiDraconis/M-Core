#!/usr/bin/env python3
"""Companheiro numérico da rodada 62: a abscissa de `Σ μ(n)n^{−s}` e `Σ (Λ(n) − 1)n^{−s}` (ATK/ZeroClasses/Abscissa.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`). **Nada aqui é certificado.**

* `tendsto_mu`: somas parciais de `Σ μ(n)n^{−s}` em `s = 0,75; 0,75 + 10i; 1,2 + 3i` contra `1/ζ(s)`;
* `tendsto_cL`: o mesmo para `Σ (Λ(n) − 1)n^{−s}` contra `−ζ′/ζ(s) − ζ(s)`;
* o lado "não converge": em `s = 0,4` as somas parciais de `Σ μ(n)n^{−s}` oscilam com amplitude crescente
  (a abscissa é `½`, teorema de Hardy + rodada 62).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def tabelas(N):
    mu = [1] * (N + 1)
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    lam = [0.0] * (N + 1)
    for p in range(2, N + 1):
        if eh[p]:
            for k in range(2 * p, N + 1, p):
                eh[k] = 0
            for k in range(p, N + 1, p):
                mu[k] = -mu[k]
            for k in range(p * p, N + 1, p * p):
                mu[k] = 0
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    return mu, lam


def main(saida=None):
    mu, lam = tabelas(NMAX)
    marcas = {10 ** k for k in range(3, 7)}
    res = {"mu": [], "cL": [], "mu_0_4": []}
    h = 1e-6
    for s in (complex(0.75, 0), complex(0.75, 10), complex(1.2, 3)):
        z = zc.zeta(s)
        dz = (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h)
        alvo_mu = 1 / z
        alvo_cl = -dz / z - z
        Sm = Sc = 0j
        for n in range(1, NMAX + 1):
            t = n ** (-s)
            if mu[n]:
                Sm += mu[n] * t
            Sc += (lam[n] - 1) * t
            if n in marcas:
                res["mu"].append({"s": str(s), "N": n, "dif": abs(Sm - alvo_mu)})
                res["cL"].append({"s": str(s), "N": n, "dif": abs(Sc - alvo_cl)})
    S = 0.0
    mx = 0.0
    for n in range(1, NMAX + 1):
        if mu[n]:
            S += mu[n] * n ** (-0.4)
        mx = max(mx, abs(S))
        if n in marcas:
            res["mu_0_4"].append({"N": n, "max_abs": mx})
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "abscissa.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
