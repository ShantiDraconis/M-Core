#!/usr/bin/env python3
"""Companheiro numérico da rodada 58: `ψ(x) − x` e `M(x)` não são `o(√x)` (ATK/ZeroClasses/OmegaPsi.lean).

Só biblioteca padrão (`ζ` por Euler–Maclaurin, de `zeroclasses.py`). **Nada aqui é certificado.**

* `cota_inf_H`: `(σ − ½)|ζ′/ζ(σ + iγ₁) + ζ(σ + iγ₁)|` para `σ − ½ = 10⁻¹, …, 10⁻⁴` no primeiro zero `γ₁ = 14,1347…`
  — tende a `m = 1` (zero simples);
* `cota_inf_F`: `(σ − ½)|1/ζ(σ + iγ₁)|` — tende a `1/|ζ′(ρ₁)| ≈ 1,26`;
* `psi_nao_o`, `mertens_nao_o` (o lado dos dados): `max |ψ(N) − N|/√N` e `max |M(N)|/√N` por década até `10⁶` —
  não tendem a zero.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 6
GAMMA1 = 14.134725141734693


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
            for k in range(p * p, N + 1, p * p):
                mu[k] = 0
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    mu[0] = 0
    return mu, lam


def main(saida=None):
    polo = []
    h = 1e-7
    for k in range(1, 5):
        d = 10.0 ** (-k)
        s = complex(0.5 + d, GAMMA1)
        z = zc.zeta(s)
        dz = (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h)
        H = -dz / z - z
        polo.append({"sigma_menos_meio": d, "d_vezes_H": d * abs(H), "d_vezes_inv_zeta": d / abs(z)})
    rho = complex(0.5, GAMMA1)
    dz1 = abs((zc.zeta(rho + h) - zc.zeta(rho - h)) / (2 * h))
    mu, lam = tabelas(NMAX)
    psi = 0.0
    m = 0
    dec = []
    a, b = 10, 100
    mx_p = mx_m = 0.0
    for n in range(1, NMAX + 1):
        psi += lam[n]
        m += mu[n]
        if n >= a:
            mx_p = max(mx_p, abs(psi - n) / math.sqrt(n))
            mx_m = max(mx_m, abs(m) / math.sqrt(n))
        if n == b:
            dec.append({"de": a, "ate": b, "max_psi_sqrt": mx_p, "max_M_sqrt": mx_m})
            a, b = b, 10 * b
            mx_p = mx_m = 0.0
    res = {"gamma1": GAMMA1, "abs_dzeta_rho1": dz1, "inv_abs_dzeta_rho1": 1 / dz1, "polo": polo, "decadas": dec}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "omega_psi.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
