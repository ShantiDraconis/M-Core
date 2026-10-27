"""Testes do companheiro numérico da rodada 81 (ZeroClasses/TNPPi.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import tnp_pi  # noqa: E402

_CACHE = {}


def _out():
    if "o" not in _CACHE:
        with tempfile.TemporaryDirectory() as d:
            _CACHE["o"] = tnp_pi.main(os.path.join(d, "tnp_pi.json"))
    return _CACHE["o"]


def test_sqrt_log_e_abel():
    # `sqrt_log_le_V` (forma logarítmica) e `abel_dif` (Abel exato entre primos)
    out = _out()
    assert all(r["folga_minima"] > 0 for r in out["sqrt_log_le_V"])
    for r in out["abel"]:
        assert abs(r["pi"] - r["abel"]) < 1e-6 * r["pi"]


def test_tnp_ordem():
    # `pi_tnp`: |π − Li| fica abaixo de x e^{−½√log x} na faixa calculada
    for r in _out()["tnp"]:
        assert abs(r["pi_menos_Li"]) < r["x_exp"]
