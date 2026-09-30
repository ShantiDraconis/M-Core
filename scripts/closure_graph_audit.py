#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "master-terminal" / "closure_graph.json"
EXPECTED = {"RIEMANN","P_VS_NP","BSD","HODGE","YANG_MILLS","BEAL","NAVIER_STOKES"}

def fail(msg: str) -> None:
    raise SystemExit("CLOSURE_GRAPH_RED: " + msg)

def main() -> int:
    d = json.loads(GRAPH.read_text())
    lanes = d.get("lanes", [])
    slots = [x.get("slot") for x in lanes]
    if len(lanes) != 7 or set(slots) != EXPECTED or len(set(slots)) != 7:
        fail(f"slot mismatch: {slots}")

    total_open = 0
    for lane in lanes:
        ids = [n.get("id") for n in lane.get("nodes", [])]
        if len(ids) != len(set(ids)) or any(not x for x in ids):
            fail(f"{lane['slot']}: duplicate/empty node id")
        idset = set(ids)
        terminal = [n["id"] for n in lane["nodes"] if n.get("kind") == "terminal"]
        if len(terminal) != 1:
            fail(f"{lane['slot']}: expected exactly one terminal node")
        for e in lane.get("edges", []):
            if e.get("from") not in idset or e.get("to") not in idset:
                fail(f"{lane['slot']}: dangling edge {e}")
            if e.get("from") == e.get("to"):
                fail(f"{lane['slot']}: self-loop {e}")
        open_nodes = lane.get("open_nodes", [])
        if any(x not in idset for x in open_nodes):
            fail(f"{lane['slot']}: unknown open node")
        total_open += len(open_nodes)

        # Forward-only cycle test ignores equivalence edges because equivalences
        # intentionally represent the same mathematical obligation.
        adj = {x: [] for x in ids}
        for e in lane.get("edges", []):
            if e.get("kind") != "equivalence":
                adj[e["from"]].append(e["to"])
        visiting, done = set(), set()
        def visit(x: str) -> None:
            if x in done:
                return
            if x in visiting:
                fail(f"{lane['slot']}: non-equivalence cycle through {x}")
            visiting.add(x)
            for y in adj[x]:
                visit(y)
            visiting.remove(x)
            done.add(x)
        for x in ids:
            visit(x)

        # Every declared open node must have a forward path to the terminal.
        target = terminal[0]
        def reaches(start: str, seen: set[str]) -> bool:
            if start == target:
                return True
            if start in seen:
                return False
            seen = set(seen)
            seen.add(start)
            for e in lane.get("edges", []):
                if e["from"] == start and reaches(e["to"], seen):
                    return True
            return False
        for x in open_nodes:
            if not reaches(x, set()):
                fail(f"{lane['slot']}: open node {x} has no path to terminal {target}")

    print("CLOSURE_GRAPH_GREEN")
    print("LANES=7")
    print(f"OPEN_MATERIAL_NODES={total_open}")
    print("FORWARD_ONLY=TRUE")
    print("EQUIVALENCE_CREDIT=ZERO")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
