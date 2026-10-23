"""Testes do companheiro numérico de ATK/GamaCotas, GramExato, GramDois, BarreiraModelos, ZeroSegundo/Terceiro."""
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import gram2  # noqa: E402


def test_gama_cercado():
    assert gram2.l(39) < gram2.GAMMA < gram2.u(40)
    assert D("0.5772156") < gram2.l(39) and gram2.u(40) < D("0.5772163")


def test_sequencias_monotonas():
    us = [gram2.u(n) for n in range(0, 30)]
    ls = [gram2.l(n) for n in range(0, 30)]
    assert all(us[i + 1] <= us[i] for i in range(len(us) - 1))
    assert all(ls[i] <= ls[i + 1] for i in range(len(ls) - 1))


def test_G11_e_G12():
    G = gram2.gram()
    assert abs(G["G11"] - D("1.2606614015078126")) < D("1e-15")
    assert abs(G["G12"] - D("0.7722092559908731")) < D("1e-15")


def test_pares_forma_fechada_igual_soma_de_degraus():
    for K in (1, 3, 7, 12):
        assert abs(gram2.passos12(2 * K) - gram2.Pc(K)) < D("1e-40")


def test_pares_convergem_para_G12():
    G = gram2.gram()["G12"]
    e1 = G - (gram2.Pc(250) + D(1) / 2)
    e2 = G - (gram2.Pc(1000) + D(1) / 2)
    assert 0 < e2 < e1 and abs(e2 * 1000 - D("0.1458")) < D("1e-3")


def test_D1_D2_e_D_infinito():
    G = gram2.gram()
    assert D("0.85821") < G["D1"] < D("0.85822")
    assert D("0.2899") < G["D2"] < D("0.2900")
    assert G["det"] > 0
    assert G["D2"] < D("0.29670246")


def test_C0():
    c0 = 2 + gram2.GAMMA - (4 * gram2.PI).ln()
    assert D("0.04619") < c0 < D("0.04620")


def test_ajuste_intercepto_negativo():
    r = gram2.ajuste()
    assert r["produto_8000"] < r["produto_256"]
    assert D("-2.92e-5") < r["intercepto"] < D("-2.90e-5")


def test_tabela_barreira():
    assert D("0.000998") < gram2.barreira("0.6", "14.134725") < D("0.000999")
    assert D("0.002489") < gram2.barreira("0.75", "14.134725") < D("0.002490")
    assert D("0.003972") < gram2.barreira("0.9", "14.134725") < D("0.003973")


def test_segundo_e_terceiro_zeros():
    z2, z3 = gram2.zeros_theta()
    assert abs(z2 - D("21.0220396388")) < D("1e-6")
    assert abs(z3 - D("25.0108575801")) < D("1e-6")
