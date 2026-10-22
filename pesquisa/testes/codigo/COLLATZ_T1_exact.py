"""Control A for COLLATZ T1: exact rational law of Syrac(Z/3^n) by forward DP on the definition
X = sum_{k=1}^n 3^(k-1) 2^-(a1+...+ak) mod 3^n, a_i ~ Geom(1/2), using a_i mod L_n (L_n = ord of 2 mod 3^n),
P(a = r mod L) = 2^(L-r)/(2^L-1), r = 1..L. Integer numerators over (2^L-1)^n. Compares with the C dump.
Usage: python3 -I COLLATZ_T1_exact.py NMAX dumpdir
"""
import sys
from fractions import Fraction


def exact(n):
    mod = 3 ** n
    L = 2 * 3 ** (n - 1)
    D = 2 ** L - 1
    inv2 = pow(2, -1, mod)
    ipow = [pow(inv2, s, mod) for s in range(L)]
    w = [2 ** (L - r) for r in range(1, L + 1)]
    states = {(0, 0): 1}
    for k in range(1, n + 1):
        c = 3 ** (k - 1)
        new = {}
        for (S, X), wt in states.items():
            for r in range(1, L + 1):
                S2 = (S + r) % L
                key = (S2, (X + c * ipow[S2]) % mod)
                new[key] = new.get(key, 0) + wt * w[r - 1]
        states = new
    law = {}
    for (S, X), wt in states.items():
        law[X] = law.get(X, 0) + wt
    den = D ** n
    return {x: Fraction(v, den) for x, v in law.items()}


def main():
    nmax = int(sys.argv[1])
    dumpdir = sys.argv[2]
    for n in range(1, nmax + 1):
        law = exact(n)
        tot = sum(law.values())
        cmin = min(law.values())
        units = [x for x in range(3 ** n) if x % 3]
        missing = [x for x in units if x not in law]
        alg = {}
        with open(f"{dumpdir}/syrac_P{n}.txt") as fh:
            for line in fh:
                a, b = line.split()
                alg[int(a)] = float(b)
        maxrel = max(abs(alg[x] - float(law[x])) / float(law[x]) for x in law)
        cstr = str(cmin) if n <= 3 else f"{float(cmin):.17g} (den. (2^{2*3**(n-1)}-1)^{n})"
        print(f"n={n}: sum=1? {tot == 1}; support = all units? {not missing and len(law) == len(units)}; "
              f"c_n = {cstr}; max rel |alg-exact| = {maxrel:.2e}")
        sys.stdout.flush()


main()
