#!/usr/bin/env python3
"""Companheiro numérico da rodada 42: Riemann–von Mangoldt (ATK/ZeroClasses/RiemannVonMangoldt.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `riemannVonMangoldt`: `N(T) − m(T)`, `m(T) = (T/2π) log(T/2π) − T/2π`, para `T` até 300, com os zeros de
  `canonico.zeros` (trocas de sinal de `Z(t)`), contra `log T`; a média de `N(T) − m(T) − 7/8` é pequena;
* `formula_N`: `πN(T) = Im E(½ + iT) + arg ζ(2 + iT) − Im ∫_{1/2}^{2} ζ′/ζ(σ + iT) dσ + C₁`, com
  `E(s) = log s + log(s − 1) − (s/2) log π + log Γ(s/2)` (`stirling_complexo.ell`) e `C₁` calculada pela base
  `Im ∫_{1/2}^{2} ξ′/ξ(x + i) dx − Im Λ(2 + i)`;
* `im_E_meio`: `Im E(½ + iT) − ((T/2) log(T/2π) − T/2 + 7π/8)` contra `18/T`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402
import stirling_complexo as sc  # noqa: E402
import variacao_arg as va  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def m(T):
    u = T / (2 * math.pi)
    return u * math.log(u) - u


def E(s):
    return cmath.log(s) + cmath.log(s - 1) - math.log(math.pi) / 2 * s + sc.ell(s / 2)


def g(s, h=1e-6):
    return (en.xi(s + h) - en.xi(s - h)) / (2 * h) / en.xi(s)


def simpson(f, a, b, n=1000):
    hh = (b - a) / n
    tot = f(a) + f(b)
    for k in range(1, n):
        tot += (4 if k % 2 else 2) * f(a + k * hh)
    return tot * hh / 3


def main(saida=None):
    zs = ca.zeros()
    K1 = simpson(lambda x: g(complex(x, 1)), 0.5, 2)
    L21 = E(complex(2, 1)) + cmath.log(zc.zeta(complex(2, 1)))
    C1 = K1.imag - L21.imag
    tab = {}
    desv = []
    for T in (20.5, 37.3, 60.1, 100.7, 150.2, 200.9, 250.4, 299.7):
        N = sum(1 for x in zs if x <= T)
        d = N - m(T)
        desv.append(d - 7 / 8)
        form = (E(complex(0.5, T)).imag + cmath.phase(zc.zeta(complex(2, T))) - va.V(T) + C1) / math.pi
        imE = E(complex(0.5, T)).imag - (T / 2 * math.log(T / (2 * math.pi)) - T / 2 + 7 * math.pi / 8)
        tab[str(T)] = {"N": N, "N_menos_m": d, "razao_log": d / math.log(T), "formula_N": form,
                       "imE_erro": imE, "cota_18_T": 18 / T}
    res = {"C1": C1, "alturas": tab, "media_N_menos_m_menos_7_8": sum(desv) / len(desv)}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "rvm.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
