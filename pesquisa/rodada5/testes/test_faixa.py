"""Testes do companheiro numérico da rodada 29 (FaixaAval, FaixaGeral, FaixaPecas1–3, Faixa)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import faixa as fa  # noqa: E402


def test_plano_dos_retangulos():
    # `peca_ret`: cota racional ≤ B, malha exata, raio h² ≥ hσ² + ht², limiar v = (B/r)h + 1/50
    out = fa.main()
    assert out["retangulos"] == 50 and out["centros"] == 930
    ok = out["verificacoes"]
    assert ok["cota"] == ok["malha"] == ok["raio"] == ok["limiar"] == 50
    assert ok["folga_min"] > 0.01
    # `faixa_ate_13`: os retângulos têm a área de [½, 1] × [43/50, 13] (partição binária, sem sobreposição)
    assert out["area_coberta"] == out["area_alvo"] == "607/100"


def test_faixa_e_primeiro_zero():
    # `faixa_sem_zeros`, `zeros_acima_13`, `primeiro_zero_entre`
    out = fa.main()
    assert out["min_metade_direita"]["min"] > 1 / 50 and out["min_metade_esquerda"] > 1 / 50
    b, g = out["primeiro_zero"]
    assert abs(b - 0.5) < 1e-9 and 13 < g < 14.2 and abs(g - 14.134725141734693) < 1e-9
