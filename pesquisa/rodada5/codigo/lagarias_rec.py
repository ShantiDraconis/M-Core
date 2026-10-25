#!/usr/bin/env python3
"""Companheiro numérico da rodada 34: as recíprocas de Lagarias e de Sondow–Dumitrescu
(ATK/ZeroClasses/LagariasHadamard.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `logDeriv_xi_eq`: `ξ′/ξ(s)` por diferença finita contra `B + Σ_{|γ| ≤ 300} (1/(s − ρ) + 1/ρ)` mais a cauda
  `≈ s·Σ_{|γ|>300} 1/γ²`;
* `Lg_sob_RH`: `L(s) = Re ξ′/ξ(s)` contra `Σ (σ − ½)/|s − ρ|²` mais a cauda `(σ − ½)·Σ_{|γ|>300} 1/γ²` (os zeros
  conhecidos estão todos na linha), e
  `L(½) = 0`;
* `rec_monotonia`: `|ξ(σ + it)|` amostrado em `½ < σ ≤ 3` para vários `t`, sempre estritamente crescente.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402
import inteira as it  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def ld_xi(s, h=1e-5):
    return (en.xi(s + h) - en.xi(s - h)) / (2 * h) / en.xi(s)


def main(saida=None):
    g = [it.refina(t) for t in ca.zeros()]
    zs = [complex(0.5, x) for x in g] + [complex(0.5, -x) for x in g]
    T = 300.0
    sig = (math.log(T / (2 * math.pi)) + 1) / (math.pi * T)  # Σ_{|γ|>T} 1/γ² (os dois sinais)
    pts = {}
    for nome, s in (("2", 2 + 0j), ("0.8+5i", complex(0.8, 5)), ("0.6+14i", complex(0.6, 14)),
                    ("1.5+30i", complex(1.5, 30))):
        direto = ld_xi(s)
        serie = ca.BC + sum(1 / (s - r) + 1 / r for r in zs) + s * sig
        lsoma = sum((s.real - 0.5) / abs(s - r) ** 2 for r in zs) + (s.real - 0.5) * sig
        pts[nome] = {"logDeriv_direto": [direto.real, direto.imag], "B_mais_serie_cauda": [serie.real, serie.imag],
                     "erro_serie": abs(serie - direto), "L_direto": direto.real, "L_soma_RH_cauda": lsoma,
                     "erro_L": abs(lsoma - direto.real)}
    L_meio = ld_xi(0.5 + 0j).real
    mono = {}
    for t in (0.3, 5.0, 14.134725, 20.0, 50.0):
        vals = [abs(en.xi(complex(0.5 + k * 0.025, t))) for k in range(1, 101)]
        mono[str(t)] = {"crescente": all(b > a for a, b in zip(vals, vals[1:])), "min": vals[0], "max": vals[-1]}
    res = {"pontos": pts, "L(1/2)": L_meio, "monotonia": mono}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "lagarias_rec.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
