#!/usr/bin/env python3
"""Companheiro numérico da rodada 65: RH ⟺ `θ(x) = x + O(√x log³ x)` ⟺ `π(x) = Li(x) + O(√x log² x)`
(ATK/ZeroClasses/PiLiRH.lean).

Só biblioteca padrão (`Li` de `pi_li.py`, série de Ramanujan). **Nada aqui é certificado.**

* `theta_RH`: `max |θ(x) − x|/(√x log³ x)` por década até `10⁷`;
* `pi_RH`: `|π(x) − Li(x)|/(√x log² x)` e `/(√x log x/8π)` (Schoenfeld, sob RH, `x ≥ 2657`) em `x = 10^k`;
* `pi_sub_Li`: a fórmula de partes `π − Li = (θ − x)/log x + ∫_2^x (θ − t)/(t log² t) + 2/log 2` em `x = 10⁴`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pi_li  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 7


def main(saida=None, N=NMAX):
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    for p in range(2, int(N ** 0.5) + 1):
        if eh[p]:
            eh[p * p::p] = bytearray(len(range(p * p, N + 1, p)))
    th = 0.0
    pi = 0
    dec = []
    k = 1
    m3 = 0.0
    pontos = []
    thetas = {}
    for n in range(2, N + 1):
        if eh[n]:
            th += math.log(n)
            pi += 1
        for x in (n, n + 1 - 1e-9):
            m3 = max(m3, abs(th - x) / (math.sqrt(x) * math.log(x) ** 3))
        if n == 10 ** (k + 1):
            dec.append({"x": n, "max_theta_log3": m3})
            m3 = 0.0
            k += 1
            L = pi_li.Li(n)
            d = pi - L
            pontos.append({"x": n, "pi": pi, "Li": L, "pi-Li": d,
                           "razao_log2": abs(d) / (math.sqrt(n) * math.log(n) ** 2),
                           "razao_schoenfeld": abs(d) / (math.sqrt(n) * math.log(n) / (8 * math.pi))})
        if n <= 10 ** 4:
            thetas[n] = th
    # a fórmula de partes em x = 10⁴ (θ é constante por partes: soma exata nos intervalos [n, n+1])
    X = 10 ** 4
    integ = 0.0
    for n in range(2, X):
        t0, t1 = n, n + 1
        # ∫_{t0}^{t1} (θ(n) − t)/(t log² t) dt por Simpson
        f = lambda t: (thetas[n] - t) / (t * math.log(t) ** 2)  # noqa: E731
        m = 8
        h = (t1 - t0) / m
        integ += h / 3 * sum((1 if j in (0, m) else 4 if j % 2 else 2) * f(t0 + j * h) for j in range(m + 1))
    pi_X = sum(1 for n in range(2, X + 1) if eh[n])
    lado = (thetas[X] - X) / math.log(X) + integ + 2 / math.log(2)
    out = {"decadas_theta": dec, "pi_Li": pontos,
           "partes_10^4": {"pi-Li": pi_X - pi_li.Li(X), "formula": lado},
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PiLiRH.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "pi_li_rh.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    for d in o["decadas_theta"]:
        print(d)
    for p in o["pi_Li"]:
        print(p)
    print(o["partes_10^4"])
