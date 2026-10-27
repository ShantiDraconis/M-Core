#!/usr/bin/env python3
"""Companheiro numérico da rodada 81: o TNP com erro para `θ` e `π` (ATK/ZeroClasses/TNPPi.lean).

Só biblioteca padrão (`li`/`Li` de `pi_li.py`). **Nada aqui é certificado.**

* `sqrt_log_le_V`: em `u = √log x ≥ 2b + 4`, `u²/2 + 2 log u ≤ u² − bu` (a forma logarítmica de
  `√x log x ≤ x e^{−b√log x}`), numa grade de `b` e `u`;
* `abel_dif`: a fórmula de Abel `π(x) = θ(x)/log x + ∫_2^x θ(t)/(t log²t) dt`, com a integral somada exatamente entre
  primos (`θ` é constante em cada intervalo), em `x = 10², 10³, 10⁴, 10⁵`;
* `pi_tnp`: `|π(x) − Li(x)|`, `x e^{−½√log x}` e `x/log³x` em `x = 10³ … 10⁷` (só ordem de grandeza: as
  constantes da prova não são explícitas).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pi_li  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def crivo(n):
    m = bytearray([1]) * (n + 1)
    m[0] = m[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if m[p]:
            m[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    return [i for i in range(n + 1) if m[i]]


def abel(x, primos):
    ps = [p for p in primos if p <= x]
    theta = 0.0
    soma = 0.0
    for i, p in enumerate(ps):
        theta += math.log(p)
        b = ps[i + 1] if i + 1 < len(ps) else x
        soma += theta * (1 / math.log(p) - 1 / math.log(b))
    return {"x": x, "pi": len(ps), "abel": theta / math.log(x) + soma}


def main(saida=None):
    grade = []
    for b in (0.1, 0.5, 1.0, 3.0):
        piores = min((u * u - b * u) - (u * u / 2 + 2 * math.log(u))
                     for u in [2 * b + 4 + 0.5 * k for k in range(200)])
        grade.append({"b": b, "folga_minima": piores})
    primos = crivo(10 ** 7)
    abels = [abel(x, primos) for x in (100, 1000, 10 ** 4, 10 ** 5)]
    tnp = []
    for k in range(3, 8):
        x = 10 ** k
        pi = sum(1 for p in primos if p <= x)
        tnp.append({"x": x, "pi_menos_Li": pi - pi_li.Li(x),
                    "x_exp": x * math.exp(-0.5 * math.sqrt(math.log(x))), "x_log3": x / math.log(x) ** 3})
    out = {"sqrt_log_le_V": grade, "abel": abels, "tnp": tnp,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/TNPPi.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "tnp_pi.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
