#!/usr/bin/env python3
"""Companheiro numérico da rodada 82: `‖c‖₁` controlado por `‖res‖²_σ` (ATK/ZeroClasses/BDNormaL1.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `media_inf`: para vetores reais pseudoaleatórios `a` (`N = 5, 10, 20`) e `T = 2N(N + 1)`,
  `∫_{−T}^{T} |Σ_k a_k (k+1)^{−iτ}|² dτ` pela forma fechada
  `2TΣa_k² + Σ_{j≠k} a_j a_k · 2 sin(Tμ_{jk})/μ_{jk}`, `μ_{jk} = log((j+1)/(k+1))`, contra a cota
  `(2T − 2N(N+1)) Σ a_k² = 2N(N+1) Σ a_k²`;
* a forma fechada contra quadratura (ponto médio) em `N = 5`, `T = 60`;
* `norma_l1_le`: o expoente `σ + 3/2 + 2η` em `σ = 0,75`, e o teto resultante `κ(σ) ≤ (2σ + 3)(σ − Θ)/Θ`
  (rodada 83) sob RH, `= 2,25` em `σ = 0,75`, contra as inclinações `1,53–1,76` da rodada 75.
"""
import cmath
import json
import math
import os
import random

AQUI = os.path.dirname(os.path.abspath(__file__))


def fechada(a, T):
    n = len(a)
    tot = 2 * T * sum(x * x for x in a)
    for j in range(n):
        for k in range(n):
            if j != k:
                mu = math.log((j + 1) / (k + 1))
                tot += a[j] * a[k] * 2 * math.sin(T * mu) / mu
    return tot


def quadratura(a, T, m=200000):
    h = 2 * T / m
    s = 0.0
    for i in range(m):
        tau = -T + (i + 0.5) * h
        z = sum(x * cmath.exp(-1j * tau * math.log(k + 1)) for k, x in enumerate(a))
        s += abs(z) ** 2
    return s * h


def main(saida=None):
    rng = random.Random(82)
    linhas = []
    for n in (5, 10, 20):
        for _ in range(3):
            a = [rng.uniform(-1, 1) for _ in range(n)]
            T = 2 * n * (n + 1)
            linhas.append({"N": n, "T": T, "integral": fechada(a, T),
                           "cota": (2 * T - 2 * n * (n + 1)) * sum(x * x for x in a)})
    a5 = [rng.uniform(-1, 1) for _ in range(5)]
    conf = {"fechada": fechada(a5, 60.0), "quadratura": quadratura(a5, 60.0)}
    sigma = 0.75
    out = {"media_inf": linhas, "conferencia": conf, "expoente_l1": sigma + 1.5,
           "teto_RH": (2 * sigma + 3) * (sigma - 0.5) / 0.5, "piso_RH": 2 * sigma - 1,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDNormaL1.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_normal1.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
