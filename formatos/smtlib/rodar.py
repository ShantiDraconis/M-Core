#!/usr/bin/env python3
"""Roda z3 (e cvc5, se houver) em cada .smt2; cada arquivo nega um teorema: espera-se `unsat`."""
import glob, os, subprocess, shutil, sys, json
aqui = os.path.dirname(os.path.abspath(__file__))
res, ok = {}, True
solvers = [s for s in ("z3", "cvc5") if shutil.which(s)]
if not solvers:
    try:
        import z3  # noqa
        solvers = ["z3py"]
    except ImportError:
        print("nenhum resolvedor SMT disponível"); sys.exit(2)
for f in sorted(glob.glob(os.path.join(aqui, "*.smt2"))):
    res[os.path.basename(f)] = {}
    for s in solvers:
        if s == "z3py":
            import z3
            sol = z3.Solver(); sol.from_file(f); out = str(sol.check())
        else:
            args = [s, f] if s == "z3" else [s, "--lang=smt2", f]
            out = subprocess.run(args, capture_output=True, text=True, timeout=600).stdout.strip().splitlines()[-1]
        res[os.path.basename(f)][s] = out
        ok &= (out == "unsat")
        print(f"{os.path.basename(f):28s} {s:5s} {out}")
json.dump(res, open(os.path.join(aqui, "resultado_smt.json"), "w"), indent=1)
print("TODOS unsat" if ok else "FALHA"); sys.exit(0 if ok else 1)
