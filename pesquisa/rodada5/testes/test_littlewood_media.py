"""Testes do companheiro numérico da rodada 94 (ZeroClasses/LittlewoodMedia.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_media  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_media.main(os.path.join(d, "littlewood_media.json"), ymax=13.0, h=0.002)
    return _C["o"]


def test_media_limitada():
    # `integral_F_log`: ∫₁ʸ F fica limitada em y ≤ 13
    o = _out()
    assert o["max_abs_I"] < 3


def test_cotas_auxiliares():
    # `integral_re_pw_le` e `H_ge`
    o = _out()
    for r in o["re_pw"]:
        assert abs(r["integral"]) <= r["cota"]
    assert o["H_ge_folga_min"] >= -1e-12
