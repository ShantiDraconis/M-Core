"""Testes do companheiro numérico da rodada 95 (ZeroClasses/LittlewoodPi.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_pi  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_pi.main(os.path.join(d, "littlewood_pi.json"), n=200_000)
    return _C["o"]


def test_identidades():
    # `Li_eq` e `pi_sub_Li`
    o = _out()
    for r in o["Li_por_partes"]:
        assert abs(r["Li"] - r["por_partes"]) < 1e-3
    for r in o["pi_menos_Li"]:
        if r["x"] <= 200_000:
            assert abs(r["pi_menos_Li"] - r["formula"]) < 1e-3


def test_resto_e_sinal():
    # o resto 2/log 2 + E(x) é uma fração de √x/log x que diminui; π < Li a partir de x = 8
    o = _out()
    rs = [abs(r["resto_sobre_raiz_log"]) for r in o["pi_menos_Li"] if r["x"] <= 200_000]
    assert all(a > b for a, b in zip(rs, rs[1:]))
    assert o["ultimo_k_com_pi_maior_ou_igual_Li"] == 7
