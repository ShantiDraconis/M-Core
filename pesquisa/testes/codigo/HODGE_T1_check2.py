"""Checagem cruzada para m medio: enumera multiconjuntos de Hodge em Python e recalcula
orb_indec, orb_indec_qdec (definicao LITERAL de quase-decomponivel) e R_m; compara com o C."""
import sys, math
sys.path.insert(0, '.')
from HODGE_T1_check import units, is_hodge, dec_literal, qdec_literal, orbit_rep

def census(m):
    U = units(m)
    orbs = set()
    def rec(pref, lo, rem, k):
        if k == 1:
            if lo <= rem <= m - 1:
                a = tuple(pref + [rem])
                if is_hodge(a, m, U):
                    orbs.add(orbit_rep(a, m, U))
            return
        for x in range(lo, min(m - 1, rem // k) + 1):
            rec(pref + [x], x, rem - x, k - 1)
    rec([], 1, 3 * m, 6)
    ind = [o for o in orbs if not dec_literal(o, m, U)]
    q = [o for o in ind if qdec_literal(o, m, U)]
    return len(orbs), len(ind), len(q), len(ind) - len(q)

for m in map(int, sys.argv[1:]):
    print(m, 'orbits, indec, indec_qdec, R =', census(m), flush=True)
