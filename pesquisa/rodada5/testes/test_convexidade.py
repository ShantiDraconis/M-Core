"""Testes do companheiro numérico da rodada 86 (ZeroClasses/Convexidade.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import convexidade  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = convexidade.main(os.path.join(d, "convexidade.json"))
    return _C["o"]


def test_jordan_e_peso():
    out = _out()
    assert out["jordan_folga_minima"] >= 0
    assert out["peso_erro_relativo_max"] < 1e-10


def test_convexidade_limitada():
    # `convexidade`: |ζ(σ + it)|/t^{(1−σ)/2} fica limitado em 1 ≤ t ≤ 500
    for r in _out()["convexidade"]:
        assert r["max_razao"] < 5
