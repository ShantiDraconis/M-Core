#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Forcar (rodada 23): o que se força, e onde.

Só biblioteca padrão. **Nada aqui é certificado.**

* o quarteto P(s) = ((s − ½)² − δ² + T²)² + 4T²δ² = Q δ T: identidade, zeros ½ ± δ ± iT, simetrias;
* Ξ_λ = ξ + λP: no zero ρ de P, Ξ_λ(ρ) = ξ(ρ) para todo λ;
* o certificado de módulo mínimo `2|f(c)| + L·r < r|f′(c)|` nos exemplos (linear, quadrático, contraexemplo) e
  em ζ: discos em torno dos zeros 1–5 da linha **passam** (L amostrado); discos fora da linha numa malha
  0,6 ≤ σ ≤ 0,9, 10 ≤ t ≤ 50 **falham** todos (como deve ser numa região sem zeros);
* o que o certificado exigiria no ponto gigante: |ζ(c)| < r|ζ′(c)|/2 com r = δ/2 ≈ 2,5·10⁻¹⁰⁰¹;
* SAT: R_φ(x) = Σ q_C(x), q_C = ∏(1 − ℓ); lacuna R < 1 ⟹ R = 0, em fórmulas 3-SAT aleatórias pequenas;
* zero assintótico: (log n)²/n → 0, mas n^{log n} passa C·nᵏ.
"""
import cmath
import itertools
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402
import encontro as en  # noqa: E402


def Pq(d, T, s):
    w = s - 0.5
    return (w * w - d * d + T * T) ** 2 + 4 * T * T * d * d


def Q(d, T, s):
    return ((s - 0.5 - d) ** 2 + T * T) * ((s - 0.5 + d) ** 2 + T * T)


def dz(f, s, h=1e-6):
    return (f(s + h) - f(s - h)) / (2 * h)


def certificado(f, c, r, amostras=24, aneis=3):
    """Teste `2|f(c)| + L·r < r|f′(c)|` com L = max|f′(z) − f′(c)| amostrado no disco (heurístico)."""
    d0 = dz(f, c)
    L = 0.0
    for a in range(1, aneis + 1):
        for k in range(amostras):
            z = c + r * a / aneis * cmath.exp(2j * math.pi * k / amostras)
            L = max(L, abs(dz(f, z) - d0))
    esq, dir_ = 2 * abs(f(c)) + L * r, r * abs(d0)
    return {"2|f(c)|+L*r": esq, "r|f'(c)|": dir_, "passa": esq < dir_}


def viol(x, C):
    p = 1
    for (i, pol) in C:
        p *= 0 if (x[i] == pol) else 1
    return p


def R(phi, x):
    return sum(viol(x, C) for C in phi)


def main(saida=None):
    res = {}
    d, T = 0.1, 7.0
    s = complex(0.3, 2.0)
    zeros = [complex(0.5 + e * d, f * T) for e in (1, -1) for f in (1, -1)]
    res["quarteto"] = {"|Pq-Q|": abs(Pq(d, T, s) - Q(d, T, s)), "max|Pq(zero)|": max(abs(Pq(d, T, z)) for z in zeros),
                       "|Pq(1-s)-Pq(s)|": abs(Pq(d, T, 1 - s) - Pq(d, T, s)),
                       "|Pq(conj s)-conj Pq(s)|": abs(Pq(d, T, s.conjugate()) - Pq(d, T, s).conjugate())}
    rho = complex(0.5 + d, T)
    res["somar_nao_forca"] = {"xi(rho)": abs(en.xi(rho)),
                              "Xi_lambda(rho) para lambda=1,10,1e6": [abs(en.xi(rho) + l * Pq(d, T, rho))
                                                                      for l in (1, 10, 1e6)]}
    c = complex(0.75, 10)
    lin = lambda z: z - complex(0.8, 10)  # noqa: E731
    quad = lambda z: (z - c) + 0.25 * (z - c) ** 2 + 0.05  # noqa: E731
    cont = lambda z: 1 + (z - c)  # noqa: E731
    w = -2 + math.sqrt(95) / 5
    res["exemplos"] = {"linear": certificado(lin, c, 1 / 8), "quadratico": certificado(quad, c, 1 / 8),
                       "zero_quadratico": [(c + w).real, (c + w).imag], "contraexemplo": certificado(cont, c, 1 / 8)}
    # ζ: discos em torno de zeros da linha (passam) e discos fora da linha (falham)
    linha = []
    for g in en.GAMMAS:
        r0 = zc.zero_newton(complex(0.5, g))
        cc = r0 + complex(2e-4, -1e-4)
        linha.append({"gamma": r0.imag, **certificado(zc.zeta, cc, 1e-3)})
    res["zeta_discos_linha"] = linha
    fora = {"discos": 0, "passam": 0}
    for sig in (0.6, 0.7, 0.8, 0.9):
        for t in range(10, 51):
            r = min(0.05, abs(sig - 0.5) / 2)
            out = certificado(zc.zeta, complex(sig, t), r, amostras=12, aneis=2)
            fora["discos"] += 1
            fora["passam"] += out["passa"]
    res["zeta_discos_fora"] = fora
    res["gigante"] = {"r=delta/2": "≈ 2,5·10⁻¹⁰⁰¹",
                      "exigencia": "|ζ(c)| < r|ζ′(c)|/2 − L·r/2; ζ em 10¹⁰⁰ não é avaliável (≈ 4·10⁴⁹ termos)"}
    # SAT
    random.seed(23)
    sat = {"formulas": 0, "satisfativeis": 0, "lacuna_ok": True}
    for _ in range(200):
        n, m = 6, random.randint(5, 40)
        phi = [[(random.randrange(n), random.random() < 0.5) for _ in range(3)] for _ in range(m)]
        vals = [R(phi, x) for x in itertools.product((False, True), repeat=n)]
        sat["formulas"] += 1
        sat["satisfativeis"] += min(vals) == 0
        sat["lacuna_ok"] &= all(v == 0 or v >= 1 for v in vals) and all(isinstance(v, int) for v in vals)
    res["sat"] = sat
    res["sat_exemplos"] = {"(x0 ∨ ¬x1)": min(R([[(0, True), (1, False)]], x)
                                           for x in itertools.product((False, True), repeat=2)),
                           "x0 ∧ ¬x0": min(R([[(0, True)], [(0, False)]], x) for x in ((False,), (True,)))}
    res["quase_polinomial"] = {"(log n)^2/n em n=10^k": {str(k): (k * math.log(10)) ** 2 / 10 ** k for k in (2, 4, 8, 16)},
                               "log(n^{log n}) - log(n^3) em n=e^5": 5 * 5 - 3 * 5}
    res["aviso"] = "ponto flutuante e L amostrado; o kernel prova os critérios (Forcar.lean), não estes números"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
