# BEAL T1: gera padroes de divisibilidade (dx,dy,dz) por cenario e por assinatura candidata.
# Um triplo de Beal (x,y,z) (a^x + b^y = c^z) e coberto por uma equacao assinada A^p + B^q = C^r sobre Z
# (sem solucao primitiva nao trivial, fora uma lista conhecida) se existe um arranjo dos termos
# (+a^x, +b^y, -c^z) [ou todos com sinal trocado] nos slots (+A^p, +B^q, -C^r) tal que
# o expoente do slot divide o expoente do termo e, se o sinal do termo difere do sinal do slot,
# o expoente do slot e impar (o sinal entra na base).
import itertools, sys

EMAX = 200

def primes(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** .5) + 1))]

PR = primes(EMAX)

def patterns_ordered(sig):
    """Padroes (dx,dy,dz) vindos da equacao ordenada A^p + B^q = C^r (sig=(p,q,r))."""
    slots = [(+1, sig[0]), (+1, sig[1]), (-1, sig[2])]
    terms = [+1, +1, -1]  # a^x, b^y, -c^z
    out = set()
    for flip in (+1, -1):
        for perm in itertools.permutations(range(3)):  # termo i -> slot perm[i]
            ok = True
            for i in range(3):
                ssign, sexp = slots[perm[i]]
                if terms[i] * flip != ssign and sexp % 2 == 0:
                    ok = False; break
            if ok:
                out.add(tuple(slots[perm[i]][1] for i in range(3)))
    return {p for p in out if all(d <= EMAX for d in p)}

def patterns(sig, all_perms):
    if not all_perms:
        return patterns_ordered(sig)
    out = set()
    for s in set(itertools.permutations(sig)):
        out |= patterns_ordered(s)
    return out

# ---------------- entradas por cenario ----------------
# cada entrada: (cenario, rotulo, lista de assinaturas, all_perms?)  all_perms=False <=> '*' do survey
E = []
# S0: kernel incondicional (ExclusaoResidualRegular)
for d in (3, 4, 5, 7, 11, 13, 17, 19):
    E.append((0, f"kernel FLT({d})", [(d, d, d)], True))
E.append((0, "kernel (4,4,2) e perms", [(4, 4, 2), (4, 2, 4), (2, 4, 4)], False))
E.append((0, "kernel (6,6,2) [6|x,6|y,2|z]", [(6, 6, 2)], False))
# S1: + FLT (B2)
E.append((1, "FLT (n,n,n)", [(n, n, n) for n in range(3, EMAX + 1)], True))
# S2: + Darmon-Merel forma fraca do kernel (A,B>0; so o arranjo x,y -> n e z -> 2/3)
DMW = set()
for n in range(4, EMAX + 1):
    DMW.add((n, n, 2))
for n in range(3, EMAX + 1):
    DMW.add((n, n, 3))
# S3: + Darmon-Merel inteiro (todas as permutacoes/sinais); (4,4,2) = Fermat
E.append((3, "DM inteiro (n,n,2) n>=4, (n,n,3) n>=3", [(n, n, 2) for n in range(4, EMAX + 1)] +
          [(n, n, 3) for n in range(3, EMAX + 1)], True))
