"""Tarefa 1+2: verifica a fórmula de Vasyunin contra integração direta (independente) e confere as
afirmações repassadas. Integração direta: G_hk = int_0^inf {t/h}{t/k} t^-2 dt (x = 1/t), exata por
pedaços até X = M*lcm(h,k); cauda = sum_n (-1)^n (n+1) m_n L^-(n+2) zeta(n+2, M), m_n = int_0^L f s^n
(momentos racionais exatos). Nada do kernel é importado."""
import sys
from fractions import Fraction as Fr
from math import gcd
import mpmath as mp
mp.mp.dps = 45

def lcm(a, b): return a * b // gcd(a, b)

def direct(h, k, M=20, nterms=60):
    L = lcm(h, k)
    X = M * L
    pts = sorted(set(list(range(0, X + 1, h)) + list(range(0, X + 1, k))))
    tot = mp.mpf(min(h, k)) / (h * k)
    for u, v in zip(pts, pts[1:]):
        if v <= min(h, k):
            continue
        a, b = u // h, u // k
        tot += mp.mpf(v - u) / (h * k) - (mp.mpf(b) / h + mp.mpf(a) / k) * mp.log(mp.mpf(v) / u) \
               + a * b * (mp.mpf(1) / u - mp.mpf(1) / v)
    # momentos exatos num período
    pp = sorted(set(list(range(0, L + 1, h)) + list(range(0, L + 1, k))))
    tail = mp.mpf(0)
    for n in range(nterms):
        mn = Fr(0)
        for u, v in zip(pp, pp[1:]):
            a, b = u // h, u // k
            c = Fr(b, h) + Fr(a, k)
            F = lambda s: Fr(s ** (n + 3), (n + 3) * h * k) - c * Fr(s ** (n + 2), n + 2) + a * b * Fr(s ** (n + 1), n + 1)
            mn += F(v) - F(u)
        term = (-1) ** n * (n + 1) * (mp.mpf(mn.numerator) / mn.denominator) / mp.mpf(L) ** (n + 2) * mp.zeta(n + 2, M)
        tail += term
    return tot + tail

def V(h, k, inv=False):
    if k == 1: return mp.mpf(0)
    hh = pow(h, -1, k) if inv else h
    return mp.fsum(mp.mpf((m * hh) % k) / k * mp.cot(mp.pi * m / k) for m in range(1, k))

def vas(h, k, inv=False):
    d = gcd(h, k); h0, k0 = h // d, k // d
    t = (mp.log(2 * mp.pi) - mp.euler) / 2 * (mp.mpf(1) / h0 + mp.mpf(1) / k0)
    if h0 != k0: t += mp.mpf(k0 - h0) / (2 * h0 * k0) * mp.log(mp.mpf(h0) / k0)
    t -= mp.pi / (2 * h0 * k0) * (V(h0, k0, inv) + V(k0, h0, inv))
    return t / d

pairs = [(1,1),(1,2),(1,3),(2,3),(1,7),(3,5),(2,7),(3,7),(5,7),(4,9),(7,10),(5,12),(8,13),(11,17),
         (12,18),(6,10),(9,12),(13,29),(17,23),(10,25)]
print("h k | direto (M=20) | |direto(M=20)-direto(M=40)| | |Vasyunin-direto| | |variante h^-1 - direto|")
worst = 0
for h, k in pairs:
    d20 = direct(h, k, 20); d40 = direct(h, k, 40)
    e = abs(vas(h, k) - d20); worst = max(worst, e)
    print(f"{h} {k} | {mp.nstr(d20, 30)} | {mp.nstr(abs(d20-d40),3)} | {mp.nstr(e,3)} | {mp.nstr(abs(vas(h,k,True)-d20),3)}")
print("pior |Vasyunin - direto| =", mp.nstr(worst, 3))
g = mp.euler; A = mp.log(2*mp.pi) - g
print("G11 direto - (log2pi - gamma) =", mp.nstr(direct(1,1) - A, 3))
print("G(12,18) - G(2,3)/6 =", mp.nstr(direct(12,18) - direct(2,3)/6, 3))

# b_k direto: int_0^1 {1/(kx)} dx = (1/k) int_{1/k}^inf {t}/t^2 dt  (pedaços exatos + cauda)
def bdirect(k, M=4000):
    s = mp.log(k) if k > 1 else mp.mpf(0)          # int_{1/k}^1 dt/t
    # int_1^inf {t}/t^2 = sum_n int_n^{n+1} (t-n)/t^2 = sum_n [log((n+1)/n) - n(1/n - 1/(n+1))]
    s += mp.nsum(lambda n: mp.log((n+1)/n) - 1/(n+1), [1, mp.inf])
    return s / k
print("\n== Afirmações repassadas ==")
for k in [1, 2, 3, 7]:
    bd = bdirect(k)
    print(f"b_{k}: direto={mp.nstr(bd,20)}  (log k+1-g)/k={mp.nstr((mp.log(k)+1-g)/k,20)}  (1-g-log k)/k={mp.nstr((1-g-mp.log(k))/k,20)}")
print("||rho_1||^2 direto =", mp.nstr(direct(1,1), 25), " log2pi-g =", mp.nstr(A, 25), " log2pi-g-1 =", mp.nstr(A-1, 25))
p = 1 - g
D1 = 1 - p**2 / A
print("D_1 = 1-(1-g)^2/(log2pi-g) =", mp.nstr(D1, 25))
B = vas(1, 2); print("B = <rho1,rho2> =", mp.nstr(B, 25), " direto:", mp.nstr(direct(1,2), 25))
C = vas(2, 2); q = (mp.log(2) + 1 - g) / 2
print("C = G22 =", mp.nstr(C, 20), " A/2 =", mp.nstr(A/2, 20))
gain = (A*q - B*p)**2 / (A*(A*C - B**2))
G2 = mp.matrix([[A, B], [B, C]]); bb = mp.matrix([p, q])
D2 = 1 - (bb.T * mp.lu_solve(G2, bb))[0]
print("D_1-D_2 fórmula =", mp.nstr(gain, 25), "  direto 2x2: D_2 =", mp.nstr(D2, 25), " D_1-D_2 =", mp.nstr(D1 - D2, 25))
qw = (1 - g - mp.log(2)) / 2
bw = mp.matrix([p, qw]); D2w = 1 - (bw.T * mp.lu_solve(G2, bw))[0]
print("com b errado (1-g-log k)/k: D_2 =", mp.nstr(D2w, 20))
