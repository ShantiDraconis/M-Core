#!/usr/bin/env python3
"""Companheiro numérico de ATK/HurwitzJensen.lean e ATK/DBNFechado.lean (rodada 14).

Só biblioteca padrão; nada é certificado e nada prova HR.

* J^{d,0}(w/d) = Σⱼ (d^{(j)}/dʲ) aⱼ wʲ → B(w) = Σ aⱼ wʲ (`tendstoUniformlyOn_Fj`): o erro em w = −50 cai como 1/d.
* H_t(0) = ∫e^{tu²}Φ(u)du > 0 (`H_ne_zero_at_zero`) e o primeiro zero real de H_t varia continuamente com t
  (S fechado, `isClosed_S`): bisseção perto de 14,13 para t = −0,1, 0, 0,1.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dbn  # noqa: E402
import edrei  # noqa: E402

A = [edrei.a_xi(n) for n in range(30)]


def B(w):
    return sum(a * w ** j for j, a in enumerate(A))


def F(d, w):
    return sum((math.perm(d, j) / d ** j) * A[j] * w ** j for j in range(min(d, len(A) - 1) + 1))


def primeiro_zero(t, a=13.0, b=15.5, it=60):
    fa = dbn.H(t, a)
    for _ in range(it):
        m = (a + b) / 2
        fm = dbn.H(t, m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2


def main(saida=None):
    w = -50.0
    erros = {str(d): abs(F(d, w) - B(w)) for d in (10, 20, 40, 80, 160, 320)}
    res = {
        "B(-50)=Xi(sqrt50)": format(B(w), ".10g"),
        "|J^{d,0}(w/d)-B(w)|_w=-50": {k: format(v, ".3g") for k, v in erros.items()},
        "H_t(0)>0_t=-0.5,0,0.5": [dbn.H(t, 0.0) > 0 for t in (-0.5, 0.0, 0.5)],
        "primeiro_zero_H_t_t=-0.1,0,0.1": [format(primeiro_zero(t), ".8f") for t in (-0.1, 0.0, 0.1)],
        "aviso": "verificação finita; HR ⟺ todos os J^{d,n} hiperbólicos é OPEN_MATH",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
