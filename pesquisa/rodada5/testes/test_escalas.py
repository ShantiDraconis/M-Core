"""Testes do companheiro numérico de ATK/ZeroClasses/Escalas (rodada 20)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import escalas as es  # noqa: E402
import zeroclasses as zc  # noqa: E402


def test_janela_alarga():
    # `janela_alarga`: a largura excluída junto às bordas decresce com a altura
    lts = [math.log(es.H), 50.0, 100.0, 1000.0, 1e4, 1e6]
    ds = [es.delta_melhor(lt) for lt in lts]
    assert all(ds[i + 1] < ds[i] for i in range(len(ds) - 1))
    assert ds[-1] < 1e-6


def test_janela_em_H():
    d = es.delta_melhor(math.log(es.H))
    assert 0.007 < d < 0.0072  # janela ≈ (0,00711; 0,99289) em |γ| = 3·10¹²


def test_retas_atk_na_janela():
    # `retas_atk_acima_de_H`: 6 < R log t para t > H, logo todas as retas ATK ficam na janela
    assert 6 < es.R_CLASSICA * math.log(es.H)
    d = es.delta_classica(math.log(es.H))
    assert all(d < es.sigma_atk(n) < 1 - d for n in range(1000))


def test_cruzamentos():
    # Littlewood passa a clássica em log t ≈ 76,46 (como em Bellotti–Trudgian–Yang); KV só para log t > 482 036
    lt = math.exp(es.R_LITTLEWOOD / es.R_CLASSICA)
    assert abs(lt - 76.46) < 0.01
    assert es.delta_littlewood(lt * 1.01) > es.delta_classica(lt * 1.01)
    assert es.delta_kv(4e5) < es.delta_littlewood(4e5)
    assert es.delta_kv(5e5) > es.delta_littlewood(5e5)


def test_guth_maynard_limiar():
    # 30(1 − σ)/13 < 1 ⟺ σ > 17/30; a reta ATK n = 6 é exatamente 17/30
    assert abs(es.sigma_atk(6) - 17 / 30) < 1e-15
    assert es.expoente_gm(es.sigma_atk(5)) < 1 <= es.expoente_gm(es.sigma_atk(6)) + 1e-12


def test_lei_da_cauda():
    # `lei_da_cauda`: |c|/2 ≤ R/d ≤ 3|c|/2 no disco certificado; numericamente R/d → |ζ′(ρ₁)| ≈ 0,79316
    rho = zc.zero_newton(complex(0.5, 14.13))
    c = abs(es.C_CERT)
    for d in (1e-3, 1e-4, 1e-5):
        q = abs(zc.zeta(rho + d)) / d
        assert c / 2 <= q <= 3 * c / 2
    assert abs(abs(zc.zeta(rho + 1e-5)) / 1e-5 - 0.79316) < 1e-4
