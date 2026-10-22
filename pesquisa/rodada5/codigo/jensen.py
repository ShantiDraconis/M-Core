#!/usr/bin/env python3
"""Rota de Jensen–Pólya para ξ: coeficientes, Turán, Toeplitz, momentos (companheiro de
ATK/JensenTuran.lean).

Θ(x) = ξ(½ + √x) = Σ aₙ xⁿ,   aₙ = 8·4ⁿ·Mₙ/(2n)!,   Mₙ = ∫₀^∞ u^{2n} Φ(u) du,
Φ(u) = Σ_{m≥1} (2π²m⁴e^{9u} − 3πm²e^{5u}) exp(−πm²e^{4u})   (núcleo theta; Φ par).

Só biblioteca padrão (Decimal/Fraction): a "função indisponível" da tentativa anterior não é
necessária. Mₙ pela regra do trapézio na reta (Φ par e analítica na faixa |Im u| < π/8: erro
≈ exp(−π²/(4h))), conferida com h e h/2.

Controles: a₀ = ξ(½) = 0,49712077818831410…; troca de sinal de Θ(−t²) = Ξ(t) em torno de
t₁ = 14,134725… (primeiro zero).

Verificações numéricas (NÃO certificadas):
  * Turán normalizado γ_{k+1}² ≥ γ_kγ_{k+2}, γₙ = n!aₙ;
  * Turán de ordem 3: 4(γ₁²−γ₀γ₂)(γ₂²−γ₁γ₃) ≥ (γ₁γ₂−γ₀γ₃)² (deslocado);
  * sanduíche dos momentos M_{n+1}² ≤ MₙM_{n+2} ≤ (2n+3)/(2n+1)·M_{n+1}²;
  * menores de Toeplitz D_{r,k} = det[γ_{k+i−j}] (e o mesmo para aₙ), exatos em Fraction;
  * hiperbolicidade de J^{d,n}(X) = Σ C(d,j) γ_{n+j} X^j por Sturm exato (d ≤ 8).
"""
import json, math, sys, time
from decimal import Decimal as D, getcontext
from fractions import Fraction

PREC = 130
getcontext().prec = PREC


def pi_dec():
    getcontext().prec += 5
    three = D(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 5
    return +s


PI = pi_dec()
LIM = D(PREC) * D(10).ln() + 60


def Phi(u):
    e4, e5, e9 = (4 * u).exp(), (5 * u).exp(), (9 * u).exp()
    s, m = D(0), 1
    while True:
        arg = PI * m * m * e4
        if arg > LIM:
            break
        s += (2 * PI * PI * m ** 4 * e9 - 3 * PI * m * m * e5) * (-arg).exp()
        m += 1
    return s


def momentos(N, h, U=D("2.4")):
    """Mₙ, n = 0..N, por trapézio: ∫₀^∞ f = h(f(0)/2 + Σ_{j≥1} f(jh)) (f par)."""
    J = int(U / h) + 1
    us = [h * j for j in range(J + 1)]
    ph = [Phi(u) for u in us]
    M = []
    for n in range(N + 1):
        s = ph[0] / 2 if n == 0 else D(0)
        for u, p in zip(us[1:], ph[1:]):
            s += u ** (2 * n) * p
        M.append(h * s)
    return M


def coeficientes(N, h):
    M = momentos(N, h)
    a = [D(8) * D(4) ** n * M[n] / D(math.factorial(2 * n)) for n in range(N + 1)]
    g = [D(math.factorial(n)) * a[n] for n in range(N + 1)]
    return M, a, g


def Theta(a, x):
    s, p = D(0), D(1)
    for c in a:
        s += c * p
        p *= x
    return s


def primeiro_zero(a, lo=D("14.13"), hi=D("14.14"), tol=D("1e-28")):
    """Bisseção de Ξ(t) = Θ(−t²) (real em t real) no primeiro zero."""
    flo = Theta(a, -(lo * lo))
    while hi - lo > tol:
        mid = (lo + hi) / 2
        fm = Theta(a, -(mid * mid))
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


# Números do certificado do kernel (ATK/ZeroCritico.lean, `cert_ok` por decide +kernel):
CERT_KERNEL = {
    "t0": "14.1347251417", "delta": "1e-5", "r": "1e-6",
    "zeta(z0) re": ["-5.520245e-9", "5.528543e-9"], "zeta(z0) im": ["-5.551111e-9", "5.497564e-9"],
    "zeta(z0+i*delta) re": ["-1.252487870e-6", "-1.241439031e-6"],
    "zeta(z0+i*delta) im": ["7.827425428e-6", "7.838474040e-6"],
    "c": ["0.783297650741587", "0.124696759939979"], "resto_EM": "5.476247e-9", "F2": "6648.199",
    "contracao: (r0+r1)/delta + F2(delta+r) <= c/2": ["0.0753399", "0.3916488"],
    "mapeamento: |A0|+r0 <= r*c/2": ["1.1079654e-8", "3.91648825e-7"],
}


def det_frac(Mx):
    """Determinante exato (Bareiss) de uma matriz de Fractions."""
    A = [row[:] for row in Mx]
    n = len(A)
    sign, prev = 1, Fraction(1)
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if sw is None:
                return Fraction(0)
            A[k], A[sw] = A[sw], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) / prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def toeplitz(seq, r, k):
    def e(m):
        return seq[m] if 0 <= m < len(seq) else Fraction(0)
    return det_frac([[e(k + i - j) for j in range(r)] for i in range(r)])


