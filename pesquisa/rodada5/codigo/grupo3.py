#!/usr/bin/env python3
"""Companheiro numérico de ATK/XiMomentos, ATK/ProdutoresTN e ATK/JensenPolya (rodada 13, "Grupo 3").

Só biblioteca padrão. Nada aqui é certificado e nada prova HR: é a investigação sugerida — onde a positividade
total dos aₙ de Ξ aparece, onde fica indeterminada pela precisão, e onde as estruturas mais fracas (Hankel, Gram)
falham.

* M1: aₙ = 2∫Φ(u)u²ⁿ/(2n)!du > 0 (`aXi_eq_mom`, `aXi_pos`).
* M2: Cauchy–Schwarz `a_{n+1}²((2n+2)!)² ≤ aₙ(2n)!·a_{n+2}(2n+4)!` (incondicional) e Turán
  `γ(n)γ(n+2) ≤ γ(n+1)²`, γ(k) = k!aₖ (sob HR no kernel; incondicional por Csordas–Norfolk–Varga).
* M3: menores de Toeplitz contíguos det(a_{k+i−j}) com teste de estabilidade do sinal sob perturbação relativa.
* G3.7: hiperbolicidade dos J^{d,n} (Sturm exato nos coeficientes em ponto flutuante).
* Ressalva: μ = (3/2)δ₀ + ½δ₁ tem Hankel positiva e um menor de Toeplitz −7/2880 (`hankel_nao_toeplitz`).
"""
import json
import math
import os
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dbn  # noqa: E402
import edrei  # noqa: E402

NMAX = 14


def coef_xi(nmax=NMAX):
    return [edrei.a_xi(n) for n in range(nmax)]


def det(M):
    M = [list(r) for r in M]
    n, d = len(M), F(1)
    for i in range(n):
        p = next((k for k in range(i, n) if M[k][i] != 0), None)
        if p is None:
            return F(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        for k in range(i + 1, n):
            f = M[k][i] / M[i][i]
            for j in range(i, n):
                M[k][j] -= f * M[i][j]
    return d


def toep(b, i, j):
    return b[i - j] if 0 <= i - j < len(b) else F(0)


def menor_contiguo(a, r, k):
    """det(a_{k+i−j})_{i,j<r} (linhas k..k+r−1, colunas 0..r−1)."""
    b = [F(x) for x in a]
    return det([[toep(b, k + i, j) for j in range(r)] for i in range(r)])


def sinal_estavel(a, r, k, eps=1e-11, amostras=12, semente=0):
    """+1/−1 se o sinal do menor não muda sob perturbação relativa eps dos aₙ; 0 = indeterminado."""
    rng = random.Random(semente + 97 * r + k)
    s0 = menor_contiguo(a, r, k)
    sinais = {(s0 > 0) - (s0 < 0)}
    for _ in range(amostras):
        ap = [x * (1 + eps * (2 * rng.random() - 1)) for x in a]
        d = menor_contiguo(ap, r, k)
        sinais.add((d > 0) - (d < 0))
    return sinais.pop() if len(sinais) == 1 else 0


def jensen(gam, d, n):
    return [F(math.comb(d, j)) * F(gam[n + j]) for j in range(d + 1)]


def main(saida=None):
    a = coef_xi()
    gam = [math.factorial(k) * a[k] for k in range(NMAX)]
    cs = [a[n + 1] ** 2 * math.factorial(2 * n + 2) ** 2 / (a[n] * math.factorial(2 * n) * a[n + 2] *
          math.factorial(2 * n + 4)) for n in range(NMAX - 2)]
    tur = [gam[n + 1] ** 2 / (gam[n] * gam[n + 2]) for n in range(NMAX - 2)]
    menores = {}
    for r in (2, 3, 4, 6, 8):
        menores[str(r)] = [sinal_estavel(a, r, k, eps=1e-12) for k in range(0, NMAX - r)]
    jen = {str(d): [dbn.raizes_reais(jensen(gam, d, n)) for n in range(0, NMAX - d)] for d in (2, 3, 4, 5, 6)}
    bex = [(F(3, 2) * (1 if n == 0 else 0) + F(1, 2)) / math.factorial(2 * n) for n in range(6)]
    mex = det([[toep(bex, i, j) for j in (0, 1, 2)] for i in (1, 2, 3)])
    res = {
        "M1_a_n>0": all(x > 0 for x in a),
        "M1_a_0..3": [format(x, ".12g") for x in a[:4]],
        "M2_CS_razao<=1": [format(x, ".6f") for x in cs],
        "M2_Turan_razao>=1": [format(x, ".6f") for x in tur],
        "M3_sinal_menores_contiguos(+1/0/-1)": menores,
        "G3.7_Jensen_hiperbolico_d=2..6": jen,
        "Hankel_nao_Toeplitz_menor": str(mex),
        "aviso": "verificação finita em ponto flutuante; PF∞(aₙ) e a hiperbolicidade de todos os J^{d,n} são HR "
                 "(OPEN_MATH)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
