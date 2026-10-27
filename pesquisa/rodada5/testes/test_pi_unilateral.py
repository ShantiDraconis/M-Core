"""Testes do companheiro numérico da rodada 97 (ZeroClasses/PiUnilateral.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import pi_unilateral  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = pi_unilateral.main(os.path.join(d, "pi_unilateral.json"), n=200_000)
    return _C["o"]


def test_lado_de_cima():
    # no intervalo, o lado de cima vale com folga: θ(N) < N sempre e π(N) < Li(N) a partir de 8
    o = _out()
    e = o["extremos_a_partir_de_100"]
    assert o["ultimo_N_com_theta_maior_ou_igual_N"] is None
    assert o["ultimo_N_com_pi_maior_ou_igual_Li"] == 7
    assert e["theta_max"]["valor"] < 0 and e["pi_max"]["valor"] < 0


def test_lado_de_baixo():
    # o lado de baixo fica na escala √x (θ) e √x/log x (π − Li), como RH prevê
    o = _out()
    e = o["extremos_a_partir_de_100"]
    assert -3 < e["theta_min"]["valor"] < e["theta_max"]["valor"]
    assert -3 < e["pi_min"]["valor"] < e["pi_max"]["valor"]
