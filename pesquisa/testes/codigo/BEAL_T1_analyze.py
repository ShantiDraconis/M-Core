# BEAL T1: analise. (1) 2a implementacao de S0/S2 direto das definicoes Lean; (2) % por cenario em E e no
# subdominio mdc<=2; (3) ABC_{7/4} e Q de Laishram-Shorey; (4) triplos descobertos com s > 1/1.62991;
# (5) rankings de assinaturas; (6) checagem de levantamento das solucoes conhecidas.
import sys
from math import gcd
from fractions import Fraction
from collections import Counter

W = sys.argv[1]
LO, HI = 3, 200
N = HI - LO + 1
NC = N ** 3

def load(tag):
    with open(f"{W}/beal_level_{tag}.bin", "rb") as f:
        b = f.read()
    assert len(b) == NC
    return b

lev = {"cons": load("cons"), "perm": load("perm")}
L = lev["cons"]

# ---------- (1) implementacao independente de S0 (ExclusaoResidualRegular) e S2 (ResidualFinal) ----------
cS0 = cS2 = cG2 = 0
mism = 0
g2 = bytearray(NC)
i = 0
for x in range(LO, HI + 1):
    for y in range(LO, HI + 1):
        gxy = gcd(x, y)
        for z in range(LO, HI + 1):
            g = gcd(gxy, z)
            f442 = (x % 4 == 0 and y % 4 == 0 and z % 2 == 0) or (x % 4 == 0 and y % 2 == 0 and z % 4 == 0) or \
                   (x % 2 == 0 and y % 4 == 0 and z % 4 == 0)
            s0 = any(g % d == 0 for d in (3, 4, 5, 7, 11, 13, 17, 19)) or f442 or \
                 (x % 6 == 0 and y % 6 == 0 and z % 2 == 0)
            resfinal = g <= 2 and not f442 and not (gxy >= 4 and z % 2 == 0) and not (gxy >= 3 and z % 3 == 0)
            s2 = not resfinal
            cS0 += s0; cS2 += s2
            if g <= 2:
                g2[i] = 1; cG2 += 1
            if s0 != (L[i] <= 0) or s2 != (L[i] <= 2):
                mism += 1
            i += 1
print(f"[2a impl.] S0 = {cS0} ({100*cS0/NC:.4f}%), S2 = {cS2} ({100*cS2/NC:.4f}%), "
      f"divergencias celula a celula vs padroes = {mism}; |mdc<=2| = {cG2}")

# ---------- (2) percentuais por cenario ----------
def s_le_47(x, y, z):  # 1/x+1/y+1/z <= 4/7
    return 7 * (x * y + y * z + z * x) <= 4 * x * y * z

names = ["S0 kernel", "S1 +FLT(B2)", "S2 +DM fraca(B8)", "S3 +DM inteira", "S4 +literatura arbitrada",
         "S5 +GRH", "S6 +(3,5,7),(13,13,5) s/arbitr.", "S7 +SFC (Mihailescu)"]
abc = bytearray(NC)
i = 0
for x in range(LO, HI + 1):
    for y in range(LO, HI + 1):
        for z in range(LO, HI + 1):
            abc[i] = s_le_47(x, y, z); i += 1
print("\ncenario | cons: E% | cons: mdc<=2 % | perm: E% | perm: mdc<=2 %")
for sc in range(8):
    row = []
    for tag in ("cons", "perm"):
        Lv = lev[tag]
        cE = sum(1 for v in Lv if v <= sc)
        cD = sum(1 for j in range(NC) if g2[j] and Lv[j] <= sc)
        row += [cE, cD]
    print(f"{names[sc]:34s} | {row[0]:8d} {100*row[0]/NC:6.2f}% | {row[1]:8d} {100*row[1]/cG2:6.2f}% | "
          f"{row[2]:8d} {100*row[2]/NC:6.2f}% | {row[3]:8d} {100*row[3]/cG2:6.2f}%")
for base in (4, 7):
    cE = sum(1 for j in range(NC) if L[j] <= base or abc[j])
    cD = sum(1 for j in range(NC) if g2[j] and (L[j] <= base or abc[j]))
    print(f"S{base}+ABC_7/4 (s<=4/7)                  | {cE:8d} {100*cE/NC:6.2f}% | {cD:8d} {100*cD/cG2:6.2f}%")
print("ABC_7/4 sozinho:", sum(abc), f"{100*sum(abc)/NC:.2f}%")

