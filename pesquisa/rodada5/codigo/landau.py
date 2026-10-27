#!/usr/bin/env python3
"""Companheiro numérico da rodada 36: o lema de Landau (ATK/ZeroClasses/Landau.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

`landau`: se `f` é analítica em `‖z − z₀‖ ≤ R`, `f(z₀) ≠ 0` e `‖f‖ ≤ M‖f(z₀)‖` no disco (`M ≥ 1`), então

  `‖f′/f(z₀) − Σ_{ρ ∈ S} m_ρ/(z₀ − ρ)‖ ≤ 16(log M + 1)/R`,

`S` = zeros em `‖z − z₀‖ ≤ R/4`. Aqui:

* um polinômio com um zero duplo e um simples no disco pequeno e um zero fora (o termo fora entra no erro);
* `f = ζ` em `z₀ = 0,55 + 14,13i`, `R = 1` (o primeiro zero `ρ₁` está a `≈ 0,05` do centro) e em
  `z₀ = 1,1 + γ₁ i`, `R = ½` (nenhum zero a `1/8`: a soma é vazia). `M` é o máximo amostrado de `|f|` no círculo
  de raio `R` (módulo máximo) dividido por `|f(z₀)|`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
G1 = 14.134725141734693


def ld(f, z, h=1e-6):
    return (f(z + h) - f(z - h)) / (2 * h) / f(z)


def caso(f, z0, R, zeros, n=720):
    """`zeros`: lista de (ρ, multiplicidade). Devolve o erro, a cota e os dados."""
    M = max(abs(f(z0 + R * cmath.exp(2j * math.pi * k / n))) for k in range(n)) / abs(f(z0))
    S = [(r, m) for r, m in zeros if abs(r - z0) <= R / 4]
    soma = sum(m / (z0 - r) for r, m in S)
    erro = abs(ld(f, z0) - soma)
    cota = 16 * (math.log(M) + 1) / R
    return {"z0": [z0.real, z0.imag], "R": R, "M": M, "S": [[r.real, r.imag, m] for r, m in S],
            "erro": erro, "cota": cota, "ok": erro <= cota and M >= 1}


def main(saida=None):
    def poli(z):
        return (z - 0.1) ** 2 * (z + 0.2) * (z - 3)

    zs_poli = [(0.1 + 0j, 2), (-0.2 + 0j, 1), (3 + 0j, 1)]
    rho1 = complex(0.5, G1)
    zeros_zeta = [(rho1, 1), (rho1.conjugate(), 1), (complex(0.5, 21.022039638771555), 1)]
    res = {
        "polinomio": caso(poli, 0j, 1.0, zs_poli),
        "zeta_perto_do_zero": caso(zc.zeta, complex(0.55, 14.13), 1.0, zeros_zeta),
        "zeta_reta_um": caso(zc.zeta, complex(1.1, G1), 0.5, zeros_zeta),
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "landau.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(), indent=1, ensure_ascii=False))
