#!/usr/bin/env python3
"""Companheiro numérico da rodada 43: `J(ε) → 0` sob RH (ATK/ZeroClasses/JSobRH.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `tendsto_J`: `J(ε) = ∫ |1 − ζ(½ + iτ)/ζ(½ + ε + iτ)|²/|½ + iτ|² dτ`, truncada em `|τ| ≤ T` (trapézio; o
  integrando é par), para `ε` de `0,4` a `0,01`;
* `razao_Gamma`: `|Γ(¼ + h + iy)| / (|Γ(¼ + iy)|·(1 + |y|)^{1/4})` numa grade, contra a constante `e^{17/2}` da
  prova em `|y| ≥ 2`;
* `razao_zeta`: `|ζ(½ + iτ)| / (|ζ(½ + ε + iτ)|·(1 + |τ|)^{1/4})` numa grade;
* `xi_meio_le`: `|ξ(½ + iτ)| ≤ |ξ(½ + ε + iτ)|` numa grade (é o que RH dá; aqui só se observa).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def integrando(tau, eps):
    s = complex(0.5, tau)
    r = zc.zeta(s) / zc.zeta(s + eps)
    return abs(1 - r) ** 2 / abs(s) ** 2


def J(eps, T=120.0, h=0.05):
    n = int(T / h)
    tot = 0.5 * (integrando(0.0, eps) + integrando(T, eps))
    for k in range(1, n):
        tot += integrando(k * h, eps)
    return 2 * tot * h


def xi_abs(s):
    return abs(s * (s - 1) / 2 * cmath.exp(-s / 2 * math.log(math.pi)) * en.gamma(s / 2) * zc.zeta(s))


def main(saida=None):
    Js = {}
    for eps in (0.4, 0.2, 0.1, 0.05, 0.02, 0.01):
        Js[str(eps)] = J(eps)
    pior_gamma = 0.0
    for h in (0.0, 0.05, 0.125, 0.25):
        for k in range(0, 401):
            y = k * 0.5
            num = abs(en.gamma(complex(0.25 + h, y)))
            den = abs(en.gamma(complex(0.25, y))) * (1 + y) ** 0.25
            pior_gamma = max(pior_gamma, num / den)
    pior_zeta = {}
    for eps in (0.05, 0.25, 0.45):
        m = 0.0
        for k in range(0, 2001):
            tau = k * 0.1
            s = complex(0.5, tau)
            m = max(m, abs(zc.zeta(s)) / (abs(zc.zeta(s + eps)) * (1 + tau) ** 0.25))
        pior_zeta[str(eps)] = m
    mono_ok = True
    for eps in (0.01, 0.1, 0.4):
        for k in range(0, 301):
            tau = 0.3 + k * 0.5
            s = complex(0.5, tau)
            if xi_abs(s) > xi_abs(s + eps) * (1 + 1e-9):
                mono_ok = False
    res = {"J_truncada_T120": Js, "razao_Gamma_max": pior_gamma, "exp_17_2": math.exp(8.5),
           "razao_zeta_max": pior_zeta, "monotonia_xi_na_grade": mono_ok}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "jsobrh.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
