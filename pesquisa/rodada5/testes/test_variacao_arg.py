"""Testes do companheiro numérico da rodada 41 (ZeroClasses/VariacaoArg.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import variacao_arg as va  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return va.main(os.path.join(d, "variacao_arg.json"))


def test_variacao():
    # `variacao`: |V(T)| ≤ (k + 1)π; `conta_zeros_re`: k ≤ cota de Jensen; `variacao_log`: V(T) = O(log T)
    out = _out()
    for v in out["alturas"].values():
        assert abs(v["V"]) <= v["cota_variacao"] + 1e-9
        assert v["k"] <= v["jensen"]
    assert out["max_V_sobre_logT"] < 1


def test_cota_quarto():
    # `cota_zeta_quarto`: |ζ(s)| ≤ ½ + 1/|s − 1| + 6|s| em Re s ≥ ¼
    assert _out()["zeta_quarto_razao_max"] <= 1
