#!/usr/bin/env python3
"""Companheiro numérico de ATK/GamaCotas.lean, ATK/GramExato.lean, ATK/GramDois.lean,
ATK/BarreiraModelos.lean e ATK/ZeroSegundo.lean / ZeroTerceiro.lean.

Só biblioteca padrão (Decimal/Fraction). Nada aqui é certificado: os teoremas estão no kernel.

* γ por u_n = H_n − log(n+½) − 1/(24(n+1)²) (decrescente) e l_n = H_{n+1} − log(n+3/2) − 1/(24(n+1)(n+2))
  (crescente): em n = 40 / 39 dão 0,5772156 < γ < 0,5772163 (`gama_cotas`).
* G₁₁ = log 2π − γ; G₁₂ = ¾(log 2π − γ) − ¼ log 2, conferido pela forma fechada Pc(K) das somas de pares
  (`integral_pares`) com K grande; D₁, D₂ exatos; D_∞ ≤ D₂ < 0,29.
* C₀ = 2 + γ − log 4π; o ajuste de dois pontos com D₂₅₆, D₈₀₀₀ relatados (intercepto < 0).
* Tabela da barreira B(β, γ) = (2β−1)((1−β)²+γ²)/(β²+γ²)².
* 2º e 3º zeros: troca de sinal de Θ(−t²) = Ξ(t) (coeficientes de jensen.py).
"""
import json
import os
import sys
from decimal import Decimal as D, getcontext
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

getcontext().prec = 60
GAMMA = D("0.57721566490153286060651209008240243104215933593992")
PI = D("3.14159265358979323846264338327950288419716939937510")
LN2 = D(2).ln()


def harmonic(n):
    return sum(Fraction(1, k) for k in range(1, n + 1))


def dec(q):
    return D(q.numerator) / D(q.denominator)


def u(n):
    return dec(harmonic(n)) - (D(n) + D(1) / 2).ln() - D(1) / (24 * (n + 1) ** 2)


def l(n):
    return dec(harmonic(n + 1)) - (D(n) + D(3) / 2).ln() - D(1) / (24 * (n + 1) * (n + 2))


def gram():
    L = (2 * PI).ln()
    g11 = L - GAMMA
    g12 = D(3) / 4 * g11 - LN2 / 4
    g22 = g11 / 2
    b1 = 1 - GAMMA
    b2 = (LN2 + 1 - GAMMA) / 2
    num = g22 * b1 * b1 - 2 * g12 * b1 * b2 + g11 * b2 * b2
    det = g11 * g22 - g12 * g12
    return {"G11": g11, "G12": g12, "G22": g22, "b1": b1, "b2": b2,
            "D1": 1 - b1 * b1 / g11, "D2": 1 - num / det, "det": det}


def Pc(K):
    """Forma fechada de ∫_{1/(2K+1)}^1 {1/t}{1/(2t)} dt (`ATK.GramDois.Pc`)."""
    lf2 = sum(D(j).ln() for j in range(2, 2 * K + 1))
    lf1 = sum(D(j).ln() for j in range(2, K + 1))
    HK = dec(harmonic(K)) if K < 400 else sum(D(1) / j for j in range(1, K + 1))
    H2 = dec(harmonic(2 * K + 1)) if K < 400 else sum(D(1) / j for j in range(1, 2 * K + 2))
    return (2 * K + D(1) / 2 - 2 * K * (2 * D(K) + 1).ln() + lf2 / 2 + K * LN2 + lf1 - HK / 4 - H2 / 2)


def passos12(M):
    """Soma direta dos degraus J(n, ⌊(n+1)/2⌋), n < M (`integral_step_rho12`)."""
    s = D(0)
    for n in range(M):
        b = D((n + 1) // 2)
        s += D(1) / 2 - (b + D(n + 1) / 2) * ((D(n) + 2).ln() - (D(n) + 1).ln()) + b / (n + 2)
    return s


def barreira(b, g):
    b, g = D(b), D(g)
    return (2 * b - 1) * ((1 - b) ** 2 + g * g) / (b * b + g * g) ** 2


def ajuste():
    D256, D8000 = D("0.0082337162772"), D("0.0050691202")
    L0, L1 = D(256).ln(), D(8000).ln()
    a = (D8000 * L1 - D256 * L0) / (L1 - L0)
    return {"produto_256": D256 * L0, "produto_8000": D8000 * L1, "intercepto": a}


def zeros_theta():
    import jensen
    _, a, _ = jensen.coeficientes(60, D(1) / 64)

    def bis(lo, hi, it=60):
        flo = jensen.Theta(a, -(lo * lo))
        for _ in range(it):
            mid = (lo + hi) / 2
            fm = jensen.Theta(a, -(mid * mid))
            if (fm > 0) == (flo > 0):
                lo, flo = mid, fm
            else:
                hi = mid
        return (lo + hi) / 2

    return bis(D("21.02"), D("21.03")), bis(D("25.01"), D("25.02"))


def main(saida=None):
    G = gram()
    res = {
        "u40": str(u(40))[:20], "l39": str(l(39))[:20],
        "gama_cotas": [str(D("0.5772156")), str(D("0.5772163"))],
        "G11": str(G["G11"])[:22], "G12": str(G["G12"])[:22], "D1": str(G["D1"])[:22], "D2": str(G["D2"])[:22],
        "Pc_2000_mais_meio": str(Pc(2000) + D(1) / 2)[:22],
        "C0": str(2 + GAMMA - (4 * PI).ln())[:22],
        "ajuste": {k: str(v)[:22] for k, v in ajuste().items()},
        "barreira": {f"{b}@{g}": str(barreira(b, g))[:16] for b in ("0.6", "0.75", "0.9")
                     for g in ("14.134725", "100")},
    }
    try:
        z2, z3 = zeros_theta()
        res["zero2"], res["zero3"] = str(z2)[:16], str(z3)[:16]
    except Exception as e:  # pragma: no cover
        res["zeros_erro"] = repr(e)
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
