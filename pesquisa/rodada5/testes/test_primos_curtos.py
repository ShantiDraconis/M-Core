"""Testes do companheiro numérico da rodada 101 (ZeroClasses/PrimosCurtos.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import primos_curtos  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = primos_curtos.main(os.path.join(d, "primos_curtos.json"), n=200_000)
    return _C["o"]


def test_lacunas_recordes():
    # as lacunas recordes conhecidas (OEIS A002386 / A005250) até 2·10⁵
    o = _out()
    ps = [r["p"] for r in o["recordes"]]
    gs = [r["g"] for r in o["recordes"]]
    assert ps == [2, 3, 7, 23, 89, 113, 523, 887, 1129, 1327, 9551, 15683, 19609, 31397, 155921]
    assert gs == [1, 2, 4, 6, 8, 14, 18, 20, 22, 34, 36, 44, 52, 72, 86]


def test_escalas():
    # no intervalo, as lacunas ficam bem abaixo de √p log³ p, de √p log p e de log² p (p ≥ 11)
    o = _out()
    assert o["max_g_sobre_raiz_log3_p_ge_11"] < 0.1
    assert o["max_g_sobre_raiz_log_p_ge_11"] < 1
    assert o["max_g_sobre_log2_p_ge_11"] < 1
