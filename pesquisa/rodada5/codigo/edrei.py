#!/usr/bin/env python3
"""Companheiro numérico de ATK/EdreiInteira.lean e ATK/XiTP.lean (rodada 10).

Só biblioteca padrão. Nada aqui é certificado e **nenhuma verificação finita de menores prova PF∞**: os
teoremas estão no kernel, e a positividade total dos coeficientes de Ξ é `OPEN_MATH` (equivalente a HR).

* Edrei para funções inteiras: B(w) = Σ wⁿ/(n!)² = I₀(2√w) tem zeros −j₀,ₖ²/4; os coeficientes b de
  1/B(−x) = 1/J₀(2√x) são positivos, log-côncavos, e b_{k+1}/b_k ↓ L = 4/j₀,₁² (passo `raio_ser`/`raiz_ser`).
* Ξ(t) = Σ (−1)ⁿ aₙ t²ⁿ com aₙ = 2∫₀^∞ Φ(u)u²ⁿ/(2n)! du (ATK.XiTP.aXi); a₀ = Ξ(0) = ξ(½).
"""
import json
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import asw  # noqa: E402
import fechamento  # noqa: E402

J01 = 2.404825557695773  # primeiro zero de J₀
XI_MEIO = 0.497120778188314  # ξ(1/2)


def coef_I0(n):
    return [F(1, math.factorial(k) ** 2) for k in range(n)]


def razoes_inversa_I0(n=60):
    b = asw.inversa_neg(coef_I0(n), n)
    return b, [float(b[k + 1] / b[k]) for k in range(n - 1)]


def phi(u, nmax=8):
    s = 0.0
    for n in range(1, nmax):
        c = math.pi * n * n
        s += (4 * c * c * math.exp(9 * u / 2) - 6 * c * math.exp(5 * u / 2)) * math.exp(-c * math.exp(2 * u))
    return s


def a_xi(n, umax=4.0, passos=4000):
    """aₙ = 2∫₀^∞ Φ(u) u²ⁿ/(2n)! du (Simpson)."""
    h = umax / passos
    f = lambda u: phi(u) * u ** (2 * n) / math.factorial(2 * n)  # noqa: E731
    s = f(0) + f(umax) + sum((4 if i % 2 else 2) * f(i * h) for i in range(1, passos))
    return 2 * s * h / 3


def main(saida=None):
    b, rz = razoes_inversa_I0()
    a = [a_xi(n) for n in range(10)]
    res = {
        "I0_razao_final": format(rz[-1], ".12g"),
        "I0_4/j01^2": format(4 / J01 ** 2, ".12g"),
        "I0_razoes_decrescem": all(rz[k + 1] <= rz[k] + 1e-15 for k in range(len(rz) - 1)),
        "I0_menor_min_toeplitz": str(fechamento.menor_minimo(coef_I0(8))),
        "a_xi_0..4": [format(x, ".12g") for x in a[:5]],
        "a_xi_0_menos_xi_meio": format(a[0] - XI_MEIO, ".3g"),
        "turan_a_xi_n=1..8": [a[n] ** 2 >= a[n - 1] * a[n + 1] for n in range(1, 9)],
        "aviso": "verificação finita; PF∞(aₙ) é OPEN_MATH (equivale a HR)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
