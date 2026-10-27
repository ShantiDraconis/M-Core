"""Testes do companheiro numérico da rodada 40 (ZeroClasses/ArgRetangulo.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import arg_retangulo as ar  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return ar.main(os.path.join(d, "arg_retangulo.json"))


def test_bordo_inv():
    # `bordo_inv`: ∮ ds/(s − u) = 2πi dentro, 0 fora
    out = _out()
    v = out["bordo_inv"]
    assert abs(v["(0.3+0.7j)"][1] - 1) < 1e-9 and abs(v["(1.9-0.9j)"][1] - 1) < 1e-9
    assert abs(v["(2.5+1j)"][1]) < 1e-9


def test_principio_argumento():
    # `principio_argumento`: o polinômio tem 3 zeros (com multiplicidade) dentro; ζ tem 3 em [0,1; 0,9] × [10, 30]
    out = _out()
    assert abs(out["contagem_polinomio"][0] - 3) < 1e-6
    assert abs(out["contagem_zeta_10_30"][0] - 3) < 1e-6
