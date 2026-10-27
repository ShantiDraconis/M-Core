"""Testes do companheiro numérico da rodada 74 (ZeroClasses/BDDesloc.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_desloc  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_desloc.main(os.path.join(d, "bd_desloc.json"))


def test_desloc():
    # `desloc`: A_N(s) − 1/ζ(s) = (1/2π) ∫ W(−δ+iy) N^{−δ+iy}/ζ(s−δ+iy) dy
    out = _out()
    a = complex(*out["A_menos_inv_zeta"])
    b = complex(*out["integral_deslocada"])
    assert abs(a - b) < 1e-5


def test_cota():
    # `molif_cota`: |A_N − 1/ζ| N^δ fica limitado
    out = _out()
    v = [c["erro_vezes_N_delta"] for c in out["cota"]]
    assert max(v) < 2
    assert out["cota"][-1]["erro"] < out["cota"][0]["erro"]
