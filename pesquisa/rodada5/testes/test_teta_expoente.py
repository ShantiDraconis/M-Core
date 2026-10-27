"""Testes do companheiro numérico da rodada 98 (ZeroClasses/TetaExpoente.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import teta_expoente  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = teta_expoente.main(os.path.join(d, "teta_expoente.json"), n=200_000)
    return _C["o"]


def test_lados_vazios():
    # os lados de cima de θ − N e π − Li não têm nenhum N ≥ 8 positivo; ψ − N e M trocam de sinal
    p = _out()["quantos_N_com_E_positivo_a_partir_de_8"]
    assert p["theta_cima"] == 0 and p["pi_cima"] == 0
    for k in ("psi_cima", "psi_baixo", "M_cima", "M_baixo"):
        assert p[k] > 1000


def test_expoentes_locais():
    # na última década completa, o expoente local de |E| fica entre 0,3 e 0,6 para as quatro funções
    o = _out()
    d = o["expoente_local_por_decada"]
    assert sorted(d) == ["0", "1", "2", "3", "4"]
    u = d["4"]
    for a, b in (("psi_cima", "psi_baixo"), ("theta_cima", "theta_baixo"), ("pi_cima", "pi_baixo"),
                 ("M_cima", "M_baixo")):
        e = max(x for x in (u[a], u[b]) if x is not None)
        assert 0.3 < e < 0.6
