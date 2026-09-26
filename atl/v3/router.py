#!/usr/bin/env python3
import json, math, pathlib, sys
from collections import defaultdict, deque

ATTACKABLE="OPEN_MATH_ATTACKABLE"
NONCUT={"OPEN_MATH_RESEARCH","OPEN_MATH_EXTERNAL"}

def load(path):
    return json.loads(pathlib.Path(path).read_text())

def indexes(g):
    nodes={n["id"]:n for n in g["nodes"]}
    up=defaultdict(set); down=defaultdict(set)
    for e in g["edges"]:
        if e["relation"] in {"DEPENDS_ON","IMPLIES","PRODUCES","VALIDATES","REPLACES","MINES"}:
            down[e["from"]].add(e["to"]); up[e["to"]].add(e["from"])
    return nodes,up,down

def latest_event(g,node,kind):
    xs=[e for e in g["log"] if e["node"]==node and e["kind"]==kind]
    return xs[-1]["data"] if xs else None

def open_class(g,node):
    ev=latest_event(g,node,"OPEN_MATH_CLASS")
    return ev.get("class") if ev else None

def descendants(down,node):
    seen=set(); q=deque([(node,0)]); out=[]
    while q:
        x,d=q.popleft()
        for y in down.get(x,()):
            if y not in seen:
                seen.add(y); out.append((y,d+1)); q.append((y,d+1))
    return out

def cost_for(n,h):
    samples=[s for s in h.get("samples",[]) if s.get("node")==n["id"]]
    if len(samples)>=h.get("minimum_samples_for_empirical",20):
        cyc=sum(s["cycles"] for s in samples)/len(samples)
        fail=sum(1 for s in samples if not s.get("success",False))/len(samples)
        return cyc*(1.0+fail)
    k=h.get("by_kind",{}).get(n["kind"],h["default"])
    return k["cycles"]*(1.0+k["failure_probability"])

def unlock_score(down,node):
    return 1.0+sum(1.0/(depth+1) for _,depth in descendants(down,node))

def cut_value(nodes,down,h,cut):
    return sum(cost_for(nodes[x],h)/unlock_score(down,x) for x in cut)

def attackable(g):
    nodes,_,_=indexes(g)
    return [nid for nid,n in nodes.items()
            if n.get("superseded_by") is None and open_class(g,nid)==ATTACKABLE]

def rank_singletons(g,h):
    nodes,_,down=indexes(g)
    return sorted(((cut_value(nodes,down,h,[nid]),nid) for nid in attackable(g)))

def replacement_path(g,start):
    nodes,_,down=indexes(g); path=[start]; seen={start}; cur=start
    while True:
        nxt=[e["to"] for e in g["edges"] if e["from"]==cur and e["relation"]=="REPLACES"]
        if not nxt: return path
        cur=nxt[0]
        if cur in seen or cur not in nodes: return []
        seen.add(cur); path.append(cur)

def main():
    if len(sys.argv)<3: raise SystemExit("usage: router.py graph.json cost_history.json")
    g,h=load(sys.argv[1]),load(sys.argv[2])
    for v,n in rank_singletons(g,h):
        print(f"{n}\tcut_value={v:.6f}\treplacement={replacement_path(g,n)}")

if __name__=="__main__": main()
