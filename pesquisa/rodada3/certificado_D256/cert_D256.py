# cert_D256.py — certificado intervalar de D_256 = min_c ||chi - sum_{k<=256} c_k rho_k||^2.
#
#  Cota superior:  D_N <= Q(c) = 1 - 2 b.c + c^T G c  para todo c (definição de mínimo).  c racional (n_k/10^d).
#  Cota inferior:  Q(c) - D_N = (c - c*)^T G (c - c*) = r^T G^{-1} r <= ||r||^2 / lambda_min(G),  r = G c - b,
#                  com lambda_min(G) >= mu certificado por Cholesky intervalar de G - mu I (todos os pivôs > 0).
#  Tudo que entra nas cotas é calculado em mpmath.iv; a parte não rigorosa (c* em mp, estimativa de lambda_min,
#  arredondamento de Babai) só escolhe c e mu, e as cotas não dependem de como foram escolhidos.
# Uso: python3 cert_D256.py [N=256] [dps=60] [rump|ivchol|both]
import sys, time, json
from mpmath import iv, mp
from gram_iv import build, lo, hi, width

N = int(sys.argv[1]) if len(sys.argv) > 1 else 256
DPS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
ALVO = mp.mpf(823372) / 10**8          # hipótese do kernel: D_256 <= 0,00823372
OUT = {}
T0 = time.time()

D = build(N, DPS)
G, b = D['G'], D['b']
OUT['t_build'] = time.time() - T0
mp.dps = DPS
wG = max(width(G[i][j]) for i in range(N) for j in range(i, N))
wb = max(width(x) for x in b)
print(f"largura máx.: G {mp.nstr(wG, 3)}, b {mp.nstr(wb, 3)}")
OUT['width_G_max'] = mp.nstr(wG, 4); OUT['width_b_max'] = mp.nstr(wb, 4)

# ---------- parte NÃO rigorosa: c* = G^{-1} b em mp (dps 50) sobre os pontos médios ----------
t = time.time()
mp.dps = 50
Gm = [[(lo(G[i][j]) + hi(G[i][j])) / 2 for j in range(N)] for i in range(N)]
bm = [(lo(x) + hi(x)) / 2 for x in b]
Lm = [[mp.mpf(0)] * N for _ in range(N)]
for j in range(N):
    s = Gm[j][j] - mp.fsum(Lm[j][k] ** 2 for k in range(j))
    Lm[j][j] = mp.sqrt(s)
    for i in range(j + 1, N):
        Lm[i][j] = (Gm[i][j] - mp.fdot(Lm[i][:j], Lm[j][:j])) / Lm[j][j]
y = [mp.mpf(0)] * N
for i in range(N):
    y[i] = (bm[i] - mp.fdot(Lm[i][:i], y[:i])) / Lm[i][i]
cs = [mp.mpf(0)] * N
for i in range(N - 1, -1, -1):
    cs[i] = (y[i] - mp.fsum(Lm[j][i] * cs[j] for j in range(i + 1, N))) / Lm[i][i]
D_float = 1 - mp.fsum(v * v for v in y)
piv = [Lm[j][j] ** 2 for j in range(N)]
print(f"[c* não rigoroso] {time.time()-t:.1f}s  D_N(mp) = {mp.nstr(D_float, 30)}  pivô mín = {mp.nstr(min(piv), 4)}"
      f"  soma pivôs = {mp.nstr(mp.fsum(piv), 5)}  max|c*| = {mp.nstr(max(abs(v) for v in cs), 5)}")
OUT['D_mp_nonrig'] = mp.nstr(D_float, 40); OUT['t_solve'] = time.time() - t

# lambda_min por iteração inversa (double basta: só escolhe mu)
Lf = [[float(v) for v in row] for row in Lm]
def solve_f(v):
    z = [0.0] * N
    for i in range(N):
        z[i] = (v[i] - sum(Lf[i][k] * z[k] for k in range(i))) / Lf[i][i]
    x = [0.0] * N
    for i in range(N - 1, -1, -1):
        x[i] = (z[i] - sum(Lf[j][i] * x[j] for j in range(i + 1, N))) / Lf[i][i]
    return x
Gf = [[float(v) for v in row] for row in Gm]
x = [1.0 / (k + 1) ** 0.5 * (-1) ** k for k in range(N)]
for it in range(60):
    x = solve_f(x); nx = sum(v * v for v in x) ** 0.5; x = [v / nx for v in x]
Gx = [sum(Gf[i][j] * x[j] for j in range(N)) for i in range(N)]
lam = sum(x[i] * Gx[i] for i in range(N))
lmax_est = max(sum(abs(v) for v in row) for row in Gf)    # cota de Gershgorin (não rigorosa) p/ lambda_max
print(f"[lambda_min estimado] {lam:.6e}   (Gershgorin lambda_max <= {lmax_est:.3f})")
OUT['lambda_min_est'] = lam

