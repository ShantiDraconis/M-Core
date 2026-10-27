#!/usr/bin/env python3
"""Companheiro numérico da rodada 76: o expoente `Θ = sup Re ρ` (ATK/ZeroClasses/BDTheta.lean).

Só biblioteca padrão. **Nada aqui é certificado — e nada aqui mede `Θ`.**

* os dois instrumentos aritméticos de `Teta_le_iff_psi` / `Teta_le_iff_mertens` em `θ = 0,6`:
  `max_{N ≤ 10⁵} |ψ(N) − N|/(N + 1)^{0,6}` e `max |M(N)|/(N + 1)^{0,6}` — limitados até `10⁵`, como seriam para
  qualquer `Θ` (barreira B2: um zero fora da reta acima de `3·10¹²` não aparece em `N ≤ 10⁵`);
* `|1 − 1/ρ|` (o `w` do critério de Li): `= 1` na reta; para um `ρ` hipotético `0,6 + 100i`, `|w| < 1`, e para
  `1 − ρ`, `|w| > 1` — são os membros com `Re ρ < ½` que fazem `λ_n` crescer em módulo.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 5


def crivo(n):
    mu = [1] * (n + 1)
    lam = [0.0] * (n + 1)
    primo = bytearray([1]) * (n + 1)
    primo[0] = primo[1] = 0
    for p in range(2, n + 1):
        if primo[p]:
            for m in range(2 * p, n + 1, p):
                primo[m] = 0
            for m in range(p, n + 1, p):
                mu[m] = -mu[m]
            q = p * p
            while q <= n:
                for m in range(q, n + 1, q):
                    mu[m] = 0
                q *= p
            q = p
            while q <= n:
                lam[q] = math.log(p)
                q *= p
    return mu, lam


def main(saida=None):
    mu, lam = crivo(NMAX)
    psi = M = 0.0
    rpsi = rM = 0.0
    for n in range(1, NMAX + 1):
        psi += lam[n]
        M += mu[n]
        rpsi = max(rpsi, abs(psi - n) / (n + 1) ** 0.6)
        rM = max(rM, abs(M) / (n + 1) ** 0.6)
    w = lambda r: abs(1 - 1 / r)  # noqa: E731
    out = {"N": NMAX, "theta": 0.6, "razao_psi": rpsi, "razao_mertens": rM,
           "w_reta": w(complex(0.5, 14.134725141734693)), "w_hipotetico": w(complex(0.6, 100)),
           "w_reflexo": w(complex(0.4, 100)),
           "aviso": "numérico; nada aqui é certificado e nada aqui mede Θ — ver ATK/ZeroClasses/BDTheta.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_theta.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
