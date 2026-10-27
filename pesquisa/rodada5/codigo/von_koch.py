#!/usr/bin/env python3
"""Companheiro numérico da rodada 55: `ψ(x) = x + O(x^θ)` ⟹ `ζ ≠ 0` em `Re s > θ` (ATK/ZeroClasses/VonKoch.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`; `ζ′` por diferença central). **Nada aqui é
certificado.**

* `GA_eq_LSeries`, `LSeries_cL`: a série por partes `G(s) = Σ_{n ≥ 0} E(n + 1)((n + 1)^{−s} − (n + 2)^{−s})`, com
  `E(N) = ψ(N) − N`, contra `−ζ′/ζ(s) − ζ(s)` em `s = 1,5; 2; 3`;
* a identidade do princípio da identidade, `(s − 1)ζ₁′(s) = ζ₁(s)(1 − ζ₁(s) − (s − 1)G(s))` com `ζ₁ = (s − 1)ζ`;
* a hipótese de von Koch nos dados: `max |E(N)|/√N` e `max |E(N)|/(√N log²N)` por faixas até `10⁶` (o lado de RH;
  dado finito, sem valor de prova).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def crivo(N):
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    for p in range(2, int(N ** 0.5) + 1):
        if eh[p]:
            eh[p * p::p] = bytearray(len(range(p * p, N + 1, p)))
    return eh


def erros(N):
    eh = crivo(N)
    lam = [0.0] * (N + 1)
    for p in range(2, N + 1):
        if eh[p]:
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    E = [0.0] * (N + 1)
    psi = 0.0
    for n in range(1, N + 1):
        psi += lam[n]
        E[n] = psi - n
    return E


def serie_G(E, s):
    N = len(E) - 1
    tot = 0.0
    for n in range(N - 1):
        tot += E[n + 1] * ((n + 1) ** (-s) - (n + 2) ** (-s))
    return tot


def zeta_real(s):
    return zc.zeta(complex(s, 0)).real


def main(saida=None):
    E = erros(NMAX)
    h = 1e-5
    serie = []
    for s in (1.5, 2.0, 3.0):
        G = serie_G(E, s)
        z = zeta_real(s)
        dz = (zeta_real(s + h) - zeta_real(s - h)) / (2 * h)
        alvo = -dz / z - z
        z1 = (s - 1) * z
        dz1 = ((s + h - 1) * zeta_real(s + h) - (s - h - 1) * zeta_real(s - h)) / (2 * h)
        resid = (s - 1) * dz1 - z1 * (1 - z1 - (s - 1) * G)
        serie.append({"s": s, "G": G, "menos_logderiv_menos_zeta": alvo, "dif": abs(G - alvo),
                      "residuo_identidade": abs(resid)})
    faixas = []
    a = 100
    while a < NMAX:
        b = min(10 * a, NMAX)
        m1 = max(abs(E[n]) / math.sqrt(n) for n in range(a, b + 1))
        m2 = max(abs(E[n]) / (math.sqrt(n) * math.log(n) ** 2) for n in range(a, b + 1))
        faixas.append({"de": a, "ate": b, "max_E_sqrt": m1, "max_E_sqrt_log2": m2})
        a = b
    res = {"serie": serie, "faixas": faixas, "E_1e6": E[NMAX]}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "von_koch.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
