#!/usr/bin/env python3
"""Companheiro numérico da rodada 54: o teorema dos números primos (ATK/ZeroClasses/TNP.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `psi_tnp`, `tendsto_psi_div`: `ψ(x)/x` e `|ψ(x) − x|/x` até `x = 10⁶`;
* `tendsto_theta_div`: `θ(x)/x`;
* `tendsto_primeCounting`: `π(x) log x / x` — converge devagar (`1,16` em `10³`, `1,08` em `10⁶`), como deve:
  `π(x) = x/log x + x/log²x + …`;
* `incremento`: `h ψ(y) ≤ ψ₁(y + h) − ψ₁(y) ≤ h ψ(y + h)` com `ψ₁(y) = Σ_{n ≤ y} Λ(n)(y − n)`, em alguns pontos.
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def crivo(N):
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    for p in range(2, int(N ** 0.5) + 1):
        if eh[p]:
            eh[p * p::p] = bytearray(len(range(p * p, N + 1, p)))
    return eh


def main(saida=None):
    eh = crivo(NMAX)
    lam = [0.0] * (NMAX + 1)
    for p in range(2, NMAX + 1):
        if eh[p]:
            lp = math.log(p)
            q = p
            while q <= NMAX:
                lam[q] = lp
                q *= p
    psi = [0.0] * (NMAX + 1)
    theta = [0.0] * (NMAX + 1)
    pi = [0] * (NMAX + 1)
    for n in range(1, NMAX + 1):
        psi[n] = psi[n - 1] + lam[n]
        theta[n] = theta[n - 1] + (math.log(n) if eh[n] else 0.0)
        pi[n] = pi[n - 1] + (1 if eh[n] else 0)
    tab = []
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
        tab.append({"x": x, "psi_x": psi[x] / x, "erro_rel": abs(psi[x] - x) / x, "theta_x": theta[x] / x,
                    "pi": pi[x], "pi_log_x": pi[x] * math.log(x) / x})

    def psi1(y):
        return sum(lam[n] * (y - n) for n in range(1, int(y) + 1))

    inc = []
    for y, h in ((100.0, 7.5), (1000.0, 30.0), (5000.0, 100.0)):
        d = psi1(y + h) - psi1(y)
        inc.append({"y": y, "h": h, "baixo": h * psi[int(y)], "meio": d, "alto": h * psi[int(y + h)]})
    res = {"tabela": tab, "incremento": inc}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "tnp.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
