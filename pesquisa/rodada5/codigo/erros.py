#!/usr/bin/env python3
"""Companheiro numérico de ATK/ErrosGram.lean, ATK/ErrosAnaliticos.lean e ATK/ErrosConstantes.lean.

Para cada erro dos textos: o valor do texto, de onde ele vem e o valor correto. Só biblioteca padrão
(Decimal/Fraction). Nada aqui é certificado: os teoremas estão no kernel.

* E1  G₁₁ = log 2π − γ − 1 é só ∫_{(0,1]}{1/t}²; o D₁ do texto (≈ 0,31426) é o mínimo do resíduo local.
* E2  G₁₁ = log 2 dá D₁ ≈ 0,74212 (coerente com o texto), abaixo do D₁ correto ≈ 0,85821.
* E3  b̃_k = b_k − H_{k−1}/k; negativo para todo k ≥ 4.
* E4  G₁₂ ≈ 0,77220926; somas parciais Pc(K) + ½ ficam por baixo, com erro ≈ 0,1458/K: o 0,7722083 tabelado
      corresponde a truncar em K ≈ 1,5·10⁵.
* E9  Ξ(t) = 2∫₀^∞ Φ(u)cos(tu)du com Φ(u) = Σ(4π²n⁴e^{9u/2} − 6πn²e^{5u/2})e^{−πn²e^{2u}}.
* E10 região ½ + 1/T ≤ σ ≤ 1 − 1/T vazia para T < 4.
* E12 D_N log N < C₀ = 2 + γ − log 4π nos dois pontos.
* E13 1/ζ(3) = 0,8319073726…; 2π² = área de S³.
"""
import json
import math
import os
import sys
from decimal import Decimal as D, getcontext
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gram2  # noqa: E402

getcontext().prec = 60
G = gram2.GAMMA
PI = gram2.PI
LN2 = gram2.LN2
XI_MEIO = D("0.49712077818831410991")  # ξ(½) = Ξ(0)


def e1():
    L = (2 * PI).ln()
    a = 1 - G
    g = L - G - 1
    return {"G11": L - G, "Ioc_fr2": g, "cauda": D(1), "D1texto": 1 - a * a / g,
            "D1": 1 - a * a / (L - G), "x_local": a / g}


def residuo_local(x):
    """∫_{(0,1]}(1 − x{1/t})² = 1 − 2x(1−γ) + x²(log 2π − γ − 1)."""
    x = D(x)
    return 1 - 2 * x * (1 - G) + x * x * ((2 * PI).ln() - G - 1)


def residuo(x):
    """‖χ − xρ₁‖² = resíduo local + x² (cauda)."""
    x = D(x)
    return residuo_local(x) + x * x


def e2():
    return {"D1log2": 1 - (1 - G) ** 2 / LN2, "G11_menos_log2": PI.ln() - G}


def harm(n):
    return sum(Fraction(1, k) for k in range(1, n + 1))


def b_correto(k):
    return (D(k).ln() + 1 - G) / k


def b_texto(k):
    return (1 - G + D(k).ln() - gram2.dec(harm(k - 1))) / k


def e3(kmax=30):
    neg = [k for k in range(2, kmax + 1) if b_texto(k) < 0]
    return {"b_texto": {k: b_texto(k) for k in (2, 3, 4)}, "primeiro_negativo": neg[0],
            "todos_negativos_de_4": neg == list(range(4, kmax + 1)),
            "listados_no_texto": {2: D("0.0579657578"), 3: D("0.0072177332"), 4: D("-0.0060668825")}}


def e4():
    G12 = gram2.gram()["G12"]
    parc = {K: gram2.Pc(K) + D(1) / 2 for K in (10, 100, 1000, 10000)}
    tab = D("0.7722083")
    return {"G12": G12, "parciais": parc, "tabela": tab,
            "erro_vezes_K": {K: (G12 - v) * K for K, v in parc.items()},
            "K_estimado": D("0.1458") / (G12 - tab)}


def phi_texto(u):
    e2u, e45, e25 = (2 * u).exp(), (D(9) * u / 2).exp(), (D(5) * u / 2).exp()
    s, n = D(0), 1
    while True:
        arg = PI * n * n * e2u
        if arg > 200:
            break
        s += (4 * PI * PI * n ** 4 * e45 - 6 * PI * n * n * e25) * (-arg).exp()
        n += 1
    return s


def cos_dec(x):
    x = D(x)
    s, t, k = D(0), D(1), 0
    while abs(t) > D(10) ** (-40):
        s += t
        k += 2
        t = -t * x * x / (k * (k - 1))
    return s


def integral_phi_cos(t, h=D(1) / 64, U=D(3)):
    """∫₀^∞ Φ(u)cos(tu)du pelo trapézio (Φ par, decaimento duplo-exponencial)."""
    J = int(U / h)
    s = phi_texto(D(0)) / 2
    for j in range(1, J + 1):
        u = h * j
        s += phi_texto(u) * cos_dec(D(t) * u)
    return h * s


def e9():
    I0 = integral_phi_cos(0)
    I1 = integral_phi_cos(D("14.134725141734693790"))
    return {"int0": I0, "dois_int0": 2 * I0, "xi_meio": XI_MEIO, "dois_int_no_zero": 2 * I1}


def e10(Ts=("2.5", "3", "3.9", "4", "5")):
    out = {}
    for T in Ts:
        T = D(T)
        out[str(T)] = (D(1) / 2 + 1 / T, 1 - 1 / T)
    return out


def e12():
    r = gram2.ajuste()
    C0 = 2 + G - (4 * PI).ln()
    return {"C0": C0, "p256": r["produto_256"], "p8000": r["produto_8000"],
            "r256": r["produto_256"] / C0, "r8000": r["produto_8000"] / C0}


def e13():
    S = sum(Fraction(1, n ** 3) for n in range(1, 61))
    up = S + Fraction(1, 7320)
    lo = S + Fraction(1, 2 * 61 ** 2) + Fraction(1, 2 * 61 ** 3)
    z3 = D("1.2020569031595942853997381615114499907649862923405")
    return {"z3_lo": gram2.dec(lo), "z3_hi": gram2.dec(up), "inv_z3": 1 / z3,
            "inv_lo": 1 / gram2.dec(up), "inv_hi": 1 / gram2.dec(lo),
            "dois_pi2": 2 * PI * PI, "vol_B2": PI, "vol_B3": 4 * PI / 3, "vol_B4": PI * PI / 2}


def main(saida=None):
    def s(v):
        if isinstance(v, dict):
            return {str(k): s(x) for k, x in v.items()}
        if isinstance(v, (list, tuple)):
            return [s(x) for x in v]
        return format(v, ".18g") if isinstance(v, D) else v
    res = {"E1": s(e1()), "E2": s(e2()), "E3": s(e3()), "E4": s(e4()), "E9": s(e9()),
           "E10": s(e10()), "E12": s(e12()), "E13": s(e13())}
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
