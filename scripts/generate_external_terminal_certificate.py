#!/usr/bin/env python3
"""
Fail-closed issuer for the seven-lane external terminal certificate.

No certificate is emitted while any canonical terminal inhabitant is absent.
The FINAL_ROOT is a SHA-256 commitment to the seven terminal evidence records
only after the master manifest is in DONE / 7-of-7 state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "master-terminal" / "manifest.json"
OUT = ROOT / "master-terminal" / "EXTERNAL_CERTIFICATE.json"


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def load() -> dict:
    return json.loads(MANIFEST.read_text())


def evidence_for_lane(lane: dict) -> dict:
    term = lane.get("terminal", {})
    run = lane.get("latest_observed_run", {})
    return {
        "slot": lane.get("slot"),
        "repo": lane.get("operational_repo"),
        "theorem": term.get("theorem"),
        "sha": run.get("sha"),
        "run_id": run.get("id"),
        "kernel_checked": term.get("kernel_checked"),
        "official_consumer_linked": term.get("official_consumer_linked"),
        "sorry_count": term.get("sorry_count"),
        "admit_count": term.get("admit_count"),
        "sorryAx_count": term.get("sorryAx_count"),
        "prohibited_axioms": term.get("prohibited_axioms"),
        "hidden_oracle": term.get("hidden_oracle"),
        "terminal_credit": lane.get("terminal_credit"),
    }


def validate_done(m: dict) -> list[dict]:
    g = m.get("global", {})
    lanes = m.get("lanes", [])
    if len(lanes) != 7:
        raise SystemExit("EXTERNAL_CERTIFICATE_BLOCKED: expected exactly seven lanes")
    if g.get("state") != "DONE":
        raise SystemExit("EXTERNAL_CERTIFICATE_BLOCKED: master state is not DONE")
    if g.get("terminal_inhabitants") != 7 or g.get("final_proof") != "7/7":
        raise SystemExit("EXTERNAL_CERTIFICATE_BLOCKED: terminal count is not 7/7")

    evidence = []
    for lane in lanes:
        term = lane.get("terminal", {})
        run = lane.get("latest_observed_run", {})
        checks = {
            "terminal_credit": lane.get("terminal_credit") == 1,
            "nonempty": term.get("nonempty") is True,
            "kernel_checked": term.get("kernel_checked") is True,
            "official_consumer_linked": term.get("official_consumer_linked") is True,
            "theorem": bool(term.get("theorem")),
            "success": run.get("conclusion") == "success",
            "sha": bool(run.get("sha")),
            "run_id": bool(run.get("id")),
            "sorry_count": term.get("sorry_count") == 0,
            "admit_count": term.get("admit_count") == 0,
            "sorryAx_count": term.get("sorryAx_count") == 0,
            "prohibited_axioms": term.get("prohibited_axioms") in ([], None),
            "hidden_oracle": term.get("hidden_oracle") is False,
        }
        bad = [k for k, ok in checks.items() if not ok]
        if bad:
            raise SystemExit(
                f"EXTERNAL_CERTIFICATE_BLOCKED: {lane.get('slot')} incomplete: "
                + ",".join(bad)
            )
        evidence.append(evidence_for_lane(lane))
    return evidence


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--issue", action="store_true")
    ap.add_argument(
        "--expect-blocked",
        action="store_true",
        help="succeed only when current manifest correctly blocks issuance",
    )
    args = ap.parse_args()

    m = load()
    try:
        evidence = validate_done(m)
    except SystemExit as exc:
        if args.expect_blocked:
            print(str(exc))
            print("EXTERNAL_CERTIFICATE_FAIL_CLOSED_GREEN")
            return 0
        raise

    if args.expect_blocked:
        raise SystemExit("EXTERNAL_CERTIFICATE_RED: issuance unexpectedly became eligible")

    commitment = {
        "schema": "mcore.external-terminal-certificate.v1",
        "terminal_evidence": evidence,
    }
    final_root = hashlib.sha256(canonical_bytes(commitment)).hexdigest()
    cert = {
        **commitment,
        "FINAL_PROOF": "7/7",
        "FINAL_EXTERNAL_ISSUED": True,
        "FINAL_ROOT": final_root,
        "source_manifest": "master-terminal/manifest.json",
    }

    if not args.issue:
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 0

    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(f"EXTERNAL_CERTIFICATE_ISSUED={OUT}")
    print(f"FINAL_ROOT={final_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
