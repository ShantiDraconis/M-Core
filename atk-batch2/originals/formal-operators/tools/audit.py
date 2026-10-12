#!/usr/bin/env python3
"""Fail-closed external certificate generator. Never certifies conjectures on mere generic gates."""
import hashlib, json, pathlib, re, subprocess, sys, datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
files=sorted([*ROOT.glob('ATK/**/*.lean'),ROOT/'ATK.lean',ROOT/'lakefile.toml',ROOT/'lean-toolchain'])
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
forbidden=[]
for p in files:
    if p.suffix=='.lean':
        src=re.sub(r'/-.*?-/', '', p.read_text(), flags=re.S)
        src=re.sub(r'--[^\n]*','',src)
        for term in ('sorry','admit','axiom','unsafe'):
            if re.search(r'\b'+term+r'\b',src): forbidden.append([str(p.relative_to(ROOT)),term])
checks={}
for cmd,label in [(['lake','build'],'lake_build'),(['lake','env','lean','ATK.lean'],'root_elaboration')]:
    try:
        r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=240)
        checks[label]={'status':'PASS' if r.returncode==0 else 'FAIL','returncode':r.returncode,'log_tail':(r.stdout+'\n'+r.stderr)[-3000:]}
    except (FileNotFoundError,subprocess.TimeoutExpired) as e:
        checks[label]={'status':'NOT_RUN','reason':str(e)}
# Explicitly refuse conjecture certification until all seven independently audited semantic adapters and proofs exist.
manifest=json.loads((ROOT/'terminal_manifest.json').read_text())
terminal_ok=all(x['semantic_adapter']=='VERIFIED' and x['material_proof']=='VERIFIED' and x['bridge']=='VERIFIED' for x in manifest['lanes'])
build_ok=all(x['status']=='PASS' for x in checks.values())
cert={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashes,'forbidden_tokens':forbidden,'checks':checks,'lanes':manifest['lanes'],'terminal_certified':bool(build_ok and not forbidden and terminal_ok),'OPEN_MATH':not bool(build_ok and not forbidden and terminal_ok),'CLOSED_MATH':bool(build_ok and not forbidden and terminal_ok),'certificate_kind':'source-integrity-and-build-status; not an unconditional proof unless terminal_certified is true'}
out=ROOT/'certificates'/'EXTERNAL_AUDIT.json';out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'build':checks,'terminal_certified':cert['terminal_certified'],'forbidden':forbidden},indent=2))
sys.exit(0 if build_ok and not forbidden else 1)
