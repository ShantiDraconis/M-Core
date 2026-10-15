#!/usr/bin/env python3
"""ATK: audit literal terms across ALL local Git repositories and refs.
Read-only: never edits sources or promotes proof status. Python 3.10+.
Usage: python3 audit_language_all_refs.py /path/to/clones --output audit-language.csv
Each immediate subdirectory must be a local Git repository with refs fetched.
"""
import argparse
import csv
import pathlib
import re
import subprocess

TERMS = [
 "teoria", "hipótese", "conjectura", "proposta", "poderia existir",
 "seria possível", "se existisse", "assumimos", "supomos", "é evidente",
 "segue imediatamente", "é equivalente", "é necessário", "é suficiente",
 "é universal", "é único", "provado", "certificado", "GREEN", "FROZEN",
 "CLOSED", "OPEN", "modelo validado", "ponte concluída",
 "redução completa", "evidência numérica", "sem axiomas", "prova final",
]
EXT = {".lean", ".v", ".thy", ".agda", ".py", ".cpp", ".cc", ".h",
       ".sh", ".yml", ".yaml", ".json", ".md", ".tex", ".csv", ".txt"}
REGEX = re.compile("|".join(re.escape(t) for t in sorted(TERMS, key=len, reverse=True)), re.I)
def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE,
                          stderr=subprocess.DEVNULL, check=True).stdout

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=pathlib.Path)
    ap.add_argument("--output", default="audit-language.csv")
    a = ap.parse_args()
    repos = [p for p in sorted(a.root.iterdir()) if p.is_dir() and
             (p / ".git").exists()]
    with open(a.output, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["repo", "ref", "commit", "path", "line", "term",
                         "excerpt", "review_status"])
        for repo in repos:
            refs = git(repo, "for-each-ref", "--format=%(refname)",
                       "refs/heads", "refs/remotes", "refs/tags").decode().splitlines()
            seen = set()
            for ref in refs:
                commit = git(repo, "rev-parse", ref + "^{commit}").decode().strip()
                paths = git(repo, "ls-tree", "-r", "--name-only", commit).decode(
                    "utf-8", "replace").splitlines()
                for path in paths:
                    if pathlib.PurePosixPath(path).suffix.lower() not in EXT:
                        continue
                    # Reuse blobs at each path/ref; the output retains full provenance.
                    try:
                        blob = git(repo, "rev-parse", commit + ":" + path).decode().strip()
                    except subprocess.CalledProcessError:
                        continue
                    key = (ref, path, blob)
                    if key in seen:
                        continue
                    seen.add(key)
                    try:
                        raw = git(repo, "cat-file", "blob", blob)
                    except subprocess.CalledProcessError:
                        continue
                    if len(raw) > 2_000_000 or b"\\x00" in raw:
                        continue
                    for line_no, line in enumerate(raw.decode("utf-8", "replace").splitlines(), 1):
                        for match in REGEX.finditer(line):
                            writer.writerow([repo.name, ref, commit, path, line_no,
                                             match.group(0), line.strip()[:350], "REVIEW"])
            print(repo.name, len(refs), "refs processed", flush=True)
    print("Saved:", a.output, "— REVIEW means occurrence, not an error.")

if __name__ == "__main__":
    main()