def sturm_reais(coef):
    """Número de raízes reais distintas de Σ coef[j] X^j (Fractions), por Sturm."""
    def trim(p):
        while p and p[-1] == 0:
            p = p[:-1]
        return p

    def deriv(p):
        return [j * p[j] for j in range(1, len(p))]

    def rem(p, q):
        p = p[:]
        while len(p) >= len(q) and p:
            c = p[-1] / q[-1]
            sh = len(p) - len(q)
            for j in range(len(q)):
                p[sh + j] -= c * q[j]
            p = trim(p[:-1]) if p[-1] == 0 else trim(p)
        return p

    p0 = trim(coef)
    seq = [p0, trim(deriv(p0))]
    while seq[-1] and len(seq[-1]) > 1:
        r = rem(seq[-2], seq[-1])
        if not r:
            break
        seq.append([-c for c in r])

    def var(sgns):
        s = [x for x in sgns if x != 0]
        return sum(1 for i in range(len(s) - 1) if s[i] * s[i + 1] < 0)

    def sgn_inf(p, pos):
        lead = p[-1]
        deg = len(p) - 1
        s = 1 if lead > 0 else -1
        return s if pos or deg % 2 == 0 else -s

    return var([sgn_inf(p, False) for p in seq if p]) - var([sgn_inf(p, True) for p in seq if p])


