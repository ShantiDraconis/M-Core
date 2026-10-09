#!/usr/bin/env bash
set -euo pipefail
# MCORE_FINAL_GLOBAL v2 — fail-closed verifier.  Never promotes any state and
# never touches certs/final_external/* or ../v1 (reads them, re-runs gates on copies).
PKG="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$PKG/../../.." && pwd)"
cd "$PKG"

echo "[1/7] JSON syntax"
for f in CLOSED_MATH_GLOBAL_CERTIFICATE.json OPEN_MATH_GLOBAL_STATUS.json FINAL_GLOBAL_CERTIFICATE.json; do
  python3 -m json.tool "$f" >/dev/null
done

echo "[2/7] Payload hashes"
sha256sum -c SHA256SUMS
test "$(sha256sum SHA256SUMS | awk '{print $1}')" = "$(cat FINAL_GLOBAL_ROOT)"

echo "[3/7] v1 is untouched and superseded by reference"
(cd ../v1 && sha256sum -c --quiet SHA256SUMS)
test "$(sha256sum ../v1/SHA256SUMS | awk '{print $1}')" = "$(cat ../v1/FINAL_GLOBAL_ROOT)"

echo "[4/7] Cross-references and fail-closed invariants"
python3 - <<'PY'
import hashlib, json
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
g = json.load(open('FINAL_GLOBAL_CERTIFICATE.json'))
c = json.load(open('CLOSED_MATH_GLOBAL_CERTIFICATE.json'))
o = json.load(open('OPEN_MATH_GLOBAL_STATUS.json'))
assert g['closed_math']['sha256'] == h('CLOSED_MATH_GLOBAL_CERTIFICATE.json')
assert g['open_math']['sha256'] == h('OPEN_MATH_GLOBAL_STATUS.json')
assert g['supersedes']['sha256'] == h('../v1/FINAL_GLOBAL_CERTIFICATE.json')
ev = c['part_A_mcore_library']['axiom_evidence']
assert ev['tsv_sha256'] == h(ev['tsv'])
rows = [l.rstrip('\n').split('\t') for l in open(ev['tsv']) if l.startswith('THEOREM')]
assert len(rows) == ev['theorem_constants'] and all(r[1] == 'OK' for r in rows)
assert not [l for l in open(ev['tsv']) if l.startswith('USER_AXIOM')]
# lane closure is recomputed, never read
def closed(l):
    d = [x['demonstrated'] for x in l['obligations']]
    return all(d) if l['closes_when'] == 'all' else any(d)
n_closed = sum(closed(l) for l in o['lanes'])
assert n_closed == o['totals']['lanes_closed'] == 0
assert o['totals']['final_proof'] == g['state']['final_proof'] == c['final_proof'] == f'{n_closed}/7'
demo = [(l['lane'], x['id']) for l in o['lanes'] for x in l['obligations'] if x['demonstrated']]
assert demo == [('pVsNP', 'P01ConstructionGap')], demo
# every demonstrated obligation must be backed by a CLOSED_MATH entry with kernel evidence
b = {x['id']: x for x in c['part_B_cross_repository']}
for _, i in demo:
    e = b[i]
    assert e['state'] == 'CLOSED_GREEN_FROZEN_CERTIFIED' and e['audit']['run'] > 0
    assert e['theorem'].endswith(': P01FinalCertificate.P01ConstructionGap')
assert g['state']['FINAL_EXTERNAL_ISSUED'] is False and g['state']['FINAL_ROOT'] is None
print('invariants OK: lanes closed', n_closed, '| demonstrated', demo)
PY

echo "[5/7] Registry in Lean source agrees (no slot proved, 7 openMath)"
REG="$ROOT/lean/MCore/FinalProofRegistry.lean"
test "$(grep -c 'state := .openMath' "$REG")" = 7
test "$(grep -c 'state := .proved' "$REG")" = 0

echo "[6/7] FINAL_EXTERNAL v3 gate (on a copy) agrees with this package"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp -a "$ROOT/certs/final_external/." "$TMP/"
(cd "$TMP/v3" && bash freeze.sh >/dev/null)
cmp -s "$TMP/v3/PREPARATORY_ROOT" "$ROOT/certs/final_external/v3/PREPARATORY_ROOT"
python3 - "$ROOT" <<'PY'
import json, sys
m = json.load(open(sys.argv[1] + '/certs/final_external/v3/manifest.json'))
g = json.load(open('FINAL_GLOBAL_CERTIFICATE.json'))
assert g['final_external']['blockers'] == m['issuance_gate']['current_blockers']
assert g['final_external']['PREPARATORY_ROOT'] == open(sys.argv[1] + '/certs/final_external/v3/PREPARATORY_ROOT').read().strip()
assert m['issuance_gate']['FINAL_EXTERNAL_ISSUED'] is False
PY
test ! -e "$ROOT/certs/final_external/v3/FINAL_EXTERNAL_CERTIFICATE.json"

echo "[7/7] Result"
echo "RESULT=FINAL_GLOBAL_V2_INTEGRATION_STATE_VERIFIED"
echo "TERMINAL_MATH=0/7  OBLIGATIONS_DEMONSTRATED=1  TWO_GAP=1/2"
echo "FINAL_EXTERNAL_ISSUED=false"
