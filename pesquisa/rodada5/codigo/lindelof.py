#!/usr/bin/env python3
"""Companheiro numérico da rodada 61: RH ⟹ Lindelöf (ATK/ZeroClasses/LindelofRH.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`). **Nada aqui é certificado**: Lindelöf é uma
afirmação assintótica, e dados finitos não a testam.

* `lindelof_of_RH` (lado dos dados): `M(T) = max_{T ≤ t ≤ 2T} |ζ(½ + it)|` numa malha de passo `0,05` para
  `T = 10, 20, …, 640`, e o expoente aparente `log M(T)/log T`;
* `norm_zeta_one_sub_le` (o passo da equação funcional): `|ζ(½ − δ + it)|/|ζ(½ + δ − it)|` contra
  `2C_Γ|½ + δ − it|^δ`, `δ = ¼`;
* `fator_le`: `(1 + |t|)^a |s + 2|^{−k} ≤ 2^a` em pontos da faixa.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
CGAMMA = math.sqrt(2 * math.pi) * math.exp(1.5) * math.exp(3 * math.pi / 4)


def main(saida=None):
    tab = []
    T = 10.0
    while T <= 640:
        n = int(T / 0.05)
        m = 0.0
        for i in range(n + 1):
            t = T + i * 0.05
            m = max(m, abs(zc.zeta(complex(0.5, t))))
        tab.append({"T": T, "max_zeta": m, "expoente": math.log(m) / math.log(T)})
        T *= 2
    d = 0.25
    fe = []
    for t in (10.0, 50.0, 200.0):
        w = complex(0.5 + d, -t)
        r = abs(zc.zeta(1 - w)) / abs(zc.zeta(w))
        fe.append({"t": t, "razao": r, "cota": 2 * CGAMMA * abs(w) ** d, "assint": (t / (2 * math.pi)) ** d})
    fat = []
    for sig in (0.25, 0.5, 0.75):
        for t in (0.0, 3.0, 100.0):
            s = complex(sig, t)
            a, k = 0.1, 0.2
            fat.append((1 + abs(t)) ** a * abs(s + 2) ** (-k))
    res = {"maximos": tab, "equacao_funcional": fe, "fator_max": max(fat), "CGamma": CGAMMA}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "lindelof.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
