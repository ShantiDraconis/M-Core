#!/usr/bin/env python3
"""Compila um módulo Lean e suas dependências locais (topológico) com `lean -o`, sem lake.
uso: kcompile.py SRC_ROOT MODULO OUT_DIR"""
import os, re, subprocess, sys
src, root, out = sys.argv[1], sys.argv[2], sys.argv[3]
K = "/home/user/M-Core/atk-kernel/.lake/packages"
libs = [os.path.join(os.environ.get("EXTRA_OUT", "/nonexistent"))] + [os.path.join(K, p, ".lake/build/lib/lean") for p in os.listdir(K)]
env = dict(os.environ, LEAN_PATH=":".join([out] + libs))
def path(m): return os.path.join(src, *m.split(".")) + ".lean"
order, seen = [], set()
def visit(m):
    if m in seen: return
    seen.add(m)
    p = path(m)
    if not os.path.exists(p): return  # externo (Mathlib etc.)
    for line in open(p, encoding="utf-8"):
        mm = re.match(r"\s*import\s+(\S+)", line)
        if mm: visit(mm.group(1))
    order.append(m)
visit(root)
ok = True
for m in order:
    o = os.path.join(out, *m.split(".")) + ".olean"
    os.makedirs(os.path.dirname(o), exist_ok=True)
    r = subprocess.run(["lean", "--root=" + src, path(m), "-o", o], env=env, capture_output=True, text=True)
    log = r.stdout + r.stderr
    errs = [l for l in log.splitlines() if ": error" in l]
    print(f"== {m}: {'OK' if r.returncode == 0 else 'FALHA'}")
    for mm in re.finditer(r"'[^']+' (?:depends on axioms: \[[^\]]*\]|does not depend on any axioms)", log):
        print("   " + " ".join(mm.group(0).split()))
    for l in log.splitlines():
        if ": error" in l or "sorry" in l: print("   " + l[:300])
    if r.returncode != 0: ok = False; break
sys.exit(0 if ok else 1)
