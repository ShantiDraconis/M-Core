# Uniform family at m=4q: a_q={1,1+q,1+2q,1+3q,2q+4,4q-8}; certificate a+{2,-2}+{4,-4} = S+Q,
# S={1,4,2q+1,2q+4,4q-8,4q-2} (quasi-decomposable), Q={2,q+1,3q+1,4q-4} (grade 2).
import math, itertools, sys
def U(m): return [t for t in range(1,m) if math.gcd(t,m)==1]
def grade(v,m,u):
    if any(x%m==0 for x in v) or sum(v)%m: return 0
    y=sum(v)//m
    return y if all(sum((t*x)%m for x in v)==y*m for t in u) else 0
def dec(v,m): return any((x+y)%m==0 for x,y in itertools.combinations(v,2))
def qdec(v,m,u):
    for T in itertools.combinations(range(6),3):
        s=sum(v[i] for i in T)%m
        if s and grade([v[i] for i in T]+[m-s],m,u)==2: return True
    return False
res=[]
for q in range(3,int(sys.argv[1])+1):
    m=4*q; u=U(m)
    a=[1,1+q,1+2*q,1+3*q,2*q+4,4*q-8]
    S=[1,4,2*q+1,2*q+4,4*q-8,4*q-2]; Q=[2,q+1,3*q+1,4*q-4]
    hodge=grade(a,m,u)==3
    resid=hodge and not dec(a,m) and not qdec(a,m,u)
    cert= sorted(a+[2,m-2,4,m-4])==sorted(S+Q) and grade(S,m,u)==3 and qdec(S,m,u) and not dec(S,m) and grade(Q,m,u)==2
    res.append((q,m,hodge,resid,cert))
print("q with a_q Hodge:", [q for q,m,h,r,c in res if h])
print("q with a_q residual (indec, not qdec):", [q for q,m,h,r,c in res if r])
print("q Hodge but certificate fails:", [q for q,m,h,r,c in res if h and not c])
