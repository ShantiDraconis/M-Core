#!/usr/bin/env python3
"""Companheiro numérico da rodada 32: o produto canônico é inteiro, tem os zeros de ξ e cresce como
`e^{C|s|^{3/2}}` (ATK/ZeroClasses/CanonicoInteira.lean).

Só biblioteca padrão. **Nada aqui é certificado.** Zeros `½ ± iγ`, `0 < γ ≤ 300`, de `canonico.zeros()`.

* `norm_E1_le`: `‖E1 z‖ ≤ e^{3‖z‖^{3/2}}` numa malha de `|z| ≤ 6` (razão máxima do logaritmo);
* `soma_ordem_inv_pot`: `Σ_{|γ| ≤ 300} 1/|ρ|^{3/2}` e a cauda `∫_{300}^∞ (log(t/2π)/2π)·2t^{−3/2} dt`;
* `Pcan_norm_le`: `log|P_{300}(s)|` em círculos `|s| = 5, 10, 20, 40` contra `3·S·|s|^{3/2}`;
* `ordem_Pcan`, `ordem_Pcan_eq_xi`: `|P_{300}(ρ₁ + h)|/|h|` estabiliza e `ξ/P_{300}` fica liso perto de `ρ₁`,
  e igual a `e^{A + Bρ₁}` vezes a cauda `exp(−ρ₁²/2 · Σ_{|γ|>300} 1/ρ²)` (o quociente que a rodada seguinte
  precisa provar ser `e^{A+Bs}`). Os zeros de Riemann–Siegel são refinados pela secante em `Ξ(t) = ξ(½ + it)`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def E1(z):
    return (1 - z) * cmath.exp(z)


def P(s, g):
    v = 1 + 0j
    for x in g:
        for r in (complex(0.5, x), complex(0.5, -x)):
            v *= E1(s / r)
    return v


def refina(t, it=8):
    """Refina um zero de Riemann–Siegel pela secante em `Ξ(t) = ξ(½ + it)` (real)."""
    f = lambda u: en.xi(complex(0.5, u)).real  # noqa: E731
    a, b = t - 1e-3, t + 1e-3
    fa, fb = f(a), f(b)
    for _ in range(it):
        if fb == fa:
            break
        a, b, fa = b, b - fb * (b - a) / (fb - fa), fb
        fb = f(b)
    return b


def main(saida=None):
    g = [refina(t) for t in ca.zeros()]
    # ‖E1 z‖ ≤ exp(3‖z‖^{3/2})
    pior = 0.0
    for i in range(1, 121):
        rr = 6 * i / 120
        for k in range(48):
            z = rr * cmath.exp(2j * math.pi * k / 48)
            pior = max(pior, math.log(max(abs(E1(z)), 1e-300)) / (3 * rr ** 1.5))
    # S = Σ 1/|ρ|^{3/2}
    S300 = sum(2 / (0.25 + x * x) ** 0.75 for x in g)
    T = 300.0
    # cauda: ∫_T^∞ (1/2π) log(t/2π) · 2 t^{-3/2} dt = (2/π) (log(T/2π) + 2)/√T
    cauda = (2 / math.pi) * (math.log(T / (2 * math.pi)) + 2) / math.sqrt(T)
    S = S300 + cauda
    circ = {}
    for R in (5, 10, 20, 40):
        m = max(math.log(abs(P(R * cmath.exp(2j * math.pi * k / 96), g))) for k in range(96))
        circ[str(R)] = {"max_log_P": m, "cota_3SR32": 3 * S * R ** 1.5, "ok": m <= 3 * S * R ** 1.5}
    # perto de ρ₁
    rho1 = complex(0.5, g[0])
    BC = ca.BC
    alvo = cmath.exp(-math.log(2) + BC * rho1)
    perto = []
    for h in (1e-2, 1e-3, 1e-4):
        s = rho1 + h
        perto.append({"h": h, "|P|/h": abs(P(s, g)) / h, "xi/P": [(en.xi(s) / P(s, g)).real,
                                                              (en.xi(s) / P(s, g)).imag]})
    # a cauda ∏_{|γ|>300} E1(s/ρ) ≈ exp(−s²/2 · Σ_{|γ|>300} 1/ρ²), Σ ≈ −(log(T/2π) + 1)/(πT)
    sig2 = -(math.log(T / (2 * math.pi)) + 1) / (math.pi * T)
    previsto = alvo * cmath.exp(-rho1 ** 2 / 2 * sig2)
    res = {
        "zeros_usados": len(g),
        "max_logE1_sobre_3r32": pior,
        "S_3/2": {"parcial_300": S300, "cauda": cauda, "total_estimado": S},
        "circulos": circ,
        "perto_rho1": perto,
        "e^(A+B rho1)": [alvo.real, alvo.imag],
        "previsto_com_cauda": [previsto.real, previsto.imag],
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "inteira.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(), indent=1, ensure_ascii=False))
