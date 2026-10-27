#!/usr/bin/env python3
"""Companheiro numérico da rodada 47: a teta na cúspide (ATK/ZeroClasses/HardyCuspide.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `norm_th_cusp`: `|θ(i + η)|` (série `Σ (−1)^n e^{−πn²η}`) contra `K₀ |η|^{−1/2} e^{−(π/4) Re(1/η)}`, com
  `K₀ = Σ_{n∈ℤ} e^{−π(n² − |n|)}`, em pontos com `Re(1/η) ≥ 1`;
* `iteratedDeriv_Th_tendsto` (só a tendência): `|Θ(iα)|` e `|Θ′(iα)|` (diferença finita), `α = π/4 − 2r`, caem
  quando `r → 0` (em `r ≤ 1/250` os valores ficam abaixo da precisão da máquina);
* `norm_Th_cusp`: a cota `2K₀ (2r/π)^{−1/2} e^{−1/(288 r)}` para `r ≤ 1/250`, que vai a `0`.
"""
import cmath
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def theta(y, N=None):
    """θ(y) = Σ_{n∈ℤ} e^{−πn²y}, Re y > 0."""
    if N is None:
        N = int(math.sqrt(40 / (math.pi * y.real))) + 3
    return 1 + 2 * sum(cmath.exp(-math.pi * n * n * y) for n in range(1, N + 1))


def Th(u):
    return cmath.exp(u / 2) * theta(cmath.exp(2 * u))


K0 = sum(math.exp(-math.pi * (n * n - abs(n))) for n in range(-40, 41))


def main(saida=None):
    cusp = []
    for eta in (complex(0.2, 0.3), complex(0.1, -0.2), complex(0.05, 0.05), complex(0.06, 0.02), complex(0.03, 0.1)):
        R = (1 / eta).real
        if R < 1:
            continue
        val = abs(theta(1j + eta))
        cota = K0 * abs(eta) ** -0.5 * math.exp(-math.pi / 4 * R)
        cusp.append({"eta": [eta.real, eta.imag], "Re_inv": R, "theta": val, "cota": cota})
    Thc = []
    for r in (0.08, 0.06, 0.04, 0.03, 0.02):
        alpha = math.pi / 4 - 2 * r
        u = 1j * alpha
        h = r / 20
        val = abs(Th(u))
        deriv = abs((Th(u + h) - Th(u - h)) / (2 * h))
        Thc.append({"r": r, "Th": val, "dTh": deriv})
    cotas = {str(r): 2 * K0 * (2 * r / math.pi) ** -0.5 * math.exp(-1 / (288 * r)) for r in (0.004, 0.002, 0.001, 0.0005)}
    res = {"K0": K0, "cuspide": cusp, "Th_iα": Thc, "cota_r_le_1_250": cotas}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "hardy_cuspide.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
