"""Compara D_N entre dois arquivos (TSV do RH_Gram_dn ou CSV do kernel): erro absoluto e relativo máximos por faixa."""
import sys
from decimal import Decimal, getcontext
getcontext().prec = 60
def load(fn):
    d = {}
    with open(fn) as f:
        sep = ',' if fn.endswith('.csv') else '\t'
        next(f)
        for line in f:
            p = line.strip().split(sep)
            d[int(p[0])] = Decimal(p[1])
    return d
a, b = load(sys.argv[1]), load(sys.argv[2])
edges = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [10, 100, 300, 1000, 1500, 2000, 3000, 5000, 10000]
lo = 1
for hi in edges:
    ks = [n for n in range(lo, hi + 1) if n in a and n in b]
    if not ks: break
    ea = max(abs(a[n] - b[n]) for n in ks)
    er = max(abs(a[n] - b[n]) / abs(b[n]) for n in ks)
    print(f"N em [{lo},{hi}]: max|dif| = {float(ea):.2e}   max rel = {float(er):.2e}")
    lo = hi + 1
