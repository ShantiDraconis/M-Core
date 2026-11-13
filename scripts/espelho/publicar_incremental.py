#!/usr/bin/env python3
"""Incremental update of atk-math-core-public with the M-Core kernel Lean files added after the MVEI-verified commit.

usage: publicar_incremental.py <m-core repo> <commit> <mirror repo> <ci.json>
ci.json: {"ci": [...newest first...], "local": "...", "tabela": [[file, n, content], ...],
          "ver_ci": {name: axioms}, "so_ci": [name prefixes checked only by CI]}
Only atk-kernel/ is published (audit/ tooling and planted test cases stay private).
"""
import csv, datetime, hashlib, io, json, os, re, subprocess, sys

MC, C, MIR, CIJ = sys.argv[1:5]
VER = "390e3781109fa42e977d143caa9204ed94166a7b"
PADRAO = "propext, Classical.choice, Quot.sound"


def git(*a):
    return subprocess.run(["git", "-C", MC, *a], check=True, capture_output=True).stdout


full = git("rev-parse", C).decode().strip()
date = git("show", "-s", "--format=%cI", full).decode().strip()
date = datetime.datetime.fromisoformat(date).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
pub = re.compile(r"(\.lean$|(^|/)lakefile\.[a-z]+$|(^|/)lean-toolchain$|(^|/)lake-manifest\.json$)")
added, changed = [], []
for line in git("diff", "--name-status", VER, full).decode().splitlines():
    st, path = line.split("\t", 1)
    if not pub.search(path) or not path.startswith("atk-kernel/"):
        continue
    if st == "A":
        added.append(path)
    elif st == "M":
        changed.append(path)
    else:
        sys.exit(f"status inesperado {st} {path}")
added.sort(); changed.sort()

for p in added + changed:
    data = git("show", f"{full}:{p}")
    dst = os.path.join(MIR, "imports/M-Core", p)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "wb").write(data)

sp = os.path.join(MIR, "mvei/SOURCES.sha256")
ent = {}
for l in open(sp):
    h, f = l.rstrip("\n").split("  ", 1)
    ent[f] = h
for p in added + changed:
    f = "imports/M-Core/" + p
    ent[f] = hashlib.sha256(open(os.path.join(MIR, f), "rb").read()).hexdigest()
open(sp, "w").write("".join(f"{ent[f]}  {f}\n" for f in sorted(ent)))
nfiles = len(ent)
nlean = sum(1 for f in ent if f.endswith(".lean"))

ax = {}
for l in git("show", f"{full}:atk-kernel/audits/axioms.txt").decode().splitlines():
    if l.startswith("#") or "\t" not in l:
        continue
    n, a = l.split("\t", 1)
    ax[n] = a
cp = os.path.join(MIR, "mvei/AFTER_VERIFIED_COMMIT.csv")
rows = list(csv.reader(open(cp, newline="")))
head, rows = rows[0], rows[1:]
ja = {r[0] for r in rows}
ci = json.load(open(CIJ))
por_arquivo = {}
for p in added:
    if not p.startswith("atk-kernel/ATK/") or p in ja:
        continue
    stack, novos = [], []
    for i, line in enumerate(git("show", f"{full}:{p}").decode().split("\n"), start=1):
        m = re.match(r"^namespace\s+(\S+)", line)
        if m:
            stack.append(("ns", m.group(1))); continue
        m = re.match(r"^section(?:\s+(\S+))?\s*$", line)
        if m:
            stack.append(("sec", m.group(1) or "")); continue
        if re.match(r"^end(?:\s+(\S+))?\s*$", line):
            if stack:
                stack.pop()
            continue
        m = re.match(r"^(?:theorem|lemma)\s+([^\s(:{\[]+)", line)
        if m:
            name = ".".join([n for k, n in stack if k == "ns"] + [m.group(1)])
            a = ax.get(name)
            if a is None:
                sys.exit(f"sem axiomas registrados: {name}")
            if a == "VER CI":
                a = ci["ver_ci"].get(name)
                if a is None:
                    sys.exit(f"VER CI sem valor do CI: {name}")
                quem = "M-Core CI (T1)"
            elif any(name.startswith(pre) for pre in ci.get("so_ci", [])):
                quem = "M-Core CI (T1)"
            else:
                quem = "M-Core CI (T1) and local lake build, Lean v4.34.1"
            if not set(x.strip() for x in a.split(",")) <= set(PADRAO.split(", ")):
                sys.exit(f"axiomas fora do padrão: {name}: {a}")
            novos.append([p, str(i), name, a, "closed", quem])
    rows += novos
    por_arquivo[p] = len(novos)
buf = io.StringIO()
w = csv.writer(buf, lineterminator="\n")
w.writerow(head)
w.writerows(rows)
open(cp, "w", newline="").write(buf.getvalue())
nthm = len(rows)

