#!/usr/bin/env python3
"""ATK-CEZ (Closed Math): constantes, conferência numérica das leis provadas e figuras.

O kernel prova as leis (ATK/ClosedMathCEZ.lean); aqui elas são conferidas em ponto flutuante
nos zeros reais de ζ (até γ = 300, rodada 4) e em zeros construídos (f_a, G_λ), e desenhadas
no plano, no plano trocado, na esfera de Riemann, no cilindro e no cone.
Uso: python3 cez.py <dir_saida>
"""
import json, math, os, sys, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zeta_em import zeta

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
AQUI = os.path.dirname(os.path.abspath(__file__))
R4 = os.path.join(AQUI, "..", "..", "rodada4", "dados")

T = lambda s: 1j * np.conj(s)
R = lambda s: 1 - np.conj(s)
D = lambda s: np.real(s) - 0.5
def P(s):
    a = 1 + abs(s) ** 2
    return np.array([2 * s.real / a, 2 * s.imag / a, (abs(s) ** 2 - 1) / a])
def Cil(s):
    return np.array([math.cos(2 * math.pi * s.real), math.sin(2 * math.pi * s.real), s.imag])
def K(delta, theta):
    return np.array([abs(delta) * math.cos(theta), abs(delta) * math.sin(theta), delta])
def G(l, g, s):
    return ((s - 0.5) ** 2 - l ** 2 + g ** 2) ** 2 + 4 * g ** 2 * l ** 2
def fa(a, s):
    return (s - 0.5) ** 2 - a ** 2


def constantes():
    gE = 0.57721566490153286060651209
    c = {
        "pi": math.pi, "gamma_E": gE, "log_2pi": math.log(2 * math.pi),
        "C0 = 2 + gamma_E - log 4pi": 2 + gE - math.log(4 * math.pi),
        "zeta(2) = pi^2/6": math.pi ** 2 / 6,
        "2 - pi^2/6 (cota |zeta(2+iy)|)": 2 - math.pi ** 2 / 6,
        "L0 = -log(2 - pi^2/6)": -math.log(2 - math.pi ** 2 / 6),
        "lambda Bohr-Landau (delta=1/4) = log(1.375/1.3125)": math.log(1.375 / 1.3125),
        "D_1 = 1 - (1-gamma)^2/(log 2pi - gamma)": 1 - (1 - gE) ** 2 / (math.log(2 * math.pi) - gE),
        "D_256 (rodada 2)": 0.0082337162772610214, "D_256 <= (certificado intervalar)": 0.00823372,
        "D_8000 (rodada 3)": 0.005069120200107221,
        "altura verificada (Platt-Trudgian 2021)": 3e12,
        "pi < 3.14159265358979323847 (Mathlib)": 3.14159265358979323847,
    }
    return c


def zeros_reais():
    d = json.load(open(os.path.join(R4, "ate300", "zero_incognito.json")))
    b = np.array(d["newton"]["beta"]); g = np.array(d["newton"]["gamma"])
    o = np.argsort(g)
    return b[o] + 1j * g[o]


