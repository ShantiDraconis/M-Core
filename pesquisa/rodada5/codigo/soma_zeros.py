#!/usr/bin/env python3
"""Companheiro numérico da rodada 63: a soma sobre os zeros e `ζ′/ζ` local (ATK/ZeroClasses/SomaZeros.lean).

Só biblioteca padrão (zeros por Riemann–Siegel, de `canonico.py`; `ζ` por Euler–Maclaurin, de `zeroclasses.py`).
**Nada aqui é certificado.**

* `soma_wz_O`: `S(t) = Σ_ρ 1/(1 + (t − γ)²)` (zeros com `0 < γ ≤ 600`, os dois sinais) contra `log t`; o valor
  esperado é `≈ ½ log(t/2π)` (densidade `(1/2π) log(t/2π)` vezes `∫ du/(1 + u²) = π`);
* `card_perto_O`: `#{ρ : |γ − t| ≤ 1}` contra `log t`;
* `zeta_local`: `|ζ′/ζ(s) − Σ_{|γ − t| ≤ 1} 1/(s − ρ)|/log t` em `σ = 0,6; 1; 1,5; 2`;
* `norm_digamma_le`: `|ψ(z)| ≤ log(2 + |Im z|) + 11` em `Re z ∈ {0,05; 0,5; 1}`, `Im z ∈ {3, 30, 300}`;
* `logDeriv_RH`: `(σ − ½)|ζ′/ζ(σ + it)|/log t` limitado quando `σ → ½⁺` (aqui `t = 100`, sem zero em `t`).
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
TMAX = 600.0


def digamma(z, N=60):
    """ψ(z) = log(z + N) − 1/(2(z + N)) − 1/(12(z + N)²) − Σ_{k < N} 1/(z + k)."""
    w = z + N
    return cmath.log(w) - 1 / (2 * w) - 1 / (12 * w * w) - sum(1 / (z + k) for k in range(N))


def logderiv(s, h=1e-5):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)


def main(saida=None):
    g = ca.zeros(T=TMAX)
    soma = []
    for t in (50.0, 100.0, 200.0, 300.0, 400.0):
        S = sum(1 / (1 + (t - x) ** 2) + 1 / (1 + (t + x) ** 2) for x in g)
        n = sum(1 for x in g if abs(x - t) <= 1)
        soma.append({"t": t, "S": S, "S/log t": S / math.log(t), "esperado": 0.5 * math.log(t / (2 * math.pi)),
                     "perto": n, "perto/log t": n / math.log(t)})
    local = []
    for t in (50.0, 100.0, 200.0):
        perto = [complex(0.5, x) for x in g if abs(x - t) <= 1] + [complex(0.5, -x) for x in g if abs(-x - t) <= 1]
        for sig in (0.6, 1.0, 1.5, 2.0):
            s = complex(sig, t)
            r = logderiv(s) - sum(1 / (s - p) for p in perto)
            local.append({"t": t, "sigma": sig, "resto": abs(r), "resto/log t": abs(r) / math.log(t)})
    dig = []
    for a in (0.05, 0.5, 1.0):
        for b in (3.0, 30.0, 300.0):
            z = complex(a, b)
            v = abs(digamma(z))
            dig.append({"z": str(z), "|psi|": v, "cota": math.log(2 + b) + 11})
    rh = []
    t = 100.0
    for d in (0.5, 0.1, 0.01, 0.001):
        s = complex(0.5 + d, t)
        rh.append({"sigma-1/2": d, "(sigma-1/2)|zeta'/zeta|/log t": d * abs(logderiv(s)) / math.log(t)})
    out = {"n_zeros": len(g), "soma_wz": soma, "zeta_local": local, "digamma": dig, "logDeriv_RH": rh,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/SomaZeros.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "soma_zeros.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    print(o["n_zeros"])
    for r in o["soma_wz"]:
        print(r)
    for r in o["zeta_local"]:
        print(r)
    for r in o["digamma"]:
        print(r)
    for r in o["logDeriv_RH"]:
        print(r)
