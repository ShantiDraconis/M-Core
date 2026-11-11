"""Testes do companheiro numérico da rodada 110 (ZeroClasses/BDMonoide.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_monoide  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_monoide.main(os.path.join(d, "bd_monoide.json"), X=20000, M=100000)


def test_constantes_e_serie():
    out = _out()
    # aceleração CVZ conferida contra ζ(2) = π²/6, ζ(4) = π⁴/90, β(3) = π³/32
    for v in out["conferencia_constantes"].values():
        assert abs(v) < 1e-50
    # μ_F = μ ⋆ (χ₋₄ μ): μ_F(2) = −1, μ_F(3) = 0, μ_F(5) = −2, μ_F(9) = χ(3) = −1, μ_F(10) = 2
    mf = out["mu_F_ate_12"]
    assert (mf[1], mf[2], mf[4], mf[8], mf[9]) == (-1, 0, -2, -1, 2)
    # GF_serie: as caudas exatas conferem com a soma direta Σ_{n ≤ M} μ_F(n) ψ(n/x)
    for r in out["serie_direta"]:
        assert abs(r["direta"] - r["exata"]) <= r["cota_cauda"]


def test_escala_raiz():
    # consistência com RH ∧ GRH(χ₋₄) (não é medida): |G_F(N)| ≤ 0,02 √N a partir de N = 10 e G_F troca de sinal
    out = _out()
    assert all(b["max_G_sobre_raiz"] < 2e-2 for b in out["blocos"][1:])
    assert out["trocas_de_sinal"] > 5
