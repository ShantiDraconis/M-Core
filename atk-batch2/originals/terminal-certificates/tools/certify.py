#!/usr/bin/env python3
"""Fail-closed terminal certification. Never issues terminal success on syntax scan alone."""
import pathlib, json, hashlib, shutil, subprocess, re, datetime, sys
root=pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((root/'terminal_manifest.json').read_text())
files=sorted(root.rglob('*.lean'))
violations=[]
for p in files:
    content=p.read_text()
    for marker in ('sorry','admit','axiom','unsafe'):
        if re.search(r'\b'+marker+r'\b',content):
            # Conservative: also flags occurrences in comments.
            violations.append({'file':str(p.relative_to(root)),'marker':marker})
source_hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
lake=shutil.which('lake')
result={'schema':'atk-terminal-audit/v1','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':source_hashes,'marker_violations':violations,'lake_present':bool(lake),'build':'NOT_RUN','axiom_audit':'NOT_RUN','original_imports_complete':False,'terminal_certified':0,'open_math':True,'closed_math':False}
if lake and not violations:
    try:
        p=subprocess.run([lake,'build'],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=900)
        (root/'evidence/build.log').write_text(p.stdout)
        result['build']='PASS' if p.returncode==0 else 'FAIL'
    except Exception as exc:
        result['build']='ERROR:'+str(exc)
# Never promote based on compilation of conditional interfaces.
(root/'certificates/EXTERNAL_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['marker_violations','lake_present','build','terminal_certified','open_math','closed_math']},indent=2))
sys.exit(0 if not violations else 1)
