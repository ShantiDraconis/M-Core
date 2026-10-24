#!/usr/bin/env python3
"""Companheiro numérico de ATK/ArgPrincipio e ATK/ZeroClasses/Rouche (rodada 25).

Só biblioteca padrão. **Nada aqui é certificado.**

* princípio do argumento: (1/2πi)∮ ζ′/ζ por trapézios (N pontos) em vários círculos — conta 1 em torno do 1º zero,
  0 num disco fora da linha, 3 num disco grande com os zeros 14,13; 21,02; 25,01;
* Rouché: F(z) = ζ′(ρ₁)(z − ρ₁) e ζ no círculo |z − ρ₁| = 0,05: |ζ − F| < |F|;
* E1 afiado: |ζ(c)| + M r²/2 < r|ζ′(c)| perto do 1º zero (M amostrado);
* o exemplo quadrático: 69/1280 < 160/1280.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402


def dz(s, h=1e-6):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h)


def d2z(s, h=1e-4):
    return (zc.zeta(s + h) - 2 * zc.zeta(s) + zc.zeta(s - h)) / (h * h)


def conta(c, R, N=1200):
    """(1/2πi) ∮_{|z−c|=R} ζ′/ζ dz pela regra do trapézio (exponencialmente precisa para integrandos periódicos)."""
    tot = 0
    for k in range(N):
        th = 2 * math.pi * k / N
        z = c + R * cmath.exp(1j * th)
        dzdth = 1j * R * cmath.exp(1j * th)
        tot += dz(z) / zc.zeta(z) * dzdth
    return tot * (2 * math.pi / N) / (2j * math.pi)


def main(saida=None):
    res = {}
    rho = zc.zero_newton(complex(0.5, 14.13))
    casos = {"1o_zero_r0.3": (rho, 0.3), "fora_0.75+14.13i_r0.2": (complex(0.75, 14.13), 0.2),
             "grande_0.5+20i_r7": (complex(0.5, 20.0), 7.0), "fora_0.8+30i_r0.25": (complex(0.8, 30.0), 0.25)}
    res["contagem"] = {k: [round(v.real, 8), round(v.imag, 8)] for k, (c, R) in casos.items()
                       for v in [conta(c, R)]}
    # Rouché
    a = dz(rho)
    r = 0.05
    pior = max(abs(zc.zeta(rho + r * cmath.exp(2j * math.pi * k / 64)) - a * r * cmath.exp(2j * math.pi * k / 64))
               / abs(a * r) for k in range(64))
    res["rouche_razao_max_|ζ−F|/|F|"] = pior
    # E1 afiado perto do 1º zero
    c = rho + complex(1e-3, -5e-4)
    r = 5e-3
    M = 1.25 * max(abs(d2z(c + r * cmath.exp(2j * math.pi * k / 16))) for k in range(16))
    res["E1_afiado_1o_zero"] = {"|ζ(c)|+M r²/2": abs(zc.zeta(c)) + M * r * r / 2, "r|ζ′(c)|": r * abs(dz(c))}
    res["exemplo_quadratico"] = {"esq": 1 / 20 + 0.5 * (1 / 8) ** 2 / 2, "dir": 1 / 8, "69/1280": 69 / 1280}
    res["aviso"] = "trapézios e M amostrado; o kernel prova os teoremas (ArgPrincipio.lean, Rouche.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
