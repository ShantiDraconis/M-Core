"""Testes do companheiro numérico da rodada 53 (ZeroClasses/ChebyshevSuave.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import chebyshev_suave as cs  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return cs.main(os.path.join(d, "chebyshev_suave.json"))


def test_soma_suave():
    # `chebyshev_suave` (numérico): Ssm(x)/x → 1/2; erro relativo pequeno até 10⁶
    out = _out()
    assert all(r["erro_rel"] < 3e-3 for r in out["tabela"])
    assert out["tabela"][-1]["erro_rel"] < 1e-4


def test_residuo_e_cauda():
    # `phx_one`: K(1) = 1/2; `cauda`: π − 2 arctan T ≤ 2/T
    out = _out()
    assert out["K1"] == 0.5
    assert all(c["pi_menos_2arctan"] <= c["2_T"] for c in out["cauda"])