# ---------- (3) residuo apos S7+ABC: comparar com Q de Laishram-Shorey ----------
def idx2(i):
    z = i % N; y = (i // N) % N; x = i // (N * N)
    return x + LO, y + LO, z + LO
res8 = Counter()
for j in range(NC):
    if L[j] > 7 and not abc[j]:
        res8[tuple(sorted(idx2(j)))] += 1
def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
def reduces_to_Q(t):
    import itertools
    for a, b, c in itertools.permutations(t):
        if a % 3 == 0 and b % 4 == 0 and any(is_prime(p) and p >= 5 and c % p == 0 for p in range(5, c + 1)):
            return True
        if a % 3 == 0 and b % 5 == 0 and any(c % p == 0 for p in (7, 11, 13, 17, 19, 23)):
            return True
    return False
notQ = [t for t in res8 if not reduces_to_Q(t)]
print(f"\nResiduo S7+ABC: {sum(res8.values())} triplos ordenados, {len(res8)} classes (a menos de permutacao);"
      f" fora da reducao a Q de L-S: {len(notQ)} -> {sorted(notQ)[:30]}")
print("  menores classes do residuo S7+ABC:", sorted(res8)[:40])

# ---------- (4) descobertos em S4 com s > 1/1.62991 (nao seriam recorde abc) ----------
thr = Fraction(100000, 162991)
low = Counter()
for j in range(NC):
    if L[j] > 4:
        x, y, z = idx2(j)
        if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) > thr:
            low[tuple(sorted((x, y, z)))] += 1
print(f"\nDescobertos em S4 com s > 0.61353: {sum(low.values())} ordenados, {len(low)} classes:")
print("  ", sorted(low))

# ---------- (5) rankings ----------
sig = {}
with open(f"{W}/beal_cands_sig.txt") as f:
    for line in f:
        a, p, q, r = map(int, line.split()); sig[a] = (p, q, r)
for tag in ("cons", "perm"):
    raw = {4: {}, 6: {}}; greedy = []
    with open(f"{W}/beal_rank_{tag}.txt") as f:
        for line in f:
            t = line.split()
            if t[0] == "raw":
                raw[int(t[1][1:])][int(t[2])] = int(t[3])
            else:
                greedy.append((int(t[1]), int(t[2]), int(t[3])))
    unc4 = sum(1 for v in lev[tag] if v > 4)
    print(f"\n[{tag}] descobertos em S4: {unc4}")
    top = sorted(raw[4].items(), key=lambda t: -t[1])[:25]
    print("  top-25 bruto (sobre S4): " + "; ".join(f"{sig[c]}:{v} [{raw[6][c]}]" for c, v in top))
    acc = 0
    out = []
    for it, c, v in greedy:
        acc += v; out.append(f"{it}.{sig[c]} +{v} ({100*acc/unc4:.1f}%)")
    print("  guloso (ganho marginal sobre S4, % acumulado do descoberto): " + "; ".join(out))
    for s in [(2, 3, 13), (2, 5, 7), (3, 5, 11), (3, 4, 7), (2, 3, 11), (3, 5, 7), (2, 5, 5), (3, 4, 11)]:
        cid = [k for k, v in sig.items() if v == tuple(sorted(s))]
        if cid:
            print(f"   {s}: bruto S4 = {raw[4][cid[0]]}, S6 = {raw[6][cid[0]]}")

# ---------- (6) levantamento das solucoes primitivas conhecidas ----------
def iroot(n, k):
    lo, hi = 0, 1
    while hi ** k <= n:
        hi *= 2
    while lo < hi - 1:
        m = (lo + hi) // 2
        if m ** k <= n: lo = m
        else: hi = m
    return lo
def exps(v):  # expoentes e in [3,200] com v = t^e
    if v == 1:
        return list(range(3, 201))
    return [e for e in range(3, 201) if iroot(v, e) ** e == v]
known = [((1, 3), (2, 3), (3, 2)), ((2, 5), (7, 2), (3, 4)), ((7, 3), (13, 2), (2, 9)), ((2, 7), (17, 3), (71, 2)),
         ((3, 5), (11, 4), (122, 2)), ((17, 7), (76271, 3), (21063928, 2)), ((1414, 3), (2213459, 2), (65, 7)),
         ((9262, 3), (15312283, 2), (113, 7)), ((43, 8), (96222, 3), (30042907, 2)), ((33, 8), (1549034, 2), (15613, 3))]
print("\nLevantamento: termos u^e das 10 identidades conhecidas (+Catalan 1+2^3=3^2):")
for t in known:
    assert t[0][0] ** t[0][1] + t[1][0] ** t[1][1] == t[2][0] ** t[2][1], t
    ex = [exps(b ** e) for b, e in t]
    lifts = all(ex)
    print(f"  {t[0][0]}^{t[0][1]} + {t[1][0]}^{t[1][1]} = {t[2][0]}^{t[2][1]}: termos com expoente>=3 possivel: "
          f"{[bool(e) for e in ex]} -> levanta a Beal? {lifts}")
