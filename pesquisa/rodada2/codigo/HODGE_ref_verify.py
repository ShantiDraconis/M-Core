# Independent re-verification (pure Python) of every certificate printed by HODGE_ref_closure.
import re, sys, math, itertools
from collections import Counter
def units(M): return [t for t in range(1,M) if math.gcd(t,M)==1]
def grade(v,M,U):
    if any(x%M==0 for x in v) or sum(v)%M: return 0
    y=sum(v)//M
    return y if all(sum((t*x)%M for x in v)==y*M for t in U) else 0
def is_std(v,M,p):
    if len(v)!=p+1 or M%p: return False
    k=M//p
    return any(sorted([i+j*k for j in range(p)]+[(-p*i)%M])==sorted(v) for i in range(1,k) if (p*i)%M)
def qdec6(v,M,U):
    for T in itertools.combinations(range(6),3):
        s=sum(v[i] for i in T)%M
        if s and grade([v[i] for i in T]+[M-s],M,U)==2 and grade([v[i] for i in range(6) if i not in T]+[s],M,U)==2: return True
    return False
def tsplit(v,M): return any(sum(v[i] for i in T)%M==0 for T in itertools.combinations(range(6),3))
ok=bad=0
for fn in sys.argv[1:]:
    for line in open(fn):
        if 'blocks:' not in line: continue
        M=int(re.search(r'level (\d+)',line).group(1)); U=units(M)
        a=list(map(int,re.search(r"a'=\(([\d,]+)\)",line).group(1).split(',')))
        pairs=[tuple(map(int,p.split(','))) for p in re.findall(r'\{(\d+,\d+)\}',line)]
        blocks=[(t,list(map(int,b.split(',')))) for t,b in re.findall(r'(\w+)\(([\d,]+)\)',line.split('blocks:')[1])]
        lhs=Counter(a); [lhs.update(p) for p in pairs]
        rhs=Counter(); [rhs.update(b) for _,b in blocks]
        good = lhs==rhs and grade(a,M,U)==3 and all((p[0]+p[1])%M==0 for p in pairs)
        for t,b in blocks:
            g=grade(b,M,U)
            if t=='pair': good&= len(b)==2 and (b[0]+b[1])%M==0
            elif t=='quad': good&= len(b)==4 and g==2
            elif t=='std5': good&= g==3 and is_std(b,M,5)
            elif t=='std7': good&= g==4 and is_std(b,M,7)
            elif t=='qdec6': good&= g==3 and qdec6(b,M,U) and not any((x+y)%M==0 for x,y in itertools.combinations(b,2))
            elif t=='tsplit': good&= g==3 and tsplit(b,M)
            elif t=='dec6': good&= g==3
            else: good=False
        # nontriviality: a itself must not be one of the blocks
        good &= all(sorted(b)!=sorted(a) for _,b in blocks)
        ok+=good; bad+=(not good)
        if not good: print("FAILED:",line.strip())
print("certificates verified:",ok,"failed:",bad)
