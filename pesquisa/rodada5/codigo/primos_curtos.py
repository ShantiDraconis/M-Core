#!/usr/bin/env python3
"""Companheiro numérico da rodada 101: primos em intervalos curtos (ATK/ZeroClasses/PrimosCurtos.lean).

Só biblioteca padrão. **Nada aqui é certificado.** Os teoremas são assintóticos, com constantes não explícitas.
Aqui se olham as lacunas recordes `g = p_{n+1} − p_n` até `n₀` e as razões:

* `g/(√p log³ p)`: a escala de `primo_curto_RH`;
* `g/(√p log p)`: a escala de Cramér (1920) sob RH;
* `g/log² p`: a conjectura de Cramér;
* `g/p^{½}`: a escala `x^θ` de `primo_curto_Teta` com `θ = ½`.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def crivo(n):
    c = bytearray([1]) * (n + 1)
    c[0] = c[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if c[p]:
            c[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    return [k for k in range(n + 1) if c[k]]


def main(saida=None, n=1_000_000):
    ps = crivo(n)
    recordes = []
    g_max = 0
    max_rh, max_cramer_rh, max_cramer, max_raiz = 0.0, 0.0, 0.0, 0.0
    for p, q in zip(ps, ps[1:]):
        g = q - p
        if g > g_max:
            g_max = g
            recordes.append({"p": p, "g": g})
        if p >= 11:
            lp = math.log(p)
            max_rh = max(max_rh, g / (math.sqrt(p) * lp ** 3))
            max_cramer_rh = max(max_cramer_rh, g / (math.sqrt(p) * lp))
            max_cramer = max(max_cramer, g / lp ** 2)
            max_raiz = max(max_raiz, g / math.sqrt(p))
    out = {"n": n, "recordes": recordes,
           "max_g_sobre_raiz_log3_p_ge_11": max_rh, "max_g_sobre_raiz_log_p_ge_11": max_cramer_rh,
           "max_g_sobre_log2_p_ge_11": max_cramer, "max_g_sobre_raiz_p_ge_11": max_raiz,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PrimosCurtos.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "primos_curtos.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    print([(r["p"], r["g"]) for r in o["recordes"]])
    for k, v in o.items():
        if k.startswith("max"):
            print(k, v)
