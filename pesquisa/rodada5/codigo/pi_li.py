#!/usr/bin/env python3
"""Companheiro numérico da rodada 60: `RH ⟺ π(x) = Li(x) + O(x^{1/2+ε})` (ATK/ZeroClasses/PiLi.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `Li(x) = ∫_2^x dt/log t = li(x) − li(2)`, com `li` pela série de Ramanujan;
* `Li_partes`, `Li_log_partes`: as duas integrações por partes conferidas por Simpson em `x = 100, 1000`;
* `semZeros_iff_pi` (lado dos dados): `π(x) − Li(x)` e `|π(x) − Li(x)|/(√x log x)` em `x = 10³, …, 10⁶`, contra a
  cota de Schoenfeld sob RH `1/(8π)`; `max |θ(x) − x|/√x`.
"""
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
GAMMA = 0.5772156649015329
NMAX = 10 ** 6


def li(x):
    L = math.log(x)
    tot = 0.0
    termo = 1.0
    soma_impar = 0.0
    for n in range(1, 200):
        termo *= L / n
        if (n - 1) % 2 == 0:
            soma_impar += 1 / n
        c = (-1) ** (n - 1) * termo / 2 ** (n - 1) * soma_impar
        tot += c
        if abs(c) < 1e-18 * max(1.0, abs(tot)):
            break
    return GAMMA + math.log(L) + math.sqrt(x) * tot


def Li(x):
    return li(x) - li(2.0)


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def main(saida=None):
    partes = []
    for x in (100.0, 1000.0):
        d1 = Li(x) - (x / math.log(x) - 2 / math.log(2) + simpson(lambda t: 1 / math.log(t) ** 2, 2, x))
        d2 = Li(x) * math.log(x) - (x - 2 + simpson(lambda t: Li(t) / t, 2, x, 4000))
        d0 = Li(x) - simpson(lambda t: 1 / math.log(t), 2, x)
        partes.append({"x": x, "Li": Li(x), "dif_simpson": d0, "dif_partes": d1, "dif_log_partes": d2})
    eh = bytearray([1]) * (NMAX + 1)
    eh[0] = eh[1] = 0
    for p in range(2, int(NMAX ** 0.5) + 1):
        if eh[p]:
            eh[p * p::p] = bytearray(len(range(p * p, NMAX + 1, p)))
    tab = []
    pi = 0
    th = 0.0
    mx = 0.0
    for n in range(1, NMAX + 1):
        if eh[n]:
            pi += 1
            th += math.log(n)
        if n >= 2:
            mx = max(mx, abs(th - n) / math.sqrt(n))
        if n in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6):
            d = pi - Li(n)
            tab.append({"x": n, "pi": pi, "Li": Li(n), "pi_menos_Li": d,
                        "razao_sqrt_log": abs(d) / (math.sqrt(n) * math.log(n))})
    res = {"partes": partes, "tabela": tab, "max_theta_sqrt": mx, "schoenfeld": 1 / (8 * math.pi)}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "pi_li.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
