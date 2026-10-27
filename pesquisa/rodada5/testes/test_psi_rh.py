"""Testes do companheiro numérico da rodada 64 (ZeroClasses/PsiRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import psi_rh  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return psi_rh.main(os.path.join(d, "psi_rh.json"), N=10 ** 6)


def test_psi_dentro_de_schoenfeld():
    # `psi_RH` (numérico): |ψ(x) − x| < √x log² x/(8π) até 10⁶, e a razão por √x log³ x fica < 0,01
    out = _out()
    assert all(b["max_schoenfeld"] < 1 and b["max_log3"] < 0.01 for b in out["blocos"])


def test_perron_e_integral():
    # `norm_fL_le`: η Λ(n) n^{−η} ≤ 1; `integral_um_abs`: quadratura = 2 log(1 + T)
    out = _out()
    assert out["fL_max"] <= 1
    q = out["integral_um_abs"]
    assert abs(q["quadratura"] - q["formula"]) < 1e-6
