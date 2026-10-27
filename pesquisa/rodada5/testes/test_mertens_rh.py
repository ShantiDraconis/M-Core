"""Testes do companheiro numérico da rodada 51 (ZeroClasses/MertensRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import mertens_rh as mr  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return mr.main(os.path.join(d, "mertens_rh.json"))


def test_G_e_abel():
    # `G_eq_LSeries` em z = 2 e a identidade de `abel`
    out = _out()
    assert abs(out["G2"] - out["inv_zeta2"]) < 1e-8
    assert abs(out["abel"]["lhs"] - out["abel"]["rhs"]) < 1e-9


def test_M_amostra():
    # valores conhecidos de M(N) e |M(N)| < √N na faixa (dado numérico, não critério)
    out = _out()
    assert out["M_amostra"] == {"10": -1, "100": 1, "1000": 2, "10000": -23, "100000": -48}
    assert all(r["max_M_sobre_raiz"] < 1 for r in out["razoes"].values())
