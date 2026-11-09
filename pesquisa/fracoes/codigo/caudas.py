#!/usr/bin/env python3
"""Companheiro numérico da rodada 103: caudas em fração (atk-kernel/ATK/Fracoes*.lean).

Só biblioteca padrão. **Nada aqui é certificado**; os teoremas estão em `atk-kernel/ATK/Fracoes*.lean`.
Cada problema é olhado como uma *cauda* com um expoente:

* RH — `zeros`: a parte imaginária de cada zero vira fração contínua; a cauda é o resto `x_k` num
  intervalo racional (o mesmo cálculo que `FracoesGama.lean` certifica).
* BSD — `bsd`: produtos parciais `∏_{p ≤ x} N_p/p` (frações exatas, gigantes) para 11a1, 37a1, 389a1
  (postos 0, 1, 2) — a forma original de Birch–Swinnerton-Dyer diz que crescem como `(log x)^r`; e
  `L(E,1)/Ω = 1/5` para 11a1 (o lado aritmético: `|Ш|·c₁₁/|T|² = 1·5/5²`).
* Beal — `beal`: contagem de soluções primitivas de `A^x + B^y = C^z` até `X`: cresce como `X^χ` no
  lado esférico, é finita no hiperbólico, vazia em `(3, 3, 3)`.
* NS — `burgers`: cauda de Fourier da solução exata (Cole–Hopf) de Burgers viscosa com `u₀ = sin x`:
  exponencial `e^{−δk}` para `ν > 0`. Em `t = 1` (o tempo de quebra) o limite invíscido é contínuo, com
  cúspide `|x − π|^{1/3}` e coeficientes exatos `2J_k(k)/k ~ 0,8946·k^{−4/3}`; ali `δ ∝ ν^{3/4}`. Só depois
  do choque (`t = 2`) a cauda invíscida é `1/k` e `δ ∝ ν`.
* YM — `z2_gauge`: teoria de calibre `Z₂` na rede 2D, enumerada exatamente: `⟨W⟩ = (1/2)^{área}` com
  `e^{2β} = 3` — cauda exponencial em fração (lei de área, tensão `log 2`).
* P vs NP — `sat`: média exata `7/8` das cláusulas satisfeitas; passeio de Schöning contra `(3/4)ⁿ`.
* Hodge — `euler`: `V − E + F = 2` e os defeitos angulares (Descartes) em frações de `π`.
* Rodada 106 — `linearizacao`: `|ζ(−2m−δ)| = 2 sin(πδ/2)·K_m(δ)` com `K_m = (2π)^{−(2m+1+δ)}Γ(2m+1+δ)ζ(2m+1+δ)`
  (`FracoesLinearizacao.lean`); `primons`: o gás de primos `Tr e^{−σH} = Σ (n+1)^{−σ} → ζ(σ)` e a lacuna
  `log 2` (`FracoesPrimons.lean`).
* Rodada 107 — `derivadas_triviais`: `|ζ′(−2m)| = (2m)!ζ(2m+1)/(2(2π)^{2m})` contra o quociente `|ζ(−2m−δ)|/δ`
  (`FracoesZerosTriviais.lean`); `fermions`: `Σ μ(n) n^{−σ} → 1/ζ(σ)` e o índice de Witten (`FracoesFermions.lean`).
"""
import json
import math
import os
import random
from fractions import Fraction as F
from itertools import product

AQUI = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------------------------------------------
# RH: frações contínuas com cauda
def fc_intervalo(lo, hi, maxk=80):
    passos = []
    while len(passos) < maxk:
        a, b = math.floor(lo), math.floor(hi)
        if a != b or lo == a:
            break
        passos.append(a)
        lo, hi = 1 / (hi - a), 1 / (lo - a)
    return passos, (lo, hi)


def convergentes(a):
    p0, q0, p1, q1 = 1, 0, a[0], 1
    out = [(p1, q1)]
    for x in a[1:]:
        p0, p1 = p1, x * p1 + p0
        q0, q1 = q1, x * q1 + q0
        out.append((p1, q1))
    return out


