#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/* e ATK/TruncamentoToeplitz (rodada 16).

Só biblioteca padrão. Nada aqui é certificado e nada prova HR: são as verificações finitas que o
kernel **não** faz (ζ em pontos da faixa, mínimos m_n em malhas, sinais de menores de Toeplitz).

* ζ por Euler–Maclaurin de ordem 2K, conferida em ζ(2), ζ(−2) = 0 e no 1º zero 1/2 + 14,1347…i;
* órbita {ρ, ρ̄, 1 − ρ, 1 − ρ̄} do 1º zero (todos ≈ 0), cardinal 2 na reta (`quarteto_ou_par`);
* K₃ = ∅ (`K_tres`); m_n = min |ζ| numa malha **global** de K_n, n = 4..16 — as malhas são encaixadas,
  logo os mínimos decrescem exatamente (`m_antitone`); a queda forte em n = 15 vem do 1º zero
  (altura 14,13 ≤ 15, distância 1/15 da reta);
* camada B heurística: margem min|ζ(c)| − L·h/√2 com L ≈ max|ζ′| por diferenças (`certificado_derivada`);
* truncamento de Toeplitz: sinais de **todos** os menores com índices ≤ N, N = 0..6 (`P`), o menor 3×3
  `a₁³ − 2a₀a₁a₂ + a₀²a₃` (`menor3`), D₂ e o fluxo (`D2_fluxo`, `volta_ingenua_invalida`);
