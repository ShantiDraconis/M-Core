"""Testes do companheiro numérico da rodada 44 (ZeroClasses/Perron.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import perron as pe  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return pe.main(os.path.join(d, "perron.json"))


def test_perron_degrau():
    # `perron_degrau`: |perron(L, c, T) − 1_{L>0}| ≤ e^{cL}/(πT|L|)
    out = _out()
    assert out["max_erro_sobre_cota"] <= 1
    assert len(out["grade"]) == 36


def test_L_zero_meio():
    # fora da cota: em L = 0 o núcleo tende a ½
    out = _out()
    assert abs(out["L_zero"]["60.0"][0] - 0.5) < 0.01
