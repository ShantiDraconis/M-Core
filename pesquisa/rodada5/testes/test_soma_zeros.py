"""Testes do companheiro numérico da rodada 63 (ZeroClasses/SomaZeros.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import soma_zeros  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return soma_zeros.main(os.path.join(d, "soma_zeros.json"))


def test_soma_e_local_O_log():
    # `soma_wz_O`, `card_perto_O`, `zeta_local_O` (numérico): as razões por log t ficam abaixo de 1
    out = _out()
    assert out["n_zeros"] > 300
    assert all(r["S/log t"] < 1 and r["perto/log t"] < 1 for r in out["soma_wz"])
    assert all(r["resto/log t"] < 1 for r in out["zeta_local"])


def test_digamma_e_RH():
    # `norm_digamma_le`: |ψ(z)| abaixo da cota; `logDeriv_RH`: (σ − ½)|ζ′/ζ|/log t limitado quando σ → ½⁺
    out = _out()
    assert all(r["|psi|"] <= r["cota"] for r in out["digamma"])
    assert all(r["(sigma-1/2)|zeta'/zeta|/log t"] < 1 for r in out["logDeriv_RH"])
