"""Testes do companheiro numérico da rodada 84 (ZeroClasses/BDSemPotencia.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_sem_potencia  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_sem_potencia.main(os.path.join(d, "bd_sem_potencia.json"))


def test_amostra_compativel_com_contracao():
    # B2: os dados finitos são compatíveis com contração (o teorema a exclui assintoticamente)
    assert _out()["max_razao_diadica_100_4000"] < 0.95


def test_expoente_cai():
    # `DN_sem_potencia`: o expoente local médio cai de bloco em bloco
    e = [b["expoente_medio"] for b in _out()["expoentes_por_bloco"]]
    assert e[0] > 0.3 and e[-1] < 0.15
