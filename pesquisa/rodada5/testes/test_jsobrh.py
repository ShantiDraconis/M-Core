"""Testes do companheiro numérico da rodada 43 (ZeroClasses/JSobRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import jsobrh as jr  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return jr.main(os.path.join(d, "jsobrh.json"))


def test_J_decresce_para_zero():
    # `tendsto_J`: J(ε) → 0 quando ε → 0⁺ (truncada em |τ| ≤ 120)
    out = _out()
    v = [out["J_truncada_T120"][k] for k in ("0.4", "0.2", "0.1", "0.05", "0.02", "0.01")]
    assert all(a > b for a, b in zip(v, v[1:]))
    assert v[-1] < 0.01


def test_razoes_e_monotonia():
    # `razao_Gamma`, `razao_zeta` e `xi_meio_le` na grade
    out = _out()
    assert out["razao_Gamma_max"] <= out["exp_17_2"]
    assert max(out["razao_zeta_max"].values()) < 2
    assert out["monotonia_xi_na_grade"]
