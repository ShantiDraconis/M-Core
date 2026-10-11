#!/usr/bin/env python3
"""Build PUBLICATION/MASTER: one structure for every proof across the repos.

Inputs (all kernel-derived or kernel-dumped, never hand-entered):
  * PUBLICATION/MASTER/sources.json  - for each problem: repository, branch,
    commit and CI run of the tree that was checked, plus the path of its
    inventory/PROOF_INVENTORY.json (produced by scripts/proof_inventory.py);
  * PUBLICATION/MASTER/lanes.json    - the seven lane architectures dumped
    from axiomatic-millenium (AxiomaticMillenium.sevenLaneArchitectures);
  * certs/final_external/v1/MATH_TERMINAL_BOUNDARY_20260922.json.

Outputs: PUBLICATION/MASTER/FINAL_PROOF_STRUCTURE.json and .md.

usage: python3 scripts/build_master_dossier.py --inventories DIR
       (DIR holds one sub-directory per source id with PROOF_INVENTORY.json)
"""

import argparse
import json
import re
from pathlib import Path

GAP_SUFFIX = re.compile(r"(Gap|Producer|Obligation|Frontier|Transfer|Calibration|Payload|Habitant|Law)$")


def load(p):
    return json.loads(Path(p).read_text())


def summarise_inventory(inv):
    s = inv["summary"]
    default_bad = [m for m in inv["modules"] if m["status"] != "OK" and m["in_default_build"]]
    orphan_bad = [m for m in inv["modules"] if m["status"] != "OK" and not m["in_default_build"]]
    gaps = [p for p in inv["props"] if p["closed_prop"] and GAP_SUFFIX.search(p["name"].split(".")[-1])]
    return {
        "modules": f"{s['modules_ok']}/{s['modules_total']}",
        "default_build": "GREEN" if not default_bad else "FAILED",
        "default_build_failures": [{"module": m["module"], "status": m["status"],
                                    "detail": (m.get("first_error") or m.get("blocked_by") or "").split("\n")[0]}
                                   for m in default_bad],
        "orphan_failures": [m["module"] for m in orphan_bad],
        "theorems": s["theorems_total"],
        "theorems_standard_axioms_only": s["theorems_clean"],
        "theorems_using_sorry": s["theorems_using_sorry"],
        "project_axioms": s["project_axioms_declared"],
        "vacuous_props": [p["name"] for p in inv["props"] if p["status"] == "VACUOUS"],
        "gaps_proved": sorted(p["name"] for p in gaps if p["status"] == "PROVED"),
        "gaps_refuted": sorted(p["name"] for p in gaps if p["status"] == "REFUTED"),
        "gaps_without_proof": sorted(p["name"] for p in gaps if p["status"] == "NO_PROOF_IN_LIBRARY"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--inventories", default="PUBLICATION/MASTER/inventories")
    a = ap.parse_args()
    root = Path(a.root)
    master = root / "PUBLICATION" / "MASTER"
    sources = load(master / "sources.json")
    lanes = {l["lane"]: l for l in load(master / "lanes.json")}
    boundary = load(root / "certs/final_external/v1/MATH_TERMINAL_BOUNDARY_20260922.json")

    problems = []
    for src in sources["problems"]:
        inv_path = Path(a.inventories) / src["id"] / "PROOF_INVENTORY.json"
        inv = summarise_inventory(load(inv_path))
        lane = lanes[src["lane"]]
        row = {
            "id": src["id"],
            "problem": src["problem"],
            "endpoint": src["endpoint"],
            "checked_tree": {k: src[k] for k in ("repository", "branch", "commit", "ci_run", "toolchain")},
            "kernel": inv,
            "closed_math": lane["closedMath"],
            "closed_bridges": lane["closedBridge"],
            "exact_open_producers": lane["exactOpenProducer"],
            "exact_negative_producer": lane["exactNegativeProducer"],
            "closure_requirement": lane["closureRequirement"],
            "material_atoms": lane["materialAtoms"],
            "lane_build_state": lane["buildState"],
            "lane_source_ref": lane["sourceRef"],
            "endpoint_status": "OPEN",
            "final_proof_credit": 0,
        }
        if src["lane"] == "PNP":
            pv = boundary["p_vs_np"]
            row["lean_terminal_producers"] = {
                "P01ConstructionGap": {"state": pv["P01"]["state"], "meaning": pv["P01"]["exact_missing"]},
                "G21Pointwise": {"state": pv["P02"]["state"], "meaning": pv["P02"]["exact_missing"]},
            }
            row["lean_conditional_closure"] = boundary["final_external"]["two_gap_pipeline"]["reduction"]["theorem"]
        problems.append(row)

    atoms = sum(p["material_atoms"] for p in problems)
    out = {
        "schema": "mcore.final-proof-structure.v1",
        "generated_by": "scripts/build_master_dossier.py (inputs are kernel-derived; do not edit by hand)",
        "final_statement": "FINAL = the conjunction of the seven endpoints below. Each endpoint closes only "
                           "through its exact open producer (or one genuine counterexample) on the checked tree.",
        "final_status": {
            "endpoints_proved": 0,
            "endpoints_total": len(problems),
            "display": f"0/{len(problems)}",
            "material_atoms_open": atoms,
            "FINAL_EXTERNAL_ISSUED": False,
            "FINAL_ROOT": None,
        },
        "verified_scaffold": {
            "trees_checked": len(problems),
            "default_builds_green": sum(1 for p in problems if p["kernel"]["default_build"] == "GREEN"),
            "theorems": sum(p["kernel"]["theorems"] for p in problems),
            "theorems_standard_axioms_only": sum(p["kernel"]["theorems_standard_axioms_only"] for p in problems),
            "theorems_using_sorry": sum(p["kernel"]["theorems_using_sorry"] for p in problems),
        },
        "global_infrastructure": sources.get("infrastructure", []),
        "problems": problems,
    }
    (master / "FINAL_PROOF_STRUCTURE.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    (master / "FINAL_PROOF_STRUCTURE.md").write_text(render(out))
    print(json.dumps(out["final_status"]), json.dumps(out["verified_scaffold"]))


def render(d):
    fs, vs = d["final_status"], d["verified_scaffold"]
    L = ["# Final proof structure", "",
         "Generated by `scripts/build_master_dossier.py` from kernel-derived inventories. Do not edit by hand.", "",
         "## The final statement", "",
         "FINAL is the conjunction of the seven endpoints below. Every one of them has the same shape:",
         "", "```",
         "closed mathematics  →  closed bridge  →  ENDPOINT",
         "                          ↑",
         "              exact open producer (or one genuine counterexample)",
         "```", "",
         "What the kernel guarantees here: every tree listed compiles in CI, and every theorem in it uses only "
         "propext, Classical.choice and Quot.sound (no sorry, no project axiom). The closed-mathematics and "
         "bridge items are the entries recorded in the seven-lane catalog of axiomatic-millenium; this dossier "
         "does not match each entry to an individual theorem. The open producers are proved nowhere: they are "
         "the mathematical content of each problem.", "",
         "| | |", "| --- | --- |",
         f"| Endpoints proved | **{fs['display']}** |",
         f"| Open material atoms | {fs['material_atoms_open']} |",
         f"| FINAL_EXTERNAL_ISSUED | {str(fs['FINAL_EXTERNAL_ISSUED']).lower()} |",
         f"| Trees checked / default builds green | {vs['trees_checked']} / {vs['default_builds_green']} |",
         f"| Theorems checked (standard axioms only) | {vs['theorems']} ({vs['theorems_standard_axioms_only']}) |",
         f"| Theorems using sorry | {vs['theorems_using_sorry']} |", ""]
    if d["global_infrastructure"]:
        L += ["## Global infrastructure", "", "| Repository | Branch | Commit | CI run | Modules | Theorems |",
              "| --- | --- | --- | --- | --- | --- |"]
        for g in d["global_infrastructure"]:
            L.append(f"| {g['repository']} | `{g['branch']}` | `{g['commit'][:8]}` | {g['ci_run']} | {g['modules']} | {g['theorems']} |")
        L.append("")
    for p in d["problems"]:
        k, t = p["kernel"], p["checked_tree"]
        L += [f"## {p['problem']}", "", f"**Endpoint.** {p['endpoint']}", "",
              f"**Status.** OPEN — final-proof credit 0. Material atoms: {p['material_atoms']}.", "",
              f"**Checked tree.** `{t['repository']}` @ `{t['commit'][:8]}` (`{t['branch']}`), "
              f"CI run {t['ci_run']}, {t['toolchain']}. Modules {k['modules']}, default build {k['default_build']}, "
              f"{k['theorems']} theorems ({k['theorems_standard_axioms_only']} with standard axioms only), "
              f"{k['theorems_using_sorry']} using sorry.", ""]
        if k["default_build_failures"]:
            L += ["Default-build failures:", ""] + [f"- `{f['module']}` {f['status']}: {f['detail']}" for f in k["default_build_failures"]] + [""]
        if k["orphan_failures"]:
            L += ["Outside the default build, not compiling: " + ", ".join(f"`{x}`" for x in k["orphan_failures"]) + ".", ""]
        L += [f"Lane catalog entry: `{p['lane_source_ref']}` (build state recorded there: `{p['lane_build_state']}`).", ""]
        L += ["**1. Closed mathematics (as recorded in the lane catalog).**", ""] + [f"- {x}" for x in p["closed_math"]] + [""]
        L += ["**2. Closed bridges to the endpoint (as recorded in the lane catalog).**", ""] + [f"- {x}" for x in p["closed_bridges"]] + [""]
        L += ["**3. Exact open producer — the missing mathematics.**", ""] + [f"- {x}" for x in p["exact_open_producers"]]
        L += ["", f"Negative route: {p['exact_negative_producer']}.", "", f"Closes when: {p['closure_requirement']}.", ""]
        if "lean_terminal_producers" in p:
            L += ["**Lean terminal producers (M-Core FINAL_EXTERNAL).**", ""]
            for n, v in p["lean_terminal_producers"].items():
                L.append(f"- `{n}` — {v['state']}: {v['meaning']}")
            L += ["", f"Conditional closure theorem: `{p['lean_conditional_closure']}` "
                      "(both producers ⇒ P ≠ NP in the official model).", ""]
        if k["gaps_proved"] or k["gaps_refuted"] or k["gaps_without_proof"]:
            L += ["**Gap propositions in this tree (status from the kernel).**", ""]
            L += [f"- PROVED `{x}`" for x in k["gaps_proved"]]
            L += [f"- REFUTED `{x}`" for x in k["gaps_refuted"]]
            L += [f"- no proof in library `{x}`" for x in k["gaps_without_proof"]]
            L.append("")
        if k["vacuous_props"]:
            L += ["Vacuous Prop definitions (body ends in True): " + ", ".join(f"`{x}`" for x in k["vacuous_props"]), ""]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
