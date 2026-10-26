"""Testes do companheiro numérico da rodada 30 (ZeroClasses/Jensen.lean: N(T) = O(T log T))."""
import math
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import contagem as co  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return co.main(os.path.join(d, "contagem.json"))


def test_cotas_pontuais():
    # `cota_zeta`, `Gamma_le`, `cota_xi`, `xi_metade_ne_zero`
    out = _out()
    assert abs(out["xi_meio"] - 0.4971207781883) < 1e-9
    assert out["cota_zeta"]["pontos"] == 1331 and out["cota_zeta"]["max_razao"] < 1
    assert all(v["ok"] for v in out["Gamma_le"].values())
    assert all(c["ok"] and c["max_xi_circ"] < c["Bx"] for c in out["cota_xi"])


def test_contagem_jensen():
    # `N_cota`, `N_O_TlogT`: RvM ≤ cota de Jensen ≤ C·T·log T; N(100) = 29 e N(1000) = 649 ficam abaixo
    out = _out()
    assert abs(out["C"] - ((13 + out["A=|log xi(1/2)|"] / math.log(2)) / 2 + 4) / math.log(2)) < 1e-12
    for lin in out["contagem"]:
        assert lin["ok"]
    tab = {lin["T"]: lin for lin in out["contagem"] if "N_tabelado" in lin}
    assert tab[100]["cota_jensen"] > 29 and tab[1000]["cota_jensen"] > 649
    # a cota é da ordem certa T log T, mas ~9 vezes o termo principal 1/(2π)
    grande = out["contagem"][-1]
    assert 1 < grande["razao_cota_sobre_TlogT"] < 1.5
    assert grande["cota_jensen"] / grande["rvm"] < 12
