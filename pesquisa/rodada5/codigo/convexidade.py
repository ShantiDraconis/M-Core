#!/usr/bin/env python3
"""Companheiro numérico da rodada 86: a cota de convexidade (ATK/ZeroClasses/Convexidade.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`). **Nada aqui é certificado.**

* `arg_mul_re_le` (Jordan): `|arg z| · Re z ≤ (π/2)|Im z|` em 2000 pontos pseudoaleatórios com `Re z > 0`;
* `norm_peso`: `|w^{−ℓ}|` contra `|s + 2|^{−(3+δ−σ)/2} e^{−arg w · t/2}` em amostras, `δ = 0,25`;
* `convexidade`: `max_{1 ≤ t ≤ 500} |ζ(σ + it)|/t^{(1−σ)/2}` para `σ = 0,25; 0,5; 0,75` (passo `0,25`), contra a
  cota (sem `δ`); a hipótese de Lindelöf (OPEN_MATH) preveria `|t|^ε`.
"""
import cmath
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None):
    rng = random.Random(86)
    folga = min(math.pi / 2 * abs(z.imag) - abs(cmath.phase(z)) * z.real
                for z in (complex(rng.uniform(1e-3, 10), rng.uniform(-50, 50)) for _ in range(2000)))
    delta = 0.25
    peso = []
    for _ in range(20):
        s = complex(rng.uniform(-delta, 1 + delta), rng.uniform(-60, 60))
        w = -1j * (s + 2)
        ell = (3 + delta - s) / 2
        lhs = abs(w ** (-ell))
        rhs = abs(s + 2) ** (-(3 + delta - s.real) / 2) * math.exp(-cmath.phase(w) * s.imag / 2)
        peso.append(abs(lhs - rhs) / rhs)
    conv = []
    for sigma in (0.25, 0.5, 0.75):
        m = 0.0
        k = 0
        t = 1.0
        while t <= 500:
            m = max(m, abs(zc.zeta(complex(sigma, t))) / t ** ((1 - sigma) / 2))
            t += 0.25
            k += 1
        conv.append({"sigma": sigma, "max_razao": m, "pontos": k})
    out = {"jordan_folga_minima": folga, "peso_erro_relativo_max": max(peso), "convexidade": conv,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/Convexidade.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "convexidade.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
