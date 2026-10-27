"""Testes do companheiro numérico da rodada 38 (ZeroClasses/LittlewoodRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_rh as lw  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return lw.main(os.path.join(d, "littlewood_rh.json"))


def test_tres_circulos_e_young():
    # `tres_circulos`: log M(r) convexa em log r; `young_rpow` na grade; `a(δ) < 1`
    out = _out()
    assert out["tres_circulos"]["convexa"]
    assert out["young_ok"]
    assert all(0 < v < 1 for v in out["expoente"].values())
    assert out["expoente"]["0.5"] < out["expoente"]["0.1"] < out["expoente"]["0.01"]


def test_H_e_janelas():
    # `nucleo`: |H| bem abaixo de log(36|t|); `cota_sob_RH`: crescimento lento de |ζ|^{±1} nas janelas
    out = _out()
    assert all(v["abs_H"] < v["cota_log36t"] for v in out["H"].values())
    for linha in out["janelas"].values():
        assert linha["640"]["max_zeta"] < 640 ** 0.35 and linha["640"]["max_inv"] < 640 ** 0.35
