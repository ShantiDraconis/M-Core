"""Auditoria do atk-ns: cada teorema listado em `#print axioms` precisa compilar, depender só de
propext / Classical.choice / Quot.sound e vir de fonte sem sorry/admit/axiom."""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = os.path.join(ROOT, "reports")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
rows, ok_all = [], True
for f in sorted(glob.glob(os.path.join(ROOT, "AtkNS", "**", "*.lean"), recursive=True)):
    rel = os.path.relpath(f, ROOT)
    src = open(f, encoding="utf-8").read()
    code = re.sub(r"--.*", "", re.sub(r"/-.*?-/", "", src, flags=re.S))
    flags = [w for w in ("sorry", "admit") if re.search(rf"\b{w}\b", code)]
    if re.search(r"^\s*axiom\s", code, re.M):
        flags.append("axiom")
    expected = re.findall(r"^#print axioms (\S+)", src, re.M)
    log_path = os.path.join(REP, "audit_" + rel.replace("/", "_") + ".log")
    log = open(log_path, encoding="utf-8").read() if os.path.exists(log_path) else ""
    status = open(os.path.join(REP, "status_" + rel.replace("/", "_") + ".txt")).read().strip() \
        if os.path.exists(os.path.join(REP, "status_" + rel.replace("/", "_") + ".txt")) else "NOT_RUN"
    ax = {m.group(1): [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
          for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S)}
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", log):
        ax[m.group(1)] = []
    for thm in expected:
        a = ax.get(thm)
        if status != "OK":
            v, why = "NOT_CERTIFIED", f"arquivo {status}"
        elif a is None:
            v, why = "NOT_CERTIFIED", "sem saída de #print axioms"
        elif not set(a) <= ALLOWED:
            v, why = "NOT_CERTIFIED", "axiomas extras: " + ", ".join(sorted(set(a) - ALLOWED))
        elif flags:
            v, why = "NOT_CERTIFIED", "fonte contém " + ", ".join(flags)
        else:
            v, why = "CERTIFIED", ""
        ok_all &= v == "CERTIFIED"
        rows.append({"file": rel, "theorem": thm, "verdict": v, "axioms": a, "reason": why})
cert = sum(r["verdict"] == "CERTIFIED" for r in rows)
state = "CERTIFIED" if rows and ok_all else "PARTIAL" if cert else "NOT_CERTIFIED"
json.dump({"state": state, "certified": cert, "total": len(rows), "rows": rows},
          open(os.path.join(REP, "report.json"), "w"), indent=1, ensure_ascii=False)
md = [f"## ATK-NS: {state} — {cert}/{len(rows)} teoremas", "", "| teorema | veredito | axiomas |",
      "|---|---|---|"]
md += [f"| `{r['theorem']}` | {r['verdict']} {r['reason']} | {', '.join(r['axioms'] or [])} |"
       for r in rows]
open(os.path.join(REP, "report.md"), "w").write("\n".join(md) + "\n")
print("\n".join(md))
if os.environ.get("GITHUB_ACTIONS"):
    print(f"::notice title=ATK-NS {state} {cert}/{len(rows)}::OpenAI NavierStokesAndEuler 8937a8f · mathlib v4.34.0-rc2")
sys.exit(0 if rows and ok_all else 1)
