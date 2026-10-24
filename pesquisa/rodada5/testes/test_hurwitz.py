"""Testes do companheiro numérico de ATK/HurwitzJensen e ATK/DBNFechado (rodada 14)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import dbn  # noqa: E402
import hurwitz  # noqa: E402


def test_jensen_escalonado_converge():
    # J^{d,0}(w/d) → B(w) (`tendstoUniformlyOn_Fj`); B(−t²) = Ξ(t) = 2H₀(t)
    w = -50.0
    assert abs(hurwitz.B(w) - 2 * dbn.H(0, 50 ** 0.5)) < 1e-12
    erros = [abs(hurwitz.F(d, w) - hurwitz.B(w)) for d in (20, 40, 80, 160, 320)]
    assert all(erros[i + 1] < erros[i] for i in range(len(erros) - 1))
    assert erros[-1] < 1e-3


def test_H_t_positivo_e_zero_continuo():
    # H_t(0) > 0 (`H_ne_zero_at_zero`); o primeiro zero real varia continuamente com t (`isClosed_S`)
    assert all(dbn.H(t, 0.0) > 0 for t in (-0.5, 0.0, 0.5))
    z = [hurwitz.primeiro_zero(t) for t in (-0.1, 0.0, 0.1)]
    assert abs(z[1] - 14.134725141734693) < 1e-6
    assert z[0] > z[1] > z[2] and z[0] - z[2] < 0.5
