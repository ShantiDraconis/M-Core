"""Independent control for YM_T3.c at L=2: brute-force link basis (2^8 configs), gauge orbits, mpmath eigsy.
Prints the distinct eigenvalues of the normalised T' = T * exp(-3 beta L^2) in the gauge-invariant sector,
plus the flux label (F_x, F_y eigenvalues) of each eigenvector."""
import sys, itertools, math
import mpmath as mp
mp.mp.dps = 30
L = 2
beta = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf("0.3")
links = [("x", x, y) for y in range(L) for x in range(L)] + [("y", x, y) for y in range(L) for x in range(L)]
idx = {l: i for i, l in enumerate(links)}
NLk = len(links)
plaqs = [[idx[("x", x, y)], idx[("y", (x + 1) % L, y)], idx[("x", x, (y + 1) % L)], idx[("y", x, y)]]
         for y in range(L) for x in range(L)]
def site_links(x, y):  # links touching site (x,y)
    return [idx[("x", x, y)], idx[("x", (x - 1) % L, y)], idx[("y", x, y)], idx[("y", x, (y - 1) % L)]]
configs = list(range(1 << NLk))
spin = lambda c, i: -1 if (c >> i) & 1 else 1
gauge_masks = []
for g in range(1 << (L * L)):
    m = 0
    for s in range(L * L):
        if (g >> s) & 1:
            for i in site_links(s % L, s // L):
                m ^= 1 << i
    gauge_masks.append(m)
orbit_of, orbits = {}, []
for c in configs:
    if c in orbit_of:
        continue
    O = sorted(set(c ^ m for m in gauge_masks))
    for o in O:
        orbit_of[o] = len(orbits)
    orbits.append(O)
print("orbits", len(orbits), "sizes", set(len(O) for O in orbits))
def D(c):
    return mp.e ** (beta * sum(spin(c, p[0]) * spin(c, p[1]) * spin(c, p[2]) * spin(c, p[3]) for p in plaqs))
def K(c, c2):
    d = bin(c ^ c2).count("1")
    return mp.e ** (beta * (NLk - d)) * mp.e ** (-beta * d)
n = len(orbits)
T = mp.matrix(n, n)
Dv = {c: D(c) for c in configs}
for a, Oa in enumerate(orbits):
    for b, Ob in enumerate(orbits):
        s = mp.mpf(0)
        for c in Oa:
            for c2 in Ob:
                s += mp.sqrt(Dv[c]) * K(c, c2) * mp.sqrt(Dv[c2])
        T[a, b] = s / mp.sqrt(len(Oa) * len(Ob)) * mp.e ** (-3 * beta * L * L)
E, Q = mp.eigsy(T)
# flux operator F_x: flip x-links at column x0=0 for all y (changes W_x only)
Fx = 0
for y in range(L):
    Fx ^= 1 << idx[("x", 0, y)]
Fy = 0
for x in range(L):
    Fy ^= 1 << idx[("y", x, 0)]
perm_x = [orbit_of[orbits[a][0] ^ Fx] for a in range(n)]
perm_y = [orbit_of[orbits[a][0] ^ Fy] for a in range(n)]
res = []
for k in range(n):
    v = [Q[a, k] for a in range(n)]
    ex = sum(v[a] * v[perm_x[a]] for a in range(n))
    ey = sum(v[a] * v[perm_y[a]] for a in range(n))
    res.append((E[k], int(mp.nint(ex)), int(mp.nint(ey))))
res.sort(key=lambda r: -r[0])
for e, ex, ey in res:
    print(mp.nstr(e, 15), ex, ey)
