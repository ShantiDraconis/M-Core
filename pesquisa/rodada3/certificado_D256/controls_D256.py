# controls_D256.py — controles do certificado intervalar de D_256 (não fazem parte da prova).
#  (1) G_11 contém log 2pi - gamma; G_ii = G_11/i.
#  (2) V pela definição completa sum_{m<k} {mh/k} cot(pi m/k) (iv) contra a forma pareada usada no certificado.
#  (3) todas as 32 896 entradas contra uma implementação independente em double (definição completa de V).
#  (4) amostra de entradas contra o código C da wave2 (RH_Gram_dn, binary128 e dd, variável DUMPG).
#  (5) algumas G_ij e b_k contra integração numérica direta (mp.quad, não rigorosa), cauda por momentos + Hurwitz zeta.
#  (6) D_256 do código C (dd e binary128) dentro do envelope.
import sys, os, math, random, subprocess, time
from math import gcd
from mpmath import iv, mp
from gram_iv import build, lo, hi, width

N = 256
CBIN = "/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/wave2/code/RH_Gram_dn"
D = build(N, 60)
G, b = D['G'], D['b']
mp.dps = 60
def mid(x): return (lo(x) + hi(x)) / 2
def contains(x, v, tol=0):
    v = mp.mpf(v); return lo(x) - tol <= v <= hi(x) + tol

# (1)
mp.dps = 100
A100 = mp.log(2 * mp.pi) - mp.euler
mp.dps = 60
print("(1) G_11 contém log 2pi - gamma:", contains(G[0][0], A100), " largura", mp.nstr(width(G[0][0]), 3),
      "| G_ii = G_11/i contém A/i p/ todo i:", all(contains(G[i][i], A100 / (i + 1)) for i in range(N)))

# (2) definição completa de V em iv, pares de amostra
PI = D['PI']; V = D['V']
def V_full(h, k):
    s = iv.mpf(0)
    for m in range(1, k):
        x = PI * m / k
        s = s + iv.mpf(m * h % k) / k * (iv.cos(x) / iv.sin(x))
    return s
pairs = [(1, 2), (2, 7), (3, 10), (5, 7), (7, 128), (37, 255), (100, 251), (255, 256), (1, 256), (17, 240)]
ok2 = True; dmax = mp.mpf(0)
for h, k in pairs:
    vf, vp = V_full(h, k), V[(h, k)]
    ok2 &= (lo(vf) <= hi(vp) and lo(vp) <= hi(vf)); dmax = max(dmax, abs(mid(vf) - mid(vp)))
print(f"(2) V completo x pareado em {len(pairs)} pares: intervalos se intersectam = {ok2}, |dif. dos meios| máx {mp.nstr(dmax, 3)}")

# (3) double independente, todas as entradas
gam = 0.57721566490153286061; Af = math.log(2 * math.pi) - gam
def Vf(h, k):
    return sum(((m * h) % k) / k / math.tan(math.pi * m / k) for m in range(1, k))
emax = 0.0; worst = None
for i in range(1, N + 1):
    for j in range(i, N + 1):
        d = gcd(i, j); h, k = i // d, j // d
        if k == 1:
            gf = Af / d
        else:
            vkh = 0.0 if h == 1 else Vf(k % h, h)
            gf = (Af / 2 * (1 / h + 1 / k) + (k - h) / (2 * h * k) * math.log(h / k)
                  - math.pi / (2 * h * k) * (Vf(h, k) + vkh)) / d
        e = abs(float(mid(G[i - 1][j - 1])) - gf)
        if e > emax: emax, worst = e, (i, j)
print(f"(3) {N*(N+1)//2} entradas x double independente: |dif| máx {emax:.2e} em {worst}")

# (4) código C da wave2: binary128 e dd
random.seed(256)
samp = sorted({(random.randint(1, N), random.randint(1, N)) for _ in range(3000)} |
              {(1, 1), (1, 2), (2, 3), (255, 256), (256, 256), (128, 256), (1, 256), (191, 193)})
