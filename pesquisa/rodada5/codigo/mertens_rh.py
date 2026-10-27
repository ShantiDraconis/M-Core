#!/usr/bin/env python3
"""Companheiro numérico da rodada 51: o critério de Littlewood `RH ⟺ M(x) = O(x^{1/2+ε})`
(ATK/ZeroClasses/MertensRH.lean).

Só biblioteca padrão. **Nada aqui é certificado** — e nenhum cálculo finito decide RH.

* `M(N) = Σ_{n ≤ N} μ(n)` por crivo até `N = 2·10⁵`: o máximo de `|M(N)|/√N` em faixas `[a, b]` (a conjectura de Mertens
  `|M(N)| < √N` vale aqui, mas é falsa em geral — Odlyzko–te Riele, 1985 — e não é o que o critério pede);
* `G_eq_LSeries`: a série por partes `G(2) = Σ_{n≥0} M(n + 1)((n + 1)^{−2} − (n + 2)^{−2})` contra `1/ζ(2) = 6/π²`;
* `abel` (identidade finita): `Σ_{n ≤ N} μ(n)n^{−s} = M(N)N^{−s} + Σ_{n < N} M(n)(n^{−s} − (n + 1)^{−s})` em
  `s = 0,75`, `N = 10⁴`.
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 200000


def moebius_ate(N):
    mu = [1] * (N + 1)
    mu[0] = 0
    eh_primo = [True] * (N + 1)
    for p in range(2, N + 1):
        if eh_primo[p]:
            for k in range(p, N + 1, p):
                if k > p:
                    eh_primo[k] = False
                mu[k] = -mu[k]
            pp = p * p
            for k in range(pp, N + 1, pp):
                mu[k] = 0
    return mu


def main(saida=None):
    mu = moebius_ate(NMAX)
    M = [0] * (NMAX + 1)
    for n in range(1, NMAX + 1):
        M[n] = M[n - 1] + mu[n]
    razoes = {}
    for a, b in ((2, 10 ** 3), (10 ** 3, 10 ** 4), (10 ** 4, 10 ** 5), (10 ** 5, NMAX)):
        r, arg = max((abs(M[n]) / math.sqrt(n), n) for n in range(a, b + 1))
        razoes[f"{a}-{b}"] = {"max_M_sobre_raiz": r, "em": arg}
    G2 = sum(M[n + 1] * ((n + 1) ** -2.0 - (n + 2) ** -2.0) for n in range(NMAX - 1))
    s, N = 0.75, 10 ** 4
    lhs = sum(mu[n] * n ** -s for n in range(1, N + 1))
    rhs = M[N] * N ** -s + sum(M[n] * (n ** -s - (n + 1) ** -s) for n in range(1, N))
    res = {"razoes": razoes, "M_amostra": {str(k): M[k] for k in (10, 100, 1000, 10000, 100000)},
           "G2": G2, "inv_zeta2": 6 / math.pi ** 2, "abel": {"lhs": lhs, "rhs": rhs}}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "mertens_rh.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
