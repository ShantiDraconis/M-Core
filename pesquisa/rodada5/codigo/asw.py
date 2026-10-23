#!/usr/bin/env python3
"""Companheiro numérico de ATK/ASWReciproca.lean (rodada 9): a recíproca de Aissen–Schoenberg–Whitney.

Só biblioteca padrão (Fraction). Nada aqui é certificado: os teoremas estão no kernel.

Para p(0) > 0, B = 1/p(−x) = Σ b_k x^k. O kernel prova:
* T(coef p) TN ⇒ todos os menores de T(b) com colunas iniciais {0..r−1} são ≥ 0 (Jacobi);
* daí b_k > 0, b_{k+1}/b_k decresce para L > 0 e p(−1/L) = 0;
* (1 − Lx)·B tem de novo menores de colunas iniciais ≥ 0 — indução no grau.
Aqui: exemplos exatos com p = (x+1)(x+2)(x+3) e o contraexemplo 1 + x + x² (b_3 = −1).
"""
import itertools
import json
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fechamento  # noqa: E402


def inversa_neg(p, n):
    """Coeficientes b_0..b_{n−1} de 1/p(−x) (p = lista de coeficientes, p[0] ≠ 0)."""
    q = [F(c) * (-1) ** k for k, c in enumerate(p)]
    b = []
    for k in range(n):
        s = F(1 if k == 0 else 0) - sum(q[i] * b[k - i] for i in range(1, min(k, len(q) - 1) + 1))
        b.append(s / q[0])
    return b


def menor_cols_iniciais_min(b, rmax=3, linhas=10):
    """Mínimo dos menores de T(b) com colunas {0..r−1} e linhas crescentes < `linhas`."""
    T = fechamento.toeplitz(b, linhas)
    m = None
    for r in range(1, rmax + 1):
        for rows in itertools.combinations(range(linhas), r):
            d = fechamento.det([[T[i][j] for j in range(r)] for i in rows])
            m = d if m is None or d < m else m
    return m


def remove_fator(b, L):
    """b′_k = b_k − L·b_{k−1}: coeficientes de (1 − Lx)·B."""
    return [b[k] - (L * b[k - 1] if k else 0) for k in range(len(b))]


def main(saida=None):
    p = fechamento.poli_de_raizes(1, [1, 2, 3])  # (x+1)(x+2)(x+3), raízes −1, −2, −3
    b = inversa_neg(p, 40)
    razoes = [b[k + 1] / b[k] for k in range(39)]
    L = F(1)  # 1/min ρ = 1/1
    b1 = remove_fator(b, L)
    res = {
        "p": [str(c) for c in p],
        "b_0..5": [str(x) for x in b[:6]],
        "razao_b39/b38": format(float(razoes[-1]), ".12g"),
        "razoes_decrescem": all(razoes[k + 1] <= razoes[k] for k in range(38)),
        "menor_min_cols_iniciais_b": str(menor_cols_iniciais_min(b)),
        "menor_min_cols_iniciais_(1-x)b": str(menor_cols_iniciais_min(b1)),
        "p(-1/L)": str(sum(c * F(-1) ** k for k, c in enumerate(p))),
        "b_de_1+x+x2": [str(x) for x in inversa_neg([1, 1, 1], 8)],
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
