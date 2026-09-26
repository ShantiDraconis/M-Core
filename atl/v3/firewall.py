#!/usr/bin/env python3
import json, pathlib, re, sys
from collections import defaultdict

FORBIDDEN=re.compile(r"(^|[^A-Za-z0-9_])(sorry|admit|sorryAx)([^A-Za-z0-9_]|$)")

def load(p): return json.loads(pathlib.Path(p).read_text())

def ids(g): return {n["id"] for n in g["nodes"]}

def fw_graph(g):
    known=ids(g); errors=[]
    for e in g["edges"]:
        if e["from"] not in known or e["to"] not in known:
            errors.append({"firewall":"CIRCULARITY","detail":f"dangling edge {e}"})
    adj=defaultdict(list)
    for e in g["edges"]: adj[e["from"]].append(e["to"])
    color={}
    def dfs(x):
        color[x]=1
        for y in adj[x]:
            if color.get(y)==1: return True
            if color.get(y,0)==0 and dfs(y): return True
        color[x]=2; return False
    if any(color.get(x,0)==0 and dfs(x) for x in known):
        errors.append({"firewall":"CIRCULARITY","detail":"cycle in canonical graph"})
    return errors

def fw_semantic(n):
    return [] if n.get("statement_hash") else [{"firewall":"SEMANTIC","node":n["id"],"detail":"statement_hash UNSET"}]

def fw_interface(n):
    s=n["semantic_statement"].lower()
    suspicious=("placeholder" in s or "skeleton" in s or "prop fingindo" in s)
    return [{"firewall":"INTERFACE","node":n["id"],"detail":"placeholder/interface marker"}] if suspicious else []

def fw_vacuous(n):
    s=n["formal_statement"]
    bad=s in {"True","False",""} or n["semantic_statement"].strip().lower() in {"true","trivial"}
    return [{"firewall":"VACUOUS","node":n["id"],"detail":"trivial/empty statement marker"}] if bad else []

def fw_source(n,root):
    errors=[]
    for rel in n["source_files"]:
        p=root/rel
        if not p.exists(): errors.append({"firewall":"AXIOM","node":n["id"],"detail":f"missing source {rel}"}); continue
        if FORBIDDEN.search(p.read_text(errors="ignore")):
            errors.append({"firewall":"AXIOM","node":n["id"],"detail":f"forbidden token in {rel}"})
    return errors

def run(g,root):
    out=fw_graph(g)
    for n in g["nodes"]:
        out += fw_semantic(n)+fw_interface(n)+fw_vacuous(n)+fw_source(n,root)
    return out

def main():
    g=load(sys.argv[1]); root=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else ".")
    errors=run(g,root)
    print(json.dumps({"green":not errors,"errors":errors},indent=2))
    raise SystemExit(1 if errors else 0)

if __name__=="__main__": main()
