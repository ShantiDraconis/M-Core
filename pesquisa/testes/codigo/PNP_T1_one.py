"""Single instance: python3 PNP_T1_one.py FUNC n basis mode s timeout [cadical options...]"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get("PNPWORK", "/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/work")
os.environ["CNFDIR"] = "/dev/shm/pnp"  # / is full (Lean build); CNFs are transient
from PNP_T1_enc import *
fn, n, basis, mode, s, to = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
extra = [a for a in sys.argv[7:] if not a.startswith('maxnot=')]
mn = [int(a[7:]) for a in sys.argv[7:] if a.startswith('maxnot=')]
mn = mn[0] if mn else None
f = FUNCS[fn](n)
C, meta = encode(n, s, f, basis, mode, maxnot=mn)
st, model, dt = solve(C, to, extra=extra)
ver = None; G = None
if st == "SAT":
    G = decode(meta, model)
    comp = atk_computa(G, n) if basis == "ATK" else b2_computa(G, n, f[0])
    ver = (comp == f)
rec = dict(f=fn, n=n, basis=basis, mode=mode, s=s, maxnot=mn, status=st, time=round(dt, 1), opts=extra, verified=ver,
           circuit=[[g[0] if not isinstance(g[0], tuple) else list(g[0]), g[1], g[2]] for g in G] if G else None)
print(json.dumps(rec), flush=True)
with open(os.path.join(WORK, "PNP_T1_single.jsonl"), "a") as fh:
    fh.write(json.dumps(rec) + "\n")
