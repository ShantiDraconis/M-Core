#!/usr/bin/env python3
"""Companheiro numérico da rodada 110: a Mertens suavizada de um produto (ATK/ZeroClasses/BDMonoide.lean).

Só biblioteca padrão (`decimal`, 60 dígitos). **Nada aqui é certificado.**

`F = ζ · L(·, χ₋₄) = ζ_{ℚ(i)}`, com `1/F = Σ μ_F(n) n^{−s}` e `μ_F = μ ⋆ (χ₋₄ μ)`. A Mertens suavizada do produto é
`G_F(x) = Σ_n μ_F(n) ψ(n/x) = Σ_{n > x} μ_F(n) φ(x/n)`, com `φ(y) = y²(1 − y)²/2`; como `φ` é polinomial,
`G_F(x) = (x²/2)T₂ − x³T₃ + (x⁴/2)T₄` com caudas exatas `T_k = 1/F(k) − Σ_{n ≤ x} μ_F(n)/n^k`.
Os valores `ζ(k)` e `β(k) = L(k, χ₋₄)` saem da aceleração de Cohen–Villegas–Zagier para séries alternadas,
conferida contra `ζ(2) = π²/6`, `ζ(4) = π⁴/90` e `β(3) = π³/32`.

Consistência (não medida, barreira B2): sob RH ∧ GRH(χ₋₄), `|G_F(x)| ≪ √x`; o teorema `juncao` diz que uma taxa de
`D_N^F` certifica as duas regiões sem zeros ao mesmo tempo.
"""
import json
import math
import os
from decimal import Decimal, getcontext

AQUI = os.path.dirname(os.path.abspath(__file__))
getcontext().prec = 60
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494")


def cvz(a, n=90):
    """Σ_{k≥0} (−1)^k a(k) pela aceleração de Cohen–Villegas–Zagier (erro ~ 5,8^{−n})."""
    d = (3 + Decimal(8).sqrt()) ** n
    d = (d + 1 / d) / 2
    b, c, s = Decimal(-1), -d, Decimal(0)
    for k in range(n):
        c = b - c
        s += c * a(k)
        b = b * (k + n) * (k - n) / ((Decimal(k) + Decimal("0.5")) * (k + 1))
    return s / d


def zeta(k):
    eta = cvz(lambda j: 1 / Decimal(j + 1) ** k)
    return eta / (1 - Decimal(2) ** (1 - k))


def beta(k):
    return cvz(lambda j: 1 / Decimal(2 * j + 1) ** k)


def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


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
            for m in range(p * p, n + 1, p * p):
                mu[m] = 0
    return mu


def mu_F(n, mu):
    """μ_F = μ ⋆ (χ₋₄ μ)."""
    out = [0] * (n + 1)
    for d in range(1, n + 1):
        if mu[d] == 0:
            continue
        for m in range(d, n + 1, d):
            e = m // d
            out[m] += mu[d] * chi4(e) * mu[e]
    return out


def psi(t):
    return 0.0 if t <= 1 else (t - 1) ** 2 / (2 * t ** 4)


def main(saida=None, X=100000, M=200000):
    z = {k: zeta(k) for k in (2, 3, 4)}
    b = {k: beta(k) for k in (2, 3, 4)}
    conf = {"zeta2_menos_pi2_6": float(z[2] - PI ** 2 / 6), "zeta4_menos_pi4_90": float(z[4] - PI ** 4 / 90),
            "beta3_menos_pi3_32": float(b[3] - PI ** 3 / 32)}
    invF = {k: 1 / (z[k] * b[k]) for k in (2, 3, 4)}
    mu = mobius(max(X, M))
    mf = mu_F(max(X, M), mu)
    s = {k: Decimal(0) for k in (2, 3, 4)}
    G = [Decimal(0)] * (X + 1)
    for n in range(1, X + 1):
        if mf[n]:
            dn = Decimal(n)
            for k in (2, 3, 4):
                s[k] += mf[n] / dn ** k
        x = Decimal(n)
        G[n] = x ** 2 / 2 * (invF[2] - s[2]) - x ** 3 * (invF[3] - s[3]) + x ** 4 / 2 * (invF[4] - s[4])
    direta = []
    for x in (3, 10, 25):
        soma = sum(mf[n] * psi(n / x) for n in range(1, M + 1))
        direta.append({"x": x, "direta": soma, "exata": float(G[x]), "cota_cauda": 2 * x * x * math.log(M) / M})  # |μ_F(n)| ≤ d(n): cauda ≤ (x²/2) Σ_{n>M} d(n)/n²
    raz = [abs(float(G[n])) / math.sqrt(n) for n in range(1, X + 1)]
    blocos = [{"faixa": [10 ** (a - 1), 10 ** a], "max_G_sobre_raiz": max(raz[10 ** (a - 1) - 1:10 ** a])}
              for a in range(1, 6) if 10 ** a <= X]
    trocas = sum(1 for n in range(2, X + 1) if (G[n] > 0) != (G[n - 1] > 0))
    out = {"conferencia_constantes": conf, "catalan": float(b[2]), "inv_F": {k: float(v) for k, v in invF.items()},
           "mu_F_ate_12": mf[1:13], "serie_direta": direta, "X": X, "blocos": blocos, "trocas_de_sinal": trocas,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDMonoide.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_monoide.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
