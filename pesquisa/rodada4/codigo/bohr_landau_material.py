#!/usr/bin/env python3
"""Lado material da prova de Bohr–Landau (ATK.BLProva.bohrLandau).

1. Média quadrática (1/Y)∫_{1/2}^{Y}|ζ(σ+it)|² dt contra ζ(2σ) (o teorema provado diz só O(Y)).
2. Constante efetiva M para σ ∈ [σ0, 4], σ0 = 1/2 + δ/2, Y ≤ Ymax (numérica, não certificada).
3. Lado de Jensen: (média(|ζ|², 2+iy, R) + L0)/λ por janela, e a constante C que a prova produz.

ζ por Euler–Maclaurin de ordem 2K (numpy), conferida em ζ(2), no 1º zero e em ζ(1/2+10i).
"""
import math, json, sys
import numpy as np

B2K = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510, 43867/798, -174611/330]

def zeta(s, N=None, K=8):
    s = np.asarray(s, dtype=complex)
    if N is None:
        N = int(0.5 * np.max(np.abs(s))) + 40
    n = np.arange(1, N, dtype=float)
    logn = np.log(n)
    out = np.empty(s.shape, dtype=complex)
    flat, res = s.ravel(), out.ravel()
    for i0 in range(0, flat.size, 2000):
        ss = flat[i0:i0 + 2000]
        part = np.exp(-np.outer(ss, logn)).sum(axis=1)
        Ns = np.exp(-ss * math.log(N))
        part += N * Ns / (ss - 1) + Ns / 2
        poch = ss.copy()               # (s)_{2k-1}
        Npow = Ns / N                  # N^{-s-1}
        fact = 2.0                     # (2k)!
        for k in range(1, K + 1):
            part += B2K[k - 1] / fact * poch * Npow
            poch = poch * (ss + 2 * k - 1) * (ss + 2 * k)
            Npow = Npow / (N * N)
            fact *= (2 * k + 1) * (2 * k + 2)
        res[i0:i0 + 2000] = part
    return out

def controles():
    z2 = zeta(np.array([2.0]))[0]
    z0 = zeta(np.array([0.5 + 14.134725141734693j]))[0]
    z10 = zeta(np.array([0.5 + 10j]))[0]
    return {"zeta(2)-pi^2/6": abs(z2 - math.pi ** 2 / 6), "|zeta(rho_1)|": abs(z0),
            "zeta(1/2+10i)": [z10.real, z10.imag]}

def media(sigma, Y, h=0.005):
    t = np.arange(0.5, Y + h / 2, h)
    v = np.abs(zeta(sigma + 1j * t)) ** 2
    cum = np.concatenate([[0.0], np.cumsum((v[1:] + v[:-1]) * h / 2)])   # trapézio
    return t, cum

def main():
    rel = {"controles": controles()}
    print("controles:", rel["controles"], flush=True)
    sigmas = [0.55, 0.6, 0.625, 0.75, 1.0, 1.5, 2.0, 4.0]
    Ys = [10, 50, 100, 200, 400]
    tab = {}
    for sg in sigmas:
        t, cum = media(sg, max(Ys))
        z2s = zeta(np.array([2 * sg]))[0].real
        lin = {}
        for Y in Ys:
            i = int(round((Y - 0.5) / 0.005))
            lin[str(Y)] = cum[i] / Y
        mask = t >= 1
        sup = float(np.max(cum[mask] / t[mask]))
        tab[str(sg)] = {"zeta(2sigma)": z2s, "media/Y": lin, "sup_{1<=Y<=400} I(Y)/Y": sup}
        print(f"σ={sg}: ζ(2σ)={z2s:.4f}  " + "  ".join(f"Y={Y}:{lin[str(Y)]:.4f}" for Y in Ys) + f"  sup={sup:.4f}", flush=True)
    rel["media_quadratica"] = tab
    # lado de Jensen com δ = 1/4
    d = 0.25
    R, r = 1.5 - d / 2, 1.5 - 3 * d / 4
    lam = math.log(R / r)
    L0 = -math.log(2 - math.pi ** 2 / 6)
    th = np.linspace(0, 2 * math.pi, 4096, endpoint=False)
    jan = []
    for y in [2, 5, 10, 14.13, 20, 50, 100, 200, 400]:
        z = 2 + 1j * y + R * np.exp(1j * th)
        avg = float(np.mean(np.abs(zeta(z)) ** 2))
        jan.append({"y": y, "media_|zeta|^2": avg, "cota_por_janela": (avg + L0) / lam})
        print(f"y={y}: média(|ζ|²)={avg:.4f}  cota de zeros na janela={(avg + L0) / lam:.1f}", flush=True)
    Mnum = tab["0.625"]["sup_{1<=Y<=400} I(Y)/Y"]
    Cnum = (5 * Mnum / 2 + L0) / (lam * d)
    rel["jensen"] = {"delta": d, "R": R, "r": r, "lambda": lam, "L0": L0, "janelas": jan,
                     "M_numerico(sigma0=0.625)": Mnum, "C_da_prova_com_M_numerico": Cnum,
                     "log10_T_a_partir_do_qual_C*T_<_(T/2pi)log(T/2pie)": (2 * math.pi * Cnum + 1 + math.log(2 * math.pi)) / math.log(10)}
    print(f"λ={lam:.5f} L0={L0:.5f} M≈{Mnum:.4f} C≈{Cnum:.1f} log10 T*≈{rel['jensen']['log10_T_a_partir_do_qual_C*T_<_(T/2pi)log(T/2pie)']:.0f}")
    json.dump(rel, open(sys.argv[1] if len(sys.argv) > 1 else "bohr_landau_material.json", "w"), indent=1, default=float)

if __name__ == "__main__":
    main()
