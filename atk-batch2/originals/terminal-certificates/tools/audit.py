import json, pathlib, re, shutil, subprocess, hashlib
root=pathlib.Path(__file__).resolve().parents[1]
files=sorted(root.rglob('*.lean'))
forbidden=['sorry','admit','axiom','unsafe']
found={str(p.relative_to(root)):[t for t in forbidden if re.search(r'\b'+t+r'\b',p.read_text())] for p in files}
clean=all(not x for x in found.values())
lake=shutil.which('lake')
status='NOT_RUN'
if lake:
    r=subprocess.run([lake,'build'],cwd=root,capture_output=True,text=True)
    status='PASS' if r.returncode==0 else 'FAIL'
    (root/'build_output.log').write_text(r.stdout+'\n'+r.stderr)
report={'text_scan': 'PASS' if clean else 'FAIL','files':found,'kernel':status,
        'original_semantics_integrated':False,'universal_witnesses_supplied':0,
        'terminal_certified':0,'OPEN_MATH':True,'CLOSED_MATH':False,
        'sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(root/'AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
