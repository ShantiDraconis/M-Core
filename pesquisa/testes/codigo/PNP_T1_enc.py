"""PNP T1 — exact circuit size by SAT (CaDiCaL), own DIMACS encoding.

Bases:
  ATK : gates AND, OR, NOT (fan-in 2, NOT ignores 2nd input, NOT counted);
        faithful to ATK.Shannon.Circuito: gate k may read any wire < n+k, and a
        reference to a wire >= n+k reads `false` (modelled by one extra candidate 'F').
        Output = last wire (s=0 -> x_{n-1}).
  B2  : all 16 binary functions (normalised gates g(0,0)=0, output negation free).
  U2  : B2 minus XOR/XNOR (De Morgan basis with free negations).
Modes:
  faithful : no symmetry breaking (ATK only meaningful one).
  sb       : symmetry breaking valid for MINIMUM circuits of a non-constant,
             non-projection f: a<b for AND/OR (b=a for NOT), no constant 'F',
             every non-output gate is read, gates compute pairwise distinct,
             non-constant functions different from inputs, adjacent independent
             gates in lexicographic order of (a,b).
"""
import itertools, subprocess, os, time, tempfile

CADICAL = "/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/pylibs/cadical/build/cadical"


class CNF:
    def __init__(self):
        self.nv = 0
        self.cl = []

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.cl.append(c)

    def exactly_one(self, lits):
        self.add(list(lits))
        for a, b in itertools.combinations(lits, 2):
            self.add([-a, -b])

    def dimacs(self):
        out = ["p cnf %d %d" % (self.nv, len(self.cl))]
        out += [" ".join(map(str, c)) + " 0" for c in self.cl]
        return "\n".join(out) + "\n"


