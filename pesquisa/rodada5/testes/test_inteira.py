"""Testes do companheiro numérico da rodada 32 (CanonicoInteira.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import inteira as it  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return it.main(os.path.join(d, "inteira.json"))


def test_cotas_de_crescimento():
    # `norm_E1_le`, `Pcan_norm_le`: log‖E1‖ ≤ 3‖z‖^{3/2} e log|P| ≤ 3·S·|s|^{3/2} nos círculos
    out = _out()
    assert out["max_logE1_sobre_3r32"] <= 1
    assert 0.3 < out["S_3/2"]["total_estimado"] < 1
    assert all(c["ok"] for c in out["circulos"].values())


def test_zero_simples_e_quociente():
    # `ordem_Pcan`: |P(ρ₁ + h)|/h estabiliza (zero simples); ξ/P é liso perto de ρ₁ e bate com e^{A+Bs}·cauda
    out = _out()
    p = out["perto_rho1"]
    assert abs(p[1]["|P|/h"] - p[2]["|P|/h"]) / p[2]["|P|/h"] < 1e-3
    q1, q2 = complex(*p[1]["xi/P"]), complex(*p[2]["xi/P"])
    assert abs(q1 - q2) < 1e-3
    assert abs(q2 - complex(*out["previsto_com_cauda"])) < 1e-3
