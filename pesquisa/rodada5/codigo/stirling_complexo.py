#!/usr/bin/env python3
"""Companheiro numérico da rodada 39: Stirling complexo (ATK/ZeroClasses/StirlingComplexo.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `ell(z) = (z − ½) log z − z + ½ log 2π − Σ_k e_k(z)`, `e_k(z) = 1 − (z + k + ½)(log(z + k + 1) − log(z + k))`
  (soma truncada em `K` termos + cauda `≈ −1/(12(z + K))`);
* `exp_ell`: `exp(ell z)` contra `Γ(z)` de Lanczos (`encontro.gamma`) em vários pontos de `Re z > 0`;
* `norm_ek_le`: `|e_k(z)|·|z + k|² ≤ 2` numa grade;
* `stirling`: `|Σ e_k(z)|` contra `8/|Im z|`;
* `im_ell_quarto`: `Im ell(¼ + iτ) − (τ log τ − τ − π/8)` contra `9/τ`;
* `hasDerivAt_ell`: `ell′` por diferença finita contra `ψ = Γ′/Γ` por diferença finita de `log Γ`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def ek(z, k):
    return 1 - (z + k + 0.5) * (cmath.log(z + k + 1) - cmath.log(z + k))


def EE(z, K=4000):
    return sum(ek(z, k) for k in range(K)) - 1 / (12 * (z + K))


def ell(z):
    return (z - 0.5) * cmath.log(z) - z + 0.5 * math.log(2 * math.pi) - EE(z)


def main(saida=None):
    pts = [complex(0.25, 0.5), complex(1, 0), complex(2, 3), complex(0.5, 10), complex(0.25, 7), complex(3, -5)]
    exp_ell = {}
    for z in pts:
        g = en.gamma(z)
        exp_ell[str(z)] = abs(cmath.exp(ell(z)) - g) / abs(g)
    pior_ek = 0.0
    for a in (0.1, 0.25, 1.0, 3.0):
        for v in (0.0, 0.5, 2.0, 10.0, 100.0):
            for k in range(0, 60):
                w = complex(a, v) + k
                if abs(w) >= 2:
                    pior_ek = max(pior_ek, abs(ek(complex(a, v), k)) * abs(w) ** 2)
    stir = {}
    for v in (2.0, 5.0, 20.0, 100.0):
        z = complex(0.25, v)
        stir[str(v)] = {"abs_EE": abs(EE(z)), "cota": 8 / v}
    quarto = {}
    for tau in (2.0, 5.0, 10.0, 50.0, 200.0):
        val = ell(complex(0.25, tau)).imag - (tau * math.log(tau) - tau - math.pi / 8)
        quarto[str(tau)] = {"erro": val, "cota": 9 / tau, "erro_vezes_tau": val * tau}
    deriv = {}
    for z in (complex(0.5, 1), complex(2, 3), complex(0.25, 7)):
        h = 1e-5
        d_ell = (ell(z + h) - ell(z - h)) / (2 * h)
        d_lg = (cmath.log(en.gamma(z + h) / en.gamma(z - h))) / (2 * h)
        deriv[str(z)] = abs(d_ell - d_lg)
    res = {"exp_ell_erro_relativo": exp_ell, "ek_vezes_w2_max": pior_ek, "stirling": stir,
           "im_ell_quarto": quarto, "derivada_vs_digama": deriv, "ell_1": [ell(1).real, ell(1).imag]}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "stirling_complexo.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