def encode(n, s, f, basis="ATK", mode="sb", symmetric=True, maxnot=None):
    """f: list of 2^n bits, f[x], bit c of x = x_c. Returns (cnf, meta) or None if s==0."""
    assert s >= 1
    N = 1 << n
    C = CNF()
    sb = (mode == "sb")
    val = [[C.var() for x in range(N)] for i in range(s)]  # gate values

    def wval(c, x):  # literal or constant for wire c at row x
        if c == 'F':
            return False
        if c < n:
            return bool((x >> c) & 1)
        return val[c - n][x]

    A, B, ops, inA, inB = [], [], [], [], []
    for i in range(s):
        cands = list(range(n + i))
        if basis == "ATK" and not sb:
            cands = cands + ['F']
        Ai = {c: C.var() for c in cands}
        Bi = {c: C.var() for c in cands}
        C.exactly_one(list(Ai.values()))
        C.exactly_one(list(Bi.values()))
        A.append(Ai); B.append(Bi)
        ia = [C.var() for x in range(N)]
        ib = [C.var() for x in range(N)]
        inA.append(ia); inB.append(ib)
        for sel, inp in ((Ai, ia), (Bi, ib)):
            for c, lit in sel.items():
                for x in range(N):
                    w = wval(c, x)
                    if w is True:
                        C.add([-lit, inp[x]])
                    elif w is False:
                        C.add([-lit, -inp[x]])
                    else:
                        C.add([-lit, -inp[x], w]); C.add([-lit, inp[x], -w])
        v = val[i]
        if basis == "ATK":
            oA, oO, oN = C.var(), C.var(), C.var()
            C.exactly_one([oA, oO, oN])
            ops.append((oA, oO, oN))
            for x in range(N):
                a, b, y = ia[x], ib[x], v[x]
                C.add([-oA, -y, a]); C.add([-oA, -y, b]); C.add([-oA, y, -a, -b])
                C.add([-oO, y, -a]); C.add([-oO, y, -b]); C.add([-oO, -y, a, b])
                C.add([-oN, y, a]); C.add([-oN, -y, -a])
            if sb:
                # a<b for AND/OR, b=a for NOT
                for c in cands:
                    for d in cands:
                        if d < c:
                            C.add([-Ai[c], -Bi[d]])
                    C.add([-Ai[c], -Bi[c], oN])
                    C.add([-oN, -Ai[c], Bi[c]])
        else:  # B2 / U2, normalised gates
            g01, g10, g11 = C.var(), C.var(), C.var()
            ops.append((g01, g10, g11))
            C.add([g01, g10, g11])            # not constant 0
            C.add([g01, -g10, -g11])          # not projection a  (0,1,1)
            C.add([-g01, g10, -g11])          # not projection b  (1,0,1)
            if basis == "U2":
                C.add([-g01, -g10, g11])      # not XOR (1,1,0)
            gb = {(0, 1): g01, (1, 0): g10, (1, 1): g11}
            for x in range(N):
                a, b, y = ia[x], ib[x], v[x]
                C.add([a, b, -y])
                for (p, q), g in gb.items():
                    la = -a if p else a
                    lb = -b if q else b
                    C.add([la, lb, -y, g]); C.add([la, lb, y, -g])
            for c in cands:  # a<b always (normalised B2 gates are closed under swap)
                for d in cands:
                    if d <= c:
                        C.add([-Ai[c], -Bi[d]])
    # output
    target = f if basis == "ATK" else [fx ^ f[0] for fx in f]
    for x in range(N):
        C.add([val[s - 1][x] if target[x] else -val[s - 1][x]])
    if sb:
        # every non-output gate is read by a later gate
        for i in range(s - 1):
            w = n + i
            C.add([A[j][w] for j in range(i + 1, s)] + [B[j][w] for j in range(i + 1, s)])
        # gate functions: non-constant, != inputs, pairwise distinct
        for i in range(s):
            C.add([val[i][x] for x in range(N)])
            C.add([-val[i][x] for x in range(N)])
            for c in range(n):
                C.add([(-val[i][x] if (x >> c) & 1 else val[i][x]) for x in range(N)])
        for i in range(s):
            for j in range(i + 1, s):
                ds = []
                for x in range(N):
                    d = C.var(); ds.append(d)
                    C.add([-d, val[i][x], val[j][x]]); C.add([-d, -val[i][x], -val[j][x]])
                C.add(ds)
        # adjacent independent gates: (a_i,b_i) <=lex (a_{i+1},b_{i+1})
        for i in range(s - 1):
            w = n + i
            ind = C.var()
            C.add([A[i + 1][w], B[i + 1][w], ind])
            eq = C.var()
            for c in A[i]:
                C.add([-A[i][c], -A[i + 1][c], eq])
                for c2 in A[i + 1]:
                    if c2 < c:
                        C.add([-ind, -A[i][c], -A[i + 1][c2]])
            for d in B[i]:
                for d2 in B[i + 1]:
                    if d2 < d:
                        C.add([-ind, -eq, -B[i][d], -B[i + 1][d2]])
    if sb:
        # f depends on every input -> every input is read by some gate
        for c in range(n):
            C.add([A[i][c] for i in range(s)] + [B[i][c] for i in range(s)])
        # symmetric f: minimise the (a,b)-word also over input permutations ->
        # first gate reads x0 and (x0 or x1)  [compatible with the lex rule above]
        if symmetric and n >= 2:
            C.add([A[0][0]])
            C.add([B[0][0], B[0][1]])
    if basis == "ATK" and maxnot is not None:
        # at most `maxnot` NOT gates (Sinz sequential counter).  Valid when maxnot = s - C_U2(f):
        # absorbing every NOT into the U2 gates that read it leaves a U2 circuit with s - #NOT gates.
        xs = [ops[i][2] for i in range(s)]
        K = maxnot
        if K == 0:
            for x in xs:
                C.add([-x])
        else:
            R = [[C.var() for j in range(K)] for i in range(s)]
            for i, x in enumerate(xs):
                C.add([-x, R[i][0]])
                if i > 0:
                    for j in range(K):
                        C.add([-R[i - 1][j], R[i][j]])
                    for j in range(1, K):
                        C.add([-x, -R[i - 1][j - 1], R[i][j]])
                    C.add([-x, -R[i - 1][K - 1]])
    meta = dict(A=A, B=B, ops=ops, n=n, s=s, basis=basis, mode=mode)
    return C, meta


def solve(C, timeout, tag="", extra=()):
    fd, path = tempfile.mkstemp(suffix=".cnf", dir=os.environ.get("CNFDIR", "/tmp"))
    with os.fdopen(fd, "w") as fh:
        fh.write(C.dimacs())
    t0 = time.time()
    try:
        p = subprocess.run(["nice", "-n", "10", CADICAL, "-q", "-t", str(timeout)] + list(extra) + [path],
                           capture_output=True, text=True, timeout=timeout + 30)
        out, rc = p.stdout, p.returncode
    except subprocess.TimeoutExpired:
        out, rc = "", 0
    dt = time.time() - t0
    try:
        os.unlink(path)
    except OSError:
        pass
    if rc == 10:
        model = set()
        for line in out.splitlines():
            if line.startswith("v "):
                for t in line[2:].split():
                    k = int(t)
                    if k > 0:
                        model.add(k)
        return "SAT", model, dt
    if rc == 20:
        return "UNSAT", None, dt
    return "UNKNOWN", None, dt


