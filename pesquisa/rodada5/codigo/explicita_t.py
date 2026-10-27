#!/usr/bin/env python3
"""Companheiro numérico da rodada 72: a fórmula explícita com `T → ∞` (ATK/ZeroClasses/ExplicitaT.lean).

Só biblioteca padrão (zeros de `canonico.py`, `ψ` de `explicita_limite.py`). **Nada aqui é certificado.**

* `soma_faixa_le`: a massa dos zeros com `k + 6 < |γ| ≤ k + 7` (os 341 zeros de `0 < γ ≤ 600`, ambos os sinais)
  contra a cota `4 (a₀ + log(k + 9))/l₀`, `a₀ = log 31 + |log(2 − π²/6)|`, `l₀ = log(19/16)`;
* `formula_explicita_T`: `Σ_{|γ|≤T} x^ρ/ρ` em alturas quaisquer (`T = 77,7; 150,2; 333,3; 599,9`) contra
  `x − ψ(N) − log 2π − ½ log(1 − x^{−2})`, `x = 10,5`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import explicita_limite as el  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
A0 = math.log(31) + abs(math.log(2 - math.pi ** 2 / 6))
L0 = math.log(19 / 16)


def main(saida=None):
    g = ca.zeros(T=600.0)
    faixas = []
    for k in range(0, 593):
        massa = 2 * sum(1 for t in g if k + 6 < t <= k + 7)
        faixas.append((k, massa, 4 * (A0 + math.log(k + 9)) / L0))
    pior = max(m / c for _, m, c in faixas)
    N, x = 10, 10.5
    alvo = x - el.psi_cheb(N) - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
    alturas = []
    for T in (77.7, 150.2, 333.3, 599.9):
        soma = sum(2 * (x ** complex(0.5, t) / complex(0.5, t)).real for t in g if t <= T)
        alturas.append({"T": T, "soma": soma, "erro": soma - alvo})
    out = {"a0": A0, "l0": L0, "massa_max_faixa": max(m for _, m, _ in faixas),
           "cota_min_faixa": min(c for _, _, c in faixas), "razao_max": pior,
           "x": x, "alvo": alvo, "alturas": alturas,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/ExplicitaT.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "explicita_t.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
