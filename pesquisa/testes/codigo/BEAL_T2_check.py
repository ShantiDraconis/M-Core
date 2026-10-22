# BEAL T2: implementacao independente (inteiros de Python) para conferir a lista de acertos do C numa caixa pequena.
import sys
from math import gcd

def iroot(n, k):
    lo, hi = 1, 1
    while hi ** k <= n:
        hi *= 2
    while lo < hi - 1:
        m = (lo + hi) // 2
        if m ** k <= n: lo = m
        else: hi = m
    return lo

QS = [q for q in range(2, 128) if all(q % d for d in range(2, q))]
p, N = int(sys.argv[1]), int(sys.argv[2])
hits = []
for x in range(2, N + 1):
    for y in range(-x + 1, x):
        if y == 0 or gcd(x, abs(y)) != 1:
            continue
        num = x ** p + y ** p
        assert num % (x + y) == 0
        F = num // (x + y)
        G, e = F, 0
        while G % p == 0:
            G //= p; e += 1
        for q in QS:
            if 2 ** q > G:
                break
            z = iroot(G, q)
            if z >= 2 and z ** q == G:
                hits.append((x, y, e, q, z))
for h in sorted(hits):
    print("HIT p=%d x=%d y=%d e=%d q=%d z=%d" % ((p,) + h))
print("total", len(hits))
