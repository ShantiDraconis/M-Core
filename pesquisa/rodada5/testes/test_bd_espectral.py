"""Testes do companheiro numérico da rodada 73 (ZeroClasses/BDEspectral.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_espectral  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_espectral.main(os.path.join(d, "bd_espectral.json"))


def test_riesz():
    # `hasMellin_wR`, `wR_inv`, `LSeries_aN_int`
    out = _out()
    assert abs(complex(*out["mellin_w"]) - complex(*out["W"])) < 1e-6
    for r in out["inversao"]:
        assert abs(r["inversa"] - r["w"]) < 1e-6
    assert abs(complex(*out["A_N"]) - complex(*out["representacao"])) < 1e-6


def test_cota_decai():
    # `DNσ_le_molif`: a cota espectral em σ = 0,8 cai com N
    out = _out()
    cotas = [d["cota"] for d in out["cota_DN_sigma_0_8"]]
    assert cotas[0] > cotas[1] > cotas[2] > 0
