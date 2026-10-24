#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Componentes (rodada 22): real × imaginário, mínimos, contagem.

Só biblioteca padrão. **Nada aqui é certificado.**

* Cauchy–Riemann no 1º zero por diferenças: ∂σu = Re ζ′, ∂tu = −Im ζ′, …; gradientes ortogonais;
* princípio do módulo mínimo na malha: os mínimos locais de |ζ| em 0,05 ≤ σ ≤ 0,95, 10 ≤ t ≤ 100 caem **todos**
  sobre zeros da linha (29 zeros, 29 mínimos), e na faixa 0,55 ≤ σ ≤ 0,95 **não há** mínimo interior — o mínimo
  fica na borda σ = 0,55;
* resíduo (s − ρ₁)ζ′/ζ → 1;
* Riemann–von Mangoldt: N(T) ≈ (T/2π)(log(T/2π) − 1) + 7/8; em T = 10¹⁰⁰ o termo principal é ≈ 3,62·10¹⁰¹
  (não 10¹⁰²); espaçamento médio 2π/log(T/2π);
* modelo cosh(s − ½): zeros em ½ ± i(2k+1)π/2, todos na linha.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402


def dz(s, h=1e-6):
    return (zc.zeta(s + h) - zc.zeta(s - h)) / (2 * h)


def cauchy_riemann(s, h=1e-6):
    u = lambda z: zc.zeta(z).real  # noqa: E731
    v = lambda z: zc.zeta(z).imag  # noqa: E731
    us = (u(s + h) - u(s - h)) / (2 * h)
    ut = (u(s + 1j * h) - u(s - 1j * h)) / (2 * h)
    vs = (v(s + h) - v(s - h)) / (2 * h)
    vt = (v(s + 1j * h) - v(s - 1j * h)) / (2 * h)
    return us, ut, vs, vt


def N_principal(T):
    x = T / (2 * math.pi)
    return x * (math.log(x) - 1) + 7 / 8


def N_principal_log(log10T):
    """log10 do termo principal de N(T) para T = 10^log10T (sem overflow)."""
    lnT = log10T * math.log(10)
    ln_x = lnT - math.log(2 * math.pi)
    return (ln_x + math.log(ln_x - 1)) / math.log(10)


def malha(s0, s1, t0, t1, hs, ht):
    ns, nt = int(round((s1 - s0) / hs)), int(round((t1 - t0) / ht))
    sig = [s0 + hs * i for i in range(ns + 1)]
    tt = [t0 + ht * k for k in range(nt + 1)]
    A = [[abs(zc.zeta(complex(s, t))) for t in tt] for s in sig]
    return sig, tt, A


def minimos_locais(sig, tt, A):
    out = []
    for i in range(1, len(sig) - 1):
        for k in range(1, len(tt) - 1):
            a = A[i][k]
            if all(a < A[i + di][k + dk] for di in (-1, 0, 1) for dk in (-1, 0, 1) if di or dk):
                out.append((sig[i], tt[k], a))
    return out


def main(saida=None):
    res = {}
    rho = zc.zero_newton(complex(0.5, 14.13))
    w = dz(rho)
    us, ut, vs, vt = cauchy_riemann(rho)
    res["cauchy_riemann_rho1"] = {"zeta'": [w.real, w.imag], "u_sigma": us, "u_t": ut, "v_sigma": vs, "v_t": vt,
                                  "u_sigma-v_t": us - vt, "u_t+v_sigma": ut + vs,
                                  "grad_u.grad_v": us * vs + ut * vt,
                                  "|grad_u|^2-|zeta'|^2": us * us + ut * ut - abs(w) ** 2}
    res["residuo_rho1"] = [format(abs(d * dz(rho + d) / zc.zeta(rho + d) - 1), ".2e") for d in (1e-2, 1e-3, 1e-4)]
    # mínimos locais na faixa (incluindo a linha) e só à direita
    sig, tt, A = malha(0.05, 0.95, 10.0, 100.0, 0.05, 0.02)
    mins = minimos_locais(sig, tt, A)
    zeros = []
    for (_, t, _) in mins:
        r = zc.zero_newton(complex(0.5, t))
        zeros.append([r.real, r.imag])
    res["minimos_faixa"] = {"malha": "σ 0,05:0,05:0,95 × t 10:0,02:100", "quantidade": len(mins),
                            "sigma_dos_minimos": sorted({round(m[0], 3) for m in mins}),
                            "zeros_por_newton": [[round(a, 10), round(b, 6)] for a, b in zeros]}
    sig2, tt2, A2 = malha(0.55, 0.95, 10.0, 100.0, 0.01, 0.02)
    mins2 = minimos_locais(sig2, tt2, A2)
    i, k = min(((i, k) for i in range(len(sig2)) for k in range(len(tt2))), key=lambda p: A2[p[0]][p[1]])
    res["faixa_direita"] = {"minimos_interiores": len(mins2), "minimo_global": A2[i][k],
                            "onde": [sig2[i], tt2[k]], "na_borda": i in (0, len(sig2) - 1) or k in (0, len(tt2) - 1)}
    # contagem de Riemann–von Mangoldt
    cont = {}
    for nome, T in (("10^3", 1e3), ("10^12", 1e12), ("3·10^12", 3000175332800.0), ("10^23", 1e23)):
        cont[nome] = {"N_principal": format(N_principal(T), ".6g"),
                      "espacamento_medio": format(2 * math.pi / math.log(T / (2 * math.pi)), ".6g")}
    cont["10^100"] = {"log10_N_principal": N_principal_log(100),
                      "N_principal": "≈ " + format(10 ** (N_principal_log(100) - 101), ".4f") + "·10^101",
                      "espacamento_medio": format(2 * math.pi / (100 * math.log(10) - math.log(2 * math.pi)), ".6g")}
    res["riemann_von_mangoldt"] = cont
    # modelo cosh(s − ½)
    zs = [0.5 + 1j * (2 * k + 1) * math.pi / 2 for k in range(-3, 3)]
    res["cosh_modelo"] = {"max|F(zero)|": max(abs(cmath.cosh(z - 0.5)) for z in zs),
                          "re_dos_zeros": sorted({z.real for z in zs}),
                          "F(1-s)-F(s)": abs(cmath.cosh(0.5 - 0.3 - 2j) - cmath.cosh(0.3 + 2j - 0.5))}
    res["aviso"] = "ponto flutuante; o kernel prova as leis (Componentes.lean), não estes números"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
