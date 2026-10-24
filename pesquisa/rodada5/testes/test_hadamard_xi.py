"""Testes do companheiro numérico da rodada 33 (ZeroClasses/Hadamard.lean: ξ = e^{A+Bs}·P)."""
import math
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import hadamard_xi as hx  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return hx.main(os.path.join(d, "hadamard_xi.json"))


def test_constantes():
    # `xi_hadamard`: A = log ξ(0) = −log 2, B = ξ′(0)/ξ(0) = −γ/2 − 1 + ½ log 4π = −Σ Re(1/ρ)
    out = _out()
    assert abs(out["A"] + math.log(2)) < 1e-9
    assert abs(out["B_diferenca_finita"] - out["B_formula"]) < 1e-8
    assert abs(out["B_soma_300_mais_cauda"] - out["B_formula"]) < 1e-5


def test_identidade_e_g_afim():
    # `hadamardXi`: ξ(s) = e^{A+Bs}·P(s) (com a cauda dos zeros acima de 300); `g_afim`: g″ ≈ 0
    out = _out()
    for p in out["identidade"].values():
        assert p["erro_rel"] < 1e-3
    for v in out["g_segunda_derivada"].values():
        assert v < 1e-3
    for c in out["circulos"].values():
        assert c["max_posLog_xi_sobre_P"] < c["R2"]
