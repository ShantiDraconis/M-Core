"""Testes do companheiro numérico da rodada 82 (ZeroClasses/BDNormaL1.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_normal1  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = bd_normal1.main(os.path.join(d, "bd_normal1.json"))
    return _C["o"]


def test_media_inf():
    # `media_inf`: a integral fica acima de (2T − 2N(N+1)) Σ a²
    for r in _out()["media_inf"]:
        assert r["integral"] >= r["cota"] > 0


def test_fechada_quadratura():
    c = _out()["conferencia"]
    assert abs(c["fechada"] - c["quadratura"]) < 1e-4 * abs(c["fechada"])
