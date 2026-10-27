#!/usr/bin/env python3
"""Companheiro numérico da rodada 79: o piso `ℓ¹` (ATK/ZeroClasses/BDPisoL1.lean).

Só biblioteca padrão. Lê `dados/bd_taxa.json` (rodada 75). **Nada aqui é certificado.**

* `head0_le`, `J_le`: `∫_0^ε t^{β−1} = ε^β/β` e `∫_ε^1 t^{2(β−σ)−1} ≤ ε^{2(β−σ)}/(2(σ−β))` por quadratura;
* `norm_cN_le`: `‖c_N‖₁ ≤ N` para o molificador de Riesz, `N = 10, …, 160`;
* `piso_L1` com `ρ₁ = ½ + 14,1347i` e `σ = 0,75` (`a = 2(σ − β)/β = 1`): a constante explícita da prova,
  `C = C₀ m₀^a`, e o piso `C/(1 + ‖c_N‖₁)` contra a cota espectral de `‖res_{c_N}‖²_σ` da rodada 75.

As inclinações locais da rodada 75 (`1,53–1,76`) passam do teto assintótico `4σ − 2 = 1` que `taxaL_RH` dá sob RH.
Não há contradição: o piso tem constante `C ≈ 1,6·10⁻⁶` e só morde para `N` muito grande. É a cegueira numérica B2 de
novo: amostras com `N ≤ 160` não medem `κ`.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
GAMMA1 = 14.134725141734693


def moebius(n):
    m, k, p = n, 0, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            k += 1
        p += 1
    if m > 1:
        k += 1
    return -1 if k % 2 else 1


def norma_cN(N):
    return sum(abs(moebius(k)) * max(1 - k / N, 0.0) ** 2 for k in range(1, N + 1))


def constante(beta, gamma, sigma):
    r = 1 / (2 * math.hypot(beta, gamma))
    a = 2 * (sigma - beta) / beta
    m0 = min(1.0, r * beta)
    c0 = min(3 * r * r * (sigma - beta) / 4, (3 * r * (1 - beta) / 8) ** 2 / (2 - 2 * sigma))
    return {"r": r, "a": a, "m0": m0, "C0": c0, "C": c0 * m0 ** a}


def quad(f, a, b, n=200000):
    h = (b - a) / n
    return h * sum(f(a + (j + 0.5) * h) for j in range(n))


def main(saida=None):
    beta, sigma = 0.5, 0.75
    integrais = []
    for eps in (0.5, 0.1, 0.01):
        integrais.append({"eps": eps,
                          "head": quad(lambda t: t ** (beta - 1), 0, eps), "head_formula": eps ** beta / beta,
                          "J": quad(lambda t: t ** (2 * (beta - sigma) - 1), eps, 1),
                          "J_cota": eps ** (2 * (beta - sigma)) / (2 * (sigma - beta))})
    k = constante(beta, GAMMA1, sigma)
    with open(os.path.join(AQUI, "..", "dados", "bd_taxa.json"), encoding="utf-8") as fh:
        taxa = json.load(fh)
    linhas = []
    for row in taxa["cotas"]:
        N = row["N"]
        L = norma_cN(N)
        linhas.append({"N": N, "norma_l1": L, "piso": k["C"] / (1 + L) ** k["a"], "cota_espectral": row["cota"]})
    out = {"sigma": sigma, "rho": [beta, GAMMA1], "constante": k, "integrais": integrais, "molificador": linhas,
           "teto_sob_RH": 4 * sigma - 2, "inclinacoes_r75": taxa["expoentes_locais"],
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDPisoL1.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_piso_l1.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
