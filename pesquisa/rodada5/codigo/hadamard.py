#!/usr/bin/env python3
"""Companheiro numérico de ATK/HadamardGenero0.lean e ATK/XiCrescimento.lean (rodada 11).

Só biblioteca padrão. Nada aqui é certificado: os teoremas estão no kernel, e a positividade total dos
coeficientes de Ξ continua `OPEN_MATH` (equivale a HR). Os testes são verificações de consistência.

* Hadamard de gênero 0 (`coef_eq_lim`, `prodCoef_mono`, `prodCoef_le`): B(w) = Σ wⁿ/(n!)² = I₀(2√w) tem zeros
  −j₀,ₖ²/4, logo B = ∏(1 + αₖw) com αₖ = 4/j₀,ₖ²; as funções simétricas elementares dos αₖ são os coeficientes:
  Σαₖ = 1, e₂ = 1/4, e₃ = 1/36, … (= 1/(n!)²), crescem com o número de fatores e ficam ≤ (Σαₖ)ⁿ.
* Ξ (`rh_iff_genero0`): com os zeros 1/2 + iγₖ na linha crítica, B(w) = a₀∏(1 + w/γₖ²), logo
  a₁/a₀ = Σ1/γₖ² e a₂/a₀ = e₂(1/γₖ²). Usa os 20 primeiros zeros (valores clássicos) e a cauda pela fórmula de
  Riemann–von Mangoldt N(t) = θ(t)/π + 1 + S(t) (desprezando ∫S(t)/t³). Os aₙ vêm de aₙ = 2∫₀^∞Φ(u)u²ⁿ/(2n)!du
  (rodada 10, `edrei.a_xi`). Os zeros usados foram verificados numericamente por outros; isto não prova HR.
"""
import json
import math
import os
import sys
from decimal import Decimal as D
from decimal import getcontext

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edrei  # noqa: E402

# 20 primeiros zeros γₖ de ζ(1/2 + iγ) (Odlyzko)
GAMMAS = [
    14.134725141734693, 21.022039638771555, 25.010857580145688, 30.424876125859513,
    32.935061587739189, 37.586178158825671, 40.918719012147495, 43.327073280914999,
    48.005150881167159, 49.773832477672302, 52.970321477714460, 56.446247697063394,
    59.347044002602353, 60.831778524609809, 65.112544048081606, 67.079810529494173,
    69.546401711173979, 72.067157674481907, 75.704690699083933, 77.144840068874805,
]
GAMMA_21 = 79.337375020249367


def prod_coef(a0, alphas, nmax):
    """`ATK.Edrei.prodCoef`: coeficientes de a₀∏(1 + αⱼz) (recursão do Lean)."""
    c = [a0] + [0.0] * nmax
    for al in alphas:
        for n in range(nmax, 0, -1):
            c[n] += al * c[n - 1]
    return c


def _j0_j1(x, prec=90):
    getcontext().prec = prec
    x = D(repr(x))
    h = (x / 2) ** 2
    t, s0, k = D(1), D(0), 0
    s1, t1 = D(0), x / 2
    while True:
        s0 += t
        s1 += t1
        k += 1
        t = -t * h / (k * k)
        t1 = -t1 * h / (k * (k + 1))
        if abs(t) < D(10) ** (-40) and abs(t1) < D(10) ** (-40) and k > 5:
            break
    return float(s0), float(s1)


def mcmahon(k):
    b = (k - 0.25) * math.pi
    m = 8 * b
    return b + 1 / m - 124 / (3 * m ** 3) + 120928 / (15 * m ** 5)


def zeros_j0(K=30):
    """Os K primeiros zeros de J₀ (Newton em precisão alta a partir de McMahon)."""
    zs = []
    for k in range(1, K + 1):
        x = mcmahon(k)
        for _ in range(8):
            j0, j1 = _j0_j1(x)
            x = x + j0 / j1  # J₀' = −J₁
        zs.append(x)
    return zs


def potencias_alpha_I0(K=30, M=200000, jmax=5):
    """p_j = Σαₖʲ (αₖ = 4/j₀,ₖ²): K zeros exatos, McMahon até M, cauda integral para j = 1."""
    zs = zeros_j0(K)
    al = [4 / z ** 2 for z in zs] + [4 / mcmahon(k) ** 2 for k in range(K + 1, M + 1)]
    p = [math.fsum(a ** j for a in al) for j in range(1, jmax + 1)]
    p[0] += 4 / (math.pi ** 2 * (M + 0.25))  # Σ_{k>M} 4/((k − 1/4)π)² ≈ ∫_{M+1/2}^∞
    return zs, p


def elementares(p):
    """Identidades de Newton: e₁..e_n a partir de p₁..p_n."""
    e = [1.0]
    for n in range(1, len(p) + 1):
        e.append(sum((-1) ** (i - 1) * e[n - i] * p[i - 1] for i in range(1, n + 1)) / n)
    return e


def theta(t):
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def p_xi(T=None):
    """Σ1/γₖ² e Σ1/γₖ⁴: 20 zeros + cauda ∫_T^∞ t^{−j} dN̄(t), N̄ = θ/π + 1 (sem o termo S(t))."""
    if T is None:
        T = (GAMMAS[-1] + GAMMA_21) / 2
    n = len(GAMMAS)
    c = 2 * math.pi
    # ∫_T^∞ N̄(t)/t³ dt e ∫_T^∞ N̄(t)/t⁵ dt com N̄ = (t/2π)(log(t/2π) − 1) + 7/8 + 1/(48πt)
    i3 = math.log(T / c) / (c * T) + 7 / (16 * T ** 2) + 1 / (144 * math.pi * T ** 3)
    i5 = ((math.log(T / c) + 1 / 3) / (3 * T ** 3) - 1 / (3 * T ** 3)) / c + 7 / (32 * T ** 4) \
        + 1 / (240 * math.pi * T ** 5)
    p1 = math.fsum(1 / g ** 2 for g in GAMMAS) - n / T ** 2 + 2 * i3
    p2 = math.fsum(1 / g ** 4 for g in GAMMAS) - n / T ** 4 + 4 * i5
    return p1, p2


def main(saida=None):
    zs, p = potencias_alpha_I0()
    e = elementares(p)
    alphas = [4 / z ** 2 for z in zs]
    pcs = [prod_coef(1.0, alphas[:N], 4) for N in (5, 10, 20, 30)]
    a = [edrei.a_xi(n) for n in range(3)]
    p1, p2 = p_xi()
    res = {
        "I0_j01": format(zs[0], ".15g"),
        "I0_soma_alpha": format(p[0], ".12g"),
        "I0_soma_alpha2": format(p[1], ".12g"),
        "I0_e_n_vs_1/(n!)^2": [[format(e[n], ".10g"), format(1 / math.factorial(n) ** 2, ".10g")]
                               for n in range(1, 6)],
        "I0_prodCoef_n=1..3_N=5,10,20,30": [[format(c[n], ".8g") for n in (1, 2, 3)] for c in pcs],
        "Xi_a1/a0": format(a[1] / a[0], ".10g"),
        "Xi_soma_1/gamma^2": format(p1, ".10g"),
        "Xi_a2/a0": format(a[2] / a[0], ".10g"),
        "Xi_e2(1/gamma^2)": format((p1 ** 2 - p2) / 2, ".10g"),
        "aviso": "consistência numérica (zeros conhecidos na linha); PF∞(aₙ) é OPEN_MATH (equivale a HR)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
