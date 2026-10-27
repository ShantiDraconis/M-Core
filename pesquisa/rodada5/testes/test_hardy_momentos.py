"""Testes do companheiro numérico da rodada 49 (ZeroClasses/HardyMomentos.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import hardy_momentos as hm  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return hm.main(os.path.join(d, "hardy_momentos.json"))


def test_inversao_e_momentos():
    # `integral_Fx_cos` e `momento` (n = 0, 1; α = 0,2, 0,3, 0,4)
    out = _out()
    for c in out["inversao"]:
        assert abs(c["integral"] - c["pi2_Hr"]) < 1e-10
    for m in out["momentos"]:
        assert abs(m["integral"] - m["formula"]) < 1e-6 * abs(m["formula"])


def test_cuspide():
    # `momento_tendsto` (lado direito): o valor em α = 0,78 está perto de (−1)^n π 4^{−n} cos(π/8)
    out = _out()
    for c in out["cuspide"]:
        assert abs(c["formula"][-1] - c["limite"]) < 5e-3
