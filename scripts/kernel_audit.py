from pathlib import Path
import re, sys

files = [
    Path("lean/MCore/TopologyCore.lean"),
    Path("lean/MCore/SpanCospanCore.lean"),
    Path("lean/MCore/ResolutionPredicate.lean"),
    Path("lean/MCore/ExactGapLedger.lean"),
    Path("lean/MCore/RecoveryFirewall.lean"),
    Path("lean/MCore/DeltaIsolation.lean"),
    Path("lean/MCore/TopologyLimitClosed.lean"),
    Path("lean/MCore/ErrorTheoryClosed.lean"),
    Path("lean/MCore/PoincareRealImport.lean"),
    Path("lean/MCore/HistoricalFull.lean"),
    Path("lean/MCore/SigmaClassification.lean"),
    Path("lean/MCore/SevenDeltasFormal.lean"),
    Path("lean/MCore/SevenParallelAttack.lean"),
    Path("lean/MCore/Attack/NS/MNavierStokes.lean"),
    Path("lean/MCore/Attack/NS/G5DirectCorrected.lean"),
    Path("lean/MCore/KernelBuild.lean"),
]
patterns = {
    "sorry": re.compile(r"\bsorry\b"),
    "admit": re.compile(r"\badmit\b"),
    "axiom": re.compile(r"^\s*axiom\b", re.M),
}
hits = []
for f in files:
    text = f.read_text(encoding="utf-8")
    for name, pat in patterns.items():
        for m in pat.finditer(text):
            hits.append((str(f), name, text.count("\n", 0, m.start()) + 1))

for path, kind, line in hits:
    print(f"{kind.upper()} {path}:{line}")

print(f"PROOF_GAP_HITS: {len(hits)}")
print("FINAL PROOF 0/7")
sys.exit(1 if hits else 0)
