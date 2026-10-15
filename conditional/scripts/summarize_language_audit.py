#!/usr/bin/env python3
"""Summarize ATK language scan without equating term occurrences with errors.

Usage: python3 summarize_language_audit.py audit-language.csv --output language-summary.json
The exact CHANGE_REQUIRED count is only meaningful after human review of every
candidate, including a decision on whether copies across refs count separately.
"""
import argparse
import collections
import csv
import json
from pathlib import Path

STATES = {"REVIEW", "CORRECT", "CHANGE_REQUIRED", "FALSE_POSITIVE"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("--output", type=Path, default=Path("language-summary.json"))
    args = ap.parse_args()
    rows = list(csv.DictReader(args.input.open(encoding="utf-8", newline="")))
    required = {"repo", "ref", "commit", "path", "line", "term", "review_status"}
    if not rows:
        raise SystemExit("No findings: verify scanner completion and coverage before claiming zero errors")
    if not required.issubset(rows[0]):
        raise SystemExit("Missing columns: " + ", ".join(sorted(required - set(rows[0]))))
    unknown = sorted({r["review_status"] for r in rows} - STATES)
    if unknown:
        raise SystemExit("Unknown review states: " + repr(unknown))
    files = lambda subset: {(r["repo"], r["ref"], r["path"]) for r in subset}
    by_state = {s: [r for r in rows if r["review_status"] == s] for s in sorted(STATES)}
    pending = by_state["REVIEW"]
    result = {
        "scope": "Only the input CSV, not automatically all repositories and branches",
        "occurrences_total": len(rows),
        "files_with_matches_by_repo_ref_path": len(files(rows)),
        "reviewed_occurrences": len(rows) - len(pending),
        "unreviewed_occurrences": len(pending),
        "change_required_occurrences": len(by_state["CHANGE_REQUIRED"]),
        "change_required_files_by_repo_ref_path": len(files(by_state["CHANGE_REQUIRED"])),
        "unique_repo_path_with_change_required": len({(r["repo"], r["path"]) for r in by_state["CHANGE_REQUIRED"]}),
        "occurrences_by_status": {s: len(v) for s, v in by_state.items()},
        "exact_global_error_count_certified": False,
        "reason": "Must verify all repository refs were scanned and every candidate was reviewed",
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
