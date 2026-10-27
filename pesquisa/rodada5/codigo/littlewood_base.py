#!/usr/bin/env python3
"""Companheiro numérico da rodada 90: Littlewood, parte 1 (ATK/ZeroClasses/LittlewoodBase.lean).

Só biblioteca padrão (`A_τ`, `Φ_τ` de `explicita_gauss.py`). **Nada aqui é certificado.**

* `integral_kg_exp`: `∫ k_τ(v) e^{lv} dv = e^{τl²}` por quadratura;
* `A_sub_eq`: `A_τ(u) − e^{u/2 + τ/4}` contra `∫ k_τ(v) F(u − v) dv`, `F(y) = (ψ(e^y) − e^y)e^{−y/2}`;
* `re_pw_RH`: `Re(W(ρ)/ρ)` contra `e^{−τγ²}(cos(γu)/2 + γ sen(γu))/|ρ|²` em `Re ρ = ½`;
* `Fpsi_le_RH` (sanidade): `max_{0 < y < 14} |F(y)|/(1 + y²)` (RH até essa altura é conhecida numericamente).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explicita_gauss as eg  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def psi_tab(xmax):
    lam = [0.0] * (xmax + 1)
    crivo = bytearray([1]) * (xmax + 1)
    for p in range(2, xmax + 1):
        if crivo[p]:
            for q in range(p * p, xmax + 1, p):
                crivo[q] = 0
            lp = math.log(p)
            pk = p
            while pk <= xmax:
                lam[pk] = lp
                pk *= p
    tab = [0.0] * (xmax + 1)
    acc = 0.0
    for n in range(1, xmax + 1):
        acc += lam[n]
        tab[n] = acc
    return tab


def main(saida=None):
    tau = 0.02
    mgf = []
    for l in (-0.5, 1.0, 3.0):
        h = 0.0005
        tot = 0.0
        v = -3.0
        while v <= 3.0:
            tot += eg.kg(tau, v) * math.exp(l * v) * h
            v += h
        mgf.append({"l": l, "quad": tot, "exp": math.exp(tau * l * l)})
    tab = psi_tab(int(math.exp(14.0)) + 2)

    def F(y):
        x = math.exp(y)
        p = tab[int(x)] if x >= 1 else 0.0
        return (p - x) * math.exp(-y / 2)
    lado = []
    for u in (3.0, 4.0, 5.0):
        h = 0.00001
        tot = 0.0
        v = -1.2
        while v <= 1.2:
            tot += eg.kg(tau, v) * F(u - v) * h
            v += h
        lado.append({"u": u, "A_menos_W1": eg.A(tau, u) - math.exp(u / 2 + tau / 4), "integral": tot})
    rh = []
    for g, u in ((14.134725, 3.0), (-21.02204, 4.5), (25.010858, 7.0)):
        rho = complex(0.5, g)
        w = eg.W(rho, u, tau) / rho
        f = math.exp(-tau * g * g) * (math.cos(g * u) / 2 + g * math.sin(g * u)) / abs(rho) ** 2
        rh.append({"gamma": g, "re": w.real, "formula": f})
    fmax = max(abs(F(y)) / (1 + y * y) for y in [i * 0.01 for i in range(1, 1400)])
    out = {"tau": tau, "mgf": mgf, "lado_psi": lado, "re_pw_RH": rh, "max_F_sobre_1_y2": fmax,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodBase.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_base.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
