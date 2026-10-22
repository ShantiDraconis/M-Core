#!/usr/bin/env python3
"""1/2 como incógnita: o sistema Re ζ(β+iγ) = 0, Im ζ(β+iγ) = 0 com β e γ livres.

Nada é fixado em 1/2. O script:
1. conta os zeros em retângulos β ∈ [−1, 2], γ ∈ [γa, γb] pelo princípio do argumento
   (variação do argumento de ζ na borda, amostragem adaptativa);
2. resolve o sistema por Newton complexo a partir de sementes espalhadas pela região toda;
3. confere de forma independente as trocas de sinal de Z(t) na reta (Riemann–Siegel θ);
4. mede como ζ se comporta fora de 1/2 em cada zero: |ζ(1/2+ε+iγ_n)| / (|ε|·|ζ'(ρ_n)|);
5. traça o perfil m(β) = min_γ |ζ(β+iγ)| e as curvas Re ζ = 0, Im ζ = 0.

Ponto flutuante (numpy), sem certificação intervalar: ilustração, não prova.
Uso: python3 zero_incognito.py <dir_saida> [gamma_max]
"""
import math, json, os, sys
import numpy as np
from scipy.special import loggamma
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bohr_landau_material import zeta

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
GMAX = float(sys.argv[2]) if len(sys.argv) > 2 else 100.0
os.makedirs(OUT, exist_ok=True)


def dzeta(s, h=1e-6):
    return (zeta(s + h) - zeta(s - h)) / (2 * h)


def var_arg(path):
    """Variação do argumento de ζ ao longo de uma poligonal, refinando até passos < π/8."""
    total = 0.0
    for a, b in zip(path[:-1], path[1:]):
        n = max(8, int(abs(b - a) * 20))
        while True:
            pts = a + (b - a) * np.linspace(0, 1, n + 1)
            v = zeta(pts)
            d = np.angle(v[1:] / v[:-1])
            if np.max(np.abs(d)) < math.pi / 8:
                break
            n *= 2
            if n > 2_000_000:
                raise RuntimeError("amostragem não convergiu (zero na borda?)")
        total += d.sum()
    return total


def conta_argumento(b0, b1, g0, g1):
    path = [complex(b0, g0), complex(b1, g0), complex(b1, g1), complex(b0, g1), complex(b0, g0)]
    return var_arg(path) / (2 * math.pi)


def newton_livre(b0, b1, g0, g1):
    bs = np.linspace(b0 + 0.05, b1 - 0.05, 13)
    gs = np.arange(g0 + 0.25, g1, 0.5)
    s = (bs[:, None] + 1j * gs[None, :]).ravel()
    for _ in range(60):
        f, df = zeta(s), dzeta(s)
        step = f / df
        big = np.abs(step) > 0.5
        step[big] *= 0.5 / np.abs(step[big])
        s = s - step
    f = np.abs(zeta(s))
    ok = (f < 1e-9) & (s.real > b0) & (s.real < b1) & (s.imag > g0) & (s.imag < g1)
    raizes = []
    for z in s[ok]:
        if all(abs(z - r) > 1e-6 for r in raizes):
            raizes.append(z)
    raizes.sort(key=lambda z: z.imag)
    # polimento final
    raizes = np.array(raizes)
    for _ in range(5):
        raizes = raizes - zeta(raizes) / dzeta(raizes)
    return raizes, len(s)


def Z(t):
    t = np.asarray(t, dtype=float)
    theta = np.imag(loggamma(0.25 + 0.5j * t)) - 0.5 * t * math.log(math.pi)
    return np.real(np.exp(1j * theta) * zeta(0.5 + 1j * t))


def trocas_de_sinal(g0, g1, h=0.002):
    t = np.arange(g0, g1, h)
    z = Z(t)
    return int(np.sum(np.sign(z[1:]) != np.sign(z[:-1])))


