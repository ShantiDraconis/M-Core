#!/usr/bin/env python3
"""Companheiro numérico da rodada 88: `Ω±(√x)` e zeros simples (ATK/ZeroClasses/OmegaRaiz.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`; crivo de `unilateral.py`).
**Nada aqui é certificado.**

* `psi_omega_mais_raiz`/`_menos_raiz` com `ρ₀ = ½ + 14,1347…i` (o primeiro zero): `c = 1/(8|ρ₀|)`; conta os
  `N ≤ 10⁶` com `ψ(N) − N > c√(N + 1)` e com `ψ(N) − N < −c√(N + 1)`;
* `mertens_omega_mais_raiz`/`_menos_raiz` (constante não explícita): conta `|M(N)| > 0,1√(N + 1)` de cada lado;
* `simples_of_mertens_le`: `|ζ′(ρ)|` por diferença central nos 3 primeiros zeros (a simplicidade numérica é
  conhecida até alturas enormes; aqui só a sanidade).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unilateral  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
ZEROS = (14.134725141734693, 21.022039638771555, 25.010857580145688)


def main(saida=None, n=10 ** 6):
    mu, lam = unilateral.crivo(n)
    rho0 = complex(0.5, ZEROS[0])
    c = 1 / (8 * abs(rho0))
    M = 0
    psi = 0.0
    acima = abaixo = macima = mabaixo = 0
    for k in range(1, n + 1):
        M += mu[k]
        psi += lam[k]
        r = math.sqrt(k + 1)
        d = psi - k
        if d > c * r:
            acima += 1
        if d < -c * r:
            abaixo += 1
        if M > 0.1 * r:
            macima += 1
        if M < -0.1 * r:
            mabaixo += 1
    h = 1e-5
    derivs = []
    for g in ZEROS:
        rho = complex(0.5, g)
        dz = (zc.zeta(rho + h) - zc.zeta(rho - h)) / (2 * h)
        derivs.append({"gamma": g, "abs_zeta": abs(zc.zeta(rho)), "abs_deriv": abs(dz)})
    out = {"N": n, "c_psi": c, "psi_acima": acima, "psi_abaixo": abaixo, "M_acima_0_1": macima,
           "M_abaixo_0_1": mabaixo, "zeros": derivs,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/OmegaRaiz.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "omega_raiz.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
