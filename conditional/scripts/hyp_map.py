#!/usr/bin/env python3
"""Mapa de descarga de hipóteses.

1. Indexa TODAS as declarações theorem/lemma/def/instance de todos os branches dos repositórios
   (conclusão normalizada, nº de hipóteses, sorry/?_/axiom no arquivo).
2. Para cada teorema CONDICIONAL que conclui um alvo dos 7 problemas, extrai as hipóteses
   (tipos dos binders explícitos de nível zero).
3. Uma hipótese é DESCARREGADA se existe declaração limpa (sem hipóteses explícitas, sem
   variable/include, sem sorry/?_/axiom no arquivo) cuja conclusão normalizada é idêntica.

Uso: hyp_map.py <saida.json> <repo_dir> [<repo_dir> ...]
"""
import json, os, re, subprocess, sys
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import proof_scan as ps

DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
                  r"(theorem|lemma|def|instance|abbrev)\b", re.M)


def norm(t):
    t = " ".join(t.split())
    t = re.sub(r"\s*([(),:])\s*", r"\1", t)
    while t.startswith("(") and t.endswith(")") and balanced(t[1:-1]):
        t = t[1:-1]
    return t


def balanced(s):
    d = 0
    for ch in s:
        if ch in "([{": d += 1
        elif ch in ")]}":
            d -= 1
            if d < 0: return False
    return d == 0


def top_binders(b):
    out, depth, buf, opener = [], 0, "", None
    for ch in b:
        if depth == 0 and ch in "({[⦃":
            depth, buf, opener = 1, "", ch
            continue
        if depth > 0:
            if ch in "({[⦃": depth += 1
            elif ch in ")}]⦄":
                depth -= 1
                if depth == 0:
                    out.append((opener, buf)); continue
            buf += ch
    return out


def binder_type(s):
    d = 0
    for i, ch in enumerate(s):
        if ch in "([{": d += 1
        elif ch in ")]}": d -= 1
        elif ch == ":" and d == 0:
            return s[:i].strip(), s[i+1:].strip()
    return None, None


def decls_of(code):
    res = []
    starts = [m.start() for m in DECL.finditer(code)] + [len(code)]
    for a, b in zip(starts, starts[1:]):
        chunk = code[a:b]
        head = chunk.split(":=", 1)[0] if ":=" in chunk else chunk.split(" where", 1)[0]
        head = " ".join(head.split())
        m = re.match(r"(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
                     r"(theorem|lemma|def|instance|abbrev)\s*([^\s(:{\[⦃]*)\s*(.*)", head)
        if not m: continue
        kind, name, rest = m.groups()
        binders, concl = ps.split_signature(rest)
        if not concl.strip(): continue
        hyps = []
        for opener, inner in top_binders(binders):
            if opener != "(": continue
            names, typ = binder_type(inner)
            if typ: hyps.append(norm(typ))
        res.append({"kind": kind, "name": name, "concl": norm(concl), "hyps": hyps,
                    "line": code[:a].count("\n") + 1})
    return res


def git(repo, *a, inp=None):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, input=inp).stdout


def main(outp, repos):
    index = defaultdict(list)          # concl normalizada -> declarações limpas sem hipótese
    conditionals = []                  # teoremas condicionais que concluem um alvo
    for repo in repos:
        name = os.path.basename(repo.rstrip("/"))
        refs = [r for r in git(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").decode().split()
                if not r.endswith("/HEAD")]
        locs = defaultdict(set)
        for ref in refs:
            for line in git(repo, "ls-tree", "-r", ref).decode("utf-8", "replace").splitlines():
                meta, path = line.split("\t", 1)
                if path.endswith(".lean") and meta.split()[1] == "blob":
                    locs[meta.split()[2]].add((ref.replace("refs/remotes/origin/", ""), path))
        blobs = list(locs)
        data = git(repo, "cat-file", "--batch", inp=("\n".join(blobs) + "\n").encode()) if blobs else b""
        pos = 0
        while pos < len(data):
            nl = data.index(b"\n", pos)
            hdr = data[pos:nl].decode().split()
            sha, size = hdr[0], int(hdr[2])
            raw = data[nl+1:nl+1+size].decode("utf-8", "replace")
            pos = nl + 1 + size + 1
            code = ps.strip_comments(raw)
            dirty = bool(re.search(r"\b(sorry|admit)\b", code)) or bool(
                re.search(r"(exact|refine|apply)\s+\?_\s*$|:=\s*\?_\s*$", code, re.M)) or bool(
                re.search(r"^\s*axiom\s", code, re.M))
            secvar = bool(re.search(r"^\s*variable\b[^\n]*\([^)]*:", code, re.M))
            loc = sorted(locs[sha])[0]
            for d in decls_of(code):
                entry = {"repo": name, "branch": loc[0], "path": loc[1], "name": d["name"], "kind": d["kind"]}
                if not d["hyps"] and not dirty and not secvar and d["kind"] in ("theorem", "lemma", "def", "instance"):
                    c = d["concl"]
                    index[c].append(entry)
                    if c.startswith("Nonempty"):
                        index[norm(c[len("Nonempty"):])].append(dict(entry, via="Nonempty"))
                t = ps.TARGET_RX.search(re.sub(r"^(Nonempty\s*\(?|\(\s*)+", "", d["concl"]))
                if t and d["hyps"] and "↔" not in d["concl"] and not d["concl"].startswith("¬") \
                        and d["kind"] in ("theorem", "lemma") and not dirty:
                    conditionals.append(dict(entry, concl=d["concl"][:200], target=t.group(1),
                                             problem=ps.TARGETS[t.group(1)].split("(")[0], hyps=d["hyps"]))
        print(f"{name}: blobs={len(blobs)} index={sum(len(v) for v in index.values())} condicionais={len(conditionals)}",
              flush=True)
    # descarga
    hyp_stats = defaultdict(lambda: {"count": 0, "problems": Counter(), "examples": [], "discharged_by": None})
    for c in conditionals:
        for h in c["hyps"]:
            s = hyp_stats[h]
            s["count"] += 1
            s["problems"][c["problem"]] += 1
            if len(s["examples"]) < 3:
                s["examples"].append(f"{c['repo']}::{c['branch']}::{c['path']}::{c['name']}")
            if s["discharged_by"] is None and h in index:
                s["discharged_by"] = index[h][:3]
    fully = []
    for c in conditionals:
        open_h = [h for h in c["hyps"] if hyp_stats[h]["discharged_by"] is None]
        if not open_h:
            fully.append(c)
    out = {"conditionals": len(conditionals), "distinct_hypotheses": len(hyp_stats),
           "discharged": sum(1 for s in hyp_stats.values() if s["discharged_by"]),
           "fully_discharged_conditionals": fully,
           "hypotheses": [{"type": h, "count": s["count"], "problems": dict(s["problems"]),
                           "examples": s["examples"], "discharged_by": s["discharged_by"]}
                          for h, s in sorted(hyp_stats.items(), key=lambda kv: -kv[1]["count"])]}
    json.dump(out, open(outp, "w"), indent=1, ensure_ascii=False)
    print(f"\nCONDICIONAIS LIMPOS={out['conditionals']} HIPÓTESES DISTINTAS={out['distinct_hypotheses']} "
          f"DESCARREGADAS={out['discharged']} CONDICIONAIS TOTALMENTE DESCARREGADOS={len(fully)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
