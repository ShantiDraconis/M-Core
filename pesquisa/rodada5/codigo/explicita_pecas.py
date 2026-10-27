#!/usr/bin/env python3
"""Companheiro numérico da rodada 66: as peças da fórmula explícita (ATK/ZeroClasses/ExplicitaPecas.lean).

Só biblioteca padrão (zeros por Riemann–Siegel, de `canonico.py`; `ζ` por Euler–Maclaurin, de `zeroclasses.py`).
**Nada aqui é certificado.**

* `soma_ordem_norm`: `Σ_{|γ| ≤ T} 1/|ρ|` (os dois sinais) contra `(1 + log T)²`, `T ≤ 600`;
* `separa`/`altura_boa`: o algoritmo da prova (candidatos `T₀ + k/(n + 1)`) em `T₀ = 100, 200, 300, 400`; a
  separação obtida, `δ(n + 1) ≥ ½`, e `|ζ′/ζ(σ ± iT)|/log²(2 + T)` em `σ = ¼, ½, 1, 2`;
* `logDeriv_quarto_RH`: `max |ζ′/ζ(¼ + it)|/log(2 + |t|)` em `t ∈ [0, 300]`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def logderiv(s, h=1e-5):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)


def main(saida=None):
    g = ca.zeros(T=600.0)
    soma = []
    for T in (50.0, 100.0, 200.0, 400.0, 600.0):
        S = sum(2 / math.hypot(0.5, x) for x in g if x <= T)
        soma.append({"T": T, "soma": S, "razao": S / (1 + math.log(T)) ** 2})
    alturas = []
    for T0 in (100.0, 200.0, 300.0, 400.0):
        W = [x for x in g if T0 - 1 <= x <= T0 + 2]
        n = len(W)
        delta = 1 / (2 * (n + 1))
        T = None
        for k in range(n + 1):
            t = T0 + k / (n + 1)
            if all(abs(t - x) >= delta for x in W):
                T = t
                break
        sep = min(abs(T - x) for x in g)
        vals = {}
        for sig in (0.25, 0.5, 1.0, 2.0):
            v = max(abs(logderiv(complex(sig, T))), abs(logderiv(complex(sig, -T))))
            vals[str(sig)] = v / math.log(2 + T) ** 2
        alturas.append({"T0": T0, "n": n, "T": T, "delta": delta, "separacao": sep, "razoes": vals})
    m = 0.0
    t = 0.0
    while t <= 300.0:
        m = max(m, abs(logderiv(complex(0.25, t))) / math.log(2 + t))
        t += 0.25
    out = {"soma_ordem_norm": soma, "alturas": alturas, "quarto_max": m,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaPecas.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_pecas.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    for r in o["soma_ordem_norm"]:
        print(r)
    for r in o["alturas"]:
        print(r)
    print(o["quarto_max"])
