#!/usr/bin/env python3
"""Companheiro numérico da rodada 68: o critério de Li completo (ATK/ZeroClasses/LiCompleto.lean).

Só biblioteca padrão (zeros por Riemann–Siegel, de `canonico.py`). **Nada aqui é certificado.**

* `lam`: `λ_n = Σ_ρ Re(1 − (1 − 1/ρ)^n)` com os 341 zeros de `0 < γ ≤ 600` (pares conjugados) mais a cauda
  `≈ Σ_{γ>600} 2(n/2 + C(n,2))/γ² ≈ n² (log(600/2π) + 1)/(2π·600)` (densidade de Riemann–von Mangoldt);
  `λ_1` contra a forma fechada `1 + γ/2 − ½ log 4π = 0,0230957…` e `λ_2, λ_3` contra os valores publicados
  `0,0923457…`, `0,2076389…`; a assintótica `(n/2)(log n − 1 + γ − log 2π)`;
* `resto_binom`: `|(1 − u)^n − 1 + nu| ≤ n²|u|²(1 + |u|)^n` em amostras;
* `RH_of_lam_nonneg` (ilustração): um zero hipotético fora da reta, `ρ = 0,4 + 14,13i`, faz `Re(1 − w^n)` crescer como
  `−|w|^n cos(n arg w)` — o primeiro `n` com a parcela abaixo de `−10` (com a soma verdadeira, `λ_n` fica
  positivo e cresce como `(n/2) log n`).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
EULER = 0.5772156649015329
T = 600.0


def main(saida=None):
    g = ca.zeros(T=T)
    cauda1 = (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
    lams = []
    for n in range(1, 31):
        s = 0.0
        for t in g:
            rho = complex(0.5, t)
            w = 1 - 1 / rho
            s += 2 * (1 - w ** n).real
        lams.append({"n": n, "lam_600": s, "lam_estimado": s + n * n * cauda1,
                     "assintotico": n / 2 * (math.log(n) - 1 + EULER - math.log(2 * math.pi))})
    fechado = 1 + EULER / 2 - 0.5 * math.log(4 * math.pi)
    # resto binomial
    amostras = []
    for u in (0.1 + 0.05j, -0.2 + 0.3j, 0.01 - 0.07j):
        for n in (1, 5, 20):
            lhs = abs((1 - u) ** n - 1 + n * u)
            rhs = n ** 2 * abs(u) ** 2 * (1 + abs(u)) ** n
            amostras.append({"u": str(u), "n": n, "lhs": lhs, "rhs": rhs})
    # zero hipotético fora da reta
    rho0 = complex(0.4, 14.13)
    w0 = 1 - 1 / rho0
    n_neg = next(n for n in range(1, 10 ** 6) if (1 - w0 ** n).real < -10)
    out = {"lams": lams, "lam1_fechado": fechado, "resto_binom": amostras,
           "hipotetico": {"rho": str(rho0), "abs_w": abs(w0), "primeiro_n_parcela_menor_que_-10": n_neg},
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LiCompleto.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "li_completo.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    for r in o["lams"][:6] + o["lams"][-3:]:
        print(r)
    print(o["lam1_fechado"], o["hipotetico"])
