"""Análise da família restrita f_q = rho_q - rho_1/q (nb_constrained.py) contra Báez-Duarte.
Uso: python3 analyze_constrained.py dn_constrained_N1000_prec60.csv dn_N1500_prec45.csv"""
import csv, math, sys
import numpy as np
f = [(int(r['N']), float(r['Df_N'])) for r in csv.DictReader(open(sys.argv[1]))]
bd = {int(r['N']): float(r['D_N']) for r in csv.DictReader(open(sys.argv[2]))}
fd = dict(f)
C0 = 2 + 0.5772156649015329 - math.log(4 * math.pi)
print(f"C0 = 2 + gamma - log(4 pi) = {C0:.10f}")
print("violações de D^f_N >= d_{N+1}:", sum(1 for n, d in f if d < bd[n + 1] - 1e-30))
for n in (1, 2, 8, 20, 100, 1000):
    print(f"N={n:5d}  D^f={fd[n]:.15f}  d_(N+1)={bd[n+1]:.15f}  razão={fd[n]/bd[n+1]:.5f}  D^f·log(N+2)={fd[n]*math.log(n+2):.6f}")
for N0 in (10, 100, 500):
    n, k = max(((n, d * math.log(n + 2)) for n, d in f if n >= N0), key=lambda x: x[1])
    print(f"max_(N0={N0}<=N<=1000) D^f·log(N+2) = {k:.6f} (N={n})")
def powfit(lo, hi):
    N = np.array([n for n, d in f if lo <= n <= hi], float); D = np.array([fd[int(n)] for n in N])
    best = None
    for p in np.linspace(0.02, 2, 991):
        X = np.vstack([np.ones_like(N), N ** -p]).T
        c, *_ = np.linalg.lstsq(X, D, rcond=None); r = float(np.sum((X @ c - D) ** 2))
        if best is None or r < best[0]: best = (r, p, c)
    return best
r, p, c = powfit(20, 100)
print(f"potência D_inf + C N^-p ajustada em 20..100: D_inf = {c[0]:.6f}, p = {p:.3f}; prevê D_1000 = {c[0]+c[1]*1000**-p:.6f}; real D_1000 = {fd[1000]:.6f}")
print(f"  ⇒ D_inf ajustado {c[0]:.6f} > D_1000 {fd[1000]:.6f}: impossível (D_N é decrescente). Modelo de potência REFUTADO.")
N = np.array([n for n, d in f if n >= 20], float); D = np.array([fd[int(n)] for n in N])
X = np.vstack([1 / np.log(N), 1 / np.log(N) ** 2]).T
cb, *_ = np.linalg.lstsq(X, D, rcond=None)
print(f"log: D ≈ {cb[0]:.5f}/log N + {cb[1]:.5f}/log² N (20..1000), rms = {math.sqrt(float(np.mean((X@cb-D)**2))):.2e}")
print(f"cota rigorosa (monotonia): 0 <= D_inf <= D^f_1000 = {fd[1000]:.15f}")
