#!/usr/bin/env python3
"""Companheiro numérico da rodada 28: `m₄ > 0` (ATK/ZeroClasses/Quarto*) e a competição `Re(ξ′/ξ)` (Lagarias).

* m₄ = min |ζ(¼ + it)| em ¼ ≤ t ≤ 4 (malha fina) e o espelho |ζ(¾ + it)|;
* as quatro peças do certificado: a cota racional `cotaQ` (frações exatas, a mesma recursão do Lean), a constante
  de Lipschitz B/r, o passo h = (b − a)/(2n), o limiar v = (B/r)h + 1/20 e o menor |ζ| nos centros;
* comparação da cota grosseira com o máximo amostrado de |ζ| na região e de |ζ′| no segmento;
* L(s) = Re(ξ′/ξ)(s): zero na linha, antissimetria L(1 − s̄) = −L(s), sinal positivo amostrado em ½ < σ ≤ 2,
  0,5 ≤ t ≤ 40, e negativo logo à esquerda de um zero artificial fora da linha (modelo (s − ρ)·ξ(s)).
"""
import json
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402
import zeroclasses as zc  # noqa: E402

BT = {0: F(1), 1: F(-1, 2), 2: F(1, 6), 4: F(-1, 30), 6: F(1, 42), 8: F(-1, 30), 10: F(5, 66)}


def bt(j):
    return BT.get(j, F(0))


def pochRQ(R, k):
    p = F(1)
    for i in range(k):
        p *= R + i
    return p


def CbR(M):
    return sum(abs(bt(i)) * math.comb(M, i) for i in range(M + 1))


def cotaQ(N, M, R, d):
    s = F(N) + F(N) / d + F(1, 2)
    s += sum(abs(bt(j)) / math.factorial(j) * pochRQ(R, j - 1) / F(N) ** (j - 1) for j in range(2, M + 1))
    s += pochRQ(R, M) / math.factorial(M) * (CbR(M) / F(N) ** (M - 1) / (M - 1))
    return s


# (a, b, B, R, d, Nc, Mc, n) — os mesmos números de Quarto.lean
PECAS = [(F(1, 4), F(1), F(611, 100), F(667, 500), F(51, 100), 1, 4, 20),
         (F(1), F(2), F(491, 100), F(2293, 1000), F(183, 200), 2, 10, 27),
         (F(2), F(3), F(87, 20), F(3277, 1000), F(229, 125), 2, 10, 24),
         (F(3), F(4), F(119, 25), F(4269, 1000), F(1403, 500), 3, 10, 24)]
R_ = F(6, 25)
DELTA = F(1, 20)


def Lg(s, h=1e-6):
    s = complex(s)
    d = (en.xi(s + h) - en.xi(s - h)) / (2 * h)
    return (d / en.xi(s)).real


def main(saida=None):
    res = {}
    ts = [0.25 + i * 3.75 / 7500 for i in range(7501)]
    v = [abs(zc.zeta(complex(0.25, t))) for t in ts]
    i0 = v.index(min(v))
    res["m4"] = {"min": min(v), "t_min": ts[i0], "max": max(v)}
    w = [abs(zc.zeta(complex(0.75, t))) for t in ts]
    res["espelho_min"] = min(w)
    pecas = []
    for a, b, B, R, d, Nc, Mc, n in PECAS:
        c = cotaQ(Nc, Mc, R, d)
        h = (b - a) / (2 * n)
        vv = B / R_ * h + DELTA
        centros = [a + h * (2 * k + 1) for k in range(n)]
        zc_min = min(abs(zc.zeta(complex(0.25, float(t)))) for t in centros)
        reg = max(abs(zc.zeta(complex(0.25 + float(R_) * x / 6, float(a - R_) + (float(b - a + 2 * R_)) * y / 60)))
                  for x in range(-6, 7) for y in range(61))
        dmax = max(abs((zc.zeta(complex(0.25, t + 1e-5)) - zc.zeta(complex(0.25, t - 1e-5))) / 2e-5)
                   for t in [float(a) + float(b - a) * k / 200 for k in range(201)])
        pecas.append({"a": str(a), "b": str(b), "cotaQ": float(c), "B": str(B), "cota_ok": c <= B,
                      "L=B/r": float(B / R_), "n": n, "h": str(h), "v": float(vv), "min_zeta_centros": zc_min,
                      "folga": zc_min - float(vv), "max_zeta_regiao": reg, "max_dzeta_segmento": dmax,
                      "fecha": c <= B and (b - a) == 2 * h * n and zc_min > float(vv)})
    res["pecas"] = pecas
    res["centros"] = sum(p["n"] for p in pecas)
    # Lagarias
    linha = [abs(Lg(complex(0.5, t))) for t in (3.0, 7.5, 10.0, 20.0, 33.3)]
    anti = max(abs(Lg(complex(1 - s, t)) + Lg(complex(s, t)))
               for s in (0.6, 0.75, 0.9, 1.3) for t in (2.0, 9.0, 17.5, 26.0))
    pos = [Lg(complex(0.5 + 1.5 * i / 30, 0.5 + 39.5 * j / 79)) for i in range(1, 31) for j in range(80)]
    rho = complex(0.7, 30.0)

    def mod(s):
        return (s - rho) * en.xi(s)

    def Lmod(s, h=1e-6):
        dd = (mod(s + h) - mod(s - h)) / (2 * h)
        return (dd / mod(s)).real
    res["lagarias"] = {"max|L(1/2+it)|": max(linha), "max|L(1-s)+L(s)|": anti,
                       "pontos": len(pos), "positivos": sum(x > 0 for x in pos), "min": min(pos),
                       "modelo_fora": {"rho": [rho.real, rho.imag],
                                       "L(rho-h)": [Lmod(rho - hh) for hh in (0.1, 0.05, 0.01)]}}
    res["aviso"] = "ponto flutuante para ζ e ξ; o kernel prova m₄ ≥ 1/20 e as leis de L (Quarto.lean, Lagarias.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
