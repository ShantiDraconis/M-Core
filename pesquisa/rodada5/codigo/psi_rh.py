#!/usr/bin/env python3
"""Companheiro numérico da rodada 64: RH ⟺ `ψ(x) = x + O(√x log³ x)` (ATK/ZeroClasses/PsiRH.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `psi_RH`: `max |ψ(x) − x|/(√x log³ x)` e `max |ψ(x) − x|/(√x log² x)` em cada década `10^{k−1} < x ≤ 10^k`, `k = 2…7`,
  contra a cota explícita de Schoenfeld (1976, sob RH) `|ψ(x) − x| < √x log² x/(8π)` para `x ≥ 73,2`;
* `norm_fL_le`: `η Λ(n) n^{−η} ≤ 1` para `η = 1/log x` (os coeficientes de Perron);
* `integral_um_abs`: `∫_{−T}^{T} dy/(1 + |y|) = 2 log(1 + T)` por quadratura.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
NMAX = 10 ** 7


def vonmangoldt(N):
    lam = [0.0] * (N + 1)
    eh = bytearray([1]) * (N + 1)
    eh[0] = eh[1] = 0
    for p in range(2, N + 1):
        if eh[p]:
            for m in range(p * p, N + 1, p):
                eh[m] = 0
            lp = math.log(p)
            q = p
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def main(saida=None, N=NMAX):
    lam = vonmangoldt(N)
    psi = 0.0
    blocos = []
    k = 2
    m3 = m2 = sch = 0.0
    for n in range(1, N + 1):
        psi += lam[n]
        if n >= 74:
            for x in (n, n + 1 - 1e-9):  # ψ é constante em [n, n + 1)
                e = abs(psi - x)
                r = math.sqrt(x) * math.log(x)
                m3 = max(m3, e / (r * math.log(x) ** 2))
                m2 = max(m2, e / (r * math.log(x)))
                sch = max(sch, e / (r * math.log(x) / (8 * math.pi)))
        if n == 10 ** k:
            blocos.append({"x": n, "psi-x": psi - n, "max_log3": m3, "max_log2": m2, "max_schoenfeld": sch})
            m3 = m2 = sch = 0.0
            k += 1
    eta = 1 / math.log(N)
    fL_max = max(eta * lam[n] * n ** (-eta) for n in range(2, 10 ** 5))
    T = 1000.0
    h = 0.001
    quad = sum(h / (1 + abs(-T + (j + 0.5) * h)) for j in range(int(2 * T / h)))
    out = {"blocos": blocos, "fL_max": fL_max, "integral_um_abs": {"T": T, "quadratura": quad,
           "formula": 2 * math.log(1 + T)},
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PsiRH.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "psi_rh.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    for b in o["blocos"]:
        print(b)
    print(o["fL_max"], o["integral_um_abs"])
