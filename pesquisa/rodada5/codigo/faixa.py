#!/usr/bin/env python3
"""Companheiro numérico da rodada 29: nenhum zero de ζ na faixa crítica até a altura 13 (ATK/ZeroClasses/Faixa*).

* lê o plano dos retângulos (dados/faixa_plano.json, o mesmo de FaixaPecas1–3.lean) e refaz, com frações exatas,
  a cota racional `cotaQ`, o raio de cobertura `h ≥ √(hσ² + ht²)`, o limiar `v = (B/r)h + 1/50` e o menor |ζ| nos
  centros (ponto flutuante);
* confere que os retângulos cobrem `[½, 1] × [43/50, 13]` sem buracos;
* min |ζ| numa malha fina das duas metades da faixa e o primeiro zero `½ + 14,1347…i` (Newton).
"""
import json
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import quarto as qu  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
R_ = F(2, 5)
DELTA = F(1, 50)


def folhas(t, out):
    if "leaf" in t:
        out.append({k: (F(v) if isinstance(v, str) else v) for k, v in t["leaf"].items()})
    else:
        folhas(t["l"], out)
        folhas(t["r"], out)
    return out


def main(saida=None):
    plano = json.load(open(os.path.join(AQUI, "..", "dados", "faixa_plano.json")))
    fs = []
    for st in plano:
        folhas(st["tree"], fs)
    res = {"retangulos": len(fs), "centros": sum(f["ns"] * f["nt"] for f in fs)}
    ok = {"cota": 0, "malha": 0, "raio": 0, "limiar": 0, "folga_min": 1.0}
    area = F(0)
    for f in fs:
        c = qu.cotaQ(f["Nc"], f["Mc"], f["R"], f["d"])
        ok["cota"] += c <= f["B"]
        ok["malha"] += (f["s0"] + 2 * f["hs"] * f["ns"] == f["s1"]) and (f["a"] + 2 * f["ht"] * f["nt"] == f["b"])
        ok["raio"] += f["hs"] ** 2 + f["ht"] ** 2 <= f["h"] ** 2
        ok["limiar"] += f["B"] / R_ * f["h"] + DELTA == f["v"]
        mn = min(abs(zc.zeta(complex(float(f["s0"] + f["hs"] * (2 * i + 1)), float(f["a"] + f["ht"] * (2 * j + 1)))))
                 for i in range(f["ns"]) for j in range(f["nt"]))
        ok["folga_min"] = min(ok["folga_min"], mn - float(f["v"]))
        area += (f["s1"] - f["s0"]) * (f["b"] - f["a"])
    res["verificacoes"] = ok
    res["area_coberta"] = str(area)
    res["area_alvo"] = str(F(1, 2) * (F(13) - F(43, 50)))
    grade = [(0.5 + 0.5 * i / 40, 0.86 + (13 - 0.86) * j / 1200) for i in range(41) for j in range(1201)]
    v = [abs(zc.zeta(complex(s, t))) for s, t in grade]
    k = v.index(min(v))
    res["min_metade_direita"] = {"min": min(v), "em": grade[k]}
    w = [abs(zc.zeta(complex(1 - s, t))) for s, t in grade]
    res["min_metade_esquerda"] = min(w)
    rho = zc.zero_newton(complex(0.5, 14.13))
    res["primeiro_zero"] = [rho.real, rho.imag]
    res["aviso"] = "ponto flutuante para ζ; o kernel prova |ζ| ≥ 1/50 nos retângulos e ζ ≠ 0 para |Im s| ≤ 13 (Faixa.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
