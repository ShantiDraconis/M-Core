# gram_iv.py — Gram de Báez-Duarte G_N e vetor b em aritmética intervalar (mpmath.iv).
#
#   H = L^2(0,inf), chi = 1_(0,1], rho_k(x) = {1/(kx)}.
#   b_k = <chi, rho_k> = (log k + 1 - gamma)/k
#   G_ij = <rho_i, rho_j>  (fórmula de Vasyunin 1995; Landreau–Richard 2002, Thm 2.1; Bettin–Conrey 2013, eq. 13):
#     d = gcd(i,j), h = i/d, k = j/d, h < k (após troca),
#     G_ij = (1/d) [ (log 2pi - gamma)/2 (1/h + 1/k) + (k-h)/(2hk) log(h/k) - pi/(2hk) (V(h,k) + V(k,h)) ],
#     V(h,k) = sum_{m=1}^{k-1} {mh/k} cot(pi m/k),  V(k,h) = V(k mod h, h),  V(k,1) = 0,
#     G_ii = (log 2pi - gamma)/i.
#   Pareando m e k-m (gcd(h,k)=1, cot(pi(k-m)/k) = -cot(pi m/k), cot(pi/2) = 0):
#     V(h,k) = (1/k) sum_{1 <= m < k/2} (2 (mh mod k) - k) cot(pi m/k)   (pesos inteiros exatos).
#
# Rigor: toda operação é feita em mpmath.iv (arredondamento para fora em +,-,*,/,sqrt).  Os valores
# transcendentes de base (pi, gamma, log k, cos/sin) vêm das rotinas de mpmath com arredondamento
# dirigido; por segurança cada um é ainda inflado por um fator relativo EPS_INFL = 1e-50 (com dps = 60; 1e-(dps-10) em geral),
# de modo que basta que essas rotinas acertem 50 dígitos relativos.
from math import gcd
from mpmath import iv, mp

EPS_INFL = '1e-50'


def lo(x):
    """extremo inferior exato (mp.mpf, sem arredondamento)"""
    return mp.make_mpf(x._mpi_[0])


def hi(x):
    return mp.make_mpf(x._mpi_[1])


def width(x):
    return hi(x) - lo(x)


def build(N, dps=60, eps=None, verbose=True):
    import time
    t0 = time.time()
    iv.dps = dps
    if eps is None:
        eps = EPS_INFL if dps == 60 else '1e-%d' % (dps - 10)
    E = iv.mpf(['-' + eps, eps])

    def infl(x):
        return x + E * abs(x)

    PI = infl(iv.mpf(iv.pi))
    GAM = infl(iv.mpf(iv.euler))
    A = infl(iv.log(2 * PI)) - GAM          # log 2pi - gamma
    L = [None, iv.mpf(0)] + [infl(iv.log(iv.mpf(k))) for k in range(2, N + 1)]
    # tabela de cot(pi m/k), 1 <= m < k/2, uma vez por k
    cot = {}
    for k in range(2, N + 1):
        M = (k - 1) // 2
        row = []
        for m in range(1, M + 1):
            x = PI * m / k
            row.append(infl(iv.cos(x) / iv.sin(x)))
        cot[k] = row
    t_cot = time.time() - t0
    # inteiros como intervalos (exatos)
    W = {w: iv.mpf(w) for w in range(-N, N + 1)}
    # V(h,k) para 1 <= h < k <= N, gcd = 1 (memoizado)
    V = {}
    for k in range(2, N + 1):
        ck = cot[k]
        M = len(ck)
        for h in range(1, k):
            if gcd(h, k) != 1:
                continue
            s = iv.mpf(0)
            r = 0
            for m in range(M):
                r += h
                if r >= k:
                    r -= k
                s = s + W[2 * r - k] * ck[m]
            V[(h, k)] = s / k
    t_V = time.time() - t0
    # G0(h,k) para coprimos h < k
    half = iv.mpf(1) / 2
    G0 = {}
    for (h, k), vhk in V.items():
        vkh = iv.mpf(0) if h == 1 else V[(k % h, h)]
        hk2 = 2 * h * k
        g = (A * half * (iv.mpf(1) / h + iv.mpf(1) / k)
             + iv.mpf(k - h) / hk2 * (L[h] - L[k])
             - PI / hk2 * (vhk + vkh))
        G0[(h, k)] = g
    # matriz completa 0-indexada (simétrica)
    G = [[None] * N for _ in range(N)]
    for i in range(1, N + 1):
        G[i - 1][i - 1] = A / i
        for j in range(i + 1, N + 1):
            d = gcd(i, j)
            g = G0[(i // d, j // d)]
            if d > 1:
                g = g / d
            G[i - 1][j - 1] = g
            G[j - 1][i - 1] = g
    b = [(L[k] + 1 - GAM) / k for k in range(1, N + 1)]
    t_G = time.time() - t0
    if verbose:
        print(f"[build N={N} dps={dps}] cot {t_cot:.1f}s, V {t_V:.1f}s ({len(V)} pares), G {t_G:.1f}s", flush=True)
    return dict(G=G, b=b, A=A, GAM=GAM, PI=PI, L=L, V=V, cot=cot, N=N, dps=dps)
