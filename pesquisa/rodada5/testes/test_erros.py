"""Testes do companheiro numérico de ATK/ErrosGram, ErrosAnaliticos e ErrosConstantes."""
import os
import sys
from decimal import Decimal as D
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import erros  # noqa: E402


def test_E1_partes_e_D1_texto():
    r = erros.e1()
    assert abs(r["G11"] - (r["Ioc_fr2"] + r["cauda"])) < D("1e-40")
    assert D("0.31425") < r["D1texto"] < D("0.31427")
    assert D("0.85821") < r["D1"] < D("0.85822")
    # o D₁ do texto é o mínimo do resíduo local; o resíduo verdadeiro soma x²
    x = r["x_local"]
    assert abs(erros.residuo_local(x) - r["D1texto"]) < D("1e-40")
    for y in (D("0.5"), D("1"), D("1.5"), D("2")):
        assert erros.residuo_local(y) >= r["D1texto"]
        assert abs(erros.residuo(y) - erros.residuo_local(y) - y * y) < D("1e-40")


def test_E2_log2():
    r = erros.e2()
    assert D("0.74212") < r["D1log2"] < D("0.74213")
    assert r["G11_menos_log2"] > 0


def test_E3_b_texto():
    r = erros.e3()
    assert r["primeiro_negativo"] == 4 and r["todos_negativos_de_4"]
    b, lst = r["b_texto"], r["listados_no_texto"]
    assert abs(b[2] - lst[2]) < D("1e-10")
    assert abs(b[3] - lst[3]) > D("8e-5")
    assert abs(b[4] - lst[4]) > D("3e-6")
    for k in range(2, 20):
        h = sum(Fraction(1, j) for j in range(1, k))
        assert abs(erros.b_texto(k) - (erros.b_correto(k) - D(h.numerator) / D(h.denominator) / k)) < D("1e-40")
        assert erros.b_correto(k) > 0


def test_E4_parciais_por_baixo():
    r = erros.e4()
    assert D("0.7722084") < r["G12"] < D("0.7722094")
    vals = [r["parciais"][K] for K in (10, 100, 1000, 10000)]
    assert all(v < r["G12"] for v in vals) and vals == sorted(vals)
    assert r["tabela"] < D("0.7722084")
    # erro ≈ 0,1458/K: o valor tabelado corresponde a K ≈ 1,5·10⁵ (não ~150)
    assert abs(r["erro_vezes_K"][10000] - D("0.1458")) < D("1e-3")
    assert D("140000") < r["K_estimado"] < D("170000")


def test_E9_fator_dois():
    r = erros.e9()
    assert abs(r["dois_int0"] - r["xi_meio"]) < D("1e-15")
    assert abs(r["int0"] - r["xi_meio"]) > D("0.2")
    assert abs(r["dois_int_no_zero"]) < D("1e-15")


def test_E10_regiao_vazia():
    r = erros.e10()
    for T in ("2.5", "3", "3.9"):
        lo, hi = r[T]
        assert lo > hi
    lo, hi = r["5"]
    assert lo < hi


def test_E12_abaixo_de_C0():
    r = erros.e12()
    assert r["p8000"] < r["p256"] < r["C0"]
    assert D("0.988") < r["r256"] < D("0.9885")
    assert D("0.986") < r["r8000"] < D("0.9864")


def test_E13_constantes():
    r = erros.e13()
    assert r["z3_lo"] < D(1) / r["inv_z3"] < r["z3_hi"]
    assert D("0.831907") < r["inv_lo"] and r["inv_hi"] < D("0.8319075") < D("0.831908")
    assert D("19.739208") < r["dois_pi2"] < D("19.739209")
    assert max(r["vol_B2"], r["vol_B3"], r["vol_B4"]) < D(6)
