#!/usr/bin/env python3
"""Companheiro numérico da rodada 87: cotas de um lado só (ATK/ZeroClasses/Unilateral.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `integral_escada`: `∫_1^X x^{−s−1} M(⌊x⌋) dx` contra `GA M(s)/s = 1/(s ζ(s))` em `s = 2` (`3/π²`), com cauda
  `≤ X^{−1}`;
* `psi_omega_mais/menos`, `mertens_omega_mais/menos`: `max` e `min` de `(ψ(N) − N)/√(N + 1)` e de `M(N)/√(N + 1)`
  para `100 ≤ N ≤ 10⁶`, e o número de trocas de sinal — as oscilações dos dois lados que os teoremas `Ω±(x^θ)`,
  `θ < Θ`, garantem (a escala `√x` com constante é da rodada seguinte).
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def crivo(n):
    """Möbius e von Mangoldt até `n` por crivo linear."""
    mu = [1] * (n + 1)
    lam = [0.0] * (n + 1)
    primo = bytearray([1]) * (n + 1)
    primo[0] = primo[1] = 0
    mu[0] = 0
    primos = []
    for i in range(2, n + 1):
        if primo[i]:
            primos.append(i)
            mu[i] = -1
        for p in primos:
            if i * p > n:
                break
            primo[i * p] = 0
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    for p in primos:
        lp = math.log(p)
        q = p
        while q <= n:
            lam[q] = lp
            q *= p
    return mu, lam


def main(saida=None, n=10 ** 6):
    mu, lam = crivo(n)
    M = 0
    psi = 0.0
    mmax = (-1e9, 0)
    mmin = (1e9, 0)
    pmax = (-1e9, 0)
    pmin = (1e9, 0)
    trocas_m = 0
    trocas_p = 0
    sinal_m = 0
    sinal_p = 0
    # ∫_1^X x^{-3} M(⌊x⌋) dx = Σ_{k=1}^{X-1} M(k) (k^{-2} − (k+1)^{-2}) / 2
    integral = 0.0
    for k in range(1, n + 1):
        M += mu[k]
        psi += lam[k]
        r = M / math.sqrt(k + 1)
        e = (psi - k) / math.sqrt(k + 1)
        if k >= 100:
            if r > mmax[0]:
                mmax = (r, k)
            if r < mmin[0]:
                mmin = (r, k)
            if e > pmax[0]:
                pmax = (e, k)
            if e < pmin[0]:
                pmin = (e, k)
        sm = (M > 0) - (M < 0)
        if sm and sinal_m and sm != sinal_m:
            trocas_m += 1
        if sm:
            sinal_m = sm
        d = psi - k
        sp = (d > 0) - (d < 0)
        if sp and sinal_p and sp != sinal_p:
            trocas_p += 1
        if sp:
            sinal_p = sp
        if k < n:
            integral += M * (k ** -2.0 - (k + 1) ** -2.0) / 2
    alvo = 3 / math.pi ** 2
    out = {
        "N": n,
        "integral_escada_s2": integral, "alvo_3_sobre_pi2": alvo, "erro_integral": abs(integral - alvo),
        "cota_cauda": 1.0 / n,
        "M_max_sobre_raiz": {"valor": mmax[0], "N": mmax[1]},
        "M_min_sobre_raiz": {"valor": mmin[0], "N": mmin[1]},
        "psi_max_sobre_raiz": {"valor": pmax[0], "N": pmax[1]},
        "psi_min_sobre_raiz": {"valor": pmin[0], "N": pmin[1]},
        "trocas_sinal_M": trocas_m, "trocas_sinal_psi": trocas_p,
        "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/Unilateral.lean",
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "unilateral.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
