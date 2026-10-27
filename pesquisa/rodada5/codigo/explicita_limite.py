#!/usr/bin/env python3
"""Companheiro numérico da rodada 71: a fórmula explícita de Riemann–von Mangoldt
(ATK/ZeroClasses/ExplicitaLimite.lean).

Só biblioteca padrão (zeros de `canonico.py`, `ζ` de `zeroclasses.py`, `Γ` de `encontro.py`). **Nada aqui é certificado.**

* `norm_tan_le_dois`, `norm_tan_le_um`: `‖tan z‖ ≤ 2` em `|Im z| ≥ 1`; `‖tan(π s/2)‖ = 1` em `Re s = 2K + 3/2`;
* `digamma_hor`: `‖ψ(s)‖ ≤ log(2 + |Im s|) + 11 + Re s/3` numa grade (`ψ` por recorrência + Stirling);
* `logDeriv_esq_le`: a equação funcional `ζ′/ζ(w) = −ζ′/ζ(1 − w) + log 2π − ψ(1 − w) + (π/2) tan(π(1 − w)/2)`
  em pontos de `Re w < 0`;
* `formula_explicita`: `Σ_{|γ|≤T} x^ρ/ρ` contra `x − ψ(N) − log 2π − ½ log(1 − x^{−2})` para `x = 10,5` e
  `x = 30,5`, com `T = 50, 100, 200, 400, 600` (os 341 zeros de `0 < γ ≤ 600`).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
B2 = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6]


def digamma(z):
    """`ψ(z)`, `Re z > 0`: recorrência até `Re z ≥ 12` e a série de Stirling."""
    z = complex(z)
    acc = 0
    while z.real < 12:
        acc -= 1 / z
        z += 1
    s = cmath.log(z) - 1 / (2 * z)
    zz = z * z
    p = zz
    for k, b in enumerate(B2, start=1):
        s -= b / (2 * k * p)
        p *= zz
    return s + acc


def zeta(s):
    """`ζ(s)`: Euler–Maclaurin em `Re s ≥ ½`, a equação funcional em `Re s < ½`."""
    s = complex(s)
    if s.real >= 0.5:
        return zc.zeta(s)
    return 2 * (2 * math.pi) ** (s - 1) * en.gamma(1 - s) * cmath.sin(math.pi * s / 2) * zc.zeta(1 - s)


def dlog_zeta(s, h=1e-5):
    return (zeta(s + h) - zeta(s - h)) / (2 * h) / zeta(s)


def psi_cheb(N):
    tot = 0.0
    for n in range(2, N + 1):
        m, p = n, 2
        while p * p <= m and m % p:
            p += 1
        if p * p > m:
            p = m
        while m % p == 0:
            m //= p
        if m == 1:
            tot += math.log(p)
    return tot


def main(saida=None):
    # tangente
    tan_dois = max(abs(cmath.tan(complex(a / 7, b))) for a in range(-30, 31) for b in (1, -1, 1.5, -3, 8))
    tan_um = [abs(cmath.tan(math.pi * complex(2 * K + 1.5, -y) / 2)) for K in (1, 2, 5) for y in (0, 0.3, 2, 20)]
    # digama
    folga = min(math.log(2 + abs(b)) + 11 + a / 3 - abs(digamma(complex(a, b)))
                for a in (1, 1.5, 3, 10, 40) for b in (3, -3, 6, 50, -400))
    # equação funcional de ζ′/ζ
    fe = []
    for w in (complex(-2.5, 3), complex(-4.5, 0.7), complex(-0.5, 12)):
        lhs = dlog_zeta(w)
        rhs = -dlog_zeta(1 - w) + math.log(2 * math.pi) - digamma(1 - w) + math.pi / 2 * cmath.tan(math.pi * (1 - w) / 2)
        fe.append(abs(lhs - rhs))
    # a fórmula explícita
    g = ca.zeros(T=600.0)
    form = []
    for N in (10, 30):
        x = N + 0.5
        alvo = x - psi_cheb(N) - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
        linha = {"N": N, "x": x, "alvo": alvo, "erros": []}
        for T in (50, 100, 200, 400, 600):
            soma = sum(2 * (x ** complex(0.5, t) / complex(0.5, t)).real for t in g if t <= T)
            linha["erros"].append({"T": T, "soma": soma, "erro": soma - alvo})
        form.append(linha)
    out = {"tan_max_im_ge_1": tan_dois, "tan_reta_esquerda": tan_um, "folga_digamma_hor": folga,
           "eq_funcional_logDeriv": fe, "formula_explicita": form,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaLimite.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_limite.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
