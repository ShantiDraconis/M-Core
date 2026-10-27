#!/usr/bin/env python3
"""Companheiro numérico da rodada 56: RH ⟹ `ψ(x) = x + O(x^{1/2+ε})` (ATK/ZeroClasses/VonKochRH.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`; `ζ′` por diferença central). **Nada aqui é
certificado.**

* `somas_limitadas`, `cota_gen`: as somas parciais `S_N(σ) = Σ_{n ≤ N} (Λ(n) − 1) n^{−σ}` em `σ = 0,8`, contra
  `H(σ) = −ζ′/ζ(σ) − ζ(σ)` (a continuação, holomorfa em `Re s > ½` se RH vale);
* `norm_H_le`: `|H(σ + it)|` em `σ = 0,6; 0,75; 1; 1,5` e `t = 10, 100, 1000`, dividido por `(1 + t)^{0,1}`;
* `norm_cL_le`: `max_n |Λ(n) − 1|/((1/δ + 1) n^δ)` até `10⁶`, para `δ = 0,05; 0,1; 0,25`;
* `psi_of_RH`: `max_{N ≤ 10⁶} |ψ(N) − N|/(N + 1)^{1/2 + ε}` para `ε = 0,05; 0,1; 0,25`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def von_mangoldt(N):
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    for p in range(2, int(N ** 0.5) + 1):
        if eh[p]:
            eh[p * p::p] = bytearray(len(range(p * p, N + 1, p)))
    lam = [0.0] * (N + 1)
    for p in range(2, N + 1):
        if eh[p]:
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def H(s, h=1e-6):
    z = zc.zeta(s)
    dz = (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h)
    return -dz / z - z


def main(saida=None):
    lam = von_mangoldt(NMAX)
    sigma = 0.8
    alvo = H(complex(sigma, 0)).real
    parciais = []
    S = 0.0
    marcas = {10 ** k for k in range(2, 7)}
    for n in range(1, NMAX + 1):
        S += (lam[n] - 1) * n ** (-sigma)
        if n in marcas:
            parciais.append({"N": n, "S_N": S, "dif": abs(S - alvo)})
    crescimento = []
    for sig in (0.6, 0.75, 1.0, 1.5):
        for t in (10.0, 100.0, 1000.0):
            v = abs(H(complex(sig, t)))
            crescimento.append({"sigma": sig, "t": t, "abs_H": v, "razao": v / (1 + t) ** 0.1})
    coef = []
    for d in (0.05, 0.1, 0.25):
        B = 1 / d + 1
        coef.append({"delta": d, "max_razao": max(abs(lam[n] - 1) / (B * n ** d) for n in range(1, NMAX + 1))})
    psi = 0.0
    E = [0.0] * (NMAX + 1)
    for n in range(1, NMAX + 1):
        psi += lam[n]
        E[n] = psi - n
    vk = []
    for eps in (0.05, 0.1, 0.25):
        vk.append({"eps": eps, "max_razao": max(abs(E[n]) / (n + 1) ** (0.5 + eps) for n in range(1, NMAX + 1))})
    res = {"sigma": sigma, "H_sigma": alvo, "parciais": parciais, "crescimento": crescimento,
           "coeficientes": coef, "von_koch": vk}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "von_koch_rh.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
