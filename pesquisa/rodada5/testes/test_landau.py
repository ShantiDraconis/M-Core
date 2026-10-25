"""Testes do companheiro numérico da rodada 36 (ZeroClasses/Landau.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import landau as la  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return la.main(os.path.join(d, "landau.json"))


def test_landau_cota():
    # `landau`: ‖f′/f(z₀) − Σ_S m/(z₀ − ρ)‖ ≤ 16(log M + 1)/R nos três casos
    out = _out()
    assert all(v["ok"] for v in out.values())


def test_landau_conjunto():
    # S = zeros a R/4: dois no polinômio (o duplo conta 2), ρ₁ perto de 0,55 + 14,13i, vazio em 1,1 + γ₁i
    out = _out()
    assert [m for _, _, m in out["polinomio"]["S"]] == [2, 1]
    assert len(out["zeta_perto_do_zero"]["S"]) == 1
    assert out["zeta_reta_um"]["S"] == []
    # o resto do polinômio é o termo do zero de fora: 1/(0 − 3) = −1/3
    assert abs(out["polinomio"]["erro"] - 1 / 3) < 1e-6
