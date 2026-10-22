"""Checks for RH T1/T2.
 (1) zeta (Euler-Maclaurin C) vs mpmath.zeta at the dumped samples.
 (2) Plancherel/t-side control: D_N(sigma), N<=5, from the t-side Gram  <rho_j,rho_k> = int_0^inf {x/j}{x/k} x^(-2s-1) dx,
     <chi,rho_k> = int_1^inf {x/k} x^(-2s-1) dx, |chi|^2 = 1/(2 sigma)   (x = 1/t), vs the Mellin-side C output.
 (3) Pick floor (sigma < beta0): D >= (1/2pi) w* K^-1 w, K_ij = 1/(2pi(z_i + conj z_j - 2 sigma)), w_i = B(z_i)/z_i,
     B(s) = (s-1)/(s-2sigma+1), z = rho0, conj rho0.
 (4) Structural floor for the spec'd F = zeta R (rational R): D_N^F >= min|R|^2 * sum_n min_{a,b} ||h - a/t - b||^2_{I_n},
     I_n = (1/(n+1),1/n], h = 1 + 2 Re[(A/rho0)(t^-rho0 - 1)], A = Res_{rho0} 1/R   (valid for sigma > beta0).
usage: python3 -I RH_T2_checks.py workdir
"""
import sys, math, os
sys.path[:0] = [p for p in os.environ.get("PYTHONPATH", "").split(":") if p]
import mpmath as mp

wd = sys.argv[1]
G1 = mp.mpf("14.134725141734693790")


def zeta_check(sig):
    fn = f"{wd}/s{sig}_zeta_samples.txt"
    mp.mp.dps = 25
    worst = 0; cnt = 0; worst_tau = None
    with open(fn) as fh:
        rows = [tuple(map(float, l.split())) for l in fh]
    # all low-tau samples + every high-tau sample up to a budget
    for tau, zr, zi in rows:
        z = mp.zeta(mp.mpc(sig, tau))
        rel = abs(mp.mpc(zr, zi) - z) / abs(z)
        cnt += 1
        if rel > worst:
            worst = rel; worst_tau = tau
    return cnt, float(worst), worst_tau


def tside_DN(sig, Nmax=5, X=20000):
    mp.mp.dps = 30
    s2 = 2 * mp.mpf(sig)
    def piece(j, k, m):  # int_m^{m+1} {x/j}{x/k} x^{-2s-1} dx, floors constant on (m, m+1)
        p, q = m // j, m // k
        a, b = mp.mpf(m), mp.mpf(m + 1)
        F2 = lambda x: x ** (2 - s2) / (2 - s2)
        F1 = lambda x: x ** (1 - s2) / (1 - s2)
        F0 = lambda x: x ** (-s2) / (-s2)
        return (F2(b) - F2(a)) / (j * k) - (mp.mpf(q) / j + mp.mpf(p) / k) * (F1(b) - F1(a)) + p * q * (F0(b) - F0(a))
    def mean_frac(j, k):  # mean of {x/j}{x/k} over a period
        L = j * k // math.gcd(j, k)
        tot = mp.mpf(0)
        for m in range(L):
            p, q = m // j, m // k
            # int_m^{m+1} (x/j - p)(x/k - q) dx
            f = lambda x: x ** 3 / (3 * j * k) - (mp.mpf(q) / j + mp.mpf(p) / k) * x ** 2 / 2 + p * q * x
            tot += f(mp.mpf(m + 1)) - f(mp.mpf(m))
        return tot / L
    def gram(j, k):
        v = 1 / (mp.mpf(j * k) * (2 - s2))  # x in (0,1): {x/j}{x/k} = x^2/(jk)
        for m in range(1, X):
            v += piece(j, k, m)
        return v + mean_frac(j, k) * mp.mpf(X) ** (-s2) / s2
    def bvec(k):
        v = mp.mpf(0)
        for m in range(1, X):
            p = m // k
            a, b = mp.mpf(m), mp.mpf(m + 1)
            v += ((b ** (1 - s2) - a ** (1 - s2)) / (1 - s2)) / k - p * ((b ** (-s2) - a ** (-s2)) / (-s2))
        mk = mp.mpf(1) / 2  # mean of {x/k}
        return v + mk * mp.mpf(X) ** (-s2) / s2
    G = mp.matrix(Nmax, Nmax); b = mp.matrix(Nmax, 1)
    for j in range(1, Nmax + 1):
        b[j - 1] = bvec(j)
        for k in range(j, Nmax + 1):
            G[j - 1, k - 1] = G[k - 1, j - 1] = gram(j, k)
    out = []
    for N in range(1, Nmax + 1):
        GN = G[:N, :N]; bN = b[:N, :]
        x = mp.lu_solve(GN, bN)
        out.append(1 / s2 - (bN.T * x)[0])
    return out


