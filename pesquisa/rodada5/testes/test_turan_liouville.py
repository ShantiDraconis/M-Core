"""Testes do companheiro numérico da rodada 100 (ZeroClasses/TuranLiouville.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import turan_liouville  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = turan_liouville.main(os.path.join(d, "turan_liouville.json"), n=200_000)
    return _C["o"]


def test_turan_no_intervalo():
    # T(N) > 0 em todo o intervalo (a hipótese de `rh_of_turan` vale até lá) e T(N) → 0
    o = _out()
    assert o["min_T"] > 0
    assert 0 < o["T_n"] < 0.01


def test_escala_e_serie():
    # √N·T(N) fica limitado e positivo no intervalo; Σ λ(n)/n² = π²/15
    o = _out()
    assert 0 < o["min_raiz_N_T_a_partir_de_100"] < o["max_raiz_N_T_a_partir_de_100"] < 5
    assert abs(o["serie_s1"] - o["pi2_sobre_15"]) < 1e-5