envs = ",".join(f"{i}:{j}" for i, j in samp)
for ty, tol in (("q", mp.mpf('1e-30')), ("dd", mp.mpf('1e-27'))):
    env = dict(os.environ, DUMPG=envs, DUMPONLY="1")
    p = subprocess.run([CBIN, ty, str(N), "/dev/null"], env=env, capture_output=True, text=True)
    vals = [ln.split() for ln in p.stderr.splitlines() if ln.startswith("G ")]
    bad = 0; rmax = mp.mpf(0)
    for _, i, j, v in vals:
        g = G[int(i) - 1][int(j) - 1]
        rmax = max(rmax, abs(mp.mpf(v) - mid(g)) / abs(mid(g)))
        if not contains(g, v, tol * abs(mid(g))): bad += 1
    print(f"(4) {len(vals)} entradas do C ({ty}): fora de [G] ± {mp.nstr(tol,1)}·|G|: {bad};  |dif|/|G| máx {mp.nstr(rmax, 3)}")

# (5) integração direta (não rigorosa), dps 40; meios de [G] tomados com 60 dígitos
Gmid = {(i, j): mid(G[i - 1][j - 1]) for i in range(1, 11) for j in range(1, 11)}
bmid = {k: mid(b[k - 1]) for k in range(1, 11)}
mp.dps = 40
def direct(i, j, M=20, R=60):
    Lc = i * j // gcd(i, j)
    def seg_int(a, bnd, r=0):  # ∫_a^b {t/i}{t/j} t^(r-2) dt com pisos fixos (integrando suave)
        tm = (a + bnd) / 2; p, q = int(mp.floor(tm / i)), int(mp.floor(tm / j))
        return mp.quad(lambda t: (t / i - p) * (t / j - q) * t ** (r - 2), [a, bnd])
    def pts(X):
        s = sorted({mp.mpf(m * i) for m in range(0, X // i + 1)} | {mp.mpf(m * j) for m in range(0, X // j + 1)})
        return s
    X = M * Lc
    P = pts(X)
    head = mp.mpf(min(i, j)) / (i * j) + mp.fsum(seg_int(P[n], P[n + 1]) for n in range(len(P) - 1) if P[n] >= min(i, j))
    # cauda: sum_{n>=M} ∫_0^L f(s)/(nL+s)^2 ds = sum_r (-1)^r (r+1) m_r L^{-r-2} zeta(r+2, M),  m_r = ∫_0^L f(s) s^r ds
    PL = pts(Lc)
    def mom(r):
        return mp.fsum(seg_int(PL[n], PL[n + 1], r + 2) for n in range(len(PL) - 1))
    tail = mp.fsum((-1) ** r * (r + 1) * mom(r) * mp.mpf(Lc) ** (-r - 2) * mp.zeta(r + 2, M) for r in range(R))
    return head + tail
def direct_b(k, M=40, R=60):  # b_k = ∫_1^inf {t/k} t^-2 dt
    head = mp.fsum(mp.quad(lambda t, n=n: (t / k - n) / t ** 2, [max(1, n * k), (n + 1) * k]) for n in range(M))
    mom = lambda r: mp.quad(lambda s: (s / k) * s ** r, [0, k])
    tail = mp.fsum((-1) ** r * (r + 1) * mom(r) * mp.mpf(k) ** (-r - 2) * mp.zeta(r + 2, M) for r in range(R))
    return head + tail
t = time.time()
dm = mp.mpf(0)
for i, j in [(1, 1), (1, 2), (2, 3), (3, 5), (5, 7), (4, 6), (7, 10), (6, 9)]:
    v = direct(i, j); e = abs(v - Gmid[(i, j)]); dm = max(dm, e)
    print(f"    G({i},{j}): direto {mp.nstr(v, 22)}  |dif| {mp.nstr(e, 2)}")
for k in (1, 3, 10):
    v = direct_b(k); e = abs(v - bmid[k]); dm = max(dm, e)
    print(f"    b_{k}: direto {mp.nstr(v, 22)}  |dif| {mp.nstr(e, 2)}")
print(f"(5) integração direta: |dif| máx {mp.nstr(dm, 3)}  ({time.time()-t:.1f}s)")

# (6) D_256 do código C
mp.dps = 60
encl = (mp.mpf('0.00823371627726102144159803810263543453410462295'), mp.mpf('0.00823371627726102144159803810263543453410462301'))
for ty in ("dd", "q"):
    out = f"/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/wave3/cert/c_{ty}_256.tsv"
    subprocess.run([CBIN, ty, str(N), out], capture_output=True)
    last = open(out).read().split("\n")[-2].split("\t")
    v = mp.mpf(last[1]); e = 0 if encl[0] <= v <= encl[1] else min(abs(v - encl[0]), abs(v - encl[1]))
    print(f"(6) D_256 do C ({ty}) = {last[1]}  distância ao envelope {mp.nstr(e, 3)}  (rel. {mp.nstr(e / v, 2)})")
    os.remove(out)
