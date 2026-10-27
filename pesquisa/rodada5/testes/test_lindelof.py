"""Testes do companheiro numérico da rodada 61 (ZeroClasses/LindelofRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import lindelof  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return lindelof.main(os.path.join(d, "lindelof.json"))


def test_equacao_funcional_e_fator():
    # `norm_zeta_one_sub_le`: |ζ(1 − w)|/|ζ(w)| ≤ 2C_Γ|w|^δ, e ≈ (t/2π)^δ; `fator_le`: ≤ 2^a
    out = _out()
    for r in out["equacao_funcional"]:
        assert r["razao"] <= r["cota"]
        assert abs(r["razao"] / r["assint"] - 1) < 1e-3
    assert out["fator_max"] <= 2 ** 0.1


def test_maximos_na_reta():
    # dado finito: max_{[T,2T]} |ζ(½ + it)| cresce devagar (expoente aparente < ½ até T = 640)
    out = _out()
    m = out["maximos"]
    assert all(a["max_zeta"] < b["max_zeta"] for a, b in zip(m, m[1:]))
    assert all(r["expoente"] < 0.5 for r in m)