def main():
    rel = {}
    # 1. contagem livre por faixas de altura
    faixas = []
    total_arg = 0
    for g0 in np.arange(1.0, GMAX, 10.0):
        g1 = min(g0 + 10.0, GMAX)
        c = conta_argumento(-1.0, 2.0, g0, g1)
        faixas.append({"gamma": [g0, g1], "contagem_argumento": c})
        total_arg += round(c)
        print(f"γ∈[{g0:.0f},{g1:.0f}]: zeros em β∈[−1,2] pelo argumento = {c:.6f}", flush=True)
    rel["faixas"] = faixas
    # 2. Newton livre
    raizes, nsem = newton_livre(-1.0, 2.0, 1.0, GMAX)
    eps = raizes.real - 0.5
    print(f"Newton livre: {nsem} sementes, {len(raizes)} soluções; max|β−1/2| = {np.max(np.abs(eps)):.2e}", flush=True)
    # 3. reta, independente
    trocas = trocas_de_sinal(1.0, GMAX)
    print(f"trocas de sinal de Z(t) em (1, {GMAX:.0f}): {trocas}; contagem pelo argumento: {total_arg}", flush=True)
    rel["newton"] = {"sementes": nsem, "solucoes": len(raizes),
                     "beta": raizes.real.tolist(), "gamma": raizes.imag.tolist(),
                     "max_abs_beta_menos_meio": float(np.max(np.abs(eps)))}
    rel["contagem_argumento_total"] = total_arg
    rel["trocas_de_sinal_Z"] = trocas
    # 4. comportamento fora de 1/2
    comp = []
    for r in raizes[:10]:
        d = abs(dzeta(np.array([r]))[0])
        linha = {"gamma": r.imag, "abs_dzeta": d}
        for e in (0.001, 0.01, 0.1, 0.25):
            v = abs(zeta(np.array([complex(0.5 + e, r.imag)]))[0])
            linha[f"eps={e}"] = v
            linha[f"razao eps={e}"] = v / (e * d)
        comp.append(linha)
    rel["fora_de_meio"] = comp
    for c in comp[:5]:
        print(f"γ={c['gamma']:.6f} |ζ'|={c['abs_dzeta']:.4f} |ζ(1/2+ε+iγ)| ε=0.01: {c['eps=0.01']:.5f} (razão {c['razao eps=0.01']:.4f}), ε=0.25: {c['eps=0.25']:.4f}", flush=True)
    # 5. perfil m(β) = min_γ |ζ(β+iγ)|, γ ∈ [10, GMAX]
    betas = np.round(np.arange(0.0, 1.0001, 0.02), 4)
    perfil = []
    janelas = [np.linspace(g - 0.6, g + 0.6, 1201) for g in raizes.imag if g >= 10]
    grade = np.arange(10.0, GMAX, 0.05)
    for b in betas:
        m = np.min(np.abs(zeta(b + 1j * grade)))
        for jw in janelas:
            m = min(m, float(np.min(np.abs(zeta(b + 1j * jw)))))
        perfil.append(m)
    rel["perfil_min"] = {"beta": betas.tolist(), "min_abs_zeta": perfil}
    print("m(β): " + "  ".join(f"{b:.2f}:{m:.4f}" for b, m in zip(betas[::5], perfil[::5])), flush=True)
    json.dump(rel, open(os.path.join(OUT, "zero_incognito.json"), "w"), indent=1, default=float)
    # figura
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    B, G = np.meshgrid(np.linspace(-1, 2, 601), np.linspace(0.5, 50, 1981))
    V = zeta(B + 1j * G)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6.2), gridspec_kw={"width_ratios": [1.15, 1]})
    ax[0].contour(B, G, V.real, levels=[0], colors="#2563eb", linewidths=1.1)
    ax[0].contour(B, G, V.imag, levels=[0], colors="#ea580c", linewidths=1.1)
    sel = raizes.imag <= 50
    ax[0].plot(raizes.real[sel], raizes.imag[sel], "o", ms=5, mfc="none", mec="#111827", mew=1.2)
    ax[0].axvline(0.5, color="#6b7280", lw=0.6, ls=":")
    ax[0].set_xlabel("β = Re s (incógnita)")
    ax[0].set_ylabel("γ = Im s (incógnita)")
    ax[0].set_title("Re ζ = 0 (azul) e Im ζ = 0 (laranja): os zeros são os cruzamentos")
    ax[0].set_xlim(-1, 2); ax[0].set_ylim(0.5, 50)
    ax[1].plot(betas, perfil, "-o", ms=3, color="#111827")
    ax[1].axvline(0.5, color="#6b7280", lw=0.6, ls=":")
    ax[1].set_xlabel("β")
    ax[1].set_ylabel(f"min sobre γ ∈ [10, {GMAX:.0f}] de |ζ(β+iγ)|")
    ax[1].set_title("Fora de β = 1/2 o mínimo é positivo")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "zero_incognito.png"), dpi=150)
    print("figura gravada", flush=True)


if __name__ == "__main__":
    main()
