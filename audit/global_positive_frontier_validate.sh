#!/usr/bin/env bash
set -euo pipefail

MODULE="MCore.FinalFail.GlobalPositiveMaterialFrontier"
SOURCE="lean/MCore/FinalFail/GlobalPositiveMaterialFrontier.lean"
DEPENDENCY_FILES=(
  "lean/MCore/FinalFail/GlobalConditionalFinal.lean"
  "lean/MCore/FinalFail/Semantic/Riemann.lean"
  "lean/MCore/FinalFail/Semantic/Beal.lean"
  "lean/MCore/FinalFail/Semantic/PvsNP.lean"
  "lean/MCore/FinalFail/Semantic/NavierStokes.lean"
  "lean/MCore/FinalFail/Semantic/Hodge.lean"
  "lean/MCore/FinalFail/Semantic/BSD.lean"
  "lean/MCore/FinalFail/Semantic/YangMills.lean"
  "lean/MCore/FinalFail/SemanticParallel.lean"
)

echo "[GLOBAL-POSITIVE] source hygiene"
for f in "$SOURCE" "${DEPENDENCY_FILES[@]}"; do
  test -f "$f" || { echo "MISSING: $f"; exit 1; }
done

python3 - "$SOURCE" "${DEPENDENCY_FILES[@]}" <<'PY'
import re, sys
from pathlib import Path

def strip_lean(text: str) -> str:
    out=[]
    i=0
    depth=0
    in_string=False
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1; i += 2
            elif text.startswith('-/', i):
                depth -= 1; i += 2
            else:
                i += 1
            continue
        if in_string:
            if text[i] == '\\':
                i += 2
            elif text[i] == '"':
                in_string=False; i += 1
            else:
                i += 1
            continue
        if text.startswith('/-', i):
            depth=1; i += 2; continue
        if text.startswith('--', i):
            j=text.find('\n', i)
            if j < 0: break
            out.append('\n'); i=j+1; continue
        if text[i] == '"':
            in_string=True; i += 1; continue
        out.append(text[i]); i += 1
    return ''.join(out)

bad=False
for name in sys.argv[1:]:
    raw=Path(name).read_text(encoding='utf-8')
    code=strip_lean(raw)
    for tok in ('sorry','admit'):
        for m in re.finditer(r'(?<![A-Za-z0-9_])'+tok+r'(?![A-Za-z0-9_])', code):
            line=code.count('\n',0,m.start())+1
            print(f"ERROR: {tok} token in {name}:{line}")
            bad=True
    for m in re.finditer(r'(?m)^\s*(axiom|constant)\s+', code):
        line=code.count('\n',0,m.start())+1
        print(f"ERROR: explicit {m.group(1)} declaration in {name}:{line}")
        bad=True
if bad:
    sys.exit(1)
print("[GLOBAL-POSITIVE] active Lean sources contain no sorry/admit/axiom/constant declarations")
PY

echo "[GLOBAL-POSITIVE] build"
lake build "$MODULE" 2>&1 | tee audit/GLOBAL_POSITIVE_FRONTIER_BUILD.log

echo "[GLOBAL-POSITIVE] axiom audit"
cat > /tmp/global_positive_frontier_audit.lean <<'EOF'
import MCore.FinalFail.GlobalPositiveMaterialFrontier
#print axioms MCore.FinalFail.Semantic.beal_target_iff_gcd_lower_bound
#print axioms MCore.FinalFail.Semantic.pvsnp_target_iff_sat_np_and_not_p
#print axioms MCore.FinalFail.Semantic.ns_target_iff_exists_universal_stabilizer
#print axioms MCore.FinalFail.Semantic.hodge_target_iff_pointwise_realization
#print axioms MCore.FinalFail.Semantic.bsd_target_iff_rank_and_refined
#print axioms MCore.FinalFail.Semantic.ym_target_iff_exists_physical_theory
#print axioms MCore.FinalFail.Semantic.rh_excludes_offCriticalZero
#print axioms MCore.FinalFail.Semantic.positive_rh_incompatible_with_negative_lane
#print axioms MCore.FinalFail.Semantic.global_positive_root_iff_components
#print axioms MCore.FinalFail.Semantic.positive_root_excludes_mixed_negative_root
#print axioms MCore.FinalFail.Semantic.build_global_positive_material_root
EOF

lake env lean /tmp/global_positive_frontier_audit.lean   | tee audit/GLOBAL_POSITIVE_FRONTIER_AXIOMS.log

if grep -q 'sorryAx' audit/GLOBAL_POSITIVE_FRONTIER_AXIOMS.log; then
  echo "ERROR: sorryAx detected"
  exit 1
fi

python3 - <<'PY'
import re, sys
p="audit/GLOBAL_POSITIVE_FRONTIER_AXIOMS.log"
text=open(p,encoding="utf-8").read()
allowed={"propext","Classical.choice","Quot.sound"}
blocks=re.findall(r"depends on axioms:\s*\[([^\]]*)\]", text, flags=re.S)
if not blocks:
    print("ERROR: no axiom-audit blocks found")
    sys.exit(1)
bad=set()
for block in blocks:
    names={x.strip() for x in block.replace("\n"," ").split(",") if x.strip()}
    bad |= names-allowed
if bad:
    print("ERROR: unexpected axioms:", sorted(bad))
    sys.exit(1)
print("[GLOBAL-POSITIVE] allowed axioms only:", sorted(allowed))
PY

echo "[GLOBAL-POSITIVE] semantic firewalls"
grep -q 'positive_root_excludes_mixed_negative_root' "$SOURCE"
grep -q 'global_positive_root_iff_components' "$SOURCE"
grep -q 'rh_excludes_offCriticalZero' "$SOURCE"

echo "[GLOBAL-POSITIVE] GREEN"
