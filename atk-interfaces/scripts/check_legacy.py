#!/usr/bin/env python3
"""
Auditoria dos arquivos Lean ORIGINAIS da outra sessão (src/), sem modificá-los.

Para cada arquivo: gera reports/<nome>.audit.lean = original + linhas `#print axioms` dos teoremas
esperados, compila com `lake env lean`, e decide teorema a teorema:
  CERTIFIED     — o teorema existe e seus axiomas ⊆ {propext, Classical.choice, Quot.sound}
  NOT_CERTIFIED — erro (entra com sorryAx), ausente, ou axioma extra
Um erro num teorema não invalida os outros do mesmo arquivo: cada declaração é verificada
pelo kernel separadamente, e as que falham entram com `sorryAx`.
Os `example` sem nome só contam como verificados se o arquivo inteiro compilar sem erro.
"""
import hashlib, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REP = os.path.join(ROOT, "reports")
os.makedirs(REP, exist_ok=True)
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

expected = {}
for line in open(os.path.join(ROOT, "scripts", "expected.txt")):
    if line.strip():
        f, thm = line.split()
        expected.setdefault(f, []).append(thm)

rows, files = [], []
for f, thms in expected.items():
    src = open(os.path.join(ROOT, f), encoding="utf-8").read()
    sha = hashlib.sha256(src.encode()).hexdigest()
    audit = os.path.join(REP, os.path.basename(f).replace(".lean", ".audit.lean"))
    open(audit, "w", encoding="utf-8").write(src + "\n\n" + "".join(f"#print axioms {t}\n" for t in thms))
    p = subprocess.run(["lake", "env", "lean", audit], cwd=ROOT, capture_output=True, text=True)
    log = p.stdout + p.stderr
    open(audit.replace(".audit.lean", ".log"), "w").write(log)
    errs = [l for l in log.splitlines() if "error" in l]
    n_examples = len(re.findall(r"^\s*example\b", src, re.M))
    files.append({"file": f, "sha256": sha, "exit_code": p.returncode, "errors": errs[:15],
                  "examples": n_examples, "examples_ok": p.returncode == 0})
    ax = {}
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log, re.S):
        ax[m.group(1)] = [a.strip() for a in m.group(2).replace("\n", " ").split(",") if a.strip()]
    for m in re.finditer(r"'([^']+)' does not depend on any axioms", log):
        ax[m.group(1)] = []
    for t in thms:
        a = ax.get(t)
        if a is None:
            v, why = "NOT_CERTIFIED", "sem saída de #print axioms (não elaborado)"
        elif not set(a) <= ALLOWED:
            v, why = "NOT_CERTIFIED", "axiomas extras: " + ", ".join(sorted(set(a) - ALLOWED))
        else:
            v, why = "CERTIFIED", ""
        rows.append({"file": f, "theorem": t, "axioms": a, "verdict": v, "reason": why})

ok = sum(r["verdict"] == "CERTIFIED" for r in rows)
ver = subprocess.run(["lean", "--version"], capture_output=True, text=True).stdout.strip()
rep = {"certified": ok, "total": len(rows), "lean": ver, "mathlib": "v4.34.1",
       "commit": os.environ.get("GITHUB_SHA", "local"), "files": files, "theorems": rows}
json.dump(rep, open(os.path.join(REP, "legacy_report.json"), "w"), indent=2, ensure_ascii=False)

md = [f"## ATK-INTERFACES (arquivos da sessão de 12/10, Lean v4.34.1): {ok}/{len(rows)} teoremas certificados", ""]
for fi in files:
    md.append(f"- `{fi['file']}` sha256 `{fi['sha256'][:16]}…` · saída {fi['exit_code']} · "
              f"{fi['examples']} `example` {'verificados' if fi['examples_ok'] else 'NÃO verificados (arquivo com erro)'}")
md += ["", "| Teorema | Veredito | Motivo |", "|---|---|---|"]
for r in rows:
    md.append(f"| `{r['theorem']}` | {'✅' if r['verdict']=='CERTIFIED' else '❌'} {r['verdict']} | {r['reason']} |")
for fi in files:
    if fi["errors"]:
        md += ["", f"**Erros em {fi['file']}:**", "```"] + fi["errors"] + ["```"]
out = "\n".join(md)
print(out)
if os.environ.get("GITHUB_ACTIONS"):
    esc = lambda s: s.replace("%", "%25").replace("\n", "%0A")
    print(f"::notice title=ATK-INTERFACES {ok}/{len(rows)}::" + esc("\n".join(
        f"{fi['file']} sha256={fi['sha256']} exit={fi['exit_code']} examples_ok={fi['examples_ok']}" for fi in files)))
    for fi in files:
        lines = [f"{r['verdict']} {r['theorem']} [{', '.join(r['axioms']) if r['axioms'] is not None else '—'}] {r['reason']}"
                 for r in rows if r["file"] == fi["file"]]
        print(f"::notice title=ATK-INTERFACES {fi['file']}::" + esc("\n".join(lines + ["ERROS:"] + fi["errors"][:6])))
    open(os.environ["GITHUB_STEP_SUMMARY"], "a").write(out + "\n")
sys.exit(0)