def pick_floor(sig, beta0):
    mp.mp.dps = 30
    r0 = mp.mpc(beta0, G1)
    zs = [r0, mp.conj(r0)]
    B = lambda s: (s - 1) / (s - 2 * sig + 1)
    w = mp.matrix([B(z) / z for z in zs])
    K = mp.matrix(2, 2)
    for i in range(2):
        for j in range(2):
            K[i, j] = 1 / (2 * mp.pi * (zs[i] + mp.conj(zs[j]) - 2 * sig))
    x = mp.lu_solve(K, w)
    val = sum(mp.conj(w[i]) * x[i] for i in range(2))
    return float(mp.re(val) / (2 * mp.pi))


def structural_floor(sig, beta0, nmax=3000):
    r1 = complex(0.5, float(G1)); r0 = complex(beta0, float(G1))
    A = (r0 - r1) * (r0 - r1.conjugate()) / (r0 - r0.conjugate())
    c = A / r0
    h = lambda t: 1 + 2 * (c * (t ** (-r0) - 1)).real
    # Gauss-Legendre 24 nodes
    xs, ws = [], []
    nodes = mp.gauss_legendre if hasattr(mp, "gauss_legendre") else None
    import mpmath.calculus.quadrature as qd
    gl = qd.GaussLegendre(mp.mp)
    pts = gl.calc_nodes(5, 30)  # degree 5 -> 3*2^4 nodes on [-1,1]
    xs = [float(p[0]) for p in pts]; ws = [float(p[1]) for p in pts]
    tot = 0.0
    for n in range(1, nmax + 1):
        a, b = 1.0 / (n + 1), 1.0 / n
        mid, half = (a + b) / 2, (b - a) / 2
        S = [[0.0] * 2 for _ in range(2)]; y = [0.0, 0.0]; hh = 0.0
        for x, w in zip(xs, ws):
            t = mid + half * x; wt = w * half * t ** (2 * sig - 1)
            f = [1 / t, 1.0]; hv = h(t)
            for i in range(2):
                y[i] += wt * f[i] * hv
                for j in range(2):
                    S[i][j] += wt * f[i] * f[j]
            hh += wt * hv * hv
        det = S[0][0] * S[1][1] - S[0][1] * S[1][0]
        p0 = (S[1][1] * y[0] - S[0][1] * y[1]) / det; p1 = (-S[1][0] * y[0] + S[0][0] * y[1]) / det
        tot += max(hh - (p0 * y[0] + p1 * y[1]), 0.0)
    # min |R| on the line
    R = lambda tau: abs((complex(sig, tau) - r0) * (complex(sig, tau) - r0.conjugate()) / ((complex(sig, tau) - r1) * (complex(sig, tau) - r1.conjugate())))
    mR = min(R(i * 0.001) for i in range(0, 200000))
    return tot, mR, mR * mR * tot


if __name__ == "__main__":
    what = sys.argv[2] if len(sys.argv) > 2 else "all"
    if what in ("all", "zeta"):
        for sig in ("0.7", "0.9"):
            print("zeta check sigma", sig, "samples, max rel err, at tau:", zeta_check(float(sig)), flush=True)
    if what in ("all", "pick"):
        for sig, b0 in ((0.7, 0.75), (0.6, 0.65), (0.6, 0.75)):
            print(f"Pick floor sigma={sig} beta0={b0}: D >= {pick_floor(sig, b0):.4e}", flush=True)
    if what in ("all", "struct"):
        for sig, b0 in ((0.9, 0.75), (0.9, 0.65), (0.8, 0.75), (0.8, 0.65), (0.7, 0.65)):
            tot, mR, lb = structural_floor(sig, b0)
            print(f"structural floor sigma={sig} beta0={b0}: dist^2(h, closure) >= {tot:.4e}, min|R| = {mR:.4f}, D_N^F >= {lb:.4e} for ALL N", flush=True)
    if what in ("all", "tside"):
        for sig in (0.7, 0.9):
            vals = tside_DN(sig)
            print(f"t-side D_N sigma={sig}:", " ".join(f"{float(v):.10e}" for v in vals), flush=True)
