"""Testes do companheiro numérico da rodada 72 (ZeroClasses/ExplicitaT.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_t  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_t.main(os.path.join(d, "explicita_t.json"))


def test_soma_faixa():
    # `soma_faixa_le`: a massa de cada faixa k + 6 < |γ| ≤ k + 7 fica abaixo de 4 (a₀ + log(k + 9))/l₀
    out = _out()
    assert out["razao_max"] < 1


def test_alturas_quaisquer():
    # `formula_explicita_T`: em alturas quaisquer o erro já é pequeno e cai
    out = _out()
    erros = [abs(a["erro"]) for a in out["alturas"]]
    assert erros[-1] < 0.1
    assert erros[-1] < erros[0]
