"""Testes do companheiro numérico de ATK/XiPhi e ATK/ToeplitzTN (rodada 8)."""
import os
import sys
from decimal import Decimal as D
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import fechamento  # noqa: E402


def test_constante_theta_zero():
    th = fechamento.theta_somas()
    assert abs(th["quatroT_menos"]) < D("1e-45")
    assert abs(th["constante"]) < D("1e-45")


def test_tn_raizes_reais():
    assert fechamento.menor_minimo(fechamento.poli_de_raizes(1, [1, 1, 1])) >= 0
    assert fechamento.menor_minimo(fechamento.poli_de_raizes(2, [F(1, 2), 1, 3])) >= 0


def test_1_x_x2_falha():
    assert fechamento.Dtri(1, 1, 1, 3) == -1
    assert fechamento.menor_minimo([1, 1, 1]) < 0


def test_grau_dois_fronteira():
    # a₁² < 4a₀a₂: algum D_r < 0, cada vez mais tarde perto da fronteira
    r1 = fechamento.primeiro_negativo(1, F(19, 10), 1)
    r2 = fechamento.primeiro_negativo(1, F(199, 100), 1)
    assert r1 is not None and r2 is not None and r2 > r1
    # a₁² = 4a₀a₂ (raiz dupla real): todos os D_r = r + 1 > 0
    assert all(fechamento.Dtri(1, 2, 1, r) == r + 1 for r in range(40))
