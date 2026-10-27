#!/usr/bin/env python3
"""Companheiro numérico da rodada 67: RH ⟺ `ψ(x) = x + O(√x log² x)` ⟺ `π(x) = Li(x) + O(√x log x)`
(ATK/ZeroClasses/PsiLog2.lean).

Só biblioteca padrão (zeros de `canonico.py`, `Li` de `pi_li.py`). **Nada aqui é certificado.**

* `psi_RH_log2`: `max |ψ(x) − x|/(√x log² x)` por década até `10⁷`;
* `pi_RH_log`: `|π(x) − Li(x)|/(√x log x)` em `x = 10^k`;
* o resíduo explícito (`bordo_explicita`) em números: `ψ₀(x)` contra `x − Σ_{|γ|<T} x^ρ/ρ − log 2π − ½ log(1 − x^{−2})`
  com os 341 zeros de `0 < γ ≤ 600`, em `x = 100,5; 1000,5; 10000,5`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import pi_li  # noqa: E402
import psi_rh  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 7


def main(saida=None, N=NMAX):
    lam = psi_rh.vonmangoldt(N)
    psi = 0.0
    pi = 0
    dec = []
    pts = []
    k = 3
    m2 = 0.0
    psis = {}
    for n in range(1, N + 1):
        psi += lam[n]
        if lam[n] > 0 and abs(math.exp(lam[n]) - n) < 0.5:
            pi += 1
        if n >= 100:
            for x in (n, n + 1 - 1e-9):
                m2 = max(m2, abs(psi - x) / (math.sqrt(x) * math.log(x) ** 2))
        if n in (100, 1000, 10000):
            psis[n] = psi
        if n == 10 ** k:
            dec.append({"x": n, "max_psi_log2": m2})
            m2 = 0.0
            pts.append({"x": n, "pi-Li": pi - pi_li.Li(n),
                        "razao_log": abs(pi - pi_li.Li(n)) / (math.sqrt(n) * math.log(n))})
            k += 1
    g = ca.zeros(T=600.0)
    expl = []
    for n in (100, 1000, 10000):
        x = n + 0.5
        soma = sum(2 * (cmath.exp(complex(0.5, t) * math.log(x)) / complex(0.5, t)).real for t in g)
        f = x - soma - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
        expl.append({"x": x, "psi": psis[n], "formula_600": f, "dif": psis[n] - f,
                     "soma_zeros": soma, "cota_sqrt_soma": math.sqrt(x) * sum(2 / abs(complex(0.5, t)) for t in g)})
    out = {"decadas_psi": dec, "pi_Li": pts, "formula_explicita": expl,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PsiLog2.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "psi_log2.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    for d in o["decadas_psi"]:
        print(d)
    for p in o["pi_Li"]:
        print(p)
    for e in o["formula_explicita"]:
        print(e)
