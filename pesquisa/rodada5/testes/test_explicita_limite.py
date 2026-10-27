"""Testes do companheiro numérico da rodada 71 (ZeroClasses/ExplicitaLimite.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_limite  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_limite.main(os.path.join(d, "explicita_limite.json"))


def test_cotas():
    # `norm_tan_le_dois`, `norm_tan_le_um`, `digamma_hor`, `logDeriv_esq_le`
    out = _out()
    assert out["tan_max_im_ge_1"] <= 2
    assert all(abs(t - 1) < 1e-9 for t in out["tan_reta_esquerda"])
    assert out["folga_digamma_hor"] > 0
    assert max(out["eq_funcional_logDeriv"]) < 1e-6


def test_formula_explicita():
    # `formula_explicita`: Σ_{|γ|≤T} x^ρ/ρ → x − ψ(N) − log 2π − ½ log(1 − x^{−2})
    out = _out()
    for linha in out["formula_explicita"]:
        erros = [abs(e["erro"]) for e in linha["erros"]]
        assert erros[-1] < 0.25
        assert erros[-1] < erros[0]
