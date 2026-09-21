#!/usr/bin/env bash
set -euo pipefail

lake update
lake build MCoreAudit 2>&1 | tee build.log
python3 scripts/kernel_audit.py | tee audit.log
lake env lean lean/MCore/KernelBuild.lean 2>&1 | tee kernel.log

grep -q "PROOF_GAP_HITS: 0" audit.log

echo "SOURCE_BUILD=GREEN"
echo "CERTIFIED=NO (requires pinned commit SHA + provenance/audit seal)"
echo "POINCARE_FORMAL_IMPORT=PENDING"
echo "ERROR_INVARIANCE=OPEN"
echo "NS_G5_1=OPEN_MATH"
echo "NS_G5_2=OPEN_MATH"
echo "NS_SEMANTIC_ADAPTER=OPEN"
echo "FINAL_PROOF=0/7"
