#!/usr/bin/env bash
set -euo pipefail

PKG="certs/final_external/v1"
MANIFEST="$PKG/manifest.json"
STATUS="$PKG/status.json"
PREP="$PKG/PREPARATORY_ROOT"
OUT="$PKG/FINAL_CLAIM_GATE.json"

python3 - "$MANIFEST" "$STATUS" "$PREP" "$OUT" <<'PY'
import json,sys
manifest=json.load(open(sys.argv[1]))
status=json.load(open(sys.argv[2]))
prep=open(sys.argv[3]).read().strip()
out_path=sys.argv[4]

reasons=[]
fp=manifest["final_proof"]["display"]
if fp != "7/7":
    reasons.append(f"FINAL_PROOF={fp}")
if manifest["math_state"].startswith("OPEN_MATH"):
    reasons.append(f"MATH_STATE={manifest['math_state']}")
if manifest["issuance_gate"]["FINAL_EXTERNAL_ISSUED"] is not True:
    reasons.append("FINAL_EXTERNAL_ISSUED=false")
if manifest["human_review"]["authority"] == "UNSET":
    reasons.append("HUMAN_REVIEW=UNSET")
if manifest["production"]["app"]["app_repository"] == "UNSET":
    reasons.append("APP=UNSET")
if manifest["production"]["crypto"]["crypto_provider"] == "UNSET":
    reasons.append("CRYPTO=UNSET")
if manifest["production"]["hardware_attestation"]["status"] == "UNSET":
    reasons.append("HARDWARE=UNSET")

out={
  "schema":"atk.final-claim-gate.v1",
  "preparatory_root":prep,
  "final_root":None,
  "final_proof":fp,
  "external_claim":"BLOCKED" if reasons else "ELIGIBLE_FOR_FINAL_ROOT",
  "reasons":reasons,
  "policy":"FINAL_ROOT and EXTERNAL_PROVED require 7/7 material producers plus all issuance gates; ATK/truncation status alone cannot promote external mathematics."
}
open(out_path,"w").write(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
print("CLAIM_BLOCKED" if reasons else "CLAIM_ELIGIBLE")
PY
