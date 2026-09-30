#!/usr/bin/env bash
set -euo pipefail

PACKAGE_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PACKAGE_DIR"

echo "[finalize_root.sh] fail-closed FINAL_ROOT gate"

python3 <<'PY'
import json, sys
m=json.load(open('manifest.json'))
s=json.load(open('status.json'))
b=json.load(open('MATERIAL_ONLY_BOUNDARY_20260930.json'))

errors=[]
math_root=s.get('normative_state',{}).get('FINAL_ROOT_MATH')
if not math_root:
    errors.append('FINAL_ROOT_MATH is null')

material=b.get('p_vs_np_final_external',{}).get('material_blockers',[])
mechanical=b.get('p_vs_np_final_external',{}).get('mechanical_blockers',[])
if material:
    errors.append('material blockers remain: ' + ', '.join(material))
if mechanical:
    errors.append('mechanical blockers remain: ' + ', '.join(mechanical))

hr=m.get('human_review',{})
for k in ('authority','quorum','evidence_policy'):
    if hr.get(k) in (None,'','UNSET'):
        errors.append('human_review.'+k+' is UNSET')

prod=m.get('production',{})
app=prod.get('app',{})
crypto=prod.get('crypto',{})
hw=prod.get('hardware_attestation',{})
if app.get('app_repository') in (None,'','UNSET'):
    errors.append('production.app.app_repository is UNSET')
if app.get('app_commit') in (None,'','UNSET'):
    errors.append('production.app.app_commit is UNSET')
if crypto.get('crypto_provider') in (None,'','UNSET'):
    errors.append('production.crypto.crypto_provider is UNSET')
if crypto.get('public_key_or_key_id') in (None,'','UNSET'):
    errors.append('production.crypto.public_key_or_key_id is UNSET')
if hw.get('status') in (None,'','UNSET'):
    errors.append('production.hardware_attestation.status is UNSET')

if m.get('G3',{}).get('status') != 'CLOSED_GREEN_FROZEN_CERTIFIED':
    errors.append('G3 is not CLOSED_GREEN_FROZEN_CERTIFIED')

if errors:
    print('FINAL_ROOT_BLOCKED')
    for e in errors:
        print(' -', e)
    sys.exit(2)

print('FINAL_ROOT_PREREQUISITES_GREEN')
PY

FINAL_PAYLOAD=(
  manifest.json
  status.json
  provenance.json
  gate_ledger.json
  axiom_footprint.json
  reproducibility.md
  MATERIAL_ONLY_BOUNDARY_20260930.json
  FINAL_ROOT_CLOSURE_PLAN_20260930.json
  revocation.json
)

rm -f FINAL_SHA256SUMS FINAL_ROOT
sha256sum "${FINAL_PAYLOAD[@]}" > FINAL_SHA256SUMS
sha256sum -c FINAL_SHA256SUMS
sha256sum FINAL_SHA256SUMS | awk '{print $1}' > FINAL_ROOT

echo "FINAL_ROOT=$(cat FINAL_ROOT)"
echo "RESULT=FINAL_ROOT_COMPUTED_NOT_ISSUED"
echo "FINAL_EXTERNAL_ISSUED=false"
