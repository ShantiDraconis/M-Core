"""Testes do companheiro numérico de ATK/ZeroClasses/Pontes (rodada 24)."""
import itertools
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import pontes as po  # noqa: E402

EX1 = [[(0, True), (1, True)], [(0, False), (1, True)], [(0, True), (1, False)]]
EX2 = [[(0, True)], [(0, False)]]


def test_exemplos():
    # `exemplo_um`, `exemplo_zero`: Z = t(1+t)³ e (1+t)²
    assert po.analisa(EX1, 2)["N"] == 1
    assert po.poly_prod([po.R(EX1, x) for x in itertools.product((False, True), repeat=2)]) == [0, 1, 3, 3, 1]
    assert po.analisa(EX2, 1)["N"] == 0
    assert po.poly_prod([po.R(EX2, x) for x in ((False,), (True,))]) == [1, 2, 1]


def test_ordem_det_posto():
    # `ordem_Zpol`, `det_diag_zero_iff`, `posto_mais_nucleo`
    random.seed(7)
    for _ in range(60):
        n = random.randint(1, 6)
        phi = [[(random.randrange(n), random.random() < 0.5) for _ in range(2)] for _ in range(random.randint(1, 12))]
        a = po.analisa(phi, n)
        assert a["ord0"] == a["N"] and (a["det"] == 0) == (a["N"] > 0) and a["posto+N"] == 2 ** n


def test_T2_recupera():
    # `Fger_zero`, `Fger_aprox`, `recupera_contagem`
    random.seed(8)
    for _ in range(60):
        n = random.randint(1, 6)
        phi = [[(random.randrange(n), random.random() < 0.5) for _ in range(3)] for _ in range(random.randint(1, 15))]
        a = po.analisa(phi, n)
        assert 0 <= a["F(z)-N"] <= a["cota 2^n z"] <= 0.25 and a["arredonda"]


def test_B1_e_Q():
    # `B1_divisibilidade`, `sat_iff_raiz_real` (pontos booleanos)
    a = po.analisa(EX1, 2)
    assert a["B1"] and a["Q_bool_zero_iff_sat"]
    assert po.Q(EX1, [1, 1]) == 0 and po.Q(EX1, [0.5, 0.5]) > 0
