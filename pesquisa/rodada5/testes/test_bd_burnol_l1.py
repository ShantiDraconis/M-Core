"""Testes do companheiro numérico da rodada 80 (ZeroClasses/BDBurnolL1.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_burnol_l1  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_burnol_l1.main(os.path.join(d, "bd_burnol_l1.json"))


def test_J_reta():
    for r in _out()["J_reta"]:
        assert abs(r["quad"] - r["formula"]) < 1e-3 * r["formula"]


def test_piso_log():
    # `burnol_L1`: piso C/(log N + B'') > 0, com piso·log N crescendo para C (forma 1/log N)
    out = _out()
    k = out["constantes"]
    assert k["C"] > 0 and k["B"] > 0
    p = [r["piso_vezes_log"] for r in out["pisos"]]
    assert all(a < b for a, b in zip(p, p[1:])) and p[-1] < k["C"]
    assert all(r["piso"] < r["burnol_assintotico"] for r in out["pisos"])
