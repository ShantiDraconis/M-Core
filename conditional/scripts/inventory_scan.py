#!/usr/bin/env python3
"""Inventário multilíngue de um repositório (todos os branches).

Uso: inventory_scan.py <repo_dir> <saida.json>

* Conta arquivos distintos (por conteúdo) por linguagem.
* Lean: delega a proof_scan.py (declarações que concluem alvos, sorry/?_/axiom, alegações).
* Coq/Rocq (.v), Agda (.agda), Isabelle (.thy): teoremas cujo enunciado menciona um dos 7
  problemas + escapatórias da linguagem (Admitted/Axiom/Parameter/Hypothesis; postulate;
  sorry/oops/axiomatization).
"""
import json, os, re, subprocess, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import proof_scan as ps

LANG = {".lean": "Lean", ".v": "Coq/Rocq", ".agda": "Agda", ".lagda": "Agda", ".thy": "Isabelle",
        ".py": "Python", ".ipynb": "Jupyter", ".tex": "LaTeX", ".md": "Markdown", ".json": "JSON",
        ".yml": "YAML", ".yaml": "YAML", ".toml": "TOML", ".csv": "CSV", ".tsv": "CSV", ".sh": "Shell",
        ".jl": "Julia", ".sage": "Sage", ".r": "R", ".R": "R", ".c": "C/C++", ".cpp": "C/C++", ".h": "C/C++",
        ".rs": "Rust", ".js": "JS/TS", ".ts": "JS/TS", ".html": "HTML", ".m": "MATLAB/ObjC", ".hs": "Haskell",
        ".mm": "Metamath", ".smt2": "SMT", ".tptp": "TPTP", ".p": "TPTP"}
PROVERS = {".v", ".agda", ".lagda", ".thy"}
KEY = re.compile(r"riemann|zeta|navier|stokes|hodge|birch|swinnerton|\bbsd\b|yang.?mills|mass.?gap|"
                 r"p_?neq_?np|p_?ne_?np|\bpnp\b|p\s*!=\s*np|beal|fermat|millennium", re.I)
ESC = {
    "Coq/Rocq": re.compile(r"\bAdmitted\.|\badmit\.|^\s*(Axiom|Axioms|Parameter|Parameters|Hypothesis|Hypotheses|Conjecture)\s", re.M),
    "Agda": re.compile(r"^\s*postulate\b", re.M),
    "Isabelle": re.compile(r"\bsorry\b|\boops\b|\baxiomatization\b"),
}
DECL = {
    "Coq/Rocq": re.compile(r"^\s*(Theorem|Lemma|Corollary|Proposition|Fact|Remark)\s+([\w']+)\s*(.*?)\.\s*$", re.M | re.S),
    "Isabelle": re.compile(r"^\s*(theorem|lemma|corollary|proposition)\s+([\w']*)\s*:?\s*(.*?)$", re.M),
    "Agda": re.compile(r"^([\w'\-]+)\s*:\s*(.+)$", re.M),
}


def git(repo, *a, inp=None):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, input=inp).stdout


def strip_c(code, lang):
    if lang == "Coq/Rocq" or lang == "Isabelle":
        return re.sub(r"\(\*.*?\*\)", " ", code, flags=re.S)
    if lang == "Agda":
        code = re.sub(r"\{-.*?-\}", " ", code, flags=re.S)
        return re.sub(r"--[^\n]*", "", code)
    return code


def main(repo, outp):
    name = os.path.basename(repo.rstrip("/"))
    refs = [r for r in git(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").decode().split()
            if not r.endswith("/HEAD")]
    langs = Counter()
    prover_blobs = defaultdict(set)
    seen = set()
    for ref in refs:
        for line in git(repo, "ls-tree", "-r", ref).decode("utf-8", "replace").splitlines():
            meta, path = line.split("\t", 1)
            parts = meta.split()
            if parts[1] != "blob": continue
            blob = parts[2]
            ext = os.path.splitext(path)[1]
            if (blob, ext) not in seen:
                seen.add((blob, ext))
                langs[LANG.get(ext, ext or "(sem extensão)")] += 1
            if ext in PROVERS:
                prover_blobs[blob].add((ref.replace("refs/remotes/origin/", ""), path))
    prover = {"files": 0, "with_escape": 0, "target_statements": []}
    if prover_blobs:
        blobs = list(prover_blobs)
        data = git(repo, "cat-file", "--batch", inp=("\n".join(blobs) + "\n").encode())
        pos = 0
        while pos < len(data):
            nl = data.index(b"\n", pos)
            hdr = data[pos:nl].decode().split()
            sha, size = hdr[0], int(hdr[2])
            raw = data[nl+1:nl+1+size].decode("utf-8", "replace")
            pos = nl + 1 + size + 1
            loc = sorted(prover_blobs[sha])[0]
            ext = os.path.splitext(loc[1])[1]
            lang = LANG[ext]
            code = strip_c(raw, lang)
            esc = ESC[lang].findall(code)
            prover["files"] += 1
            if esc: prover["with_escape"] += 1
            for m in DECL[lang].finditer(code):
                stmt = " ".join(m.group(m.lastindex).split())[:220]
                nm = m.group(2) if lang != "Agda" else m.group(1)
                if KEY.search(stmt) or KEY.search(nm or ""):
                    prover["target_statements"].append({
                        "lang": lang, "name": nm, "statement": stmt, "branch": loc[0], "path": loc[1],
                        "file_escapes": sorted(set(e if isinstance(e, str) else e[0] for e in esc))[:6],
                        "n_locations": len(prover_blobs[sha])})
    lean_out = outp.replace(".json", ".lean.json")
    lean = None
    if langs.get("Lean"):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ps.main(repo, lean_out)
        lean = json.load(open(lean_out))
    res = {"repo": name, "branches": len(refs), "languages": dict(langs.most_common()),
           "provers_other": prover,
           "lean": None if lean is None else {"lean_blobs": lean["lean_blobs"], "findings": lean["findings"],
                                               "claims": lean["claims"]}}
    json.dump(res, open(outp, "w"), ensure_ascii=False, indent=1)
    lf = 0 if lean is None else len(lean["findings"])
    print(f"{name}: branches={len(refs)} lean={langs.get('Lean',0)} coq={langs.get('Coq/Rocq',0)} "
          f"agda={langs.get('Agda',0)} isabelle={langs.get('Isabelle',0)} py={langs.get('Python',0)} "
          f"tex={langs.get('LaTeX',0)} | achados_lean={lf} enunciados_outros_provadores={len(prover['target_statements'])}",
          flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
