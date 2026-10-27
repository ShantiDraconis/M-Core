"""Testes do companheiro numérico da rodada 99 (ZeroClasses/LiouvilleRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import liouville_rh  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = liouville_rh.main(os.path.join(d, "liouville_rh.json"), n=200_000)
    return _C["o"]


def test_serie_de_dirichlet():
    # `LSeries_lam_mul_zeta`: Σ λ(n)/n^s = ζ(2s)/ζ(s) em s = 2 e s = 3
    o = _out()
    assert abs(o["serie_s2"] - o["zeta4_sobre_zeta2"]) < 1e-5
    assert abs(o["serie_s3"] - o["zeta6_sobre_zeta3"]) < 1e-9


def test_polya_e_vies():
    # Pólya vale no intervalo (L(N) ≤ 0 para N ≥ 2), e a média de L(N)/√N fica perto de 1/ζ(½)
    o = _out()
    assert o["max_L_N_de_2_a_n"] <= 0
    assert abs(o["media_L_sobre_raiz_na_ultima_decada"] - o["inv_zeta_meio"]) < 0.2
    assert o["max_abs_L_sobre_raiz"] < 2
