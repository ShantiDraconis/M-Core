"""Testes do companheiro numérico da rodada 31 (JensenLocal.lean, Canonico.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import canonico as ca  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return ca.main(os.path.join(d, "canonico.json"))


def test_zeros_e_jensen_local():
    # contagem por Riemann–Siegel contra RvM; `N_succ_le`: N(T+1) − N(T) ≤ 2 Lc(T + ½), com folga grande
    out = _out()
    assert out["zeros_ate_300"] == 138 and abs(out["primeiros"][0] - 14.1347) < 5e-3
    for v in out["contagem"].values():
        assert abs(v["N"] - v["rvm"]) < 1.5
    jl = out["jensen_local"]
    assert jl["max_razao_N_sobre_2Lc"] < 0.05 and jl["folga_minima"] > 60


def test_soma_e_produto():
    # `soma_inv_quadrado`: parcial + cauda ≈ 2 + γ − log 4π; `hadamardXi_iff`: ξ ≈ e^{A+Bs}·P dentro da cauda
    out = _out()
    si = out["soma_inv_quadrado"]
    assert abs(si["parcial_mais_cauda"] - si["constante"]) < 1e-5
    assert abs(si["constante"] - 0.0461914179) < 1e-9
    assert abs(out["B"] + 0.0230957090) < 1e-9
    for p in out["produto_canonico"].values():
        assert p["erro_rel"] < p["cota_cauda"]
