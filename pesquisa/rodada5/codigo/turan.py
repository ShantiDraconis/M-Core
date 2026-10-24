#!/usr/bin/env python3
"""Companheiro numérico de ATK/TuranDispersao.lean (rodada 15).

Só biblioteca padrão; nada é certificado e nada prova HR.

* Φ′ termo a termo: ∂ᵤphiT(c,u) = (−8w³ + 30w² − 15w)e^{u/2−w}, w = ce^{2u} (`hasDerivAt_phiT`), conferido por
  diferenças finitas.
* O lema de Csordas (`BUILD_PENDING` no kernel): ψ(u) = −Φ′(u)/(uΦ(u)) é crescente — verificado numa malha de (0, 2].
* A identidade de dispersão de ordem 2 (`turan_disp`):
  (2m+3)γ_{m+1}² − (2m+1)γ_mγ_{m+2} = ½∬K(t)K(s)(ts)^{2m+2}(t²−s²)(ψ(t)−ψ(s)), γ_k = ∫u^{2k}Φ,
  conferida por quadratura (1D e 2D) para m = 0, 1, 2.
"""
import json
import math
import sys


def phi_e_phid(u, nmax=10):
    s = d = 0.0
    for n in range(1, nmax):
        c = math.pi * n * n
        w = c * math.exp(2 * u)
        h = math.exp(u / 2 - w)
        s += (4 * w * w - 6 * w) * h
        d += (-8 * w ** 3 + 30 * w * w - 15 * w) * h
    return s, d


def psi(u):
    s, d = phi_e_phid(u)
    return -d / (u * s)


def gam(k, N=4000, U=2.5):
    h = U / N
    tot = 0.0
    for i in range(N + 1):
        u = i * h
        p = 1 if i in (0, N) else (4 if i % 2 else 2)
        tot += (u ** (2 * k) if u > 0 or k > 0 else 1.0) * phi_e_phid(u)[0] * p
    return tot * h / 3


def dispersao(m, N=300, U=2.2):
    """½∬ K(t)K(s)(ts)^{2m+2}(t²−s²)(ψ(t)−ψ(s)) por Simpson 2D."""
    h = U / N
    pts = [i * h for i in range(N + 1)]
    pesos = [1 if i in (0, N) else (4 if i % 2 else 2) for i in range(N + 1)]
    vals = []
    for u in pts:
        if u == 0:
            vals.append((0.0, 0.0))
        else:
            s, _ = phi_e_phid(u)
            vals.append((s, psi(u)))
    tot = 0.0
    for i, t in enumerate(pts):
        Kt, pt = vals[i]
        if t == 0:
            continue
        for j, s in enumerate(pts):
            Ks, ps = vals[j]
            if s == 0:
                continue
            tot += pesos[i] * pesos[j] * Kt * Ks * (t * s) ** (2 * m + 2) * (t * t - s * s) * (pt - ps)
    return 0.5 * tot * (h / 3) ** 2


def main(saida=None):
    u, e = 0.3, 1e-6
    fd = (phi_e_phid(u + e)[0] - phi_e_phid(u - e)[0]) / (2 * e)
    malha = [k * 0.0005 for k in range(1, 4001)]
    ps = [psi(x) for x in malha]
    g = [gam(k) for k in range(6)]
    disp = {}
    for m in (0, 1, 2):
        lhs = (2 * m + 3) * g[m + 1] ** 2 - (2 * m + 1) * g[m] * g[m + 2]
        disp[str(m)] = [format(lhs, ".10g"), format(dispersao(m), ".10g")]
    res = {
        "Phi'_formula_vs_dif_finita_u=0.3": [format(phi_e_phid(u)[1], ".12g"), format(fd, ".12g")],
        "psi_crescente_(0,2]": all(ps[i + 1] > ps[i] for i in range(len(ps) - 1)),
        "psi(0.0005),psi(1),psi(2)": [format(ps[0], ".8g"), format(psi(1.0), ".8g"), format(ps[-1], ".8g")],
        "dispersao_m:[lado_esquerdo,integral_dupla]": disp,
        "aviso": "verificação finita; o lema de Csordas é BUILD_PENDING e PF∞ é OPEN_MATH (equivale a HR)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
