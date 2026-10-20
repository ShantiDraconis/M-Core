from __future__ import annotations
import math
from .constants import DELTA_TEST_VALUES, LAM_TEST_VALUES, PHI_SAMPLES, PHI_REFERENCE
from .dag import has_cycle_G1_G4, downstream_of_G1_only


def audit_A1(I, deltas=DELTA_TEST_VALUES):
    b=I.base()
    if b <= 0: return {"pass": False, "reason": "A1 obstruction needs positive witness I(u0)>0"}
    checks=[]
    for d in deltas:
        if not (0 < d < 1): raise ValueError("test delta must lie in (0,1)")
        threshold=(1-d)/b
        A=threshold + 1.0
        value=I.amplitude(A)
        checks.append((d,A,value,value>1-d))
    return {"pass": all(x[3] for x in checks), "checks": checks,
            "status": "numerical witnesses for the analytic A1 theorem"}


def audit_A2(I):
    e=list(I.dag_edges()); cyc=has_cycle_G1_G4(e); gate=downstream_of_G1_only(e)
    return {"pass": cyc and not gate, "cycle": cyc, "downstream_ok": gate, "edges": e}


def _ratio(g,h):
    if h == 0: return math.nan
    return g/h


def audit_A3(I, sample_sizes=(10,100,1000,10000), tol=1e-3):
    paths=list(I.zero_paths())
    if len(paths)<2: return {"pass":False,"reason":"need >=2 explicit paths of the same G/H"}
    limits=[]; details=[]
    for p in paths:
        seq=[]; gh_to_zero=True
        for n in sample_sizes:
            g,h=p.samples(n); gh_to_zero &= abs(g) <= 1/n + tol and abs(h) <= 1/n + tol
            seq.append(_ratio(g,h))
        if any(math.isnan(x) for x in seq): return {"pass":False,"reason":f"denominator hit zero on path {p.name}"}
        L=seq[-1]; limits.append(L); details.append((p.name,seq,gh_to_zero))
    separated=max(limits)-min(limits)>tol
    return {"pass": separated and all(x[2] for x in details), "paths":details,
            "limits":limits,"path_dependent":separated,
            "status":"finite-sample witness; analytic path limits remain Lean/proof obligations"}


def audit_A4(I, lambdas=LAM_TEST_VALUES, tol=1e-9):
    b=I.base(); checks=[(l,I.scale(l),abs(I.scale(l)-b)<tol) for l in lambdas]
    return {"pass":all(x[2] for x in checks),"checks":checks,
            "phi_samples":PHI_SAMPLES,"phi_reference":PHI_REFERENCE,
            "tau_rigid":None,"eps0_rigid":None,
            "status":"scale invariance tested; Phi/eps0/tau rigidity deliberately NOT inferred"}
