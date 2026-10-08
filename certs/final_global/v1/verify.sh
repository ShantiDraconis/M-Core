#!/usr/bin/env bash
set -euo pipefail
# MCORE_FINAL_GLOBAL v1 — fail-closed verifier.
# Re-checks the package; never promotes any state and never touches
# certs/final_external/v1 (it only reads it and re-runs freeze.sh on a copy).
PKG="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$PKG/../../.." && pwd)"
cd "$PKG"
PAYLOAD=(CLOSED_MATH_GLOBAL_CERTIFICATE.json OPEN_MATH_GLOBAL_STATUS.json FINAL_GLOBAL_CERTIFICATE.json
         SOURCE_INVENTORY.json FINAL_EXTERNAL_BLOCKERS.md GLOBAL_AXIOM_AUDIT.md GLOBAL_KERNEL_RUNS.md
         axiom_audit_run37819802090.tsv verify.sh)

echo "[1/6] JSON syntax"
for f in CLOSED_MATH_GLOBAL_CERTIFICATE.json OPEN_MATH_GLOBAL_STATUS.json FINAL_GLOBAL_CERTIFICATE.json SOURCE_INVENTORY.json; do
  python3 -m json.tool "$f" >/dev/null
done

echo "[2/6] Payload hashes"
sha256sum -c SHA256SUMS
test "$(sha256sum SHA256SUMS | awk '{print $1}')" = "$(cat FINAL_GLOBAL_ROOT)"

echo "[3/6] Cross-references and fail-closed invariants"
python3 - <<'PY'
import hashlib, json
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
g = json.load(open('FINAL_GLOBAL_CERTIFICATE.json'))
c = json.load(open('CLOSED_MATH_GLOBAL_CERTIFICATE.json'))
o = json.load(open('OPEN_MATH_GLOBAL_STATUS.json'))
assert g['closed_math']['sha256'] == h('CLOSED_MATH_GLOBAL_CERTIFICATE.json')
assert g['open_math']['sha256'] == h('OPEN_MATH_GLOBAL_STATUS.json')
assert g['source_repositories']['sha256'] == h('SOURCE_INVENTORY.json')
assert g['final_external']['blockers_sha256'] == h('FINAL_EXTERNAL_BLOCKERS.md')
assert c['axiom_evidence']['tsv_sha256'] == h('axiom_audit_run37819802090.tsv')
# fail-closed: nothing terminal may be claimed while any obligation is open
demonstrated = sum(ob['demonstrated'] for l in o['lanes'] for ob in l['obligations'])
total = sum(len(l['obligations']) for l in o['lanes'])
assert (demonstrated, total) == (o['totals']['demonstrated'], o['totals']['terminal_obligations'])
assert c['terminal_endpoints_closed'] == 0 and c['final_proof'] == '0/7'
assert g['state']['final_proof'] == '0/7' and g['state']['terminal_math_closure'] == 'OPEN'
assert g['state']['FINAL_EXTERNAL_ISSUED'] is False and g['state']['FINAL_ROOT'] is None
assert g['final_external']['issued'] is False
# axiom evidence
rows = [l.rstrip('\n').split('\t') for l in open('axiom_audit_run37819802090.tsv') if l.startswith('THEOREM')]
assert len(rows) == c['counts']['theorem_constants']
assert not [r for r in rows if r[1] != 'OK']
assert not [l for l in open('axiom_audit_run37819802090.tsv') if l.startswith('USER_AXIOM')]
print('invariants OK: demonstrated', demonstrated, 'of', total)
PY

echo "[4/6] Registry in Lean source agrees (provedCount = 0, 7 openMath slots)"
REG="$ROOT/lean/MCore/FinalProofRegistry.lean"
test "$(grep -c 'state := .openMath' "$REG")" = 7
test "$(grep -c 'state := .proved' "$REG")" = 0

echo "[5/6] FINAL_EXTERNAL v1 preparatory gate (on a copy)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp -a "$ROOT/certs/final_external/v1/." "$TMP/"
(cd "$TMP" && bash freeze.sh >/dev/null)
cmp -s "$TMP/PREPARATORY_ROOT" "$ROOT/certs/final_external/v1/PREPARATORY_ROOT"
test ! -e FINAL_EXTERNAL_CERTIFICATE.json

echo "[6/6] Result"
echo "RESULT=FINAL_GLOBAL_INTEGRATION_STATE_VERIFIED"
echo "TERMINAL_MATH=0/7"
echo "FINAL_EXTERNAL_ISSUED=false"
