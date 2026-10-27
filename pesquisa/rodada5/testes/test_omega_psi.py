"""Testes do companheiro numérico da rodada 58 (ZeroClasses/OmegaPsi.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import omega_psi  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return omega_psi.main(os.path.join(d, "omega_psi.json"))


def test_polo_no_primeiro_zero():
    # `cota_inf_H`: (σ − ½)|H| → m = 1; `cota_inf_F`: (σ − ½)|1/ζ| → 1/|ζ′(ρ₁)|
    out = _out()
    p = out["polo"]
    assert abs(p[-1]["d_vezes_H"] - 1) < 1e-3
    assert abs(p[-1]["d_vezes_inv_zeta"] - out["inv_abs_dzeta_rho1"]) < 1e-3
    assert all(r["d_vezes_H"] >= 0.5 for r in p)


def test_dados_nao_o():
    # `psi_nao_o`, `mertens_nao_o` (dado finito): o máximo por década de |ψ(N) − N|/√N e |M(N)|/√N não cai a zero
    out = _out()
    d = out["decadas"]
    assert all(r["max_psi_sqrt"] > 0.5 for r in d)
    assert all(r["max_M_sqrt"] > 0.4 for r in d)
