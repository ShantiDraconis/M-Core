#!/usr/bin/env python3
"""O modelo ρ_N = A_N/B_N com a regra do kernel: ρ_N = zero de ζ_N perto de ρ_k, onde
ζ_N(s) = Σ_{m=1}^{N} m^{−s} + N^{1−s}/(s−1)   (ATK.TruncamentoZero.zetaN).

Mede ε_N = Re ρ_N − 1/2, o resíduo verdadeiro |ζ(ρ_N)|, a cota do kernel |s|·N^{−σ}/σ
(`residuo_trunc`) e a previsão de primeira ordem ρ_N − ρ ≈ −N^{−ρ}/(2ζ′(ρ)).
Ponto flutuante; ilustração.  Uso: python3 truncamento_zero.py <dir_saida>
"""
import math, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bohr_landau_material import zeta

OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def zN(N, s):
    m = np.arange(1, N + 1, dtype=float)
    lm = np.log(m)
    t = np.exp(-s * lm)
    v = t.sum() + N ** (1 - s) / (s - 1)
    d = -(lm * t).sum() + N ** (1 - s) * (-math.log(N) * (s - 1) - 1) / (s - 1) ** 2
    return v, d


def raiz_trunc(N, s0):
    s = s0
    for _ in range(40):
        v, d = zN(N, s)
        step = v / d
        if abs(step) > 0.3:
            step *= 0.3 / abs(step)
        s -= step
        if abs(step) < 1e-15:
            break
    return s, abs(zN(N, s)[0])


def raiz_exata(s0):
    s = s0
    for _ in range(30):
        f = zeta(np.array([s]))[0]
        d = (zeta(np.array([s + 1e-6]))[0] - zeta(np.array([s - 1e-6]))[0]) / 2e-6
        s -= f / d
    return s, d


def main():
    alvos = [14.134725141734694, 21.022039638771555, 25.010857580145689]
    Ns = sorted(set(list(range(2, 201)) + [int(round(10 ** (k / 20))) for k in range(46, 101)]))
    rel = {"zetaN": "Σ_{m=1}^{N} m^{-s} + N^{1-s}/(s-1)", "zeros": []}
    for g in alvos:
        rho, dz = raiz_exata(complex(0.5, g))
        linhas = []
        for N in Ns:
            r, res = raiz_trunc(N, rho)
            if abs(r - rho) > 0.5 or res > 1e-10:
                continue
            true_res = abs(zeta(np.array([r]))[0])
            prev = -N ** (-rho) / (2 * dz)
            cota = abs(r) * N ** (-r.real) / r.real
            linhas.append({"N": N, "beta": r.real, "gamma": r.imag, "eps": r.real - 0.5,
                           "abs_rhoN_menos_rho": abs(r - rho), "abs_zeta_rhoN": true_res,
                           "cota_kernel": cota, "eps_previsto": prev.real,
                           "abs_previsto": abs(prev)})
        sinais = [1 if l["eps"] > 0 else -1 for l in linhas]
        trocas = sum(1 for a, b in zip(sinais, sinais[1:]) if a != b)
        zero_eps = sum(1 for l in linhas if l["eps"] == 0.0)
        info = {"rho": [rho.real, rho.imag], "abs_dzeta": abs(dz), "linhas": linhas,
                "trocas_de_sinal_de_eps": trocas, "eps_exatamente_zero": zero_eps}
        rel["zeros"].append(info)
        print(f"ρ = {rho.real:.15f} + {rho.imag:.12f}i  |ζ'|={abs(dz):.4f}  N convergidos: {len(linhas)}  "
              f"trocas de sinal de ε_N: {trocas}  ε_N = 0 exato: {zero_eps}", flush=True)
        for l in linhas:
            if l["N"] in (10, 100, 1000, 10000, 100000):
                print(f"  N={l['N']:>6}: ε_N={l['eps']:+.3e} (prev {l['eps_previsto']:+.3e})  |ρ_N−ρ|={l['abs_rhoN_menos_rho']:.3e} "
                      f"(prev {l['abs_previsto']:.3e})  |ζ(ρ_N)|={l['abs_zeta_rhoN']:.3e}  cota={l['cota_kernel']:.3e}", flush=True)
    json.dump(rel, open(os.path.join(OUT, "truncamento_zero.json"), "w"), indent=1, default=float)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 5.2))
    cores = ["#2563eb", "#ea580c", "#059669"]
    for info, c in zip(rel["zeros"], cores):
        N = np.array([l["N"] for l in info["linhas"]])
        e = np.array([l["eps"] for l in info["linhas"]])
        ax.plot(N, e, "-", color=c, lw=1, label=f"perto de ρ com γ = {info['rho'][1]:.3f}")
        ax.plot(N, N ** -0.5 / (2 * info["abs_dzeta"]), ":", color=c, lw=0.8)
        ax.plot(N, -N ** -0.5 / (2 * info["abs_dzeta"]), ":", color=c, lw=0.8)
    ax.axhline(0, color="#111827", lw=0.6)
    ax.set_xscale("log")
    ax.set_xlabel("N (termos do truncamento)")
    ax.set_ylabel("ε_N = Re ρ_N − 1/2")
    ax.set_title("Zeros de ζ_N: ε_N ≠ 0 e ε_N → 0; pontilhado = ±N^(−1/2)/(2|ζ′(ρ)|)")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "truncamento_zero.png"), dpi=150)


if __name__ == "__main__":
    main()
