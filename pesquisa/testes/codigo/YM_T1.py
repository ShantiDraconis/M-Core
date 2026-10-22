"""YM T1 — exact single-link Dobrushin thresholds for Wilson lattice gauge theory.

Action beta * sum_p (n - ReTr U_p).  Conditional law of one link x given the k = 2(d-1) staples:
    mu_h(x) ∝ exp(beta * sum_j ReTr(x h_j)) = exp(beta * ReTr(x M)),  M = sum_j h_j.
Dobrushin coefficient for a neighbouring link (6(d-1) of them, each in exactly one common plaquette):
    c(beta) = sup_{h, h' differing in one staple} TV(mu_h, mu_h');   alpha = 6(d-1) c(beta).
WLOG h_1 = 1, h_1' = g (conjugacy-class rep), others an arbitrary multiset R of k-1 elements.
beta_D = sup{beta : alpha(beta) < 1} (bisection; monotonicity checked on a grid).
"""
import math, cmath, itertools, sys, json, time

# ---------------- groups as lists of complex matrices ----------------
def mat_mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))

def retr(A):
    return sum(A[i][i] for i in range(len(A))).real

def key(A):
    return tuple(round(z.real, 9) + 0j + 1j * round(z.imag, 9) for row in A for z in row)

def closure(gens):
    n = len(gens[0])
    I = tuple(tuple(1 + 0j if i == j else 0j for j in range(n)) for i in range(n))
    elems = {key(I): I}
    frontier = [I]
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = mat_mul(a, g)
                kb = key(b)
                if kb not in elems:
                    elems[kb] = b
                    new.append(b)
        frontier = new
    return list(elems.values())

def cyclic(N):
    return [((cmath.exp(2j * math.pi * k / N),),) for k in range(N)]

c3, s3 = math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3)
S3 = closure([((c3 + 0j, -s3 + 0j), (s3 + 0j, c3 + 0j)), ((1 + 0j, 0j), (0j, -1 + 0j))])
# quaternion units as SU(2) matrices: i -> [[i,0],[0,-i]], j -> [[0,1],[-1,0]], k -> [[0,i],[i,0]]
QI = ((1j, 0j), (0j, -1j)); QJ = ((0j, 1 + 0j), (-1 + 0j, 0j)); QK = ((0j, 1j), (1j, 0j))
Q8 = closure([QI, QJ])
w = tuple(tuple(0.5 * (a + b + c + d) for a, b, c, d in zip(r0, r1, r2, r3)) for r0, r1, r2, r3 in
          zip(((1 + 0j, 0j), (0j, 1 + 0j)), QI, QJ, QK))  # (1+i+j+k)/2
T2 = closure([QI, QJ, w])
GROUPS = {"Z2": (cyclic(2), 1), "Z3": (cyclic(3), 1), "Z4": (cyclic(4), 1),
          "S3": (S3, 2), "Q8": (Q8, 2), "2T": (T2, 2)}

def conj_classes(G):
    reps, seen = [], set()
    inv = {key(g): g for g in G}
    def inverse(g):
        for h in G:
            P = mat_mul(g, h)
            if abs(retr(P) - len(g)) < 1e-9 and abs(P[0][0] - 1) < 1e-9:
                return h
    for g in G:
        if key(g) in seen:
            continue
        cls = set()
        for u in G:
            ui = inverse(u)
            cls.add(key(mat_mul(mat_mul(ui, g), u)))
        seen |= cls
        reps.append((g, len(cls)))
    return reps

def finite_profiles(G, kminus1):
    """Distinct functions x -> sum_{j} ReTr(x h_j) over multisets of size k-1 (as tuples over G)."""
    phi = {key(h): tuple(retr(mat_mul(x, h)) for x in G) for h in G}
    vecs = list(set(tuple(round(v, 12) for v in p) for p in phi.values()))
    S = {tuple(0.0 for _ in G)}
    for _ in range(kminus1):
        S = {tuple(round(a + b, 10) for a, b in zip(s, v)) for s in S for v in vecs}
    return list(S), phi

