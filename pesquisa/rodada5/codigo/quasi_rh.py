#!/usr/bin/env python3
"""Companheiro numérico da rodada 57: quasi-RH ⟺ cotas de `ψ` e de `M` (ATK/ZeroClasses/QuasiRH.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`). **Nada aqui é certificado**, e nenhum dado
finito decide `SemZeros θ`.

* `psi_of_semZeros`, `mertens_of_semZeros` (o lado "cota"): `max_{N ≤ 10⁶} |ψ(N) − N|/(N + 1)^θ` e
  `max_{N ≤ 10⁶} |M(N)|/(N + 1)^θ` para `θ = 0,5; 0,6; 0,75; 0,9` — todos limitados, como em RH;
* `somas_limitadas_gen` com `a = μ` (o deslocamento): `Σ_{n ≤ N} μ(n)n^{−0,8}` contra `1/ζ(0,8)`;
* `norm_F_le`: `|1/ζ(σ + it)|` em `σ = 0,6; 0,75` e `t = 10, 100, 1000`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6


def tabelas(N):
    mu = [1] * (N + 1)
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    lam = [0.0] * (N + 1)
    for p in range(2, N + 1):
        if eh[p]:
            for k in range(2 * p, N + 1, p):
                eh[k] = 0
            for k in range(p, N + 1, p):
                mu[k] = -mu[k]
            pp = p * p
            for k in range(pp, N + 1, pp):
                mu[k] = 0
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    mu[0] = 0
    return mu, lam


def main(saida=None):
    mu, lam = tabelas(NMAX)
    E = [0.0] * (NMAX + 1)
    M = [0] * (NMAX + 1)
    psi = 0.0
    m = 0
    for n in range(1, NMAX + 1):
        psi += lam[n]
        m += mu[n]
        E[n] = psi - n
        M[n] = m
    cotas = []
    for th in (0.5, 0.6, 0.75, 0.9):
        cotas.append({"theta": th,
                      "max_psi": max(abs(E[n]) / (n + 1) ** th for n in range(1, NMAX + 1)),
                      "max_M": max(abs(M[n]) / (n + 1) ** th for n in range(1, NMAX + 1))})
    sigma = 0.8
    alvo = 1 / zc.zeta(complex(sigma, 0)).real
    parciais = []
    S = 0.0
    marcas = {10 ** k for k in range(2, 7)}
    for n in range(1, NMAX + 1):
        if mu[n]:
            S += mu[n] * n ** (-sigma)
        if n in marcas:
            parciais.append({"N": n, "S_N": S, "dif": abs(S - alvo)})
    inv = []
    for sig in (0.6, 0.75):
        for t in (10.0, 100.0, 1000.0):
            inv.append({"sigma": sig, "t": t, "abs_inv_zeta": 1 / abs(zc.zeta(complex(sig, t)))})
    res = {"cotas": cotas, "sigma": sigma, "inv_zeta_sigma": alvo, "parciais_mu": parciais, "inv_zeta": inv,
           "M_1e6": M[NMAX], "E_1e6": E[NMAX]}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "quasi_rh.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
