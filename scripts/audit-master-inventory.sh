#!/usr/bin/env bash
set -euo pipefail

lake build MCore.Audit.MasterCertificate
lake build

if grep -RInE '\b(sorry|admit|sorryAx)\b' --include='*.lean'   lean/MCore/Canonical   lean/MCore/Reuse   lean/MCore/Problems   lean/MCore/OpenMath   lean/MCore/Audit; then
  echo "MASTER_INVENTORY_HYGIENE_RED"
  exit 1
fi

echo "MASTER_INVENTORY_BUILD_GREEN"
echo "MASTER_INVENTORY_HYGIENE_GREEN"
