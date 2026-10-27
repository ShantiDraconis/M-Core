"""Testes do companheiro numérico da rodada 76 (ZeroClasses/BDTheta.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_theta  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_theta.main(os.path.join(d, "bd_theta.json"))


def test_instrumentos():
    # `Teta_le_iff_psi`, `Teta_le_iff_mertens`: razões limitadas até 10⁵ (compatível com qualquer Θ ≤ 0,6)
    out = _out()
    assert out["razao_psi"] < 5
    assert out["razao_mertens"] < 5


def test_w():
    # `w = 1 − 1/ρ`: |w| = 1 na reta, < 1 em Re ρ > ½, > 1 em Re ρ < ½
    out = _out()
    assert abs(out["w_reta"] - 1) < 1e-12
    assert out["w_hipotetico"] < 1 < out["w_reflexo"]
