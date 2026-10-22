# Second independent implementation in Shioda's x-vector language (pure Python), literal definitions.
# M_m(1) is computed by brute force (not assumed to be pairs).
import sys, math, itertools
from functools import lru_cache
def run(m):
    U=[t for t in range(1,m) if math.gcd(t,m)==1]
    def inM(x):  # x: tuple of counts indexed 1..m-1 (x[0] unused)
        s=sum(i*x[i] for i in range(1,m))
        if s==0 or s%m: return 0
        y=s//m
        for t in U:
            if sum(((t*i)%m)*x[i] for i in range(1,m))!=y*m: return 0
        return y
    def parts(total,maxpart,k=None):
        # multisets of parts in [1, maxpart] summing to total (exactly k parts if k given)
        if total==0:
            if k in (None,0): yield []
            return
        if k==0: return
        for p in range(min(total,maxpart),0,-1):
            if k is not None and p*k<total: break
            for rest in parts(total-p,p,None if k is None else k-1): yield [p]+rest
    def vec(ms):
        x=[0]*m
        for v in ms: x[v]+=1
        return tuple(x)
    # M_m(1) literally
    M1=[vec(p) for p in parts(m,m-1) if inM(vec(p))==1] if m<=64 else [vec([b,m-b]) for b in range(1,m//2+1)]  # m>64: pairs (parity argument)
    assert all(sum(x)==2 for x in M1), "M_m(1) has non-pair element!"
    # M_m(3) via multisets of 1..m-1 summing (t=1) to 3m
    M3=[vec(p) for p in parts(3*m,m-1,6) if inM(vec(p))==3]
    def subvecs(x):
        rng=[range(c+1) for c in x]
        for c in itertools.product(*rng): yield c
    def dec(x):
        for c in subvecs(x):
            d=tuple(xi-ci for xi,ci in zip(x,c))
            if any(c) and any(d) and inM(c) and inM(d): return True
        return False
    def qdec(x):
        for b in M1:
            ab=tuple(p+q for p,q in zip(x,b))
            for c in subvecs(ab):
                d=tuple(p-q for p,q in zip(ab,c))
                if not any(c) or not any(d): continue
                if c==x or d==x: continue
                if inM(c) and inM(d): return True
        return False
    def act(x,t):
        y=[0]*m
        for i in range(1,m): y[(t*i)%m]+=x[i]
        return tuple(y)
    seen=set(); orb=nd=nq=nr=0
    for x in M3:
        if x in seen: continue
        O={act(x,t) for t in U}; seen|=O; orb+=1
        if dec(x): nd+=1
        elif qdec(x): nq+=1
        else: nr+=1
    dim=sum(math.factorial(6)//math.prod(math.factorial(c) for c in x) for x in M3)
    return dim,orb,nd,nq,nr
for m in map(int,sys.argv[1:]):
    print("m=%d dimB=%d orbits=%d dec=%d qdec=%d R=%d"%((m,)+run(m)),flush=True)
