"""Testes do companheiro numérico da rodada 68 (ZeroClasses/LiCompleto.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import li_completo  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return li_completo.main(os.path.join(d, "li_completo.json"))


def test_lambdas():
    # `lam`: λ_1, λ_2, λ_3 batem com os valores conhecidos (4 casas); λ_n > 0 e crescente até n = 30
    out = _out()
    lam = [r["lam_estimado"] for r in out["lams"]]
    assert abs(lam[0] - out["lam1_fechado"]) < 1e-4
    assert abs(lam[1] - 0.0923457352) < 1e-3 and abs(lam[2] - 0.2076389205) < 1e-3
    assert all(v > 0 for v in lam) and all(a < b for a, b in zip(lam, lam[1:]))


def test_resto_e_hipotetico():
    # `resto_binom` nas amostras; um zero fora da reta derruba a parcela (crescimento |w|^n)
    out = _out()
    assert all(a["lhs"] <= a["rhs"] + 1e-15 for a in out["resto_binom"])
    assert out["hipotetico"]["abs_w"] > 1
