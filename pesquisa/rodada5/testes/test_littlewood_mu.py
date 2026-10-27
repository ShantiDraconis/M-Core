"""Testes do companheiro numérico da rodada 46 (ZeroClasses/LittlewoodMu.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_mu as lm  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return lm.main(os.path.join(d, "littlewood_mu.json"))


def test_littlewood_converge():
    # `littlewood`: Σ_{n≤N} μ(n) n^{−w} → 1/ζ(w); o erro em N = 10⁵ é menor que em N = 10
    out = _out()
    for linhas in out["littlewood"].values():
        assert linhas[-1]["erro"] < linhas[0]["erro"]
        # `cota_PN`: o quociente pela taxa (N + ½)^{−ε/4} fica limitado
        assert max(l["erro_sobre_taxa"] for l in linhas) < 4


def test_espectral_dominado():
    # `entradaLittlewood`: o erro espectral vezes (1 + |τ|)^{5/4} fica limitado na grade
    out = _out()
    assert max(e["erro_vezes_peso"] for e in out["espectral_eps_0_2_N_2000"]) < 2
