"""Testes do companheiro numérico da rodada 42 (ZeroClasses/RiemannVonMangoldt.lean)."""
import math
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import rvm  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return rvm.main(os.path.join(d, "rvm.json"))


def test_formula_N():
    # `formula_N`: πN(T) = Im E(½ + iT) + arg ζ(2 + iT) − Im ∫ ζ′/ζ + C₁ reproduz a contagem
    out = _out()
    for v in out["alturas"].values():
        assert abs(v["formula_N"] - v["N"]) < 1e-3


def test_rvm_e_im_E():
    # `riemannVonMangoldt`: |N − m| pequeno frente a log T; `im_E_meio`: erro ≤ 18/T
    out = _out()
    for v in out["alturas"].values():
        assert abs(v["razao_log"]) < 0.5
        assert abs(v["imE_erro"]) <= v["cota_18_T"]
