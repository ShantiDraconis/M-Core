"""Testes do companheiro numérico da rodada 102 (ZeroClasses/PontesRH.lean)."""
import os
import sys
import tempfile
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import pontes_rh  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = pontes_rh.main(os.path.join(d, "pontes_rh.json"), m=30)
    return _C["o"]


def test_gap_exato():
    # o gap entre os centros é exato em ℚ; 9585/5777953 = (71/10000)·ḡ é derivado e difere do gap real
    o = _out()
    assert F(*o["gap_centros"]) == F(166747138007957, 10 ** 17)
    assert F(*o["erro_gap"]) == F(367, 5 * 10 ** 19)
    assert o["mdc_9585_5777953"] == 1
    assert o["u_igual_71e4_vezes_gbar"]
    assert 8e-6 < o["gap_menos_u"] < 9e-6
    assert o["um_e_menos_17_sobre_gap"] < 1e-14


def test_escala_local():
    # s normalizado ≈ 0,00714; S(C₀) ≈ −0,38; contagem esperada na janela ≈ 23 111 813
    o = _out()
    assert 0.0071 < o["s_normalizado"] < 0.0072
    assert -0.4 < o["S_de_C0"] < -0.35
    assert abs(o["zeros_esperados_janela"] - o["zeros_declarados_janela"]) < 1


def test_tautologia_e_mobius():
    o = _out()
    assert F(*o["media_tautologica"]) == F(1, 2)
    assert F(*o["re_abs"]) == F(24970213, 50000000)
    assert o["mobius_tensao_ok"]
    assert F(*o["M_meio"]) == F(-1, 3)
    assert F(*o["theta_graus_71e4"]) == F(-397160, 1119)


def test_gue():
    o = _out()
    assert abs(o["gue_normalizacao"] - 1) < 1e-3
    assert 1.09e-6 < o["gue_P_s_lt_0_01"] < 1.10e-6
    assert 4.9e-5 < o["gue_P_s_gt_3"] < 5.0e-5
