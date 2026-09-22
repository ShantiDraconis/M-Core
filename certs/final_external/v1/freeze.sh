#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

required_files=(
  manifest.json README.md provenance.json gate_ledger.json
  axiom_footprint.json reproducibility.md status.json revocation.json
)

for f in "${required_files[@]}"; do
  [[ -f "$f" ]] || { echo "FAIL: missing $f" >&2; exit 1; }
done

python3 - <<'PY'
import json, sys
from pathlib import Path

manifest = json.loads(Path("manifest.json").read_text())
status = json.loads(Path("status.json").read_text())
prov = json.loads(Path("provenance.json").read_text())

errors = []

def walk(x, path=""):
    if isinstance(x, dict):
        for k,v in x.items():
            walk(v, f"{path}.{k}" if path else k)
    elif isinstance(x, list):
        for i,v in enumerate(x):
            walk(v, f"{path}[{i}]")
    elif x == "UNSET" or (isinstance(x, str) and x.startswith("UNSET_")):
        errors.append(path)

# Fail closed on release-critical sections only.
for section in ("human_review","production","G3"):
    walk(manifest.get(section), section)

if manifest.get("G3", {}).get("status") == "OPEN_CONSTRUCTION":
    errors.append("G3.status")

if status.get("issuance", {}).get("FINAL_EXTERNAL_ISSUED") is not False:
    print("FAIL: preparatory freeze requires FINAL_EXTERNAL_ISSUED=false", file=sys.stderr)
    sys.exit(1)

for repo_name, rec in prov.get("repositories", {}).items():
    if rec.get("optional") is True:
        continue
    for key in ("repo","branch","sha"):
        v=rec.get(key)
        if v is None or (isinstance(v,str) and v.startswith("UNSET")):
            errors.append(f"provenance.repositories.{repo_name}.{key}")

if errors:
    print("FAIL_CLOSED: unresolved fields:", file=sys.stderr)
    for e in sorted(set(errors)):
        print(f"  - {e}", file=sys.stderr)
    sys.exit(2)

print("RELEASE_FIELDS_RESOLVED=PASS")
PY

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

sha256sum   manifest.json README.md provenance.json gate_ledger.json   axiom_footprint.json reproducibility.md status.json revocation.json   freeze.sh > "$tmp"

mv "$tmp" SHA256SUMS

PACKAGE_ROOT="$(sha256sum SHA256SUMS | awk '{print $1}')"
printf '%s  SHA256SUMS\n' "$PACKAGE_ROOT" > ROOT.sha256

echo "SHA256SUMS=GENERATED"
echo "PACKAGE_ROOT=$PACKAGE_ROOT"
echo "NOTE: ROOT.sha256 is the package-root hash. The issued layer-root must additionally use exact frozen component anchors from provenance.json."
