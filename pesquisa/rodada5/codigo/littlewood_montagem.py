#!/usr/bin/env python3
"""Companheiro numérico da rodada 92: a montagem de Littlewood (ATK/ZeroClasses/LittlewoodMontagem.lean).

Só biblioteca padrão. **Nada aqui é certificado**; o teorema é assintótico (`log log log x` cresce devagar
demais para ser visto numericamente). O que se confere:

* `integral_abs_gauss`: `∫ |y| e^{−τy²} dy = 1/τ` por quadratura;
* `log_N_le`: para `T = 10, 20, 30`, com `K = 2N(3T)` (zeros de `canonico.py`) e `Q = ⌈(1 + log 3T)²⌉`,
  `log(⌈T²⌉ Q^K + 2)` contra `C_G T^{3/2}` (`C_G = 11 + 168(a₀ + 6)/l₀`) e contra `T²`;
* as oscilações de `F(y) = (ψ(e^y) − e^y) e^{−y/2}` em `y ≤ 15`: os extremos de cada lado e o sinal trocando
  muitas vezes, como o teorema exige (aqui só ilustrativo).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import littlewood_base as lb  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
A0_CONST = math.log(31) + abs(math.log(2 - math.pi ** 2 / 6))
L0 = math.log(19 / 16)
CG = 11 + 168 * (A0_CONST + 6) / L0


def main(saida=None):
    gauss = []
    for tau in (0.5, 0.1, 0.02):
        h = 0.001
        lim = 12 / math.sqrt(tau)
        n = int(2 * lim / h)
        tot = sum(abs(-lim + i * h) * math.exp(-tau * (-lim + i * h) ** 2) for i in range(n + 1)) * h
        gauss.append({"tau": tau, "quad": tot, "inv": 1 / tau})
    gs = ca.zeros(100.0)
    cresc = []
    for T in (10.0, 20.0, 30.0):
        K = 2 * sum(1 for g in gs if g <= 3 * T)
        Q = math.ceil((1 + math.log(3 * T)) ** 2)
        lnN = math.log(math.ceil(T * T)) + K * math.log(Q) + math.log(3)
        cresc.append({"T": T, "K": K, "Q": Q, "log_N": lnN, "cota": CG * T ** 1.5, "T2": T * T})
    xmax = int(math.exp(15.0)) + 2
    tab = lb.psi_tab(xmax)

    def F(y):
        x = math.exp(y)
        return (tab[int(x)] - x) * math.exp(-y / 2)
    ys = [2 + i * 0.001 for i in range(13001)]
    vals = [F(y) for y in ys]
    trocas = sum(1 for a, b in zip(vals, vals[1:]) if (a > 0) != (b > 0))
    imax = max(range(len(vals)), key=lambda i: vals[i])
    imin = min(range(len(vals)), key=lambda i: vals[i])
    osc = {"y_max": ys[imax], "F_max": vals[imax], "y_min": ys[imin], "F_min": vals[imin],
           "trocas_de_sinal": trocas,
           "logloglog_x_max": math.log(math.log(15.0))}
    out = {"integral_abs_gauss": gauss, "crescimento": cresc, "oscilacao": osc,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodMontagem.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_montagem.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for k in ("integral_abs_gauss", "crescimento"):
        for r in o[k]:
            print(k, r)
    print("oscilacao", o["oscilacao"])