def confere(zs):
    rng = random.Random(1)
    pts = [complex(rng.uniform(-3, 3), rng.uniform(-40, 40)) for _ in range(2000)]
    err = {}
    err["T(T(s)) = s"] = max(abs(T(T(s)) - s) for s in pts)
    err["R(R(s)) = s"] = max(abs(R(R(s)) - s) for s in pts)
    err["|T s1 - T s2| = |s1 - s2|"] = max(abs(abs(T(a) - T(b)) - abs(a - b)) for a, b in zip(pts, pts[1:]))
    err["D(R s) = -D(s)"] = max(abs(D(R(s)) + D(s)) for s in pts)
    err["T(R(T(w))) = conj(w) + i"] = max(abs(T(R(T(w))) - (np.conj(w) + 1j)) for w in pts)
    err["|P(s)| = 1"] = max(abs(np.linalg.norm(P(s)) - 1) for s in pts)
    err["Cil(R s) = (X, -Y, Z)"] = max(np.max(np.abs(Cil(R(s)) - Cil(s) * np.array([1, -1, 1]))) for s in pts)
    err["K: X^2 + Y^2 = Z^2"] = max(abs(K(d, th)[0] ** 2 + K(d, th)[1] ** 2 - d ** 2)
                                     for d, th in [(rng.uniform(-1, 1), rng.uniform(0, 7)) for _ in range(500)])
    l, g = 0.13, 20.0
    raizes = [0.5 + l + 1j * g, 0.5 + l - 1j * g, 0.5 - l + 1j * g, 0.5 - l - 1j * g]
    err["G_lambda(1/2 ± l ± ig) = 0 (relativo)"] = max(abs(G(l, g, r)) for r in raizes) / g ** 4
    err["G(1-s) = G(s)"] = max(abs(G(l, g, 1 - s) - G(l, g, s)) / (1 + abs(G(l, g, s))) for s in pts)
    err["f_a(1-s) = f_a(s)"] = max(abs(fa(0.2, 1 - s) - fa(0.2, s)) for s in pts)
    # zeros reais de ζ
    zz = zeta(np.array(zs))
    err["|zeta(rho)| nos 138 zeros"] = float(np.max(np.abs(zz)))
    err["|zeta(R rho)| (reflexo)"] = float(np.max(np.abs(zeta(np.array([R(z) for z in zs])))))
    err["max |D(rho)| (deslocamento)"] = float(np.max(np.abs(np.real(zs) - 0.5)))
    err["max |Im T(rho) - 1/2| (linha trocada)"] = float(np.max(np.abs(np.imag([T(z) for z in zs]) - 0.5)))
    return {k: float(v) for k, v in err.items()}


def estados(zs):
    """Estado de cada ponto testado: C, E, NC, NE (para ζ e para G_λ)."""
    cont = {"zeta": {"C": 0, "E": 0}, "G_0.13": {"C": 0, "E": 0}}
    for z in zs:
        cont["zeta"]["C" if abs(z.real - 0.5) < 1e-9 else "E"] += 1
    for r in [0.5 + 0.13 + 20j, 0.5 - 0.13 + 20j, 0.5 + 0.13 - 20j, 0.5 - 0.13 - 20j]:
        cont["G_0.13"]["C" if abs(r.real - 0.5) < 1e-12 else "E"] += 1
    # pontos que não são zeros: certificação |F(s)| > raio
    s_nc = 0.5 + 10j
    s_ne = 0.8 + 10j
    cont["zeta(1/2+10i)"] = {"valor": abs(complex(zeta(np.array([s_nc]))[0])), "estado": "NC"}
    cont["zeta(0.8+10i)"] = {"valor": abs(complex(zeta(np.array([s_ne]))[0])), "estado": "NE"}
    return cont


