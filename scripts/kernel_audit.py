from pathlib import Path
import re, sys

root = Path("lean/MCore")
patterns = {
    "sorry": re.compile(r"\bsorry\b"),
    "admit": re.compile(r"\badmit\b"),
    "axiom": re.compile(r"^\s*axiom\b", re.M),
}
hits = []
for f in root.rglob("*.lean"):
    text = f.read_text(encoding="utf-8")
    for name, pat in patterns.items():
        for m in pat.finditer(text):
            hits.append((str(f), name, text.count("\n", 0, m.start()) + 1))

for path, kind, line in hits:
    print(f"{kind.upper()} {path}:{line}")

print(f"PROOF_GAP_HITS: {len(hits)}")
print("FINAL PROOF 0/7")
sys.exit(1 if hits else 0)