* lei de existência: z² + 1 tem zero imaginário puro e nenhum real (`exemplo_quadrado`).
"""
import cmath
import itertools
import json
import math
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edrei  # noqa: E402

B2K = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6, -3617 / 510, 43867 / 798,
       -174611 / 330]
GAMMA1 = 14.134725141734693


def zeta(s, N=None, K=10):
    """ζ(s) por Euler–Maclaurin (s ≠ 1)."""
    s = complex(s)
    if N is None:
        N = max(20, int(abs(s)) + 20)
    tot = sum(n ** (-s) for n in range(1, N))
    Ns = N ** (-s)
    tot += N * Ns / (s - 1) + Ns / 2
    poch, Npow, fact = s, Ns / N, 2.0
    for k in range(1, K + 1):
        tot += B2K[k - 1] / fact * poch * Npow
        poch *= (s + 2 * k - 1) * (s + 2 * k)
        Npow /= N * N
        fact *= (2 * k + 1) * (2 * k + 2)
    return tot


def zero_newton(s0, it=30):
    s = complex(s0)
    for _ in range(it):
        h = 1e-6
        d = (zeta(s + h) - zeta(s - h)) / (2 * h)
        s -= zeta(s) / d
    return s


def orbita(rho, c=0.5):
    return [rho, rho.conjugate(), 2 * c - rho, 2 * c - rho.conjugate()]


def card_orbita(z, c=0.5, tol=1e-12):
    pts = []
    for w in orbita(z, c):
        if all(abs(w - p) > tol for p in pts):
            pts.append(w)
    return len(pts)


def K_contem(n, s):
    return 1 / n <= s.real <= 0.5 - 1 / n and 1 / n <= s.imag <= n


HS, HT = 0.0125, 0.0125  # malha global: σ = j·HS, t = k·HT


def malha_K(n):
    j0, j1 = math.ceil((1 / n) / HS - 1e-9), math.floor((0.5 - 1 / n) / HS + 1e-9)
    k0, k1 = math.ceil((1 / n) / HT - 1e-9), math.floor(n / HT + 1e-9)
    return [(j, k) for j in range(j0, j1 + 1) for k in range(k0, k1 + 1)]


_cache = {}


def zg(j, k):
    if (j, k) not in _cache:
        _cache[(j, k)] = zeta(complex(j * HS, k * HT))
    return _cache[(j, k)]


def m_malha(n):
    pts = malha_K(n)
    if not pts:
        return 0.0, None
    v, arg = min((abs(zg(j, k)), (j * HS, k * HT)) for j, k in pts)
    return v, arg


def lipschitz_heur(n):
    """max|ζ′| ≈ diferenças entre vizinhos da malha (heurístico)."""
    pts = set(malha_K(n))
    L = 0.0
    for j, k in pts:
        for dj, dk, h in ((1, 0, HS), (0, 1, HT)):
            if (j + dj, k + dk) in pts:
                L = max(L, abs(zg(j + dj, k + dk) - zg(j, k)) / h)
    return L


def coef(n_max=12):
    return [edrei.a_xi(n) for n in range(n_max)]


def toep(a, i, j):
    return a[i - j] if 0 <= i - j < len(a) else Fr(0)


def det(M):
    M = [list(r) for r in M]
    n, d = len(M), Fr(1)
    for i in range(n):
        p = next((k for k in range(i, n) if M[k][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        for k in range(i + 1, n):
            f = M[k][i] / M[i][i]
            for jj in range(i, n):
                M[k][jj] -= f * M[i][jj]
    return d


def menor(a, I, J):
    return det([[toep(a, i, j) for j in J] for i in I])


def sinais_P(a, N, eps=1e-12, amostras=3, semente=1):
    """Classifica todos os menores com índices ≤ N: (positivos, zeros estruturais, indeterminados, negativos)."""
    rng = random.Random(semente + N)
    af = [Fr(x) for x in a]
    pert = [[Fr(x * (1 + eps * (2 * rng.random() - 1)))
             for x in a] for _ in range(amostras)]
    pos = zer = ind = neg = 0
    for r in range(1, N + 2):
        for I in itertools.combinations(range(N + 1), r):
            for J in itertools.combinations(range(N + 1), r):
                d0 = menor(af, I, J)
                if d0 == 0:
                    zer += 1
                    continue
                sg = {d0 > 0}
                for ap in pert:
                    sg.add(menor(ap, I, J) > 0)
                if len(sg) == 2:
                    ind += 1
                elif d0 > 0:
                    pos += 1
                else:
                    neg += 1
    return pos, zer, ind, neg


def D2(a, n):
    return a[n + 1] ** 2 - a[n] * a[n + 2]


def fluxo(a, tau):
    return [a[n] * math.exp(-tau * n * (n - 1)) for n in range(len(a))]


def main(saida=None):
    controles = {
        "zeta(2)-pi^2/6": abs(zeta(2) - math.pi ** 2 / 6),
        "zeta(-2)": abs(zeta(-2)),
        "|zeta(1/2+i*gamma1)|": abs(zeta(complex(0.5, GAMMA1))),
    }
    rho = zero_newton(complex(0.5, 14.13))
    orb = [abs(zeta(w)) for w in orbita(rho)]
    ms = {}
    for n in range(3, 17):
        v, arg = m_malha(n)
        ms[str(n)] = {"m_malha": format(v, ".6g"), "argmin": arg}
    camadaB = {}
    for n in (4, 6, 8, 10):
        L = lipschitz_heur(n)
        v, _ = m_malha(n)
        camadaB[str(n)] = {"L_heur": format(L, ".4g"), "margem": format(v - L * math.hypot(HS, HT) / 2, ".4g")}
    a = coef(12)
    P = {str(N): dict(zip(("pos", "zero_estr", "indet", "neg"), sinais_P(a, N))) for N in range(0, 6)}
    m3 = a[1] ** 3 - 2 * a[0] * a[1] * a[2] + a[0] ** 2 * a[3]
    d2 = [format(D2(a, n) / a[n + 1] ** 2, ".6g") for n in range(9)]
    fl = {str(t): [format(D2(fluxo(a, t), n) / (math.exp(-2 * t * (n + 1) * n) * a[n + 1] ** 2), ".6g")
                   for n in range(5)] for t in (0.0, 0.1, 1.0)}
    ex = [1.0, 1.0, 2.0, 1.0]
    res = {
        "controles_zeta": {k: format(v, ".3g") for k, v in controles.items()},
        "primeiro_zero": [rho.real, rho.imag],
        "orbita_|zeta|": [format(x, ".3g") for x in orb],
        "orbita_card": card_orbita(rho),
        "K3_vazio": not malha_K(3),
        "m_n_malha(h=0.0125)": ms,
        "camada_B_heuristica": camadaB,
        "P(N)_sinais_menores": P,
        "menor3=a1^3-2a0a1a2+a0^2a3": format(m3, ".6g"),
        "menor3/a1^3": format(m3 / a[1] ** 3, ".6g"),
        "D2_normalizado_n=0..8": d2,
        "fluxo_D2_normalizado": fl,
        "volta_ingenua": {"D2(a)_0": D2(ex, 0), "D2(b(1))_0": D2(fluxo(ex, 1.0), 0)},
        "z2+1": {"|f(i)|": abs(1j ** 2 + 1), "min_real_|f|": min(abs(x * x + 1) for x in
                                                                [k / 100 for k in range(-500, 501)])},
        "aviso": "verificação finita em ponto flutuante; ∀ n ≥ 4, m_n > 0 é HR (OPEN_MATH); m₄ > 0 é finita mas "
                 "sem certificado no kernel (BUILD_PENDING: aritmética intervalar de ζ)",
    }
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
