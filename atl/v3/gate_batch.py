#!/usr/bin/env python3
import hashlib, json, pathlib, subprocess, sys

CLASSES=[("TYPE",("type mismatch","application type mismatch")),
         ("AXIOM",("sorryAx","declaration uses 'sorry'","declaration uses sorry")),
         ("SEMANTIC",("statement hash","semantic")),
         ("OPEN_MATH",("OPEN_MATH",)),
         ("BUILD",("unknown identifier","unknown constant","error:"))]

def classify(text):
    for cls,needles in CLASSES:
        if any(x in text for x in needles): return cls
    return "BUILD"

def digest(files):
    h=hashlib.sha256()
    for f in sorted(files):
        h.update(f.encode()); h.update(pathlib.Path(f).read_bytes())
    return h.hexdigest()

def run_one(f):
    p=subprocess.run(["lake","env","lean",f],text=True,capture_output=True)
    if p.returncode==0:return None
    text=(p.stdout+"\n"+p.stderr)
    return {"file":f,"class":classify(text),"detail":text.splitlines()[:12]}

def canonical(errors,upstream):
    if not errors:return []
    by_file={e["file"]:e for e in errors}
    candidates=list(errors)
    blocked=set()
    for a in errors:
        for b in errors:
            if a is b: continue
            if a["file"] in upstream.get(b["file"],[]): blocked.add(b["file"])
    return [e for e in candidates if e["file"] not in blocked]

def main():
    if len(sys.argv)<3: raise SystemExit("usage: gate_batch.py GATE file...")
    gate,files=sys.argv[1],sys.argv[2:]
    errs=[e for f in files if (e:=run_one(f))]
    result={"gate":gate,"sha":digest(files),"green":not errs,
            "independent_errors":errs,"canonical_ties":canonical(errs,{})}
    print(json.dumps(result,indent=2))
    raise SystemExit(1 if errs else 0)
if __name__=="__main__": main()
