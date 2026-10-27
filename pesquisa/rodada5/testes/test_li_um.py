"""Testes do companheiro numérico da rodada 69 (ZeroClasses/LiUm.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import li_um  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return li_um.main(os.path.join(d, "li_um.json"))


def test_B_e_lambda1():
    # `B_eq`, `lam_um`: ξ′/ξ(0) por diferença finita = −(1 + γ/2 − ½ log 4π) a 1e-8
    out = _out()
    assert abs(out["B_diferenca_finita"] - out["B_formula"]) < 1e-8
    assert out["lam1"] > 0


def test_soma_inv_quad():
    # `rh_iff_soma_inv_quad` (numérico, sob RH até 600): Σ 1/|ρ|² + cauda bate com 2 + γ − log 4π a 1e-5
    out = _out()
    assert abs(out["soma_estimada"] - out["alvo"]) < 1e-5
    assert out["par_fora_da_reta"]["excesso"] > 0
