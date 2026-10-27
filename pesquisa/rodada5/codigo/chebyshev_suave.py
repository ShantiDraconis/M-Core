#!/usr/bin/env python3
"""Companheiro numérico da rodada 53: `Σ_{n ≤ x} Λ(n)(1 − n/x) = x/2 + O(x log x · e^{−c√log x})`
(ATK/ZeroClasses/ChebyshevSuave.lean).

Só biblioteca padrão. **Nada aqui é certificado** (a constante `c` da prova não é explícita).

* `Ssm(x) = Σ_{n ≤ x} Λ(n)(1 − n/x)` por crivo até `x = 10⁶`, contra o resíduo `x/2` (`bordo_fx`): o erro relativo
  `|Ssm(x) − x/2|/x` cai com `x`;
* `phx_one`: `φ(1) = x·K(1) = x/2`, `K(s) = 1/(s(s + 1))`;
* `cauda` (o lema da cauda): `π − 2 arctan T ≤ 2/T` em alguns `T`.
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def mangoldt_ate(N):
    lam = [0.0] * (N + 1)
    eh = bytearray([1]) * (N + 1)
    for p in range(2, N + 1):
        if eh[p]:
            for k in range(p * p, N + 1, p):
                eh[k] = 0
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def Ssm(lam, x):
    return sum(lam[n] * (1 - n / x) for n in range(1, int(x) + 1))


def main(saida=None):
    lam = mangoldt_ate(NMAX)
    tab = []
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
        S = Ssm(lam, float(x))
        tab.append({"x": x, "Ssm": S, "x_2": x / 2, "erro_rel": abs(S - x / 2) / x})
    K1 = 1 / (1 * 2)
    cauda = [{"T": T, "pi_menos_2arctan": math.pi - 2 * math.atan(T), "2_T": 2 / T} for T in (1.0, 3.0, 10.0, 100.0)]
    res = {"tabela": tab, "K1": K1, "cauda": cauda}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "chebyshev_suave.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
