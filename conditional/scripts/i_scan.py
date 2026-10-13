#!/usr/bin/env python3
"""Coleta, em todos os branches de um repositório, os blobs (únicos por conteúdo) que tratam da
teoria dos números indeterminados I e da geometria fechado → meio-fechado.

Uso: i_scan.py <repo_dir> <corpus_dir>
Grava <corpus_dir>/<repo>/<blob>.<ext> e <corpus_dir>/<repo>.index.json
"""
import json, os, re, subprocess, sys

EXT = {".md", ".lean", ".tex", ".txt", ".py", ".v", ".agda", ".thy", ".rst"}
KEY_I = re.compile(r"indetermin|indeterminad|indeterminate|\bconjunto\s+I\b|𝕀|ℐ|"
                   r"\bI\s*[:=]=?\s*0\s*/\s*0|0\s*/\s*0|0\s*⊘\s*0|∞\s*[-−]\s*∞|1\s*\^\s*∞|∞\s*\^\s*0|"
                   r"seven.?states?|sete estados|7.?estados", re.I)
KEY_G = re.compile(r"meio[- ]fechad|semi[- ]?abert|semiabert|half[- ]?(open|closed)|tor[çc][ãa]o|torcid|"
                   r"comprimid|compress|tensionad|tens[ãa]o|neutro|neutral|twist", re.I)
MAXSZ = 400_000


def git(repo, *a, inp=None):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, input=inp).stdout


def main(repo, corpus):
    name = os.path.basename(repo.rstrip("/"))
    refs = [r for r in git(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").decode().split()
            if not r.endswith("/HEAD")]
    blobs = {}
    for ref in refs:
        for line in git(repo, "ls-tree", "-r", "-l", ref).decode("utf-8", "replace").splitlines():
            try:
                meta, path = line.split("\t", 1)
                mode, typ, sha, size = meta.split()
            except ValueError:
                continue
            if typ != "blob" or size == "-" or int(size) > MAXSZ:
                continue
            ext = os.path.splitext(path)[1].lower()
            if ext not in EXT:
                continue
            b = blobs.setdefault(sha, {"ext": ext, "paths": set()})
            if len(b["paths"]) < 6:
                b["paths"].add(ref.replace("refs/remotes/origin/", "") + ":" + path)
    if not blobs:
        return
    shas = list(blobs)
    out = git(repo, "cat-file", "--batch", inp=("\n".join(shas) + "\n").encode())
    idx, pos = [], 0
    os.makedirs(os.path.join(corpus, name), exist_ok=True)
    while pos < len(out):
        nl = out.index(b"\n", pos)
        hdr = out[pos:nl].decode().split()
        pos = nl + 1
        if len(hdr) < 3:
            continue
        sha, sz = hdr[0], int(hdr[2])
        data = out[pos:pos + sz]
        pos += sz + 1
        txt = data.decode("utf-8", "replace")
        hi = KEY_I.findall(txt)
        if not hi:
            continue
        hg = KEY_G.findall(txt)
        b = blobs[sha]
        fn = os.path.join(corpus, name, sha + b["ext"])
        with open(fn, "w") as f:
            f.write(txt)
        idx.append({"blob": sha, "ext": b["ext"], "paths": sorted(b["paths"]), "hits_I": len(hi),
                    "hits_G": len(hg), "size": sz})
    with open(os.path.join(corpus, name + ".index.json"), "w") as f:
        json.dump(idx, f, ensure_ascii=False, indent=0)
    print(f"{name}: blobs={len(blobs)} I={len(idx)}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
