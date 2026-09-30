#!/usr/bin/env python3
"""
Fail-closed validator for the M-Core master terminal manifest.

This script does not promote mathematical claims. It only checks that:
- every owned repository is inventoried;
- exactly seven repositories are terminal lanes;
- terminal credit is granted only when the full closure contract is present;
- the declared global 0/7..7/7 state matches the lane data.

A GREEN run of this script means the manifest is internally honest.
It does NOT mean the seven mathematical endpoints are proved.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "master-terminal" / "manifest.json"
INVENTORY = ROOT / "master-terminal" / "owned_repositories.json"

EXPECTED_SLOTS = {
    "RIEMANN",
    "P_VS_NP",
    "BSD",
    "HODGE",
    "YANG_MILLS",
    "BEAL",
    "NAVIER_STOKES",
}

FORBIDDEN_ROLE_CREDIT = {"source_or_support", "orchestrator"}


def fail(msg: str) -> None:
    raise SystemExit(f"MASTER_TERMINAL_MANIFEST_RED: {msg}")


def load(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"cannot load {path}: {exc}")


def terminal_closed(lane: dict) -> bool:
    term = lane.get("terminal", {})
    if not term.get("nonempty", False):
        return False

    run = lane.get("latest_observed_run", {})
    build = lane.get("build_state")
    checks = {
        "kernel_checked": term.get("kernel_checked") is True,
        "official_consumer_linked": term.get("official_consumer_linked") is True,
        "theorem_named": bool(term.get("theorem")),
        "successful_run": run.get("conclusion") == "success",
        "source_sha": bool(run.get("sha")),
        "build_green": build in {"GREEN", "CERTIFIED", "GREEN_FROZEN", "GREEN_FROZEN_CERTIFIED"},
        "sorry_count_zero": term.get("sorry_count") == 0,
        "admit_count_zero": term.get("admit_count") == 0,
        "sorryAx_count_zero": term.get("sorryAx_count") == 0,
        "prohibited_axioms_zero": term.get("prohibited_axioms") in ([], None),
        "hidden_oracle_false": term.get("hidden_oracle") is False,
    }
    bad = [k for k, ok in checks.items() if not ok]
    if bad:
        fail(
            f"{lane.get('slot')} claims a terminal inhabitant but closure contract is incomplete: "
            + ", ".join(bad)
        )
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-done",
        action="store_true",
        help="exit nonzero unless all seven terminal lanes are closed",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable status only",
    )
    args = parser.parse_args()

    manifest = load(MANIFEST)
    inventory = load(INVENTORY)

    repos = inventory.get("repositories", [])
    declared_count = inventory.get("count")
    if declared_count != len(repos):
        fail(f"inventory count mismatch: declared={declared_count} actual={len(repos)}")

    names = [r.get("repo") for r in repos]
    if any(not n for n in names):
        fail("inventory contains a repository without a name")
    if len(names) != len(set(names)):
        fail("inventory contains duplicate repository names")

    roles = {r["repo"]: r.get("role") for r in repos}
    credits = {r["repo"]: r.get("terminal_credit", 0) for r in repos}

    for repo, role in roles.items():
        if role in FORBIDDEN_ROLE_CREDIT and credits[repo] != 0:
            fail(f"non-terminal repository has terminal credit: {repo}")

    lanes = manifest.get("lanes", [])
    if len(lanes) != 7:
        fail(f"expected 7 terminal lanes, found {len(lanes)}")

    slots = [l.get("slot") for l in lanes]
    if set(slots) != EXPECTED_SLOTS or len(slots) != len(set(slots)):
        fail(f"terminal slot set mismatch: {slots}")

    lane_repos = [l.get("operational_repo") for l in lanes]
    if len(lane_repos) != len(set(lane_repos)):
        fail("two terminal slots point to the same operational repository")

    for lane in lanes:
        repo = lane.get("operational_repo")
        if repo not in roles:
            fail(f"terminal lane repository is absent from owned inventory: {repo}")
        if roles[repo] != "terminal_lane":
            fail(f"terminal lane repository has wrong inventory role: {repo} -> {roles[repo]}")

    inventory_terminal = {r["repo"] for r in repos if r.get("role") == "terminal_lane"}
    if inventory_terminal != set(lane_repos):
        fail(
            "inventory terminal-lane set differs from manifest: "
            f"inventory={sorted(inventory_terminal)} manifest={sorted(lane_repos)}"
        )

    closed_slots = []
    for lane in lanes:
        closed = terminal_closed(lane)
        declared_credit = lane.get("terminal_credit", 0)
        expected_credit = 1 if closed else 0
        if declared_credit != expected_credit:
            fail(
                f"{lane['slot']} terminal_credit mismatch: "
                f"declared={declared_credit} expected={expected_credit}"
            )
        if closed:
            closed_slots.append(lane["slot"])

    closed_count = len(closed_slots)
    computed_final = f"{closed_count}/7"
    declared_global = manifest.get("global", {})
    if declared_global.get("terminal_inhabitants") != closed_count:
        fail(
            "global terminal_inhabitants mismatch: "
            f"declared={declared_global.get('terminal_inhabitants')} computed={closed_count}"
        )
    if declared_global.get("final_proof") != computed_final:
        fail(
            f"global final_proof mismatch: declared={declared_global.get('final_proof')} "
            f"computed={computed_final}"
        )

    computed_state = "DONE" if closed_count == 7 else "OPEN"
    if declared_global.get("state") != computed_state:
        fail(
            f"global state mismatch: declared={declared_global.get('state')} "
            f"computed={computed_state}"
        )

    if computed_state == "DONE" and not declared_global.get("final_root"):
        fail("DONE requires a non-null final_root")
    if computed_state != "DONE" and declared_global.get("final_root") is not None:
        fail("OPEN state must not advertise a final_root")

    report = {
        "schema": "mcore.master-terminal-status.v1",
        "inventory_count": len(repos),
        "terminal_slots": 7,
        "closed_slots": closed_slots,
        "open_slots": [s for s in slots if s not in closed_slots],
        "final_proof": computed_final,
        "state": computed_state,
        "manifest_valid": True,
        "meaning": (
            "Manifest structure is fail-closed and internally consistent. "
            "This status is not a mathematical proof."
        ),
    }

    if args.json:
        print(json.dumps(report, sort_keys=True))
    else:
        print("MASTER_TERMINAL_MANIFEST_GREEN")
        print(f"OWNED_REPOSITORIES={len(repos)}")
        print(f"FINAL_PROOF={computed_final}")
        print(f"GLOBAL_STATE={computed_state}")
        print("CLOSED=" + (",".join(closed_slots) if closed_slots else "NONE"))
        print("OPEN=" + ",".join(report["open_slots"]))

    if args.require_done and computed_state != "DONE":
        print(
            "MASTER_TERMINAL_CLOSURE_OPEN: --require-done requested but not all "
            "terminal inhabitants exist.",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
