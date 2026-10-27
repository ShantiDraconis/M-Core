"""Testes do companheiro numérico da rodada 45 (ZeroClasses/PerronDirichlet.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import perron_dirichlet as pdr  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return pdr.main(os.path.join(d, "perron_dirichlet.json"))


def test_perron_mu():
    # `perron_LSeries` com f = μ: o erro fica abaixo da cota e cai com T
    out = _out()
    for linha in out["perron_mu"]:
        assert linha["erro"] <= linha["cota"]
    erros = {(l["N"], l["T"]): l["erro"] for l in out["perron_mu"]}
    assert erros[(10, 50.0)] < erros[(10, 20.0)] and erros[(30, 50.0)] < erros[(30, 20.0)]


def test_abs_log_ge():
    # `abs_log_ge`: |log(x/n)| ≥ 1/(4x + 2) para x = N + ½
    assert _out()["min_log_vezes_4x2"] >= 1
