#!/usr/bin/env python3
"""Companheiro numérico da rodada 48: a representação de Fourier de Ξ (ATK/ZeroClasses/HardyFourier.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `Hr_neg`: `Hr(−u) = Hr(u)` para `Hr(u) = e^{−u/2} − 2e^{u/2}ψ(e^{2u})`, `ψ(x) = Σ_{n≥1} e^{−πn²x}`;
* `abs_Hr_le`: `|Hr(u)| ≤ 5e^{−|u|/2}`;
* `integral_exp_cos`: `∫₀^∞ e^{−u/2} cos(tu) du = (1/2)/(t² + 1/4)` (Simpson);
* `Fx_eq`: `Ξ(t) = (t² + 1/4) ∫₀^∞ Hr(u) cos(tu) du`; em `t = 0` dá `ξ(1/2) = 0,4971207781…`, e o valor troca de
  sinal em volta do primeiro zero `t₁ = 14,134725…`;
* `abs_Xi_le`: os mesmos valores contra `24 CΓ (1 + |t|)⁴ e^{−π|t|/4}`.
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

XI_MEIO = 0.49712077818831410991  # ξ(1/2), valor conhecido
T1 = 14.134725141734693790  # primeiro zero


def psi(x):
    s = 0.0
    n = 1
    while True:
        e = math.exp(-math.pi * n * n * x)
        s += e
        if e < 1e-300 or (n > 2 and e < 1e-20 * s):
            return s
        n += 1


def Hr(u):
    return math.exp(-u / 2) - 2 * math.exp(u / 2) * psi(math.exp(2 * u))


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(a + k * h)
    return s * h / 3


def Fx(t, L=80.0, n=80000):
    return simpson(lambda u: Hr(u) * math.cos(t * u), 0.0, L, n)


CGAMMA = math.sqrt(2 * math.pi) * math.exp(1.5) * math.exp(3 * math.pi / 4)


def main(saida=None):
    par = [{"u": u, "Hr": Hr(u), "Hr_neg": Hr(-u)} for u in (0.1, 0.5, 1.0, 2.0, 3.0)]
    cota = [{"u": u, "abs_Hr": abs(Hr(u)), "cota": 5 * math.exp(-abs(u) / 2)} for u in (-3.0, -1.0, 0.0, 0.3, 1.0, 4.0, 10.0)]
    expcos = [{"t": t, "simpson": simpson(lambda u: math.exp(-u / 2) * math.cos(t * u), 0.0, 80.0, 80000),
               "exato": 0.5 / (t * t + 0.25)} for t in (0.0, 1.0, 5.0)]
    xi0 = 0.25 * Fx(0.0)
    zero = [{"t": t, "Xi": (t * t + 0.25) * Fx(t)} for t in (T1 - 0.05, T1 + 0.05)]
    dec = []
    for t in (0.0, 5.0, 10.0, 20.0, 30.0):
        X = (t * t + 0.25) * Fx(t)
        dec.append({"t": t, "Xi": X, "cota": 24 * CGAMMA * (1 + t) ** 4 * math.exp(-math.pi / 4 * t)})
    res = {"Hr_par": par, "Hr_cota": cota, "exp_cos": expcos, "Xi_meio": {"integral": xi0, "conhecido": XI_MEIO},
           "troca_t1": zero, "decaimento": dec}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "hardy_fourier.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