def figuras(zs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    zs = zs[zs.imag <= 60]
    hip = np.array([0.5 + 0.13 + 22.5j, 0.5 - 0.13 + 22.5j, 0.5 + 0.3 + 47j, 0.5 - 0.3 + 47j])
    triv = np.array([-2, -4, -6, -8], dtype=complex)
    fig = plt.figure(figsize=(16, 9))
    # plano
    ax = fig.add_subplot(2, 3, 1)
    ax.axvline(0.5, color="#9ca3af", lw=0.8, ls=":")
    ax.plot(zs.real, zs.imag, "o", ms=4, color="#2563eb", label="zeros de ζ (C)")
    ax.plot(hip.real, hip.imag, "x", ms=7, color="#dc2626", label="externos construídos (G_λ)")
    ax.plot(triv.real, triv.imag, "s", ms=4, color="#059669", label="triviais")
    ax.set_xlim(-9, 2); ax.set_title("Plano s = σ + it"); ax.legend(fontsize=7, frameon=False)
    # plano trocado
    ax = fig.add_subplot(2, 3, 2)
    w = np.array([T(z) for z in zs]); wh = np.array([T(z) for z in hip])
    ax.axhline(0.5, color="#9ca3af", lw=0.8, ls=":")
    ax.plot(w.real, w.imag, "o", ms=4, color="#2563eb")
    ax.plot(wh.real, wh.imag, "x", ms=7, color="#dc2626")
    ax.set_ylim(-0.2, 1.2); ax.set_title("Plano trocado w = T(s) = i s̄: a linha vira Im w = 1/2")
    # esfera
    ax = fig.add_subplot(2, 3, 3, projection="3d")
    u, v = np.mgrid[0:2 * np.pi:40j, 0:np.pi:20j]
    ax.plot_wireframe(np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v), color="#e5e7eb", lw=0.4)
    tt = np.linspace(-60, 60, 400); lin = np.array([P(0.5 + 1j * t) for t in tt])
    ax.plot(lin[:, 0], lin[:, 1], lin[:, 2], color="#9ca3af", lw=1)
    pz = np.array([P(z) for z in zs]); ph = np.array([P(z) for z in hip])
    ax.scatter(pz[:, 0], pz[:, 1], pz[:, 2], s=8, color="#2563eb")
    ax.scatter(ph[:, 0], ph[:, 1], ph[:, 2], s=20, color="#dc2626", marker="x")
    ax.set_title("Esfera de Riemann (P injetiva)")
    # cilindro
    ax = fig.add_subplot(2, 3, 4, projection="3d")
    th = np.linspace(0, 2 * np.pi, 60); hh = np.linspace(0, 60, 2)
    TH, HH = np.meshgrid(th, hh)
    ax.plot_surface(np.cos(TH), np.sin(TH), HH, color="#f3f4f6", alpha=0.3)
    cz = np.array([Cil(z) for z in zs]); ch = np.array([Cil(z) for z in hip])
    ax.scatter(cz[:, 0], cz[:, 1], cz[:, 2], s=8, color="#2563eb")
    ax.scatter(ch[:, 0], ch[:, 1], ch[:, 2], s=20, color="#dc2626", marker="x")
    ax.set_title("Cilindro: a linha é a geratriz (−1, 0, t)")
    # cone
    ax = fig.add_subplot(2, 3, 5, projection="3d")
    dd = np.linspace(-0.4, 0.4, 30); TH, DD = np.meshgrid(th, dd)
    ax.plot_surface(np.abs(DD) * np.cos(TH), np.abs(DD) * np.sin(TH), DD, color="#f3f4f6", alpha=0.3)
    kz = np.array([K(D(z), 2 * np.pi * z.imag / 60) for z in zs])
    kh = np.array([K(D(z), 2 * np.pi * z.imag / 60) for z in hip])
    ax.scatter(kz[:, 0], kz[:, 1], kz[:, 2], s=8, color="#2563eb")
    ax.scatter(kh[:, 0], kh[:, 1], kh[:, 2], s=20, color="#dc2626", marker="x")
    ax.set_title("Cone: zeros na linha no vértice")
    # família de cruzamento
    ax = fig.add_subplot(2, 3, 6)
    ls = np.linspace(-0.3, 0.3, 61)
    for sgn, cor in ((1, "#dc2626"), (-1, "#7c3aed")):
        ax.plot(0.5 + sgn * ls, ls, color=cor, lw=1.5, label=f"Re = 1/2 {'+' if sgn > 0 else '−'} λ")
    ax.axvline(0.5, color="#9ca3af", lw=0.8, ls=":")
    ax.plot([0.5], [0], "o", color="#111827")
    ax.set_xlabel("Re do zero de G_λ"); ax.set_ylabel("λ")
    ax.set_title("G_λ: encontro em λ = 0 (raiz dupla), separação para λ ≠ 0")
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "cez_geometrias.png"), dpi=140)


def main():
    zs = zeros_reais()
    rel = {"constantes": constantes(), "conferencias": confere(zs), "estados": estados(zs),
           "n_zeros": int(len(zs))}
    json.dump(rel, open(os.path.join(OUT, "cez.json"), "w"), indent=1, ensure_ascii=False)
    for k, v in rel["constantes"].items():
        print(f"  {k}: {v:.15g}")
    for k, v in rel["conferencias"].items():
        print(f"  erro {k}: {v:.2e}")
    print(json.dumps(rel["estados"], ensure_ascii=False))
    figuras(zs)


if __name__ == "__main__":
    main()
