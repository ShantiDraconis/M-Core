#!/usr/bin/env python3
"""Companheiro numérico da rodada 38: Littlewood sob RH (ATK/ZeroClasses/LittlewoodRH.lean).

Só biblioteca padrão. **Nada aqui é certificado** (e RH não é usada nem testada: os números só ilustram as cotas).

* `tres_circulos`: para `g(z) = e^{z²} + z³` em torno de `c = 0,3`, `log M(r)` é convexa em `log r` (o teorema) em
  `r ∈ [0,5; 2]`;
* `nucleo`: o expoente `a(δ) = log((5/2 − δ)/(3/2))/log((5/2 − δ/2)/(3/2)) < 1` para vários `δ`; e, em `c = 3 + it`,
  `|H(σ + it)| = |log ζ(σ + it) − log ζ(3 + it)|` (ramo contínuo ao longo do segmento horizontal) contra o raio do
  disco onde ele vive;
* `cota_sob_RH`: `max |ζ(σ + it)|^{±1}` em janelas `t ∈ [T, 2T]` para `σ = 0,6; 0,75; 1`, `T = 10, …, 640`: o
  crescimento observado é muito menor que qualquer `|t|^ε` com `ε` moderado (log-log quase plano);
* `young_rpow`: `B x^a ≤ εx + B X₀^a` com `X₀ = (B/ε)^{1/(1−a)} + 1` numa grade.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def expoente(delta):
    return math.log((2.5 - delta) / 1.5) / math.log((2.5 - delta / 2) / 1.5)


def tres_circulos(n=360):
    def g(z):
        return cmath.exp(z * z) + z ** 3

    c = 0.3
    rs = [0.5 + 0.1 * k for k in range(16)]
    logM = [math.log(max(abs(g(c + r * cmath.exp(2j * math.pi * k / n))) for k in range(n))) for r in rs]
    lr = [math.log(r) for r in rs]
    # convexidade: a inclinação não decresce
    incl = [(logM[i + 1] - logM[i]) / (lr[i + 1] - lr[i]) for i in range(len(rs) - 1)]
    return {"convexa": all(b >= a - 1e-9 for a, b in zip(incl, incl[1:])), "inclinacoes": incl}


def log_ramo(t, sigma, passos=400):
    """log ζ(σ + it) − log ζ(3 + it) pelo ramo contínuo no segmento [σ, 3] (soma de incrementos de arg)."""
    tot = 0j
    prev = zc.zeta(complex(3, t))
    for k in range(1, passos + 1):
        s = 3 + (sigma - 3) * k / passos
        cur = zc.zeta(complex(s, t))
        tot += cmath.log(cur / prev)
        prev = cur
    return tot


def janelas():
    out = {}
    for sigma in (0.6, 0.75, 1.0):
        linha = {}
        for T in (10, 20, 40, 80, 160, 320, 640):
            vals = [abs(zc.zeta(complex(sigma, T + T * k / 200))) for k in range(201)]
            linha[str(T)] = {"max_zeta": max(vals), "max_inv": 1 / min(vals)}
        out[str(sigma)] = linha
    return out


def young():
    ok = True
    for a in (0.3, 0.7, 0.95):
        for B in (1.0, 50.0):
            for eps in (0.1, 0.5):
                X0 = (B / eps) ** (1 / (1 - a)) + 1
                C = B * X0 ** a
                for k in range(0, 2001):
                    x = 10 ** (k / 250) - 1
                    if B * x ** a > eps * x + C + 1e-9:
                        ok = False
    return ok


def main(saida=None):
    a = {str(d): expoente(d) for d in (0.5, 0.25, 0.1, 0.01)}
    H = {}
    for t in (14.0, 50.0, 200.0):
        for sigma in (0.6, 1.0, 1.5):
            v = log_ramo(t, sigma)
            H[f"{t}_{sigma}"] = {"abs_H": abs(v), "cota_log36t": math.log(36 * t)}
    res = {"tres_circulos": tres_circulos(), "expoente": a, "H": H, "janelas": janelas(), "young_ok": young()}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_rh.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
