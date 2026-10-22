"""Tarefa 4: análise de D_N (arquivo TSV do RH_Gram_dn em dd). Escreve data/RH_Gram_DN.tsv (N, D_N, g_N, eta_N)
e imprime as tabelas usadas em RH_Gram.md.  Uso: python3 RH_Gram_analyze.py dn_dd_NNNN.tsv out.tsv"""
import sys, math
from decimal import Decimal, getcontext
getcontext().prec = 50
import mpmath as mp

fn, out = sys.argv[1], sys.argv[2]
D, Y2 = {0: Decimal(1)}, {}
for line in open(fn):
    if line.startswith("N"): continue
    p = line.split("\t")
    n = int(p[0]); D[n] = Decimal(p[1]); Y2[n] = Decimal(p[3])
Nmax = max(D)
g = {n: Y2[n + 1] for n in range(0, Nmax)}            # g_N = D_N - D_{N+1} = y_{N+1}^2
eta = {n: g[n] / D[n] for n in range(0, Nmax)}
with open(out, "w") as f:
    f.write("N\tD_N\tg_N\teta_N\n")
    for n in range(1, Nmax):
        f.write(f"{n}\t{D[n]:.25e}\t{g[n]:.17e}\t{eta[n]:.17e}\n")
gam = mp.euler
C0 = float(2 + gam - mp.log(4 * mp.pi))
print(f"Nmax={Nmax}  C0 = 2+gamma-log(4pi) = {C0:.10f}")

def fac(n):
    r, p = [], 2
    while p * p <= n:
        e = 0
        while n % p == 0: n //= p; e += 1
        if e: r.append((p, e))
        p += 1
    if n > 1: r.append((n, 1))
    return r
def fstr(n): return "·".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in fac(n)) or "1"
def sqfree(n): return all(e == 1 for _, e in fac(n))

# (a) D_N log N
print("\n(a) N | D_N | D_N log N | /C0")
for n in [10, 100, 256, 500, 1000, 1500, 2000, 2310, 3000, 4000, 5000, 6000, 7000, 8000]:
    if n <= Nmax:
        x = float(D[n]) * math.log(n)
        print(f"{n} | {float(D[n]):.10e} | {x:.6f} | {x / C0:.4f}")
# média log-uniforme de D_N log N por blocos diádicos
print("\n(a) bloco [N,2N): min, média(peso 1/n), max de D_n log n")
N = 16
while 2 * N - 1 <= Nmax:
    xs = [(float(D[n]) * math.log(n), 1 / n) for n in range(N, 2 * N)]
    m = sum(a * w for a, w in xs) / sum(w for _, w in xs)
    print(f"[{N},{2*N}) | {min(a for a,_ in xs):.5f} | {m:.5f} | {max(a for a,_ in xs):.5f}")
    N *= 2

def wls(rows, lo, hi):
    """mínimos quadrados com peso 1/n (uniforme em log n). rows(n) -> (y, [x...])"""
    ns = range(lo, hi + 1)
    data = [rows(n) for n in ns]
    k = len(data[0][1])
    A = mp.matrix(k, k); b = mp.matrix(k, 1)
    for n, (y, x) in zip(ns, data):
        w = 1.0 / n
        for i in range(k):
            b[i] += w * x[i] * y
            for j in range(k): A[i, j] += w * x[i] * x[j]
    return [float(v) for v in mp.lu_solve(A, b)]

def resid(pred, lo, hi):
    r = [pred(n) / float(D[n]) - 1 for n in range(lo, hi + 1)]
    return math.sqrt(sum(x * x for x in r) / len(r)), max(abs(x) for x in r)

print("\n(a) ajustes (peso 1/n); resíduo relativo em D_N: rms, max")
for lo, hi in [(100, Nmax), (100, 1000), (1000, Nmax), (2000, Nmax)]:
    if hi > Nmax or lo >= hi: continue
    # F1: C0 fixo: C0/D - log N = a + b/log N
    a, bb = wls(lambda n: (C0 / float(D[n]) - math.log(n), [1.0, 1 / math.log(n)]), lo, hi)
    r1 = resid(lambda n: C0 / (math.log(n) + a + bb / math.log(n)), lo, hi)
    # F2: C livre: 1/D = alpha log N + beta
    al, be = wls(lambda n: (1 / float(D[n]), [math.log(n), 1.0]), lo, hi)
    r2 = resid(lambda n: 1 / (al * math.log(n) + be), lo, hi)
    # F3: C livre + 1/log: 1/D = alpha log N + beta + gam/log N
    al3, be3, ga3 = wls(lambda n: (1 / float(D[n]), [math.log(n), 1.0, 1 / math.log(n)]), lo, hi)
    r3 = resid(lambda n: 1 / (al3 * math.log(n) + be3 + ga3 / math.log(n)), lo, hi)
    print(f"[{lo},{hi}] F1(C0 fixo): a={a:.4f} b={bb:.4f} rms={r1[0]:.2e} max={r1[1]:.2e} | "
          f"F2: C={1/al:.5f} ({1/al/C0:.3f} C0) beta/alpha={be/al:.3f} rms={r2[0]:.2e} max={r2[1]:.2e} | "
          f"F3: C={1/al3:.5f} ({1/al3/C0:.3f} C0) rms={r3[0]:.2e}")
