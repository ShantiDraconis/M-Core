#!/usr/bin/env python3
"""ATK–Closed Math completo: espelho numérico e exato dos teoremas do kernel.

Módulos Lean correspondentes: ATK/ClosedMathCompleto.lean, ATK/ClosedMathToro.lean,
ATK/RHTerminal.lean. Aqui:

* aritmética **exata** (racionais gaussianos e polinômios com coeficientes em Q[i]) para as
  identidades algébricas: fatorações, expansão quártica, raízes, multiplicidades, simetrias;
* conferência **numérica** (ponto flutuante) de geometria (esfera, cilindro, cone, toro),
  curvatura, área, Gauss–Bonnet, integrais de contorno (contagens 3 e 6), limites e do critério
  terminal de somas finitas de Euler–Maclaurin em K_n (instâncias com n fixo, tempo "presente":
  observação numérica, não prova).

Uso: python3 closed_math.py <dir_saida>   (gera closed_math.json e figuras)
"""
from fractions import Fraction as Fr
import json, math, os, sys, cmath
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

# ---------------------------------------------------------------- racionais gaussianos
class Q:
    """a + b i com a, b racionais exatos."""
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o): o = _q(o); return Q(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = _q(o); return Q(s.a - o.a, s.b - o.b)
    def __rsub__(s, o): return _q(o) - s
    def __neg__(s): return Q(-s.a, -s.b)
    def __mul__(s, o): o = _q(o); return Q(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = _q(o); d = o.a * o.a + o.b * o.b
        return Q((s.a * o.a + s.b * o.b) / d, (s.b * o.a - s.a * o.b) / d)
    def __pow__(s, n):
        r = Q(1)
        for _ in range(n): r = r * s
        return r
    def __eq__(s, o): o = _q(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def conj(s): return Q(s.a, -s.b)
    def re(s): return s.a
    def im(s): return s.b
    def normSq(s): return s.a * s.a + s.b * s.b
    def __repr__(s): return f"({s.a}+{s.b}i)"
    def c(s): return complex(float(s.a), float(s.b))

def _q(x): return x if isinstance(x, Q) else Q(x)
I = Q(0, 1)
HALF = Q(Fr(1, 2))

# ---------------------------------------------------------------- polinômios em Q[i][X]
class Poly:
    def __init__(self, cs): self.cs = [_q(c) for c in cs]; self._trim()
    def _trim(self):
        while len(self.cs) > 1 and self.cs[-1] == 0: self.cs.pop()
    @staticmethod
    def X(): return Poly([0, 1])
    def deg(self): return 0 if self.cs == [Q(0)] else len(self.cs) - 1
    def __add__(s, o):
        o = o if isinstance(o, Poly) else Poly([o]); n = max(len(s.cs), len(o.cs))
        return Poly([(s.cs[i] if i < len(s.cs) else Q(0)) + (o.cs[i] if i < len(o.cs) else Q(0)) for i in range(n)])
    def __sub__(s, o):
        o = o if isinstance(o, Poly) else Poly([o]); return s + o * Poly([-1])
    def __mul__(s, o):
        o = o if isinstance(o, Poly) else Poly([o]); r = [Q(0)] * (len(s.cs) + len(o.cs) - 1)
        for i, a in enumerate(s.cs):
            for j, b in enumerate(o.cs): r[i + j] = r[i + j] + a * b
        return Poly(r)
    def __pow__(s, n):
        r = Poly([1])
        for _ in range(n): r = r * s
        return r
    def __eq__(s, o): return s.cs == o.cs
    def ev(s, z):
        r = Q(0)
        for c in reversed(s.cs): r = r * z + c
        return r
    def deriv(s): return Poly([s.cs[i] * i for i in range(1, len(s.cs))] or [0])

def lin(a): return Poly([-_q(a), 1])           # X − a
def prod_lin(roots):
    p = Poly([1])
    for a in roots: p = p * lin(a)
    return p
def mult(p, a):
    """Multiplicidade de a: primeira derivada que não se anula (ordem_por_derivadas)."""
    k, q = 0, p
    while q.ev(a) == 0: q, k = q.deriv(), k + 1
    return k

# ---------------------------------------------------------------- modelo e operadores
def G(d, g, s):           # forma do kernel: ((s−½)² − λ² + γ²)² + 4γ²λ²
    x = s - HALF; return (x ** 2 - Q(d) ** 2 + Q(g) ** 2) ** 2 + 4 * Q(g) ** 2 * Q(d) ** 2
def G_fat(d, g, s):
    return ((s - HALF - d) ** 2 + Q(g) ** 2) * ((s - HALF + d) ** 2 + Q(g) ** 2)
def raizes(d, g):
    d, g = Q(d), Q(g)
    return [HALF + d + g * I, HALF + d - g * I, HALF - d + g * I, HALF - d - g * I]
opJ = lambda s: s.conj()
opR = lambda s: 1 - s.conj()          # torção
opS = lambda s: 1 - s
opT = lambda s: I * s.conj()          # troca

# ---------------------------------------------------------------- verificador (P6)
def checar(m, r):
    return "naoZero" if r < abs(m) else "indeterminado"
def checarIC(lo_re, hi_re, lo_im, hi_im):
    exclui = lo_re > 0 or hi_re < 0 or lo_im > 0 or hi_im < 0
    return "naoZero" if exclui else "indeterminado"

# ---------------------------------------------------------------- geometrias
def P(s):
    a = 1 + abs(s) ** 2
    return np.array([2 * s.real / a, 2 * s.imag / a, (abs(s) ** 2 - 1) / a])
def Cil(s): return np.array([math.cos(2 * math.pi * s.real), math.sin(2 * math.pi * s.real), s.imag])
def Kc(delta, theta): return np.array([abs(delta) * math.cos(theta), abs(delta) * math.sin(theta), delta])
def Kt(T, delta, t):
    th = 2 * math.pi * t / T
    return np.array([abs(delta) * math.cos(th), abs(delta) * math.sin(th), delta, t])
def tor(R, r, T, s):
    th, ph = 2 * math.pi * s.real, 2 * math.pi * s.imag / T
    return np.array([(R + r * math.cos(th)) * math.cos(ph), (R + r * math.cos(th)) * math.sin(ph), r * math.sin(th)])
def Kg(R, r, th): return math.cos(th) / (r * (R + r * math.cos(th)))

# ---------------------------------------------------------------- contorno
def contorno(logderiv, c, R, n=20000):
    """(1/2πi)∮ f'/f por trapézio no círculo |z−c| = R."""
    th = np.linspace(0, 2 * np.pi, n, endpoint=False)
    z = c + R * np.exp(1j * th); dz = 1j * R * np.exp(1j * th) * (2 * np.pi / n)
    return complex(np.sum(logderiv(z) * dz) / (2j * np.pi))

# ---------------------------------------------------------------- Euler–Maclaurin (como no kernel)
def bernoulli(m):
    B = [Fr(1)]
    for k in range(1, m + 1):
        B.append(-sum(math.comb(k + 1, j) * B[j] for j in range(k)) / (k + 1))
    return B              # B_1 = −1/2 (convenção do Mathlib)
BN = bernoulli(30)
def Cb(k): return float(sum(abs(BN[i]) * math.comb(k, i) for i in range(k + 1)))
def poch(s, m):
    r = 1
    for j in range(m): r *= (s + j)
    return r
def EM(N, M, s):
    s = complex(s); tot = sum((n + 1) ** (-s) for n in range(N))
    tot += N ** (1 - s) / (s - 1) - N ** (-s) / 2
    for j in range(2, M + 1):
        tot += float(BN[j]) / math.factorial(j) * poch(s, j - 1) * N ** (-s - (j - 1))
    return tot
def Eb(n, N, M):
    return (math.sqrt(1 + n * n) + M) ** M / math.factorial(M) * (Cb(M) * N ** (0.5 - M) / (M - 0.5))
def Kn_grade(n, ns=60, nt=None):
    nt = nt or max(200, 40 * n)
    sig = np.linspace(0.5 + 1 / n, 1 - 1 / n, ns); t = np.linspace(-n, n, nt)
    S, Tt = np.meshgrid(sig, t); return (S + 1j * Tt).ravel()

# ---------------------------------------------------------------- tempos verbais
TEMPOS = [
    ("classificação exaustiva C/E/N_C/N_E", "perfeito", "ATK.ClosedMath.classificacao"),
    ("simetria força a linha crítica", "negado", "ATK.ClosedMath.a_simetria"),
    ("HR ⟺ ZE = ∅", "perfeito", "ATK.CEZ.rh_iff_externa_vazia"),
    ("zeros no equador interno do toro, se HR", "condicional", "ATK.ClosedMath.a_toro_condicional"),
    ("HR", "futuro", "ATK.ClosedMath.a_rh"),
    ("HR ⟺ critério de somas finitas em todo K_n", "perfeito", "ATK.ClosedMath.Terminal.rh_iff_criterioEM"),
    ("critério verificado para n = 5..N (grade)", "presente", "(numérico, este script)"),
    ("primeiros zeros na linha (Platt–Trudgian até 3·10¹²)", "presente", "(literatura; não no kernel)"),
]


def calcula():
    out = {}
    # identidades exatas do modelo
    d, g = Fr(1, 4), Fr(1)
    pts = [Q(Fr(a, 7), Fr(b, 5)) for a in range(-3, 4) for b in range(-3, 4)]
    out["G_fatora"] = all(G(d, g, s) == G_fat(d, g, s) for s in pts)
    out["G_R"] = all(G(d, g, opS(s)) == G(d, g, s) for s in pts)
    out["G_conj"] = all(G(d, g, opJ(s)) == G(d, g, s).conj() for s in pts)
    out["P1_zeros"] = [str(z) for z in raizes(d, g)]
    out["P1_ok"] = all(G(d, g, z) == 0 for z in raizes(d, g))
    out["G_meio"] = str(G(d, g, HALF))
    out["G_meio_eq"] = G(d, g, HALF) == Q((d * d + g * g) ** 2)
    out["G_2"] = str(G(d, g, Q(2)))
    # polinômio, conservação, multiplicidades
    for (dd, nome) in [(Fr(1, 4), "d=1/4"), (Fr(0), "d=0")]:
        p = prod_lin(raizes(dd, g))
        out[f"grau_{nome}"] = p.deg()
        out[f"mult_{nome}"] = mult(p, raizes(dd, g)[0])
        hn = prod_lin([HALF + g * I, HALF - g * I] + raizes(dd, g))   # numerador de H
        out[f"H_mult_meio+i_{nome}"] = mult(hn, HALF + g * I)
        out[f"eval_{nome}"] = all(p.ev(s) == G(dd, g, s) for s in pts)
    x = Poly([-HALF, 1])
    out["quartica"] = prod_lin(raizes(d, g)) == x ** 4 + x ** 2 * (2 * (g * g - d * d)) + Poly([(g * g + d * d) ** 2])
    out["mult_(z-2)^m"] = {m: mult(lin(2) ** m, Q(2)) for m in range(1, 7)}
    # operadores: grupo de Klein, troca
    s = Q(Fr(3, 10), Fr(14))
    out["klein"] = (opJ(opJ(s)) == s and opR(opR(s)) == s and opS(opS(s)) == s and
                    opR(opJ(s)) == opS(s) and opR(opS(s)) == opJ(s) and opJ(opS(s)) == opR(s))
    out["TRT"] = opT(opR(opT(s))) == s.conj() + I
    out["troca_fluxo"] = opT(opT(s) + Fr(1, 3)) == s + Q(0, Fr(1, 3))
    dd, t = Fr(1, 10), Fr(14)
    sp, sm = HALF + dd + t * I, HALF - dd + t * I
    out["centro"] = str((sp + sm) / 2); out["separacao"] = float(math.sqrt((sp - sm).normSq()))
    out["centro_troca"] = str((opT(sp) + opT(sm)) / 2)
    # verificador
    out["checar"] = {"G(0.6+13.99i)": checar(complex(G(Fr(1, 10), 14, Q(Fr(3, 5), Fr(1399, 100))).c()), 0),
                     "zero exato": checar(0, 0)}
    # P-POSNEG, sin πz, 1/z², limite, truncamento
    out["posneg"] = all(abs((z * z - 4) * (z * z + 9)) < 1e-12 for z in [2, -2, 3j, -3j])
    out["sin_pi_inteiros"] = max(abs(cmath.sin(math.pi * k)) for k in range(-20, 21))
    out["sin_pi_nao_inteiro"] = abs(cmath.sin(math.pi * (0.5 + 0.1j)))
    out["zero_infinito"] = all(abs(1 / (1 / w) ** 2 - w ** 2) < 1e-12 for w in [0.3, 2 + 1j, -1j])
    out["limite"] = [(x, (x * x - 1) / (x - 1)) for x in [1.1, 1.01, 1.001, 0.999]]
    out["truncamentos"] = all(Fr((10 ** n) // 3, 10 ** n) != Fr(1, 3) for n in range(0, 60))
    out["f(0.33)"] = str(Fr(33, 100) - Fr(1, 3))
    # integrais de contorno
    L = lambda z: 3 / (z - 1) + 2 / (z + 2) - 2 / z - 1 / (z - 4)
    out["contorno_fArg"] = contorno(L, 0, 3).real
    for dd in (0.25, 0.0):
        A = [0.5 + 1j, 0.5 - 1j, 0.5 + dd + 1j, 0.5 + dd - 1j, 0.5 - dd + 1j, 0.5 - dd - 1j]
        out[f"contorno_H_d={dd}"] = contorno(lambda z: sum(1 / (z - a) for a in A), 0.5, 2).real
    # H com Γ
    from scipy.special import gamma as Gm
    out["H_meio"] = 289 / 256 / Gm(1.25)
    out["Gamma(5/4)"] = Gm(1.25)
    # esfera, cilindro, cone (exemplos dos anexos)
    sp, sm = 0.6 + 14j, 0.4 + 14j
    corda = np.linalg.norm(P(sp) - P(sm))
    out["esfera_corda"] = corda
    out["esfera_corda_formula"] = 2 * abs(sp - sm) / math.sqrt((1 + abs(sp) ** 2) * (1 + abs(sm) ** 2))
    out["esfera_angulo"] = 2 * math.asin(corda / 2)
    out["cilindro_dist"] = float(np.linalg.norm(Cil(sp)[:2] - Cil(sm)[:2]))
    out["cilindro_formula"] = 2 * abs(math.sin(2 * math.pi * 0.1))
    out["cone_K(0.1,pi)"] = Kc(0.1, math.pi).tolist(); out["cone_K(-0.1,pi)"] = Kc(-0.1, math.pi).tolist()
    # toro
    R, r, T = 3.0, 1.0, 28.0
    out["toro"] = {
        "superficie": max(abs((math.hypot(*tor(R, r, T, z)[:2]) - R) ** 2 + tor(R, r, T, z)[2] ** 2 - r * r)
                          for z in [0.3 + 2j, 0.5 + 14j, 0.9 - 7j]),
        "linha_raio": math.hypot(*tor(R, r, T, 0.5 + 5j)[:2]), "R-r": R - r,
        "par_dist": float(np.linalg.norm(tor(R, r, T, 0.6 + 14j) - tor(R, r, T, 0.4 + 14j))),
        "par_formula": 2 * r * abs(math.sin(2 * math.pi * 0.1)),
        "reencontro": float(np.linalg.norm(tor(R, r, T, 1 + 1j) - tor(R, r, T, 0 + 1j))),
        "K_linha": Kg(R, r, math.pi), "K_linha_formula": -1 / (r * (R - r)),
        "K_externo": Kg(R, r, 0), "area_num": None, "area_formula": 4 * math.pi ** 2 * R * r,
        "gauss_bonnet_num": None,
        "S_fixos": [str(z) for z in (0, 0.5, 0 + 14j, 0.5 + 14j)],
    }
    th = np.linspace(0, 2 * np.pi, 4001)
    out["toro"]["area_num"] = float(2 * np.pi * np.trapezoid(r * (R + r * np.cos(th)), th))
    out["toro"]["gauss_bonnet_num"] = float(2 * np.pi * np.trapezoid(
        np.array([Kg(R, r, x) for x in th]) * r * (R + r * np.cos(th)), th))
    # terminal: E(n,N,M) e min |EM| em K_n (numérico)
    term = []
    for n in [5, 8, 10, 13, 15, 20, 25, 30]:
        N, M = 40, 10
        zs = Kn_grade(n)
        mins = float(np.min(np.abs([EM(N, M, z) for z in zs])))
        term.append({"n": n, "N": N, "M": M, "E": Eb(n, N, M), "min|EM| (grade)": mins,
                     "E<min": Eb(n, N, M) < mins})
    out["terminal"] = term
    out["tempos"] = TEMPOS
    return out


def figuras(dirout, out):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    R, r, T = 3.0, 1.0, 28.0
    fig = plt.figure(figsize=(13, 5.2))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    th, ph = np.meshgrid(np.linspace(0, 2 * np.pi, 80), np.linspace(0, 2 * np.pi, 120))
    Xs = (R + r * np.cos(th)) * np.cos(ph); Ys = (R + r * np.cos(th)) * np.sin(ph); Zs = r * np.sin(th)
    Kv = np.cos(th) / (r * (R + r * np.cos(th)))
    ax.plot_surface(Xs, Ys, Zs, facecolors=plt.cm.coolwarm((Kv - Kv.min()) / (Kv.max() - Kv.min())),
                    alpha=0.35, linewidth=0, shade=False)
    t = np.linspace(0, T, 400)
    lin = np.array([tor(R, r, T, 0.5 + 1j * x) for x in t])
    ax.plot(*lin.T, color="k", lw=2, label="linha crítica → equador interno")
    try:
        sys.path.insert(0, AQUI)
        d = json.load(open(os.path.join(AQUI, "..", "..", "rodada4", "dados", "ate300", "zero_incognito.json")))
        gam = np.sort(np.array(d["newton"]["gamma"]))
    except Exception:
        gam = np.array([14.134725, 21.02204, 25.010858])
    zp = np.array([tor(R, r, T, 0.5 + 1j * g) for g in gam])
    ax.scatter(*zp.T, s=8, color="crimson", label=f"{len(gam)} zeros de ζ (t mod {T:g})")
    par = np.array([tor(R, r, T, s) for s in (0.6 + 14j, 0.4 + 14j)])
    ax.scatter(*par.T, s=40, color="orange", marker="^", label="par hipotético ½±0,1+14i")
    ax.set_title("Toro: curvatura (azul<0, vermelho>0), linha crítica e zeros")
    ax.legend(fontsize=7, loc="upper left"); ax.set_box_aspect((1, 1, 0.35))
    ax2 = fig.add_subplot(1, 2, 2)
    ns = [x["n"] for x in out["terminal"]]
    ax2.semilogy(ns, [x["E"] for x in out["terminal"]], "o-", label="E(n,N=40,M=10) (cota provada)")
    ax2.semilogy(ns, [x["min|EM| (grade)"] for x in out["terminal"]], "s-", label="min |EM| em K_n (grade)")
    ax2.set_xlabel("n"); ax2.set_title("Critério terminal: instâncias com n fixo (numérico)")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(dirout, "closed_math_toro.png"), dpi=130)


def main():
    dirout = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(dirout, exist_ok=True)
    out = calcula()
    json.dump(out, open(os.path.join(dirout, "closed_math.json"), "w"), indent=1, ensure_ascii=False,
              default=lambda o: o if not isinstance(o, (np.floating, np.bool_)) else o.item())
    figuras(dirout, out)
    for k, v in out.items():
        if k not in ("terminal", "tempos", "toro", "limite"):
            print(f"{k}: {v}")
    print("toro:", json.dumps(out["toro"], ensure_ascii=False))
    for x in out["terminal"]: print(x)


if __name__ == "__main__":
    main()
