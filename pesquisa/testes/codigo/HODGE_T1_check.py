"""Verificacao independente (Python puro) do censo HODGE_T1.c.

1. Para m pequeno (<= MMAX_BRUTE): enumera TODAS as 6-uplas ordenadas, testa Hodge com todas as
   unidades t, e recalcula dim Hdg^2_prim; recalcula dec/qdec pela definicao LITERAL de da Silva
   (a + b = c + d, b em M_m(1), c,d em M_m quaisquer, c,d != a), sem a reducao 3+3 usada no C.
2. Para cada representante residual (linhas REP) de qualquer m: re-verifica Hodge, ausencia de
   decomposicao e de quase-decomposicao pela definicao literal, e classifica:
   - tsplit: duas triplas de soma 0;
   - aoki5:  a = {x + j m/5 : j=0..4} U {-5x}  (progressao de passo m/5; tipo "standard" de Aoki).
Uso: python3 HODGE_T1_check.py arquivo_saida_do_C [MMAX_BRUTE]
"""
import sys, itertools, math
from collections import Counter

def units(m):
    return [t for t in range(1, m) if math.gcd(t, m) == 1]

def in_M(c, m, U):
    if len(c) % 2 or len(c) == 0:
        return False
    y2 = len(c)  # 2y
    for t in U:
        if 2 * sum((t * x) % m for x in c) != y2 * m:
            return False
    return all(x % m for x in c)

def is_hodge(a, m, U):
    return all(x % m for x in a) and all(sum((t * x) % m for x in a) == 3 * m for t in U)

def sub_multisets(ms, k):
    """todos os sub-multiconjuntos de tamanho k (como tuplas ordenadas), sem repeticao"""
    return set(tuple(sorted(c)) for c in itertools.combinations(sorted(ms), k))

def minus(ms, sub):
    c = Counter(ms); c.subtract(Counter(sub))
    if any(v < 0 for v in c.values()):
        return None
    return tuple(sorted(c.elements()))

def dec_literal(a, m, U):
    for k in (2, 4):
        for c in sub_multisets(a, k):
            d = minus(a, c)
            if in_M(c, m, U) and in_M(d, m, U):
                return True
    return False

def qdec_literal(a, m, U):
    A = tuple(sorted(a))
    for b in range(1, m):
        big = A + (b, m - b)
        for k in (2, 4, 6):
            for c in sub_multisets(big, k):
                d = minus(big, c)
                if c == A or d == A:
                    continue
                if in_M(c, m, U) and in_M(d, m, U):
                    return True
    return False

def tsplit(a, m):
    for I in itertools.combinations(range(6), 3):
        if sum(a[i] for i in I) % m == 0:
            return True
    return False

def aoki5(a, m):
    if m % 5:
        return False
    A = sorted(a)
    for x in range(1, m):
        cand = sorted([(x + j * (m // 5)) % m for j in range(5)] + [(-5 * x) % m])
        if 0 not in cand and cand == A:
            return True
    return False

def orbit_rep(a, m, U):
    return min(tuple(sorted((t * x) % m for x in a)) for t in U)

def brute(m):
    U = units(m)
    dim = 0
    reps = {}
    for a in itertools.product(range(1, m), repeat=6):
        if sum(a) % m:
            continue
        if is_hodge(a, m, U):
            dim += 1
            s = tuple(sorted(a))
            if s not in reps:
                reps[s] = None
    orbs = set(orbit_rep(s, m, U) for s in reps)
    nind = 0; nR = 0
    for o in orbs:
        if not dec_literal(o, m, U):
            nind += 1
            if not qdec_literal(o, m, U):
                nR += 1
    return dim, len(reps), len(orbs), nind, nR

def main():
    fn = sys.argv[1]
    mmax_brute = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    sums = {}
    reps = []
    for line in open(fn):
        if line.startswith('SUM'):
            kv = dict(x.split('=') for x in line.split()[1:])
            sums[int(kv['m'])] = kv
        elif line.startswith('REP'):
            parts = line.split()
            m = int(parts[1].split('=')[1])
            a = tuple(int(x) for x in parts[2].split('=')[1].strip('()').split(','))
            ts = int(parts[4].split('=')[1])
            reps.append((m, a, ts))
    print('== brute force (todas as 6-uplas ordenadas, definicoes literais) ==')
    for m in range(3, mmax_brute + 1):
        dim, nms, norb, nind, nR = brute(m)
        kv = sums[m]
        ok = (dim == int(kv['dimHdgPrim']) and nms == int(kv['multisets']) and norb == int(kv['orbits'])
              and nind == int(kv['orb_indec']) and nR == int(kv['R_orbits']))
        print(f'm={m}: dim={dim} multisets={nms} orbits={norb} indec_orbits={nind} R={nR}  C-agree={ok}')
    print('== re-verificacao dos representantes residuais ==')
    bad = 0
    from collections import defaultdict
    cls = defaultdict(lambda: [0, 0, 0, 0])
    for (m, a, ts) in reps:
        U = units(m)
        h = is_hodge(a, m, U)
        d = dec_literal(a, m, U)
        q = qdec_literal(a, m, U)
        t = tsplit(a, m)
        k5 = aoki5(a, m)
        if not h or d or q or t != bool(ts):
            bad += 1
            print('DIVERGENCIA', m, a, h, d, q, t, ts)
        c = cls[m]
        c[0] += 1; c[1] += t; c[2] += k5; c[3] += (not t and not k5)
    print('representantes com divergencia:', bad, 'de', len(reps))
    print('m  R_orbits  tsplit  aoki5  restantes(nem tsplit nem aoki5)')
    for m in sorted(cls):
        print(m, *cls[m])
    for (m, a, ts) in reps:
        if not tsplit(a, m) and not aoki5(a, m):
            print('LEFT', m, a)

if __name__ == '__main__':
    main()
