"""Driver: python3 PNP_T1_run.py <jobfile-tag> ; jobs defined below. Appends JSON lines to work/PNP_T1_<tag>.jsonl"""
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get("PNPWORK", "/tmp/claude-0/-home-claude/a7d41c1e-9201-5acd-ad60-9a9635944b71/scratchpad/research/tests/work")
os.environ["CNFDIR"] = "/dev/shm/pnp"  # / is full (Lean build); CNFs are transient
from PNP_T1_enc import min_size

JOBS = {
    # calibration in B2 / U2 (sb mode); expected B2 MOD3 (Knuth via KPS): n=3: 3,4,4; n=4: 7,7,6; n=5: 10,9,10
    "calib": [("MOD3_%d" % r, n, "B2", "sb", n - 1, 14, 120) for n in (3, 4) for r in (0, 1, 2)]
             + [("XOR", n, "U2", "sb", n - 1, 3 * (n - 1), 120) for n in (2, 3, 4)],
    "calib5": [("MOD3_%d" % r, 5, "B2", "sb", 4, 12, 200) for r in (0, 1, 2)]
              + [("XOR", 5, "U2", "sb", 4, 12, 200)],
    "atk_small": [("OR", n, "ATK", "sb", n - 1, n - 1 + 3, 60) for n in (2, 3, 4, 5, 6)]
                 + [("XOR", n, "ATK", "sb", n - 1, 4 * (n - 1), 120) for n in (2, 3, 4)]
                 + [("MAJ", 3, "ATK", "sb", 2, 10, 120)]
                 + [("MOD3_%d" % r, 3, "ATK", "sb", 2, 14, 120) for r in (0, 1, 2)],
    "u2": [("MOD3_%d" % r, n, "U2", "sb", n - 1, 16, 200) for n in (3, 4) for r in (0, 1, 2)],
    "u2maj5": [("MAJ", 5, "U2", "sb", 4, 14, 400)],
    "atk_mod3_4": [("MOD3_2", 4, "ATK", "sb", 3, 16, 300, 9), ("MOD3_0", 4, "ATK", "sb", 3, 16, 300, 10),
                   ("MOD3_1", 4, "ATK", "sb", 3, 16, 300, 10)],
    "atk_cu2_check": [("MOD3_%d" % r, 3, "ATK", "sb", 2, 14, 120, c) for r, c in ((0, 5), (1, 6), (2, 6))]
                     + [("XOR", n, "ATK", "sb", n - 1, 4 * (n - 1), 120, 3 * (n - 1)) for n in (2, 3)],
    "atk_faithful": [("OR", n, "ATK", "faithful", n - 1, n - 1 + 3, 60) for n in (2, 3, 4)]
                    + [("XOR", n, "ATK", "faithful", n - 1, 4 * (n - 1), 120) for n in (2, 3)]
                    + [("MAJ", 3, "ATK", "faithful", 2, 10, 120)]
                    + [("MOD3_%d" % r, 3, "ATK", "faithful", 2, 14, 120) for r in (0, 1, 2)],
}

if __name__ == "__main__":
    tag = sys.argv[1]
    jobs = JOBS.get(tag, [])
    if len(sys.argv) > 2:  # explicit job: f n basis mode lo hi timeout
        a = sys.argv[2:]
        jobs = [(a[0], int(a[1]), a[2], a[3], int(a[4]), int(a[5]), int(a[6])) + ((int(a[7]),) if len(a) > 7 else ())]
    out = open(os.path.join(WORK, "PNP_T1_%s.jsonl" % tag), "a")
    T0 = time.time()
    for job in jobs:
        fn, n, basis, mode, lo, hi, to = job[:7]
        cu2 = job[7] if len(job) > 7 else None
        r = min_size(fn, n, basis, mode, lo, hi, to, lambda m: print(m, flush=True), cu2=cu2)
        r["circuit"] = [list(map(lambda z: z if not isinstance(z, tuple) else list(z), g)) for g in (r["circuit"] or [])]
        print("RESULT %s n=%d %s/%s: lo=%s hi=%s verified=%s" % (fn, n, basis, mode, r["lo"], r["hi"], r["verified"]), flush=True)
        out.write(json.dumps(r) + "\n"); out.flush()
    print("total wall %.1fs" % (time.time() - T0))
