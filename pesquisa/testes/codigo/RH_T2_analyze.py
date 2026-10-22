"""Slope fits for RH T1/T2 outputs. Least-squares slope of log y vs log N over a window (dense N: oscillation averaged).
usage: python3 -I RH_T2_analyze.py workdir"""
import sys, math, os
sys.path[:0] = [p for p in os.environ.get("PYTHONPATH", "").split(":") if p]
wd = sys.argv[1]


def fit(xs, ys):
    lx = [math.log(x) for x in xs]; ly = [math.log(y) for y in ys]
    n = len(lx); mx = sum(lx) / n; my = sum(ly) / n
    sxx = sum((a - mx) ** 2 for a in lx); sxy = sum((a - mx) * (b - my) for a, b in zip(lx, ly))
    sl = sxy / sxx; res = [b - (my + sl * (a - mx)) for a, b in zip(lx, ly)]
    se = math.sqrt(sum(r * r for r in res) / max(n - 2, 1) / sxx)
    return sl, se


def load_E(fn):
    E = {}
    for l in open(fn):
        if l.startswith("E N"):
            p = l.split(); N = int(p[2]); E[N] = [float(p[4]), float(p[6]), float(p[8])]
    return E


def load_D(fn):
    D = {}
    for l in open(fn):
        if l[0] == "#": continue
        p = l.split(); D[int(p[0])] = [float(x) for x in p[1:4]]
    return D


def pick_floor_D(sig, b0, K=30):
    import mpmath as mp
    mp.mp.dps = 30
    zs = [mp.mpc(b0, 2 * mp.pi * k / mp.log(2)) for k in range(-K, K + 1)]
    B = lambda s: (s - 1) / (s - 2 * sig + 1)
    w = mp.matrix([B(z) / z for z in zs]); n = len(zs)
    Km = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            Km[i, j] = 1 / (2 * mp.pi * (zs[i] + mp.conj(zs[j]) - 2 * sig))
    x = mp.lu_solve(Km, w)
    return float(mp.re(sum(mp.conj(w[i]) * x[i] for i in range(n))) / (2 * mp.pi))


labels = ["zeta", "b0=0.65", "b0=0.75"]
for mode in ("R", "D"):
    print(f"===== MODE {mode} ({'spec: F = zeta*R rational' if mode == 'R' else 'corrected: F = zeta*(1-2^(b0-s))'})")
    for sig in ("0.6", "0.7", "0.8", "0.9"):
        s = float(sig)
        E = load_E(f"{wd}/{mode}{sig}_summary.txt"); D = load_D(f"{wd}/{mode}{sig}_DN.txt")
        print(f"-- sigma={sig}")
        for v in range(3):
            b0 = [0.5, 0.65, 0.75][v]
            pred = -(2 * s - 1) if v == 0 else (-2 * (s - b0) if (mode == "D" and s > b0) else None)
            Ns = sorted(N for N in E if 100 <= N <= 800)
            sE, eE = fit(Ns, [E[N][v] for N in Ns])
            Nd = [N for N in range(60, 241)]
            sD, eD = fit(Nd, [D[N][v] for N in Nd])
            Nd2 = [N for N in range(120, 241)]
            sD2, eD2 = fit(Nd2, [D[N][v] for N in Nd2])
            ratio = D[200][v] / E[200][v] if 200 in E else float("nan")
            extra = ""
            if v > 0:
                dl = [D[N][v] - D[N][0] for N in Nd]
                if min(dl) > 0:
                    sd, ed = fit(Nd, dl); extra = f" | Delta=D^F-D^zeta slope[60,240] {sd:+.3f}+-{ed:.3f}"
            ps = f"{pred:+.2f}" if pred is not None else ("floor(0)" if (mode == "R" and v > 0) or s < b0 else "n/a")
            print(f"  {labels[v]:8s} pred {ps:>8s} | E slope[100,800] {sE:+.3f}+-{eE:.3f} E800={E[800][v]:.3e} | "
                  f"D slope[60,240] {sD:+.3f}+-{eD:.3f} [120,240] {sD2:+.3f} D240={D[240][v]:.3e} | D200/E200={ratio:.3f}{extra}")
        if mode == "D":
            for b0 in (0.65, 0.75):
                if s < b0:
                    print(f"  Pick floor (zeros b0+2pi i k/log2, |k|<=30) sigma={sig} b0={b0}: D >= {pick_floor_D(s, b0):.4e};"
                          f" observed D_240 = {D[240][1 if b0 == 0.65 else 2]:.4e}")
