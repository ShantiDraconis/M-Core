"""Testes do companheiro numérico de ATK/ArgPrincipio e ATK/ZeroClasses/Rouche (rodada 25)."""
import cmath
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import argumento as ar  # noqa: E402
import zeroclasses as zc  # noqa: E402


def test_principio_do_argumento():
    # `principio_argumento`, `contagem_zeta`
    rho = zc.zero_newton(complex(0.5, 14.13))
    assert abs(ar.conta(rho, 0.3) - 1) < 1e-6
    assert abs(ar.conta(complex(0.75, 14.13), 0.2)) < 1e-6  # disco fora da linha: nenhum zero
    assert abs(ar.conta(complex(0.5, 20.0), 7.0) - 3) < 1e-3  # zeros 14,13; 21,02; 25,01


def test_rouche():
    # `rouche_zeta` com F(z) = ζ′(ρ₁)(z − ρ₁)
    rho = zc.zero_newton(complex(0.5, 14.13))
    a = ar.dz(rho)
    r = 0.05
    for k in range(32):
        e = cmath.exp(2j * math.pi * k / 32)
        assert abs(zc.zeta(rho + r * e) - a * r * e) < abs(a * r * e)


def test_E1_afiado_e_exemplo():
    # `E1_afiado`, `E1_zeta_linha`, `exemplo_quadratico_unico`
    out = ar.main()
    e = out["E1_afiado_1o_zero"]
    assert e["|ζ(c)|+M r²/2"] < e["r|ζ′(c)|"]
    assert abs(1 / 20 + 0.5 * (1 / 8) ** 2 / 2 - 69 / 1280) < 1e-15 and 69 / 1280 < 1 / 8