def decode(meta, model):
    n, s = meta["n"], meta["s"]
    gates = []
    for i in range(s):
        a = [c for c, l in meta["A"][i].items() if l in model][0]
        b = [c for c, l in meta["B"][i].items() if l in model][0]
        if meta["basis"] == "ATK":
            oA, oO, oN = meta["ops"][i]
            op = "e" if oA in model else ("ou" if oO in model else "nao")
        else:
            g01, g10, g11 = meta["ops"][i]
            op = (int(g01 in model), int(g10 in model), int(g11 in model))
        # 'F' -> any wire index >= n+i reads false in ATK semantics; use n+s-1
        if a == 'F':
            a = n + s - 1
        if b == 'F':
            b = n + s - 1
        gates.append((op, a, b))
    return gates


# ---------- independent evaluators ----------
def atk_avalia(G, v0):
    """Literal transcription of ATK.Shannon.avalia: foldl, getD false."""
    v = list(v0)
    for (op, a, b) in G:
        xa = v[a] if a < len(v) else False
        xb = v[b] if b < len(v) else False
        if op == "e":
            r = xa and xb
        elif op == "ou":
            r = xa or xb
        else:
            r = not xa
        v = v + [r]
    return v[-1] if v else False


def atk_computa(G, n):
    return [int(atk_avalia(G, [bool((x >> c) & 1) for c in range(n)])) for x in range(1 << n)]


def b2_computa(G, n, f0):
    out = []
    for x in range(1 << n):
        v = [(x >> c) & 1 for c in range(n)]
        for (op, a, b) in G:
            g01, g10, g11 = op
            tt = {(0, 0): 0, (0, 1): g01, (1, 0): g10, (1, 1): g11}
            v.append(tt[(v[a], v[b])])
        out.append(v[-1] ^ f0)
    return out


# ---------- functions ----------
def tt(n, fn):
    return [int(fn([(x >> c) & 1 for c in range(n)])) for x in range(1 << n)]

FUNCS = {
    "OR": lambda n: tt(n, lambda xs: any(xs)),
    "XOR": lambda n: tt(n, lambda xs: sum(xs) % 2),
    "MAJ": lambda n: tt(n, lambda xs: 2 * sum(xs) > n),
    "MOD3_0": lambda n: tt(n, lambda xs: sum(xs) % 3 == 0),
    "MOD3_1": lambda n: tt(n, lambda xs: sum(xs) % 3 == 1),
    "MOD3_2": lambda n: tt(n, lambda xs: sum(xs) % 3 == 2),
}


def min_size(fname, n, basis, mode, s_lo, s_hi, timeout, log, cu2=None, extra=()):
    """cu2: proven C_U2(f); then for ATK every s < cu2 is excluded and #NOT <= s - cu2 is imposed."""
    f = FUNCS[fname](n)
    rows = []
    lo = s_lo  # every s < lo is excluded (by theory)
    # s = 0 handled directly (ATK: output x_{n-1})
    proven_unsat_upto = s_lo - 1
    if cu2 is not None:
        s_lo = max(s_lo, cu2)
        proven_unsat_upto = s_lo - 1
    for s in range(max(s_lo, 1), s_hi + 1):
        C, meta = encode(n, s, f, basis, mode, maxnot=(s - cu2) if cu2 is not None else None)
        st, model, dt = solve(C, timeout, extra=extra)
        rows.append((s, st, round(dt, 2), C.nv, len(C.cl)))
        log("  %s n=%d %s/%s s=%d -> %s (%.1fs, %d vars, %d cl)" % (fname, n, basis, mode, s, st, dt, C.nv, len(C.cl)))
        if st == "UNSAT" and proven_unsat_upto == s - 1:
            proven_unsat_upto = s
        if st == "SAT":
            G = decode(meta, model)
            comp = atk_computa(G, n) if basis == "ATK" else b2_computa(G, n, f[0])
            ok = (comp == f)
            return dict(f=fname, n=n, basis=basis, mode=mode, cu2=cu2, lo=proven_unsat_upto + 1, hi=s,
                        circuit=G, verified=ok, rows=rows)
    return dict(f=fname, n=n, basis=basis, mode=mode, cu2=cu2, lo=proven_unsat_upto + 1, hi=None,
                circuit=None, verified=None, rows=rows)
