#!/usr/bin/env python3
"""Companheiro numérico da rodada 49: os momentos de Hardy (ATK/ZeroClasses/HardyMomentos.lean).

Só biblioteca padrão (ξ por Lanczos + Euler–Maclaurin, de `encontro.py`). **Nada aqui é certificado.**

* `integral_Fx_cos` (inversão de Fourier): `∫₀^∞ Fx(t) cos(xt) dt = (π/2) Hr(x)`, `Fx(t) = Ξ(t)/(t² + 1/4)`;
* `momento`: `∫₀^∞ Fx(t) t^{2n} cosh(αt) dt = (−1)^n (π/2)(2·4^{−n} cos(α/2) − Re Θ^{(2n)}(iα))` para `n = 0, 1`,
  com `Θ(u) = e^{u/2}θ(e^{2u})` e `Θ''` pela série;
* `momento_tendsto` (só o lado direito): `(−1)^n (π/2)(2·4^{−n}cos(α/2) − Re Θ^{(2n)}(iα)) → (−1)^n π 4^{−n} cos(π/8)`
  quando `α → π/4`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
H = 0.01
TMAX = 60.0


def Xi(t):
    return en.xi(complex(0.5, t)).real


def psi(x):
    s, n = 0.0, 1
    while True:
        e = math.exp(-math.pi * n * n * x)
        s += e
        if e < 1e-300 or (n > 2 and e < 1e-20 * s):
            return s
        n += 1


def Hr(u):
    return math.exp(-u / 2) - 2 * math.exp(u / 2) * psi(math.exp(2 * u))


def Theta_k(u, k):
    """Θ(u) (k = 0) e Θ''(u) (k = 2) pela série Σ_{m∈ℤ} exp(u/2 − πm²e^{2u})."""
    E = cmath.exp(2 * u)
    tot = 0
    for m in range(-30, 31):
        a = math.pi * m * m * E
        phi = u / 2 - a
        term = cmath.exp(phi)
        if k == 2:
            term *= (0.5 - 2 * a) ** 2 - 4 * a
        tot += term
    return tot


def simpson(ys, h):
    n = len(ys) - 1
    s = ys[0] + ys[-1] + 4 * sum(ys[1:n:2]) + 2 * sum(ys[2:n:2])
    return s * h / 3


def main(saida=None):
    N = int(round(TMAX / H))
    ts = [k * H for k in range(N + 1)]
    F = [Xi(t) / (t * t + 0.25) for t in ts]
    inv = []
    for x in (0.0, 0.5, 1.0, 2.0):
        lhs = simpson([f * math.cos(x * t) for f, t in zip(F, ts)], H)
        inv.append({"x": x, "integral": lhs, "pi2_Hr": math.pi / 2 * Hr(x)})
    mom = []
    for n in (0, 1):
        for a in (0.2, 0.3, 0.4):
            lhs = simpson([f * t ** (2 * n) * math.cosh(a * t) for f, t in zip(F, ts)], H)
            rhs = (-1) ** n * math.pi / 2 * (2 * 0.25 ** n * math.cos(a / 2) - Theta_k(1j * a, 2 * n).real)
            mom.append({"n": n, "alpha": a, "integral": lhs, "formula": rhs})
    cusp = []
    for n in (0, 1):
        lim = (-1) ** n * math.pi * 0.25 ** n * math.cos(math.pi / 8)
        vals = []
        for a in (0.5, 0.65, 0.72, 0.76, 0.775, 0.78):
            vals.append((-1) ** n * math.pi / 2 * (2 * 0.25 ** n * math.cos(a / 2) - Theta_k(1j * a, 2 * n).real))
        cusp.append({"n": n, "alfas": [0.5, 0.65, 0.72, 0.76, 0.775, 0.78], "formula": vals, "limite": lim})
    res = {"inversao": inv, "momentos": mom, "cuspide": cusp}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "hardy_momentos.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