# S4: literatura arbitrada (Ratcliffe-Grechuk Tab. 1.1, sem GRH)
S4 = [
    ("(2,3,n) n in {7,8,9,10,12,15}", [(2, 3, n) for n in (7, 8, 9, 10, 12, 15)], True),
    ("(2,4,n) n>=5", [(2, 4, n) for n in range(5, EMAX + 1)], True),
    ("(2,6,n) n>=3", [(2, 6, n) for n in range(3, EMAX + 1)], True),
    ("(2,2n,3)* 3<=n", [(2, 2 * n, 3) for n in range(3, EMAX // 2 + 1)], False),
    ("(2,2n,m)* m in {6,9,10,15,21}, n>=2", [(2, 2 * n, m) for m in (6, 9, 10, 15, 21) for n in range(2, EMAX // 2 + 1)], False),
    ("(4,2n,3)* n>=2", [(4, 2 * n, 3) for n in range(2, EMAX // 2 + 1)], False),
    ("(3,4,5)", [(3, 4, 5)], True),
    ("(3,3,n) n<=1e9", [(3, 3, n) for n in range(3, EMAX + 1)], True),
    ("(3,6,n) n>=3", [(3, 6, n) for n in range(3, EMAX + 1)], True),
    ("(5,5,7),(5,5,19),(7,7,5)", [(5, 5, 7), (5, 5, 19), (7, 7, 5)], True),
    ("(2j,2k,n)* j,k>=5 primos, n in {3,5,7,11,13}", [(2 * j, 2 * k, n) for j in PR if j >= 5 and 2 * j <= EMAX
                                                      for k in PR if k >= 5 and 2 * k <= EMAX for n in (3, 5, 7, 11, 13)], False),
    ("(2j,2k,17)* j,k primos !=5", [(2 * j, 2 * k, 17) for j in PR if j != 5 and 2 * j <= EMAX
                                    for k in PR if k != 5 and 2 * k <= EMAX], False),
    ("(2n,2n,5)* n>=2", [(2 * n, 2 * n, 5) for n in range(2, EMAX // 2 + 1)], False),
    ("(2n,2n,17)* n>=2", [(2 * n, 2 * n, 17) for n in range(2, EMAX // 2 + 1)], False),
    # (3j,3k,n)* j,k>=2: redundante com (3,3,n) (todas as permutacoes, n<=1e9) no mesmo cenario -> omitido
]
for lab, sigs, ap in S4:
    E.append((4, lab, sigs, ap))
# S5: + GRH
E.append((5, "GRH: (2,3,11),(5,5,11),(5,5,13),(7,7,11),(13,13,7)",
          [(2, 3, 11), (5, 5, 11), (5, 5, 13), (7, 7, 11), (13, 13, 7)], True))
# S6: + alegacoes sem arbitragem: (3,5,7) Chocian 2609.26996; (13,13,5) Best-Dahmen-Freitas 2510.12092
E.append((6, "sem arbitragem: (3,5,7), (13,13,5)", [(3, 5, 7), (13, 13, 5)], True))
# S7: + Strong Fermat-Catalan (Mihailescu 2509.18275): x^p+y^p=z^q, p>=5 primo, q primo impar != p
E.append((7, "SFC (p,p,q)", [(p, p, q) for p in PR if p >= 5 for q in PR if q >= 3 and q != p], True))

def scenario_patterns(permissive=False):
    pats = {}
    for sc, lab, sigs, ap in E:
        for s in sigs:
            for pt in patterns(s, ap or (permissive and sc >= 4)):  # permissiva so na literatura
                if pt not in pats or pats[pt][0] > sc:
                    pats[pt] = (sc, lab)
    for pt in DMW:  # S2
        if pt not in pats or pats[pt][0] > 2:
            pats[pt] = (2, "DM fraca do kernel")
    return pats

def candidates(maxe=50):
    C = []
    for p in range(2, maxe + 1):
        for q in range(p, maxe + 1):
            for r in range(q, maxe + 1):
                if q * r + p * r + p * q < p * q * r:  # 1/p+1/q+1/r < 1
                    C.append(((p, q, r), sorted(patterns((p, q, r), True))))
    return C

if __name__ == "__main__":
    outdir = sys.argv[1]
    for tag, perm in (("cons", False), ("perm", True)):
        pats = scenario_patterns(perm)
        with open(f"{outdir}/beal_pats_{tag}.txt", "w") as f:
            for pt, (sc, lab) in sorted(pats.items(), key=lambda t: (t[1][0], t[0])):
                f.write(f"{sc} {pt[0]} {pt[1]} {pt[2]}\n")
        print(tag, "padroes:", len(pats), {s: sum(1 for v in pats.values() if v[0] == s) for s in range(8)})
    C = candidates()
    with open(f"{outdir}/beal_cands.txt", "w") as f:
        for i, (sig, pl) in enumerate(C):
            for pt in pl:
                f.write(f"{i} {pt[0]} {pt[1]} {pt[2]}\n")
    with open(f"{outdir}/beal_cands_sig.txt", "w") as f:
        for i, (sig, pl) in enumerate(C):
            f.write(f"{i} {sig[0]} {sig[1]} {sig[2]}\n")
    print("candidatas:", len(C))
    # sanidade do motor de arranjos
    print("padroes (5,5,2):", sorted(patterns((5, 5, 2), True)))
    print("padroes (2,2*3,3)* :", sorted(patterns((2, 6, 3), False)))
    print("padroes (4,4,2) perms:", sorted(patterns((4, 4, 2), True)))