def main(N=60, dmax=8, nmax=30, rmax=8, kmax=24, saida=None):
    t0 = time.time()
    h1, h2 = D(1) / 64, D(1) / 128
    M1, a1, g1 = coeficientes(N, h1)
    M, a, g = coeficientes(N, h2)
    conc = min(int(-((a[n] - a1[n]) / a[n]).copy_abs().log10()) if a[n] != a1[n] else PREC
               for n in range(N + 1))
    xi_meio = D("0.49712077818831410991")
    ctrl_a0 = float(abs(a[0] - xi_meio))
    t1 = D("14.134725141734693790457251983562")
    th = {str(t): float(Theta(a, -(t * t))) for t in (D("14.13"), t1, D("14.14"))}
    troca = th["14.13"] * th["14.14"] < 0
    t1 = primeiro_zero(a)

    tur = [g[k + 1] ** 2 - g[k] * g[k + 2] for k in range(N - 1)]
    tur_rel = [float(tur[k] / g[k + 1] ** 2) for k in range(N - 1)]
    tur3 = []
    for k in range(N - 2):
        x0, x1, x2, x3 = g[k:k + 4]
        tur3.append(float((4 * (x1 ** 2 - x0 * x2) * (x2 ** 2 - x1 * x3) - (x1 * x2 - x0 * x3) ** 2)
                          / (x1 * x2) ** 2))
    sand = []
    for n in range(N - 1):
        lo = M[n + 1] ** 2 / (M[n] * M[n + 2])
        hi = (D(2 * n + 3) / D(2 * n + 1)) * M[n + 1] ** 2 / (M[n] * M[n + 2])
        sand.append({"n": n, "M1^2/(M0M2)": float(lo), "(2n+3)/(2n+1)*M1^2/(M0M2)": float(hi),
                     "logconvexo": lo <= 1, "turan": hi >= 1})

    gF = [Fraction(x) for x in g]
    aF = [Fraction(x) for x in a]
    tpl = {"gamma": {}, "a": {}}
    neg = {"gamma": [], "a": []}
    for nome, seq in (("gamma", gF), ("a", aF)):
        for r in range(1, rmax + 1):
            linha = []
            for k in range(0, kmax + 1):
                d = toeplitz(seq, r, k)
                ref = seq[k] ** r if seq[k] != 0 else Fraction(1)
                linha.append(float(d / ref))
                if d < 0:
                    neg[nome].append((r, k))
            tpl[nome][r] = linha
    hip = {}
    for d in range(1, dmax + 1):
        falhas = []
        for n in range(0, nmax + 1):
            coef = [Fraction(math.comb(d, j)) * gF[n + j] for j in range(d + 1)]
            if sturm_reais(coef) != d:
                falhas.append(n)
        hip[d] = {"testados": nmax + 1, "falhas": falhas}

    res = {
        "parametros": {"N": N, "prec": PREC, "h": [str(h1), str(h2)], "dmax": dmax, "nmax": nmax,
                       "rmax": rmax, "kmax": kmax},
        "concordancia_digitos_h_vs_h2": conc,
        "controle_a0_menos_xi_meio": ctrl_a0,
        "Theta(-t^2)": th,
        "troca_de_sinal_no_primeiro_zero": troca,
        "primeiro_zero_t1": str(t1)[:32],
        "t1_menos_t0_certificado": float(t1 - D("14.1347251417")),
        "certificado_kernel": CERT_KERNEL,
        "a": [float(x) for x in a[:16]],
        "gamma": [float(x) for x in g[:16]],
        "turan_todos_positivos": all(x > 0 for x in tur),
        "turan_relativo_min": min(tur_rel),
        "turan_relativo": tur_rel[:20],
        "turan3_todos_nao_negativos": all(x >= 0 for x in tur3),
        "turan3_relativo_min": min(tur3),
        "sanduiche": sand[:20],
        "sanduiche_todos": all(s["logconvexo"] and s["turan"] for s in sand),
        "toeplitz_menores_negativos": {k: v for k, v in neg.items()},
        "toeplitz_rel": {nome: {r: v[:12] for r, v in t.items()} for nome, t in tpl.items()},
        "jensen_hiperbolico": hip,
        "tempo_s": round(time.time() - t0, 1),
    }
    if saida:
        with open(saida, "w") as f:
            json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else None
    r = main(saida=out)
    for k in ("concordancia_digitos_h_vs_h2", "controle_a0_menos_xi_meio", "Theta(-t^2)",
              "troca_de_sinal_no_primeiro_zero", "primeiro_zero_t1", "t1_menos_t0_certificado",
              "turan_todos_positivos", "turan_relativo_min",
              "turan3_todos_nao_negativos", "turan3_relativo_min", "sanduiche_todos",
              "toeplitz_menores_negativos", "jensen_hiperbolico", "tempo_s"):
        print(k, "=", r[k])
    print("a[0..5] =", r["a"][:6])
    print("gamma[0..5] =", r["gamma"][:6])
