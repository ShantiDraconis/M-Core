#!/usr/bin/env python3
"""Coeficientes de Li λₙ a partir de Θ (companheiro de ATK/LiCriterio.lean).

λₙ = (1/(n−1)!) dⁿ/dsⁿ [s^{n−1} log ξ(s)] em s = 1  =  n Σ_{k=1}^{n} C(n−1, k−1) c_k,
com log ξ(1+u) = Σ c_k u^k e ξ(1+u) = Θ(¼ + u + u²) = Σ aₘ (¼ + u + u²)^m (aₘ de jensen.py).

Controle: λ₁ = 1 + γ/2 − ½ log(4π) = 0,0230957089661210338…  HR ⟺ λₙ ≥ 0 ∀n (Li 1997); aqui só
os primeiros n, numericamente (não certificado).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jensen  # noqa: E402

D = jensen.D


def serie_xi_em_1(a, grau):
    """Coeficientes de ξ(1+u) até u^grau."""
    base = [D(1) / 4, D(1), D(1)] + [D(0)] * (grau - 2)
    pot = [D(1)] + [D(0)] * grau
    out = [D(0)] * (grau + 1)
    for am in a:
        for i in range(grau + 1):
            out[i] += am * pot[i]
        nova = [D(0)] * (grau + 1)
        for i, x in enumerate(pot):
            if x == 0:
                continue
            for j in range(min(3, grau + 1 - i)):
                nova[i + j] += x * base[j]
        pot = nova
    return out


def log_serie(f, grau):
    """c_k de log f(u) (k ≥ 1), por g' = f'/f."""
    c = [D(0)] * (grau + 1)
    for k in range(1, grau + 1):
        s = k * f[k]
        for j in range(1, k):
            s -= j * c[j] * f[k - j]
        c[k] = s / (k * f[0])
    return c


def lambdas(nmax=20, N=60):
    _, a, _ = jensen.coeficientes(N, D(1) / 64)
    f = serie_xi_em_1(a, nmax)
    c = log_serie(f, nmax)
    return [n * sum(math.comb(n - 1, k - 1) * c[k] for k in range(1, n + 1)) for n in range(1, nmax + 1)]


GAMMA = D("0.57721566490153286060651209008240243104215933593992")


def lambda1_exato():
    return 1 + GAMMA / 2 - (4 * jensen.PI).ln() / 2


if __name__ == "__main__":
    lam = lambdas()
    res = {"lambda": [str(x)[:22] for x in lam], "lambda1_formula": str(lambda1_exato())[:22],
           "todos_positivos": all(x > 0 for x in lam)}
    if len(sys.argv) > 1:
        json.dump(res, open(sys.argv[1], "w"), indent=1)
    print(json.dumps(res, indent=1))
