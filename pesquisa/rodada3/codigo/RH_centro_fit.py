#!/usr/bin/env python3
"""RH_centro_fit.py — "centro" e "tolerância" de D_∞ a partir de D_N (N ≤ 8000).

Uso: python3 RH_centro_fit.py dn_dd_8000.tsv [dn_baixa_precisao.tsv rótulo ...]

Saídas (stdout): ajustes com D_∞ livre por modelo e janela; teste nulo D_∞ = 0; erro padrão ingênuo e
corrigido por autocorrelação; sensibilidade ao número de dígitos de D_N; cauda (derivada e integral);
N necessário para cada tolerância; piso de um zero fora da linha.  Tudo em double (suficiente: os D_N
entram com ≥ 12 dígitos e as tolerâncias de interesse são ≥ 1e-6 relativas).
"""
import math, sys

GAMMA = 0.57721566490153286061
C0 = 2 + GAMMA - math.log(4 * math.pi)


def load(path):
    D = {}
    for line in open(path):
        p = line.split('\t')
        if not p[0].isdigit():
            continue
        D[int(p[0])] = float(p[1])
    return D


def sample(D, nmin, nmax, K=300):
    pts = sorted({int(round(nmin * (nmax / nmin) ** (i / (K - 1)))) for i in range(K)})
    return [(n, D[n]) for n in pts if n in D]


