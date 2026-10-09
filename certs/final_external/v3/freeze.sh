#!/usr/bin/env bash
set -euo pipefail
# ELYON_FINAL_EXTERNAL v3.0.0 / package revision v3.0.0-preparatory
# FAIL-CLOSED PREPARATORY freeze. SUPERSEDES v2 (v1 and v2 are read, never modified).
# Never emits FINAL_ROOT or ISSUED.  As v2, plus:
#   * P01 closure must carry kernel evidence (theorem, SHAs, run, axioms).
# Differences of v2 from v1:
#   * blockers are DERIVED from the data and checked against the manifest
#     (v1 hard-coded the list, so it could never accept a closed gate);
#   * the issuance condition text is asserted IDENTICAL to v1 (gate meaning
#     unchanged);
#   * v1's PREPARATORY_ROOT is re-derived and must match the supersession record.
PACKAGE_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PACKAGE_DIR"
V1="$PACKAGE_DIR/../v1"
V2="$PACKAGE_DIR/../v2"
echo "[freeze.sh v3] $PACKAGE_DIR - PREPARATORY_NOT_ISSUED"
JSON_FILES=(manifest.json status.json provenance.json gate_ledger.json axiom_footprint.json revocation.json MATH_TERMINAL_BOUNDARY_20261009.json)
PAYLOAD=(manifest.json README.md provenance.json gate_ledger.json axiom_footprint.json reproducibility.md status.json MATH_TERMINAL_BOUNDARY_20261009.json revocation.json freeze.sh)

echo "[1/9] JSON syntax"
for f in "${JSON_FILES[@]}"; do python3 -m json.tool "$f" >/dev/null; done

echo "[2/9] Fail-closed Lean-source hygiene if Lean files are present"
if find . -type f -name '*.lean' -print -quit | grep -q .; then
  if grep -R -n -E '(^|[^[:alnum:]_])(sorry|admit|sorryAx)([^[:alnum:]_]|$)' --include='*.lean' .; then
    echo 'FAIL forbidden proof escape'; exit 1
  fi
fi

echo "[3/9] Supersession of v2 is consistent; v1 and v2 are untouched"
test "$(sha256sum "$V1/SHA256SUMS" | awk '{print $1}')" = "$(cat "$V1/PREPARATORY_ROOT")"
(cd "$V1" && sha256sum -c --quiet SHA256SUMS)
test "$(sha256sum "$V2/SHA256SUMS" | awk '{print $1}')" = "$(cat "$V2/PREPARATORY_ROOT")"
(cd "$V2" && sha256sum -c --quiet SHA256SUMS)
V2ROOT="$(cat "$V2/PREPARATORY_ROOT")" python3 - <<'PY'
import json, os
m = json.load(open('manifest.json')); v1 = json.load(open('../v1/manifest.json'))
assert m['supersedes']['version'] == 'v2.0.0'
assert m['supersedes']['v2_preparatory_root'] == os.environ['V2ROOT']
assert m['supersedes']['v1_mutated'] is False and m['supersedes']['v2_mutated'] is False
assert m['issuance_gate']['condition'] == v1['issuance_gate']['condition'], 'issuance condition changed'
# a closed gap must carry its kernel evidence
c = m['anchors']['P01']['closure']
assert c['state'] == 'CLOSED_GREEN_FROZEN_CERTIFIED'
assert c['theorem'].endswith(': P01FinalCertificate.P01ConstructionGap')
assert len(c['source_sha']) == 40 and len(c['audit']['source_sha']) == 40 and c['audit']['run'] > 0
assert any('axioms [propext, Classical.choice, Quot.sound]' in x for x in c['audit']['checks'])
PY

echo "[4/9] Normative preparatory state"
python3 - <<'PY'
import json
m = json.load(open('manifest.json')); s = json.load(open('status.json'))
assert m['package_state'] == 'PREPARATORY'
assert m['public_status'] == 'PREPARATORY_NOT_ISSUED'
assert m['issuance_gate']['FINAL_EXTERNAL_ISSUED'] is False
assert s['issuance']['FINAL_EXTERNAL_ISSUED'] is False
assert m['root']['FINAL_ROOT'] is None and m['root']['PREPARATORY_ROOT'] is None
assert s['final_proof'] == '0/7' and m['final_proof']['display'] == '0/7'
assert m['final_proof']['taxonomy']['GLOBAL_7_PROBLEMS'] == '0/7'
assert m['final_proof']['taxonomy']['P_VS_NP_ENDPOINT'] == 'OPEN'
PY

echo "[5/9] Blockers derived from data (same rules as v1)"
python3 - <<'PY'
import json
m = json.load(open('manifest.json'))
b = json.load(open('MATH_TERMINAL_BOUNDARY_20261009.json'))
blockers = []
if 'P01ConstructionGap' in b.get('open_gaps', []): blockers.append('P01ConstructionGap')
if 'G21Pointwise' in b.get('open_gaps', []): blockers.append('G21Pointwise')
if m['G3']['status'] != 'CLOSED_GREEN_FROZEN_CERTIFIED': blockers.append('G3')
if m['human_review']['authority'] == 'UNSET': blockers.append('human_review')
if m['production']['app']['app_repository'] == 'UNSET': blockers.append('app')
if m['production']['crypto']['crypto_provider'] == 'UNSET': blockers.append('crypto')
if m['production']['hardware_attestation']['status'] == 'UNSET': blockers.append('hardware')
assert m['production']['hardware_attestation']['status'] in m['production']['hardware_attestation']['allowed_values']
assert blockers == m['issuance_gate']['current_blockers'], (blockers, m['issuance_gate']['current_blockers'])
assert blockers, 'all gates closed: v3 is preparatory and cannot issue; prepare a signed v4 with human approval'
print('blockers:', blockers)
PY

echo "[6/9] Generate canonical PACKAGE_SHA256SUMS"
rm -f SHA256SUMS PREPARATORY_ROOT
sha256sum "${PAYLOAD[@]}" > SHA256SUMS

echo "[7/9] Generate PREPARATORY_ROOT out-of-band"
sha256sum SHA256SUMS | awk '{print $1}' > PREPARATORY_ROOT
cat PREPARATORY_ROOT

echo "[8/9] Re-verify payload was not mutated"
sha256sum -c SHA256SUMS

echo "[9/9] FINAL_ROOT remains null / issuance remains false"
python3 - <<'PY'
import json
m = json.load(open('manifest.json')); s = json.load(open('status.json'))
assert m['root']['FINAL_ROOT'] is None
assert m['issuance_gate']['FINAL_EXTERNAL_ISSUED'] is False
assert s['issuance']['FINAL_EXTERNAL_ISSUED'] is False
PY

echo 'RESULT=FROZEN_PREPARATORY_V3'
echo 'FINAL_EXTERNAL_ISSUED=false'
