#!/usr/bin/env python3
"""Companheiro numérico da rodada 94: as médias de `F` sob RH (ATK/ZeroClasses/LittlewoodMedia.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `integral_F_log`: `I(y) = ∫₁ʸ F(u) du`, `F(u) = (ψ(e^u) − e^u)e^{−u/2}`, fica limitada em `1 ≤ y ≤ 15`,
  embora `F` mesma oscile; compara-se `max |I|` com `max |F|`;
* `integral_re_pw_le`: `|∫ₐᵇ Re(W_u(ρ)/ρ) du| ≤ 3/|ρ|²` nos três primeiros zeros (`τ = 0,02`);
* `H_ge`: `e^v + e^{−v} − 2 ≥ v²/2 + |v|³/6` numa malha.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import littlewood_base as lb  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
ZEROS = [14.134725141734693, 21.022039638771555, 25.010857580145688]


def main(saida=None, ymax=15.0, h=0.001):
    tab = lb.psi_tab(int(math.exp(ymax)) + 2)

    def F(u):
        x = math.exp(u)
        return (tab[int(x)] - x) * math.exp(-u / 2)
    n = int((ymax - 1.0) / h)
    I = 0.0
    maxI = maxF = 0.0
    for k in range(n):
        u = 1.0 + (k + 0.5) * h
        f = F(u)
        I += f * h
        maxI = max(maxI, abs(I))
        maxF = max(maxF, abs(f))
    pw = []
    tau = 0.02
    for g in ZEROS:
        rho = complex(0.5, g)
        for a, b in ((0.0, 1.0), (2.0, 7.5), (3.0, 30.0)):
            m = 4000
            hh = (b - a) / m
            tot = 0.0
            for i in range(m):
                u = a + (i + 0.5) * hh
                w = cmath.exp((rho - 0.5) * u + tau * (rho - 0.5) ** 2)
                tot += (w / rho).real * hh
            pw.append({"gamma": g, "a": a, "b": b, "integral": tot, "cota": 3 / abs(rho) ** 2})
    hge = min(math.exp(v) + math.exp(-v) - 2 - (v * v / 2 + abs(v) ** 3 / 6)
              for v in [i * 0.01 for i in range(-1000, 1001)])
    out = {"ymax": ymax, "max_abs_I": maxI, "max_abs_F": maxF, "I_final": I, "re_pw": pw,
           "H_ge_folga_min": hge,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodMedia.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_media.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    print({k: v for k, v in o.items() if k != "re_pw"})
    for r in o["re_pw"]:
        print(r)
