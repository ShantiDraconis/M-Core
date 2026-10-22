"""Classifica estruturalmente os representantes residuais (R_m) do censo."""
import sys, math, itertools
from collections import Counter, defaultdict
sys.path.insert(0, '.')
from HODGE_T1_check import tsplit, aoki5

def contains_prog(a, m, d):
    """contem progressao aditiva {x + j m/d : j<d} (coset de (m/d)Z/mZ)"""
    if m % d: return False
    A = Counter(a)
    for x in set(a):
        S = Counter((x + j * (m // d)) % m for j in range(d))
        if all(A[k] >= v for k, v in S.items()): return True
    return False

def contains_multcoset(a, m, d):
    """contem x*H, H subgrupo ciclico de ordem d de (Z/m)^*"""
    gens = [g for g in range(2, m) if math.gcd(g, m) == 1 and pow(g, d, m) == 1
            and all(pow(g, e, m) != 1 for e in range(1, d))]
    A = Counter(a)
    for g in gens:
        for x in set(a):
            S = Counter((x * pow(g, k, m)) % m for k in range(d))
            if all(A[k] >= v for k, v in S.items()): return True
    return False

rows = defaultdict(Counter)
for fn in sys.argv[1:]:
    for line in open(fn):
        if not line.startswith('REP'): continue
        p = line.split()
        m = int(p[1].split('=')[1]); a = tuple(int(x) for x in p[2].split('=')[1].strip('()').split(','))
        if tsplit(a, m): c = 'tsplit'
        elif aoki5(a, m): c = 'aoki5'
        elif contains_multcoset(a, m, 5): c = 'mult5'
        elif contains_prog(a, m, 5): c = 'prog5'
        elif contains_prog(a, m, 4): c = 'prog4'
        elif contains_multcoset(a, m, 4): c = 'mult4'
        elif contains_prog(a, m, 3): c = 'prog3'
        elif contains_multcoset(a, m, 3): c = 'mult3'
        else: c = 'outro'
        rows[m][c] += 1
        if c in ('mult5', 'outro', 'mult4', 'mult3'):
            print('  ', m, a, c)
cats = ['tsplit', 'aoki5', 'mult5', 'prog5', 'prog4', 'mult4', 'prog3', 'mult3', 'outro']
print('m', *cats)
for m in sorted(rows):
    print(m, *[rows[m][c] for c in cats])
