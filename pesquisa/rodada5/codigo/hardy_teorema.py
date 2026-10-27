#!/usr/bin/env python3
"""Companheiro numérico da rodada 50: o teorema de Hardy (ATK/ZeroClasses/HardyTeorema.lean).

Só biblioteca padrão (ξ por Lanczos + Euler–Maclaurin, de `encontro.py`). **Nada aqui é certificado.**

* `trocasInfinitas` / `existe_zero_acima`: as trocas de sinal de `Ξ(t) = ξ(1/2 + it)` em `(0, 100]`, numa malha de
  passo `0,01`; são `29`, o valor de `N(100)` (todos os zeros até a altura 100 estão na reta), e as dez primeiras
  caem a `0,01` das ordenadas conhecidas `γ₁, …, γ₁₀`;
* a contagem contra o termo principal de Riemann–von Mangoldt `(T/2π) log(T/2π) − T/2π + 7/8`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
GAMMAS = [14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
          37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478]


def Xi(t):
    return en.xi(complex(0.5, t)).real


def trocas(T, h=0.01):
    out = []
    a, fa = h, Xi(h)
    k = 1
    while a < T:
        b = (k + 1) * h
        fb = Xi(b)
        if fa * fb < 0:
            out.append(round((a + b) / 2, 3))
        a, fa = b, fb
        k += 1
    return out


def main(saida=None):
    tr = trocas(100.0)
    rvm = {str(T): (T / (2 * math.pi)) * math.log(T / (2 * math.pi)) - T / (2 * math.pi) + 7 / 8 for T in (50, 100)}
    cont = {"50": sum(1 for t in tr if t <= 50), "100": len(tr)}
    dif = [abs(a - g) for a, g in zip(tr, GAMMAS)]
    res = {"trocas": tr, "contagem": cont, "rvm_principal": rvm, "dif_gammas": dif}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "hardy_teorema.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
