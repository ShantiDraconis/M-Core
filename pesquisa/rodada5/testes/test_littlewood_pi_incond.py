"""Testes do companheiro numérico da rodada 96 (ZeroClasses/LittlewoodPiIncond.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_pi_incond  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_pi_incond.main(os.path.join(d, "littlewood_pi_incond.json"), n=200_000)
    return _C["o"]


def test_decomposicao():
    # `Pi_sub_pi`, `lam_sub_Li` e `aPi_eq` nos marcos
    o = _out()
    assert [r["N"] for r in o["marcos"]] == [100, 1000, 10_000, 100_000]
    for r in o["marcos"]:
        assert 0 <= r["Pi_menos_pi"] <= r["psi_menos_theta_sobre_log2"]
        assert r["inv_log_N"] <= r["lam_menos_Li"] <= r["inv_log_2"]
        assert abs(r["a"] - r["decomposicao"]) < 1e-6


def test_vies():
    # π − Li negativo de 8 em diante, enquanto a(N) = Π(N) − λ(N) troca de sinal muitas vezes
    o = _out()
    assert o["ultimo_N_com_pi_maior_ou_igual_Li"] == 7
    assert o["trocas_de_sinal_pi_menos_Li_depois_de_8"] == 0
    assert o["trocas_de_sinal_a"] > 100
    assert all(r["pi_menos_Li"] < 0 for r in o["marcos"])
