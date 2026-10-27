#!/usr/bin/env python3
"""Companheiro numérico da rodada 73: a forma espectral de `D_N(σ)` e o molificador de Riesz
(ATK/ZeroClasses/BDEspectral.lean).

Só biblioteca padrão (`ζ` de `zeroclasses.py`). **Nada aqui é certificado.**

* `hasMellin_wR`: `∫_0^1 t^{z−1}(1 − t)² dt` (Simpson) contra `W(z) = 2/(z(z + 1)(z + 2))`;
* `wR_inv`: `(1/2π) ∫ u^{−(c+iy)} W(c + iy) dy` contra `w(u) = (1 − u)²₊` em `u = 0,3; 1,7`;
* `LSeries_aN_int`: `A_N(s) = Σ_{k<N} μ(k)(1 − k/N)² k^{−s}` contra `(1/2π) ∫ W(c + iy) N^{c+iy}/ζ(s + c + iy) dy`;
* `DNσ_le_molif`: `(1/2π) ∫ |1 − ζ(s)A_N(s)|²/|s|² dτ` em `σ = 0,8` para `N = 10, 40, 160` (decai com `N`).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def W(z):
    return 2 / (z * (z + 1) * (z + 2))


def w(u):
    return max(1 - u, 0) ** 2


def mobius(n):
    m, r, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            r = -r
        p += 1
    return -r if m > 1 else r


def simpson(f, a, b, n):
    h = (b - a) / n
    tot = f(a) + f(b)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(a + i * h)
    return tot * h / 3


def A(N, s):
    return sum(mobius(k) * w(k / N) * k ** (-s) for k in range(1, N))


def main(saida=None):
    z = complex(0.7, 3)
    # t = v^10 tira a singularidade em 0: ∫_0^1 10 v^{10z−1} (1 − v^10)² dv
    mel = simpson(lambda v: 10 * v ** (10 * z - 1) * (1 - v ** 10) ** 2 if v > 0 else 0, 0, 1, 20000)
    inv = []
    for u in (0.3, 1.7):
        val = simpson(lambda y: (u ** (-complex(1, y)) * W(complex(1, y))), -400, 400, 40000) / (2 * math.pi)
        inv.append({"u": u, "inversa": val.real, "w": w(u)})
    N, s, c = 10, complex(1.5, 2), 0.5
    rep = simpson(lambda y: W(complex(c, y)) * N ** complex(c, y) / zc.zeta(s + complex(c, y)), -300, 300, 30000)
    rep /= 2 * math.pi
    dn = []
    sigma = 0.8
    for N in (10, 40, 160):
        f = lambda t: abs(1 - zc.zeta(complex(sigma, t)) * A(N, complex(sigma, t))) ** 2 / abs(complex(sigma, t)) ** 2  # noqa: E731
        dn.append({"N": N, "cota": 2 * simpson(f, 0, 200, 4000) / (2 * math.pi)})
    out = {"mellin_w": [mel.real, mel.imag], "W": [W(z).real, W(z).imag], "inversao": inv,
           "A_N": [A(10, s).real, A(10, s).imag], "representacao": [rep.real, rep.imag],
           "cota_DN_sigma_0_8": dn,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDEspectral.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_espectral.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