sj = os.path.join(MIR, "mvei/SOURCE.json")
d = json.load(open(sj))
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
d.update({
    "source_commit": full, "source_commit_date": date, "files": nfiles, "lean_files": nlean,
    "lean_files_added_after_verified_commit": added,
    "lean_files_changed_after_verified_commit": changed,
    "published_at": now,
    "published_by": "incremental update of the MVEI mirror (only the atk-kernel files added or changed after the verified commit)",
    "kernel_check_after_verified_commit": {
        "file": "mvei/AFTER_VERIFIED_COMMIT.csv", "theorems": nthm,
        "ci": ci["ci"][0], "local": ci["local"], "ci_earlier": ci["ci"][1:],
    },
})
json.dump(d, open(sj, "w"), ensure_ascii=False, indent=1)
open(sj, "a").write("\n")

rp = os.path.join(MIR, "mvei/README.md")
r = open(rp).read()
r = re.sub(r"\* Source: `ShantiDraconis/M-Core`, commit `[0-9a-f]+` \([^)]*\)\.[^\n]*",
           f"* Source: `ShantiDraconis/M-Core`, commit `{full}` ({date}). This is newer than the commit MVEI verified "
           f"(`{VER[:7]}`); the files added since then are covered in "
           f"[Added after the verified commit](#added-after-the-verified-commit).", r, count=1)
r = re.sub(r"\* \d+ files: \d+ `\.lean` files", f"* {nfiles} files: {nlean} `.lean` files", r, count=1)
fmt = lambda n: f"{n:,}".replace(",", " ")
ci_lines = "\n".join(f"  * run {c['run_id']} on commit `{c['commit']}`: {c['result']}" for c in reversed(ci["ci"]))
tab = "\n".join(f"| {files} | {n or por_arquivo.get(files.strip(chr(96)), n)} | {txt} |" for files, n, txt in ci["tabela"])
sec = f"""## Added after the verified commit

Between the verified commit `{VER[:7]}` and the published commit `{full[:7]}`, {len(added)} `.lean` files were added to `atk-kernel/` and {len(changed)} changed (`atk-kernel/ATK.lean`, which only adds their imports). No other published file changed. The MVEI tables above do not cover these files. Their {fmt(nthm)} theorems were checked by the Lean kernel outside MVEI:

* **M-Core CI** (private repository), job "Lean 4 + Mathlib — compilação e auditoria de axiomas":
{ci_lines}
* **Local build**: {ci['local']}

| File | Theorems | Content |
|---|---:|---|
{tab}

None of these theorems proves the Riemann hypothesis or any other open problem. Several are equivalences with RH, which stays open. Each theorem with its file, line and axioms is in [`AFTER_VERIFIED_COMMIT.csv`](AFTER_VERIFIED_COMMIT.csv).

"""
if "## Added after the verified commit" in r:
    r = re.sub(r"## Added after the verified commit\n.*?(?=## Files in this folder)", sec, r, flags=re.S)
else:
    r = r.replace("## Files in this folder", sec + "## Files in this folder", 1)
bullet = f"* `AFTER_VERIFIED_COMMIT.csv` — the {fmt(nthm)} theorems of the files added after the verified commit: file, line, name, axioms, state\n"
r = re.sub(r"\* `AFTER_VERIFIED_COMMIT\.csv`[^\n]*\n", "", r)
r = r.replace("## Files in this folder\n\n", "## Files in this folder\n\n" + bullet, 1)
open(rp, "w").write(r)

rp = os.path.join(MIR, "README.md")
r = open(rp).read()
m = re.search(r"(<!-- mvei:start -->\n## Lean sources and kernel check \(MVEI\)\n\n)(.*?)(\n<!-- mvei:end -->)", r, re.S)
txt = m.group(2)
txt = re.sub(r"at commit `[0-9a-f]+` \([^)]*\): \d+ files\. In the MVEI verification( \(commit `[0-9a-f]+`\))?",
             f"at commit `{full[:7]}` ({date[:10]}): {nfiles} files. In the MVEI verification (commit `{VER[:7]}`)", txt)
txt = re.sub(r" The \d+ Lean files added after that commit hold [\d ]+ more theorems, all closed with only the standard axioms \(M-Core CI and a local build\)\.", "", txt)
txt = txt.replace(" A closed theorem proves",
                  f" The {len(added)} Lean files added after that commit hold {fmt(nthm)} more theorems, all closed with only the standard axioms (M-Core CI and a local build). A closed theorem proves", 1)
r = r[:m.start(2)] + txt + r[m.end(2):]
open(rp, "w").write(r)

print(json.dumps({"commit": full, "added": len(added), "changed": changed, "files": nfiles, "lean": nlean,
                  "theorems_after": nthm, "novos_por_arquivo": por_arquivo}, ensure_ascii=False, indent=1))
