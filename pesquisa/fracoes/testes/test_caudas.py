"""Testes do companheiro numérico da rodada 103 (atk-kernel/ATK/Fracoes*.lean)."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import caudas  # noqa: E402


def test_zeros_fracao_continua():
    # os mesmos quocientes que ATK/FracoesGama.lean certifica
    z = {r["nome"]: r for r in caudas.zeros()}
    assert z["gama1"]["quocientes"] == [14, 7, 2, 2, 1, 2, 1]
    assert z["gama2"]["quocientes"] == [21, 45, 2, 1, 2]
    assert z["gama3"]["quocientes"] == [25, 92]
    assert z["gigante1"]["n_certificados"] == 16 and z["gigante2"]["n_certificados"] == 17
    assert z["gama1"]["cauda"] == ["36140203/21453481", "38960203/17593481"]
    for r in z.values():
        assert r["erro_convergente_vezes_q2"] < 1


def test_bsd():
    # a_p conhecidos (LMFDB) e L(E,1)/Ω = 1/5 para 11a1
    assert caudas.a_p(caudas.CURVAS["11a1"][0], 2) == -2
    assert caudas.a_p(caudas.CURVAS["37a1"][0], 3) == -3
    assert caudas.a_p(caudas.CURVAS["389a1"][0], 7) == -5
    r = caudas.bsd_razao_11a1()
    assert abs(r["razao"] - 0.2) < 1e-12
    p = caudas.bsd_produtos(P=2000, marcos=(100, 2000))
    e = [p[k]["expoente_estimado"] for k in ("11a1", "37a1", "389a1")]
    assert e[0] < e[1] < e[2]


def test_beal():
    # (2,2,2): χ = 1/2 e a contagem cresce como X^{1/2}; (3,3,3): nenhuma; (2,3,7): as 5 conhecidas
    assert len(caudas.contar(2, 2, 2, 10 ** 4)) == 32
    assert len(caudas.contar(3, 3, 3, 10 ** 5)) == 0
    b = caudas.beal(Xs=(10 ** 3, 10 ** 4), X_hip=10 ** 9)
    assert b["hiperbolico"]["2,3,7"]["solucoes"][:2] == ["1^7 + 2^3 = 3^2", "2^7 + 17^3 = 71^2"]


def test_ym_z2_exato():
    w = caudas.z2_gauge(2)
    assert w == {"1x1": "1/2", "1x2": "1/4", "2x2": "1/16"}


def test_ns_burgers():
    a = caudas.burgers_cauda(0.2, 1.0, N=128)["delta"]
    b = caudas.burgers_cauda(0.05, 1.0, N=128)["delta"]
    assert a > b > 0
    assert caudas.choque_coeficientes(4) == ["1", "1/2", "1/3", "1/4"]


def test_ns_burgers_limite_inviscido():
    # em t = 1 (quebra de u₀ = sin x) o limite invíscido é a cúspide: cauda k^{−4/3}, não 1/k
    r = caudas.burgers_inviscido(1.0, ks=(1, 64, 256))
    for c in r["coeficientes"]:
        assert c["erro_vs_quadratura"] < 1e-12
    assert abs(r["coeficientes"][0]["b_k"] - 0.8801011714898) < 1e-12  # 2·J_1(1)
    assert abs(r["coeficientes"][-1]["abs_b_k_vezes_k_4_3"] - r["constante_k_4_3"]) < 1e-4
    # t = 0 é a condição inicial; t > 1 (depois do choque) é recusado
    r0 = caudas.burgers_inviscido(0.0, ks=(1, 2, 5))
    assert [c["b_k"] for c in r0["coeficientes"]] == [1.0, 0.0, 0.0]
    assert all(c["erro_vs_quadratura"] < 1e-12 for c in r0["coeficientes"])
    try:
        caudas.burgers_inviscido(2.0)
        assert False, "t > 1 deveria ser recusado"
    except ValueError:
        pass
    # δ ∝ ν^{3/4} na quebra, δ ∝ ν depois do choque
    p1 = caudas.expoente_largura(1.0, N=128)["p"]
    p2 = caudas.expoente_largura(2.0, N=256)["p"]
    assert all(0.70 < p < 0.80 for p in p1)
    assert all(0.95 < p < 1.15 for p in p2)


def test_sat_e_euler():
    assert caudas.sat(n=8, m=20)["media_satisfeitas"] == "7/8"
    e = caudas.euler()
    for nome in ("tetraedro", "cubo", "octaedro", "dodecaedro", "icosaedro"):
        assert e[nome]["V-E+F"] == "2" and e[nome]["defeito_total_pi"] == "4"
    assert F(e["icosaedro"]["chi"]) == F(1, 30)


def test_rodada106_linearizacao_e_primons():
    # |ζ(−2m−δ)| pela equação funcional: mínimo em m = 3 (centro 8), 0,000793; a/K = 2 sin(πδ/2) ∈ [2δ, πδ]
    L = caudas.linearizacao()
    assert L["minimo_m"] == 3
    assert abs(L["linhas"][3]["abs_zeta"] - 0.000793) < 5e-7
    for r in L["linhas"]:
        assert L["cota_inferior_2delta"] <= r["a_sobre_K"] <= L["cota_superior_pi_delta"]
    for d in (0.13, 0.14):  # anel_oito_linear: 26/100 ≤ a/K ≤ 45/100
        assert 0.26 <= caudas.linearizacao(d, [3])["linhas"][0]["a_sobre_K"] <= 0.45
    # gás de primos: traço → ζ(σ), parte conexa ≤ 2^{2−σ}(π²/6 − 1) (igualdade em σ = 2), lacuna 2^{−σ}
    P = caudas.primons()
    for sg in ("2", "3", "4"):
        assert all(v < P[sg]["zeta"] for v in P[sg]["traco"].values())
        assert P[sg]["conexo"] <= P[sg]["cota_conexo"] + 1e-12
    assert abs(P["2"]["zeta"] - math.pi ** 2 / 6) < 1e-14
    assert P["3"]["lacuna_fracao"] == "1/8"


def test_rodada107_derivadas_e_fermions():
    # |ζ′(−2m)| = (2m)!ζ(2m+1)/(2(2π)^{2m}): o quociente |ζ(−2m−δ)|/δ converge para ela
    d = caudas.derivadas_triviais()
    assert abs(d["linhas"][0]["derivada_exata"] - 0.030448457058393) < 1e-13  # ζ(3)/(4π²)
    assert min(d["linhas"], key=lambda r: r["derivada_exata"])["m"] == 3
    assert all(r["erro_relativo_menor_delta"] < 1e-5 for r in d["linhas"])
    # gás fermiônico: Σ μ(n) n^{−σ} → 1/ζ(σ), índice de Witten, M(10⁴) = −23
    f = caudas.fermions()
    assert abs(f["2"]["traco"]["10000"] - 6 / math.pi ** 2) < 1e-6
    assert f["witten_ate_200"] and f["mertens"]["M(N)"] == -23
