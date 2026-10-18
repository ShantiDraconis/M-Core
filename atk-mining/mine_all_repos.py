#!/usr/bin/env python3
"""Authenticated all-owned-repository, all-Git-ref evidence miner. Fail closed."""
import os,sys,json,urllib.request,subprocess,base64,pathlib,re,csv,hashlib
TOKEN=os.environ["ATK_READ_ALL_REPOS_TOKEN"]
SHARD=int(os.environ.get("ATK_SHARD","0")); TOTAL=int(os.environ.get("ATK_SHARDS","16"))
OUT=pathlib.Path("atk-mined"); OUT.mkdir(exist_ok=True)
HEADERS={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
def api(url):
 req=urllib.request.Request(url,headers=HEADERS)
 with urllib.request.urlopen(req,timeout=120) as f:return json.load(f)
repos=[];page=1
while True:
 batch=api("https://api.github.com/user/repos?affiliation=owner&per_page=100&page="+str(page))
 if not batch:break
 repos.extend(r for r in batch if r["owner"]["login"].lower()=="shantidraconis")
 page+=1
repos=sorted({r["full_name"]:r for r in repos}.values(),key=lambda x:x["full_name"].lower())
selected=[r for i,r in enumerate(repos) if i%TOTAL==SHARD]
patterns={
"RH":r"RiemannHypothesis|FiniteSpanApproximatesChi|DNLimit|UniformLogBound|ZeroResidue|BaezDuarte|zeta",
"PNP":r"SATNotInP|G21Pointwise|P01MachineConstruction|LowerBoundWitness|UniversalWitness|CookLevin|PneNP|complexity",
"NS":r"EnstrophyAPrioriBound|ActualNS|SignedGain|GlobalSmooth|cBulk|cTail|NavierStokes|enstrophy",
"YM":r"ConstructiveYM4D|B60ConcretePhysicalAdapter|MassGap|OSReconstruction|YangMills",
"BSD":r"BSDFull|RankResidual|RefinedOpen|TorsionPositive|QuotientIdentity|GrossZagier|elliptic",
"HODGE":r"ConcreteAlgebraicityPayload|HodgeCertificationBoundary|HigherCodimension|GradedRationalHodge|HodgeConjecture",
"BEAL":r"GCDLowerBound|BealConjecture|UniversalTripleGCD|ExclusaoResidualFinal|BealData"}
rx={k:re.compile(v,re.I) for k,v in patterns.items()}
decl=re.compile(r"^\s*(theorem|lemma|def|structure|class|axiom|constant|instance)\s+([^\s(:{]+)",re.M)
rows=[];errors=[];seen=set();refs_count=0;blobs_count=0
def git(*args):
 p=subprocess.run(["git",*args],capture_output=True,timeout=600)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors="replace")[:350])
 return p.stdout
auth=base64.b64encode(("x-access-token:"+TOKEN).encode()).decode()
for r in selected:
 name=r["full_name"];folder=pathlib.Path("mirrors")/(r["name"]+".git");folder.parent.mkdir(exist_ok=True)
 try:
  git("-c","http.https://github.com/.extraheader=AUTHORIZATION: basic "+auth,"clone","--mirror","https://github.com/"+name+".git",str(folder))
  refs=git("--git-dir",str(folder),"for-each-ref","--format=%(refname)","refs/heads").decode().splitlines()
  for ref in refs:
   refs_count+=1
   try:items=git("--git-dir",str(folder),"ls-tree","-r","-z",ref).split(b"\0")
   except Exception as e:errors.append([name,ref,str(e)]);continue
   for item in items:
    if b"\t" not in item:continue
    meta,path=item.split(b"\t",1);filename=path.decode(errors="replace")
    if not filename.endswith((".lean",".v",".agda",".thy",".py",".md",".json",".tex",".txt")):continue
    sha=meta.split()[-1].decode()
    key=(name,sha)
    if key in seen:continue
    seen.add(key);blobs_count+=1
    try:body=git("--git-dir",str(folder),"cat-file","blob",sha).decode(errors="replace")
    except Exception as e:errors.append([name,filename,str(e)]);continue
    lanes=[k for k,v in rx.items() if v.search(body)]
    if not lanes:continue
    unsafe=bool(re.search(r"\b(sorry|admit|sorryAx)\b",body))
    ds="; ".join(a+" "+b for a,b in decl.findall(body)[:70])
    for lane in lanes:rows.append([name,ref,filename,sha,lane,unsafe,ds,hashlib.sha256(body.encode()).hexdigest()])
 except Exception as e:errors.append([name,"clone_or_scan",str(e)])
 finally:
  if folder.exists():
   import shutil
   shutil.rmtree(folder,ignore_errors=True)
with (OUT/"ALL_MATCHES.csv").open("w",newline="") as f:
 w=csv.writer(f);w.writerow(["repo","ref","path","blob_sha","lane","unsafe_lexical","declarations","text_sha256"]);w.writerows(rows)
for lane in patterns:
 with (OUT/(lane+"_DENSE.md")).open("w") as f:
  f.write("# "+lane+" — mined source candidates (not proofs)\n\n")
  for row in rows:
   if row[4]==lane:f.write("- "+ " | ".join(str(x)[:400] for x in row[:7])+"\n")
summary={"owner_repositories_listed":len(repos),"shard":SHARD,"shards":TOTAL,"repos_assigned":len(selected),"repos": [r["full_name"] for r in selected],"refs_scanned":refs_count,"unique_blobs":blobs_count,"matches":len(rows),"errors":errors,"closed_math":False,"kernel_run":False}
(OUT/"SUMMARY.json").write_text(json.dumps(summary,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k not in ("repos","errors")},indent=2))
if errors:sys.exit(2)