def solve(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def inv(A):
    n = len(A)
    cols = [solve(A, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def linfit(X, y):
    p = len(X[0])
    XtX = [[sum(r[i] * r[j] for r in X) for j in range(p)] for i in range(p)]
    Xty = [sum(r[i] * yy for r, yy in zip(X, y)) for i in range(p)]
    beta = solve(XtX, Xty)
    res = [yy - sum(bi * xi for bi, xi in zip(beta, r)) for r, yy in zip(X, y)]
    sse = sum(e * e for e in res)
    return beta, res, sse, inv(XtX)


def corr_len(res, Ls):
    """comprimento de correlação dos resíduos em log N (lag em que a ACF cai abaixo de 1/e)."""
    n = len(res)
    m = sum(res) / n
    v = sum((e - m) ** 2 for e in res) / n
    if v == 0:
        return 0.0
    dL = (Ls[-1] - Ls[0]) / (n - 1)
    for lag in range(1, n // 2):
        c = sum((res[i] - m) * (res[i + lag] - m) for i in range(n - lag)) / (n * v)
        if c < math.exp(-1):
            return lag * dL
    return (n // 2) * dL


def se_report(beta0_var, sse, n, p, res, Ls):
    s2 = sse / (n - p)
    se = math.sqrt(s2 * beta0_var)
    lc = corr_len(res, Ls)
    span = Ls[-1] - Ls[0]
    neff = max(p + 1.0, min(n, span / lc if lc > 0 else n))
    infl = math.sqrt(n / neff)
    return se, se * infl, neff


def grid_a(pts, build, a_lo=-4.0, a_hi=20.0, step=0.01):
    best = None
    a = a_lo
    while a <= a_hi:
        try:
            X, y = build(pts, a)
            beta, res, sse, Vi = linfit(X, y)
            if best is None or sse < best[0]:
                best = (sse, a, beta, res, Vi)
        except ZeroDivisionError:
            pass
        a += step
    # refino
    sse, a0, *_ = best
    a = a0 - step
    while a <= a0 + step:
        X, y = build(pts, a)
        beta, res, sse2, Vi = linfit(X, y)
        if sse2 < best[0]:
            best = (sse2, a, beta, res, Vi)
        a += step / 50
    return best


def fit_all(pts):
    Ls = [math.log(n) for n, _ in pts]
    ys = [d for _, d in pts]
    n = len(pts)
    out = {}
    # A: D = D∞ + A/(L+a)
    sse, a, beta, res, Vi = grid_a(pts, lambda P, a: ([[1.0, 1 / (math.log(m) + a)] for m, _ in P], [d for _, d in P]))
    se, sei, neff = se_report(Vi[0][0], sse, n, 3, res, Ls)
    out['A'] = dict(Dinf=beta[0], se=se, sei=sei, neff=neff, rms=math.sqrt(sse / n), par=f"A/C0={beta[1]/C0:.3f} a={a:.2f}")
    # B: D = D∞ + A/L + B/L²
    X = [[1.0, 1 / L, 1 / L ** 2] for L in Ls]
    beta, res, sse, Vi = linfit(X, ys)
    se, sei, neff = se_report(Vi[0][0], sse, n, 3, res, Ls)
    out['B'] = dict(Dinf=beta[0], se=se, sei=sei, neff=neff, rms=math.sqrt(sse / n), par=f"A/C0={beta[1]/C0:.3f} B={beta[2]:.4f}")
    # C: D = D∞ + C0/(L+a), C0 fixo
    sse, a, beta, res, Vi = grid_a(pts, lambda P, a: ([[1.0] for m, _ in P], [d - C0 / (math.log(m) + a) for m, d in P]))
    se, sei, neff = se_report(Vi[0][0], sse, n, 2, res, Ls)
    out['C'] = dict(Dinf=beta[0], se=se, sei=sei, neff=neff, rms=math.sqrt(sse / n), par=f"a={a:.2f}")
    # 0: nulo D∞ = 0, D = A/(L+a)
    sse0, a0, beta0, res0, _ = grid_a(pts, lambda P, a: ([[1 / (math.log(m) + a)] for m, _ in P], [d for _, d in P]))
    out['0'] = dict(Dinf=0.0, rms=math.sqrt(sse0 / n), par=f"A/C0={beta0[0]/C0:.3f} a={a0:.2f}")
    return out


def main():
    D = load(sys.argv[1])
    Nmax_all = max(D)
    D8 = D[Nmax_all]
    print(f"C0 = 2 + γ − log 4π = {C0:.10f};  D_{Nmax_all} = {D8:.12e}")
    print("\n## 1. Intervalo rigoroso [0, D_N]: centro D_N/2, tolerância ±D_N/2 (= ±100% do centro)")
    for N in (1, 2, 10, 100, 256, 1000, 2000, 4000, 8000):
        if N in D:
            print(f"N={N:5d}  D_N={D[N]:.10f}  centro={D[N]/2:.10f}  tol=±{D[N]/2:.10f}")

    print("\n## 2. Ajustes com D∞ livre (amostra log-uniforme de 300 pontos)")
    print("modelo | janela | D∞ | D∞ / D_8000 (%) | EP ingênuo | EP corrigido (n_eff) | rms rel | parâmetros")
    rows = []
    wins = [(50, 8000), (100, 8000), (200, 8000), (400, 8000), (800, 8000), (1600, 8000),
            (100, 1000), (100, 2000), (100, 4000)]
    for (a, b) in wins:
        pts = sample(D, a, min(b, Nmax_all))
        f = fit_all(pts)
        rms_ref = None
        for mname in ('A', 'B', 'C', '0'):
            r = f[mname]
            meanD = sum(d for _, d in pts) / len(pts)
            if mname == '0':
                print(f"{mname} | [{a},{b}] | 0 (forçado) | — | — | — | {r['rms']/meanD:.2e} | {r['par']}")
            else:
                rows.append((mname, a, b, r['Dinf'], r['sei']))
                print(f"{mname} | [{a},{b}] | {r['Dinf']:+.3e} | {100*r['Dinf']/D8:+.1f}% | {r['se']:.1e} | {r['sei']:.1e} ({r['neff']:.1f}) | {r['rms']/meanD:.2e} | {r['par']}")
    full = [r for r in rows if r[2] == 8000]
    vals = sorted(r[3] for r in full)
    med = vals[len(vals) // 2]
    print(f"\nResumo (janelas até 8000, modelos A/B/C): mediana D∞ = {med:+.3e} ({100*med/D8:+.1f}% de D_8000); "
          f"faixa [{vals[0]:+.3e}, {vals[-1]:+.3e}] = [{100*vals[0]/D8:+.1f}%, {100*vals[-1]/D8:+.1f}%]")
    print("Convergência do centro com Nmax (modelo C, janela [100, Nmax]):")
    for b in (500, 1000, 2000, 3000, 4000, 6000, 8000):
        f = fit_all(sample(D, 100, b))
        print(f"  Nmax={b:5d}  D∞(C)={f['C']['Dinf']:+.3e}  ±{f['C']['sei']:.1e}  D∞(A)={f['A']['Dinf']:+.3e} ±{f['A']['sei']:.1e}  D∞(B)={f['B']['Dinf']:+.3e} ±{f['B']['sei']:.1e}")

    print("\n## 3. Precisão de D_N vs centro: arredonda D_N a k algarismos significativos e reajusta (janela [100, 8000])")
    base = fit_all(sample(D, 100, 8000))
    for k in (2, 3, 4, 5, 6, 8, 12):
        Dk = {n: float(f"{d:.{k-1}e}") for n, d in D.items()}
        f = fit_all(sample(Dk, 100, 8000))
        print(f"k={k:2d}  D∞(A)={f['A']['Dinf']:+.4e} (Δ={f['A']['Dinf']-base['A']['Dinf']:+.1e})  "
              f"D∞(B)={f['B']['Dinf']:+.4e} (Δ={f['B']['Dinf']-base['B']['Dinf']:+.1e})  D∞(C)={f['C']['Dinf']:+.4e} (Δ={f['C']['Dinf']-base['C']['Dinf']:+.1e})")
    for path, lab in zip(sys.argv[2::2], sys.argv[3::2]):
        Dl = load(path)
        top = max(Dl)
        common = [n for n in D if n in Dl]
        worst = max(abs(Dl[n] - D[n]) / D[n] for n in common)
        print(f"\n[{lab}] N até {top}; desvio relativo máximo de D_N contra dd: {100*worst:.2e}%")
        for N in (10, 100, 256, 1000, 2000, 4000, 8000):
            if N in Dl:
                print(f"   N={N:5d}  D_N={Dl[N]:.10e}  desvio={100*(Dl[N]-D[N])/D[N]:+.3e}%")
        if top >= 1000:
            f = fit_all(sample(Dl, 100, top))
            g = fit_all(sample(D, 100, top))
            for mname in 'ABC':
                print(f"   centro {mname}: {lab} {f[mname]['Dinf']:+.4e}  vs dd {g[mname]['Dinf']:+.4e}  (Δ = {f[mname]['Dinf']-g[mname]['Dinf']:+.1e})")

    print("\n## 4. Cauda: derivada (ganho por passo) e integral (soma dos ganhos)")
    print("bloco | média g_N·N·log²N / C0 (previsto 1 se D_N ~ C0/log N) | Σ_bloco g = D_ini − D_fim | previsto C0(1/logN1 − 1/logN2)")
    b = 64
    while 2 * b <= 8000:
        e = min(2 * b, 8000)
        gs = [(D[n] - D[n + 1]) * n * math.log(n) ** 2 / C0 for n in range(b, e) if n + 1 in D]
        print(f"[{b},{e}) | {sum(gs)/len(gs):.3f} | {D[b]-D[e]:.6e} | {C0*(1/math.log(b)-1/math.log(e)):.6e}")
        b *= 2
    print("Integral da tolerância em escala log: Σ_{n<N} D_n/n  vs  C0·log log N + const")
    for N in (100, 1000, 8000):
        s = sum(D[n] / n for n in range(1, N))
        print(f"  N={N:5d}  Σ D_n/n = {s:.6f}   C0·log log N = {C0*math.log(math.log(N)):.6f}")
    s_eta = sum((D[n] - D[n + 1]) / D[n] for n in range(1, 8000))
    print(f"Σ_{{n<8000}} η_n = {s_eta:.4f};  log(D_0/D_8000) = {math.log(1/D[8000]):.4f} (D_0 = 1);  log log 8000 = {math.log(math.log(8000)):.4f}")

    print("\n## 5. N necessário para cada tolerância (sob RH, D_N ≈ C0/(log N + a), a do ajuste C)")
    a = float(base['C']['par'].split('=')[1])
    for tau in (5e-3, 2.5e-3, 1e-3, 1e-4, 1e-6, 1e-25):
        L = C0 / tau - a
        print(f"  tol={tau:.0e}  log N ≈ {L:.4g}  N ≈ 10^{L/math.log(10):.4g}   dN/dτ = −N·C0/τ²")

    print("\n## 6. Piso de um zero fora da linha (kernel: piso_DN, m(ρ) = 1/(|ρ|(1/√(2σ−1) + 1/(1−σ))))")
    best = min(((1 / math.sqrt(2 * s - 1) + 1 / (1 - s)), s) for s in [0.5 + i * 1e-5 for i in range(1, 50000)])
    T = 3.0001753328e12
    print(f"  min_σ f(σ) = {best[0]:.6f} em σ = {best[1]:.5f};  com |ρ| ≥ {T:.4e} (Platt–Trudgian 2021): m(ρ)² ≤ {1/(T*best[0])**2:.3e}")
    f78 = 1 / math.sqrt(2 * 0.875 - 1) + 1 / (1 - 0.875)
    print(f"  (com σ ≤ 7/8, quasi-RH não revisada, o máximo continua em σ = {best[1]:.4f} < 7/8)")
    for s in (0.5 + 1e-6, 0.5001, 0.51, 0.6, best[1]):
        fs = 1 / math.sqrt(2 * s - 1) + 1 / (1 - s)
        print(f"  σ={s:.6f}: m² ≤ {1/(T*fs)**2:.3e}")


if __name__ == '__main__':
    main()
