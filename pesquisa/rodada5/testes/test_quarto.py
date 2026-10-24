"""Testes do companheiro numérico da rodada 28 (Quarto.lean, Lagarias.lean)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import quarto as qu  # noqa: E402


def test_m4_e_espelho():
    # `m4_cota`, `m4_menor_um`, `espelho_sem_zeros`
    out = qu.main()
    assert 1 / 20 <= out["m4"]["min"] < 1
    assert abs(out["m4"]["min"] - 0.4611) < 1e-3 and abs(out["m4"]["t_min"] - 2.175) < 0.01
    assert out["espelho_min"] > 1 / 20


def test_pecas_fecham():
    # `peca1`–`peca4`, `peca_cert`, `cotaQ_spec`: cota racional ≤ B, b − a = 2hn, |ζ| nos centros > v
    out = qu.main()
    assert out["centros"] == 95 and len(out["pecas"]) == 4
    for p in out["pecas"]:
        assert p["cota_ok"] and p["fecha"] and p["folga"] > 0.02
        # a cota grosseira domina o máximo amostrado de |ζ| e B/r domina |ζ′| no segmento
        assert p["cotaQ"] > p["max_zeta_regiao"] and p["L=B/r"] > p["max_dzeta_segmento"]


def test_lagarias():
    # `Lg_linha`, `Lg_antissim`, `sinal_negativo` (no modelo com zero artificial fora da linha)
    out = qu.main()["lagarias"]
    assert out["max|L(1/2+it)|"] < 1e-6 and out["max|L(1-s)+L(s)|"] < 1e-6
    assert out["positivos"] == out["pontos"] == 2400
    assert all(x < 0 for x in out["modelo_fora"]["L(rho-h)"])
