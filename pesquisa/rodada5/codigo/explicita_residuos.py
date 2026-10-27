#!/usr/bin/env python3
"""Companheiro numérico da rodada 70: os resíduos da fórmula explícita no retângulo largo
(ATK/ZeroClasses/ExplicitaResiduos.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin de `zeroclasses.py`). **Nada aqui é certificado.**

* `logDeriv_zeta1_zero`: `ζ₁′/ζ₁(0)` por diferença finita de `ζ₁(s) = (s − 1)ζ(s)` contra `log 2π − 1`;
* `deriv_trivial`: `ζ′(−2k)`, `k = 1..5`, por diferença finita (de `ζ` pela equação funcional) contra a forma fechada
  `(−1)^k (2k)! ζ(2k + 1)/(2(2π)^{2k})` (nunca zero: os zeros triviais são simples);
* `bordo_largo`: `(1/2πi)∮ x^s(−ζ′/ζ)(s)/s ds` no retângulo `[−(2K + ½), 2] × [−20, 20]` (Simpson nos quatro lados)
  contra `x − Σ_{|γ|<20} x^ρ/ρ + Σ_{n<K} x^{−2(n+1)}/(2(n+1)) − log 2π`, para `x = 10,3` e `K = 1, 2`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
G1 = 14.134725141734693


def dlog_zeta(s, h=1e-5):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)


def zeta_neg(s):
    """`ζ(s)` real, `s < 0`, pela equação funcional `ζ(s) = 2(2π)^{s−1} Γ(1 − s) sen(πs/2) ζ(1 − s)`."""
    return 2 * (2 * math.pi) ** (s - 1) * math.gamma(1 - s) * math.sin(math.pi * s / 2) * zc.zeta(1 - s).real


def simpson(f, a, b, n=2000):
    hh = (b - a) / n
    tot = f(a) + f(b)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(a + i * hh)
    return tot * hh / 3


def bordo(g, a, b, c, d):
    """Convenção de `ArgRetangulo.bordo` (anti-horário) em `[a, b] × [c, d]`."""
    inf = simpson(lambda t: g(complex(t, c)), a, b)
    sup = simpson(lambda t: g(complex(t, d)), a, b)
    dir_ = simpson(lambda y: g(complex(b, y)), c, d)
    esq = simpson(lambda y: g(complex(a, y)), c, d)
    return inf - sup + 1j * dir_ - 1j * esq


def main(saida=None):
    h = 1e-5
    z1 = lambda s: (s - 1) * zc.zeta(s)  # noqa: E731
    ld0 = ((z1(h) - z1(-h)) / (2 * h) / z1(0)).real
    triv = []
    for k in range(1, 6):
        num = (zeta_neg(-2 * k + h) - zeta_neg(-2 * k - h)) / (2 * h)
        fech = (-1) ** k * math.factorial(2 * k) * zc.zeta(2 * k + 1).real / (2 * (2 * math.pi) ** (2 * k))
        triv.append({"k": k, "dif_finita": num, "forma_fechada": fech})
    x = 10.3
    F = lambda s: x ** s * (-dlog_zeta(s)) / s  # noqa: E731
    ret = []
    for K in (1, 2):
        I = bordo(F, -(2 * K + 0.5), 2.0, -20.0, 20.0) / (2j * math.pi)
        rho = complex(0.5, G1)
        alvo = x - 2 * (x ** rho / rho).real + sum(x ** (-2 * (n + 1)) / (2 * (n + 1)) for n in range(K)) \
            - math.log(2 * math.pi)
        ret.append({"K": K, "integral_re": I.real, "integral_im": I.imag, "residuos": alvo})
    out = {"logDeriv_zeta1_zero": ld0, "log2pi_menos_1": math.log(2 * math.pi) - 1,
           "zeros_triviais": triv, "x": x, "retangulo_largo": ret,
           "cauda_trivial_K50": sum(x ** (-2 * (n + 1)) / (2 * (n + 1)) for n in range(50)),
           "menos_meio_log": -0.5 * math.log(1 - x ** -2),
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaResiduos.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_residuos.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
