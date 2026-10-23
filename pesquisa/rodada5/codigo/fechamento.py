#!/usr/bin/env python3
"""Companheiro numérico de ATK/XiPhi.lean e ATK/ToeplitzTN.lean (rodada 8).

Só biblioteca padrão (Decimal/Fraction). Nada aqui é certificado: os teoremas estão no kernel.

* Ξ(t) = 2∫₀^∞ Φ(u)cos(tu)du: a constante ½ + 2Σ h_c′(0) = ½ + Σ(1 − 4c)e^{−c} (c = πn²) é 0, e
  4Σ c e^{−c} = ψ(1) + ½ (equação funcional de θ derivada em x = 1).
* Toeplitz: todos os menores (até 4×4, seção 8×8) de T(coef p) são ≥ 0 para p com zeros reais ≤ 0;
  para 1 + x + x², D₃ = −1; em grau 2, o primeiro D_r < 0 quando a₁² < 4a₀a₂.
"""
import itertools
import json
import os
import sys
from decimal import Decimal as D, getcontext
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gram2  # noqa: E402

getcontext().prec = 60
PI = gram2.PI


def theta_somas(nmax=30):
    """ψ(1) = Σ e^{−c}, T = Σ c e^{−c}, constante ½ + Σ(1 − 4c)e^{−c}, c = πn²."""
    psi1 = sum((-PI * n * n).exp() for n in range(1, nmax))
    T = sum(PI * n * n * (-PI * n * n).exp() for n in range(1, nmax))
    const = D(1) / 2 + sum((1 - 4 * PI * n * n) * (-PI * n * n).exp() for n in range(1, nmax))
    return {"psi1": psi1, "T": T, "quatroT_menos": 4 * T - psi1 - D(1) / 2, "constante": const}


def toeplitz(a, N):
    return [[(a[i - j] if 0 <= i - j < len(a) else F(0)) for j in range(N)] for i in range(N)]


def det(M):
    M = [row[:] for row in M]
    n, s = len(M), F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            s = -s
        s *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return s


def menor_minimo(a, N=8, rmax=4):
    T = toeplitz([F(x) for x in a], N)
    m = None
    for r in range(1, rmax + 1):
        for rows in itertools.combinations(range(N), r):
            for cols in itertools.combinations(range(N), r):
                d = det([[T[i][j] for j in cols] for i in rows])
                m = d if m is None or d < m else m
    return m


def poli_de_raizes(c, raizes):
    p = [F(c)]
    for r in raizes:
        q = [F(0)] * (len(p) + 1)
        for k, x in enumerate(p):
            q[k] += F(r) * x
            q[k + 1] += x
        p = q
    return p


def Dtri(a0, a1, a2, r):
    d0, d1 = F(1), F(a1)
    if r == 0:
        return d0
    for _ in range(r - 1):
        d0, d1 = d1, F(a1) * d1 - F(a0) * F(a2) * d0
    return d1


def primeiro_negativo(a0, a1, a2, rmax=200):
    return next((r for r in range(rmax) if Dtri(a0, a1, a2, r) < 0), None)


def main(saida=None):
    th = theta_somas()
    res = {
        "theta": {k: format(v, ".18g") for k, v in th.items()},
        "menor_min_(1+x)^3": str(menor_minimo(poli_de_raizes(1, [1, 1, 1]))),
        "menor_min_(x+1)(x+2)(x+3)": str(menor_minimo(poli_de_raizes(1, [1, 2, 3]))),
        "menor_min_1+x+x2": str(menor_minimo([1, 1, 1])),
        "D3_1+x+x2": str(Dtri(1, 1, 1, 3)),
        "primeiro_D_neg": {f"a1={a1}": primeiro_negativo(1, F(a1), 1) for a1 in ("1", "1.9", "1.99")},
        "D_nao_neg_com_disc_0": all(Dtri(1, 2, 1, r) >= 0 for r in range(60)),
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
