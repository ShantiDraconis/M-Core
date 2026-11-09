#!/usr/bin/env python3
"""Companheiro numérico da rodada 109: o piso ponderado exato `κ(σ) = 2(σ − Θ)` (ATK/ZeroClasses/BDPisoExato.lean).

Só biblioteca padrão (`decimal` com 60 dígitos). **Nada aqui é certificado.**

* `hasMellin_psi`: `∫_1^∞ t^{s−1} ψ(t) dt = K(s) = 1/((2 − s)(3 − s)(4 − s))`, `ψ(t) = (t − 1)²/(2t⁴)` (t ≥ 1),
  por quadratura em `s = 0,5; 1; 1,5`;
* `Gl_mobius`: a Mertens suavizada `G(x) = Σ_n μ(n) ψ(n/x) = Σ_{n > x} μ(n) φ(x/n)`, `φ(y) = y²(1 − y)²/2`.
  Como `φ` é polinomial em `y ≤ 1`, `G(x) = (x²/2)T₂ − x³T₃ + (x⁴/2)T₄` com as caudas exatas
  `T_k = 1/ζ(k) − Σ_{n ≤ x} μ(n)/n^k`; confere com a soma direta truncada;
* a escala de `G` até `X = 10⁵`: `max |G(N)|/√N` (sob RH, `G(x) = Σ_ρ x^ρ K(ρ)/ζ′(ρ) + O(x^{−2})`, então
  `|G(x)| ≪ √x`; `Gl_omega` diz que `G` não é `O(x^θ)` para `θ < Θ`). Isso é consistência, não medida de `Θ`.
"""
import json
import math
import os
from decimal import Decimal, getcontext

AQUI = os.path.dirname(os.path.abspath(__file__))
getcontext().prec = 60
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494")
APERY = Decimal("1.20205690315959428539973816151144999076498629234049888179227")
INV_Z2 = 6 / PI ** 2
INV_Z3 = 1 / APERY
INV_Z4 = 90 / PI ** 4


def mobius(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    primo = [True] * (n + 1)
    for p in range(2, n + 1):
        if primo[p]:
            for m in range(2 * p, n + 1, p):
                primo[m] = False
            for m in range(p, n + 1, p):
                mu[m] = -mu[m]
            pp = p * p
            for m in range(pp, n + 1, pp):
                mu[m] = 0
    return mu


def psi(t):
    return 0.0 if t <= 1 else (t - 1) ** 2 / (2 * t ** 4)


def K(s):
    return 1 / ((2 - s) * (3 - s) * (4 - s))


def mellin_psi(s, n=200000):
    # t = 1/u, u = v²: ∫_1^∞ t^{s−1} ψ(t) dt = ∫_0^1 u^{1−s}(1 − u)²/2 du = ∫_0^1 v^{3−2s}(1 − v²)² dv (ponto médio)
    h = 1 / n
    return h * sum(((j + 0.5) * h) ** (3 - 2 * s) * (1 - ((j + 0.5) * h) ** 2) ** 2 for j in range(n))


def G_exato(X, mu):
    """G(N) para N = 1..X pelas caudas exatas (Decimal)."""
    s2 = s3 = s4 = Decimal(0)
    out = [Decimal(0)] * (X + 1)
    for n in range(1, X + 1):
        if mu[n]:
            d = Decimal(n)
            s2 += mu[n] / d ** 2
            s3 += mu[n] / d ** 3
            s4 += mu[n] / d ** 4
        x = Decimal(n)
        out[n] = x ** 2 / 2 * (INV_Z2 - s2) - x ** 3 * (INV_Z3 - s3) + x ** 4 / 2 * (INV_Z4 - s4)
    return out


def main(saida=None, X=100000, M=400000):
    mu = mobius(max(X, M))
    mel = [{"s": s, "quad": mellin_psi(s), "K": K(s)} for s in (0.5, 1.0, 1.5)]
    G = G_exato(X, mu)
    direta = []
    for x in (2, 7, 10, 25):
        soma = sum(mu[n] * psi(n / x) for n in range(1, M + 1))
        direta.append({"x": x, "direta": soma, "exata": float(G[x]), "erro_max_cauda": x * x / (2 * M)})
    razoes = [abs(float(G[n])) / math.sqrt(n) for n in range(1, X + 1)]
    rmax = max(razoes)
    nmax = razoes.index(rmax) + 1
    blocos = []
    for a in range(1, 6):
        lo, hi = 10 ** (a - 1), 10 ** a
        r = max(razoes[lo - 1:hi])
        blocos.append({"faixa": [lo, hi], "max_G_sobre_raiz": r})
    trocas = sum(1 for n in range(2, X + 1) if (G[n] > 0) != (G[n - 1] > 0))
    out = {"mellin_psi": mel, "serie_direta": direta, "X": X,
           "max_G_sobre_raiz": rmax, "N_do_max": nmax, "G_no_max": float(G[nmax]), "blocos": blocos,
           "trocas_de_sinal": trocas,
           "G_amostra": {str(n): float(G[n]) for n in (10, 100, 1000, 10000, 100000) if n <= X},
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDPisoExato.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_piso_exato.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
