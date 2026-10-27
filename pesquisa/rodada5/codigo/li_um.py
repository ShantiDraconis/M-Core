#!/usr/bin/env python3
"""Companheiro numérico da rodada 69: `λ₁ = 1 + γ/2 − ½ log 4π` e RH ⟺ `Σ_ρ 1/|ρ|² = 2 + γ − log 4π`
(ATK/ZeroClasses/LiUm.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `lam_um`, `B_eq`: `λ₁ = 0,0230957…`, `B = −λ₁` contra `ξ′/ξ(0)` por diferença finita de `ξ` (de `encontro.py`);
* `rh_iff_soma_inv_quad`: `Σ_{0<γ≤600} 2/(¼ + γ²)` mais a cauda `2(log(600/2π) + 1)/(2π·600)` contra
  `2 + γ − log 4π = 0,0461914…`;
* `par_eq`: um par fora da reta `ρ = β + iγ`, `1 − ρ` soma `(1 − 2β)²/(|ρ|²|1 − ρ|²) > 0` a mais.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
EULER = 0.5772156649015329
T = 600.0


def main(saida=None):
    lam1 = 1 + EULER / 2 - 0.5 * math.log(4 * math.pi)
    h = 1e-5
    xi0 = en.xi(complex(0, 1e-9)).real
    dxi0 = ((en.xi(complex(h, 0)) - en.xi(complex(-h, 0))) / (2 * h)).real
    B_num = dxi0 / xi0
    g = ca.zeros(T=T)
    soma = sum(2 / (0.25 + t * t) for t in g)
    cauda = 2 * (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
    alvo = 2 + EULER - math.log(4 * math.pi)
    beta, gam = 0.4, 100.0
    par = (1 - 2 * beta) ** 2 / ((beta ** 2 + gam ** 2) * ((1 - beta) ** 2 + gam ** 2))
    out = {"lam1": lam1, "B_formula": -lam1, "B_diferenca_finita": B_num,
           "soma_inv_quad_600": soma, "cauda": cauda, "soma_estimada": soma + cauda, "alvo": alvo,
           "par_fora_da_reta": {"beta": beta, "gamma": gam, "excesso": par},
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LiUm.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "li_um.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
