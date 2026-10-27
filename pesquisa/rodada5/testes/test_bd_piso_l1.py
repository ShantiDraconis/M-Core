"""Testes do companheiro numérico da rodada 79 (ZeroClasses/BDPisoL1.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_piso_l1  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_piso_l1.main(os.path.join(d, "bd_piso_l1.json"))


def test_integrais():
    # `head0_le` (igualdade) e `J_le`
    for r in _out()["integrais"]:
        assert abs(r["head"] - r["head_formula"]) < 1e-2 * r["head_formula"]
        assert r["J"] <= r["J_cota"]


def test_piso_e_norma():
    # `norm_cN_le` e `piso_L1`: o piso fica abaixo de ‖res‖² do molificador
    out = _out()
    assert out["constante"]["C"] > 0
    for r in out["molificador"]:
        assert r["norma_l1"] <= r["N"]
        assert 0 < r["piso"] < r["cota_espectral"]
