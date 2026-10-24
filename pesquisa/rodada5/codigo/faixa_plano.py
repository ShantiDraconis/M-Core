import math, sys, json
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import zeroclasses as zc
from fractions import Fraction as F
BT={0:F(1),1:F(-1,2),2:F(1,6),4:F(-1,30),6:F(1,42),8:F(-1,30),10:F(5,66)}
bt=lambda j: BT.get(j,F(0))
def pochRQ(R,k):
    p=F(1)
    for i in range(k): p*=R+i
    return p
def CbR(M): return sum(abs(bt(i))*math.comb(M,i) for i in range(M+1))
def cotaQ(N,M,R,d):
    s=F(N)+F(N)/d+F(1,2)
    s+=sum(abs(bt(j))/math.factorial(j)*pochRQ(R,j-1)/F(N)**(j-1) for j in range(2,M+1))
    s+=pochRQ(R,M)/math.factorial(M)*(CbR(M)/F(N)**(M-1)/(M-1))
    return s
r=F(2,5); DELTA=F(1,50); MARG=0.012
_c={}
def za(s,t):
    k=(s,t)
    if k not in _c: _c[k]=abs(zc.zeta(complex(float(s),float(t))))
    return _c[k]
def ceilq(x,den): return F(math.ceil(x*den),den)
def leaf(s0,s1,a,b):
    R2=(s1+r)**2+(b+r)**2
    R=ceilq(math.sqrt(R2),1000)
    while R*R<R2: R+=F(1,1000)
    d=a-r
    c,Nc,Mc=min((cotaQ(N,M,R,d),N,M) for N in range(1,12) for M in (6,8,10))
    B=ceilq(float(c),100)
    if B<c: B+=F(1,100)
    best=None
    for ns in range(1,41):
        hs=(s1-s0)/(2*ns)
        for nt in range(1,400):
            if best and ns*nt>=best[0]: break
            ht=(b-a)/(2*nt)
            h=ceilq(math.sqrt(hs*hs+ht*ht),100000)
            while h*h<hs*hs+ht*ht: h+=F(1,100000)
            v=B/r*h+DELTA
            ok=all(za(s0+hs*(2*i+1),a+ht*(2*j+1))-MARG>=float(v) for i in range(ns) for j in range(nt))
            if ok:
                best=(ns*nt,ns,nt,hs,ht,h,v); break
    if best is None: return None
    Ne=6 if b<=5 else (8 if b<=9 else 10)
    return dict(s0=s0,s1=s1,a=a,b=b,R=R,d=d,Nc=Nc,Mc=Mc,B=B,ns=best[1],nt=best[2],hs=best[3],ht=best[4],h=best[5],v=best[6],Ne=Ne,n=best[0])
def plano(s0,s1,a,b,depth=0):
    L=leaf(s0,s1,a,b)
    cost=L['n'] if L else 10**9
    tree=('leaf',L)
    if depth<6 and cost>24:
        sm=(s0+s1)/2; tm=(a+b)/2
        for kind,parts,mid in (('re',[(s0,sm,a,b),(sm,s1,a,b)],sm),('im',[(s0,s1,a,tm),(s0,s1,tm,b)],tm)):
            sub=[plano(*p,depth=depth+1) for p in parts]
            tot=sub[0][0]+sub[1][0]
            if tot<cost: cost=tot; tree=(kind,mid,sub[0][1],sub[1][1])
    return cost,tree
T0=F(sys.argv[1]) if len(sys.argv)>1 else F(13)
cuts=[F(43,50)]+[F(k) for k in range(2,int(T0)+1)]
strips=[]
tot=0
for a,b in zip(cuts[:-1],cuts[1:]):
    c,t=plano(F(1,2),F(1),a,b)
    strips.append((a,b,t)); tot+=c
    print(f"[{a},{b}] centros={c}",file=sys.stderr)
print("total",tot,file=sys.stderr)
def ser(t):
    if t[0]=='leaf':
        L=t[1]; return {'leaf':{k:(str(v) if isinstance(v,F) else v) for k,v in L.items()}}
    return {t[0]:str(t[1]),'l':ser(t[2]),'r':ser(t[3])}
json.dump([{'a':str(a),'b':str(b),'tree':ser(t)} for a,b,t in strips],open(sys.argv[2],'w'),indent=0)
