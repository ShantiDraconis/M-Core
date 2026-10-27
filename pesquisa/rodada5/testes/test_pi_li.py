"""Testes do companheiro numérico da rodada 60 (ZeroClasses/PiLi.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import pi_li  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return pi_li.main(os.path.join(d, "pi_li.json"))


def test_partes():
    # `Li_partes`, `Li_log_partes`: as integrações por partes (Simpson) e Li pela série de Ramanujan
    out = _out()
    for r in out["partes"]:
        assert abs(r["dif_simpson"]) < 1e-4
        assert abs(r["dif_partes"]) < 1e-4
        assert abs(r["dif_log_partes"]) < 1e-3


def test_pi_menos_Li():
    # `semZeros_iff_pi` (dado finito): π(10⁶) = 78498, Li(10⁶) = 78626,5; |π − Li| ≤ √x log x/(8π) (Schoenfeld)
    out = _out()
    t = out["tabela"]
    assert t[-1]["pi"] == 78498
    assert abs(t[-1]["Li"] - 78626.504) < 0.01
    assert all(r["razao_sqrt_log"] < out["schoenfeld"] for r in t)
