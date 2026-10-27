#!/usr/bin/env python3
"""Companheiro numérico da rodada 89: a fórmula explícita gaussiana (ATK/ZeroClasses/ExplicitaGauss.lean).

Só biblioteca padrão (zeros de `canonico.py`, `ζ′/ζ` à esquerda de `explicita_limite.py`). **Nada aqui é
certificado.**

* `integral_linha`: `∫ exp((a + iy)Y + τ(a + iy)²) dy = 2π k_τ(Y)` por quadratura;
* `lado_aritmetico`: `Φ_τ(Y) = e^{−Y/2 + τ/4} erfc((τ − Y)/(2√τ))/2` (forma fechada) e `A_τ(u) = Σ Λ(n) n^{−1/2} Φ_τ(u − log n)`;
* `formula_gauss`: `A_τ(u)` contra `W(1) + W(−2)/2 − W(0) log 2π − Σ_ρ W(ρ)/ρ + (1/2π)∫ F_W(−5/2 + iy) dy`,
  `W(s) = e^{(s−½)u + τ(s−½)²}`, com os zeros `0 < γ ≤ 80` (de `canonico.py`; `e^{−τγ²}` corta o resto) e
  `τ = 0,02`, `u ∈ {2; 3; 4}`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import explicita_limite as el  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def W(s, u, tau):
    z = s - 0.5
    return cmath.exp(z * u + tau * z * z)


def kg(tau, v):
    return math.exp(-v * v / (4 * tau)) / math.sqrt(4 * math.pi * tau)


def phi(tau, Y):
    return math.exp(-Y / 2 + tau / 4) * 0.5 * math.erfc((tau - Y) / (2 * math.sqrt(tau)))


def lam(n):
    m, p = n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
        p += 1
    return math.log(m) if m > 1 else 0.0


def A(tau, u):
    nmax = int(math.exp(u + 12 * math.sqrt(tau) + 2)) + 2
    return sum(lam(n) * n ** -0.5 * phi(tau, u - math.log(n)) for n in range(2, nmax + 1))


def esq(tau, u, Y=60.0, h=0.01):
    tot = 0j
    y = -Y
    while y <= Y:
        s = complex(-2.5, y)
        tot += W(s, u, tau) * (-el.dlog_zeta(s)) / s * h
        y += h
    return tot / (2 * math.pi)


def linha(tau, a, Y, L=40.0, h=0.002):
    tot = 0j
    y = -L
    while y <= L:
        z = complex(a, y)
        tot += cmath.exp(z * Y + tau * z * z) * h
        y += h
    return tot


def main(saida=None):
    tau = 0.02
    g = ca.zeros(T=80.0)
    lin = [{"a": a, "Y": Y, "quad": abs(linha(tau, a, Y)), "2pi_k": 2 * math.pi * kg(tau, Y)}
           for a, Y in ((1.5, 0.1), (1.5, -0.2), (-3.0, 0.3))]
    res = []
    for u in (2.0, 3.0, 4.0):
        zs = sum(2 * (W(complex(0.5, t), u, tau) / complex(0.5, t)).real for t in g)
        e = esq(tau, u)
        rhs = (W(1, u, tau) + W(-2, u, tau) / 2 - W(0, u, tau) * math.log(2 * math.pi) - zs + e).real
        lhs = A(tau, u)
        res.append({"u": u, "A": lhs, "direita": rhs, "erro": abs(lhs - rhs), "esq": abs(e)})
    out = {"tau": tau, "zeros": len(g), "linha": lin, "formula": res,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaGauss.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_gauss.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
