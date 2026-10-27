#!/usr/bin/env python3
"""Companheiro numérico da rodada 52: `ζ′/ζ = O(log² t)` na região livre de zeros
(ATK/ZeroClasses/LogDerivZeta.lean).

Só biblioteca padrão (ζ por Euler–Maclaurin, de `zeroclasses.py`; `ζ′` por diferença central). **Nada aqui é
certificado.**

* `logDeriv_zeta_le`: `|ζ′/ζ(σ + it)|/log²t` para `t = 10, 100, 1000` e `σ = 1 − 0,05/log t, 1, 1 + 1/log t, 2`;
* `norm_logDeriv_le`: `|ζ′/ζ(σ + it)| ≤ −ζ′/ζ(σ)` em `σ = 1,1; 1,5; 2`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def logderiv(s, h=1e-5):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)


def main(saida=None):
    regiao = []
    for t in (10.0, 100.0, 1000.0):
        L = math.log(t)
        for sig in (1 - 0.05 / L, 1.0, 1 + 1 / L, 2.0):
            v = abs(logderiv(complex(sig, t)))
            regiao.append({"t": t, "sigma": sig, "abs_logderiv": v, "razao_log2": v / L ** 2})
    serie = []
    for sig in (1.1, 1.5, 2.0):
        ref = -logderiv(complex(sig, 0)).real
        for t in (3.0, 30.0, 300.0):
            serie.append({"sigma": sig, "t": t, "abs": abs(logderiv(complex(sig, t))), "menos_logderiv_real": ref})
    res = {"regiao": regiao, "serie": serie}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "logderiv_zeta.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
