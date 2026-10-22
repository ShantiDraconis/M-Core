# verifica_coef.py — verificação independente de uma cota superior a partir do arquivo de coeficientes.
# Lê coef_*.txt (linhas "k n_k", c_k = n_k/10^d), recalcula Q(c) = 1 - 2 b.c + c^T G c em mpmath.iv e
# compara com 0,00823372.  D_256 <= Q(c) vale para qualquer c (definição de D_N como mínimo).
# Uso: python3 verifica_coef.py coef_d4.txt [dps=60]
import sys, re
from mpmath import iv, mp
from gram_iv import build, lo, hi

fn = sys.argv[1]; dps = int(sys.argv[2]) if len(sys.argv) > 2 else 60
txt = open(fn).read()
d = int(re.search(r"n_k / 10\^(\d+)", txt).group(1))
n = [int(l.split()[1]) for l in txt.splitlines() if l and not l.startswith("#")]
N = len(n)
D = build(N, dps, verbose=False)
G, b = D['G'], D['b']
den = iv.mpf(10) ** d
c = [iv.mpf(v) / den for v in n]
# soma dupla direta (ordem diferente da do cert_D256.py)
Q = iv.mpf(1)
for i in range(N):
    Q = Q - 2 * b[i] * c[i] + G[i][i] * c[i] ** 2
    for j in range(i):
        Q = Q + 2 * G[i][j] * c[i] * c[j]
mp.dps = 30
alvo = mp.mpf(823372) / 10**8
print(f"{fn}: N = {N}, d = {d}, Q(c) in [{mp.nstr(lo(Q), 25)}, {mp.nstr(hi(Q), 25)}];  "
      f"0,00823372 - sup Q = {mp.nstr(alvo - hi(Q), 8)}  => D_{N} <= 0,00823372: {hi(Q) <= alvo}")
