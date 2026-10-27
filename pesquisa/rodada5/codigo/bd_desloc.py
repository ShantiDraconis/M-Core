#!/usr/bin/env python3
"""Companheiro numérico da rodada 74: o deslocamento do molificador de Riesz
(ATK/ZeroClasses/BDDesloc.lean).

Só biblioteca padrão (`ζ` de `zeroclasses.py`, `W`, `A_N` de `bd_espectral.py`). **Nada aqui é certificado.**

* `desloc`: `A_N(s) − 1/ζ(s)` contra `(1/2π) ∫ W(−δ + iy) N^{−δ+iy}/ζ(s − δ + iy) dy` em `s = 0,8 + 3i`, `δ = 0,2`,
  `N = 10` (a reta `Re = 0,6` fica à direita de ½; numericamente ζ não se anula lá);
* `molif_cota`: `|A_N(s) − 1/ζ(s)| · N^{δ}` para `N = 10, 40, 160, 640` (limitado), `s = 0,8 + 3i`, `δ = 0,25`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bd_espectral as be  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None):
    s, d, N = complex(0.8, 3), 0.2, 10
    integ = be.simpson(lambda y: be.W(complex(-d, y)) * N ** complex(-d, y) / zc.zeta(s + complex(-d, y)),
                       -300, 300, 30000) / (2 * math.pi)
    dif = be.A(N, s) - 1 / zc.zeta(s)
    cot = []
    for M in (10, 40, 160, 640):
        e = abs(be.A(M, s) - 1 / zc.zeta(s))
        cot.append({"N": M, "erro": e, "erro_vezes_N_delta": e * M ** 0.25})
    out = {"s": [s.real, s.imag], "delta": d, "N": N, "A_menos_inv_zeta": [dif.real, dif.imag],
           "integral_deslocada": [integ.real, integ.imag], "cota": cot,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDDesloc.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_desloc.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