# Landreau–Richard: d_n ~ a/sqrt(log n), MQ sem peso em n=2..Nmax
num = sum(math.sqrt(float(D[n])) / math.sqrt(math.log(n)) for n in range(2, Nmax + 1))
den = sum(1 / math.log(n) for n in range(2, Nmax + 1))
aLR = num / den
print(f"\nLR-style a (d_n ~ a/sqrt(log n), n=2..{Nmax}) = {aLR:.5f}; a^2 = {aLR*aLR:.5f}; sqrt(C0) = {math.sqrt(C0):.5f}; LR(20000): 0.21377")

# (b) eficiência por passo e_N = eta_N N log N
e = {n: float(eta[n]) * n * math.log(n) for n in range(2, Nmax)}
def quant(v, qs):
    s = sorted(v); return [s[min(len(s) - 1, int(q * len(s)))] for q in qs]
print("\n(b) e_N = eta_N N log N: quantis [min,1%,10%,50%,90%,99%,max], média")
for lo, hi in [(10, 100), (100, 1000), (1000, 4000), (1000, Nmax - 1), (4000, Nmax - 1)]:
    if hi > Nmax - 1 or lo >= hi: continue
    v = [e[n] for n in range(lo, hi + 1)]
    qq = quant(v, [0, .01, .1, .5, .9, .99, .999999])
    print(f"[{lo},{hi}] " + " ".join(f"{x:.3g}" for x in qq) + f" | média {sum(v)/len(v):.3f}")
print("\n(b) por tipo de N+1 em [100, Nmax): média e mediana de e_N, n")
cats = {}
for n in range(100, Nmax):
    m = n + 1; f_ = fac(m)
    if len(f_) == 1 and f_[0][1] == 1: c = "primo"
    elif sqfree(m): c = f"livre de quadrados, ω={len(f_)}"
    else: c = "com quadrado"
    cats.setdefault(c, []).append(e[n])
for c in sorted(cats):
    v = sorted(cats[c]); print(f"{c}: n={len(v)} média={sum(v)/len(v):.3f} mediana={v[len(v)//2]:.3f} min={v[0]:.3g}")
print("\n(b) 12 menores e_N em [100,Nmax): N, e_N, N+1 fatorado")
for n in sorted(range(100, Nmax), key=lambda n: e[n])[:12]:
    print(f"{n} {e[n]:.3e} {fstr(n+1)}")
print("\n(b) 8 maiores e_N em [100,Nmax):")
for n in sorted(range(100, Nmax), key=lambda n: -e[n])[:8]:
    print(f"{n} {e[n]:.2f} {fstr(n+1)}")
print("\n(b) mínimo de e_N por bloco diádico; fração com e_N < 0.01 e < 0.1")
N = 64
while N < Nmax - 1:
    v = [(e[n], n) for n in range(N, min(2 * N, Nmax - 1))]
    mn = min(v)
    print(f"[{N},{min(2*N, Nmax-1)}) min={mn[0]:.2e} em N={mn[1]} (N+1={fstr(mn[1]+1)}) frac<0.01={sum(1 for x,_ in v if x<0.01)/len(v):.3f} frac<0.1={sum(1 for x,_ in v if x<0.1)/len(v):.3f}")
    N *= 2

# (c) lei polinomial eta_N >= c/(N+1)
print("\n(c) f_N = eta_N (N+1): min e média por bloco; expoente efetivo c_eff = log(D_N/D_M)/log(M/N); previsto log(log M/log N)/log(M/N)")
N = 16
while N < Nmax - 1:
    M = min(2 * N, Nmax - 1)
    v = [float(eta[n]) * (n + 1) for n in range(N, M)]
    ceff = math.log(float(D[N]) / float(D[M])) / math.log(M / N)
    pred = math.log(math.log(M) / math.log(N)) / math.log(M / N)
    print(f"[{N},{M}) min f={min(v):.2e} média f={sum(v)/len(v):.4f} | c_eff={ceff:.4f} previsto={pred:.4f}")
    N *= 2
S = 0.0
print("\n(c) soma de eta: sum_{n<N} eta_n, -log D_N, log log N, log N")
for n in range(0, Nmax):
    S += float(eta[n])
    if n + 1 in (10, 100, 1000, 2000, 5000, 8000):
        print(f"N={n+1}: sum eta={S:.4f}  -log D_N={-math.log(float(D[n+1])):.4f}  log log N={math.log(math.log(n+1)):.4f}  log N={math.log(n+1):.4f}")

# (d) razões diádicas
print("\n(d) N | D_2N/D_N | log N/log 2N | razão/previsto")
for base in [1, 125]:
    N = base
    while 2 * N <= Nmax:
        r = float(D[2 * N] / D[N]); p = math.log(N) / math.log(2 * N) if N > 1 else float('nan')
        print(f"{N} | {r:.5f} | {p:.5f} | {r/p if N>1 else float('nan'):.4f}")
        N *= 2
q_all = max(float(D[2 * N] / D[N]) for N in range(100, Nmax // 2 + 1))
q_min = min(float(D[2 * N] / D[N]) for N in range(100, Nmax // 2 + 1))
print(f"max_N∈[100,{Nmax//2}] D_2N/D_N = {q_all:.5f}; min = {q_min:.5f}")
print(f"\nD_255={D[255]:.20e}\nD_256={D[256]:.20e}\nmargem 0.00823372-D_256 = {Decimal('0.00823372')-D[256]:.6e}")
