#!/usr/bin/env bash
set -euo pipefail

echo "[external-material-gate] strict external-proof policy"

LEAN_ROOT="${1:-lean}"

if [ ! -d "$LEAN_ROOT" ]; then
  echo "FAIL missing Lean root: $LEAN_ROOT"
  exit 1
fi

echo "[1/6] proof escapes"
if grep -RInE '(^|[^[:alnum:]_])(sorry|admit|sorryAx)([^[:alnum:]_]|$)' --include='*.lean' "$LEAN_ROOT"; then
  echo "FAIL proof escape"
  exit 1
fi

echo "[2/6] effectful / opaque proof escapes"
if grep -RInE '(^|[^[:alnum:]_])(unsafe|native_decide|implemented_by)([^[:alnum:]_]|$)|IO\.FS\.|\bIO\b' --include='*.lean' "$LEAN_ROOT"; then
  echo "FAIL effectful proof path"
  exit 1
fi

echo "[3/6] custom theorem-carrying axioms"
if grep -RInE '^[[:space:]]*axiom[[:space:]]+' --include='*.lean' "$LEAN_ROOT"; then
  echo "FAIL custom axiom declaration"
  exit 1
fi

echo "[4/6] external promotion guard source"
test -f lean/MCore/ExternalPromotionGuard.lean
grep -q 'search_is_material : searchStatus = .closedByMaterialProducer' lean/MCore/ExternalPromotionGuard.lean
grep -q 'truncation_cannot_be_external_proved' lean/MCore/ExternalPromotionGuard.lean
grep -q 'atk_status_alone_does_not_produce_external' lean/MCore/ExternalPromotionGuard.lean

echo "[5/6] truncation law may not fabricate target"
test -f lean/MCore/KernelTruncationLaw.lean
grep -q 'MaterialExtractor' lean/MCore/KernelTruncationLaw.lean
grep -q 'target_closed_of_truncation_and_extractor' lean/MCore/KernelTruncationLaw.lean

echo "[6/6] actions remain zero in external certificate model"
grep -q 'ioActionCount : Nat' lean/MCore/ExternalPromotionGuard.lean
grep -q 'ioActionCount = 0' lean/MCore/ExternalPromotionGuard.lean

echo "EXTERNAL_MATERIAL_GATE=GREEN"
