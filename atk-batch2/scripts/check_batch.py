#!/usr/bin/env python3
"""
ATK batch2 — compila no kernel Lean os arquivos dos pacotes de 12/10 (sem alterá-los) e audita axiomas.

uso: check_batch.py LABEL WORKDIR EXPECTED APPENDIX_DIR ORIG_DIR REPORT_DIR

Para cada arquivo listado em EXPECTED ("<arquivo relativo> <teorema>"):
  texto do arquivo em WORKDIR  +  (opcional) APPENDIX_DIR/<arquivo>  +  linhas `#print axioms`
é gravado em WORKDIR/_audit/ e compilado com `lake env lean` (ou `lean`, se não houver lakefile).
Veredito por teorema:
  CERTIFIED      — elaborado, e axiomas ⊆ {propext, Classical.choice, Quot.sound}
  NOT_CERTIFIED  — não elaborado (erro de parse/elaboração), ausente, ou axioma extra (inclui sorryAx)
Teoremas `ATK.Audit.*` vêm do apêndice de auditoria (não fazem parte do pacote original).
Também registra se o arquivo compilado é byte-idêntico ao original do zip (ORIG_DIR).
"""
import hashlib, json, os, re, subprocess, sys

label, work, expected_path, appendix_dir, orig_dir, report_dir = sys.argv[1:7]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
os.makedirs(report_dir, exist_ok=True)
os.makedirs(os.path.join(work, "_audit"), exist_ok=True)
use_lake = os.path.exists(os.path.join(work, "lakefile.toml")) or os.path.exists(os.path.join(work, "lakefile.lean"))

expected = {}
for line in open(expected_path):
    if line.strip():
        f, thm = line.split()
        expected.setdefault(f, []).append(thm)

sha = lambda b: hashlib.sha256(b).hexdigest()
rows, files = [], []
for f, thms in expected.items():
    raw = open(os.path.join(work, f), "rb").read()
    orig = os.path.join(orig_dir, f)
    identical = os.path.exists(orig) and open(orig, "rb").read() == raw
    app_path = os.path.join(appendix_dir, f)
    appendix = open(app_path, encoding="utf-8").read() if os.path.exists(app_path) else ""
    text = raw.decode("utf-8") + "\n\n" + appendix + "\n" + "".join(f"#print axioms {t}\n" for t in thms)
    audit = os.path.join(work, "_audit", f.replace("/", "_").replace(".lean", ".audit.lean"))
    open(audit, "w", encoding="utf-8").write(text)
    cmd = (["lake", "env", "lean"] if use_lake else ["lean"]) + [os.path.relpath(audit, work)]
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True)
    log = p.stdout + p.stderr
    open(os.path.join(report_dir, f"{label}__{os.path.basename(audit)}.log"), "w").write(log)
    errs = [re.sub(r"^.*?_audit/", "", l) for l in log.splitlines() if "error" in l]
    files.append({"file": f, "sha256": sha(raw), "byte_identical_to_zip": identical,
                  "appendix": bool(appendix), "exit_code": p.returncode, "errors": errs[:12]})
    ax = {}
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
        ax[m.group(1)] = [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", log):
        ax[m.group(1)] = []
    for t in thms:
        a = ax.get(t)
        if a is None:
            v, why = "NOT_CERTIFIED", "não elaborado (sem saída de #print axioms)"
        elif not set(a) <= ALLOWED:
            v, why = "NOT_CERTIFIED", "axiomas extras: " + ", ".join(sorted(set(a) - ALLOWED))
        else:
            v, why = "CERTIFIED", ""
        rows.append({"file": f, "theorem": t, "audit_appendix": t.startswith("ATK.Audit."),
                     "axioms": a, "verdict": v, "reason": why})

ver = subprocess.run(["lean", "--version"], cwd=work, capture_output=True, text=True).stdout.strip()
pkg = [r for r in rows if not r["audit_appendix"]]
aud = [r for r in rows if r["audit_appendix"]]
okp = sum(r["verdict"] == "CERTIFIED" for r in pkg)
oka = sum(r["verdict"] == "CERTIFIED" for r in aud)
rep = {"label": label, "lean": ver, "commit": os.environ.get("GITHUB_SHA", "local"),
       "run_id": os.environ.get("GITHUB_RUN_ID"), "package_certified": okp, "package_total": len(pkg),
       "audit_certified": oka, "audit_total": len(aud), "files": files, "theorems": rows,
       "OPEN_MATH": True, "TERMINAL_CERTIFIED": "0/7"}
json.dump(rep, open(os.path.join(report_dir, f"{label}.json"), "w"), indent=2, ensure_ascii=False)

head = f"{label}: pacote {okp}/{len(pkg)} · auditoria {oka}/{len(aud)} · {ver}"
md = [f"## {head}", ""]
for fi in files:
    md.append(f"- `{fi['file']}` sha256 `{fi['sha256'][:16]}…` · "
              f"{'idêntico ao zip' if fi['byte_identical_to_zip'] else 'CÓPIA CORRIGIDA'} · saída {fi['exit_code']}")
md += ["", "| Arquivo | Teorema | Veredito | Axiomas / motivo |", "|---|---|---|---|"]
for r in rows:
    axs = ", ".join(r["axioms"]) if r["axioms"] is not None else "—"
    md.append(f"| `{r['file']}` | `{r['theorem']}` | {'✅' if r['verdict']=='CERTIFIED' else '❌'} {r['verdict']} | {axs} {r['reason']} |")
for fi in files:
    if fi["errors"]:
        md += ["", f"**Erros em {fi['file']}:**", "```"] + fi["errors"] + ["```"]
out = "\n".join(md)
print(out)
if os.environ.get("GITHUB_ACTIONS"):
    esc = lambda s: s.replace("%", "%25").replace("\r", "").replace("\n", "%0A")
    print(f"::notice title=BATCH2 {head}::" + esc("\n".join(
        f"{fi['file']} sha256={fi['sha256']} identical={fi['byte_identical_to_zip']} exit={fi['exit_code']}"
        for fi in files)))
    for fi in files:
        lines = [f"{r['verdict']} {r['theorem']} [{', '.join(r['axioms']) if r['axioms'] is not None else '—'}]"
                 for r in rows if r["file"] == fi["file"]]
        print(f"::notice title=BATCH2 {label} {fi['file']}::" + esc("\n".join(lines + ["ERROS:"] + fi["errors"][:6])))
    open(os.environ["GITHUB_STEP_SUMMARY"], "a").write(out + "\n\n")
sys.exit(0)
