"""Testes do companheiro numérico de ATK/ZeroClasses/Fronteira (rodada 27)."""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import fronteira as fr  # noqa: E402


def test_produtor_e_colapso():
    # `P_eq_argmin`, `P_sub`, `P_dois_iff`, `Q_mem_P`, `P_exemplos`, `Q_soma_cotas`, `Q_soma_cotas_atingidas`
    out = fr.main()
    p = out["produtor"]
    assert p["P_eq_argmin"] == p["card_le_2"] == p["dois_iff_fronteira"] == p["Q_em_P"] == p["pontos"] == 4001
    assert out["P(1/2)"] == [0, 1] and out["P(3/2)"] == [1, 2] and out["Q(1/2)"] == 1
    assert set(out["erro_colapso_soma"]) == {"-1", "0", "1"} and sum(out["erro_colapso_soma"].values()) == 401 ** 2
    assert out["Q(1/2+1/2)-2Q(1/2)"] == -1 and out["Q(2/5+2/5)-2Q(2/5)"] == 1


def test_adjacencia_e_competicao():
    # `adj_iff`, `adj_exemplos`, `fecho_tudo`, `Dif_fatora`, `Dif_zero_iff`, `Dif_reflexao`
    out = fr.main()
    a = out["adjacencia"]
    assert a["adj_iff_dist1"] and a["0~1"] and a["1~2"] and not a["0~2"]
    assert a["classes_do_fecho_em_-6..6"] == 1
    c = out["competicao"]
    assert c["fatora"] == c["zero_iff_meio"] == c["reflexao"] == c["triplas"]
    assert fr.Dif(0, 1, Fr(1, 2)) == 0 and fr.Dif(0, 1, 1 - Fr(1, 3)) == -fr.Dif(0, 1, Fr(1, 3))


def test_intervalos_e_zeta():
    # `pts_soma`, `larg_soma`, `sub_auto_eq_zero_iff`, `estados_iff`, `estados_tolerancia`, `estados_unidade`
    out = fr.main()
    i = out["intervalos"]
    assert i["minkowski"] == i["larguras"] == i["I-I_simetrico"] == i["estados"] == i["pares"] == 300
    assert out["estados[2/5,3/5]"] == [0, 1] and out["estados[0,1]"] == [0, 1]
    assert out["estados[0,3/2]"] == [0, 1, 2]
    z = out["zeta"]
    # `tolerancia_independente`/`exemplos_nao_zeros`: |ζ| longe de 0 nos dois pontos; `reflexo_zero` em ρ₁
    assert z["|ζ(9/20+10i)|"] > 1 and z["|ζ(11/20+10i)|"] > 1
    assert abs(z["rho1"][1] - 14.134725141734693) < 1e-9 and z["|ζ(1-β+iγ)|"] < 1e-10
