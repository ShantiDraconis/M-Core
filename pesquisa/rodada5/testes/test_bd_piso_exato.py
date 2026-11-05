"""Testes do companheiro numérico da rodada 109 (ZeroClasses/BDPisoExato.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_piso_exato  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_piso_exato.main(os.path.join(d, "bd_piso_exato.json"), X=20000, M=100000)


def test_mellin_psi_e_serie():
    out = _out()
    # hasMellin_psi: ∫_1^∞ t^{s−1} ψ(t) dt = 1/((2 − s)(3 − s)(4 − s))
    for r in out["mellin_psi"]:
        assert abs(r["quad"] - r["K"]) < 1e-8
    # Gl_mobius: as caudas exatas conferem com a soma direta Σ_{n ≤ M} μ(n) ψ(n/x)
    for r in out["serie_direta"]:
        assert abs(r["direta"] - r["exata"]) <= r["erro_max_cauda"]


def test_escala_raiz():
    # consistência com Θ = ½ (não é medida de Θ): |G(N)| ≤ 0,002 √N e G troca de sinal
    out = _out()
    assert all(b["max_G_sobre_raiz"] < 2e-3 for b in out["blocos"][1:])
    assert out["trocas_de_sinal"] > 10