def tv_finite(beta, E1, E2):
    m1, m2 = max(E1), max(E2)
    w1 = [math.exp(beta * (e - m1)) for e in E1]
    w2 = [math.exp(beta * (e - m2)) for e in E2]
    z1, z2 = sum(w1), sum(w2)
    return 0.5 * sum(abs(a / z1 - b / z2) for a, b in zip(w1, w2))

def c_finite(beta, G, d, cache):
    k = 2 * (d - 1)
    if (id(G), d) not in cache:
        prof, phi = finite_profiles(G, k - 1)
        I = [g for g in G if abs(retr(g) - len(g)) < 1e-9][0]
        reps = [g for g, _ in conj_classes(G) if key(g) != key(I)]
        cache[(id(G), d)] = (prof, phi[key(I)], [phi[key(g)] for g in reps])
    prof, p1, pgs = cache[(id(G), d)]
    best, arg = 0.0, None
    for R in prof:
        E1 = [a + b for a, b in zip(R, p1)]
        for j, pg in enumerate(pgs):
            t = tv_finite(beta, E1, [a + b for a, b in zip(R, pg)])
            if t > best:
                best, arg = t, (R, j)
    return best, arg

# ---------------- SU(2): von Mises-Fisher on S^3, TV via the unit disk ----------------
def gauss_legendre(m):
    xs, ws = [], []
    for i in range(1, m + 1):
        x = math.cos(math.pi * (i - 0.25) / (m + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for kk in range(2, m + 1):
                p0, p1 = p1, ((2 * kk - 1) * x * p1 - (kk - 1) * p0) / kk
            dp = m * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws

GLX, GLW = gauss_legendre(48)

def Zvmf(kappa):  # E_unif(S^3)[exp(kappa x1)] = 2 I_1(kappa)/kappa
    t, s, j = 1.0, 0.0, 0
    q = (kappa / 2) ** 2
    while True:
        s += t
        j += 1
        t *= q / (j * (j + 1))
        if t < 1e-18 * s:
            return s + t

def P_half(beta, u1, u2, theta0):
    """(1/pi) * int_{disk, y1 > cos theta0} exp(2 beta (u1 y1 + u2 y2)) dy  (unnormalised)."""
    if theta0 <= 0:
        return 0.0
    c = 2 * beta * u2
    tot = 0.0
    h = theta0 / 2
    for x, wgt in zip(GLX, GLW):
        th = h * (x + 1)
        st = math.sin(th)
        inner = 2 * math.sinh(c * st) / c if abs(c) > 1e-12 else 2 * st
        tot += wgt * math.exp(2 * beta * u1 * math.cos(th)) * inner * st
    return tot * h / math.pi

def tv_su2(beta, s, m1, m2):
    u1, v1, u2 = m1 + s, m1 - s, m2
    ru, rv = math.hypot(u1, u2), math.hypot(v1, u2)
    Zu, Zv = Zvmf(2 * beta * ru), Zvmf(2 * beta * rv)
    t0 = (math.log(Zu) - math.log(Zv)) / (4 * beta * s)
    th0 = math.acos(max(-1.0, min(1.0, t0)))
    return P_half(beta, u1, u2, th0) / Zu - P_half(beta, v1, u2, th0) / Zv

def feasible(s, m1, m2, kminus1):
    tau = math.sqrt(max(0.0, 1 - s * s))
    return m1 * m1 + (m2 - tau) ** 2 <= kminus1 ** 2 + 1e-12

def r_norm(s, m1, m2):
    tau = math.sqrt(max(0.0, 1 - s * s))
    return math.sqrt(m1 * m1 + (m2 - tau) ** 2)

def c_su2(beta, d, fine=False):
    km1 = 2 * (d - 1) - 1
    best, arg = -1, None
    S = [0.25, 0.5, 0.75, 0.9, 1.0]
    M1 = [-km1 - 1 + i * (2 * km1 + 2) / 24 for i in range(25)]
    M2 = [i * (km1 + 1) / 12 for i in range(13)]
    for s in S:
        for m1 in M1:
            for m2 in M2:
                if feasible(s, m1, m2, km1):
                    t = tv_su2(beta, s, m1, m2)
                    if t > best:
                        best, arg = t, (s, m1, m2)
    # local refinement: projected coordinate pattern search
    x = list(arg)
    step = [0.1, 0.5, 0.5]
    while max(step) > 1e-7:
        improved = False
        for i in range(3):
            for sgn in (1, -1):
                y = list(x); y[i] += sgn * step[i]
                if not (0 < y[0] <= 1 and y[2] >= 0 and feasible(y[0], y[1], y[2], km1)):
                    # try projecting onto the feasible disk boundary
                    continue
                t = tv_su2(beta, *y)
                if t > best + 1e-15:
                    best, x, improved = t, y, True
        if not improved:
            step = [st / 2 for st in step]
    return best, tuple(x)

def bisect(cfun, d, lo, hi, tol=1e-10):
    a = lambda b: 6 * (d - 1) * cfun(b)
    assert a(lo) < 1 < a(hi), (a(lo), a(hi))
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if a(mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

if __name__ == "__main__":
    out = {}
    T0 = time.time()
    # --- control: Z2 closed form
    for d in (3, 4):
        cf = 0.5 * math.atanh(1 / (3 * (d - 1)))
        print("Z2 closed form d=%d: %.12f" % (d, cf))
    # --- group sanity
    for name, (G, n) in GROUPS.items():
        print(name, "order", len(G), "classes", len(conj_classes(G)), "dim", n)
    cache = {}
    for d in (3, 4):
        for name, (G, n) in GROUPS.items():
            cf = lambda b: c_finite(b, G, d, cache)[0]
            # grid monotonicity check
            grid = [0.005 * i for i in range(1, 61)]
            vals = [cf(b) for b in grid]
            mono = all(vals[i] <= vals[i + 1] + 1e-15 for i in range(len(vals) - 1))
            bD = bisect(cf, d, 1e-6, 0.3)
            c, (R, j) = c_finite(bD, G, d, cache)
            prof_n = len(cache[(id(G), d)][0])
            blgt = 1 / (32 * n * (d - 1))
            blgt_alpha = -math.log(1 - 1 / (8 * (d - 1))) / (4 * n)
            out[(name, d)] = dict(beta_D=bD, beta_lgt=blgt, beta_lgt_alpha=blgt_alpha, ratio=bD / blgt,
                                  monotone_grid=mono, n_profiles=prof_n)
            print("%-3s d=%d n=%d  beta_D=%.10f  lgt=%.6f  lgt(alpha-form)=%.6f  ratio=%.3f  mono=%s  #M=%d  t=%.0fs"
                  % (name, d, n, bD, blgt, blgt_alpha, bD / blgt, mono, prof_n, time.time() - T0), flush=True)
    # --- SU(2)
    # validation: normalisation and small-beta slope 8/(3 pi)
    for (b, s, m1, m2) in [(0.1, 0.7, 1.3, 2.0), (0.05, 1.0, -2.0, 0.5)]:
        u1, u2 = m1 + s, m2
        print("norm check", P_half(b, u1, u2, math.pi) / Zvmf(2 * b * math.hypot(u1, u2)))
    print("small-beta slope c(1e-4)/1e-4 =", c_su2(1e-4, 4)[0] / 1e-4, " 8/(3pi) =", 8 / (3 * math.pi))
    for d in (3, 4):
        cf = lambda b: c_su2(b, d)[0]
        bD = bisect(cf, d, 0.01, 0.2, tol=1e-8)
        c, arg = c_su2(bD, d)
        rr = r_norm(*arg)
        blgt = 1 / (32 * 2 * (d - 1))
        out[("SU2", d)] = dict(beta_D=bD, beta_lgt=blgt, ratio=bD / blgt, argmax=arg, r_at_max=rr)
        print("SU2 d=%d  beta_D=%.8f lgt=%.6f ratio=%.3f  argmax(s,m1,m2)=%s |r|=%.4f  t=%.0fs"
              % (d, bD, blgt, bD / blgt, tuple(round(v, 5) for v in arg), rr, time.time() - T0), flush=True)
    json.dump({"%s_d%d" % k: v for k, v in out.items()},
              open("/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/work/YM_T1.json", "w"), indent=1)
