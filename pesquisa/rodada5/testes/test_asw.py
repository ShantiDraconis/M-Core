"""Testes do companheiro numérico de ATK/ASWReciproca (rodada 9)."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import asw  # noqa: E402
import fechamento  # noqa: E402


def test_inversa():
    p = fechamento.poli_de_raizes(1, [1, 2, 3])
    b = asw.inversa_neg(p, 12)
    q = [c * (-1) ** k for k, c in enumerate(p)]
    for n in range(12):
        s = sum(q[i] * b[n - i] for i in range(min(n, len(q) - 1) + 1))
        assert s == (1 if n == 0 else 0)


def test_cols_iniciais_e_razao():
    p = fechamento.poli_de_raizes(1, [1, 2, 3])
    b = asw.inversa_neg(p, 30)
    assert all(x > 0 for x in b)
    assert asw.menor_cols_iniciais_min(b) >= 0
    r = [b[k + 1] / b[k] for k in range(29)]
    assert all(r[k + 1] <= r[k] for k in range(28))
    assert abs(float(r[-1]) - 1.0) < 1e-6  # L = 1, raiz −1/L = −1


def test_remocao_do_fator():
    p = fechamento.poli_de_raizes(1, [1, 2, 3])
    b1 = asw.remove_fator(asw.inversa_neg(p, 20), F(1))
    assert asw.menor_cols_iniciais_min(b1) >= 0
    # (1 − x)/p(−x) = 1/((2 − x)(3 − x))
    assert b1 == asw.inversa_neg(fechamento.poli_de_raizes(1, [2, 3]), 20)


def test_1_x_x2():
    b = asw.inversa_neg([1, 1, 1], 8)
    assert b[:5] == [1, 1, 0, -1, -1]
    assert asw.menor_cols_iniciais_min(b, rmax=1, linhas=8) < 0
