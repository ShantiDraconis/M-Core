#!/usr/bin/env python3
"""Companheiro numérico da rodada 31: Jensen local, `Σ 1/|ρ|² < ∞` e o produto canônico
(ATK/ZeroClasses/JensenLocal.lean, Canonico.lean).

Só biblioteca padrão. **Nada aqui é certificado**: os zeros vêm de trocas de sinal da função Z de Riemann–Siegel
(com o primeiro termo de correção), em ponto flutuante.

* zeros `½ + iγ` com `0 < γ ≤ 300` (malha de passo 0,01 + bissecção) e a contagem contra Riemann–von Mangoldt;
* `N_succ_le`: `N(T + 1) − N(T) ≤ 2·Lc(T + ½)` para `4 ≤ T ≤ 299` (razão máxima, folga);
* `soma_inv_quadrado`: `Σ_{|γ| ≤ T} 1/|ρ|²` + cauda `(log(T/2π) + 1)/(πT)` contra `2 + γ_E − log 4π = 0,046191…`;
* `canonico_converge` / `hadamardXi_iff`: `ξ(s) ≈ e^{A + Bs} ∏_{|γ| ≤ T} (1 − s/ρ)e^{s/ρ}` com `A = −log 2`,
  `B = −γ_E/2 − 1 + ½ log 4π` (os valores clássicos), em `s = 2` e `s = ½ + 2i` — a identidade que falta
  provar (BUILD_PENDING), aqui só conferida numericamente.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
EULER = 0.5772156649015329
B2 = 2 + EULER - math.log(4 * math.pi)  # Σ_ρ 1/(ρ(1−ρ)) = Σ_ρ 1/|ρ|² sob RH
BC = -EULER / 2 - 1 + 0.5 * math.log(4 * math.pi)  # ξ'(0)/ξ(0)


def theta(t):
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def Z(t):
    a = math.sqrt(t / (2 * math.pi))
    N = int(a)
    th = theta(t)
    s = sum(math.cos(th - t * math.log(n)) / math.sqrt(n) for n in range(1, N + 1))
    p = a - N
    c0 = math.cos(2 * math.pi * (p * p - p - 1 / 16)) / math.cos(2 * math.pi * p)
    return 2 * s + (-1) ** (N - 1) * a ** -0.5 * c0


def zeros(T=300.0, h=0.01, t0=10.0):
    out = []
    t, z = t0, Z(t0)
    while t < T:
        t2 = t + h
        z2 = Z(t2)
        if z == 0 or z * z2 < 0:
            lo, hi, flo = t, t2, z
            for _ in range(45):
                mid = (lo + hi) / 2
                fm = Z(mid)
                if (fm > 0) == (flo > 0):
                    lo, flo = mid, fm
                else:
                    hi = mid
            out.append((lo + hi) / 2)
        t, z = t2, z2
    return out


def rvm(T):
    x = T / (2 * math.pi)
    return x * math.log(x) - x + 7 / 8


def Lc(t):
    b = 2 - math.pi ** 2 / 6
    return math.log((15 * t + 62) / b) / math.log(19 / 16)


def main(saida=None):
    g = zeros()
    cont = {T: sum(1 for x in g if x <= T) for T in (50, 100, 150, 200, 250, 300)}
    rv = {T: rvm(T) for T in cont}
    # Jensen local
    pior, folga = 0.0, float("inf")
    for T in range(4, 300):
        d = sum(1 for x in g if T < x <= T + 1)
        c = 2 * Lc(T + 0.5)
        pior = max(pior, d / c)
        folga = min(folga, c - d)
    # Σ 1/|ρ|² (os dois sinais de γ) e a cauda
    parcial = sum(2 / (0.25 + x * x) for x in g)
    Tm = 300.0
    cauda = (math.log(Tm / (2 * math.pi)) + 1) / (math.pi * Tm)
    # o produto canônico em pares (ρ, ρ̄)

    def P(s):
        v = 1 + 0j
        for x in g:
            for r in (complex(0.5, x), complex(0.5, -x)):
                v *= (1 - s / r) * cmath.exp(s / r)
        return v

    prod = {}
    for nome, s in (("2", 2 + 0j), ("1/2+2i", complex(0.5, 2))):
        aprox = cmath.exp(-math.log(2) + BC * s) * P(s)
        exato = en.xi(s)
        prod[nome] = {"xi": [exato.real, exato.imag], "eAB_P": [aprox.real, aprox.imag],
                      "erro_rel": abs(aprox - exato) / abs(exato),
                      "cota_cauda": abs(s) ** 2 * cauda}
    res = {
        "zeros_ate_300": len(g),
        "primeiros": g[:5],
        "contagem": {str(T): {"N": cont[T], "rvm": rv[T]} for T in cont},
        "jensen_local": {"max_razao_N_sobre_2Lc": pior, "folga_minima": folga, "2Lc(4.5)": 2 * Lc(4.5),
                         "2Lc(299.5)": 2 * Lc(299.5)},
        "soma_inv_quadrado": {"parcial_300": parcial, "cauda_estimada": cauda, "parcial_mais_cauda": parcial + cauda,
                              "constante": B2},
        "B": BC,
        "produto_canonico": prod,
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "canonico.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
