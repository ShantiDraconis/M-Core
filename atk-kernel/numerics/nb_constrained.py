"""
Família de Nyman–Beurling RESTRITA (a usada na outra sessão ATK, 13/10):
    f_q = rho_q - rho_1 / q ,  q = 2..N+1,   rho_k(t) = {1/(k t)}.
Como sum c_k theta_k = 0, cada f_q se anula em t > 1: f_q ∈ L^2(0,1).
    b_q = <chi, f_q> = log(q)/q
    G^f(q,s) = G(q,s) - G(q,1)/s - G(1,s)/q + G(1,1)/(q s)   (G = Gram de Vasyunin, nb_gram)
    D^f_N = 1 - b^T (G^f)^{-1} b  (Cholesky incremental, decimal de precisão arbitrária)
Como span{f_2..f_{N+1}} ⊂ span{rho_1..rho_{N+1}}:  D^f_N >= D_{N+1} (Báez-Duarte).
Uso: python3 nb_constrained.py NMAX PREC SAIDA.csv
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal, getcontext
import nb_gram as nb

nmax, prec, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
getcontext().prec = prec
K = nb.Constants()
cache = {}
G = lambda j, k: nb.gram_entry(j, k, K, cache)
G11 = G(1, 1)
def Gf(q, s):
    return G(q, s) - G(q, 1) / s - G(1, s) / q + G11 / (q * s)
t0 = time.time()
L, y, rows, acc = [], [], [], Decimal(0)
for n in range(1, nmax + 1):
    q = n + 1
    g = [Gf(q, j + 1) for j in range(1, n + 1)]
    row = []
    for j in range(n - 1):
        s = g[j]
        Lj = L[j]
        for i in range(j):
            s -= row[i] * Lj[i]
        row.append(s / Lj[j])
    d = g[n - 1]
    for i in range(n - 1):
        d -= row[i] * row[i]
    if d <= 0:
        raise ArithmeticError(f"pivô não positivo em N={n}: aumente a precisão")
    piv = d.sqrt()
    row.append(piv)
    L.append(row)
    s = Decimal(q).ln() / q
    for i in range(n - 1):
        s -= row[i] * y[i]
    yn = s / piv
    y.append(yn)
    acc += yn * yn
    D = 1 - acc
    rows.append((n, q, D, D * Decimal(n + 2).ln(), yn * yn, d))
with open(out, "w") as f:
    f.write("N,q_max,Df_N,Df_N_log_N_plus_2,decremento,schur_s\n")
    for r in rows:
        f.write(",".join(str(x) for x in r) + "\n")
print(f"OK N={nmax} prec={prec} tempo={time.time()-t0:.0f}s D1={rows[0][2]} D_N={rows[-1][2]}")