# ---------- cotas superiores rigorosas ----------
def Q_iv(n, d):
    den = iv.mpf(10) ** d
    c = [iv.mpf(nk) / den for nk in n]
    Gc = []
    for i in range(N):
        s = iv.mpf(0); Gi = G[i]
        for j in range(N):
            s = s + Gi[j] * c[j]
        Gc.append(s)
    bc = iv.mpf(0); cGc = iv.mpf(0)
    for i in range(N):
        bc = bc + b[i] * c[i]; cGc = cGc + c[i] * Gc[i]
    Q = 1 - 2 * bc + cGc
    r = [Gc[i] - b[i] for i in range(N)]
    return Q, r

def nearest(d):
    return [int(mp.nint(v * 10 ** d)) for v in cs]

def babai(d):  # arredondamento de plano mais próximo (Babai) na grade 10^-d, com o fator L (não rigoroso)
    sc = mp.mpf(10) ** d
    n = [0] * N; e = [mp.mpf(0)] * N
    for i in range(N - 1, -1, -1):
        ti = cs[i] - mp.fsum(Lm[j][i] * e[j] for j in range(i + 1, N)) / Lm[i][i]
        n[i] = int(mp.nint(ti * sc)); e[i] = n[i] / sc - cs[i]
    return n

def save(n, d, tag, Qhi):
    fn = f"coef_{tag}.txt" if N == 256 else f"coef_N{N}_{tag}.txt"
    with open(fn, "w") as f:
        f.write(f"# D_256 <= Q(c) com c_k = n_k / 10^{d}, k = 1..{N}  (escolha: {tag})\n")
        f.write(f"# Q(c) <= {mp.nstr(Qhi, 30)}  (mpmath.iv, dps {DPS})\n# k n_k\n")
        for k, nk in enumerate(n, 1):
            f.write(f"{k} {nk}\n")
    return fn

OUT['upper'] = {}
for d, tag, fn_n in [(4, "d4", nearest), (4, "d4_babai", babai), (5, "d5", nearest), (6, "d6", nearest),
                     (8, "d8", nearest)]:
    t = time.time()
    n = fn_n(d)
    e = [mp.mpf(nk) / 10 ** d - cs[k] for k, nk in enumerate(n)]
    pred = mp.fsum(e[i] * mp.fdot(Gm[i], e) for i in range(N))
    Q, _ = Q_iv(n, d)
    mp.dps = DPS
    ok = hi(Q) <= ALVO
    margem = ALVO - hi(Q)
    save(n, d, tag, hi(Q))
    print(f"[sup {tag:9s}] Q(c) in [{mp.nstr(lo(Q), 22)}, {mp.nstr(hi(Q), 22)}]  larg {mp.nstr(width(Q), 3)}  "
          f"Q-D prev. {mp.nstr(pred, 4)}  margem a 0,00823372: {mp.nstr(margem, 6)}  {'OK' if ok else 'FALHA'}  "
          f"({time.time()-t:.1f}s)", flush=True)
    OUT['upper'][tag] = dict(d=d, Q_lo=mp.nstr(lo(Q), 30), Q_hi=mp.nstr(hi(Q), 30), margem=mp.nstr(margem, 8),
                             ok=bool(ok), Q_minus_D_prev=mp.nstr(pred, 4), max_abs_n=max(abs(v) for v in n))
    mp.dps = 50

# ---------- cota inferior rigorosa ----------
d = 30
n30 = nearest(d)
t = time.time()
Q30, r = Q_iv(n30, d)
rr = iv.mpf(0)
for ri in r:
    rr = rr + abs(ri) ** 2
mp.dps = DPS
print(f"[c30] Q(c30) in [{mp.nstr(lo(Q30), 45)}, {mp.nstr(hi(Q30), 45)}]  ||r||^2 <= {mp.nstr(hi(rr), 4)}  "
      f"({time.time()-t:.1f}s)", flush=True)
save(n30, d, "d30", hi(Q30))

METHOD = sys.argv[3] if len(sys.argv) > 3 else "rump"     # rump | ivchol | both

def iv_chol_ok(mu_str):
    """Cholesky intervalar de G - mu I.  Se todos os pivôs têm extremo inferior > 0, então pela isotonia de
    inclusão o Cholesky exato da matriz pontual (G - mu I) (que está no envelope) tem pivôs > 0: G - mu I > 0."""
    MU = iv.mpf(mu_str)
    L = [[] for _ in range(N)]
    minp = None; wtrace = []
    for j in range(N):
        Lj = L[j]
        s = G[j][j] - MU
        for k in range(j):
            s = s - Lj[k] ** 2
        if j % 16 == 0 or j == N - 1:
            wtrace.append((j + 1, mp.nstr(width(s), 2)))
        if not lo(s) > 0:
            print("   larguras do pivô (coluna, largura):", wtrace)
            return False, j + 1, None, None
        p = lo(s); minp = p if minp is None or p < minp else minp
        Ljj = iv.sqrt(s)
        for i in range(j + 1, N):
            Li = L[i]; tt = G[i][j]
            for k in range(j):
                tt = tt - Li[k] * Lj[k]
            Li.append(tt / Ljj)
        Lj.append(Ljj)
    print("   larguras do pivô (coluna, largura):", wtrace)
    wmax = max(width(v) for row in L for v in row)
    return True, N, minp, wmax

