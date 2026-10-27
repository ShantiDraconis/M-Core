#!/usr/bin/env python3
"""Companheiro numérico da rodada 40: o princípio do argumento em retângulos (ATK/ZeroClasses/ArgRetangulo.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `bordo_inv`: `∮ ds/(s − u) = 2πi` para `u` dentro do retângulo e `0` fora (Simpson nos quatro lados);
* `principio_argumento`: `(1/2πi)∮ f′/f` conta os zeros com multiplicidade. Os testes são um polinômio com um zero
  duplo, um simples e um fora, e `ζ` em `[0,1; 0,9] × [10, 30]`, onde há três zeros (`14,13`, `21,02`, `25,01`).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(a + k * h)
    return s * h / 3


def bordo(g, z, w, n=2000):
    """Convenção da Mathlib: base − topo + i·direito − i·esquerdo."""
    base = simpson(lambda x: g(complex(x, z.imag)), z.real, w.real, n)
    topo = simpson(lambda x: g(complex(x, w.imag)), z.real, w.real, n)
    dire = simpson(lambda y: g(complex(w.real, y)), z.imag, w.imag, n)
    esq = simpson(lambda y: g(complex(z.real, y)), z.imag, w.imag, n)
    return base - topo + 1j * dire - 1j * esq


def main(saida=None):
    z, w = complex(-1, -1), complex(2, 3)
    inv = {}
    for u in (complex(0.3, 0.7), complex(1.9, -0.9), complex(2.5, 1)):
        v = bordo(lambda s, u=u: 1 / (s - u), z, w)
        inv[str(u)] = [v.real, v.imag / (2 * math.pi)]

    def poli(s):
        return (s - 0.2) ** 2 * (s - complex(1, 1)) * (s - 5)

    def dpoli(s, h=1e-6):
        return (poli(s + h) - poli(s - h)) / (2 * h)

    cp = bordo(lambda s: dpoli(s) / poli(s), z, w) / (2j * math.pi)

    def ldz(s, h=1e-6):
        return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)

    cz = bordo(ldz, complex(0.1, 10), complex(0.9, 30), 4000) / (2j * math.pi)
    res = {"bordo_inv": inv, "contagem_polinomio": [cp.real, cp.imag],
           "contagem_zeta_10_30": [cz.real, cz.imag]}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "arg_retangulo.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
