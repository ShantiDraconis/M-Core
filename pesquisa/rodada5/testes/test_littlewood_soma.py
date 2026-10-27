"""Testes do companheiro numérico da rodada 91 (ZeroClasses/LittlewoodSoma.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_soma  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_soma.main(os.path.join(d, "littlewood_soma.json"))
    return _C["o"]


def test_cotas():
    # `massa_le_real`, `D_ge`, `cauda_le`
    o = _out()
    for r in o["massa"]:
        assert r["massa"] <= r["cota"]
    for r in o["D_ge"]:
        assert r["principal"] <= r["D"]
    for r in o["cauda"]:
        assert r["cauda"] <= r["cota"]


def test_alinhamento_forca_o_sinal():
    # `alinha` + `soma_forcada`: n ≤ Q^K, e as somas em n ± 1/T ficam perto de ±D(1/T)
    f = _out()["forcada"]
    assert 1 <= f["n"] <= f["cota_n"]
    assert abs(f["soma_mais"] - f["D"]) < 0.1 * f["D"]
    assert abs(f["soma_menos"] + f["D"]) < 0.1 * f["D"]
    assert f["soma_mais"] > 0 > f["soma_menos"]
