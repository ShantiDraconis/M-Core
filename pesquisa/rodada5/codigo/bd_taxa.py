#!/usr/bin/env python3
"""Companheiro numérico da rodada 75: `D_N(σ) ≪ N^{−2δ}` sob semiplano sem zeros (ATK/ZeroClasses/BDTaxa.lean).

Só biblioteca padrão (`ζ` de `zeroclasses.py`, `A_N` de `bd_espectral.py`). **Nada aqui é certificado.**

A cota espectral `(1/2π) ∫ |1 − ζ(s)A_N(s)|²/|s|² dτ` (rodada 73, `DNσ_le_molif`) em `σ = 0,75` para
`N = 10, 20, 40, 80, 160`, com `|τ| ≤ 1000` (Simpson) e a cauda `|τ| > 1000` estimada por `2/(2π·1000)`
(onde `|1 − ζA_N| ≈ 1` em média quadrática; só ordem de grandeza). Sob RH (numérico até onde ζ foi verificado),
`DNσ_taxa_RH` dá `D_N(σ) ≪ N^{−2δ}` para todo `δ < σ − ½ = 0,25`, isto é, expoente `> 0,5 − ε`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bd_espectral as be  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
SIGMA = 0.75
TMAX = 1000.0


def cota(N, n=20000):
    def f(t):
        s = complex(SIGMA, t)
        return abs(1 - zc.zeta(s) * be.A(N, s)) ** 2 / abs(s) ** 2
    return 2 * be.simpson(f, 0, TMAX, n) / (2 * math.pi)


def main(saida=None):
    linhas = []
    for N in (10, 20, 40, 80, 160):
        linhas.append({"N": N, "cota": cota(N)})
    incl = []
    for a, b in zip(linhas, linhas[1:]):
        incl.append(math.log(a["cota"] / b["cota"]) / math.log(b["N"] / a["N"]))
    out = {"sigma": SIGMA, "Tmax": TMAX, "cauda_estimada": 2 / (2 * math.pi * TMAX), "cotas": linhas,
           "expoentes_locais": incl, "expoente_garantido_sob_RH": 2 * (SIGMA - 0.5),
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDTaxa.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_taxa.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
