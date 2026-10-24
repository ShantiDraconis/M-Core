"""Testes do companheiro numérico de ATK/ZeroClasses/Finito (rodada 26)."""
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import finito as fi  # noqa: E402


def test_casos_enviados():
    # `exemplo_A`, `exemplo_B`, `exemplo_C`
    out = fi.main()
    a, b, c = out["caso_A"], out["caso_B"], out["caso_C"]
    assert (a["M"], a["M//B^m"], a["#SAT"], a["det(L+qI)"][1], a["M_na_base_B"]) == (704, 1, 1, 8, "1300")
    assert (b["M"], b["M//B^m"], b["#SAT"], b["det(L+qI)"][1], b["M_na_base_B"]) == (8, 0, 0, 4, "020")
    assert (c["M"], c["M//B^m"], c["#SAT"], c["det(L+qI)"][1], c["M_na_base_B"]) == (81, 1, 1, 20, "121")
    assert a["det(L+qI)"][2] == 54 and c["det(L+qI)"][4] == 800


def test_aleatorias():
    # `codificacao_inteira`, `ordem_Fpol`, `Zp_log_cotas`
    out = fi.main()["aleatorias"]
    assert out["codificacao"] == out["ord0F_min"] == out["particao"] == out["formulas"] == 300


def test_aritmetica_terminal():
    # `satAdd_assoc`, `cancelamento_falha`, `boxplus_nao_assoc`, `E01_unifica`, `E01_soma_mal_definida`
    assert fi.satAdd(7, 7, 1) == 7 == fi.satAdd(7, 6, 1)
    assert fi.boxplus(7, fi.boxplus(7, 0, 1), 1) == 0 and fi.boxplus(7, 0, fi.boxplus(7, 1, 1)) == 2
    assert fi.E01(Fr(0)) == fi.E01(Fr(1)) == fi.E01(Fr(149999, 100000)) == "01"
    assert fi.E01(Fr(0) + 1) == "01" and fi.E01(Fr(1) + 1) == 2
