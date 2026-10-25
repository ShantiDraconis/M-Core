#!/usr/bin/env python3
"""Companheiro numérico da rodada 37: a região livre de zeros de de la Vallée Poussin
(ATK/ZeroClasses/RegiaoLivre.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `cota_zeta_faixa`: `|ζ(s)| ≤ 3|t| + 12` numa grade de `½ ≤ σ ≤ 3`, `1 ≤ |t| ≤ 100`;
* `cota_zeta_real`: `(σ − 1)|ζ(σ)| ≤ 8` em `1 < σ ≤ 2`;
* `prod341`: `|ζ(σ)|³|ζ(σ + it)|⁴|ζ(σ + 2it)| ≥ 1` numa grade;
* `tres_quatro_um`: `3 Re(−ζ′/ζ)(σ) + 4 Re(−ζ′/ζ)(σ + it) + Re(−ζ′/ζ)(σ + 2it) ≥ 0` (ζ′ por diferença finita) e o
  mínimo da combinação na grade;
* `polo`: `−ζ′/ζ(σ) − 1/(σ − 1)` em `1 < σ ≤ 2` (tende a `−γ_E` quando `σ → 1`);
* `re_logDeriv_local`: a folga entre `−Re ζ′/ζ(σ + it)` e `32(2 log|t| + log(1/(σ − 1)) + 7)`;
* a aritmética da montagem: `σ = 1 + 1/(962 L)`, `3/δ + 1/(2δ) = 3367 = 7·481`, `c = 1/6734`, e a fronteira
  `1 − c/log γ` nas alturas dos zeros conhecidos (todos em `β = ½`).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
G1 = 14.134725141734693


def mld(s, h=1e-6):
    """−ζ′/ζ(s)."""
    return -(zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h) / zc.zeta(s)


def main(saida=None):
    # cota_zeta_faixa
    pior_faixa = 0.0
    for i in range(11):
        sg = 0.5 + 0.25 * i
        for t in [1, 1.5, 2, 3, 5, 8, 14.13, 21, 30, 50, 75, 100]:
            for sgn in (1, -1):
                r = abs(zc.zeta(complex(sg, sgn * t))) / (3 * t + 12)
                pior_faixa = max(pior_faixa, r)
    # cota_zeta_real
    real = {str(sg): (sg - 1) * abs(zc.zeta(sg)) for sg in (1.001, 1.01, 1.1, 1.5, 2.0)}
    # prod341 e tres_quatro_um
    prod_min, comb_min, comb_arg = math.inf, math.inf, None
    for sg in (1.01, 1.05, 1.1, 1.3):
        for k in range(1, 201):
            t = 0.25 * k
            p = abs(zc.zeta(sg)) ** 3 * abs(zc.zeta(complex(sg, t))) ** 4 * abs(zc.zeta(complex(sg, 2 * t)))
            prod_min = min(prod_min, p)
            c = 3 * mld(complex(sg, 0)).real + 4 * mld(complex(sg, t)).real + mld(complex(sg, 2 * t)).real
            if c < comb_min:
                comb_min, comb_arg = c, [sg, t]
    # polo
    polo = {str(sg): mld(complex(sg, 0)).real - 1 / (sg - 1) for sg in (1.001, 1.01, 1.1, 1.5, 2.0)}
    # re_logDeriv_local: razão entre −Re ζ′/ζ e a cota
    folga = 0.0
    for sg in (1.001, 1.01, 1.1, 1.5, 2.0):
        for t in (2, 5, G1, 30, 100):
            cota = 32 * (2 * math.log(t) + math.log(1 / (sg - 1)) + 7)
            folga = max(folga, mld(complex(sg, t)).real / cota)
    # montagem
    delta = 1 / 962
    arit = {"3/delta": 3 / delta, "1/(2 delta)": 1 / (2 * delta), "soma": 3 / delta + 1 / (2 * delta),
            "c": delta / 7, "1/6734": 1 / 6734}
    fronteira = {str(g): 1 - (1 / 6734) / math.log(g) for g in (2, G1, 100, 1e3, 1e6, 1e12)}
    res = {"faixa_pior_razao": pior_faixa, "real_(s-1)zeta": real, "prod341_min": prod_min,
           "comb341_min": comb_min, "comb341_argmin": comb_arg, "polo": polo,
           "local_pior_razao": folga, "aritmetica": arit, "fronteira": fronteira}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "regiao_livre.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
