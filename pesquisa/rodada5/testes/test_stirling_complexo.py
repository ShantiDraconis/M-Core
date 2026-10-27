"""Testes do companheiro numérico da rodada 39 (ZeroClasses/StirlingComplexo.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import stirling_complexo as sc  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return sc.main(os.path.join(d, "stirling_complexo.json"))


def test_exp_ell_e_derivada():
    # `exp_ell`: exp(ell z) = Γ(z); `hasDerivAt_ell`: ell′ = ψ; `ell 1 = 0`
    out = _out()
    assert all(v < 1e-9 for v in out["exp_ell_erro_relativo"].values())
    assert all(v < 1e-5 for v in out["derivada_vs_digama"].values())
    assert abs(out["ell_1"][0]) < 1e-9 and out["ell_1"][1] == 0


def test_cotas():
    # `norm_ek_le` (|e_k|·|w|² ≤ 2; o valor real é ≈ 1/12), `stirling` (≤ 8/|Im z|), `im_ell_quarto` (≤ 9/τ)
    out = _out()
    assert out["ek_vezes_w2_max"] <= 2
    assert all(v["abs_EE"] <= v["cota"] for v in out["stirling"].values())
    assert all(abs(v["erro"]) <= v["cota"] for v in out["im_ell_quarto"].values())
    assert abs(out["im_ell_quarto"]["200.0"]["erro_vezes_tau"] - 1 / 96) < 1e-4