ZEROS = [
    ("gama1", F(141347251417, 10 ** 10), F(1, 10 ** 6), "certificado (ATK.ZeroCritico)"),
    ("gama2", F(210220396388, 10 ** 10), F(1, 10 ** 6), "certificado (ATK.ZeroSegundo)"),
    ("gama3", F(250108575801, 10 ** 10), F(1, 10 ** 6), "certificado (ATK.ZeroTerceiro)"),
    ("gigante1", F(300018051927946511944262498325, 10 ** 17), F(285, 10 ** 20), "bola da Arb (hipótese)"),
    ("gigante2", F(300018051927946678691400506282, 10 ** 17), F(449, 10 ** 20), "bola da Arb (hipótese)"),
]


def zeros():
    out = []
    for nome, c, r, fonte in ZEROS:
        a, (lo, hi) = fc_intervalo(c - r, c + r)
        p, q = convergentes(a)[-1]
        out.append({"nome": nome, "fonte": fonte, "quocientes": a, "n_certificados": len(a),
                    "cauda": [str(lo), str(hi)], "cauda_float": [float(lo), float(hi)],
                    "convergente": [p, q], "erro_convergente_vezes_q2": float(abs(c - F(p, q)) * q * q)})
    return out


# ----------------------------------------------------------------------------------------------
# BSD
CURVAS = {  # [a1, a2, a3, a4, a6], condutor, posto
    "11a1": ([0, -1, 1, -10, -20], 11, 0),
    "37a1": ([0, 0, 1, -1, 0], 37, 1),
    "389a1": ([0, 1, 1, -2, 0], 389, 2),
}