def rump_bound(mu_str, P=None):
    """Cota de Rump (resíduo de um Cholesky aproximado):  R inteiro/2^P qualquer (aqui ~ Cholesky de mid(G) - mu I),
    G - mu I = R R^T + E,  R R^T >= 0  =>  lambda_min(G) >= mu - ||E||_2 >= mu - ||E||_F.
    R R^T é calculado EXATAMENTE em inteiros; E e ||E||_F em mpmath.iv.  Devolve o extremo inferior de mu - ||E||_F."""
    P = P or int(DPS * 3.33) + 20
    old = mp.dps; mp.dps = DPS + 10
    MUm = mp.mpf(mu_str)
    R = [[mp.mpf(0)] * (i + 1) for i in range(N)]
    for j in range(N):
        s = Gm[j][j] - MUm - mp.fsum(R[j][k] ** 2 for k in range(j))
        if s <= 0:
            mp.dps = old; return None, None
        R[j][j] = mp.sqrt(s)
        for i in range(j + 1, N):
            R[i][j] = (Gm[i][j] - mp.fdot(R[i][:j], R[j][:j])) / R[j][j]
    M = [[int(mp.nint(v * mp.mpf(2) ** P)) for v in row] for row in R]
    mp.dps = old
    MU = iv.mpf(mu_str); two2P = iv.mpf(2) ** (2 * P)
    from operator import mul
    F2 = iv.mpf(0); Emax = mp.mpf(0)
    for i in range(N):
        Mi = M[i]
        for j in range(i + 1):
            S = sum(map(mul, Mi[:j + 1], M[j][:j + 1]))       # (R R^T)_{ij} * 2^{2P}, exato
            e = G[i][j] - iv.mpf(S) / two2P
            if i == j:
                e = e - MU
            a = abs(e); Emax = max(Emax, hi(a))
            F2 = F2 + (a ** 2 if i == j else 2 * a ** 2)
    normE = iv.sqrt(iv.mpf(hi(F2)))
    lam_lo = lo(MU - normE)
    return lam_lo, hi(normE)

mu_str = mp.nstr(mp.mpf(0.99 * lam), 3)
OUT['mu'] = mu_str
lam_cert = None
if METHOD in ("rump", "both"):
    t = time.time()
    lam_r, nE = rump_bound(mu_str)
    print(f"[Rump] mu = {mu_str}: ||E||_F <= {mp.nstr(nE, 3)}  =>  lambda_min(G) >= {mp.nstr(lam_r, 12)}  ({time.time()-t:.1f}s)",
          flush=True)
    OUT['rump'] = dict(normE=mp.nstr(nE, 4), lam_lo=mp.nstr(lam_r, 15), t=time.time() - t)
    if lam_r is not None and lam_r > 0:
        lam_cert = lam_r
if METHOD in ("ivchol", "both"):
    t = time.time()
    ok, jfail, minp, wmax = iv_chol_ok(mu_str)
    print(f"[Cholesky intervalar G - mu I, mu = {mu_str}, dps {DPS}] "
          f"{'sucesso' if ok else 'falhou (pivô com extremo inferior <= 0) na coluna %d' % jfail}"
          f"{'' if not ok else ', menor pivô (extr. inf.) %s, largura máx. de L %s' % (mp.nstr(minp, 4), mp.nstr(wmax, 3))}"
          f"  ({time.time()-t:.1f}s)", flush=True)
    OUT['ivchol'] = dict(ok=ok, col=jfail, t=time.time() - t)
    if ok:
        lam_c = lo(iv.mpf(mu_str))
        lam_cert = lam_c if lam_cert is None else max(lam_cert, lam_c)
if lam_cert is not None:
    LB = Q30 - iv.mpf(hi(rr)) / iv.mpf(lam_cert)
    lo_D, hi_D = lo(LB), hi(Q30)
    print(f"\nCERTIFICADO  D_{N} in [{mp.nstr(lo_D, 45)},\n             {'':{len(str(N))}}  {mp.nstr(hi_D, 45)}]")
    print(f"largura {mp.nstr(hi_D - lo_D, 4)};  ||r||^2/lambda <= {mp.nstr(hi(rr) / lam_cert, 3)};  "
          f"folga rigorosa a 0,00823372: {mp.nstr(ALVO - hi_D, 10)}")
    OUT['lam_cert'] = mp.nstr(lam_cert, 15)
    OUT['D_lo'] = mp.nstr(lo_D, 50); OUT['D_hi'] = mp.nstr(hi_D, 50); OUT['folga'] = mp.nstr(ALVO - hi_D, 12)
    OUT['rr_over_lam'] = mp.nstr(hi(rr) / lam_cert, 4)
OUT['t_total'] = time.time() - T0
print(f"tempo total {OUT['t_total']:.1f}s")
with open(f"cert_D{N}_result_{METHOD}_dps{DPS}.json", "w") as f:
    json.dump(OUT, f, indent=1, ensure_ascii=False)
