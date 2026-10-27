#!/usr/bin/env python3
"""Companheiro numérico da rodada 91: a soma sobre os zeros forçada (ATK/ZeroClasses/LittlewoodSoma.lean).

Só biblioteca padrão (zeros `½ + iγ` com `0 < γ ≤ 300` de `canonico.py`, todos simples). **Nada aqui é
certificado.**

* `massa_le_real`: `Σ_{|γ| ≤ X} m_ρ = 2N(X)` contra `4X(a₀ + log(X + 3))/l₀`;
* `D_ge`: `D(1/T) = Σ_{|γ| ≤ 3T} e^{−Aγ²/T²} γ sen(γ/T)/|ρ|²` contra `e^{−A}/(πT) · Σ_{|γ| ≤ T} m_ρ`;
* `cauda_le`: `Σ_{3T < |γ| ≤ 300} e^{−Aγ²/T²}/|ρ|` contra `3(a₀ + log 5T)e^{−4A}/l₀`;
* `alinha` + `soma_forcada`: um `n ≤ Q^K` que alinha os zeros com `|γ| ≤ 3T` (`‖nγ/2π‖ < 1/Q`), e a soma
  `Σ_{|γ| ≤ 300} Re(W_{n ± 1/T}(ρ)/ρ)` com `W_u(s) = e^{(s−½)u + A(s−½)²/T²}` contra `±D(1/T)`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
A0_CONST = math.log(31) + abs(math.log(2 - math.pi ** 2 / 6))
L0 = math.log(19 / 16)


def re_pw(gam, u, tau):
    rho = complex(0.5, gam)
    w = cmath.exp((rho - 0.5) * u + tau * (rho - 0.5) ** 2)
    return (w / rho).real


def soma_zeros(gs, u, tau):
    # zeros simétricos ±γ, todos simples
    return sum(re_pw(g, u, tau) + re_pw(-g, u, tau) for g in gs)


def D(gs, T, A, v):
    tot = 0.0
    for g in gs:
        if g <= 3 * T:
            r2 = 0.25 + g * g
            tot += 2 * math.exp(-A * g * g / T ** 2) * g * math.sin(g * v) / r2
    return tot


def alinha(gs, T, Q):
    alvo = [g for g in gs if g <= 3 * T]
    K = len(alvo)
    for n in range(1, Q ** K + 1):
        if all(abs(n * g / (2 * math.pi) - round(n * g / (2 * math.pi))) < 1 / Q for g in alvo):
            return n, K
    return None, K


def main(saida=None):
    gs = ca.zeros(300.0)
    massa = []
    for X in (50.0, 100.0, 200.0, 300.0):
        m = 2 * sum(1 for g in gs if g <= X)
        massa.append({"X": X, "massa": m, "cota": 4 * X * (A0_CONST + math.log(X + 3)) / L0})
    dge = []
    for T, A in ((10.0, 1.0), (20.0, 1.0), (30.0, 1.0), (30.0, 2.0)):
        main_ = math.exp(-A) / (math.pi * T) * 2 * sum(1 for g in gs if g <= T)
        dge.append({"T": T, "A": A, "D": D(gs, T, A, 1 / T), "principal": main_})
    cauda = []
    for T, A in ((10.0, 1.0), (20.0, 1.0), (30.0, 1.0)):
        c = sum(2 * math.exp(-A * g * g / T ** 2) / math.hypot(0.5, g) for g in gs if g > 3 * T)
        cauda.append({"T": T, "A": A, "cauda": c, "cota": 3 * (A0_CONST + math.log(5 * T)) / L0 * math.exp(-4 * A)})
    T, A, Q = 10.0, 1.0, 8
    n, K = alinha(gs, T, Q)
    tau = A / T ** 2
    forc = {
        "T": T, "A": A, "Q": Q, "K": K, "n": n, "cota_n": Q ** K,
        "soma_mais": soma_zeros(gs, n + 1 / T, tau),
        "soma_menos": soma_zeros(gs, n - 1 / T, tau),
        "D": D(gs, T, A, 1 / T),
        "sem_alinhar_mais": soma_zeros(gs, 1 + 1 / T, tau),
    }
    out = {"massa": massa, "D_ge": dge, "cauda": cauda, "forcada": forc,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodSoma.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_soma.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for k in ("massa", "D_ge", "cauda"):
        for r in o[k]:
            print(k, r)
    print("forcada", o["forcada"])