def crivo(n):
    c = bytearray([1]) * (n + 1)
    c[0] = c[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if c[p]:
            c[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    return [k for k in range(n + 1) if c[k]]


def n_pontos(ai, p):
    """`#E(𝔽_p)` (com o ponto no infinito) para a equação de Weierstrass geral."""
    a1, a2, a3, a4, a6 = ai
    if p == 2:
        return 1 + sum(1 for x in range(2) for y in range(2)
                       if (y * y + a1 * x * y + a3 * y - x ** 3 - a2 * x * x - a4 * x - a6) % 2 == 0)
    # (2y + a1 x + a3)² = 4x³ + b2 x² + 2 b4 x + b6
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    quad = [0] * p
    for y in range(p):
        quad[y * y % p] += 1
    tot = 0
    for x in range(p):
        tot += quad[(4 * x ** 3 + b2 * x * x + 2 * b4 * x + b6) % p]
    return tot + 1


def a_p(ai, p):
    return p + 1 - n_pontos(ai, p)


def bsd_produtos(P=10000, marcos=(100, 1000, 10000)):
    ps = crivo(P)
    out = {}
    for nome, (ai, N, r) in CURVAS.items():
        prod = F(1)
        vals = []
        k = 0
        for i, p in enumerate(ps):
            if N % p:
                prod *= F(n_pontos(ai, p), p)
            prox = ps[i + 1] if i + 1 < len(ps) else 10 ** 18
            while k < len(marcos) and p <= marcos[k] < prox:
                vals.append({"x": marcos[k], "log_produto": math.log(prod.numerator) - math.log(prod.denominator),
                             "digitos_numerador": len(str(prod.numerator))})
                k += 1
        # expoente estimado entre os dois últimos marcos: Δ log P / Δ log log x
        e = None
        if len(vals) >= 2:
            x1, x2 = vals[-2]["x"], vals[-1]["x"]
            e = (vals[-1]["log_produto"] - vals[-2]["log_produto"]) / (math.log(math.log(x2)) - math.log(math.log(x1)))
        out[nome] = {"posto": r, "condutor": N, "marcos": vals, "expoente_estimado": e,
                     "a_p_iniciais": {p: a_p(ai, p) for p in (2, 3, 5, 7, 11, 13)}}
    return out


def _a_n(ai, N, nmax):
    """Coeficientes `a_n` (multiplicativos; para `p | N` usa `a_{p^k} = a_p^k`)."""
    ps = crivo(nmax)
    ap = {p: (a_p(ai, p) if N % p else _ap_ruim(ai, p)) for p in ps}
    a = [0] * (nmax + 1)
    a[1] = 1
    # a_{p^k}
    pk = {}
    for p in ps:
        v = [1, ap[p]]
        while p ** len(v) <= nmax:
            v.append(ap[p] * v[-1] - (p * v[-2] if N % p else 0))
        pk[p] = v
    for n in range(2, nmax + 1):
        m, res = n, 1
        for p in ps:
            if p * p > m:
                break
            if m % p == 0:
                k = 0
                while m % p == 0:
                    m //= p
                    k += 1
                res *= pk[p][k]
        if m > 1:
            res *= pk[m][1]
        a[n] = res
    return a


def _ap_ruim(ai, p):
    # redução multiplicativa: a_p = p − #E_ns(𝔽_p) ... aqui via contagem: a_p = p + 1 − #E(𝔽_p) − 1 + 1
    # para redução multiplicativa, #E(𝔽_p) (com o nó) = p + 1 − a_p − ... usamos a_p = p − #E_ns + 1 − 1:
    # #E_ns(𝔽_p) = p − a_p, e #E(𝔽_p) = #E_ns + 1 (o ponto singular), logo a_p = p + 1 − #E(𝔽_p).
    return p + 1 - n_pontos(ai, p)


def periodo_real(ai):
    """`Ω = ∫_{E(ℝ)} |ω|` pela AGM (Cohen, Alg. 7.4.7)."""
    a1, a2, a3, a4, a6 = ai
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    # raízes de 4x³ + b2 x² + 2 b4 x + b6
    c = [4.0, float(b2), float(2 * b4), float(b6)]
    raizes = _raizes_cubica(c)
    reais = sorted([z.real for z in raizes if abs(z.imag) < 1e-12], reverse=True)

    def agm(x, y):
        for _ in range(100):
            x, y = (x + y) / 2, math.sqrt(x * y)
        return x

    if len(reais) == 3:
        e1, e2, e3 = reais
        w1 = math.pi / agm(math.sqrt(e1 - e3), math.sqrt(e1 - e2))
        return 2 * w1
    e1 = reais[0]
    beta = math.sqrt(3 * e1 * e1 + b2 * e1 / 2 + b4 / 2)
    alpha = 3 * e1 + b2 / 4
    return 2 * math.pi / agm(2 * math.sqrt(beta), math.sqrt(2 * beta + alpha))


def _raizes_cubica(c):
    a, b, cc, d = c
    import cmath
    b, cc, d = b / a, cc / a, d / a
    q = (3 * cc - b * b) / 9
    r = (9 * b * cc - 27 * d - 2 * b ** 3) / 54
    disc = q ** 3 + r * r
    s = cmath.sqrt(disc)
    S = complex(r + s) ** (1 / 3) if (r + s) != 0 else 0
    T = -q / S if S != 0 else complex(r - s) ** (1 / 3)
    w = complex(-0.5, math.sqrt(3) / 2)
    raizes = [S + T - b / 3, w * S + w.conjugate() * T - b / 3, w.conjugate() * S + w * T - b / 3]
    # polimento de Newton
    out = []
    for z in raizes:
        for _ in range(50):
            f = ((z + b) * z + cc) * z + d
            df = (3 * z + 2 * b) * z + cc
            if df == 0:
                break
            z -= f / df
        out.append(z)
    return out


def bsd_razao_11a1(nmax=80):
    ai, N, _ = CURVAS["11a1"]
    a = _a_n(ai, N, nmax)
    L = 2 * sum(a[n] / n * math.exp(-2 * math.pi * n / math.sqrt(N)) for n in range(1, nmax + 1))
    Om = periodo_real(ai)
    return {"L_E_1": L, "Omega": Om, "razao": L / Om, "previsto_BSD": "1/5 = |Sha|·c_11/|T|² = 1·5/25",
            "erro": abs(L / Om - 0.2)}


# ----------------------------------------------------------------------------------------------
# Beal
def raiz_inteira(n, k):
    if n < 0:
        return None
    x = int(round(n ** (1.0 / k)))
    for y in (x - 1, x, x + 1):
        if y >= 0 and y ** k == n:
            return y
    return None


def contar(x, y, z, X):
    """Soluções primitivas positivas de `A^x + B^y = C^z` com `C^z ≤ X` (ordenadas)."""
    sols = []
    A = 1
    while A ** x < X:
        ax = A ** x
        B = 1
        while ax + B ** y <= X:
            C = raiz_inteira(ax + B ** y, z)
            if C and math.gcd(A, math.gcd(B, C)) == 1:
                sols.append((A, B, C))
            B += 1
        A += 1
    return sols


def beal(Xs=(10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6), X_hip=10 ** 15):
    out = {"esferico": {}, "hiperbolico": {}, "euclidiano_333": {}}
    for (x, y, z) in [(2, 2, 2), (2, 2, 3)]:
        chi = F(1, x) + F(1, y) + F(1, z) - 1
        cont = [len(contar(x, y, z, X)) for X in Xs]
        e = (math.log(cont[-1]) - math.log(cont[-2])) / (math.log(Xs[-1]) - math.log(Xs[-2]))
        out["esferico"][f"{x},{y},{z}"] = {"chi": str(chi), "X": list(Xs), "contagem": cont,
                                           "expoente_estimado": e}
    # (3,3,3): nenhuma
    out["euclidiano_333"] = {"chi": "0", "contagem_ate_1e6": len(contar(3, 3, 3, 10 ** 6))}
    # (2,3,7): as duas disposições com soluções conhecidas
    sols = []
    A = 1
    while A ** 7 <= X_hip:  # A^7 + B^3 = C^2
        a7 = A ** 7
        B = 1
        while a7 + B ** 3 <= X_hip:
            C = raiz_inteira(a7 + B ** 3, 2)
            if C and math.gcd(A, math.gcd(B, C)) == 1:
                sols.append(f"{A}^7 + {B}^3 = {C}^2")
            B += 1
        A += 1
    C = 1
    while C ** 7 <= X_hip:  # B^3 + A^2 = C^7
        c7 = C ** 7
        B = 1
        while B ** 3 < c7:
            A = raiz_inteira(c7 - B ** 3, 2)
            if A and math.gcd(A, math.gcd(B, C)) == 1:
                sols.append(f"{B}^3 + {A}^2 = {C}^7")
            B += 1
        C += 1
    out["hiperbolico"]["2,3,7"] = {"chi": str(F(1, 2) + F(1, 3) + F(1, 7) - 1), "X": X_hip, "solucoes": sols}
    return out


# ----------------------------------------------------------------------------------------------
# NS: Burgers viscosa (Cole–Hopf)
def bessel_i(k, z, termos=400):
    s, t = 0.0, (z / 2) ** k / math.factorial(k)
    for m in range(termos):
        s += t
        t *= (z / 2) ** 2 / ((m + 1) * (m + 1 + k))
        if t < 1e-17 * s:
            break
    return s


def burgers_cauda(nu, t, N=256, kmax=None):
    a = 1 / (2 * nu)
    kmax = kmax or N // 2
    I = [bessel_i(k, a) for k in range(kmax + 1)]
    # escala para evitar overflow: divide por I0
    I = [v / I[0] for v in I]
    xs = [2 * math.pi * j / N for j in range(N)]
    u = []
    for x in xs:
        phi = 1.0
        dphi = 0.0
        for k in range(1, kmax + 1):
            c = 2 * I[k] * math.exp(-nu * k * k * t)
            phi += c * math.cos(k * x)
            dphi += -k * c * math.sin(k * x)
        u.append(-2 * nu * dphi / phi)
    # coeficientes de seno (u é ímpar)
    coef = []
    for k in range(1, N // 2):
        b = 2 / N * sum(u[j] * math.sin(k * xs[j]) for j in range(N))
        coef.append(abs(b))
    # largura δ da faixa de analiticidade: inclinação de log|b_k| em k ∈ [K/4, K/2]
    ks = list(range(N // 8, N // 4))
    ys = [math.log(coef[k - 1]) for k in ks if coef[k - 1] > 1e-14]
    ks = [k for k in ks if coef[k - 1] > 1e-14]
    if len(ks) < 4:
        return {"nu": nu, "t": t, "delta": None}
    mk, my = sum(ks) / len(ks), sum(ys) / len(ys)
    sl = sum((k - mk) * (y - my) for k, y in zip(ks, ys)) / sum((k - mk) ** 2 for k in ks)
    return {"nu": nu, "t": t, "delta": -sl, "b1": coef[0], "b10": coef[9], "b20": coef[19]}


def bessel_j(n, x, M=4096):
    """`J_n(x) = (1/2π)∫₀^{2π} cos(nτ − x sin τ) dτ` pela regra do trapézio (integrando periódico)."""
    return sum(math.cos(n * (2 * math.pi * j / M) - x * math.sin(2 * math.pi * j / M)) for j in range(M)) / M


def burgers_inviscido(t=1.0, ks=(1, 2, 5, 16, 64, 256)):
    """Burgers invíscida com `u₀ = sin x`, antes ou no tempo de quebra (`t ≤ 1`).

    Pelas características `x = ξ + t sin ξ`, `u = sin ξ`, os coeficientes de seno são
    `b_k = (1/(kπ))∫ cos(kx) du = (−1)^{k+1}·2J_k(kt)/(kt)`. Confere-se a fórmula contra a quadratura direta
    em `ξ` e, em `t = 1`, `|b_k|·k^{4/3} → 2Γ(1/3)/(2^{2/3}3^{1/6}π)`: a cauda é `k^{−4/3}` (cúspide), não `1/k`.
    Em `t = 0` a fórmula vale no limite (`b_k = δ_{k1}`). Para `t > 1` as características se cruzam e a
    solução entrópica tem choque, que esta fórmula não descreve: recusa com `ValueError`.
    """
    if not 0 <= t <= 1:
        raise ValueError("burgers_inviscido: a fórmula das características só vale para 0 ≤ t ≤ 1")
    M = 8192
    linhas = []
    for k in ks:
        formula = (1.0 if k == 1 else 0.0) if t == 0 else (-1) ** (k + 1) * 2 * bessel_j(k, k * t) / (k * t)
        direto = 2 / M * sum(math.sin(xi) * math.sin(k * (xi + t * math.sin(xi))) * (1 + t * math.cos(xi))
                             for xi in (2 * math.pi * j / M for j in range(M)))
        linhas.append({"k": k, "b_k": formula, "erro_vs_quadratura": abs(formula - direto),
                       "abs_b_k_vezes_k_4_3": abs(formula) * k ** (4 / 3)})
    return {"t": t, "coeficientes": linhas,
            "constante_k_4_3": 2 * math.gamma(1 / 3) / (2 ** (2 / 3) * 3 ** (1 / 6) * math.pi)}


def expoente_largura(t, nus=(0.2, 0.1, 0.05), N=256):
    """Expoente `p` em `δ ∝ ν^p`, entre valores consecutivos de `ν`: `≈ 3/4` em `t = 1`, `≈ 1` em `t = 2`."""
    d = [burgers_cauda(nu, t, N=N)["delta"] for nu in nus]
    if any(x is None or x <= 0 for x in d):  # cauda abaixo de 1e-14 na janela: sem ajuste
        return {"t": t, "delta": d, "p": None}
    return {"t": t, "delta": d,
            "p": [math.log(d[i] / d[i + 1]) / math.log(nus[i] / nus[i + 1]) for i in range(len(d) - 1)]}


def choque_coeficientes(K=10):
    """Ilustração separada: dente de serra `(π − x)/2 = Σ sin(kx)/k`, coeficientes exatamente `1/k`.

    É a forma de um choque já formado (`t > 1`; para `t → ∞` a solução de `u₀ = sin x` fica em dente de
    serra). **Não** é o limite invíscido do experimento em `t = 1`, que é a cúspide de `burgers_inviscido`.
    """
    return [str(F(1, k)) for k in range(1, K + 1)]


# ----------------------------------------------------------------------------------------------
# YM: calibre Z2 em 2D, enumeração exata
def z2_gauge(L=2):
    """Rede `L × L` de plaquetas, contorno livre; pesos `3` (U_p = +1) e `1` (U_p = −1), isto é,
    `e^{2β} = 3`, `tanh β = 1/2`. Devolve `⟨W⟩` exato para retângulos."""
    # elos: horizontais h[i][j] (i = 0..L, j = 0..L-1), verticais v[i][j] (i = 0..L-1, j = 0..L)
    elos = [("h", i, j) for i in range(L + 1) for j in range(L)] + [("v", i, j) for i in range(L) for j in range(L + 1)]
    idx = {e: n for n, e in enumerate(elos)}

    def plaq(cfg, i, j):
        return (cfg[idx[("h", i, j)]] * cfg[idx[("h", i + 1, j)]] * cfg[idx[("v", i, j)]] *
                cfg[idx[("v", i, j + 1)]])

    def wilson(cfg, i0, j0, R, T):
        w = 1
        for j in range(j0, j0 + T):
            w *= cfg[idx[("h", i0, j)]] * cfg[idx[("h", i0 + R, j)]]
        for i in range(i0, i0 + R):
            w *= cfg[idx[("v", i, j0)]] * cfg[idx[("v", i, j0 + T)]]
        return w

    loops = [(1, 1), (1, 2), (2, 2)] if L >= 2 else [(1, 1)]
    Z = 0
    num = {lp: 0 for lp in loops}
    for cfg in product((1, -1), repeat=len(elos)):
        peso = 1
        for i in range(L):
            for j in range(L):
                peso *= 3 if plaq(cfg, i, j) == 1 else 1
        Z += peso
        for (R, T) in loops:
            num[(R, T)] += peso * wilson(cfg, 0, 0, R, T)
    return {f"{R}x{T}": str(F(num[(R, T)], Z)) for (R, T) in loops}


# ----------------------------------------------------------------------------------------------
# P vs NP
def sat(n=10, m=40, seed=1):
    rnd = random.Random(seed)
    clausulas = []
    for _ in range(m):
        vs = rnd.sample(range(n), 3)
        clausulas.append([(v, rnd.random() < 0.5) for v in vs])
    tot = 0
    for v in product((False, True), repeat=n):
        tot += sum(1 for c in clausulas if any(v[i] == s for i, s in c))
    media = F(tot, 2 ** n * m)
    return {"n": n, "m": m, "media_satisfeitas": str(media)}


def schoening(n=12, tentativas=4000, seed=2):
    rnd = random.Random(seed)
    alvo = [rnd.random() < 0.5 for _ in range(n)]
    clausulas = []
    while len(clausulas) < 5 * n:
        vs = rnd.sample(range(n), 3)
        c = [(v, rnd.random() < 0.5) for v in vs]
        if any(alvo[i] == s for i, s in c):
            clausulas.append(c)
    suc = 0
    for _ in range(tentativas):
        v = [rnd.random() < 0.5 for _ in range(n)]
        for _ in range(3 * n):
            ruins = [c for c in clausulas if not any(v[i] == s for i, s in c)]
            if not ruins:
                break
            i, _s = rnd.choice(rnd.choice(ruins))
            v[i] = not v[i]
        if not [c for c in clausulas if not any(v[i] == s for i, s in c)]:
            suc += 1
    return {"n": n, "p_sucesso": suc / tentativas, "cota_(3/4)^n": (3 / 4) ** n}


# ----------------------------------------------------------------------------------------------
# Hodge (sombra topológica): Euler e Descartes
def euler():
    out = {}
    for nome, (p, q) in {"tetraedro": (3, 3), "cubo": (4, 3), "octaedro": (3, 4), "dodecaedro": (5, 3),
                         "icosaedro": (3, 5)}.items():
        chi = F(1, 2) + F(1, p) + F(1, q) - 1
        E, V, Fc = 1 / chi, 2 / (q * chi), 2 / (p * chi)
        defeito = 2 - q * (1 - F(2, p))  # em unidades de π, por vértice
        out[nome] = {"chi": str(chi), "V": str(V), "E": str(E), "F": str(Fc), "V-E+F": str(V - E + Fc),
                     "defeito_por_vertice_pi": str(defeito), "defeito_total_pi": str(V * defeito)}
    out["icosaedro_truncado(bola)"] = {"V": 60, "E": 90, "F": 32, "V-E+F": 60 - 90 + 32}
    return out


# ---------------------------------------------------------------- rodada 106

_B2K = [F(1, 6), F(-1, 30), F(1, 42), F(-1, 30), F(5, 66), F(-691, 2730), F(7, 6), F(-3617, 510)]


def zeta_real(s, N=30):
    """ζ(s) para s real > 1 (Euler–Maclaurin com 8 termos de Bernoulli); erro ≪ 1e-15 para s ≥ 1,05."""
    z = sum(n ** -s for n in range(1, N)) + N ** (1 - s) / (s - 1) + N ** -s / 2
    fat, poch = 1.0, 1.0
    for k, b in enumerate(_B2K, start=1):
        fat *= (2 * k - 1) * (2 * k)
        poch *= (s + 2 * k - 2) if k == 1 else (s + 2 * k - 3) * (s + 2 * k - 2)
        z += float(b) / fat * poch * N ** (-s - 2 * k + 1)
    return z


GAMA1 = 14.134725141734693


def linearizacao(delta=GAMA1 - 14, ms=range(8)):
    """|ζ(−2m−δ)| = 2 sin(πδ/2)·K_m(δ) (equação funcional; `formula_exata`) e a cota 2δ ≤ a/K ≤ πδ."""
    linhas = []
    for m in ms:
        x = 2 * m + 1 + delta
        K = (2 * math.pi) ** (-x) * math.gamma(x) * zeta_real(x)
        a = 2 * abs(math.sin(math.pi * delta / 2)) * K
        linhas.append({"m": m, "centro": 14 - 2 * m, "K": K, "abs_zeta": a, "a_sobre_K": a / K})
    return {"delta": delta, "cota_inferior_2delta": 2 * delta, "cota_superior_pi_delta": math.pi * delta,
            "anel_oito_linear": [0.26, 0.45], "linhas": linhas,
            "minimo_m": min(linhas, key=lambda r: r["abs_zeta"])["m"]}


def primons(sigmas=(2, 3, 4), Ns=(10, 100, 1000)):
    """Gás de primos: Tr_N e^{−σH} = Σ_{i ≤ N} (i+1)^{−σ} → ζ(σ) (`traco_tende_zeta`); parte conexa
    ≤ 2^{2−σ}(π²/6 − 1) (`traco_conexo_le`); lacuna e^{−t·log 2} = 2^{−t} (`peso_um`, `lacuna_atingida`)."""
    out = {}
    for sg in sigmas:
        z = zeta_real(sg)
        tr = {str(N): sum((i + 1) ** -sg for i in range(N + 1)) for N in Ns}
        out[str(sg)] = {"zeta": z, "traco": tr, "resto": {k: z - v for k, v in tr.items()},
                        "conexo": z - 1, "cota_conexo": 2 ** (2 - sg) * (math.pi ** 2 / 6 - 1),
                        "lacuna_fracao": str(F(1, 2 ** sg))}
    out["lacuna"] = "log 2: o primeiro estado excitado (n = 2) pesa 2^{−t}; atingida, não só cota"
    return out


def derivadas_triviais(ms=range(1, 8), deltas=(1e-2, 1e-4, 1e-6)):
    """|ζ′(−2m)| = (2m)!·ζ(2m+1)/(2(2π)^{2m}) (`derivada_fatorial`) contra |ζ(−2m−δ)|/δ (`formula_exata`)."""
    linhas = []
    for m in ms:
        exata = math.factorial(2 * m) * zeta_real(2 * m + 1) / (2 * (2 * math.pi) ** (2 * m))
        quoc = {}
        for d in deltas:
            x = 2 * m + 1 + d
            K = (2 * math.pi) ** (-x) * math.gamma(x) * zeta_real(x)
            quoc[f"{d:g}"] = 2 * abs(math.sin(math.pi * d / 2)) * K / d
        linhas.append({"m": m, "derivada_exata": exata, "quociente": quoc,
                       "erro_relativo_menor_delta": abs(quoc[f"{deltas[-1]:g}"] / exata - 1)})
    return {"linhas": linhas, "menos_dois": "|ζ′(−2)| = ζ(3)/(4π²) = " + repr(zeta_real(3) / (4 * math.pi ** 2))}


def moebius_crivo(N):
    mu = [1] * (N + 1)
    eh_primo = [True] * (N + 1)
    for p in range(2, N + 1):
        if eh_primo[p]:
            for k in range(p, N + 1, p):
                if k > p:
                    eh_primo[k] = False
                mu[k] = -mu[k]
            for k in range(p * p, N + 1, p * p):
                mu[k] = 0
    mu[0] = 0
    return mu


def fermions(sigmas=(2, 3), Ns=(10, 100, 10000)):
    """Gás fermiônico: Σ_{n ≤ N} μ(n) n^{−σ} → 1/ζ(σ) (`traco_fermionico`); índice de Witten
    Σ_{d|n} μ(d) = [n = 1] (`indice_witten`); M(x) = Σ_{n ≤ x} μ(n) (a cauda que decide RH)."""
    N = max(Ns)
    mu = moebius_crivo(max(N, 200))  # o índice de Witten abaixo vai até n = 200
    out = {}
    for sg in sigmas:
        alvo = 1 / zeta_real(sg)
        out[str(sg)] = {"inverso_zeta": alvo,
                        "traco": {str(n): sum(mu[k] * k ** -sg for k in range(1, n + 1)) for n in Ns}}
    out["witten_ate_200"] = all(sum(mu[d] for d in range(1, n + 1) if n % d == 0) == (1 if n == 1 else 0)
                                for n in range(1, 201))
    M = 0
    maxrazao = 0.0
    for x in range(1, N + 1):
        M += mu[x]
        if x >= 10:
            maxrazao = max(maxrazao, abs(M) / math.sqrt(x))
    out["mertens"] = {"N": N, "M(N)": M, "max |M(x)|/sqrt(x), 10 <= x <= N": maxrazao}
    return out


def main(saida=None, P=10000, rapido=False):
    out = {
        "zeros": zeros(),
        "bsd_produtos": bsd_produtos(P=P, marcos=(100, 1000, P) if P > 1000 else (100, P)),
        "bsd_11a1": bsd_razao_11a1(),
        "beal": beal(Xs=(10 ** 3, 10 ** 4, 10 ** 5) if rapido else (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6),
                     X_hip=10 ** 9 if rapido else 10 ** 15),
        "burgers": [burgers_cauda(nu, 1.0, N=128 if rapido else 256) for nu in (0.2, 0.1, 0.05)],
        "burgers_inviscido_t1": burgers_inviscido(1.0),
        "burgers_expoente_largura": [expoente_largura(1.0, N=128 if rapido else 256),
                                     expoente_largura(2.0, N=128 if rapido else 256)],
        "choque_coeficientes": choque_coeficientes(),
        "z2_gauge": z2_gauge(2),
        "sat": sat(),
        "schoening": schoening(tentativas=500 if rapido else 4000),
        "euler": euler(),
        "linearizacao": linearizacao(),
        "primons": primons(),
        "derivadas_triviais": derivadas_triviais(),
        "fermions": fermions(),
        "aviso": "numérico; nada aqui é certificado — os teoremas estão em atk-kernel/ATK/Fracoes*.lean",
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "caudas.json")
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = main()
    print(json.dumps({k: v for k, v in o.items() if k != "zeros"}, ensure_ascii=False, indent=1)[:6000])
    for z in o["zeros"]:
        print(z["nome"], z["quocientes"], z["cauda_float"], z["convergente"])
